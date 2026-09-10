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

**运行解释器（重要）**：必须使用已安装 crawl4ai 的 Python 解释器调用本 skill。
本机已在 WorkBuddy 管理型 venv 中装好依赖，直接用它：

```bash
PY=/Users/user/.workbuddy/binaries/python/envs/default/bin/python
$PY scripts/md_this_page.py convert https://example.com/
```

若在其他机器/环境使用，先安装依赖：

```bash
pip install -r requirements.txt      # crawl4ai + beautifulsoup4 + lxml

# 设置 CDP 连接地址；不设置则使用 crawl4ai 本地 headless 浏览器
export CDP_URL=http://127.0.0.1:9222

# 仅回退模式需要：初始化本地浏览器
crawl4ai-setup
```

CDP 浏览器启动示例：

```bash
# Chrome / Edge（任意一个即可）
google-chrome --remote-debugging-port=9222
```

## 使用方法（CLI）

所有命令在 skill 目录下执行；下面的 `python` 均指上文提到的、已装依赖的解释器（`$PY`）。脚本内部已处理路径，用绝对路径调用亦可：

```bash
# 网页 → Markdown（打印到 stdout）
python scripts/md_this_page.py convert https://example.com/

# 保存到文件
python scripts/md_this_page.py convert <url> -o page.md

# 常用开关
python scripts/md_this_page.py convert <url> --timeout 60    # 页面超时秒数（默认 30）
python scripts/md_this_page.py convert <url> --no-metadata   # 不含 YAML 元数据头
python scripts/md_this_page.py convert <url> --no-images     # 移除图片（保留 alt 文本）
python scripts/md_this_page.py convert <url> --no-links      # 移除链接（保留文本）
python scripts/md_this_page.py convert <url> --verbose       # 输出 crawl4ai 详细日志（调试用）

# 提取主要内容摘要
python scripts/md_this_page.py extract <url> --max-length 3000

# 查看支持的站点策略
python scripts/md_this_page.py sites
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

**表格保真**：所有站点统一启用 `bypass_tables`（见 `src/crawler.py` 的 `MARKDOWN_OPTIONS`），
表格以**原始 HTML**（`<table>/<tr>/<td>`）输出，而不是转成 Markdown 管道表格。
这样可以避免合并单元格、单元格内多行/嵌套结构在转换时被破坏——
Markdown 渲染器（GitHub、Typora、Obsidian、飞书等）普遍支持 HTML 表格。
如需改回管道表格，只需把 `MARKDOWN_OPTIONS` 改为 `{"bypass_tables": False}`。

## 注意事项

1. **浏览器选择**：`CDP_URL` 已设置且端点可达时连接该浏览器；未设置或连不上时回退本地 headless。只有"浏览器连接失败"才会触发回退，页面级错误（超时/失效/风控）不会重试，避免无谓地翻倍耗时。
2. **登录态复用**：CDP 模式复用浏览器默认上下文（`use_managed_browser`），已登录站点可直接抓取，也显著降低验证码概率；抓取结束不会关闭或影响用户已打开的标签页。
3. **错误提示**：失败时返回的是压缩后的可读说明（例如"页面正文未在超时时间内出现，常见原因是链接失效/需登录/风控"），不是 crawl4ai 的原始堆栈。
4. **付费内容**：与原插件一致，仅能提取可见部分。
5. **原插件不受影响**：本 skill 为独立目录，不修改 `md-this-page/` 下任何文件。
6. **反爬提示（实测）**：
   - CSDN 在同一浏览器/IP 高频自动化访问后会弹「安全验证」，此时需在浏览器里手动通过一次验证再抓
   - Bilibili 专栏对高频访问有间歇性频控，失败后间隔几分钟重试即可
   - 遇到超时，多半是页面被风控页/404 页替代，先人工确认 URL 有效，再用 `--timeout` 适当放宽
7. **调试**：加 `--verbose` 可看到 crawl4ai 的完整抓取日志（默认静默，不污染输出）。

## 自测

```bash
python tests/test_smoke.py unit    # 仅单元断言（不需要浏览器）：域名匹配/标题清理/YAML 转义/回退策略等
python tests/test_smoke.py quick   # 普通网页链路
python tests/test_smoke.py         # 单元断言 + 全部站点抓取（需 CDP 浏览器在线）
```

## 目录结构

```
md-this-page-skill/
├── SKILL.md              # 本文件
├── requirements.txt      # 依赖
├── scripts/
│   └── md_this_page.py   # CLI 入口（convert / extract / sites）
├── src/
│   ├── crawler.py        # CDP 连接 + crawl4ai 抓取
│   ├── strategies.py     # 站点抓取策略（唯一需要维护的配置文件）
│   └── converter.py      # Markdown 转换 / 摘要 / 后处理
└── tests/
    └── test_smoke.py     # 冒烟测试（真实页面）
```
