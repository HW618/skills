#!/usr/bin/env python3
"""网页抓取工具：HTTP 优先，失败降级浏览器。

用法:
    python fetch_page.py <url> [--output <path>]
    python fetch_page.py <url> --output cache/ecs/llms.md

策略:
1. HTTP 抓取（curl + 浏览器 UA）。llms.txt 是纯 markdown，通常足够。
2. 失败时提示需用浏览器降级，打印 URL 供 agent 用浏览器工具抓取。

判断异常: 状态码非 200、内容含验证码/登录页特征、内容过短。
"""
import argparse
import subprocess
import sys
import re
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# 异常内容特征（仅当出现在内容前 2000 字符内才判异常，避免误判正文提及）
ANOMALY_PATTERNS = [
    r"请输入验证码",
    r"请完成验证",
    r"captcha required",
    r"login required",
    r"access denied",
    r"403 Forbidden",
]


def fetch_http(url: str, timeout: int = 30) -> tuple[bool, str]:
    """用 curl HTTP 抓取。返回 (成功, 内容)。"""
    try:
        result = subprocess.run(
            [
                "curl", "-sSL",
                "--max-time", str(timeout),
                "-A", UA,
                "-H", "Accept: text/plain, text/markdown, */*",
                "-H", "Accept-Language: zh-CN,zh;q=0.9",
                "-w", "\n__HTTP_STATUS__:%{http_code}",
                url,
            ],
            capture_output=True,
            text=True,
            timeout=timeout + 5,
        )
        output = result.stdout
        # 提取状态码
        status_match = re.search(r"__HTTP_STATUS__:(\d+)$", output)
        status_code = int(status_match.group(1)) if status_match else 0
        content = re.sub(r"\n__HTTP_STATUS__:\d+$", "", output)

        if status_code != 200:
            return False, f"HTTP {status_code}"
        if len(content.strip()) < 100:
            return False, "内容过短（<100 字节），疑似异常"
        # 仅检查内容前 2000 字符是否含异常特征，避免误判正文提及
        head = content[:2000]
        for pattern in ANOMALY_PATTERNS:
            if re.search(pattern, head, re.IGNORECASE):
                return False, f"内容含异常特征: {pattern}"
        return True, content
    except subprocess.TimeoutExpired:
        return False, "curl 超时"
    except Exception as e:
        return False, f"curl 异常: {e}"


def main():
    parser = argparse.ArgumentParser(description="抓取阿里云 llms.txt 页面")
    parser.add_argument("url", help="目标 URL")
    parser.add_argument("--output", "-o", help="输出文件路径")
    parser.add_argument("--timeout", type=int, default=30, help="超时秒数")
    args = parser.parse_args()

    ok, content = fetch_http(args.url, args.timeout)
    if ok:
        if args.output:
            Path(args.output).parent.mkdir(parents=True, exist_ok=True)
            Path(args.output).write_text(content, encoding="utf-8")
            print(f"✅ 抓取成功，已写入 {args.output}（{len(content)} 字节）", file=sys.stderr)
        else:
            print(content)
        return 0

    # HTTP 失败，提示浏览器降级
    print(f"❌ HTTP 抓取失败: {content}", file=sys.stderr)
    print(f"👉 请用浏览器工具降级抓取: {args.url}", file=sys.stderr)
    print("   步骤: open_browser_page → read_page → 提取文本", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
