"""
冒烟测试 + 单元断言

用法：
    export CDP_URL=http://127.0.0.1:9222
    python tests/test_smoke.py          # 单元断言 + 全部站点抓取
    python tests/test_smoke.py unit     # 只跑单元断言（不需要浏览器）
    python tests/test_smoke.py quick    # 只测普通网页链路
"""

import asyncio
import os
import sys

_SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _SKILL_DIR)

import src.converter as converter                               # noqa: E402
import src.crawler as crawler                                   # noqa: E402
from src.converter import convert_to_markdown, extract_summary   # noqa: E402
from src.crawler import CrawlResult, crawl_page                  # noqa: E402
from src.strategies import SITE_STRATEGIES, detect_strategy     # noqa: E402

QUICK_CASES = [
    # (url, 关键词必须出现在 markdown 中)
    ("https://example.com/", ["Example Domain"]),
]

# 站点策略样本：公开文章链接会随时间失效，
# 失效时从各站点首页/热榜现摘同类链接替换即可。
FULL_CASES = QUICK_CASES + [
    ("https://zhuanlan.zhihu.com/p/28852607", []),                     # 知乎专栏
    ("https://juejin.cn/post/7637856870833635343", []),                # 掘金
    ("https://www.jianshu.com/p/49801328d688", []),                    # 简书
    ("https://www.cnblogs.com/springhgui/p/22910363", []),             # 博客园
    ("https://www.oschina.net/news/502404/tailwind-is-joining-shopify", []),  # 开源中国
    ("https://mp.weixin.qq.com/s/tfiir-E816DH9P_q5bxJPg", []),         # 微信公众号
    # CSDN / Bilibili：当前环境易触发风控，手动过验证后可加入样本
    # ("https://blog.csdn.net/<user>/article/details/<id>", []),
]


def _check(results: list, label: str, cond: bool) -> None:
    results.append((label, bool(cond)))
    print(f"  {'✅' if cond else '❌'} {label}")


async def run_unit_checks() -> list:
    """不依赖浏览器的断言：域名匹配、标题清理、YAML 转义、错误精简、回退判定"""
    print("\n=== 单元断言")
    r = []
    # 1. 域名匹配：仿冒域名不应命中
    _check(r, "仿冒域名 notzhihu.com 不误命中知乎策略",
           detect_strategy("https://notzhihu.com/p/1").name == "普通网页")
    _check(r, "子域名 zhuanlan.zhihu.com 正确命中知乎策略",
           detect_strategy("https://zhuanlan.zhihu.com/p/1").name == "知乎")
    _check(r, "伪装后缀域名不命中 Bilibili 策略",
           detect_strategy("https://evil-bilibili.com.evil.com/x").name == "普通网页")
    _check(r, "www.bilibili.com 命中 Bilibili 策略",
           detect_strategy("https://www.bilibili.com/read/cv1").name == "Bilibili专栏")

    # 2. 标题后缀清理
    zhihu = detect_strategy("https://zhuanlan.zhihu.com/p/1")
    _check(r, "标题后缀 ' - 知乎' 被裁掉",
           crawler._clean_title("某文章 - 知乎", zhihu) == "某文章")

    # 3. YAML 转义：含冒号/引号的标题不破坏 front matter
    import yaml
    res = CrawlResult(url="https://example.com/", title='问题：为什么? "引号"',
                      site_name="普通网页", success=True, markdown="正文")
    md = convert_to_markdown(res)
    head = md.split("\n")[1]
    _check(r, "含特殊字符的标题被加引号转义",
           head.startswith('title: "') and head.endswith('"'))
    front_matter = md.split("---\n")[1]
    try:
        parsed = yaml.safe_load(front_matter)
        ok_yaml = parsed["title"] == '问题：为什么? "引号"' and parsed["site"] == "普通网页"
    except Exception:
        ok_yaml = False
    _check(r, "front matter 可被 YAML 正确解析（值无损）", ok_yaml)

    # 3b. YAML 转义边界：仅在必要时加引号，且往返解析无损
    scalar_cases = [
        "https://example.com/",           # URL 不应被多余加引号
        "Linux: 从入门到精通",              # 含 ": "
        "- 列表样式",                      # 以指示符开头
        "结尾有冒号:",
        "包含 # 号的内容",
        '问题：为什么? "引号"',
        "普通中文标题",
    ]
    all_lossless, quote_ok = True, True
    for c in scalar_cases:
        out = converter._yaml_scalar(c)
        try:
            all_lossless &= yaml.safe_load(f"k: {out}")["k"] == " ".join(c.split())
        except Exception:
            all_lossless = False
    quote_ok = ("https://example.com/" == converter._yaml_scalar("https://example.com/")
                and converter._yaml_scalar("Linux: 从入门到精通").startswith('"'))
    _check(r, "YAML 转义边界：必要才加引号且往返无损", all_lossless and quote_ok)

    # 4. 错误信息精简（不泄露 crawl4ai 堆栈）
    short = crawler._short_error(
        "Unexpected error in _crawl_web at line 1024\nWait condition failed: Timeout after 40000ms")
    _check(r, "长堆栈被压缩为可读提示且无行号",
           "line 1024" not in short and "超时" in short)

    # 5. 回退判定：页面错误不回退、浏览器错误才回退
    _check(r, "页面类错误不触发回退",
           not crawler._is_browser_error(RuntimeError("Wait condition failed: Timeout")))
    _check(r, "浏览器连接错误触发回退",
           crawler._is_browser_error(RuntimeError("Failed to connect to CDP endpoint")))

    # 6. 去图片/去链接开关
    res2 = CrawlResult(url="https://e.com/", title="T", success=True,
                       markdown="看 ![图](http://a/b.png) 和 [链接](http://c/d)")
    no_img = convert_to_markdown(res2, include_images=False, include_metadata=False)
    no_link = convert_to_markdown(res2, include_links=False, include_metadata=False)
    _check(r, "--no-images 去图片但保留 alt 文本", "![" not in no_img and "图" in no_img)
    _check(r, "--no-links 去链接但保留文本且不动图片",
           "[链接](" not in no_link and "链接" in no_link and "![图](http" in no_link)

    # 7. 失败结果不产生正文（避免把错误写进文件）
    fail = CrawlResult(url="https://e.com/", success=False, error="页面超时")
    _check(r, "失败结果输出错误提示而非正文", convert_to_markdown(fail).startswith("❌"))

    # 7b. 标题去重：正文已以同名 H1 开头时不再重复注入
    dup = CrawlResult(url="https://e.com/", title="标题A", site_name="站A", success=True,
                      markdown="# 标题A\n\n正文")
    _check(r, "正文已含同名 H1 时不重复注入标题",
           convert_to_markdown(dup).count("# 标题A") == 1)
    nodup = CrawlResult(url="https://e.com/", title="标题B", site_name="站B", success=True,
                        markdown="正文")
    _check(r, "正文无标题时仍注入一级标题",
           convert_to_markdown(nodup).count("# 标题B") == 1)

    # 8. 表格处理：抓取时 bypass_tables 保真，转换时简单表格转管道、复杂表格保留 HTML
    _check(r, "Markdown 生成选项启用 bypass_tables",
           crawler.MARKDOWN_OPTIONS.get("bypass_tables") is True)
    gen = crawler.build_markdown_generator()
    _check(r, "生成器选项已带入 bypass_tables",
           getattr(gen, "options", {}).get("bypass_tables") is True)

    simple = CrawlResult(url="https://e.com/", title="T", site_name="S", success=True,
                         markdown="<table><tr><th>层级</th><th>名称</th></tr>"
                                  "<tr><td>L0</td><td>基础资源层</td></tr></table>")
    simple_md = convert_to_markdown(simple)
    _check(r, "简单表格转成 Markdown 管道表格",
           "<table" not in simple_md and "| 层级 | 名称 |" in simple_md
           and "| L0 | 基础资源层 |" in simple_md)

    complex_tbl = CrawlResult(url="https://e.com/", title="T", site_name="S", success=True,
                              markdown='<table><tr><td rowspan="2">跨行</td><td>a</td></tr>'
                                       '<tr><td>b</td></tr></table>')
    complex_md = convert_to_markdown(complex_tbl)
    _check(r, "含合并单元格的表格保留 HTML（避免转坏）",
           "<table" in complex_md and "rowspan" in complex_md)

    # 8b. 表格块前后必须有空行，否则后续段落会被渲染器并入表格
    adj = CrawlResult(url="https://e.com/", title="T", site_name="S", success=True,
                      markdown="### 小标题  \n<table><tr><th>A</th></tr>"
                               "<tr><td>1</td></tr></table>\n**段落**")
    adj_md = convert_to_markdown(adj, include_metadata=False)
    _check(r, "表格与相邻段落之间有空行（段落不会被并入表格）",
           "\n\n| A |" in adj_md and "| 1 |\n\n**段落**" in adj_md)

    # 8c. 站点策略的主选择器必须是单个选择器（逗号选择器会被 crawl4ai 重复提取）
    comma = [s.name for s in SITE_STRATEGIES if "," in (s.css_selector or "")]
    _check(r, "所有站点主选择器均为单个选择器（无逗号）",
           not comma and len(SITE_STRATEGIES) >= 9)
    _check(r, "需要备选选择器的站点已配置 fallback",
           all(s.css_selector_fallbacks for s in SITE_STRATEGIES
               if s.name in ("微信公众号", "知乎", "博客园", "掘金")))

    # 8d. 重复正文兜底去重（正常文章不受影响）
    body = "\n\n".join(f"## 第 {i} 节 标题{i}\n本节讨论第 {i} 个主题的具体细节。"
                       for i in range(1, 21))
    _check(r, "正文重复 2 次时自动去重",
           abs(len(crawler._dedupe_repeats(body + "\n\n" + body)) - len(body)) < 10)
    _check(r, "正文重复 3 次时自动去重",
           abs(len(crawler._dedupe_repeats(body + "\n\n" + body + "\n\n" + body))
               - len(body)) < 10)
    _check(r, "正常正文不被误去重",
           len(crawler._dedupe_repeats(body)) == len(body))

    # 9. 超长内容：默认截断并提示，max_chars=0 不截断
    long_res = CrawlResult(url="https://e.com/", title="T", site_name="S", success=True,
                           markdown="x" * 60000)
    truncated = convert_to_markdown(long_res, include_metadata=False)
    full = convert_to_markdown(long_res, include_metadata=False, max_chars=0)
    _check(r, "超长内容默认截断并提示取全文方式",
           "内容已截断" in truncated and "--max-chars 0" in truncated)
    _check(r, "max_chars=0 时不截断", "内容已截断" not in full and len(full) >= 60000)

    # 10. 页面级失败不重复调用（本次修正的核心）
    calls = []

    async def fake_crawl_once(url, strategy, cdp_url, timeout_ms, verbose=False,
                              css_selector=None):
        calls.append((cdp_url, css_selector))
        out = CrawlResult(url=url, strategy=strategy.name)
        out.error, out.error_kind = "页面正文未在超时时间内出现。", "page"
        return out

    original = crawler._crawl_once
    crawler._crawl_once = fake_crawl_once
    try:
        # 简书：仅一个选择器，便于计数
        await crawler.crawl_page("https://www.jianshu.com/p/1")
    finally:
        crawler._crawl_once = original
    _check(r, "页面级错误只执行一次且不回退本地浏览器",
           len(calls) == 1 and all(env == calls[0][0] for env, _ in calls))

    # 10b. 主选择器未命中时按顺序用备选选择器重试
    tried = []

    async def fake_fallback(url, strategy, cdp_url, timeout_ms, verbose=False,
                            css_selector=None):
        tried.append(css_selector)
        out = CrawlResult(url=url, strategy=strategy.name)
        if css_selector == strategy.css_selector:      # 主选择器取不到正文
            out.error, out.error_kind = "主选择器未命中", "page"
        else:
            out.success, out.markdown = True, "正文内容" * 200
        return out

    crawler._crawl_once = fake_fallback
    try:
        res = await crawler.crawl_page("https://zhuanlan.zhihu.com/p/1")   # 知乎有备选
    finally:
        crawler._crawl_once = original
    _check(r, "主选择器未命中时自动改用备选选择器",
           res.success and tried == [".Post-RichTextContainer", ".RichContent-inner"])

    return r


async def run_case(url: str, keywords: list) -> bool:
    strategy = detect_strategy(url)
    print(f"\n=== [{strategy.name}] {url}")
    result = await crawl_page(url, timeout_ms=45000)

    if not result.success:
        print(f"  ❌ 失败: {result.error}")
        return False

    md = convert_to_markdown(result, include_metadata=True)
    summary = extract_summary(result, max_length=200)
    ok = True

    if len(md) < 200:
        print(f"  ⚠️ markdown 过短: {len(md)} 字符")
        ok = False
    for kw in keywords:
        if kw not in md:
            print(f"  ⚠️ 未找到关键词: {kw}")
            ok = False

    print(f"  ✅ strategy={result.strategy} title={result.title[:40]!r}")
    print(f"     markdown={len(md)} chars | summary={len(summary)} chars")
    return ok


async def main() -> int:
    argv = sys.argv[1:]
    unit_results = await run_unit_checks()
    unit_passed = sum(1 for _, ok in unit_results if ok)

    if "unit" in argv:
        print(f"\n===== 单元断言: {unit_passed}/{len(unit_results)} 通过 =====")
        return 0 if unit_passed == len(unit_results) else 1

    cases = QUICK_CASES if "quick" in argv else FULL_CASES
    crawl_passed = 0
    for url, kws in cases:
        if await run_case(url, kws):
            crawl_passed += 1

    print(f"\n===== 单元断言 {unit_passed}/{len(unit_results)} | 抓取 {crawl_passed}/{len(cases)} =====")
    all_ok = unit_passed == len(unit_results) and crawl_passed == len(cases)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
