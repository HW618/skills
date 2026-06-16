#!/usr/bin/env python3
"""Shared configuration loader for crawl4ai skill scripts.

Reads default JSON configs from references/config/, merges with environment
variables and CLI overrides, and returns ready-to-use BrowserConfig,
CrawlerRunConfig, and LLMConfig objects.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

SKILL_DIR = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_DIR = SKILL_DIR / "references" / "config"

# ---------------------------------------------------------------------------
# Provider → env-var mapping for auto-detecting API keys
# ---------------------------------------------------------------------------
PROVIDER_KEY_MAP = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "groq": "GROQ_API_KEY",
    "gemini": "GEMINI_API_KEY",
    "google": "GOOGLE_API_KEY",
    "deepseek": "DEEPSEEK_API_KEY",
    # ollama needs no key
}


def _load_json(path: Path) -> dict:
    """Load a JSON file, returning empty dict on failure."""
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def resolve_config_dir(override: str | None = None) -> Path:
    """Return the config directory path."""
    if override:
        return Path(override)
    env_dir = os.environ.get("C4A_CONFIG_DIR")
    if env_dir:
        return Path(env_dir)
    return DEFAULT_CONFIG_DIR


# ---------------------------------------------------------------------------
# Strategy name → class mapping for crawler_config.json string values
# ---------------------------------------------------------------------------
STRATEGY_MAP = {
    "RegexChunking": "crawl4ai.chunking_strategy.RegexChunking",
    "LXMLWebScrapingStrategy": "crawl4ai.content_scraping_strategy.LXMLWebScrapingStrategy",
    "DefaultTableExtraction": "crawl4ai.table_extraction.DefaultTableExtraction",
}

# Map from crawl4ai.async_configs so match_mode resolution works
_MATCH_MODE_MODULE = "crawl4ai.async_configs"
_MATCH_MODE_CLASS = "MatchMode"
_CACHE_MODE_MODULE = "crawl4ai.cache_context"
_CACHE_MODE_CLASS = "CacheMode"


def _resolve_strategy_value(val):
    """If val is a string matching a known strategy name, import and return the class."""
    if isinstance(val, str) and val in STRATEGY_MAP:
        module_path, class_name = STRATEGY_MAP[val].rsplit(".", 1)
        try:
            mod = __import__(module_path, fromlist=[class_name])
            return getattr(mod, class_name)()
        except (ImportError, AttributeError):
            return None
    return val


def _clean_config(cfg: dict) -> dict:
    """Remove _doc keys, resolve strategy strings, drop None and empty-string values that would override defaults."""
    cleaned = {}
    for k, v in cfg.items():
        if k == "_doc":
            continue
        v = _resolve_strategy_value(v)
        # Skip None (use library default) and empty strings that would override meaningful defaults
        if v is not None and v != "":
            cleaned[k] = v
    return cleaned


def load_browser_config(config_dir: Path | None = None, **overrides) -> dict:
    """Load browser config JSON and apply env-var / override resolution."""
    config_dir = resolve_config_dir(config_dir) if config_dir else DEFAULT_CONFIG_DIR
    cfg = _load_json(config_dir / "browser_config.json")

    # CDP_URL auto-detection
    cdp_url = os.environ.get("CDP_URL")
    if cdp_url:
        cfg["browser_mode"] = "custom"
        cfg["cdp_url"] = cdp_url
        cfg["use_managed_browser"] = True

    # Proxy from env
    proxy = os.environ.get("C4A_PROXY")
    if proxy:
        cfg["proxy_config"] = {"server": proxy}

    # Apply explicit overrides last
    cfg.update({k: v for k, v in overrides.items() if v is not None})
    return cfg


def load_crawler_config(config_dir: Path | None = None, **overrides) -> dict:
    """Load crawler config JSON and apply overrides."""
    config_dir = resolve_config_dir(config_dir) if config_dir else DEFAULT_CONFIG_DIR
    cfg = _load_json(config_dir / "crawler_config.json")
    cfg.update({k: v for k, v in overrides.items() if v is not None})
    return cfg


def resolve_llm_provider() -> tuple[str, str | None]:
    """Return (provider_string, api_key) from environment."""
    provider = os.environ.get("C4A_LLM_PROVIDER", "")
    explicit_key = os.environ.get("C4A_LLM_API_KEY")
    if explicit_key:
        return provider, explicit_key

    # Auto-detect key from provider prefix
    if provider:
        prefix = provider.split("/")[0]
        env_var = PROVIDER_KEY_MAP.get(prefix)
        if env_var:
            return provider, os.environ.get(env_var)
    return provider, None


def load_llm_config(config_dir: Path | None = None, **overrides) -> dict:
    """Load LLM config JSON and apply env-var / override resolution."""
    config_dir = resolve_config_dir(config_dir) if config_dir else DEFAULT_CONFIG_DIR
    cfg = _load_json(config_dir / "llm_config.json")

    provider, api_key = resolve_llm_provider()
    if provider:
        cfg["provider"] = provider
    if api_key:
        cfg["api_token"] = api_key

    base_url = os.environ.get("C4A_LLM_BASE_URL")
    if base_url:
        cfg["base_url"] = base_url

    cfg.update({k: v for k, v in overrides.items() if v is not None})
    return cfg


def build_browser_config(config_dir: Path | None = None, **overrides):
    """Build a crawl4ai BrowserConfig from merged settings."""
    from crawl4ai.async_configs import BrowserConfig
    cfg = load_browser_config(config_dir, **overrides)
    filtered = _clean_config(cfg)
    return BrowserConfig(**filtered)


def build_crawler_config(config_dir: Path | None = None, **overrides):
    """Build a crawl4ai CrawlerRunConfig from merged settings."""
    from crawl4ai.async_configs import CrawlerRunConfig
    cfg = load_crawler_config(config_dir, **overrides)
    # Convert cache_mode string to enum
    if "cache_mode" in cfg and isinstance(cfg["cache_mode"], str):
        import crawl4ai.cache_context as _cc
        cfg["cache_mode"] = _cc.CacheMode[cfg["cache_mode"]]
    # Convert match_mode string to enum
    if "match_mode" in cfg and isinstance(cfg["match_mode"], str):
        import crawl4ai.async_configs as _ac
        cfg["match_mode"] = _ac.MatchMode[cfg["match_mode"]]
    filtered = _clean_config(cfg)
    return CrawlerRunConfig(**filtered)


def build_llm_config(config_dir: Path | None = None, **overrides):
    """Build a crawl4ai LLMConfig from merged settings."""
    from crawl4ai.async_configs import LLMConfig
    cfg = load_llm_config(config_dir, **overrides)
    filtered = _clean_config(cfg)
    return LLMConfig(**filtered)


def sanitize_domain(url: str) -> str:
    """Extract and sanitize a domain from a URL for use in filenames."""
    from urllib.parse import urlparse
    parsed = urlparse(url if "://" in url else f"https://{url}")
    domain = parsed.hostname or url
    return "".join(c if c.isalnum() or c in "-_" else "_" for c in domain)[:80]


def timestamp() -> str:
    """Return a compact timestamp for filenames."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def write_markdown(path: Path, url: str, title: str, content: str, depth: int | None = None):
    """Write a markdown file with metadata header."""
    header_lines = [
        f"<!--",
        f"  url: {url}",
        f"  title: {title}",
        f"  crawled: {datetime.now().isoformat()}",
    ]
    if depth is not None:
        header_lines.append(f"  depth: {depth}")
    header_lines.append(f"-->")
    header_lines.append("")
    header_lines.append(f"# {title}")
    header_lines.append("")
    header = "\n".join(header_lines)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(header + content, encoding="utf-8")
