# Crawl4AI Skill — Product Requirements Document

## Summary

A Codex skill that wraps the Crawl4AI library (v0.8.x) to provide web crawling capabilities inside Codex conversations. It supports simple crawling, deep crawling, URL seeding, domain mapping, markdown export, external CDP browser connection, configurable LLM extraction, and compatibility with Anthropic's web-search/web-fetch tool format.

**Skill location:** `/Users/user/Documents/skills/skills/crawl4ai/`

---

## Requirements

### R1 — Simple Crawling

- Crawl a single URL and return page content as markdown.
- Use `AsyncWebCrawler.arun()` with configurable `BrowserConfig` and `CrawlerRunConfig`.
- Support content filtering options (CSS selector, excluded tags, word count threshold).
- Support JavaScript execution and wait-for conditions for dynamic pages.
- Save results as `.md` files to the current working directory (or a user-specified path).

### R2 — Deep Crawling

- Support BFS, DFS, and BestFirst deep crawl strategies via `crawl4ai.deep_crawling` module.
- **Mandatory parameters** when deep crawling: `max_depth` (maximum crawl depth beyond the seed page) and `max_pages` (maximum number of pages to crawl).
- If the user does not specify `max_depth` or `max_pages`, prompt for them before starting.
- Support streaming and non-streaming result modes.
- Support filter chains (URL patterns, domain constraints) and scorers (keyword relevance) for BestFirst strategy.
- Support `include_external` toggle (default: `False`, stay within the same domain).
- Export all crawled pages as individual markdown files plus a summary index.

### R3 — URL Seeding

- Use `AsyncUrlSeeder` with `SeedingConfig` to discover URLs from sitemaps, Common Crawl, or combined sources before crawling.
- Support pattern-based URL filtering (`pattern` parameter).
- Support metadata extraction (`extract_head=True`) for pre-crawl filtering.
- Allow users to seed URLs first, review/filter, then crawl only selected URLs.
- Provide a script that chains seeding → filtering → crawling in one command.

### R4 — Domain Mapping

- Use `DomainMapper` with `DomainMapperConfig` to discover all URLs under a domain across 8 sources (sitemap, Common Crawl, Wayback, crt.sh, probe, robots.txt, feeds, homepage).
- Support configurable source combinations (e.g., `"sitemap+cc+crt+probe"`).
- Support subdomain discovery and soft-404 detection.
- Export discovered URL list as JSON and optionally as a markdown index.
- Allow domain mapping results to feed directly into deep crawling.

### R5 — Anthropic Web-Search/Web-Fetch Compatibility

- Provide an output adapter (`scripts/compat/anthropic_adapter.py`) that transforms crawl4ai `CrawlResult` objects into Anthropic's tool-use response format.
- **web-search format:** Return a list of `{type: "web_search_result", url, title, page_age, snippet}` objects.
- **web-fetch format:** Return `{type: "web_fetch_result", url, title, content}` where `content` is the markdown text.
- The adapter is a callable module that Codex can invoke after crawling to format results for Anthropic-compatible tool chains.
- Document the mapping in a reference file.

### R6 — External CDP Browser

- If the environment variable `CDP_URL` is set, automatically configure `BrowserConfig(browser_mode="custom", cdp_url=os.environ["CDP_URL"])`.
- If `CDP_URL` is not set, fall back to `BrowserConfig(browser_mode="dedicated", headless=True)` (crawl4ai manages its own browser).
- Users never need to manually edit `BrowserConfig` for CDP setup; the scripts and SKILL.md handle it automatically.
- Validate the CDP connection before crawling with a simple health check.

### R7 — Markdown Export

- All crawl results are exportable as markdown files.
- File naming convention: `<sanitized_domain>_<timestamp>.md` for single pages; `<sanitized_domain>_deep_<timestamp>/` directory for deep crawls with an `index.md` summary.
- Each markdown file includes metadata header (URL, title, crawl date, depth if applicable).
- Support `fit_markdown` (filtered/relevant content) alongside `raw_markdown` via configurable content filters.

### R8 — LLM Provider Configuration

- Single environment variable `C4A_LLM_PROVIDER` sets the provider string (e.g., `openai/gpt-4o-mini`, `anthropic/claude-3-5-sonnet-20241022`, `ollama/llama3.3`).
- API keys are auto-detected from standard environment variables based on the provider prefix:
  - `openai/*` → `OPENAI_API_KEY`
  - `anthropic/*` → `ANTHROPIC_API_KEY`
  - `groq/*` → `GROQ_API_KEY`
  - `gemini/*` → `GEMINI_API_KEY` or `GOOGLE_API_KEY`
  - `deepseek/*` → `DEEPSEEK_API_KEY`
  - `ollama/*` → no key required
- Optional overrides: `C4A_LLM_API_KEY` (explicit key), `C4A_LLM_BASE_URL` (custom endpoint).
- These env vars populate `LLMConfig(provider=..., api_token=..., base_url=...)`.

### R9 — Default Configuration Files

- Generate three default JSON configuration files in `references/config/`:
  - `browser_config.json` — Default `BrowserConfig` parameters.
  - `crawler_config.json` — Default `CrawlerRunConfig` parameters.
  - `llm_config.json` — Default `LLMConfig` parameters.
- Scripts read these files at startup and merge them with runtime parameters (env vars, CLI args, or function arguments).
- Users can edit these files directly to persist custom behavior without changing code.
- Document each config field with comments or a companion reference file.

### R10 — Additional (Derived from Analysis)

- **Installation check:** Script or SKILL.md instruction to verify `crawl4ai` is installed (`pip install crawl4ai && crawl4ai-setup`).
- **Safety rules:** No destructive operations; respect `robots.txt`; rate limiting between requests; do not echo API keys.
- **Batch/multi-URL crawling:** Support `arun_many()` for concurrent crawling of multiple seed URLs with configurable `max_concurrent`.
- **Session management:** Support `session_id` for authenticated crawling flows (login → crawl protected pages).
- **Proxy support:** Forward `C4A_PROXY` env var to `BrowserConfig(proxy_config=...)`.
- **Error handling:** All scripts must check `result.success` and report `result.error_message` on failure; return non-zero exit codes.
- **Cache control:** Default to `CacheMode.BYPASS` for fresh content; allow `CacheMode.ENABLED` via config file or env var.

---

## Skill Structure

```
crawl4ai/
├── SKILL.md                          # Skill instructions (triggers, workflow, safety)
├── agents/
│   └── openai.yaml                   # UI metadata
├── scripts/
│   ├── simple_crawl.py               # Single-URL crawling with markdown export
│   ├── deep_crawl.py                 # Deep crawling (BFS/DFS/BestFirst) with max_depth + max_pages
│   ├── url_seed_crawl.py             # URL seeding → filter → crawl pipeline
│   ├── domain_map.py                 # Domain mapping and URL discovery
│   ├── batch_crawl.py                # Multi-URL concurrent crawling
│   └── compat/
│       └── anthropic_adapter.py      # Output adapter for Anthropic web-search/web-fetch format
├── references/
│   ├── config/
│   │   ├── browser_config.json       # Default BrowserConfig
│   │   ├── crawler_config.json       # Default CrawlerRunConfig
│   │   └── llm_config.json           # Default LLMConfig
│   ├── crawl4ai-sdk-reference.md     # Condensed SDK reference (key APIs and parameters)
│   └── anthropic-compat-mapping.md   # Documentation for Anthropic format mapping
└── PRD.md                            # This file
```

---

## Script Specifications

### `scripts/simple_crawl.py`

```
Usage: python simple_crawl.py <url> [options]

Options:
  --output PATH          Output file path (default: ./<domain>_<ts>.md)
  --css-selector SEL     Focus on CSS selector
  --js-code CODE         Execute JavaScript before extraction
  --wait-for COND        Wait condition (css:selector or js:expr)
  --fit-markdown         Export fit_markdown instead of raw_markdown
  --screenshot           Capture screenshot
  --no-cache             Force bypass cache (default behavior)
  --config PATH          Override default config directory path
```

Behavior:
1. Load configs from `references/config/` (overridable via `--config`).
2. Resolve `CDP_URL` env var → set `browser_mode` and `cdp_url` accordingly.
3. Run `arun()` with merged config.
4. Write markdown to output file with metadata header.
5. Print summary (URL, title, content length, output path).

### `scripts/deep_crawl.py`

```
Usage: python deep_crawl.py <url> [options]

Required:
  --max-depth N          Maximum crawl depth (prompt if missing)
  --max-pages N          Maximum pages to crawl (prompt if missing)

Options:
  --strategy bfs|dfs|bestfirst   Deep crawl strategy (default: bfs)
  --include-external      Follow external links (default: stay in-domain)
  --stream                Stream results as they arrive
  --scorer-keywords K1,K2,...  Keywords for BestFirst scorer
  --pattern GLOB          URL pattern filter (e.g., "*/docs/*")
  --output-dir PATH       Output directory (default: ./<domain>_deep_<ts>/)
  --config PATH           Override default config directory path
```

Behavior:
1. Validate `max_depth` and `max_pages` are provided; prompt if missing.
2. Load configs, resolve CDP URL.
3. Create deep crawl strategy with filter chain and optional scorer.
4. Run deep crawl; collect all results.
5. Write individual `.md` files per page + `index.md` summary.
6. Print summary (total pages, success/fail counts, output directory).

### `scripts/url_seed_crawl.py`

```
Usage: python url_seed_crawl.py <domain> [options]

Options:
  --source TYPE          Seeding source (default: "sitemap+cc")
  --pattern GLOB         URL pattern filter
  --max-urls N           Maximum URLs to discover
  --extract-head         Extract page metadata (default: True)
  --filter-keywords K1,K2,...  Filter discovered URLs by keywords in head data
  --crawl                After seeding, crawl the discovered URLs
  --output PATH          Save URL list to JSON (default: ./<domain>_urls.json)
  --config PATH          Override default config directory path
```

Behavior:
1. Run `AsyncUrlSeeder.urls()` with `SeedingConfig`.
2. Apply keyword/pattern filtering.
3. Save filtered URL list as JSON.
4. If `--crawl` is set, pass URLs to `batch_crawl.py` logic.
5. Print summary (discovered URLs, filtered count, crawl status if applicable).

### `scripts/domain_map.py`

```
Usage: python domain_map.py <domain> [options]

Options:
  --source TYPE          Discovery sources (default: "sitemap+cc+crt+probe")
  --probe-paths P1,P2    Additional paths to probe
  --output PATH          Save results to JSON (default: ./<domain>_map.json)
  --markdown             Also export as markdown index
  --config PATH          Override default config directory path
```

Behavior:
1. Run `DomainMapper.scan()` with `DomainMapperConfig`.
2. Save results as JSON (URL, source, subdomain, head_data).
3. Optionally export as markdown index.
4. Print summary (total URLs, sources used, subdomains found).

### `scripts/batch_crawl.py`

```
Usage: python batch_crawl.py <urls_file_or_comma_list> [options]

Options:
  --max-concurrent N     Max concurrent crawls (default: 5)
  --output-dir PATH      Output directory (default: ./batch_output/)
  --extract-schema PATH  Use CSS extraction schema
  --config PATH          Override default config directory path
```

Behavior:
1. Load URLs from file or comma-separated string.
2. Run `arun_many()` with merged config.
3. Write individual `.md` files and a summary JSON.
4. Print success/fail counts.

### `scripts/compat/anthropic_adapter.py`

```
Usage:
  From Python:  from compat.anthropic_adapter import to_web_search_results, to_web_fetch_result
  CLI:          python anthropic_adapter.py --input results.json --format web-search|web-fetch
```

Behavior:
- `to_web_search_results(crawl_results)`: Transform a list of CrawlResult into Anthropic `web_search` tool result format.
- `to_web_fetch_result(crawl_result)`: Transform a single CrawlResult into Anthropic `web_fetch` tool result format.
- Read crawl results from JSON file (CLI mode) or accept Python objects (library mode).

---

## Default Configuration Files

### `references/config/browser_config.json`

```json
{
  "_doc": "Full BrowserConfig parameters for Crawl4AI v0.8.x. Edit values to customize browser behavior. See https://docs.crawl4ai.com/api/parameters/",
  "browser_type": "chromium",
  "headless": true,
  "browser_mode": "dedicated",
  "viewport_width": 1080,
  "viewport_height": 600,
  "viewport": null,
  "device_scale_factor": 1.0,
  "use_managed_browser": false,
  "cdp_url": null,
  "debugging_port": 9222,
  "host": "localhost",
  "proxy": null,
  "proxy_config": null,
  "use_persistent_context": false,
  "user_data_dir": null,
  "chrome_channel": "chromium",
  "channel": "chromium",
  "accept_downloads": false,
  "downloads_path": null,
  "storage_state": null,
  "ignore_https_errors": true,
  "java_script_enabled": true,
  "sleep_on_close": false,
  "cookies": [],
  "headers": {},
  "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/116.0.0.0 Safari/537.36",
  "user_agent_mode": "",
  "user_agent_generator_config": {},
  "text_mode": false,
  "light_mode": false,
  "avoid_ads": false,
  "avoid_css": false,
  "extra_args": [],
  "enable_stealth": false
}
```

Notes:
- `browser_mode` and `cdp_url` are overridden at runtime when `CDP_URL` env var is set.
- `use_managed_browser` is set automatically based on `browser_mode`.

### `references/config/crawler_config.json`

```json
{
  "_doc": "Full CrawlerRunConfig parameters for Crawl4AI v0.8.x. Edit values to customize crawl behavior. See https://docs.crawl4ai.com/api/parameters/",

  "word_count_threshold": 10,
  "extraction_strategy": null,
  "chunking_strategy": "RegexChunking",
  "markdown_generator": null,
  "css_selector": null,
  "target_elements": null,
  "excluded_tags": null,
  "excluded_selector": null,
  "only_text": false,
  "prettify": false,
  "keep_data_attributes": false,
  "keep_attrs": [],
  "remove_forms": false,
  "parser_type": "lxml",
  "scraping_strategy": "LXMLWebScrapingStrategy",

  "locale": null,
  "timezone_id": null,
  "geolocation": null,
  "fetch_ssl_certificate": false,
  "proxy_config": null,
  "proxy_rotation_strategy": null,
  "max_retries": 0,
  "fallback_fetch_function": null,

  "cache_mode": "BYPASS",
  "session_id": null,
  "bypass_cache": false,
  "disable_cache": false,
  "no_cache_read": false,
  "no_cache_write": false,
  "shared_data": null,

  "wait_until": "domcontentloaded",
  "page_timeout": 60000,
  "wait_for": null,
  "wait_for_timeout": null,
  "wait_for_images": false,
  "delay_before_return_html": 0.1,
  "check_robots_txt": false,
  "mean_delay": 0.1,
  "max_range": 0.3,
  "semaphore_count": 5,

  "js_code": null,
  "js_code_before_wait": null,
  "c4a_script": null,
  "js_only": false,
  "ignore_body_visibility": true,
  "scan_full_page": false,
  "scroll_delay": 0.2,
  "max_scroll_steps": null,
  "process_iframes": false,
  "flatten_shadow_dom": false,
  "remove_overlay_elements": true,
  "remove_consent_popups": false,
  "simulate_user": false,
  "override_navigator": false,
  "magic": false,
  "adjust_viewport_to_content": false,

  "screenshot": false,
  "screenshot_wait_for": null,
  "screenshot_height_threshold": 20000,
  "force_viewport_screenshot": false,
  "pdf": false,
  "capture_mhtml": false,
  "image_description_min_word_threshold": 50,
  "image_score_threshold": 3,
  "exclude_external_images": false,
  "exclude_all_images": false,
  "table_score_threshold": 7,
  "table_extraction": "DefaultTableExtraction",

  "exclude_social_media_domains": null,
  "exclude_external_links": false,
  "exclude_social_media_links": false,
  "exclude_domains": [],
  "exclude_internal_links": false,
  "score_links": false,
  "preserve_https_for_internal_links": false,

  "verbose": true,
  "log_console": false,
  "capture_network_requests": false,
  "capture_console_messages": false,

  "method": "GET",
  "stream": false,
  "url": null,
  "user_agent": null,
  "user_agent_mode": null,
  "user_agent_generator_config": {},

  "virtual_scroll_config": null,
  "url_matcher": null,
  "match_mode": "OR",

  "deep_crawl_strategy": null,
  "link_preview_config": null,
  "experimental": null
}
```

### `references/config/llm_config.json`

```json
{
  "_doc": "Full LLMConfig parameters for Crawl4AI v0.8.x. Edit values to customize LLM provider behavior. See https://docs.crawl4ai.com/api/parameters/",
  "provider": "openai/gpt-4o-mini",
  "api_token": null,
  "base_url": null,
  "backoff_base_delay": 2,
  "backoff_max_attempts": 3,
  "backoff_exponential_factor": 2
}
```

Notes:
- `browser_mode` and `cdp_url` are overridden at runtime when `CDP_URL` env var is set.
- `use_managed_browser` is set automatically based on `browser_mode`.
- `provider` is overridden by `C4A_LLM_PROVIDER` env var if set.
- `api_token` is auto-resolved from provider-specific env vars (e.g., `OPENAI_API_KEY`) unless `C4A_LLM_API_KEY` is set.
- `backoff_*` parameters control retry behavior when the LLM provider throttles requests.
- String values for `chunking_strategy`, `scraping_strategy`, and `table_extraction` are auto-resolved to class instances by the config loader.

---

## Environment Variables

| Variable | Purpose | Default |
|---|---|---|
| `CDP_URL` | Chrome DevTools Protocol endpoint URL | Not set (use crawl4ai built-in browser) |
| `C4A_LLM_PROVIDER` | LLM provider string (e.g., `openai/gpt-4o-mini`) | From `llm_config.json` |
| `C4A_LLM_API_KEY` | Explicit API key override | Auto-detect from standard env vars |
| `C4A_LLM_BASE_URL` | Custom LLM API base URL | From `llm_config.json` |
| `C4A_PROXY` | Proxy URL for browser requests | Not set |
| `C4A_CONFIG_DIR` | Override path to config directory | `<skill_dir>/references/config/` |
| `OPENAI_API_KEY` | OpenAI API key (auto-detected) | — |
| `ANTHROPIC_API_KEY` | Anthropic API key (auto-detected) | — |
| `GROQ_API_KEY` | Groq API key (auto-detected) | — |
| `GEMINI_API_KEY` / `GOOGLE_API_KEY` | Gemini API key (auto-detected) | — |
| `DEEPSEEK_API_KEY` | DeepSeek API key (auto-detected) | — |

---

## Anthropic Compatibility Mapping

### web-search tool result format

```
Anthropic format:
{
  "type": "web_search_result",
  "url": "https://example.com/page",
  "title": "Page Title",
  "page_age": "2024-01-01",    # from result.metadata if available
  "snippet": "First 200 chars of markdown..."
}
```

Crawl4AI → Anthropic mapping:
- `result.url` → `url`
- `result.metadata.get("title", "")` → `title`
- `result.metadata.get("modification_date", "")` or crawl date → `page_age`
- `result.markdown[:200]` → `snippet`

### web-fetch tool result format

```
Anthropic format:
{
  "type": "web_fetch_result",
  "url": "https://example.com/page",
  "title": "Page Title",
  "content": "Full markdown content..."
}
```

Crawl4AI → Anthropic mapping:
- `result.url` → `url`
- `result.metadata.get("title", "")` → `title`
- `result.markdown` or `result.markdown.fit_markdown` → `content`

---

## SKILL.md Outline

The SKILL.md will follow this structure:

1. **Frontmatter** — name, description (with trigger phrases)
2. **Workflow** — Step-by-step flow for each crawling mode
3. **Environment Setup** — How to install crawl4ai, set env vars
4. **Safety Rules** — No destructive ops, respect robots.txt, rate limiting, no key echoing
5. **Configuration** — How default config files work, how to override
6. **Simple Crawling** — Usage patterns with `simple_crawl.py`
7. **Deep Crawling** — Usage patterns with `deep_crawl.py`, mandatory max_depth/max_pages
8. **URL Seeding** — Usage patterns with `url_seed_crawl.py`
9. **Domain Mapping** — Usage patterns with `domain_map.py`
10. **Batch Crawling** — Usage patterns with `batch_crawl.py`
11. **Anthropic Compatibility** — How to use the adapter for web-search/web-fetch
12. **Troubleshooting** — Common issues and fixes

---

## Assumptions and Defaults

- Crawl4AI version target: **v0.8.x** (latest stable, uses `BrowserConfig`/`CrawlerRunConfig`/`LLMConfig` from `crawl4ai.async_configs`).
- Python 3.10+ required (async context managers, type hints).
- Scripts are executable via `python scripts/<name>.py` from the skill directory.
- Output files default to the current working directory, not the skill directory.
- Deep crawling always requires explicit `max_depth` and `max_pages` — no defaults that could cause unbounded crawls.
- The `fit_markdown` variant is opt-in (via `--fit-markdown` flag or config); `raw_markdown` is the default export.
- Config files use JSON (not YAML) for simplicity and to avoid extra dependencies.
- The old skill's `tests/` directory is not carried forward; validation is done via `quick_validate.py` per skill-creator conventions.
- `cache_cdp_connection` is enabled by default in the BrowserConfig class-level defaults when using CDP, to avoid reconnecting on every crawl.

---

## Test Plan

| Scenario | Validation |
|---|---|
| Simple crawl of `example.com` | Markdown file generated, contains expected content |
| Deep crawl with `max_depth=1, max_pages=5` | Index + individual markdown files created, no more than 5 pages |
| Deep crawl without `max_depth` | Script prompts for missing parameters |
| URL seeding of `realpython.com` with `pattern="*/courses/*"` | JSON file with filtered URLs generated |
| Domain mapping of a small domain | JSON + optional markdown index generated |
| CDP_URL not set | Falls back to `browser_mode="dedicated"`, headless crawl succeeds |
| CDP_URL set to invalid endpoint | Graceful error, clear message about CDP connection failure |
| `C4A_LLM_PROVIDER=anthropic/claude-3-5-sonnet-20241022` | LLM extraction uses Anthropic provider with auto-detected key |
| Anthropic adapter on crawl results | Output matches Anthropic web-search/web-fetch schema |
| Config file override | Custom `crawler_config.json` values take effect |
| Batch crawl with 3 URLs | All 3 markdown files + summary JSON generated |

---

## Out of Scope

- Docker deployment patterns for crawl4ai.
- Crawl4AI Cloud API integration.
- C4A-Script support.
- Real-time streaming to Codex chat (results are file-based).
- Automatic retry with exponential backoff (users can add via config).
- PDF export (markdown only per requirements).
