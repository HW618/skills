#!/usr/bin/env python3
"""Deep crawling with BFS/DFS/BestFirst strategies.

Mandatory: --max-depth and --max-pages must be provided. The script will
prompt for them if missing to prevent unbounded crawls.

Usage:
    python deep_crawl.py <url> --max-depth 2 --max-pages 50
    python deep_crawl.py <url> --max-depth 3 --max-pages 100 --strategy bestfirst --scorer-keywords "api,docs"
    python deep_crawl.py <url> --max-depth 1 --max-pages 10 --stream
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


def _prompt_if_missing(name: str, value, prompt_text: str):
    """Prompt the user for a required parameter if not provided."""
    if value is not None:
        return value
    try:
        raw = input(f"{prompt_text}: ").strip()
        return int(raw)
    except (ValueError, EOFError):
        print(f"Error: --{name} is required.", file=sys.stderr)
        sys.exit(1)


async def deep_crawl(url: str, args: argparse.Namespace) -> int:
    # Validate mandatory params
    max_depth = _prompt_if_missing("max-depth", args.max_depth, "Enter max crawl depth")
    max_pages = _prompt_if_missing("max-pages", args.max_pages, "Enter max pages to crawl")

    # Build browser config
    browser_cfg = build_browser_config(args.config)

    # Build deep crawl strategy
    from crawl4ai.deep_crawling import BFSDeepCrawlStrategy, DFSDeepCrawlStrategy
    from crawl4ai.deep_crawling import BestFirstCrawlingStrategy

    strategy_kwargs = {
        "max_depth": max_depth,
        "max_pages": max_pages,
        "include_external": args.include_external,
    }

    # Add URL pattern filter if provided
    if args.pattern:
        from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter
        strategy_kwargs["filter_chain"] = FilterChain([URLPatternFilter(args.pattern)])

    # Add scorer for BestFirst
    if args.strategy == "bestfirst" and args.scorer_keywords:
        from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer
        keywords = [k.strip() for k in args.scorer_keywords.split(",")]
        strategy_kwargs["url_scorer"] = KeywordRelevanceScorer(keywords=keywords, weight=0.7)

    if args.strategy == "bfs":
        strategy = BFSDeepCrawlStrategy(**strategy_kwargs)
    elif args.strategy == "dfs":
        strategy = DFSDeepCrawlStrategy(**strategy_kwargs)
    elif args.strategy == "bestfirst":
        strategy = BestFirstCrawlingStrategy(**strategy_kwargs)
    else:
        print(f"Unknown strategy: {args.strategy}", file=sys.stderr)
        return 1

    # Build crawler config
    crawler_overrides = {
        "deep_crawl_strategy": strategy,
        "stream": args.stream,
    }
    crawler_cfg = build_crawler_config(args.config, **crawler_overrides)

    # Execute crawl
    from crawl4ai import AsyncWebCrawler

    results = []
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        if args.stream:
            async for result in await crawler.arun(url=url, config=crawler_cfg):
                results.append(result)
        else:
            raw = await crawler.arun(url=url, config=crawler_cfg)
            if isinstance(raw, list):
                results = raw
            else:
                results = [raw]

    # Output directory
    domain = sanitize_domain(url)
    ts = timestamp()
    out_dir = Path(args.output_dir) if args.output_dir else Path(f"{domain}_deep_{ts}")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Write individual pages and build index
    index_entries = []
    success_count = 0
    fail_count = 0

    for result in results:
        if not result.success:
            fail_count += 1
            continue
        success_count += 1

        depth = result.metadata.get("depth", 0) if result.metadata else 0
        title = result.metadata.get("title", "") if result.metadata else ""
        page_domain = sanitize_domain(result.url)
        page_file = out_dir / f"d{depth}_{page_domain}.md"

        content = ""
        if hasattr(result, "markdown"):
            content = result.markdown.raw_markdown if hasattr(result.markdown, "raw_markdown") else str(result.markdown)

        write_markdown(page_file, result.url, title or page_domain, content, depth=depth)
        index_entries.append({
            "url": result.url,
            "title": title,
            "depth": depth,
            "content_length": len(content),
            "file": page_file.name,
        })

    # Write index
    index_path = out_dir / "index.md"
    index_lines = [f"# Deep Crawl Index: {url}", ""]
    index_lines.append(f"- Max depth: {max_depth}")
    index_lines.append(f"- Max pages: {max_pages}")
    index_lines.append(f"- Strategy: {args.strategy}")
    index_lines.append(f"- Success: {success_count}  Failed: {fail_count}")
    index_lines.append("")
    index_lines.append("## Pages")
    index_lines.append("")
    for entry in index_entries:
        index_lines.append(f"- [{entry['title'] or entry['url']}]({entry['file']}) (depth {entry['depth']})")
    index_path.write_text("\n".join(index_lines), encoding="utf-8")

    # Write JSON summary
    summary_path = out_dir / "crawl_summary.json"
    summary_path.write_text(json.dumps({
        "seed_url": url,
        "max_depth": max_depth,
        "max_pages": max_pages,
        "strategy": args.strategy,
        "success": success_count,
        "failed": fail_count,
        "pages": index_entries,
    }, indent=2), encoding="utf-8")

    print(f"Seed:    {url}")
    print(f"Depth:   {max_depth}  Pages: {max_pages}  Strategy: {args.strategy}")
    print(f"Success: {success_count}  Failed: {fail_count}")
    print(f"Output:  {out_dir}/")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Crawl4AI deep crawler")
    parser.add_argument("url", help="Seed URL to start crawling from")
    parser.add_argument("--max-depth", type=int, default=None, help="Maximum crawl depth (required)")
    parser.add_argument("--max-pages", type=int, default=None, help="Maximum pages to crawl (required)")
    parser.add_argument("--strategy", choices=["bfs", "dfs", "bestfirst"], default="bfs", help="Deep crawl strategy")
    parser.add_argument("--include-external", action="store_true", help="Follow external links")
    parser.add_argument("--stream", action="store_true", help="Stream results as they arrive")
    parser.add_argument("--scorer-keywords", help="Comma-separated keywords for BestFirst scorer")
    parser.add_argument("--pattern", help="URL pattern filter (e.g., '*/docs/*')")
    parser.add_argument("--output-dir", help="Output directory path")
    parser.add_argument("--config", help="Override config directory path")
    args = parser.parse_args()
    sys.exit(asyncio.run(deep_crawl(args.url, args)))


if __name__ == "__main__":
    main()
