# Offline Downloader 使用说明

## 快速开始

### 1. 安装依赖

#### 安装 aria2
```bash
# macOS (使用 Homebrew)
brew install aria2

# Ubuntu/Debian
sudo apt-get install aria2

# Windows (使用 Chocolatey)
choco install aria2
```

#### 安装 aria2p
```bash
pip install aria2p
```

### 2. 启动 aria2c 守护进程

```bash
aria2c --enable-rpc --rpc-listen-all=true --daemon=true
```

### 3. 使用下载功能

#### 命令行方式
```bash
# 下载单个文件
python /Users/houston/.claude/skills/offline-downloader/scripts/download.py "https://example.com/file.zip"

# 下载到指定目录
python /Users/houston/.claude/skills/offline-downloader/scripts/download.py "https://example.com/file.zip" "/path/to/save"
```

#### 通过 Skill 触发
当你说以下内容时，skill会自动触发：
- "下载这个链接 https://example.com/file.zip"
- "帮我下载 https://example.com/document.pdf"
- "Download this file https://example.com/image.jpg"

### 4. 使用清理功能

#### 命令行方式
```bash
# 列出下载目录中的文件
python /Users/houston/.claude/skills/offline-downloader/scripts/cleanup.py --list

# 清理下载目录（需要确认）
python /Users/houston/.claude/skills/offline-downloader/scripts/cleanup.py

# 强制清理（跳过确认）
python /Users/houston/.claude/skills/offline-downloader/scripts/cleanup.py --force
```

#### 通过 Skill 触发
当你说以下内容时，skill会自动触发：
- "清理下载文件"
- "删除所有下载的内容"
- "Clean up my downloads"

## 配置说明

### 默认下载目录
```
/Users/houston/.claude/skills/offline-downloader/downloads
```

### 修改下载目录
编辑 `scripts/download.py` 和 `scripts/cleanup.py` 中的 `DOWNLOAD_DIR` 变量。

### aria2c 配置
可以通过配置文件自定义 aria2c 行为：
```bash
# 创建配置文件
mkdir -p ~/.aria2
cat > ~/.aria2/aria2.conf << 'CONF'
# RPC 设置
enable-rpc=true
rpc-listen-all=true
rpc-allow-origin-all=true

# 下载设置
max-concurrent-downloads=5
continue=true
max-connection-per-server=16
min-split-size=1M
split=16

# 下载目录
dir=/Users/houston/.claude/skills/offline-downloader/downloads
CONF
```

## 支持的协议

- HTTP/HTTPS
- FTP
- SFTP
- BitTorrent (通过 magnet 链接)
- Metalink

## 常见问题

### Q: 连接 aria2c 失败
**A:** 确保 aria2c 守护进程正在运行：
```bash
# 检查进程
ps aux | grep aria2c

# 启动守护进程
aria2c --enable-rpc --rpc-listen-all=true --daemon=true
```

### Q: 下载速度慢
**A:** 可以调整 aria2c 配置：
```bash
# 增加并发连接数
max-connection-per-server=32

# 增加分片数
split=32
```

### Q: 如何查看下载进度
**A:** 使用以下命令：
```bash
# 查看活跃下载
aria2p show

# 交互式界面
aria2p top
```

### Q: 如何暂停/恢复下载
**A:** 使用 aria2p 命令：
```bash
# 暂停所有下载
aria2p pause --all

# 恢复所有下载
aria2p resume --all
```

## 高级用法

### 使用 magnet 链接
```bash
python /Users/houston/.claude/skills/offline-downloader/scripts/download.py "magnet:?xt=urn:btih:..."
```

### 批量下载
创建一个包含URL的文件（每行一个URL），然后：
```bash
aria2p add -f urls.txt
```

### 设置下载限速
```bash
# 全局限速 (单位: 字节/秒)
aria2c --enable-rpc --max-overall-download-limit=1M

# 单任务限速
aria2c --enable-rpc --max-download-limit=500K
```

## 脚本参数说明

### download.py
```
用法: python download.py <URL> [download_dir]

参数:
  URL          要下载的文件链接
  download_dir 可选，自定义下载目录

示例:
  python download.py https://example.com/file.zip
  python download.py https://example.com/file.zip /path/to/save
```

### cleanup.py
```
用法: python cleanup.py [选项]

选项:
  --force, -f    跳过确认提示，直接删除
  --list, -l     仅列出文件，不删除

示例:
  python cleanup.py --list    # 查看下载目录内容
  python cleanup.py           # 清理（需要确认）
  python cleanup.py --force   # 强制清理
```

## 技术支持

如遇到问题，请检查：
1. aria2 是否正确安装
2. aria2c 守护进程是否运行
3. aria2p 是否安装
4. 网络连接是否正常
5. 下载目录是否有写入权限
