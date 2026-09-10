---
name: md-this-page
description: "将任意网页转换为干净的结构化 Markdown，或提取主要内容摘要。基于 crawl4ai + CDP 浏览器，内置微信公众号、知乎、CSDN、掘金、简书、博客园、开源中国、SegmentFault、Bilibili 专栏等 10 种站点抓取策略。触发关键词：网页转 MD、网页转 Markdown、把网页转成 Markdown、提取网页内容、抓取文章、保存网页正文、web to markdown、convert page to markdown、extract web content、公众号转 Markdown、知乎/CSDN 文章抓取。"
description_zh: "网页转 Markdown / 提取正文摘要，crawl4ai + CDP，内置 10 种站点抓取策略"
description_en: "Convert web pages to clean Markdown or extract main content, powered by crawl4ai over CDP with 10 per-site strategies."
---

# MD This Page

将任意网页转换为干净、结构化的 Markdown，或提取主要内容摘要。基于 **crawl4ai**，通过 **CDP** 连接浏览器（支持真实浏览器环境，可有效应对 JS 渲染页面）。

## 何时使用

- 用户要求「把这个网页/文章转成 Markdown」
- 用户要求「提取某个网页的主要内容/摘要」
- 需要抓取微信公众号、知乎、CSDN、掘金、简书、博客园、开源中国、SegmentFault、Bilibili 专栏等平台的文章

## 环境准备

**首次使用先装依赖**（幂等，可重复执行；只装 Python 依赖，不下载浏览器）：

```bash
python3 scripts/setup.py
```

浏览器运行时在**抓取时自动解析**，无需手工干预：

1. 启动即读取 `CDP_URL` 环境变量，**未设置则默认 `http://127.0.0.1:9222`**；
2. 探测该端点是否为**合规可用的 CDP 浏览器**（`GET /json/version` 返回含 `webSocketDebuggerUrl`）：
   - 合规可用 → 直接连该浏览器（复用登录态，反爬更弱）；
   - 无效 / 不可达 / 不是合规 CDP → **自动回退本地 headless 浏览器**；
3. 若回退本地时内核缺失，抓取会报错并提示安装，此时**再按需运行**：

```bash
python3 scripts/install_browser.py     # 安装本地 headless 内核（crawl4ai-setup，约 150MB，幂等）
```

> 设计说明：本地内核约 150MB，不在初始化时强制下载；只有真正需要回退本地且内核缺失时才提示安装。
> 本 skill 全部用相对路径，脚本内部基于自身位置解析目录，可从任意 cwd 以绝对路径调用；
> 统一用 `python3`（或当前已装依赖的解释器）即可，无任何机器专属硬编码路径。

自定义 CDP 地址（可选；不设置则用默认 `http://127.0.0.1:9222`）：

```bash
export CDP_URL=http://127.0.0.1:9222
```

CDP 浏览器启动示例：

```bash
# Chrome / Edge（任意一个即可）
google-chrome --remote-debugging-port=9222
```

## 使用方法（CLI）

所有命令在 skill 目录下执行；`python3` 指已装依赖的解释器（首次先跑 `python3 scripts/setup.py`）。脚本内部已处理路径，用绝对路径调用亦可：

```bash
# 网页 → Markdown（打印到 stdout）
python3 scripts/md_this_page.py convert https://example.com/

# 保存到文件
python3 scripts/md_this_page.py convert <url> -o page.md

# 常用开关
python3 scripts/md_this_page.py convert <url> --timeout 60    # 页面超时秒数（默认 45）
python3 scripts/md_this_page.py convert <url> --no-metadata   # 不含 YAML 元数据头
python3 scripts/md_this_page.py convert <url> --no-images     # 移除图片（保留 alt 文本）
python3 scripts/md_this_page.py convert <url> --no-links      # 移除链接（保留文本）
python3 scripts/md_this_page.py convert <url> --verbose       # 输出 crawl4ai 详细日志（调试用）

# 提取主要内容摘要
python3 scripts/md_this_page.py extract <url> --max-length 3000

# 查看支持的站点策略
python3 scripts/md_this_page.py sites
```

**退出码**：`0` 成功 / `1` 抓取失败 / `2` URL 非法。失败时错误信息输出到 stderr，且不会写入输出文件（避免生成垃圾文件）。

## 使用方法（Python API）

```python
import asyncio
from src import crawl_page, convert_to_markdown, extract_summary

async def main():
    result = await crawl_page("https://mp.weixin.qq.com/s/xxxxx")
    if result.success:
        markdown = convert_to_markdown(result)          # 完整 Markdown（含 YAML 头）
        summary = extract_summary(result, max_length=3000)  # 纯文本摘要
        print(markdown)
    else:
        print("失败:", result.error)                     # 已是可读的错误说明

asyncio.run(main())
```

同步场景可直接用 `from src import crawl`（内部处理事件循环；在 async 环境中请用 `crawl_page`）。

## 站点抓取策略

所有策略集中在 `src/strategies.py`，按 URL 域名自动匹配：

| 网站 | 域名 | 策略要点 |
|------|------|----------|
| 微信公众号 | mp.weixin.qq.com | 懒加载图片 data-src 修正（JS）+ 正文定位 |
| 知乎 | zhuanlan.zhihu.com | 公式图片转 `$...$`（JS）+ 正文定位 |
| CSDN | blog.csdn.net | 移除推荐/侧栏/登录浮层 + 正文定位 |
| 掘金 | juejin.cn | 正文定位 + 移除侧栏/评论 |
| 简书 | jianshu.com | 正文定位 + 移除推荐栏 |
| Bilibili 专栏 | bilibili.com | 专栏正文定位 |
| 博客园 | cnblogs.com | 正文定位 + 移除侧栏 |
| 开源中国 | oschina.net | 正文定位 |
| SegmentFault | segmentfault.com | 正文定位 |
| 普通网页 | 其他 | crawl4ai 通用内容提取（pruning filter） |

### 新增/修改站点策略

只需编辑 `src/strategies.py`，在 `SITE_STRATEGIES` 列表中追加一个条目：

```python
SiteStrategy(
    name="某某网站",
    domains=("example.com",),
    css_selector=".article-body",                    # 正文定位（必须单个选择器，见下方⚠️）
    css_selector_fallbacks=(".content", "article"),  # 主选择器失效时依次重试（可选）
    excluded_selector=".ad,.sidebar",                # 移除干扰
    wait_for="css:.article-body",                    # 等待渲染（可选）
    js_snippets=[JS_FIX_LAZY_IMAGES],                # DOM 修正（可选，可复用内置片段）
    title_suffixes=(" - 某某网",),                    # 标题里要裁掉的站点名后缀（可选）
    title_selector="h1",
    author_selector=".author",
    date_selector=".time",
)
```

> ⚠️ **`css_selector` 不要写成逗号选择器**（如 `"#content, .content"`）。
> crawl4ai 会为**每个**选择器分别提取一次再拼接，导致正文重复 2~3 遍。
> 需要多个候选时请用 `css_selector_fallbacks`：主选择器取不到正文才会依次重试。
> （另有兜底：`_dedupe_repeats` 会在检测到整篇重复时自动只保留一份。）

三个易踩的坑（都已实测）：

1. **正文重复** → 见上，逗号选择器是主因
2. **段落被并进表格** → 转换时会自动在表格块前后补空行，无需人工处理
3. **标题/作者/日期取不到** → 使用 `css_selector` 时 crawl4ai 的 `metadata` 为空，
   框架会自动把 `document.title` 与 `author_selector`/`date_selector` 注入正文容器后再解析


## 输出格式

`convert` 输出带 YAML front matter 的 Markdown：

```markdown
---
title: 文章标题
description: 页面描述
author: 作者
date: 2026-01-01
source: https://...
site: 微信公众号
---

# 文章标题

（正文 Markdown…）
```

**表格处理**：抓取阶段统一启用 `bypass_tables=True`（见 `src/crawler.py` 的 `MARKDOWN_OPTIONS`），
让 crawl4ai 把表格保留为**原始 HTML**、不做它自己那套易转坏的转换；随后 `src/converter.py` 的
`_html_tables_to_markdown` 按结构分流：

- **简单表格**（无合并单元格、无嵌套表格、单元格内无图片/列表/代码块）→ 转成 Markdown **管道表格**（更整洁）；
- **复杂表格**（含 `rowspan`/`colspan`、嵌套表格，或单元格内含块级元素）→ **保留原始 HTML**（管道表格无法表达，硬转会转坏）。

Markdown 渲染器（GitHub、Typora、Obsidian、飞书等）普遍支持 HTML 表格，故复杂表格保真无碍。

> 注意：`bypass_tables` 只决定 crawl4ai 抓取阶段是否保留 HTML；最终「管道 vs HTML」由 converter 依结构判定。
> 把 `MARKDOWN_OPTIONS` 改成 `{"bypass_tables": False}` 只会让 crawl4ai 提前自行转表（复杂表格更易转坏），
> 并**不能**让 converter 把复杂表格也变成管道表格。

## 注意事项

1. **浏览器选择**：启动即读 `CDP_URL`（未设置默认 `http://127.0.0.1:9222`）。端点为**合规可用的 CDP 浏览器**（`/json/version` 含 `webSocketDebuggerUrl`）才连接；无效/不可达/非合规 CDP 一律回退本地 headless。只有"浏览器连接失败"才触发回退，页面级错误（超时/失效/风控）不重试，避免无谓翻倍耗时。本地内核缺失时，报错会提示运行 `scripts/install_browser.py`。
2. **登录态复用（含安全权衡）**：CDP 模式复用浏览器默认上下文（`use_managed_browser`），已登录站点可直接抓取，也显著降低验证码概率；抓取结束不会关闭或影响用户已打开的标签页。
   ⚠️ **安全提示**：默认会自动连接 `http://127.0.0.1:9222` 并复用该浏览器 profile 的全部登录态，被转换页面的 JS 会在这个已认证会话里执行。若转换**不受信任/钓鱼页面**，其脚本理论上可发起同会话的认证请求（CSRF 类风险）。建议：用**专用隔离 profile** 启动 CDP 浏览器（如 `--remote-debugging-port=9222 --user-data-dir=/path/to/scratch-profile`），只在其中登录确需抓取的站点，避免用装满登录态的主 profile。
3. **错误提示**：失败时返回的是压缩后的可读说明（例如"页面正文未在超时时间内出现，常见原因是链接失效/需登录/风控"），不是 crawl4ai 的原始堆栈。
4. **付费内容**：仅能提取可见部分。
5. **反爬提示（实测）**：
   - CSDN 在同一浏览器/IP 高频自动化访问后会弹「安全验证」，此时需在浏览器里手动通过一次验证再抓
   - Bilibili 专栏对高频访问有间歇性频控，失败后间隔几分钟重试即可
   - 遇到超时，多半是页面被风控页/404 页替代，先人工确认 URL 有效，再用 `--timeout` 适当放宽
6. **调试**：加 `--verbose` 可看到 crawl4ai 的完整抓取日志（默认静默，不污染输出）。

## 自测

```bash
python3 tests/test_smoke.py unit    # 仅单元断言（不需要浏览器）：域名匹配/标题清理/YAML 转义/回退策略等
python3 tests/test_smoke.py quick   # 普通网页链路
python3 tests/test_smoke.py         # 单元断言 + 全部站点抓取（需 CDP 浏览器在线）
```

## 目录结构

```
md-this-page/
├── SKILL.md              # 本文件
├── requirements.txt      # 依赖
├── scripts/
│   ├── setup.py          # 初始化：装 Python 依赖（幂等）
│   ├── install_browser.py # 按需安装本地 headless 内核（crawl4ai-setup）
│   └── md_this_page.py   # CLI 入口（convert / extract / sites）
├── src/
│   ├── crawler.py        # CDP 连接 + crawl4ai 抓取
│   ├── strategies.py     # 站点抓取策略（唯一需要维护的配置文件）
│   └── converter.py      # Markdown 转换 / 摘要 / 后处理
└── tests/
    └── test_smoke.py     # 冒烟测试（真实页面）
```
