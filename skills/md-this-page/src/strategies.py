"""
抓取策略定义：每种网站对应一个 SiteStrategy，全部集中在本文件，便于维护。

字段说明（映射到 crawl4ai CrawlerRunConfig）：
- domains:           域名匹配列表（按"域名或子域名"匹配，如 example.com 可匹配 www.example.com）
- css_selector:      正文区域定位（单个选择器！逗号选择器会让 crawl4ai 逐个提取后拼接，导致正文重复）
- css_selector_fallbacks: 主选择器没抓到内容时依次重试的备选选择器
- excluded_selector: 需移除的干扰元素（对应原 remove_selectors）
- wait_for:          等待正文渲染的条件（"css:#xxx" 或 "js:() => ..."），解决 JS 动态内容
- js_snippets:       页面加载后、内容提取前执行的 JS（处理平台特有 DOM 问题）
- title_suffixes:    页面标题里的站点名后缀，生成标题时会被裁掉（如 " - 简书"）
- title/author/date_selector: 元数据补充定位（供 YAML 头与摘要使用）

新增站点：在 SITE_STRATEGIES 列表追加一个 SiteStrategy 即可，无需改动其他代码。
"""

from dataclasses import dataclass, field
from urllib.parse import urlparse


@dataclass
class SiteStrategy:
    """单个网站的抓取策略（声明式配置）"""
    name: str
    domains: tuple = ()
    css_selector: str = None            # 正文定位（必须单个选择器），None 表示交给 crawl4ai 通用提取
    css_selector_fallbacks: tuple = ()  # 主选择器失效时的备选（按顺序重试）
    excluded_selector: str = None       # 移除干扰元素（逗号分隔 CSS 选择器）
    wait_for: str = None                # 等待条件，如 "css:#js_content"
    js_snippets: list = field(default_factory=list)
    title_suffixes: tuple = ()          # 标题中需裁掉的站点名后缀
    title_selector: str = None
    author_selector: str = None
    date_selector: str = None

    def matches(self, url: str) -> bool:
        """按域名精确/子域名匹配，避免 notzhihu.com 之类的仿冒域名误命中"""
        host = urlparse(url).netloc.lower().split(":")[0]
        return any(host == d or host.endswith("." + d) for d in self.domains)


# JS 片段：页面加载后修正 DOM，供多个策略复用
JS_FIX_LAZY_IMAGES = """
// 将懒加载图片的 data-src/data-original/data-lazy-src 还原为 src
document.querySelectorAll('img').forEach(img => {
    const real = img.getAttribute('data-src') || img.getAttribute('data-original')
              || img.getAttribute('data-lazy-src') || img.getAttribute('data-actualsrc');
    if (real) {
        img.src = real.startsWith('//') ? 'https:' + real : real;
    }
});
"""

JS_FIX_ZHIHU_MATH = """
// 知乎：将公式图片替换为 $alt$ 行内公式文本
document.querySelectorAll('img[data-eeimg], img.equation').forEach(img => {
    const alt = img.getAttribute('alt') || img.getAttribute('data-eeimg');
    if (alt) {
        const node = document.createTextNode(img.getAttribute('data-eeimg-status') === 'block'
            ? '\\n$$' + alt + '$$\\n' : '$' + alt + '$');
        img.replaceWith(node);
    }
});
"""


def _ex(*selectors: str) -> str:
    """把多个移除选择器合并为 crawl4ai 的 excluded_selector 串"""
    return ",".join(s for s in selectors if s)


# ---------------------------------------------------------------------------
# 站点策略表（顺序即优先级：更具体的域名放前面）
# ---------------------------------------------------------------------------
SITE_STRATEGIES = [
    SiteStrategy(
        name="微信公众号",
        domains=("mp.weixin.qq.com", "weixin.qq.com"),
        title_suffixes=(" - 微信公众平台",),
        css_selector="#js_content",
        css_selector_fallbacks=(".rich_media_content",),
        excluded_selector=_ex("script", "style", ".rich_media_tool", ".qr_code_pc",
                              ".rich_media_area_extra"),
        wait_for="css:#js_content, .rich_media_content",
        js_snippets=[JS_FIX_LAZY_IMAGES],
        title_selector="h1.rich_media_title, h1",
        author_selector=".profile_nickname, #js_name",
        date_selector="#publish_time, em#publish_time",
    ),
    SiteStrategy(
        name="知乎",
        domains=("zhuanlan.zhihu.com", "zhihu.com"),
        title_suffixes=(" - 知乎",),
        css_selector=".Post-RichTextContainer",
        css_selector_fallbacks=(".RichContent-inner", "article"),
        excluded_selector=_ex("script", "style", ".RichContent-collapsedText",
                              ".ContentItem-actions", ".Reward", ".FollowButton",
                              ".AdbannerBanner", ".Sticky"),
        wait_for="css:.Post-RichTextContainer, .RichContent-inner",
        js_snippets=[JS_FIX_ZHIHU_MATH, JS_FIX_LAZY_IMAGES],
        title_selector="h1.Post-Title, h1",
        author_selector=".AuthorInfo-name, .UserLink-link",
        date_selector=".ContentItem-time, .publish-time, time",
    ),
    SiteStrategy(
        name="CSDN",
        domains=("blog.csdn.net", "csdn.net"),
        title_suffixes=(" - CSDN博客", " - CSDN"),
        css_selector="#content_views",
        css_selector_fallbacks=("article",),
        excluded_selector=_ex("script", "style", ".toolbar", ".recommend-box",
                              ".template-box", ".blog-footer", ".aside-box",
                              ".csdn-side-toolbar", ".hide-article-box",
                              ".article-bar-top", "#toolBarBox"),
        wait_for="css:#content_views, article",
        js_snippets=[JS_FIX_LAZY_IMAGES],
        title_selector="h1.title-article, h1",
        author_selector=".profile-intro-name, .follow-nickName",
        date_selector=".time, .article-time, .publish-time",
    ),
    SiteStrategy(
        name="掘金",
        domains=("juejin.cn", "juejin.im"),
        title_suffixes=(" - 掘金",),
        css_selector=".markdown-body",
        css_selector_fallbacks=(".article-content", "article"),
        excluded_selector=_ex("script", "style", ".article-suspended-panel",
                              ".article-end", ".juejin-footer", ".sidebar",
                              ".article-catalog", ".comment-box"),
        wait_for="css:.article-content, .markdown-body",
        js_snippets=[JS_FIX_LAZY_IMAGES],
        title_selector="h1.article-title, h1",
        author_selector=".username, .author-name",
        date_selector=".time, time, .publish-time",
    ),
    SiteStrategy(
        name="简书",
        domains=("jianshu.com",),
        title_suffixes=(" - 简书",),
        css_selector="article",                  # 新版简书正文在 article 标签内（class 已混淆）
        excluded_selector=_ex("script", "style", ".note-list", ".user-follow",
                              ".support-author", ".show-foot", ".jianshu-footer"),
        wait_for="css:article",
        js_snippets=[JS_FIX_LAZY_IMAGES],
        title_selector="h1.title, h1",
        author_selector=".name, .author-name",
        date_selector=".time, .publish-time, time",
    ),
    SiteStrategy(
        name="Bilibili专栏",
        domains=("bilibili.com",),
        title_suffixes=(" - 哔哩哔哩",),
        # 新版专栏(cv)会重定向到 opus 页，两种结构都覆盖
        css_selector=".article-content",
        css_selector_fallbacks=(".opus-module-content", "#read-article-holder", "article"),
        excluded_selector=_ex("script", "style", ".fixed-top-bar", ".article-bar",
                              ".recommend-list", ".comment-box", ".up-info-holder"),
        wait_for="css:.article-content, .opus-module-content, #read-article-holder",
        js_snippets=[JS_FIX_LAZY_IMAGES],
        title_selector="h1.title, .opus-module-title, .read-title, h1",
        author_selector=".up-name, .author-name",
        date_selector=".publish-time, time",
    ),
    SiteStrategy(
        name="博客园",
        domains=("cnblogs.com",),
        title_suffixes=(" - 博客园",),
        css_selector="#cnblogs_post_body",
        css_selector_fallbacks=(".postBody", "article"),
        excluded_selector=_ex("script", "style", "#sideBar", "#blog_news_kb",
                              "#blog-calendar", "#leftcontent", "#blog_post_info",
                              ".postDesc"),
        wait_for="css:#cnblogs_post_body, .postBody",
        js_snippets=[JS_FIX_LAZY_IMAGES],
        title_selector="#cb_post_title_url, h1",
        author_selector="#profile_block a, .postDesc a",
        date_selector="#post-date, .postDesc, time",
    ),
    SiteStrategy(
        name="开源中国",
        domains=("oschina.net",),
        title_suffixes=(" - OSCHINA",),
        css_selector="main",                     # 新版 OSCHINA 正文容器无 class，用 main 稳定
        excluded_selector=_ex("script", "style", ".related-article", ".article-actions",
                              ".float-bar", ".oschina-footer", "aside", "nav"),
        wait_for="css:main",
        js_snippets=[JS_FIX_LAZY_IMAGES],
        title_selector="h1.article-title, h1",
        author_selector=".user-name, .author",
        date_selector=".time, .publish-time, time",
    ),
    SiteStrategy(
        name="SegmentFault",
        domains=("segmentfault.com",),
        title_suffixes=(" - SegmentFault",),
        css_selector=".article-content",
        css_selector_fallbacks=(".question-content", "article"),
        excluded_selector=_ex("script", "style", ".side", ".related-questions",
                              ".ad-wrap", ".post-actions", ".sf-footer"),
        wait_for="css:.article-content, .question-content",
        js_snippets=[JS_FIX_LAZY_IMAGES],
        title_selector="h1, .question-title",
        author_selector=".user-name, .author",
        date_selector=".time, time",
    ),
]

# 普通网页（兜底）：不做正文定位，交给 crawl4ai 通用内容提取（pruning filter）
GENERIC_STRATEGY = SiteStrategy(name="普通网页", domains=())


def detect_strategy(url: str) -> SiteStrategy:
    """根据 URL 检测站点策略，未命中返回通用策略"""
    for s in SITE_STRATEGIES:
        if s.matches(url):
            return s
    return GENERIC_STRATEGY
