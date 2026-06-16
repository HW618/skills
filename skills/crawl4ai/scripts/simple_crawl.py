#!/usr/bin/env python3
"""Single-URL crawling with markdown export.

Usage:
    python simple_crawl.py <url> [options]

Examples:
    python simple_crawl.py https://example.com
    python simple_crawl.py https://example.com --css-selector ".main-content"
    python simple_crawl.py https://example.com --fit-markdown --screenshot
    python simple_crawl.py https://example.com --wait-for "css:.content" --js-code "window.scrollTo(0,document.body.scrollHeight)"
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Ensure skill scripts dir is on path for config_loader
sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import (
    build_browser_config,
    build_crawler_config,
    sanitize_domain,
    timestamp,
    write_markdown,
)


async def crawl(url: str, args: argparse.Namespace) -> int:
    # Build browser config (auto-detects CDP_URL)
    browser_overrides = {}
    if args.headless is not None:
        browser_overrides["headless"] = args.headless
    browser_cfg = build_browser_config(args.config, **browser_overrides)

    # Build crawler config
    crawler_overrides = {}
    if args.css_selector:
        crawler_overrides["css_selector"] = args.css_selector
    if args.js_code:
        crawler_overrides["js_code"] = args.js_code
    if args.wait_for:
        crawler_overrides["wait_for"] = args.wait_for
    if args.screenshot:
        crawler_overrides["screenshot"] = True
    if args.word_count_threshold:
        crawler_overrides["word_count_threshold"] = args.word_count_threshold

    crawler_cfg = build_crawler_config(args.config, **crawler_overrides)

    # Content filter for fit_markdown
    if args.fit_markdown:
        from crawl4ai.content_filter_strategy import PruningContentFilter
        from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
        crawler_cfg.markdown_generator = DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.48, threshold_type="fixed")
        )

    # Execute crawl
    from crawl4ai import AsyncWebCrawler

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        result = await crawler.arun(url=url, config=crawler_cfg)

    if not result.success:
        print(f"Crawl failed: {result.error_message}", file=sys.stderr)
        return 1

    # Determine output path
    domain = sanitize_domain(url)
    ts = timestamp()
    output_path = Path(args.output) if args.output else Path(f"{domain}_{ts}.md")

    # Select content
    if args.fit_markdown and hasattr(result, "markdown") and hasattr(result.markdown, "fit_markdown"):
        content = result.markdown.fit_markdown or result.markdown.raw_markdown
    elif hasattr(result, "markdown"):
        content = result.markdown.raw_markdown if hasattr(result.markdown, "raw_markdown") else str(result.markdown)
    else:
        content = str(result.markdown) if result.markdown else ""

    title = ""
    if hasattr(result, "metadata") and result.metadata:
        title = result.metadata.get("title", "")

    write_markdown(output_path, url, title or domain, content)

    # Save screenshot if captured
    if args.screenshot and result.screenshot:
        screenshot_path = output_path.with_suffix(".png")
        if isinstance(result.screenshot, str):
            import base64
            screenshot_path.write_bytes(base64.b64decode(result.screenshot))
        else:
            screenshot_path.write_bytes(result.screenshot)

    # Summary
    print(f"URL:     {result.url}")
    print(f"Title:   {title or 'N/A'}")
    print(f"Content: {len(content)} chars")
    print(f"Saved:   {output_path}")
    if args.screenshot and result.screenshot:
        print(f"Screenshot: {screenshot_path}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Crawl4AI simple crawler")
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument("--output", help="Output markdown file path")
    parser.add_argument("--css-selector", help="Focus on CSS selector")
    parser.add_argument("--js-code", help="Execute JavaScript before extraction")
    parser.add_argument("--wait-for", help="Wait condition (css:SEL or js:EXPR)")
    parser.add_argument("--fit-markdown", action="store_true", help="Export fit_markdown (filtered)")
    parser.add_argument("--screenshot", action="store_true", help="Capture screenshot")
    parser.add_argument("--headless", type=bool, default=None, help="Override headless mode")
    parser.add_argument("--word-count-threshold", type=int, help="Min words per block")
    parser.add_argument("--config", help="Override config directory path")
    args = parser.parse_args()
    sys.exit(asyncio.run(crawl(args.url, args)))


if __name__ == "__main__":
    main()
