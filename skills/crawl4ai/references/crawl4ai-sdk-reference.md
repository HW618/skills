# Crawl4AI v0.8.9 SDK Reference (Full Parameters)

**Source:** https://docs.crawl4ai.com/api/parameters/ — verified against installed v0.8.9

## Table of Contents

1. [Installation](#installation)
2. [BrowserConfig](#browserconfig)
3. [CrawlerRunConfig](#crawlerrunconfig)
4. [LLMConfig](#llmconfig)
5. [CrawlResult](#crawlresult)
6. [Deep Crawling](#deep-crawling)
7. [URL Seeding](#url-seeding)
8. [Domain Mapping](#domain-mapping)
9. [Content Extraction](#content-extraction)
10. [Markdown Generation](#markdown-generation)
11. [Session Management](#session-management)

---

## Installation

```bash
pip install crawl4ai
crawl4ai-setup
crawl4ai-doctor  # verify
```

## BrowserConfig

Controls browser launch and behavior. Import: `from crawl4ai.async_configs import BrowserConfig`

### Full Parameters (44 params)

| Parameter | Type / Default | Description |
|---|---|---|
| `browser_type` | `str` (default: `"chromium"`) | Browser engine: `"chromium"`, `"firefox"`, `"webkit"` |
| `headless` | `bool` (default: `True`) | No visible UI |
| `browser_mode` | `str` (default: `"dedicated"`) | How browser is initialized: `"dedicated"`, `"builtin"`, `"custom"`, `"docker"` |
| `use_managed_browser` | `bool` (default: `False`) | Launch browser via CDP; auto-set by browser_mode |
| `cdp_url` | `str` or `None` (default: `None`) | CDP endpoint URL, e.g. `"ws://localhost:9222/devtools/browser/"` |
| `browser_context_id` | `str` or `None` (default: `None`) | Existing browser context to connect to |
| `target_id` | `str` or `None` (default: `None`) | Specific browser target to connect to |
| `cdp_cleanup_on_close` | `bool` (default: `False`) | Clean up CDP connection on close |
| `cdp_close_delay` | `float` (default: `1.0`) | Delay before closing CDP connection |
| `cache_cdp_connection` | `bool` (default: `False`) | Reuse CDP connection across crawls |
| `create_isolated_context` | `bool` (default: `False`) | Create isolated browser context for each crawl |
| `use_persistent_context` | `bool` (default: `False`) | Persistent browser context across runs; also sets `use_managed_browser=True` |
| `user_data_dir` | `str` or `None` (default: `None`) | Directory for user data (profiles, cookies) |
| `chrome_channel` | `str` (default: `"chromium"`) | Chrome channel: `"chromium"`, `"chrome"`, `"msedge"` |
| `channel` | `str` (default: `"chromium"`) | Alias for chrome_channel |
| `proxy` | `str` or `None` (default: `None`) | Proxy URL (deprecated; use proxy_config) |
| `proxy_config` | `ProxyConfig` or `dict` or `None` (default: `None`) | Proxy settings: `{"server": "...", "username": "...", "password": "..."}` |
| `viewport_width` | `int` (default: `1080`) | Page width in px |
| `viewport_height` | `int` (default: `600`) | Page height in px |
| `viewport` | `dict` or `None` (default: `None`) | Viewport dimensions dict; overrides viewport_width/height |
| `device_scale_factor` | `float` (default: `1.0`) | Device pixel ratio. Use 2.0 for Retina screenshots |
| `accept_downloads` | `bool` (default: `False`) | Allow file downloads; requires downloads_path |
| `downloads_path` | `str` or `None` (default: `None`) | Directory to store downloaded files |
| `storage_state` | `str` or `dict` or `None` (default: `None`) | In-memory storage state (cookies, localStorage) to restore |
| `ignore_https_errors` | `bool` (default: `True`) | Continue despite invalid certificates |
| `java_script_enabled` | `bool` (default: `True`) | Disable for no JS overhead / static content only |
| `sleep_on_close` | `bool` (default: `False`) | Add delay when closing browser |
| `verbose` | `bool` (default: `True`) | Print browser logs |
| `cookies` | `list` or `None` (default: `None`) | Pre-set cookies, e.g. `[{"name": "session", "value": "...", "url": "..."}]` |
| `headers` | `dict` or `None` (default: `None`) | Extra HTTP headers, e.g. `{"Accept-Language": "en-US"}` |
| `user_agent` | `str` (default: `"Mozilla/5.0 ..."`) | Custom user agent string |
| `user_agent_mode` | `str` (default: `""`) | Set `"random"` to randomize UA from a pool |
| `user_agent_generator_config` | `dict` (default: `{}`) | Config for user agent generation when user_agent_mode="random" |
| `text_mode` | `bool` (default: `False`) | Disable images/heavy content for speed |
| `light_mode` | `bool` (default: `False`) | Disable some background features for performance |
| `extra_args` | `list` or `None` (default: `None`) | Additional browser flags, e.g. `["--disable-extensions"]` |
| `debugging_port` | `int` (default: `9222`) | Browser debugging port |
| `host` | `str` (default: `"localhost"`) | Browser connection host |
| `enable_stealth` | `bool` (default: `False`) | Enable playwright-stealth; cannot use with browser_mode="builtin" |
| `avoid_ads` | `bool` (default: `False`) | Block ad/tracker domains |
| `avoid_css` | `bool` (default: `False`) | Block CSS loading for faster text-only crawls |
| `init_scripts` | `list[str]` or `None` (default: `None`) | Scripts to run on page init |
| `memory_saving_mode` | `bool` (default: `False`) | Reduce browser memory footprint |
| `max_pages_before_recycle` | `int` (default: `0`) | Recycle browser after N pages (0 = no limit) |

### Class-Level Defaults

```python
BrowserConfig.set_defaults(cache_cdp_connection=True, cdp_close_delay=0, create_isolated_context=True)
BrowserConfig.get_defaults()
BrowserConfig.reset_defaults("cdp_close_delay")
```

Resolution order: explicit arg > class-level default > hardcoded default.

---

## CrawlerRunConfig

Controls each crawl run. Import: `from crawl4ai.async_configs import CrawlerRunConfig`

### A) Content Processing

| Parameter | Type / Default | Description |
|---|---|---|
| `word_count_threshold` | `int` (default: `1`) | Min words per text block |
| `extraction_strategy` | `ExtractionStrategy` or `None` | Structured data extraction (CSS/LLM/etc.) |
| `chunking_strategy` | `ChunkingStrategy` (default: `RegexChunking()`) | Chunking before extraction |
| `markdown_generator` | `MarkdownGenerationStrategy` (default: `DefaultMarkdownGenerator()`) | Specialized markdown output |
| `css_selector` | `str` or `None` | Retain only matching part of page |
| `target_elements` | `list[str]` or `None` | CSS selectors for focused extraction while still processing full page |
| `excluded_tags` | `list` or `None` | Remove entire tags, e.g. `["script", "style"]` |
| `excluded_selector` | `str` or `None` | CSS selector to exclude, e.g. `"#ads, .tracker"` |
| `only_text` | `bool` (default: `False`) | Extract text-only content |
| `prettiify` | `bool` (default: `False`) | Beautify final HTML (note: triple-i spelling) |
| `keep_data_attributes` | `bool` (default: `False`) | Preserve data-* attributes in cleaned HTML |
| `keep_attrs` | `list` or `None` | HTML attributes to keep, e.g. `["id", "class"]` |
| `remove_forms` | `bool` (default: `False`) | Remove all `<form>` elements |
| `parser_type` | `str` (default: `"lxml"`) | HTML parser |
| `scraping_strategy` | `ContentScrapingStrategy` or `None` | Scraping strategy; default is LXMLWebScrapingStrategy internally |

### B) Browser Location and Identity

| Parameter | Type / Default | Description |
|---|---|---|
| `locale` | `str` or `None` | Browser locale, e.g. `"en-US"` |
| `timezone_id` | `str` or `None` | Browser timezone, e.g. `"America/New_York"` |
| `geolocation` | `GeolocationConfig` or `None` | GPS coordinates: `GeolocationConfig(latitude=..., longitude=..., accuracy=...)` |
| `fetch_ssl_certificate` | `bool` (default: `False`) | Include SSL certificate info in result |
| `proxy_config` | `ProxyConfig`, `list[ProxyConfig]`, `dict`, `str`, or `None` | Proxy for this specific crawl |
| `proxy_rotation_strategy` | `ProxyRotationStrategy` or `None` | Strategy for proxy rotation |
| `proxy_session_id` | `str` or `None` | Proxy session identifier |
| `proxy_session_ttl` | `int` or `None` | Proxy session TTL in seconds |
| `proxy_session_auto_release` | `bool` (default: `False`) | Auto-release proxy sessions |
| `max_retries` | `int` (default: `0`) | Retry rounds when anti-bot detected |
| `fallback_fetch_function` | `async (str) -> str` or `None` | Last-resort fetch after all retries |

### C) Caching and Session

| Parameter | Type / Default | Description |
|---|---|---|
| `cache_mode` | `CacheMode` (default: `CacheMode.BYPASS`) | ENABLED, BYPASS, DISABLED, etc. |
| `session_id` | `str` or `None` | Reuse browser session across arun() calls |
| `bypass_cache` | `bool` (default: `False`, deprecated) | Use cache_mode instead |
| `disable_cache` | `bool` (default: `False`, deprecated) | Use cache_mode instead |
| `no_cache_read` | `bool` (default: `False`, deprecated) | Use cache_mode instead |
| `no_cache_write` | `bool` (default: `False`, deprecated) | Use cache_mode instead |
| `shared_data` | `dict` or `None` | Data shared between hooks across crawl operations |
| `check_cache_freshness` | `bool` (default: `False`) | Verify cached content is still fresh |
| `cache_validation_timeout` | `float` (default: `10.0`) | Timeout for cache freshness check |

### D) Page Navigation and Timing

| Parameter | Type / Default | Description |
|---|---|---|
| `wait_until` | `str` (default: `"domcontentloaded"`) | Navigation completion condition; often `"networkidle"` |
| `page_timeout` | `int` (default: `60000`) | Timeout for page navigation/JS steps in ms |
| `wait_for` | `str` or `None` | CSS (`"css:selector"`) or JS (`"js:() => bool"`) condition |
| `wait_for_timeout` | `int` or `None` | Specific timeout for wait_for in ms |
| `wait_for_images` | `bool` (default: `False`) | Wait for images to load |
| `delay_before_return_html` | `float` (default: `0.1`) | Pause before final HTML capture |
| `check_robots_txt` | `bool` (default: `False`) | Respect robots.txt rules |
| `mean_delay` | `float` (default: `0.1`) | Random delay between arun_many() crawls |
| `max_range` | `float` (default: `0.3`) | Random delay range for arun_many() |
| `semaphore_count` | `int` (default: `5`) | Max concurrency for arun_many() |

### E) Page Interaction

| Parameter | Type / Default | Description |
|---|---|---|
| `js_code` | `str` or `list[str]` or `None` | JavaScript to run after wait_for |
| `js_code_before_wait` | `str` or `list[str]` or `None` | JavaScript to run before wait_for |
| `c4a_script` | `str` or `list[str]` or `None` | C4A script that compiles to JavaScript |
| `js_only` | `bool` (default: `False`) | Reuse session, only apply JS; no full reload |
| `ignore_body_visibility` | `bool` (default: `True`) | Skip checking if body is visible |
| `scan_full_page` | `bool` (default: `False`) | Auto-scroll for infinite scroll content |
| `scroll_delay` | `float` (default: `0.2`) | Delay between scroll steps |
| `max_scroll_steps` | `int` or `None` | Max scroll steps during full page scan |
| `process_iframes` | `bool` (default: `False`) | Inline iframe content |
| `flatten_shadow_dom` | `bool` (default: `False`) | Flatten Shadow DOM into light DOM |
| `remove_overlay_elements` | `bool` (default: `False`) | Remove modals/popups |
| `remove_consent_popups` | `bool` (default: `False`) | Remove GDPR/cookie consent popups (OneTrust, Cookiebot, etc.) |
| `simulate_user` | `bool` (default: `False`) | Simulate mouse movements for bot avoidance |
| `override_navigator` | `bool` (default: `False`) | Override navigator properties in JS |
| `magic` | `bool` (default: `False`) | Automatic popup/consent handling (experimental) |
| `adjust_viewport_to_content` | `bool` (default: `False`) | Resize viewport to match content height |

### F) Media Handling

| Parameter | Type / Default | Description |
|---|---|---|
| `screenshot` | `bool` (default: `False`) | Capture screenshot (base64) |
| `screenshot_wait_for` | `float` or `None` | Extra wait before screenshot |
| `screenshot_height_threshold` | `int` (default: `10000`) | Threshold for alternate screenshot strategies |
| `force_viewport_screenshot` | `bool` (default: `False`) | Viewport-only screenshot |
| `pdf` | `bool` (default: `False`) | Capture PDF |
| `capture_mhtml` | `bool` (default: `False`) | Capture MHTML snapshot |
| `image_description_min_word_threshold` | `int` (default: `1`) | Min words for image alt/description |
| `image_score_threshold` | `int` (default: `2`) | Filter low-scoring images |
| `exclude_external_images` | `bool` (default: `False`) | Exclude images from other domains |
| `exclude_all_images` | `bool` (default: `False`) | Exclude all images |
| `table_score_threshold` | `int` (default: `7`) | Min score for table processing |
| `table_extraction` | `TableExtractionStrategy` or `None` | Table extraction strategy |

### G) Link/Domain Handling

| Parameter | Type / Default | Description |
|---|---|---|
| `exclude_social_media_domains` | `list` or `None` | Remove links to these domains |
| `exclude_external_links` | `bool` (default: `False`) | Remove all external links |
| `exclude_social_media_links` | `bool` (default: `False`) | Remove social media links |
| `exclude_domains` | `list` or `None` | Custom list of domains to exclude |
| `exclude_internal_links` | `bool` (default: `False`) | Remove internal links |
| `score_links` | `bool` (default: `False`) | Calculate quality scores for links |
| `preserve_https_for_internal_links` | `bool` (default: `False`) | Preserve HTTPS for internal links |

### H) Debug, Logging & Network

| Parameter | Type / Default | Description |
|---|---|---|
| `verbose` | `bool` (default: `True`) | Print crawl logs |
| `log_console` | `bool` (default: `False`) | Log page JS console output |
| `capture_network_requests` | `bool` (default: `False`) | Capture network requests in result |
| `capture_console_messages` | `bool` (default: `False`) | Capture console messages in result |

### I) Connection & HTTP

| Parameter | Type / Default | Description |
|---|---|---|
| `method` | `str` (default: `"GET"`) | HTTP method for AsyncHTTPCrawlerStrategy |
| `stream` | `bool` (default: `False`) | Enable streaming for arun_many() |
| `prefetch` | `bool` (default: `False`) | Prefetch linked resources |
| `process_in_browser` | `bool` (default: `False`) | Process content in browser context |
| `url` | `str` or `None` | URL for this config; used internally |
| `base_url` | `str` or `None` | Base URL for resolving relative URLs |
| `user_agent` | `str` or `None` | Override browser-level UA for this crawl |
| `user_agent_mode` | `str` or `None` | Override browser-level UA mode |
| `user_agent_generator_config` | `dict` (default: `{}`) | Config for UA generation |

### J) Virtual Scroll

| Parameter | Type / Default | Description |
|---|---|---|
| `virtual_scroll_config` | `VirtualScrollConfig` or `dict` or `None` | Config for virtualized scrolling (Twitter/Instagram) |

`VirtualScrollConfig` fields: `container_selector` (str, required), `scroll_count` (int, 10), `scroll_by` (str or int, "container_height"), `wait_after_scroll` (float, 0.5).

### K) URL Matching

| Parameter | Type / Default | Description |
|---|---|---|
| `url_matcher` | `str`, `Callable`, `list`, or `None` | Pattern(s) to match URLs; string (glob), function, or list |
| `match_mode` | `MatchMode` (default: `MatchMode.OR`) | OR (any match) or AND (all must match) |

### L) Advanced Crawling

| Parameter | Type / Default | Description |
|---|---|---|
| `deep_crawl_strategy` | `DeepCrawlStrategy` or `None` | Strategy for recursive deep crawling |
| `link_preview_config` | `LinkPreviewConfig` or `dict` or `None` | Config for link head extraction and scoring |
| `experimental` | `dict` or `None` | Experimental/beta features |

### Helper Methods

```python
# Clone with modifications
stream_cfg = run_cfg.clone(stream=True, cache_mode=CacheMode.BYPASS)

# Class-level defaults
CrawlerRunConfig.set_defaults(verbose=False, cache_mode=CacheMode.BYPASS)
CrawlerRunConfig.get_defaults()
CrawlerRunConfig.reset_defaults("verbose")
```

---

## LLMConfig

Configures LLM provider. Import: `from crawl4ai.async_configs import LLMConfig`

### Full Parameters (13 params)

| Parameter | Type / Default | Description |
|---|---|---|
| `provider` | `str` (default: `"openai/gpt-4o"`) | Provider string in `provider/model` format |
| `api_token` | `str` or `None` | API key; auto-read from env if not provided (e.g. `GEMINI_API_KEY` for gemini). Also supports `"env:VAR_NAME"` prefix |
| `base_url` | `str` or `None` | Custom API endpoint |
| `temperature` | `float` or `None` | Sampling temperature |
| `max_tokens` | `int` or `None` | Max tokens in response |
| `top_p` | `float` or `None` | Nucleus sampling parameter |
| `frequency_penalty` | `float` or `None` | Penalize frequent tokens |
| `presence_penalty` | `float` or `None` | Penalize present tokens |
| `stop` | `list[str]` or `None` | Stop sequences |
| `n` | `int` or `None` | Number of completions |
| `backoff_base_delay` | `int` or `None` | Seconds before first retry on throttle |
| `backoff_max_attempts` | `int` or `None` | Total tries (initial + retries) before error |
| `backoff_exponential_factor` | `int` or `None` | Multiplier for wait increase: `delay = base_delay * factor^attempt` |

Supported providers: `openai`, `anthropic`, `groq`, `gemini`, `deepseek`, `ollama`.

### Example

```python
llm_config = LLMConfig(
    provider="openai/gpt-4o-mini",
    api_token=os.getenv("OPENAI_API_KEY"),
    temperature=0.3,
    max_tokens=4096,
    backoff_base_delay=1,
    backoff_max_attempts=5,
    backoff_exponential_factor=3,
)
```

---

## CrawlResult

| Field | Type | Description |
|---|---|---|
| `url` | `str` | The crawled URL |
| `html` | `str` | Raw HTML |
| `cleaned_html` | `str` | Cleaned HTML |
| `markdown` | `MarkdownResult` or `str` | `.raw_markdown`, `.fit_markdown` |
| `media` | `dict` | `{"images": [...], "videos": [...]}` |
| `links` | `dict` | `{"internal": [...], "external": [...]}` |
| `metadata` | `dict` | `title`, `description`, etc. |
| `success` | `bool` | Whether crawl succeeded |
| `status_code` | `int` | HTTP status code |
| `error_message` | `str` | Error if failed |
| `screenshot` | `str` or `bytes` | Base64 or raw screenshot |
| `pdf` | `bytes` or `None` | PDF data if captured |
| `mhtml` | `str` or `None` | MHTML snapshot if captured |
| `extracted_content` | `str` | JSON string from extraction strategy |
| `session_id` | `str` | Session identifier |
| `ssl_certificate` | `dict` or `None` | SSL cert info if fetch_ssl_certificate=True |
| `captured_requests` | `list` | Network requests if capture_network_requests=True |
| `console_messages` | `list` | Console messages if capture_console_messages=True |

---

## Deep Crawling

Import strategies from `crawl4ai.deep_crawling`:

```python
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy, DFSDeepCrawlStrategy, BestFirstCrawlingStrategy
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer
from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter
```

### BFSDeepCrawlStrategy

Breadth-first. Params: `max_depth`, `max_pages`, `include_external`, `filter_chain`, `url_scorer`, `score_threshold`.

### DFSDeepCrawlStrategy

Depth-first. Same params as BFS.

### BestFirstCrawlingStrategy

Prioritizes by scorer. Requires `url_scorer`.

### Streaming

```python
config = CrawlerRunConfig(deep_crawl_strategy=strategy, stream=True)
async for result in await crawler.arun(url, config=config):
    process(result)
```

---

## URL Seeding

```python
from crawl4ai import AsyncUrlSeeder, SeedingConfig

seeder = AsyncUrlSeeder()
config = SeedingConfig(source="sitemap+cc", pattern="*/docs/*", extract_head=True, max_urls=100)
urls = await seeder.urls("example.com", config)
```

### SeedingConfig Parameters

| Parameter | Type / Default | Description |
|---|---|---|
| `source` | `str` (default: `"sitemap+cc"`) | Discovery source: `"sitemap"`, `"cc"`, `"sitemap+cc"` |
| `pattern` | `str` or `None` (default: `"*"`) | URL pattern filter |
| `live_check` | `bool` (default: `False`) | Verify URLs are live |
| `extract_head` | `bool` (default: `False`) | Extract page metadata |
| `max_urls` | `int` (default: `-1`) | Max URLs to return (-1 = unlimited) |
| `concurrency` | `int` (default: `1000`) | Concurrency for seeding |
| `hits_per_sec` | `int` (default: `5`) | Rate limit |
| `force` | `bool` (default: `False`) | Force re-seed even if cached |
| `base_directory` | `str` or `None` | Cache directory |
| `llm_config` | `LLMConfig` or `None` | LLM for intelligent filtering |
| `verbose` | `bool` or `None` | Verbose output |
| `query` | `str` or `None` | Search query for relevance filtering |
| `score_threshold` | `float` or `None` | Min relevance score |
| `scoring_method` | `str` (default: `"bm25"`) | Scoring method |
| `filter_nonsense_urls` | `bool` (default: `True`) | Filter out non-page URLs |
| `cache_ttl_hours` | `int` (default: `24`) | Cache TTL |
| `validate_sitemap_lastmod` | `bool` (default: `True`) | Validate sitemap lastmod |

---

## Domain Mapping

```python
from crawl4ai import DomainMapper, DomainMapperConfig

config = DomainMapperConfig(source="sitemap+cc+crt+probe")
async with DomainMapper() as mapper:
    results = await mapper.scan("example.com", config=config)
```

8 sources: `sitemap`, `cc`, `wayback`, `crt`, `probe`, `robots`, `feed`, `homepage`. Combine with `+`.

### DomainMapperConfig Parameters

| Parameter | Type / Default | Description |
|---|---|---|
| `source` | `str` (default: `"sitemap+cc+crt+probe"`) | Discovery sources |
| `max_urls` | `int` (default: `-1`) | Max URLs (-1 = unlimited) |
| `concurrency` | `int` (default: `50`) | Concurrency |
| `hits_per_sec` | `int` (default: `10`) | Rate limit |
| `force` | `bool` (default: `False`) | Force re-scan |
| `extract_head` | `bool` (default: `True`) | Extract page metadata |
| `filter_nonsense_urls` | `bool` (default: `True`) | Filter non-page URLs |
| `soft_404_detection` | `bool` (default: `True`) | Detect soft 404s |
| `query` | `str` or `None` | Search query for relevance |
| `score_threshold` | `float` or `None` | Min relevance score |
| `scoring_method` | `str` (default: `"bm25"`) | Scoring method |
| `probe_paths` | `list[str]` or `None` | Additional paths to probe |
| `common_subdomains` | `list[str]` or `None` | Subdomains to check |
| `include_subdomains` | `bool` (default: `True`) | Include subdomains |
| `source_timeout` | `float` (default: `30.0`) | Per-source timeout |
| `use_browser_for_homepage` | `bool` (default: `False`) | Use browser for homepage discovery |
| `verbose` | `bool` or `None` | Verbose output |
| `cache_ttl_hours` | `int` (default: `24`) | Cache TTL |
| `base_directory` | `str` or `None` | Cache directory |
| `dns_timeout` | `float` (default: `3.0`) | DNS timeout |
| `http_timeout` | `float` (default: `10.0`) | HTTP timeout |

---

## Content Extraction

### CSS-based (no LLM)

```python
from crawl4ai import JsonCssExtractionStrategy

schema = {"name": "items", "baseSelector": "div.product", "fields": [...]}
strategy = JsonCssExtractionStrategy(schema=schema)
```

### LLM-based

```python
from crawl4ai import LLMExtractionStrategy, LLMConfig

strategy = LLMExtractionStrategy(
    llm_config=LLMConfig(provider="openai/gpt-4o-mini", api_token="key"),
    instruction="Extract product names and prices",
    extraction_type="schema",
    schema=MyPydanticModel.model_json_schema(),
)
```

---

## Markdown Generation

```python
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter

# Pruning filter
generator = DefaultMarkdownGenerator(content_filter=PruningContentFilter(threshold=0.48, threshold_type="fixed"))

# BM25 relevance filter
generator = DefaultMarkdownGenerator(content_filter=BM25ContentFilter(user_query="machine learning", bm25_threshold=1.0))

config = CrawlerRunConfig(markdown_generator=generator)
result.markdown.raw_markdown   # Full
result.markdown.fit_markdown   # Filtered
```

---

## Session Management

```python
# Login
login_cfg = CrawlerRunConfig(session_id="my_session", js_code="...", wait_for="css:.dashboard")
await crawler.arun("https://site.com/login", config=login_cfg)

# Reuse
cfg = CrawlerRunConfig(session_id="my_session")
await crawler.arun("https://site.com/protected", config=cfg)
```
