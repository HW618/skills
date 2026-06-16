---
name: crawl4ai
description: Web crawling and data extraction using Crawl4AI (v0.8.x). Use when users need to crawl websites, scrape web pages, extract structured data, perform deep site crawling with BFS/DFS/BestFirst strategies, discover URLs via seeding or domain mapping, convert web content to markdown, batch-crawl multiple URLs, or produce results compatible with Anthropic web-search/web-fetch tool format. Triggers include crawl, scrape, spider, harvest, extract from web, deep crawl, URL discovery, domain mapping, web search, web fetch, site mapping.
---

# Crawl4AI

## Workflow

1. Verify crawl4ai is installed; run `pip install crawl4ai && crawl4ai-setup` if needed.
2. Choose crawling mode: simple, deep, URL seeding, domain mapping, or batch.
3. Load default configs from `references/config/`; apply env-var and CLI overrides.
4. Execute crawl; check `result.success`; write markdown output.
5. For Anthropic compatibility, run the adapter on results.

Read [references/crawl4ai-sdk-reference.md](references/crawl4ai-sdk-reference.md) for detailed API parameters and class definitions.
Read [references/anthropic-compat-mapping.md](references/anthropic-compat-mapping.md) when converting crawl results to Anthropic web-search/web-fetch format.

## Safety Rules

- Do not crawl sites that explicitly forbid it in `robots.txt`.
- Rate-limit between requests: add `asyncio.sleep(1-3)` between sequential crawls.
- Do not echo, log, or print API keys, tokens, or the values of `C4A_LLM_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, or any other secret environment variables. It is acceptable to report which variable names are present or missing.
- Do not perform destructive operations (delete, purge, overwrite remote content).
- Use `--dry-run` or small `max_pages` values for exploratory crawls.

## Environment Setup

```bash
pip install crawl4ai
crawl4ai-setup
crawl4ai-doctor  # verify installation
```

Required environment variables (set before running scripts):

| Variable | Purpose |
|---|---|
| `CDP_URL` | External CDP browser endpoint (optional; auto-detects) |
| `C4A_LLM_PROVIDER` | LLM provider string, e.g., `openai/gpt-4o-mini` |
| `C4A_LLM_API_KEY` | Explicit API key override (optional) |
| `C4A_LLM_BASE_URL` | Custom LLM endpoint (optional) |
| `C4A_PROXY` | Proxy URL for browser requests (optional) |
| `C4A_CONFIG_DIR` | Override config directory path (optional) |

API key auto-detection by provider prefix: `openai/*` → `OPENAI_API_KEY`, `anthropic/*` → `ANTHROPIC_API_KEY`, `groq/*` → `GROQ_API_KEY`, `gemini/*` → `GEMINI_API_KEY`, `deepseek/*` → `DEEPSEEK_API_KEY`, `ollama/*` → no key.

## Configuration

Three default JSON config files in `references/config/`:

- `browser_config.json` — BrowserConfig defaults (44 parameters)
- `crawler_config.json` — CrawlerRunConfig defaults (91 parameters across 12 categories, note: `prettiify` has 3 i's)
- `llm_config.json` — LLMConfig defaults (13 parameters including sampling and backoff retry)

Scripts load these at startup and merge with env vars and CLI args. Edit the JSON files directly to persist custom behavior. Override the config directory with `--config PATH` or `C4A_CONFIG_DIR`.

When `CDP_URL` is set, scripts automatically switch to `browser_mode="custom"` with the provided CDP endpoint. When unset, they fall back to crawl4ai's built-in headless browser (`browser_mode="dedicated"`).

## Simple Crawling

Crawl a single URL and export as markdown.

```bash
python scripts/simple_crawl.py https://example.com
python scripts/simple_crawl.py https://example.com --css-selector ".main-content" --fit-markdown
python scripts/simple_crawl.py https://example.com --js-code "window.scrollTo(0,document.body.scrollHeight)" --wait-for "css:.content"
```

Key options: `--output PATH`, `--css-selector SEL`, `--js-code CODE`, `--wait-for COND`, `--fit-markdown`, `--screenshot`.

## Deep Crawling

Crawl a site recursively with BFS, DFS, or BestFirst strategy. **`max_depth` and `max_pages` are mandatory** — the script prompts if they are missing.

```bash
python scripts/deep_crawl.py https://example.com --max-depth 2 --max-pages 50
python scripts/deep_crawl.py https://example.com --max-depth 3 --max-pages 100 --strategy bestfirst --scorer-keywords "api,docs"
python scripts/deep_crawl.py https://example.com --max-depth 1 --max-pages 10 --include-external --stream
```

Key options: `--strategy bfs|dfs|bestfirst`, `--include-external`, `--stream`, `--scorer-keywords K1,K2`, `--pattern GLOB`, `--output-dir PATH`.

Output: a directory with individual `.md` files per page, an `index.md` summary, and a `crawl_summary.json`.

## URL Seeding

Discover URLs from sitemaps and Common Crawl, then optionally crawl them.

```bash
python scripts/url_seed_crawl.py example.com --source "sitemap+cc" --pattern "*/blog/*"
python scripts/url_seed_crawl.py example.com --filter-keywords "python,tutorial" --crawl --max-urls 50
```

Key options: `--source TYPE`, `--pattern GLOB`, `--max-urls N`, `--filter-keywords K1,K2`, `--crawl`, `--output PATH`.

## Domain Mapping

Discover all URLs under a domain across 8 sources (sitemap, Common Crawl, Wayback, crt.sh, probe, robots.txt, feeds, homepage).

```bash
python scripts/domain_map.py example.com
python scripts/domain_map.py example.com --source "sitemap+cc+wayback+crt+probe+robots+feed+homepage" --markdown
```

Key options: `--source TYPE`, `--probe-paths P1,P2`, `--output PATH`, `--markdown`.

## Batch Crawling

Crawl multiple URLs concurrently.

```bash
python scripts/batch_crawl.py urls.txt --max-concurrent 5
python scripts/batch_crawl.py "https://site1.com,https://site2.com" --output-dir batch_out
```

Key options: `--max-concurrent N`, `--output-dir PATH`, `--extract-schema PATH`.

## Anthropic Compatibility

Transform crawl results into Anthropic web-search/web-fetch format.

```bash
python scripts/compat/anthropic_adapter.py --input crawl_summary.json --format web-search
python scripts/compat/anthropic_adapter.py --input result.json --format web-fetch --url https://example.com/page
```

Or in Python:

```python
from scripts.compat.anthropic_adapter import to_web_search_results, to_web_fetch_result
search_results = to_web_search_results(results_dicts)
fetch_result = to_web_fetch_result(single_result_dict, use_fit=True)
```

See [references/anthropic-compat-mapping.md](references/anthropic-compat-mapping.md) for full field mapping details.

## Troubleshooting

**crawl4ai not found:** Run `pip install crawl4ai && crawl4ai-setup`.

**CDP connection fails:** Verify the browser at `CDP_URL` is running. Check `ws://host:port/json/version` responds. Remove `CDP_URL` to fall back to built-in browser.

**JavaScript not loading:** Add `--wait-for "css:.dynamic-content"` and increase `page_timeout` in `crawler_config.json`.

**Bot detection:** Set `enable_stealth: true` in `browser_config.json`. Add `user_agent_mode: "random"`. Add delays between requests.

**Empty markdown:** Try `--css-selector` to target content area, or `--fit-markdown` to use pruning filter. Check `result.success` and `result.error_message`.

**LLM extraction errors:** Verify API key env var is set for the chosen provider. Check `C4A_LLM_PROVIDER` format is `provider/model`.
