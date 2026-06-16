#!/usr/bin/env python3
"""Domain mapping: discover all URLs under a domain across 8 sources.

Sources: sitemap, cc (Common Crawl), wayback, crt (Certificate Transparency),
probe, robots, feed, homepage. Combine with + (e.g., "sitemap+cc+crt+probe").

Usage:
    python domain_map.py example.com
    python domain_map.py example.com --source "sitemap+cc+crt+probe" --markdown
    python domain_map.py example.com --source "sitemap+cc+wayback+crt+probe+robots+feed+homepage"
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import sanitize_domain, timestamp


async def map_domain(domain: str, args: argparse.Namespace) -> int:
    from crawl4ai import DomainMapper, DomainMapperConfig

    cfg_kwargs = {"source": args.source}
    if args.probe_paths:
        cfg_kwargs["probe_paths"] = [p.strip() for p in args.probe_paths.split(",")]

    mapper_config = DomainMapperConfig(**cfg_kwargs)

    print(f"Mapping {domain} (sources: {args.source})...")
    async with DomainMapper() as mapper:
        results = await mapper.scan(domain)

    print(f"Found {len(results)} URLs")

    # Save JSON
    domain_safe = sanitize_domain(domain)
    ts = timestamp()
    output_path = Path(args.output) if args.output else Path(f"{domain_safe}_map.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"JSON saved to: {output_path}")

    # Optionally save markdown index
    if args.markdown:
        md_path = output_path.with_suffix(".md")
        lines = [f"# Domain Map: {domain}", ""]
        lines.append(f"- Sources: {args.source}")
        lines.append(f"- Total URLs: {len(results)}")
        lines.append("")

        # Group by source
        by_source: dict[str, list] = {}
        hosts: set[str] = set()
        for r in results:
            src = r.get("source", "unknown")
            by_source.setdefault(src, []).append(r)
            host = r.get("url", "").split("/")[2] if "://" in r.get("url", "") else ""
            if host:
                hosts.add(host)

        if hosts:
            lines.append("## Hosts")
            lines.append("")
            for h in sorted(hosts):
                lines.append(f"- {h}")
            lines.append("")

        for src, entries in sorted(by_source.items()):
            lines.append(f"## Source: {src} ({len(entries)} URLs)")
            lines.append("")
            for e in entries[:50]:
                url = e.get("url", "")
                title = ""
                hd = e.get("head_data")
                if isinstance(hd, dict):
                    title = hd.get("title", "")
                label = title or url
                lines.append(f"- [{label}]({url})")
            if len(entries) > 50:
                lines.append(f"- ... and {len(entries) - 50} more")
            lines.append("")

        md_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Markdown saved to: {md_path}")

    # Quick summary
    sources_used = set(r.get("source", "") for r in results)
    print(f"Sources: {', '.join(sorted(sources_used))}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Crawl4AI domain mapper")
    parser.add_argument("domain", help="Domain to map (e.g., example.com)")
    parser.add_argument("--source", default="sitemap+cc+crt+probe", help="Discovery sources (default: sitemap+cc+crt+probe)")
    parser.add_argument("--probe-paths", help="Comma-separated additional paths to probe")
    parser.add_argument("--output", help="Output JSON file path")
    parser.add_argument("--markdown", action="store_true", help="Also export as markdown index")
    parser.add_argument("--config", help="Override config directory path (not used by DomainMapper)")
    args = parser.parse_args()
    sys.exit(asyncio.run(map_domain(args.domain, args)))


if __name__ == "__main__":
    main()
