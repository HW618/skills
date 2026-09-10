#!/usr/bin/env python3
"""
md-this-page 初始化脚本（幂等，可重复执行）

只负责把 Python 依赖（crawl4ai / beautifulsoup4 / lxml）装到当前解释器。

浏览器运行时不在此处安装，而是抓取时自动解析：
  - 启动读取 CDP_URL（未设置默认 http://127.0.0.1:9222），是合规可用的 CDP 浏览器就用它；
  - 否则回退本地 headless 浏览器；
  - 若回退时本地内核缺失，抓取会报错并提示运行 scripts/install_browser.py 安装。

用法：
    python3 scripts/setup.py

退出码：0 成功 / 1 失败
"""

import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REQUIREMENTS = SKILL_DIR / "requirements.txt"


def ensure_deps() -> bool:
    """检查核心依赖，缺失则用当前解释器的 pip 安装 requirements.txt"""
    missing = []
    for module in ("crawl4ai", "bs4", "lxml"):
        try:
            __import__(module)
        except ImportError:
            missing.append(module)
    if not missing:
        print("✅ Python 依赖已就绪（crawl4ai / beautifulsoup4 / lxml）")
        return True

    print(f"⏳ 缺少依赖 {', '.join(missing)}，开始安装 {REQUIREMENTS.name} ...")
    ret = subprocess.call([sys.executable, "-m", "pip", "install", "-r", str(REQUIREMENTS)])
    if ret != 0:
        print("❌ 依赖安装失败，请检查网络或 pip 配置后重试", file=sys.stderr)
        return False
    print("✅ Python 依赖安装完成")
    return True


def main() -> int:
    print("=== md-this-page 初始化 ===")
    if not ensure_deps():
        return 1
    print("ℹ️ 浏览器运行时将在抓取时自动解析：优先 CDP_URL（默认 http://127.0.0.1:9222），"
          "不可用则回退本地 headless。")
    print("ℹ️ 若回退本地时提示内核缺失，再运行 python3 scripts/install_browser.py 安装（约 150MB）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
