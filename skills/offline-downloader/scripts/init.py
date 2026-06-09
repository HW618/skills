#!/usr/bin/env python3
"""
Initialization script for offline-downloader skill.
Detects environment and installs missing dependencies.
"""

import sys
import os
import subprocess
import platform

def run_command(cmd, check=True):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True,
            check=check
        )
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stdout.strip() if e.stdout else "", e.stderr.strip() if e.stderr else ""
    except Exception as e:
        return False, "", str(e)

def check_aria2c():
    """Check if aria2c is installed."""
    success, stdout, _ = run_command("which aria2c", check=False)
    if success and stdout:
        # Get version
        _, version, _ = run_command("aria2c --version | head -1", check=False)
        return True, stdout, version
    return False, None, None

def check_aria2p():
    """Check if aria2p is installed."""
    try:
        import aria2p
        # Try to get version from package metadata
        try:
            from importlib.metadata import version
            ver = version("aria2p")
            return True, ver
        except:
            return True, "installed"
    except ImportError:
        return False, None

def check_aria2c_daemon():
    """Check if aria2c daemon is running."""
    success, stdout, _ = run_command("ps aux | grep 'aria2c.*enable-rpc' | grep -v grep", check=False)
    return success and stdout

def install_aria2():
    """Install aria2 based on the OS."""
    system = platform.system()
    
    print("正在安装 aria2...")
    
    if system == "Darwin":  # macOS
        # Check if Homebrew is installed
        brew_installed, _, _ = run_command("which brew", check=False)
        if not brew_installed:
            print("错误: 未安装 Homebrew，请先安装 Homebrew:")
            print("  /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
            return False
        
        success, stdout, stderr = run_command("brew install aria2")
        if success:
            print("✓ aria2 安装成功")
            return True
        else:
            print(f"✗ aria2 安装失败: {stderr}")
            return False
            
    elif system == "Linux":
        # Try apt-get first (Debian/Ubuntu)
        apt_installed, _, _ = run_command("which apt-get", check=False)
        if apt_installed:
            success, stdout, stderr = run_command("sudo apt-get update && sudo apt-get install -y aria2")
            if success:
                print("✓ aria2 安装成功")
                return True
            else:
                print(f"✗ aria2 安装失败: {stderr}")
                return False
        
        # Try yum (CentOS/RHEL)
        yum_installed, _, _ = run_command("which yum", check=False)
        if yum_installed:
            success, stdout, stderr = run_command("sudo yum install -y aria2")
            if success:
                print("✓ aria2 安装成功")
                return True
            else:
                print(f"✗ aria2 安装失败: {stderr}")
                return False
        
        print("错误: 无法确定包管理器，请手动安装 aria2")
        return False
        
    elif system == "Windows":
        # Try Chocolatey
        choco_installed, _, _ = run_command("where choco", check=False)
        if choco_installed:
            success, stdout, stderr = run_command("choco install aria2 -y")
            if success:
                print("✓ aria2 安装成功")
                return True
            else:
                print(f"✗ aria2 安装失败: {stderr}")
                return False
        
        # Try winget
        winget_installed, _, _ = run_command("where winget", check=False)
        if winget_installed:
            success, stdout, stderr = run_command("winget install aria2")
            if success:
                print("✓ aria2 安装成功")
                return True
            else:
                print(f"✗ aria2 安装失败: {stderr}")
                return False
        
        print("错误: 无法确定包管理器，请手动安装 aria2")
        return False
    
    else:
        print(f"错误: 不支持的操作系统 {system}")
        return False

def install_aria2p():
    """Install aria2p Python package."""
    print("正在安装 aria2p...")
    
    # Try pip3 first, then pip
    for pip_cmd in ["pip3", "pip"]:
        pip_installed, _, _ = run_command(f"which {pip_cmd}", check=False)
        if pip_installed:
            success, stdout, stderr = run_command(f"{pip_cmd} install aria2p")
            if success:
                print("✓ aria2p 安装成功")
                return True
            else:
                print(f"✗ aria2p 安装失败: {stderr}")
                return False
    
    print("错误: 未找到 pip，请先安装 Python 和 pip")
    return False

def start_aria2c_daemon():
    """Start aria2c daemon."""
    print("正在启动 aria2c 守护进程...")
    
    # Check if already running
    if check_aria2c_daemon():
        print("✓ aria2c 守护进程已在运行")
        return True
    
    success, stdout, stderr = run_command("aria2c --enable-rpc --rpc-listen-all=true --daemon=true")
    if success:
        # Wait a moment and verify
        import time
        time.sleep(2)
        if check_aria2c_daemon():
            print("✓ aria2c 守护进程启动成功")
            return True
        else:
            print("✗ aria2c 守护进程启动失败")
            return False
    else:
        print(f"✗ aria2c 守护进程启动失败: {stderr}")
        return False

def create_download_dir():
    """Create download directory if it doesn't exist."""
    download_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "downloads")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir, exist_ok=True)
        print(f"✓ 创建下载目录: {download_dir}")
    else:
        print(f"✓ 下载目录已存在: {download_dir}")
    return True

def check_and_install_all():
    """Check and install all dependencies."""
    print("=" * 60)
    print("离线下载 Skill 初始化")
    print("=" * 60)
    print()
    
    all_ok = True
    
    # 1. Check aria2c
    print("[1/4] 检查 aria2...")
    aria2_installed, aria2_path, aria2_version = check_aria2c()
    if aria2_installed:
        print(f"✓ aria2 已安装: {aria2_path}")
        print(f"  版本: {aria2_version}")
    else:
        print("✗ aria2 未安装")
        if not install_aria2():
            all_ok = False
    
    print()
    
    # 2. Check aria2p
    print("[2/4] 检查 aria2p...")
    aria2p_installed, aria2p_version = check_aria2p()
    if aria2p_installed:
        print(f"✓ aria2p 已安装")
        print(f"  版本: {aria2p_version}")
    else:
        print("✗ aria2p 未安装")
        if not install_aria2p():
            all_ok = False
    
    print()
    
    # 3. Check download directory
    print("[3/4] 检查下载目录...")
    create_download_dir()
    
    print()
    
    # 4. Check/start daemon
    print("[4/4] 检查 aria2c 守护进程...")
    if check_aria2c_daemon():
        print("✓ aria2c 守护进程正在运行")
    else:
        if aria2_installed or check_aria2c()[0]:
            start_aria2c_daemon()
        else:
            print("✗ 跳过守护进程启动（aria2 未安装）")
            all_ok = False
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("✓ 初始化完成！所有依赖已就绪。")
        print()
        print("现在可以使用以下功能：")
        print("  - 下载文件: 提供URL链接即可下载")
        print("  - 清理文件: 说'清理下载文件'删除所有下载")
    else:
        print("⚠ 初始化完成，但存在一些问题。")
        print("请查看上面的错误信息并手动解决。")
    
    print("=" * 60)
    return all_ok

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="初始化离线下载 Skill 环境")
    parser.add_argument(
        "--check-only", "-c",
        action="store_true",
        help="仅检查环境，不安装"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="强制重新安装所有依赖"
    )
    
    args = parser.parse_args()
    
    if args.check_only:
        print("检查环境...")
        print()
        
        aria2_installed, aria2_path, aria2_version = check_aria2c()
        print(f"aria2: {'✓ 已安装' if aria2_installed else '✗ 未安装'}")
        if aria2_installed:
            print(f"  路径: {aria2_path}")
            print(f"  版本: {aria2_version}")
        
        aria2p_installed, aria2p_version = check_aria2p()
        print(f"aria2p: {'✓ 已安装' if aria2p_installed else '✗ 未安装'}")
        if aria2p_installed:
            print(f"  版本: {aria2p_version}")
        
        daemon_running = check_aria2c_daemon()
        print(f"aria2c 守护进程: {'✓ 运行中' if daemon_running else '✗ 未运行'}")
        
        download_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "downloads")
        print(f"下载目录: {'✓ 存在' if os.path.exists(download_dir) else '✗ 不存在'} ({download_dir})")
    else:
        check_and_install_all()

if __name__ == "__main__":
    main()
