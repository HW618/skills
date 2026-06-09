#!/usr/bin/env python3
"""
Download script for offline-downloader skill.
Uses aria2p to download files from URLs.
"""

import sys
import os
import time
import subprocess

# Default download directory (skill's downloads subdirectory)
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "downloads")

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

def check_dependencies():
    """Check if all dependencies are installed."""
    # Check aria2c
    success, _, _ = run_command("which aria2c", check=False)
    if not success:
        return False, "aria2 未安装"
    
    # Check aria2p
    try:
        import aria2p
    except ImportError:
        return False, "aria2p 未安装"
    
    # Check daemon
    success, stdout, _ = run_command("ps aux | grep 'aria2c.*enable-rpc' | grep -v grep", check=False)
    if not (success and stdout):
        return False, "aria2c 守护进程未运行"
    
    return True, "所有依赖已就绪"

def auto_init():
    """Automatically initialize dependencies if needed."""
    ok, msg = check_dependencies()
    if ok:
        return True
    
    print(f"检测到问题: {msg}")
    print("正在自动初始化...")
    print()
    
    # Run init script
    init_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "init.py")
    success, stdout, stderr = run_command(f"python3 {init_script}")
    
    if success:
        print(stdout)
        return True
    else:
        print(f"初始化失败: {stderr}")
        return False

def ensure_download_dir():
    """Create download directory if it doesn't exist."""
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    return DOWNLOAD_DIR

def get_aria2_api():
    """Initialize and return aria2p API connection."""
    import aria2p
    
    try:
        api = aria2p.API(
            aria2p.Client(
                host="http://localhost",
                port=6800,
                secret=""
            )
        )
        # Test connection
        api.get_stats()
        return api
    except Exception as e:
        print(f"Error: Cannot connect to aria2c daemon: {e}")
        print("尝试重新启动守护进程...")
        
        # Try to restart daemon
        run_command("aria2c --enable-rpc --rpc-listen-all=true --daemon=true", check=False)
        time.sleep(2)
        
        try:
            api = aria2p.API(
                aria2p.Client(
                    host="http://localhost",
                    port=6800,
                    secret=""
                )
            )
            api.get_stats()
            return api
        except Exception as e2:
            print(f"Error: 仍然无法连接: {e2}")
            print("请手动启动 aria2c 守护进程:")
            print("  aria2c --enable-rpc --rpc-listen-all=true --daemon=true")
            sys.exit(1)

def download_file(url, download_dir=None):
    """
    Download a file from the given URL.
    
    Args:
        url: The URL to download from
        download_dir: Optional custom download directory
    
    Returns:
        Download object if successful
    """
    if download_dir is None:
        download_dir = ensure_download_dir()
    
    api = get_aria2_api()
    
    # Set download options
    options = {
        "dir": download_dir
    }
    
    try:
        # Add download - returns a single Download object
        download = api.add_uris([url], options=options)
        if download:
            print(f"Download started: {download.name}")
            print(f"Saving to: {download_dir}")
            print(f"Download GID: {download.gid}")
            
            # Wait for download to complete
            while not download.is_complete:
                download.update()
                if download.has_failed:
                    print(f"Download failed: {download.error_message}")
                    return None
                
                # Show progress
                progress = download.progress
                speed = download.download_speed
                print(f"\rProgress: {progress:.1f}% | Speed: {format_speed(speed)}", end="", flush=True)
                time.sleep(1)
            
            print(f"\nDownload completed: {download.name}")
            return download
        else:
            print("Error: Failed to add download")
            return None
    except Exception as e:
        print(f"Error during download: {e}")
        return None

def format_speed(speed_bytes):
    """Format download speed to human readable string."""
    if speed_bytes < 1024:
        return f"{speed_bytes} B/s"
    elif speed_bytes < 1024 * 1024:
        return f"{speed_bytes / 1024:.1f} KB/s"
    else:
        return f"{speed_bytes / (1024 * 1024):.1f} MB/s"

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python download.py <URL> [download_dir]")
        print("Example: python download.py https://example.com/file.zip")
        sys.exit(1)
    
    url = sys.argv[1]
    download_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Check and auto-initialize dependencies
    ok, msg = check_dependencies()
    if not ok:
        print(f"检测到问题: {msg}")
        print("正在自动初始化...")
        if not auto_init():
            print("初始化失败，请手动运行: python3 /Users/houston/.claude/skills/offline-downloader/scripts/init.py")
            sys.exit(1)
        print()
    
    print(f"Starting download: {url}")
    result = download_file(url, download_dir)
    
    if result:
        print(f"\n✓ Download successful!")
        print(f"  File: {result.name}")
        print(f"  Size: {format_size(result.total_length)}")
        print(f"  Location: {result.dir}")
    else:
        print("\n✗ Download failed")
        sys.exit(1)

def format_size(size_bytes):
    """Format file size to human readable string."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"

if __name__ == "__main__":
    main()
