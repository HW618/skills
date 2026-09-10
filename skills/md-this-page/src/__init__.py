"""md-this-page-skill 核心包"""

from .crawler import (crawl, crawl_page, cdp_reachable, build_markdown_generator,
                      MARKDOWN_OPTIONS, CrawlResult, get_cdp_url)
from .converter import convert_to_markdown, extract_summary
from .strategies import SITE_STRATEGIES, SiteStrategy, detect_strategy

__all__ = [
    "crawl", "crawl_page", "cdp_reachable", "build_markdown_generator",
    "MARKDOWN_OPTIONS", "CrawlResult", "get_cdp_url",
    "convert_to_markdown", "extract_summary",
    "SITE_STRATEGIES", "SiteStrategy", "detect_strategy",
]
