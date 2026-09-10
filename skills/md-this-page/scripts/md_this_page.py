#!/usr/bin/env python3
"""
MD This Page Skill — CLI 入口

用法：
    export CDP_URL=http://127.0.0.1:9222        # 可选；未设置或连不上则回退本地 headless

    python scripts/md_this_page.py convert <url> [--timeout 45] [--verbose] [--no-metadata] [--no-images] [--no-links] [-o out.md]
    python scripts/md_this_page.py extract <url> [--timeout 45] [--verbose] [--max-length 3000] [-o out.md]
    python scripts/md_this_page.py sites        # 列出支持的站点策略
"""

import argparse
import asyncio
import os
import sys

# 保证可直接以脚本方式运行（无需 pip install）
_SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _SKILL_DIR)

from src.crawler import crawl_page                              # noqa: E402
from src.converter import convert_to_markdown, extract_summary  # noqa: E402
from src.strategies import SITE_STRATEGIES                      # noqa: E402


def _validate(url: str) -> str | None:
    if not url.startswith(("http://", "https://")):
        return f"❌ 无效的 URL: {url}\n请提供以 http:// 或 https:// 开头的完整 URL。"
    return None


def _emit(text: str, output: str | None) -> None:
    """打印到 stdout，或写入文件"""
    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"✅ 已保存到 {output}")
    else:
        print(text)


async def cmd_convert(args) -> int:
    if err := _validate(args.url):
        print(err)
        return 2
    result = await crawl_page(args.url, timeout_ms=args.timeout * 1000, verbose=args.verbose)
    if not result.success:
        print(f"❌ 抓取失败: {args.url}\n{result.error}", file=sys.stderr)
        return 1
    _emit(convert_to_markdown(
        result,
        include_metadata=not args.no_metadata,
        include_images=not args.no_images,
        include_links=not args.no_links,
        max_chars=args.max_chars,
    ), args.output)
    return 0


async def cmd_extract(args) -> int:
    if err := _validate(args.url):
        print(err)
        return 2
    result = await crawl_page(args.url, timeout_ms=args.timeout * 1000, verbose=args.verbose)
    if not result.success:
        print(f"❌ 抓取失败: {args.url}\n{result.error}", file=sys.stderr)
        return 1
    _emit(extract_summary(result, max_length=args.max_length), args.output)
    return 0


def cmd_sites(_) -> int:
    print(f"支持的站点策略（共 {len(SITE_STRATEGIES) + 1} 种，含普通网页兜底）：\n")
    print(f"  {'网站':<14} {'域名':<28} 策略要点")
    for s in SITE_STRATEGIES:
        focus = "正文定位" + ("+渲染等待" if s.wait_for else "") + \
                ("+JS修正" if s.js_snippets else "")
        print(f"  {s.name:<14} {s.domains[0]:<28} {focus}")
    print(f"  {'普通网页':<14} {'（其他所有网站）':<26} crawl4ai 通用提取")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="md_this_page",
        description="将网页转换为干净的 Markdown（基于 crawl4ai + CDP 浏览器）",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_conv = sub.add_parser("convert", help="网页 → Markdown")
    p_conv.add_argument("url")
    p_conv.add_argument("--timeout", type=int, default=45, help="页面超时秒数（默认 45）")
    p_conv.add_argument("--verbose", action="store_true", help="输出 crawl4ai 详细日志（调试用）")
    p_conv.add_argument("--max-chars", type=int, default=50000,
                        help="输出最大字符数，超出则截断；0 表示不限制（默认 50000）")
    p_conv.add_argument("--no-metadata", action="store_true", help="不含 YAML 元数据头")
    p_conv.add_argument("--no-images", action="store_true", help="移除图片")
    p_conv.add_argument("--no-links", action="store_true", help="移除链接（保留文本）")
    p_conv.add_argument("-o", "--output", help="保存到文件（默认打印到 stdout）")
    p_conv.set_defaults(func=cmd_convert)

    p_ext = sub.add_parser("extract", help="提取主要内容摘要")
    p_ext.add_argument("url")
    p_ext.add_argument("--timeout", type=int, default=45, help="页面超时秒数（默认 45）")
    p_ext.add_argument("--verbose", action="store_true", help="输出 crawl4ai 详细日志（调试用）")
    p_ext.add_argument("--max-length", type=int, default=3000, help="摘要最大字符数")
    p_ext.add_argument("-o", "--output", help="保存到文件（默认打印到 stdout）")
    p_ext.set_defaults(func=cmd_extract)

    p_sites = sub.add_parser("sites", help="列出支持的站点策略")
    p_sites.set_defaults(func=cmd_sites)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if asyncio.iscoroutinefunction(args.func):
        return asyncio.run(args.func(args))
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
