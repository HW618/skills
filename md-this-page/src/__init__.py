"""md-this-page-skill 核心包"""

from .crawler import (crawl, crawl_page, is_valid_cdp, build_markdown_generator,
                      MARKDOWN_OPTIONS, CrawlResult, get_cdp_url, DEFAULT_CDP_URL)
from .converter import convert_to_markdown, extract_summary
from .strategies import SITE_STRATEGIES, SiteStrategy, detect_strategy

__all__ = [
    "crawl", "crawl_page", "is_valid_cdp", "build_markdown_generator",
    "MARKDOWN_OPTIONS", "CrawlResult", "get_cdp_url", "DEFAULT_CDP_URL",
    "convert_to_markdown", "extract_summary",
    "SITE_STRATEGIES", "SiteStrategy", "detect_strategy",
]
