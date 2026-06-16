# Anthropic Compatibility Mapping

This document describes how crawl4ai CrawlResult objects map to Anthropic's
web-search and web-fetch tool-use response formats.

The adapter script lives at `scripts/compat/anthropic_adapter.py`.

---

## web-search Tool Result

Anthropic's web-search tool returns results in this format:

```json
[
  {
    "type": "web_search_result",
    "url": "https://example.com/page",
    "title": "Page Title",
    "page_age": "2024-01-01",
    "snippet": "First 200 characters of page content..."
  }
]
```

### Field Mapping

| Anthropic Field | Crawl4AI Source | Notes |
|---|---|---|
| `type` | Fixed: `"web_search_result"` | Always this value |
| `url` | `result.url` | The crawled URL |
| `title` | `result.metadata.get("title", "")` | From page metadata |
| `page_age` | `result.metadata.get("modification_date", "")` or crawl timestamp | Falls back to crawl date |
| `snippet` | `result.markdown[:200]` | First 200 chars of raw markdown |

### Usage

```python
from scripts.compat.anthropic_adapter import to_web_search_results

# With CrawlResult objects from arun_many() or deep crawl
results = to_web_search_results(crawl_results_dicts)

# With saved JSON file
# python anthropic_adapter.py --input crawl_summary.json --format web-search
```

---

## web-fetch Tool Result

Anthropic's web-fetch tool returns a single result:

```json
{
  "type": "web_fetch_result",
  "url": "https://example.com/page",
  "title": "Page Title",
  "content": "Full page content as markdown..."
}
```

### Field Mapping

| Anthropic Field | Crawl4AI Source | Notes |
|---|---|---|
| `type` | Fixed: `"web_fetch_result"` | Always this value |
| `url` | `result.url` | The crawled URL |
| `title` | `result.metadata.get("title", "")` | From page metadata |
| `content` | `result.markdown.raw_markdown` or `result.markdown.fit_markdown` | Full markdown; use `--use-fit` for fit_markdown |

### Usage

```python
from scripts.compat.anthropic_adapter import to_web_fetch_result

# Single result
result = to_web_fetch_result(crawl_result_dict)

# With fit_markdown
result = to_web_fetch_result(crawl_result_dict, use_fit=True)

# CLI
# python anthropic_adapter.py --input result.json --format web-fetch --url https://example.com/page
```

---

## Integration Patterns

### Pattern 1: Direct Library Import

After crawling with any script, load the JSON output and convert:

```python
import json
from anthropic_adapter import to_web_search_results, to_web_fetch_result

with open("crawl_summary.json") as f:
    data = json.load(f)

# web-search format
search_results = to_web_search_results(data.get("pages", data.get("results", [])))

# web-fetch format for a specific URL
single = [r for r in data["results"] if r["url"] == "https://target.com"][0]
fetch_result = to_web_fetch_result(single)
```

### Pattern 2: CLI Pipeline

```bash
# Crawl first
python simple_crawl.py https://example.com --output result.md

# Or batch crawl
python batch_crawl.py urls.txt --output-dir batch_output

# Convert to Anthropic format
python anthropic_adapter.py --input batch_output/batch_summary.json --format web-search --output search_results.json
```

### Pattern 3: In-Code Transformation

When using crawl4ai directly in a Codex workflow:

```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from anthropic_adapter import to_web_search_results, to_web_fetch_result

async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com", config=CrawlerRunConfig())

# Serialize result for adapter (the adapter works on dicts)
result_dict = {
    "url": result.url,
    "success": result.success,
    "markdown": {
        "raw_markdown": result.markdown.raw_markdown if hasattr(result.markdown, "raw_markdown") else str(result.markdown),
        "fit_markdown": result.markdown.fit_markdown if hasattr(result.markdown, "fit_markdown") else None,
    },
    "metadata": result.metadata or {},
}

search_result = to_web_search_results([result_dict])
fetch_result = to_web_fetch_result(result_dict)
```

---

## Notes

- Failed crawl results (where `success` is `False`) are automatically excluded from `web_search` output.
- The `snippet` field is capped at 200 characters per Anthropic conventions.
- `page_age` uses the best available date from metadata; falls back to the crawl timestamp.
- The adapter handles both raw CrawlResult-like dicts and the summary JSON formats produced by this skill's scripts.
