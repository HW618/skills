#!/usr/bin/env python3
"""URL seeding: discover URLs from sitemaps/Common Crawl, then optionally crawl them.

Usage:
    python url_seed_crawl.py example.com
    python url_seed_crawl.py example.com --source "sitemap+cc" --pattern "*/blog/*"
    python url_seed_crawl.py example.com --filter-keywords "python,tutorial" --crawl
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import sanitize_domain, timestamp


async def seed_and_crawl(domain: str, args: argparse.Namespace) -> int:
    from crawl4ai import AsyncUrlSeeder, SeedingConfig

    # Configure seeding
    seeding_cfg = SeedingConfig(
        source=args.source,
        pattern=args.pattern or None,
        extract_head=args.extract_head,
        max_urls=args.max_urls or 1000,
    )

    # Discover URLs
    seeder = AsyncUrlSeeder()
    print(f"Discovering URLs for {domain} (source: {args.source})...")
    urls = await seeder.urls(domain, seeding_cfg)
    print(f"Discovered {len(urls)} URLs")

    # Apply keyword filtering if requested
    if args.filter_keywords:
        keywords = [k.strip().lower() for k in args.filter_keywords.split(",")]
        filtered = []
        for u in urls:
            text_to_search = str(u.get("head_data", "")).lower() + " " + str(u.get("url", "")).lower()
            if any(kw in text_to_search for kw in keywords):
                filtered.append(u)
        print(f"Filtered to {len(filtered)} URLs matching keywords: {args.filter_keywords}")
        urls = filtered

    # Validate URLs
    valid_urls = [u for u in urls if u.get("status") == "valid"]
    print(f"Valid URLs: {len(valid_urls)}")

    # Save URL list
    domain_safe = sanitize_domain(domain)
    ts = timestamp()
    output_path = Path(args.output) if args.output else Path(f"{domain_safe}_urls.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(urls, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"URL list saved to: {output_path}")

    # Optionally crawl discovered URLs
    if args.crawl and valid_urls:
        from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
        from config_loader import build_browser_config, write_markdown

        browser_cfg = build_browser_config(args.config)
        crawl_urls = [u["url"] for u in valid_urls[:args.max_urls or 50]]

        out_dir = Path(f"{domain_safe}_seeded_{ts}")
        out_dir.mkdir(parents=True, exist_ok=True)

        crawler_cfg = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, verbose=True)
        async with AsyncWebCrawler(config=browser_cfg) as crawler:
            results = await crawler.arun_many(urls=crawl_urls, config=crawler_cfg, max_concurrent=args.max_concurrent)

        success_count = 0
        for i, result in enumerate(results):
            if not result.success:
                continue
            success_count += 1
            title = result.metadata.get("title", "") if result.metadata else ""
            page_file = out_dir / f"{i:03d}_{sanitize_domain(result.url)}.md"
            content = ""
            if hasattr(result, "markdown"):
                content = result.markdown.raw_markdown if hasattr(result.markdown, "raw_markdown") else str(result.markdown)
            write_markdown(page_file, result.url, title or sanitize_domain(result.url), content)

        print(f"Crawled {success_count}/{len(crawl_urls)} pages → {out_dir}/")

    return 0


def main():
    parser = argparse.ArgumentParser(description="Crawl4AI URL seeder")
    parser.add_argument("domain", help="Domain to discover URLs from (e.g., example.com)")
    parser.add_argument("--source", default="sitemap+cc", help="Seeding source (default: sitemap+cc)")
    parser.add_argument("--pattern", help="URL pattern filter (e.g., '*/blog/*')")
    parser.add_argument("--max-urls", type=int, help="Maximum URLs to discover")
    parser.add_argument("--extract-head", action="store_true", default=True, help="Extract page metadata")
    parser.add_argument("--filter-keywords", help="Comma-separated keywords to filter URLs by head data")
    parser.add_argument("--crawl", action="store_true", help="Crawl discovered URLs after seeding")
    parser.add_argument("--max-concurrent", type=int, default=5, help="Max concurrent crawls (with --crawl)")
    parser.add_argument("--output", help="Output JSON file path for URL list")
    parser.add_argument("--config", help="Override config directory path")
    args = parser.parse_args()
    sys.exit(asyncio.run(seed_and_crawl(args.domain, args)))


if __name__ == "__main__":
    main()
