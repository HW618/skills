"""
转换模块：将抓取结果整理为最终输出。

- convert_to_markdown: 完整 Markdown（YAML 元数据头 + 正文）
- extract_summary:     纯文本主要内容摘要
- 后处理：相对链接补全、去图片/链接、压缩空行、YAML 值转义
"""

import re
from urllib.parse import urljoin

import yaml
from bs4 import BeautifulSoup

from .crawler import CrawlResult

MAX_MARKDOWN_LENGTH = 50000

# YAML 中必须加引号的结构性情形：以指示符开头、含 ": "、含 " #"、含引号或换行
_YAML_NEEDS_QUOTE = re.compile(r'^[\s>|*&!%@`\[\]{},#?-]|:\s|\s#|["\n\r\t]|:\s*$')


def _yaml_type_unsafe(text: str) -> bool:
    """判断 YAML 是否会把该文本解析成「非字符串」或直接解析失败——两种都需加引号：

    - 解析失败：如以单引号开头却无闭合（`'90后…`），产出非法 front matter，下游直接报错；
    - 类型失真：`2024`→int、`3.14`→float、`true/yes/on`→bool、`null/~`→None，标题恰为这些值时会变类型。
    日期（如 `2024-01-01` 解析为 date）不视为失真，保持与既有 front matter 行为一致。
    """
    try:
        loaded = yaml.safe_load(f"k: {text}")
    except Exception:
        return True                       # 非法结构（如未闭合单引号），必须加引号
    val = loaded.get("k") if isinstance(loaded, dict) else loaded
    return val is None or isinstance(val, (bool, int, float))


def _yaml_scalar(value: str) -> str:
    """把任意文本安全地写成 YAML 标量（仅在必要时加引号）。

    加引号条件：含结构性字符（开头指示符 / ": " / 引号 / 换行等），
    或 YAML 不会把它解析成同一字符串（数字 / 布尔 / null / 非法结构）。
    """
    text = " ".join(str(value).split())          # 折成单行，避免换行破坏 front matter
    if not text:
        return '""'
    if _YAML_NEEDS_QUOTE.search(text) or _yaml_type_unsafe(text):
        return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return text


def _fix_links(md: str, base_url: str) -> str:
    """把 Markdown 中的相对链接补成绝对链接（crawl4ai 已处理大部分，此处兜底）"""
    if not base_url:
        return md

    def repl(match: re.Match, is_image: bool) -> str:
        text, link = match.group(1), match.group(2)
        if link.startswith(("http://", "https://", "data:", "#", "mailto:")):
            return match.group(0)
        prefix = "!" if is_image else ""
        return f"{prefix}[{text}]({urljoin(base_url, link)})"

    md = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", lambda m: repl(m, True), md)
    md = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", lambda m: repl(m, False), md)
    return md


def _strip_images(md: str) -> str:
    """移除图片语法，保留 alt 文本"""
    return re.sub(r"<img[^>]*>", "", re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", md))


def _strip_links(md: str) -> str:
    """移除链接语法，保留链接文本"""
    return re.sub(r"(?<!!)\[([^\]]+)\]\([^)]*\)", r"\1", md)


def _squeeze_blank_lines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _table_to_pipe(html_table: str) -> str:
    """把单个 <table> 转成 Markdown 管道表格。

    仅在结构简单时转换（无合并单元格、无嵌套表格、单元格内无块级元素）；
    其余情况原样保留 HTML —— 管道表格无法表达这些结构，硬转会转坏。
    """
    soup = BeautifulSoup(html_table, "html.parser")
    if (len(soup.find_all("table")) > 1                  # 嵌套表格
            or soup.find(attrs={"rowspan": True})
            or soup.find(attrs={"colspan": True})
            or soup.find(["img", "ul", "ol", "pre", "blockquote"])):
        return html_table

    rows = []
    for tr in soup.find_all("tr"):
        cells = tr.find_all(["th", "td"])
        if not cells:
            continue
        values = [" ".join(c.get_text(" ", strip=True).split()).replace("|", "\\|")
                  for c in cells]
        rows.append(values)
    if not rows:
        return html_table

    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    header, body = rows[0], rows[1:]
    lines = ["| " + " | ".join(header) + " |",
             "|" + "|".join([" --- "] * width) + "|"]
    lines += ["| " + " | ".join(r) + " |" for r in body]
    return "\n".join(lines)


def _html_tables_to_markdown(md: str) -> str:
    """把残留的 HTML 表格块转成 Markdown 表格（转换失败则保留原样）。

    表格块前后统一补空行：Markdown 表格与 HTML 块都必须与相邻段落空行分隔，
    否则紧跟其后的段落会被渲染器并入表格（表现为"最后一段话跑到表格里"）。
    """
    def repl(match: re.Match) -> str:
        try:
            table = _table_to_pipe(match.group(0))
        except Exception:
            table = match.group(0)
        return "\n\n" + table.strip() + "\n\n"

    return re.sub(r"<table\b.*?</table>", repl, md, flags=re.S | re.I)


def _yaml_header(result: CrawlResult) -> list[str]:
    """组装 YAML front matter（仅保留有值字段）"""
    lines = ["---", f"title: {_yaml_scalar(result.title or '无标题')}"]
    for key, value in (
        ("description", result.description),
        ("author", result.author),
        ("date", result.published_date),
    ):
        if value:
            lines.append(f"{key}: {_yaml_scalar(value)}")
    lines.append(f"source: {_yaml_scalar(result.url)}")
    lines.append(f"site: {_yaml_scalar(result.site_name)}")
    lines += ["---", ""]
    return lines


def convert_to_markdown(result: CrawlResult, include_metadata: bool = True,
                        include_images: bool = True,
                        include_links: bool = True,
                        max_chars: int = MAX_MARKDOWN_LENGTH) -> str:
    """抓取结果 → 完整 Markdown 文档（max_chars=0 表示不截断）"""
    if not result.success:
        return f"❌ 抓取失败: {result.url}\n{result.error}"

    md = _html_tables_to_markdown(result.markdown)
    md = _fix_links(md, result.url)
    if not include_images:
        md = _strip_images(md)
    if not include_links:
        md = _strip_links(md)
    md = _squeeze_blank_lines(md)

    out = _yaml_header(result) if include_metadata else []
    # 正文若已以同名标题开头，就不再重复注入一级标题
    first_heading = re.search(r"^#{1,3}\s+(.+)$", md, re.M)
    if (result.title and result.title != "无标题"
            and not (first_heading and first_heading.group(1).strip() == result.title.strip())):
        out += [f"# {result.title}", ""]
    out.append(md)

    text = "\n".join(out)
    if max_chars and len(text) > max_chars:
        total = len(text)
        text = (text[:max_chars] + "\n\n...\n\n"
                f"[内容已截断，原始内容共 {total} 字符；需要完整内容请加 --max-chars 0]")
    return text


def extract_summary(result: CrawlResult, max_length: int = 3000) -> str:
    """抓取结果 → 纯文本主要内容摘要"""
    if not result.success:
        return f"❌ 抓取失败: {result.url}\n{result.error}"

    text = _strip_links(_strip_images(result.markdown))
    text = re.sub(r"[#*_`>]+", "", text)          # 去掉 Markdown 记号
    text = _squeeze_blank_lines(text)
    if len(text) > max_length:
        text = text[:max_length] + "..."

    lines = [f"📄 **{result.title or '无标题'}**", f"🔗 来源: {result.url}"]
    if result.author:
        lines.append(f"✍️ 作者: {result.author}")
    lines += ["", "---", "", text]
    return "\n".join(lines)
