# 缓存目录

此目录存放阿里云产品文档的本地缓存。

首次使用前为空。运行以下命令初始化：

```bash
python scripts/update_index.py --init
```

结构：
- `_index/` — 导航页缓存
- `_registry.json` — 全局产品注册表
- `<product>/` — 各产品缓存（llms.md + meta.json + pages/）
