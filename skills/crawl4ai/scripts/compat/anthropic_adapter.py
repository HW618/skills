#!/usr/bin/env python3
"""Adapter to transform crawl4ai CrawlResult objects into Anthropic tool-use format.

Supports two Anthropic tool formats:
- web_search: Returns a list of web_search_result objects (url, title, page_age, snippet)
- web_fetch:  Returns a single web_fetch_result object (url, title, content)

Usage as library:
    from anthropic_adapter import to_web_search_results, to_web_fetch_result
    results = to_web_search_results(crawl_results)
    result  = to_web_fetch_result(single_result)

Usage as CLI:
    python anthropic_adapter.py --input crawl_summary.json --format web-search
    python anthropic_adapter.py --input crawl_summary.json --format web-fetch --url https://example.com/page
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

SNIPPET_MAX_LENGTH = 200


def _resolve_content(result: dict, base_dir: Path | None = None) -> str:
    """Resolve markdown content from a result dict, reading from file if needed."""
    # Direct markdown field (from CrawlResult serialization)
    md = result.get("markdown")
    if isinstance(md, dict):
        return md.get("raw_markdown", "") or md.get("fit_markdown", "") or ""
    if isinstance(md, str) and md:
        return md
    # Referenced file (from crawl_summary.json / batch_summary.json)
    file_ref = result.get("file")
    if file_ref and base_dir:
        file_path = base_dir / file_ref
        if file_path.exists():
            text = file_path.read_text(encoding="utf-8")
            # Strip metadata header
            if text.startswith("<!--"):
                end = text.find("-->")
                if end != -1:
                    text = text[end + 3:].lstrip("\n")
            return text
    return ""


def _extract_title(result: dict) -> str:
    """Extract title from a serialized CrawlResult dict."""
    metadata = result.get("metadata") or {}
    return metadata.get("title", "") or result.get("title", "")


def _extract_page_age(result: dict) -> str:
    """Extract or derive page age from a serialized CrawlResult dict."""
    metadata = result.get("metadata") or {}
    if metadata.get("modification_date"):
        return metadata["modification_date"]
    if metadata.get("crawled_at"):
        return metadata["crawled_at"]
    return datetime.now().strftime("%Y-%m-%d")


def _load_results_from_file(path: str) -> tuple[list[dict], Path]:
    """Load crawl results from a JSON file, returning (results, base_dir).

    Handles both:
    - A direct list of CrawlResult-like dicts
    - A crawl_summary.json with a "pages" or "results" key
    """
    p = Path(path).resolve()
    with open(p) as f:
        data = json.load(f)

    if isinstance(data, list):
        return data, p.parent
    if isinstance(data, dict):
        base = p.parent
        # Deep crawl summary
        if "pages" in data:
            return data["pages"], base
        # Batch crawl summary
        if "results" in data:
            return data["results"], base
        # Single result
        if "url" in data:
            return [data], base
    return [], p.parent


def to_web_search_results(crawl_results: list[dict], base_dir: Path | None = None) -> list[dict]:
    """Transform a list of CrawlResult dicts into Anthropic web_search result format.

    Each result becomes:
    {
        "type": "web_search_result",
        "url": "...",
        "title": "...",
        "page_age": "...",
        "snippet": "..."  (first 200 chars of markdown)
    }
    """
    output = []
    for r in crawl_results:
        # Skip failed crawls
        if r.get("success") is False:
            continue
        md = _resolve_content(r, base_dir)
        output.append({
            "type": "web_search_result",
            "url": r.get("url", ""),
            "title": _extract_title(r),
            "page_age": _extract_page_age(r),
            "snippet": md[:SNIPPET_MAX_LENGTH],
        })
    return output


def to_web_fetch_result(crawl_result: dict, use_fit: bool = False, base_dir: Path | None = None) -> dict:
    """Transform a single CrawlResult dict into Anthropic web_fetch result format.

    Returns:
    {
        "type": "web_fetch_result",
        "url": "...",
        "title": "...",
        "content": "..."  (full markdown)
    }
    """
    content = _resolve_content(crawl_result, base_dir)
    if use_fit:
        md_field = crawl_result.get("markdown")
        if isinstance(md_field, dict) and md_field.get("fit_markdown"):
            content = md_field["fit_markdown"]

    return {
        "type": "web_fetch_result",
        "url": crawl_result.get("url", ""),
        "title": _extract_title(crawl_result),
        "content": content,
    }


def main():
    parser = argparse.ArgumentParser(description="Crawl4AI → Anthropic format adapter")
    parser.add_argument("--input", required=True, help="Path to crawl results JSON file")
    parser.add_argument("--format", choices=["web-search", "web-fetch"], required=True, help="Output format")
    parser.add_argument("--url", help="Specific URL to extract (for web-fetch format)")
    parser.add_argument("--use-fit", action="store_true", help="Use fit_markdown for web-fetch content")
    parser.add_argument("--output", help="Output file path (default: stdout)")
    args = parser.parse_args()

    results, base_dir = _load_results_from_file(args.input)

    if args.format == "web-search":
        output = to_web_search_results(results, base_dir)
    elif args.format == "web-fetch":
        if args.url:
            matching = [r for r in results if r.get("url") == args.url]
            if not matching:
                print(f"URL not found in results: {args.url}", file=sys.stderr)
                sys.exit(1)
            output = to_web_fetch_result(matching[0], use_fit=args.use_fit, base_dir=base_dir)
        elif len(results) == 1:
            output = to_web_fetch_result(results[0], use_fit=args.use_fit, base_dir=base_dir)
        else:
            print("Multiple results found. Specify --url for web-fetch format.", file=sys.stderr)
            sys.exit(1)

    rendered = json.dumps(output, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
        print(f"Saved to: {args.output}")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
