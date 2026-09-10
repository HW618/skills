"""
核心抓取模块：基于 crawl4ai，通过 CDP 连接外部浏览器。

浏览器连接优先级：
1. 启动时读取环境变量 CDP_URL（未设置则默认 http://127.0.0.1:9222），
   连接前探测该端点是否为「合规且可用」的 CDP 浏览器（GET /json/version 返回含 webSocketDebuggerUrl）
2. CDP_URL 无效 / 不可达 / 不是合规 CDP 浏览器 → 回退 crawl4ai 本地 headless 浏览器
   （本地内核未安装时会在抓取报错中提示运行 scripts/install_browser.py）

注意：只有"浏览器连接失败"才会触发回退；页面级错误（超时/链接失效/风控）不会重试，
避免无谓地耗时翻倍。
"""

import asyncio
import json
import logging
import os
import urllib.request
from dataclasses import dataclass

from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

from .strategies import SiteStrategy, detect_strategy

logger = logging.getLogger(__name__)

_META_DIV_CLASS = "mtp-meta"

# CDP_URL 未设置时默认探测的 CDP 端点
DEFAULT_CDP_URL = "http://127.0.0.1:9222"

# 正文长度低于该值视为"没抓到正文"，继续尝试下一个候选选择器
# （部分站点存在同名空占位元素，例如掘金的 .article-content 为空壳）
MIN_ACCEPT_CHARS = 400

# Markdown 生成选项（对全部站点统一生效）：
# bypass_tables=True 让表格以原始 HTML 输出，而不是转成 Markdown 管道表格 ——
# 合并单元格、单元格内多行/嵌套结构在管道表格里会被转坏，保留 HTML 可保证表格格式正确
# （Markdown 渲染器普遍支持 HTML 表格）。
MARKDOWN_OPTIONS = {"bypass_tables": True}


def build_markdown_generator() -> DefaultMarkdownGenerator:
    """按统一选项构建 Markdown 生成器（所有站点共用）"""
    return DefaultMarkdownGenerator(options=dict(MARKDOWN_OPTIONS))

# 出现这些关键字说明是浏览器/连接层面的问题，值得回退到本地浏览器重试
_BROWSER_ERROR_KEYWORDS = (
    "cdp", "connect", "connection", "target closed", "targetclosed",
    "browser", "playwright", "executable doesn't exist", "browsertype",
)


def get_cdp_url() -> str:
    """读取 CDP_URL 环境变量；未设置时返回默认 DEFAULT_CDP_URL（去除首尾空白与尾部斜杠）"""
    url = os.environ.get("CDP_URL", "").strip().rstrip("/")
    return url or DEFAULT_CDP_URL


def is_valid_cdp(cdp_url: str, timeout: float = 1.5) -> bool:
    """探测端点是否为「合规且可用」的 CDP 浏览器：
    GET /json/version 返回 200，且响应 JSON 含 webSocketDebuggerUrl 字段。
    非法 URL / 端口不通 / 非 CDP 服务，一律判为不可用（触发本地回退）。"""
    if not cdp_url.startswith(("http://", "https://")):
        return False
    try:
        with urllib.request.urlopen(f"{cdp_url}/json/version", timeout=timeout) as resp:
            if resp.status != 200:
                return False
            data = json.loads(resp.read().decode("utf-8", "ignore"))
            return bool(data.get("webSocketDebuggerUrl"))
    except Exception:
        return False


def _resolve_cdp_url() -> str | None:
    """决定本次抓取使用哪个浏览器：
    读取 CDP_URL（默认 127.0.0.1:9222），若为合规可用的 CDP 浏览器则用之，
    否则返回 None，回退本地 headless。"""
    cdp_url = get_cdp_url()
    if is_valid_cdp(cdp_url):
        logger.info(f"Using CDP browser: {cdp_url}")
        return cdp_url
    logger.info(f"CDP endpoint invalid/unreachable ({cdp_url}); using local headless browser")
    return None


def build_browser_config(cdp_url: str | None, verbose: bool = False) -> BrowserConfig:
    """CDP 模式复用浏览器默认上下文（带登录态，显著降低验证码概率）"""
    if cdp_url:
        return BrowserConfig(
            cdp_url=cdp_url,
            headless=False,                    # 连接已有浏览器时该值不生效
            user_agent_mode="random",
            use_managed_browser=True,
            cdp_cleanup_on_close=False,        # 绝不关闭用户的浏览器
            verbose=verbose,
        )
    return BrowserConfig(headless=True, user_agent_mode="random", verbose=verbose)


@dataclass
class CrawlResult:
    """一次抓取的标准化结果"""
    url: str
    html: str = ""                  # 正文区域 HTML（已清理）
    markdown: str = ""              # 正文 Markdown
    title: str = ""
    author: str = ""
    published_date: str = ""
    description: str = ""
    site_name: str = ""
    strategy: str = ""
    success: bool = False
    error: str = ""                 # 面向使用者的简短错误说明
    error_kind: str = ""            # "" | "page" | "browser"，供上层决定是否回退重试


def _short_error(err: object) -> str:
    """把 crawl4ai/playwright 的长堆栈压缩成一句可读说明"""
    text = " ".join(str(err).split())
    low = text.lower()
    if ("executable doesn't exist" in low or "browsertype.launch" in low
            or "playwright install" in low or "playwright-cli install" in low):
        return ("无可用浏览器：CDP 端点不可用，且本地 headless 浏览器内核未安装。"
                "请运行 python3 scripts/install_browser.py 安装本地浏览器；"
                "或启动一个 CDP 浏览器并设置 CDP_URL（默认探测 http://127.0.0.1:9222）。")
    if "Wait condition failed" in text or "Timeout" in text or "timeout" in text:
        return ("页面正文未在超时时间内出现。常见原因：链接已失效、需要登录、"
                "或站点触发风控。可加大 --timeout，或先在浏览器中确认该页面可正常打开。")
    if len(text) > 300:
        return text[:300] + " ..."
    return text


def _is_browser_error(err: object) -> bool:
    text = str(err).lower()
    return any(k in text for k in _BROWSER_ERROR_KEYWORDS)


def _clean_title(title: str, strategy: SiteStrategy) -> str:
    """去掉页面标题里的站点名后缀（如 'xxx - 简书'）"""
    t = title.strip()
    for suffix in strategy.title_suffixes:
        idx = t.find(suffix)
        if idx > 0:
            t = t[:idx].strip()
    return t


def _build_meta_inject_js(container_selector: str, strategy: SiteStrategy) -> str:
    """生成"元数据注入"JS：启用 css_selector 后 crawl4ai 只返回正文区域，
    页面级 title/author/date 会丢失，故在提取前将其写进正文容器内的隐藏元素。

    title 优先用 title_selector 定位的正文标题（更干净，通常不含站点名后缀），
    取不到再回退 document.title（仍会经 _clean_title 裁掉后缀）。"""
    return f"""
(() => {{
    const q = s => {{ const el = s ? document.querySelector(s) : null;
                      return el ? el.textContent.trim().slice(0, 200) : ''; }};
    const attr = v => (v || '').replace(/"/g, '&quot;');
    const container = document.querySelector('{container_selector}');
    if (!container || container.querySelector('.{_META_DIV_CLASS}')) return;
    const div = document.createElement('div');
    div.className = '{_META_DIV_CLASS}';
    div.style.display = 'none';
    div.setAttribute('data-title', attr(q('{strategy.title_selector or ""}') || document.title));
    div.setAttribute('data-author', attr(q('{strategy.author_selector or ""}')));
    div.setAttribute('data-date', attr(q('{strategy.date_selector or ""}')));
    container.insertBefore(div, container.firstChild);
}})()
"""


def _extract_injected_meta(html: str) -> dict:
    """从正文 HTML 中解析注入的元数据（解析失败不影响主流程）"""
    try:
        div = BeautifulSoup(html, "lxml").find(class_=_META_DIV_CLASS)
        if div:
            return {k: (div.get(f"data-{k}") or "") for k in ("title", "author", "date")}
    except Exception as e:
        logger.debug(f"meta parse failed: {e}")
    return {}


def _pick_meta(meta: dict, *keys: str) -> str:
    """从 crawl4ai 的 metadata 字典中按优先级取值"""
    for k in keys:
        v = meta.get(k)
        if v:
            return str(v).strip()
    return ""


def _dedupe_repeats(md: str, min_block: int = 300) -> str:
    """兜底：整篇正文被重复拼接时只保留一份。

    判定方式：以首行为锚点找到第二份的起点，若该位置起的内容正好是首份的整数倍重复，
    则判定为重复拼接。只在"整块重复"时生效，正常文章不会被误伤。
    """
    text = md.strip()
    if len(text) < min_block * 2:
        return md

    lines = text.split("\n")
    anchor = lines[0].strip()
    if not anchor:
        return md

    for i in range(1, len(lines)):
        if lines[i].strip() != anchor:
            continue
        head = "\n".join(lines[:i]).strip()
        rest = "\n".join(lines[i:]).strip()
        if len(head) < min_block or not rest.startswith(head):
            continue
        remainder = rest[len(head):].strip()
        while remainder.startswith(head):          # 处理 2 份以上
            remainder = remainder[len(head):].strip()
        if not remainder:
            logger.info(f"检测到正文重复约 {len(rest) // len(head) + 1} 次，已自动去重")
            return head
    return md


async def _crawl_once(url: str, strategy: SiteStrategy, cdp_url: str | None,
                      timeout_ms: int, verbose: bool = False,
                      css_selector: str | None = None) -> CrawlResult:
    """执行一次抓取；任何异常都转成带简短说明的 CrawlResult，便于上层直接展示。

    css_selector 为该次抓取实际使用的正文选择器（主选择器或某个备选）。
    """
    selector = strategy.css_selector if css_selector is None else css_selector
    run_cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        markdown_generator=build_markdown_generator(),   # 表格保留原始 HTML（bypass_tables）
        css_selector=selector,
        excluded_selector=strategy.excluded_selector,
        excluded_tags=["script", "style", "noscript", "iframe", "nav", "footer"],
        wait_for=strategy.wait_for,
        js_code=(strategy.js_snippets
                 + ([_build_meta_inject_js(selector, strategy)] if selector else [])) or None,
        page_timeout=timeout_ms,
        word_count_threshold=5,     # 过滤短碎文本节点
        verbose=verbose,
        log_console=verbose,        # 默认静默，避免 crawl4ai 日志污染 CLI 输出
    )
    out = CrawlResult(url=url, strategy=strategy.name)

    try:
        async with AsyncWebCrawler(config=build_browser_config(cdp_url, verbose)) as crawler:
            result = await crawler.arun(url=url, config=run_cfg)
    except Exception as e:
        out.error = _short_error(e)
        out.error_kind = "browser" if _is_browser_error(e) else "page"
        return out

    if not result.success:
        out.error = _short_error(result.error_message or "抓取失败")
        return out

    meta = dict(result.metadata or {})
    out.html = result.html or ""
    raw_md = str(result.markdown.raw_markdown) if result.markdown else ""
    out.markdown = _dedupe_repeats(raw_md)
    # css_selector 模式下 metadata 为空，改用注入的元数据
    injected = _extract_injected_meta(out.html) if selector else {}
    out.title = _clean_title(
        injected.get("title") or _pick_meta(meta, "title", "og:title"), strategy)
    out.description = _pick_meta(meta, "description", "og:description")
    out.author = injected.get("author") or _pick_meta(meta, "author", "article:author")
    out.published_date = injected.get("date") or _pick_meta(
        meta, "article:published_time", "date", "pubdate")
    out.site_name = _pick_meta(meta, "og:site_name", "source") or strategy.name
    out.success = bool(out.markdown or out.html)
    if not out.success:
        out.error = f"页面加载成功但未提取到正文（策略：{strategy.name}），可能页面结构已变化。"
    return out


def _content_selectors(strategy: SiteStrategy) -> list[str]:
    """主选择器 + 备选（按顺序重试）；无主选择器时返回空列表表示通用提取"""
    if not strategy.css_selector:
        return []
    return [strategy.css_selector, *strategy.css_selector_fallbacks]


async def crawl_page(url: str, timeout_ms: int = 45000,
                     cdp_url: str | None = None, verbose: bool = False) -> CrawlResult:
    """抓取单个页面，自动按 URL 选择站点策略。

    cdp_url 留空时按 CDP_URL 环境变量解析（未设置则默认 http://127.0.0.1:9222）；
    端点非合规 CDP 或连接失败时回退本地 headless 浏览器。

    正文选择器策略：按"主选择器 → 备选"逐个尝试，取到足够长的正文即采用；
    若都偏短（页面里存在同名空占位元素时会发生），则返回其中正文最长的一次。
    verbose=True 时输出 crawl4ai 的详细日志（调试用）。
    """
    strategy = detect_strategy(url)
    cdp = cdp_url if cdp_url is not None else _resolve_cdp_url()
    logger.info(f"crawl_page: {url} (strategy={strategy.name}, browser={'cdp' if cdp else 'local'})")

    selectors = _content_selectors(strategy) or [None]
    best: CrawlResult | None = None

    for sel in selectors:
        result = await _crawl_once(url, strategy, cdp, timeout_ms, verbose, sel)
        if result.error_kind == "browser" and cdp:
            logger.warning("CDP browser failed; retrying once with local headless browser")
            result = await _crawl_once(url, strategy, None, timeout_ms, verbose, sel)

        if result.success and len(result.markdown) >= MIN_ACCEPT_CHARS:
            if sel != selectors[0]:
                logger.info(f"已用备选选择器取得正文：{sel}")
            return result

        if best is None or len(result.markdown or "") > len(best.markdown or ""):
            best = result
        logger.info(f"选择器 {sel!r} 正文过短（{len(result.markdown or '')} 字符），继续尝试备选")

    return best


def crawl(url: str, timeout_ms: int = 45000, verbose: bool = False) -> CrawlResult:
    """同步入口（CLI 与一般脚本使用）；在已运行的事件循环中请改用 crawl_page"""
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(crawl_page(url, timeout_ms, verbose=verbose))
    raise RuntimeError("检测到运行中的事件循环，请在 async 环境中直接 await crawl_page()")
