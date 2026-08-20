#!/usr/bin/env python3
"""查询阿里云产品缓存：检索相关条目，支持缺失时联网回源。

用法:
    python query.py --product ecs --keywords "规格,计费"
    python query.py --product ecs --question "ECS 有哪些实例规格族"
    python query.py --product ecs --fetch-missing <url>  # 联网补取单个子页

输出 JSON，包含匹配的缓存条目和子页内容片段。
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import jieba
    # 加入阿里云领域常用词，避免被拆分
    for w in ["规格族", "实例规格", "云服务器", "云盘", "块存储", "文件存储", "对象存储", "专有网络", "负载均衡", "云数据库", "按量付费", "包年包月", "抢占式", "节省计划", "预留实例", "存储容量", "性能等级", "预配容量"]:
        jieba.add_word(w)
    _HAS_JIEBA = True
except ImportError:
    _HAS_JIEBA = False

SKILL_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = SKILL_ROOT / "cache"


def load_product_llms(product: str) -> str | None:
    """读取产品主页缓存。"""
    path = CACHE_DIR / product / "llms.md"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def load_product_meta(product: str) -> dict | None:
    path = CACHE_DIR / product / "meta.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def parse_entries(llms_md: str) -> list:
    """解析产品主页的条目。返回 [{title, url, summary}]。"""
    entries = []
    pattern = re.compile(r"^- \[([^\]]+)\]\(([^)]+)\)(?::\s*(.+))?$", re.MULTILINE)
    for match in pattern.finditer(llms_md):
        title, url, summary = match.group(1), match.group(2), match.group(3) or ""
        entries.append({"title": title, "url": url, "summary": summary.strip()})
    return entries


def extract_keywords(question: str) -> list:
    """从自然语言问题提取关键词。用 jieba 分词（若可用），否则退化为正则。"""
    stop = {"的", "了", "是", "在", "有", "和", "与", "及", "或", "等", "都", "也", "不", "没", "什么", "怎么", "怎样", "如何", "哪些", "哪个", "吗", "呢", "吧", "啊", "请", "帮", "我", "你", "他", "介绍", "一下", "告诉", "知道", "问", "查询", "查", "看", "看看", "了解", "阿里云", "云"}
    if _HAS_JIEBA:
        tokens = jieba.lcut(question)
    else:
        tokens = re.findall(r"[\u4e00-\u9fa5]+|[a-zA-Z]+", question)
    keywords = [w for w in tokens if w not in stop and len(w) >= 2]
    return keywords


def score_entry(entry: dict, keywords: list) -> int:
    """根据关键词给条目打分。标题命中权重高，长词权重高。"""
    title = entry["title"].lower()
    summary = entry["summary"].lower()
    score = 0
    for kw in keywords:
        kw_lower = kw.lower()
        weight = len(kw)  # 长词权重高
        if kw_lower in title:
            score += 3 * weight
        elif kw_lower in summary:
            score += 1 * weight
    return score


def search_entries(entries: list, keywords: list, top_n: int = 10) -> list:
    """搜索条目，返回按分数排序的 top N。"""
    scored = [(score_entry(e, keywords), e) for e in entries]
    scored = [(s, e) for s, e in scored if s > 0]
    scored.sort(key=lambda x: -x[0])
    return [e for _, e in scored[:top_n]]


def load_cached_page(product: str, slug: str) -> str | None:
    """读取缓存的子页。"""
    path = CACHE_DIR / product / "pages" / f"{slug}.md"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def find_page_for_url(product: str, url: str) -> str | None:
    """根据 URL 找到已缓存的子页内容。"""
    meta = load_product_meta(product)
    if not meta:
        return None
    for page in meta.get("cached_pages", []):
        if page["url"] == url:
            return load_cached_page(product, page["slug"])
    return None


def fetch_missing(url: str, product: str, slug: str) -> str | None:
    """联网抓取缺失子页并写入缓存。"""
    result = subprocess.run(
        [sys.executable, str(SKILL_ROOT / "scripts" / "fetch_page.py"), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    content = result.stdout
    pages_dir = CACHE_DIR / product / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    (pages_dir / f"{slug}.md").write_text(content, encoding="utf-8")
    return content


def main():
    parser = argparse.ArgumentParser(description="查询阿里云产品缓存")
    parser.add_argument("--product", required=True, help="产品 key")
    parser.add_argument("--keywords", help="逗号分隔的关键词")
    parser.add_argument("--question", help="自然语言问题（自动提取关键词）")
    parser.add_argument("--fetch-missing", help="联网抓取指定 URL 的子页")
    parser.add_argument("--top", type=int, default=10, help="返回条目数")
    args = parser.parse_args()

    if args.fetch_missing:
        slug = re.sub(r"[^a-zA-Z0-9\-]", "-", args.fetch_missing.rsplit("/", 1)[-1].replace(".md", ""))[:80]
        content = fetch_missing(args.fetch_missing, args.product, slug)
        if content:
            print(json.dumps({"status": "ok", "slug": slug, "size": len(content)}, ensure_ascii=False))
        else:
            print(json.dumps({"status": "error"}, ensure_ascii=False))
        return

    llms_md = load_product_llms(args.product)
    if not llms_md:
        print(
            json.dumps(
                {"status": "not_cached", "message": f"产品 {args.product} 未缓存，请先运行 update_index.py --product {args.product}"},
                ensure_ascii=False,
            )
        )
        return

    # 提取关键词
    if args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",")]
    elif args.question:
        keywords = extract_keywords(args.question)
    else:
        print(json.dumps({"status": "error", "message": "需提供 --keywords 或 --question"}, ensure_ascii=False))
        return

    entries = parse_entries(llms_md)
    matched = search_entries(entries, keywords, args.top)

    # 尝试加载匹配条目对应的缓存子页
    results = []
    for entry in matched:
        page_content = find_page_for_url(args.product, entry["url"])
        results.append(
            {
                "title": entry["title"],
                "url": entry["url"],
                "summary": entry["summary"],
                "cached_page": page_content is not None,
                "page_snippet": (page_content[:500] + "...") if page_content and len(page_content) > 500 else page_content,
            }
        )

    meta = load_product_meta(args.product)
    print(
        json.dumps(
            {
                "status": "ok",
                "product": args.product,
                "updated_at": meta.get("updated_at") if meta else None,
                "total_entries": len(entries),
                "matched": results,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
