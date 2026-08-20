# 更新索引详细指南

## 命令一览

```bash
# 初始化（首次使用）：导航页 + 12 个核心产品
python scripts/update_index.py --init

# 仅更新导航页
python scripts/update_index.py

# 更新指定产品（含高价值子页）
python scripts/update_index.py --product ecs

# 更新指定产品（仅主页，不抓子页，更快）
python scripts/update_index.py --product ecs --no-subpages

# 更新所有已注册产品
python scripts/update_index.py --all

# 添加新产品到注册表并更新
python scripts/update_index.py --add nas
```

## 何时更新

- **首次使用**：运行 `--init`
- **用户明确要求"更新/刷新缓存"**：按用户指定范围更新
- **缓存过期**（meta.json 的 `updated_at` 超过 30 天）：回答问题前提示用户更新
- **新增产品需求**：用户问的产品未缓存，用 `--add` 添加

## 核心产品初始集合

`--init` 会缓存这些产品：

| 类别 | 产品 key |
|---|---|
| 计算 | `ecs`、`simple-application-server`、`ebm` |
| 存储 | `nas`、`oss` |
| 网络 | `vpc`、`eip`、`slb`、`cdn` |
| 数据库 | `rds`、`polardb`、`redis` |

## 高价值子页识别

产品主页 llms.md 中，标题或摘要含以下关键词的条目会被缓存其 `.md` 源文件：

- **规格类**：规格、实例、instance、family、规格族
- **性能类**：性能、performance、基准、突发、IOPS、吞吐
- **计费类**：计费、价格、收费、billing、pricing、按量、包年包月、抢占
- **限制类**：限制、配额、limit、quota

## 输出文件

每次更新会生成/更新：

- `cache/<product>/llms.md`：产品主页
- `cache/<product>/meta.json`：元数据（更新时间、子页列表）
- `cache/<product>/pages/<slug>.md`：高价值子页
- `cache/_registry.json`：全局注册表

## 抓取失败排查

若 `fetch_page.py` 返回失败：

1. 先看错误信息：HTTP 状态码、内容异常特征
2. HTTP 失败时，用浏览器工具降级：
   - `open_browser_page` 打开 URL
   - `read_page` 读取页面内容
   - 提取文本写入目标文件
3. 详见 `troubleshooting.md`
