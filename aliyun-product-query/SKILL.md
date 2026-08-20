---
name: aliyun-product-query
description: 阿里云产品信息查询助手。面向销售、售前、架构师等角色，回答阿里云产品的功能特性、实例规格、性能参数、计费规则、价格、使用限制等问题。当用户询问阿里云/ECS/云服务器/云盘/OSS/NAS/VPC/SLB/RDS/PolarDB/Redis 等阿里云产品的"是什么/有什么功能/支持什么/怎么收费/什么规格/性能怎么样/价格多少/限制"等问题时，必须使用本 skill。即使用户只是随口问"阿里云的 XX 怎么样"或"XX 是否支持 YY"，只要涉及阿里云产品属性查询，都应触发。也适用于用户要求"更新阿里云产品索引/缓存"的场景。
---

# 阿里云产品查询助手

## 这个 skill 做什么

帮助销售、售前、架构师等角色快速回答阿里云产品问题：功能特性、实例规格、性能参数、计费规则、价格、使用限制等。

核心设计：**本地缓存优先，缺失才联网**。阿里云官方提供 agent 友好的 `llms.txt` markdown 接口，我们把导航页和产品主页缓存到本地，查询时优先读缓存，只在缓存缺失或过期时才联网补取。这样既快又省网络。

## 数据源

阿里云帮助文档为 LLM/Agent 提供了结构化 markdown 接口，分两层：

1. **导航页** `https://help.aliyun.com/zh/llms.txt`
   - 阿里云全部产品的索引，每条目含产品名 + 一句话简介 + 指向产品 llms.txt 的链接
   - 缓存到 `cache/_index/navigation.md`

2. **产品主页** `https://help.aliyun.com/zh/<product>/llms.txt`
   - 单个产品的完整文档目录，按"用户指南/产品简介/计费/API 参考"等分类组织
   - 每条目含文档标题、`.md` 源文件链接、内容摘要
   - 缓存到 `cache/<product>/llms.md`
   - 高价值子页（规格/价格/性能/限制）缓存到 `cache/<product>/pages/<slug>.md`

**适用范围**：中国站（aliyun.com）。国际站产品组合、地域、计费有差异，本 skill 不覆盖。

## 缓存结构

```
cache/
├── _index/
│   ├── navigation.md          # 导航页缓存
│   └── meta.json              # 导航页元数据（更新时间等）
├── ecs/
│   ├── llms.md                # ECS 产品主页缓存
│   ├── meta.json              # ECS 缓存元数据
│   └── pages/                 # 高价值子页缓存
│       ├── instance-families.md
│       ├── billing.md
│       └── ...
├── oss/
│   └── ...
└── _registry.json             # 全局产品注册表（已缓存产品列表 + 路径 + 更新时间）
```

## 核心工作流

### 工作流 1：更新索引

用户说"更新索引/更新缓存/刷新阿里云数据"等时触发。

**步骤：**

1. 运行 `python scripts/update_index.py`（无参数）更新导航页
   - 抓取 `https://help.aliyun.com/zh/llms.txt`
   - 写入 `cache/_index/navigation.md`
   - 更新 `cache/_index/meta.json` 的时间戳
2. 运行 `python scripts/update_index.py --product <name>` 更新指定产品
   - 从 `_registry.json` 或导航页查找产品的 llms.txt URL
   - 抓取后写入 `cache/<product>/llms.md`
   - 同时抓取高价值子页（见下文"高价值子页识别"）
3. 运行 `python scripts/update_index.py --all` 更新所有已注册产品
4. 运行 `python scripts/update_index.py --add <product>` 添加新产品到注册表并更新

**高价值子页识别**：产品主页 llms.md 中，标题或摘要含以下关键词的条目视为高价值，需缓存其 `.md` 源文件：
- 规格类：`规格`、`实例`、`instance`、`family`、`规格族`
- 性能类：`性能`、`performance`、`基准`、`突发`、`IOPS`、`吞吐`
- 计费类：`计费`、`价格`、`收费`、`billing`、`pricing`、`按量`、`包年包月`、`抢占`
- 限制类：`限制`、`配额`、`limit`、`quota`

### 工作流 2：回答用户问题

用户问阿里云产品问题时触发。**这是最高频的工作流。**

**步骤：**

1. **识别产品**：从用户问题中识别涉及的阿里云产品（ECS、OSS、RDS 等）。参考 `references/products.md` 的产品别名映射。

2. **检查缓存**：
   - 读 `cache/_registry.json` 看该产品是否已缓存
   - 若已缓存且未过期（meta.json 的 `updated_at` 在 30 天内），用缓存
   - 若未缓存或过期，**先提示用户**："ECS 产品缓存不存在/已过期，是否现在联网更新？" 用户确认后执行工作流 1 更新，再继续回答
   - 例外：若用户明确说"查最新的/联网查"，直接联网

3. **检索缓存内容**：
   - 读 `cache/<product>/llms.md` 找到与问题相关的条目
   - 若问题涉及规格/性能/计费等细节，读对应的 `cache/<product>/pages/<slug>.md`
   - 若缓存中没有足够信息，按需联网抓取该条目的 `.md` 源文件，写入 `pages/` 后再回答

4. **组织回答**：
   - **始终用中文回答**
   - 先给结论/要点总结（2-4 句），适合销售/售前快速理解
   - 再附关键参数/规格/价格表格（如适用）
   - 最后附**原文出处链接**（来自缓存的 `.md` 链接），便于用户深挖
   - 若信息可能已过时（缓存超过 30 天），在回答末尾标注"⚠️ 此信息基于 YYYY-MM-DD 的缓存，计费/价格类信息建议核对最新文档"

5. **回答模板**：
   ```
   ## <产品名> <问题主题>

   <2-4 句要点总结>

   <可选：关键参数表格>

   📖 原文出处：
   - [文档标题](url)
   ```

## 产品别名映射

用户可能用各种名称指代产品，需映射到标准 product key。完整映射见 `references/products.md`，常用：

| 用户可能的说法 | product key | 产品全名 |
|---|---|---|
| 云主机/云服务器/ECS | `ecs` | 云服务器 ECS |
| 轻量服务器/轻量应用 | `simple-application-server` | 轻量应用服务器 |
| 裸金属/弹性裸金属 | `ebm` | 弹性裸金属服务器 |
| GPU 云服务器/GPU | `ecs/gpu` | GPU 云服务器 |
| 云盘/磁盘/块存储 | `ecs`（云盘属 ECS） | 云盘（ECS 块存储） |
| NAS/文件存储 | `nas` | 文件存储 NAS |
| OSS/对象存储 | `oss` | 对象存储 OSS |
| VPC/专有网络 | `vpc` | 专有网络 VPC |
| EIP/弹性公网 IP | `eip` | 弹性公网 IP |
| SLB/负载均衡/ALB | `slb` | 负载均衡 SLB |
| CDN | `cdn` | CDN |
| RDS/云数据库 | `rds` | 云数据库 RDS |
| PolarDB | `polardb` | 云数据库 PolarDB |
| Redis | `redis` | 云数据库 Redis |

**产品 key 不确定时**：读 `cache/_index/navigation.md` 搜索产品名，找到对应的 llms.txt URL 中的 path 段即为 key。

## 网络抓取策略

优先用 `scripts/fetch_page.py`，它封装了两级策略：

1. **第一级：HTTP 抓取**（默认）
   - 用 `curl` 带浏览器 UA 抓取
   - llms.txt 是纯 markdown 文本，HTTP 抓取通常足够
   - 成功则返回内容

2. **第二级：浏览器降级**（HTTP 失败或返回异常时）
   - 用浏览器工具（open_browser_page 等）渲染页面
   - 配合防反爬手段：合理延时、浏览器 UA、禁用自动化检测特征
   - 读取页面内容

判断"异常"：HTTP 状态码非 200、返回内容含验证码/登录页特征、内容长度异常短（<100 字节）。

## 何时读哪些文件

- **回答产品问题前**：先读 `cache/_registry.json` 确认产品已缓存
- **产品 key 不确定**：读 `cache/_index/navigation.md` 搜索
- **需要产品别名映射**：读 `references/products.md`
- **执行更新命令**：读 `references/update_guide.md` 看详细步骤
- **抓取失败需排查**：读 `references/troubleshooting.md`

## 初始化

首次使用时，`cache/` 为空。若用户问产品问题而缓存未初始化，提示用户："检测到缓存为空，是否现在初始化（更新导航页 + 核心产品索引）？约需 1-2 分钟。" 用户确认后运行 `python scripts/update_index.py --init`。

核心产品初始集合（`--init` 会缓存这些）：
- 计算：`ecs`、`simple-application-server`、`ebm`
- 存储：`nas`、`oss`
- 网络：`vpc`、`eip`、`slb`、`cdn`
- 数据库：`rds`、`polardb`、`redis`

## 限制与注意事项

- **仅覆盖中国站**。国际站产品/地域/计费有差异，不处理。
- **缓存可能过时**。计费/价格类信息变化快，回答时注意标注缓存时间，建议用户核对最新文档。
- **不提供实时价格计算器**。价格随地域/规格/时长变化大，本 skill 只提供计费规则和参考价，精确报价请指引用户用阿里云官网价格计算器。
- **不替代官方工单/售后**。涉及账号、资源状态、故障排查等问题，指引用户提工单。
