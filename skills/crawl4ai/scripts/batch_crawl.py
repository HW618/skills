#!/usr/bin/env python3
"""Batch/multi-URL concurrent crawling with markdown export.

Usage:
    python batch_crawl.py urls.txt
    python batch_crawl.py "https://site1.com,https://site2.com"
    python batch_crawl.py urls.txt --max-concurrent 3 --extract-schema schema.json
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import (
    build_browser_config,
    build_crawler_config,
    sanitize_domain,
    timestamp,
    write_markdown,
)


def load_urls(source: str) -> list[str]:
    """Load URLs from a file or comma-separated string."""
    p = Path(source)
    if p.exists():
        return [line.strip() for line in p.read_text().splitlines() if line.strip() and not line.startswith("#")]
    return [u.strip() for u in source.split(",") if u.strip()]


async def batch_crawl(args: argparse.Namespace) -> int:
    urls = load_urls(args.urls)
    if not urls:
        print("No URLs found.", file=sys.stderr)
        return 1

    print(f"Batch crawling {len(urls)} URLs (max concurrent: {args.max_concurrent})")

    browser_cfg = build_browser_config(args.config)

    # Optional extraction strategy
    crawler_overrides = {}
    if args.extract_schema:
        from crawl4ai import JsonCssExtractionStrategy
        with open(args.extract_schema) as f:
            schema = json.load(f)
        crawler_overrides["extraction_strategy"] = JsonCssExtractionStrategy(schema=schema)

    crawler_cfg = build_crawler_config(args.config, **crawler_overrides)

    from crawl4ai import AsyncWebCrawler

    out_dir = Path(args.output_dir) if args.output_dir else Path(f"batch_output_{timestamp()}")
    out_dir.mkdir(parents=True, exist_ok=True)

    results_summary = []
    success_count = 0
    fail_count = 0

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        batch_results = await crawler.arun_many(
            urls=urls, config=crawler_cfg, max_concurrent=args.max_concurrent
        )

        for i, result in enumerate(batch_results):
            if not result.success:
                fail_count += 1
                results_summary.append({"url": result.url, "status": "failed", "error": result.error_message})
                print(f"  FAIL {result.url}: {result.error_message}")
                continue

            success_count += 1
            title = result.metadata.get("title", "") if result.metadata else ""
            safe_name = sanitize_domain(result.url)
            page_file = out_dir / f"{i:03d}_{safe_name}.md"

            content = ""
            if hasattr(result, "markdown"):
                content = result.markdown.raw_markdown if hasattr(result.markdown, "raw_markdown") else str(result.markdown)

            write_markdown(page_file, result.url, title or safe_name, content)

            entry = {
                "url": result.url,
                "status": "success",
                "title": title,
                "content_length": len(content),
                "file": page_file.name,
            }
            if result.extracted_content:
                entry["extracted_content"] = result.extracted_content
            results_summary.append(entry)
            print(f"  OK   {result.url} ({len(content)} chars)")

    # Save summary
    summary_path = out_dir / "batch_summary.json"
    summary_path.write_text(json.dumps({
        "total": len(urls),
        "success": success_count,
        "failed": fail_count,
        "results": results_summary,
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nDone: {success_count} ok, {fail_count} failed → {out_dir}/")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Crawl4AI batch crawler")
    parser.add_argument("urls", help="File with URLs (one per line) or comma-separated URLs")
    parser.add_argument("--max-concurrent", type=int, default=5, help="Max concurrent crawls")
    parser.add_argument("--output-dir", help="Output directory")
    parser.add_argument("--extract-schema", help="Path to CSS extraction schema JSON")
    parser.add_argument("--config", help="Override config directory path")
    args = parser.parse_args()
    sys.exit(asyncio.run(batch_crawl(args)))


if __name__ == "__main__":
    main()
