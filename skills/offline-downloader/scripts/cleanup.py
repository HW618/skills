#!/usr/bin/env python3
"""
Cleanup script for offline-downloader skill.
Removes all files from the downloads directory.
"""

import sys
import os
import shutil
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
    """Check if required dependencies are installed (aria2c not needed for cleanup)."""
    # Check if download directory exists
    if not os.path.exists(DOWNLOAD_DIR):
        return True, "下载目录不存在（无需清理）"
    return True, "就绪"

def get_download_dir():
    """Get the download directory path."""
    return DOWNLOAD_DIR

def list_downloads():
    """List all files in the download directory."""
    if not os.path.exists(DOWNLOAD_DIR):
        print(f"Download directory does not exist: {DOWNLOAD_DIR}")
        return []
    
    files = []
    for item in os.listdir(DOWNLOAD_DIR):
        item_path = os.path.join(DOWNLOAD_DIR, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            files.append({
                "name": item,
                "path": item_path,
                "size": size
            })
        elif os.path.isdir(item_path):
            # Calculate directory size
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(item_path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(filepath)
            files.append({
                "name": item,
                "path": item_path,
                "size": total_size,
                "is_dir": True
            })
    
    return files

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

def cleanup_downloads(confirm=True):
    """
    Remove all files from the downloads directory.
    
    Args:
        confirm: If True, ask for confirmation before deleting
    
    Returns:
        True if cleanup was successful, False otherwise
    """
    if not os.path.exists(DOWNLOAD_DIR):
        print(f"Download directory does not exist: {DOWNLOAD_DIR}")
        print("Nothing to clean up.")
        return True
    
    files = list_downloads()
    
    if not files:
        print("Download directory is already empty.")
        return True
    
    # Show files to be deleted
    print(f"\nFiles in download directory ({DOWNLOAD_DIR}):")
    print("-" * 60)
    total_size = 0
    for file_info in files:
        size_str = format_size(file_info["size"])
        prefix = "[DIR] " if file_info.get("is_dir") else "      "
        print(f"{prefix}{file_info['name']} ({size_str})")
        total_size += file_info["size"]
    
    print("-" * 60)
    print(f"Total: {len(files)} items, {format_size(total_size)}")
    
    # Ask for confirmation
    if confirm:
        print("\n⚠️  WARNING: This will permanently delete ALL files listed above!")
        response = input("Are you sure you want to continue? (yes/no): ").strip().lower()
        if response not in ["yes", "y"]:
            print("Cleanup cancelled.")
            return False
    
    # Delete files
    deleted_count = 0
    failed_count = 0
    
    for file_info in files:
        try:
            if file_info.get("is_dir"):
                shutil.rmtree(file_info["path"])
            else:
                os.remove(file_info["path"])
            deleted_count += 1
        except Exception as e:
            print(f"Failed to delete {file_info['name']}: {e}")
            failed_count += 1
    
    # Report results
    print(f"\n✓ Cleanup completed!")
    print(f"  Deleted: {deleted_count} items")
    if failed_count > 0:
        print(f"  Failed: {failed_count} items")
    
    return True

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Clean up downloaded files")
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Skip confirmation prompt"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List files without deleting"
    )
    
    args = parser.parse_args()
    
    # Check dependencies (minimal for cleanup)
    ok, msg = check_dependencies()
    if not ok:
        print(f"Error: {msg}")
        sys.exit(1)
    
    if args.list:
        files = list_downloads()
        if not files:
            print("Download directory is empty or does not exist.")
        else:
            print(f"\nFiles in download directory ({DOWNLOAD_DIR}):")
            print("-" * 60)
            total_size = 0
            for file_info in files:
                size_str = format_size(file_info["size"])
                prefix = "[DIR] " if file_info.get("is_dir") else "      "
                print(f"{prefix}{file_info['name']} ({size_str})")
                total_size += file_info["size"]
            print("-" * 60)
            print(f"Total: {len(files)} items, {format_size(total_size)}")
    else:
        cleanup_downloads(confirm=not args.force)

if __name__ == "__main__":
    main()
