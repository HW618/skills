#!/usr/bin/env python3
"""更新阿里云产品索引缓存。

用法:
    python update_index.py --init              # 初始化：导航页 + 核心产品
    python update_index.py                      # 仅更新导航页
    python update_index.py --product ecs        # 更新指定产品
    python update_index.py --all                # 更新所有已注册产品
    python update_index.py --add ecs            # 添加并更新产品

缓存结构:
    cache/_index/navigation.md      导航页
    cache/_index/meta.json          导航页元数据
    cache/<product>/llms.md         产品主页
    cache/<product>/meta.json       产品元数据
    cache/<product>/pages/*.md      高价值子页
    cache/_registry.json            全局注册表
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# skill 根目录（脚本在 scripts/ 下，父目录即根）
SKILL_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = SKILL_ROOT / "cache"
INDEX_DIR = CACHE_DIR / "_index"
REGISTRY_PATH = CACHE_DIR / "_registry.json"

NAVIGATION_URL = "https://help.aliyun.com/zh/llms.txt"
PRODUCT_URL_TEMPLATE = "https://help.aliyun.com/zh/{product}/llms.txt"

# 核心产品初始集合
CORE_PRODUCTS = [
    "ecs",
    "simple-application-server",
    "ebm",
    "nas",
    "oss",
    "vpc",
    "eip",
    "slb",
    "cdn",
    "rds",
    "polardb",
    "redis",
]

# 高价值子页关键词（标题或摘要含这些词则缓存）
HIGH_VALUE_KEYWORDS = [
    "规格", "实例", "instance", "family", "规格族",
    "性能", "performance", "基准", "突发", "IOPS", "吞吐",
    "计费", "价格", "收费", "billing", "pricing", "按量", "包年包月", "抢占",
    "限制", "配额", "limit", "quota",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch(url: str) -> str:
    """调用 fetch_page.py 抓取，返回内容。失败则抛异常。"""
    result = subprocess.run(
        [sys.executable, str(SKILL_ROOT / "scripts" / "fetch_page.py"), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"抓取失败 {url}: {result.stderr}")
    return result.stdout


def slugify(url: str) -> str:
    """从 .md URL 生成文件 slug。"""
    # https://help.aliyun.com/zh/ecs/user-guide/overview-52.md -> overview-52
    slug = url.rsplit("/", 1)[-1]
    slug = re.sub(r"\.md$", "", slug)
    slug = re.sub(r"[^a-zA-Z0-9\-]", "-", slug)
    return slug[:80]


def load_registry() -> dict:
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {"products": {}}


def save_registry(reg: dict):
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.write_text(
        json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def update_navigation() -> bool:
    """更新导航页。"""
    print("📡 抓取导航页...", file=sys.stderr)
    try:
        content = fetch(NAVIGATION_URL)
    except RuntimeError as e:
        print(f"❌ {e}", file=sys.stderr)
        return False

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    (INDEX_DIR / "navigation.md").write_text(content, encoding="utf-8")
    meta = {"url": NAVIGATION_URL, "updated_at": now_iso(), "size": len(content)}
    (INDEX_DIR / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"✅ 导航页已更新（{len(content)} 字节）", file=sys.stderr)
    return True


def parse_product_links(navigation_md: str) -> dict:
    """从导航页解析产品链接。返回 {product_key: url}。"""
    links = {}
    # 匹配 [产品名](https://help.aliyun.com/zh/<key>/llms.txt)
    pattern = re.compile(
        r"\[([^\]]+)\]\((https://help\.aliyun\.com/zh/[^/]+(?:/[^/]+)*?/llms\.txt)\)"
    )
    for match in pattern.finditer(navigation_md):
        name, url = match.group(1), match.group(2)
        # 提取 product key：/zh/<key>/llms.txt 或 /zh/<key>/.../llms.txt
        path_match = re.search(r"/zh/(.+?)/llms\.txt", url)
        if path_match:
            key = path_match.group(1)
            links[key] = {"name": name, "url": url}
    return links


def is_high_value(title: str, summary: str) -> bool:
    """判断条目是否为高价值子页。"""
    text = (title + " " + summary).lower()
    for kw in HIGH_VALUE_KEYWORDS:
        if kw.lower() in text:
            return True
    return False


def parse_product_pages(product_md: str) -> list:
    """从产品主页解析子页链接。返回 [{title, url, summary, high_value}]。"""
    pages = []
    # 匹配 - [标题](url): 摘要  或  - [标题](url)
    pattern = re.compile(r"^- \[([^\]]+)\]\(([^)]+\.md)\)(?::\s*(.+))?$", re.MULTILINE)
    for match in pattern.finditer(product_md):
        title, url, summary = match.group(1), match.group(2), match.group(3) or ""
        pages.append(
            {
                "title": title,
                "url": url,
                "summary": summary.strip(),
                "high_value": is_high_value(title, summary),
            }
        )
    return pages


def update_product(product_key: str, fetch_subpages: bool = True) -> bool:
    """更新单个产品。"""
    # 先从注册表或导航页找 URL
    reg = load_registry()
    url = None
    if product_key in reg["products"]:
        url = reg["products"][product_key].get("url")
    if not url:
        # 从导航页找
        nav_path = INDEX_DIR / "navigation.md"
        if not nav_path.exists():
            print("❌ 导航页不存在，请先运行 --init 或无参数更新导航页", file=sys.stderr)
            return False
        nav_links = parse_product_links(nav_path.read_text(encoding="utf-8"))
        if product_key not in nav_links:
            print(f"❌ 导航页中未找到产品 '{product_key}'", file=sys.stderr)
            return False
        url = nav_links[product_key]["url"]

    print(f"📡 抓取产品 {product_key}...", file=sys.stderr)
    try:
        content = fetch(url)
    except RuntimeError as e:
        print(f"❌ {e}", file=sys.stderr)
        return False

    product_dir = CACHE_DIR / product_key
    product_dir.mkdir(parents=True, exist_ok=True)
    (product_dir / "llms.md").write_text(content, encoding="utf-8")

    # 解析并抓取高价值子页
    pages = parse_product_pages(content)
    high_value_pages = [p for p in pages if p["high_value"]]
    cached_pages = []
    pages_dir = product_dir / "pages"
    pages_dir.mkdir(exist_ok=True)

    if fetch_subpages:
        for p in high_value_pages:
            slug = slugify(p["url"])
            print(f"  📄 抓取子页: {p['title'][:40]}", file=sys.stderr)
            try:
                page_content = fetch(p["url"])
                (pages_dir / f"{slug}.md").write_text(page_content, encoding="utf-8")
                cached_pages.append(
                    {"slug": slug, "title": p["title"], "url": p["url"]}
                )
            except RuntimeError as e:
                print(f"  ⚠️ 子页抓取失败: {e}", file=sys.stderr)

    # 更新产品元数据
    meta = {
        "product_key": product_key,
        "url": url,
        "updated_at": now_iso(),
        "llms_size": len(content),
        "total_pages_found": len(pages),
        "high_value_pages_found": len(high_value_pages),
        "cached_pages": cached_pages,
    }
    (product_dir / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # 更新注册表
    reg["products"][product_key] = {
        "url": url,
        "updated_at": now_iso(),
        "cached_pages_count": len(cached_pages),
    }
    save_registry(reg)

    print(
        f"✅ {product_key} 已更新（主页 {len(content)} 字节，子页 {len(cached_pages)}/{len(high_value_pages)}）",
        file=sys.stderr,
    )
    return True


def cmd_init():
    """初始化：导航页 + 核心产品。"""
    print("🚀 初始化缓存...", file=sys.stderr)
    if not update_navigation():
        return False
    for product in CORE_PRODUCTS:
        update_product(product)
    print("🎉 初始化完成", file=sys.stderr)
    return True


def cmd_add(product_key: str):
    """添加并更新产品。"""
    if not (INDEX_DIR / "navigation.md").exists():
        print("导航页不存在，先更新导航页", file=sys.stderr)
        update_navigation()
    return update_product(product_key)


def cmd_all():
    """更新所有已注册产品。"""
    reg = load_registry()
    if not reg["products"]:
        print("❌ 无已注册产品，请先 --init", file=sys.stderr)
        return False
    for product in reg["products"]:
        update_product(product)
    return True


def main():
    parser = argparse.ArgumentParser(description="更新阿里云产品索引缓存")
    parser.add_argument("--init", action="store_true", help="初始化导航页+核心产品")
    parser.add_argument("--product", help="更新指定产品")
    parser.add_argument("--all", action="store_true", help="更新所有已注册产品")
    parser.add_argument("--add", help="添加并更新产品")
    parser.add_argument(
        "--no-subpages", action="store_true", help="不抓取高价值子页（仅主页）"
    )
    args = parser.parse_args()

    if args.init:
        sys.exit(0 if cmd_init() else 1)
    if args.add:
        sys.exit(0 if cmd_add(args.add) else 1)
    if args.all:
        sys.exit(0 if cmd_all() else 1)
    if args.product:
        sys.exit(0 if update_product(args.product, fetch_subpages=not args.no_subpages) else 1)
    # 默认：更新导航页
    sys.exit(0 if update_navigation() else 1)


if __name__ == "__main__":
    main()
