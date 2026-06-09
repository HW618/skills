---
name: offline-downloader
description: "Use when users want to download files from URLs, download links, initialize the download environment, or clean up downloaded files. Triggers on phrases like 'download this link', 'download this URL', 'help me download', 'initialize', 'init', 'setup download', 'clean downloads', 'clear downloaded files', or any request to download a file from a URL, initialize dependencies, or clean up download directory."
---

# Offline Downloader

A skill for downloading files from URLs using aria2p and managing downloaded files.

## Features

1. **Initialize Environment**: Detect and install missing dependencies (aria2, aria2p)
2. **URL Download**: Download files from any URL (HTTP/HTTPS/FTP)
3. **Cleanup**: Remove all downloaded files from the downloads directory

## Quick Start

### First Time Setup (Initialize)

When the user says "初始化", "initialize", "setup", or when running the skill for the first time:

1. Run the initialization script:
   ```bash
   python3 /Users/houston/.claude/skills/offline-downloader/scripts/init.py
   ```
2. The script will automatically:
   - Check if aria2 is installed (install if missing)
   - Check if aria2p is installed (install if missing)
   - Create the download directory
   - Start the aria2c daemon

**Example user messages:**
- "初始化离线下载"
- "初始化下载环境"
- "Setup download skill"
- "Initialize offline downloader"

### Check Environment Only

To check the environment without installing:
```bash
python3 /Users/houston/.claude/skills/offline-downloader/scripts/init.py --check-only
```

## Usage

### Download a file from URL

When the user provides a URL to download:

1. First, check if dependencies are installed (run init if needed)
2. Extract the URL from the user's message
3. Run the download script:
   ```bash
   python3 /Users/houston/.claude/skills/offline-downloader/scripts/download.py "<URL>"
   ```
4. Report the download status to the user

**Example user messages:**
- "下载这个链接 https://example.com/file.zip"
- "帮我下载 https://example.com/document.pdf"
- "Download this file https://example.com/image.jpg"

### Clean up downloaded files

When the user asks to clean up downloads:

1. Run the cleanup script:
   ```bash
   python3 /Users/houston/.claude/skills/offline-downloader/scripts/cleanup.py
   ```
2. Confirm the cleanup operation with the user

**Example user messages:**
- "清理下载文件"
- "删除所有下载的内容"
- "Clean up my downloads"

## Configuration

The default download directory is:
```
/Users/houston/.claude/skills/offline-downloader/downloads
```

To change the download directory, modify the `DOWNLOAD_DIR` variable in the scripts.

## Troubleshooting

### Dependencies not installed

Run the initialization script to automatically install dependencies:
```bash
python3 /Users/houston/.claude/skills/offline-downloader/scripts/init.py
```

### aria2c daemon not running

The initialization script will start the daemon automatically. Or manually:
```bash
aria2c --enable-rpc --rpc-listen-all=true --daemon=true
```

### Permission errors

Ensure the download directory has write permissions:
```bash
chmod 755 /Users/houston/.claude/skills/offline-downloader/downloads
```

## Script Reference

| Script | Purpose | Usage |
|--------|---------|-------|
| `init.py` | Initialize environment | `python3 init.py [--check-only]` |
| `download.py` | Download files | `python3 download.py <URL> [dir]` |
| `cleanup.py` | Clean downloads | `python3 cleanup.py [--force] [--list]` |

## Notes

- Downloads are saved to the skill's `downloads` subdirectory by default
- The cleanup operation deletes ALL files in the downloads directory
- Large files may take some time to download
- The skill supports HTTP, HTTPS, FTP, and magnet links
- Run `init.py` to automatically detect and install missing dependencies
