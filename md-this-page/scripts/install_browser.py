#!/usr/bin/env python3
"""安装本地 headless 浏览器内核（crawl4ai-setup，约 150MB）。

无需预先执行。仅当满足以下条件、抓取时提示本地内核缺失时再运行：
  - 没有合规可用的 CDP 浏览器（CDP_URL 未设置或不可达），且
  - 报错信息提示「本地 headless 浏览器内核未安装」。

幂等：playwright 会跳过已下载的内核。安装后，抓取即可在无 CDP 时回退本地 headless。

用法：
    python3 scripts/install_browser.py

退出码：0 成功 / 1 失败
"""

import os
import shutil
import subprocess
import sys


def local_browser_installed() -> bool:
    """检查 crawl4ai/playwright 的本地 Chromium 内核是否已下载"""
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            return os.path.exists(p.chromium.executable_path)
    except Exception:
        return False


def main() -> int:
    if local_browser_installed():
        print("✅ 本地 headless 浏览器内核已安装，无需重复操作")
        return 0

    print("⏳ 正在安装本地 headless 浏览器内核（crawl4ai-setup，约 150MB）...")
    cmd = shutil.which("crawl4ai-setup")
    if cmd:
        ret = subprocess.call([cmd])
    else:
        ret = subprocess.call(
            [sys.executable, "-c", "from crawl4ai.install import post_install; post_install()"])
    if ret != 0:
        print("❌ crawl4ai-setup 执行失败，请检查网络后重试；"
              "或启动 CDP 浏览器并设置 CDP_URL 改用远程浏览器。", file=sys.stderr)
        return 1
    print("✅ 本地 headless 浏览器内核安装完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
