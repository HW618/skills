# 阿里云云服务器 ECS 实例规格族整理

> 面向售前/客户讲解用：按"规格族群 → 规格族 → 适用场景"三层组织，先讲大类区别，再讲细分场景。

## 一句话总结

阿里云 ECS 实例按 **CPU 架构 + 业务场景** 划分为 **6 大规格族群**：x86 计算（企业级/入门级）、ARM 计算、弹性裸金属、高性能计算 HPC、超级计算集群 SCC、异构计算（GPU/FPGA）。每个族群下再按"通用 g / 计算 c / 内存 r / 大数据 d / 本地 SSD i / 高主频 hf"等细分规格族，命名中的字母代表性能领域、数字代表代际、后缀代表 CPU 厂商或增强特性。

---

## 一、6 大规格族群总览（先讲大类）

| 规格族群 | 特点 | 典型适用场景 |
|---|---|---|
| **x86 计算规格族（企业级）** | 基于 x86 架构，每个 vCPU 对应一个超线程，性能稳定、资源独享。CPU 厂商含 Intel/AMD/海光 | 各种企业级应用、数据库、视频编解码、数据分析 |
| **x86 计算规格族（入门级）** | 共享型/突发型，资源性能共享，无法保证计算性能稳定，但成本低 | 中小网站、个人开发、测试 |
| **ARM 计算规格族** | 基于 ARM 架构（倚天 710 / Ampere Altra），每个 vCPU 对应一个物理核，性能稳定且资源独享 | 容器、微服务、网站和应用服务器、基于 CPU 的机器学习 |
| **弹性裸金属服务器（ebm）** | 融合物理机与云服务器优势，业务可直接访问处理器和内存，无虚拟化开销，具备物理机级隔离 | 传统非虚拟化场景上云、容器编排、License 敏感场景 |
| **高性能计算（HPC）** | 专为 HPC 工作负载优化，物理核设计无超线程，支持 eRDMA 低延迟网络 | 科学计算、AI 训练、CAE/CFD 仿真 |
| **超级计算集群（SCC）** | 在弹性裸金属基础上加入 RDMA 高速互联，RoCE 网络达 InfiniBand 级别 | 大规模 HPC、AI 并行计算 |
| **异构计算（GPU/FPGA）** | 提供 GPU/FPGA 加速能力，结合 GPU 算力与 CPU 算力 | AI 训练/推理、图形图像处理、视频转码 |

---

## 二、企业级 x86 计算规格族（最常跟客户讲的部分）

按"性能领域字母 + 代际数字 + 厂商后缀"命名，例如 `ecs.g8ae.4xlarge` = 通用型 + 第 8 代 + AMD 增强 + 16 vCPU。

### 命名规则速查

| 字母 | 含义 | CPU:内存 | 适用场景 |
|---|---|---|---|
| **g** | 通用型（general） | 1:4 | 通用互联网应用、数据库、Web、Java 应用、游戏、搜索推广 |
| **c** | 计算型（computational） | 1:2 | 计算密集型 Web 前端、视频编码、批量计算、ML 推理、游戏服务器 |
| **r** | 内存型（ram） | 1:8 | 内存数据库、Redis/Kafka/ES、数据分析挖掘、Java 大内存应用 |
| **u** | 通用算力型（universal） | 1:1/1:2/1:4/1:8 | 对价格敏感的企业级客户，中小型应用/数据库/网站 |
| **re** | 内存增强型 | — | 大内存需求场景（SAP HANA 等） |
| **hf（c/g/r）** | 高主频型 | 1:2/1:4/1:8 | 大型多人在线游戏、HPC 科学计算、中大型数据库 |
| **i** | 本地 SSD 型 | 1:4/1:8 | OLTP、高性能关系型数据库、NoSQL（Cassandra/MongoDB）、ES、EMR 存算分离 |
| **d** | 大数据型 | 1:4 | Hadoop MapReduce、HDFS、Hive、HBase、ES、Kafka |
| **s（t/e）** | 共享型/突发型/经济型 | — | 中小网站、个人开发（入门级） |

**后缀含义**：`y`=倚天 ARM、`a`=AMD、`ae`=AMD 增强、`i`=Intel、`h`=海光、`se`=存储增强、`ne/nex`=网络增强、`t`=安全增强（vTPM）、`p`=持久内存、`re`=RDMA 增强。数字越大代际越新、性价比越高。

### 各系列在售规格族（按厂商分组）

#### 通用型 g 系列（1:4，Web/DB/Java 应用首选）
- **Intel**：g9i、g8i、g8ine（网络增强）、g7、g6e、g6
- **AMD**：g9ae、g9a、g8a、g8ae、g7a、g6a
- **海光**：g9h、g7h、g6h
- 不推荐（售罄备选）：g5、sn2ne

#### 计算型 c 系列（1:2，计算密集型）
- **Intel**：c9i、c8i、c8ine、c7、c6e、c6
- **AMD**：c9ae、c9a、c8a、c8ae、c7a、c6a
- 不推荐：ic5、c5、sn1ne

#### 内存型 r 系列（1:8，内存密集型）
- **Intel**：r9i、r8i、r7p、r7、r6e、r6
- **AMD**：r9ae、r9a、r8a、r8ae、r7a、r6a
- 不推荐：r5、se1ne、se1

#### 通用算力型 U 实例（多配比，性价比导向）
- u2a（AMD）、u2i（Intel）、u1
- 部署在多代际服务器平台，价格低于 g/c/r 系列，但不保证性能一致性

#### 大数据型 d 系列（1:4，配大容量本地 HDD）
- 推荐：d3s（存储密集）、d3c（计算密集）、d2c、d2s
- 不推荐：d1ne
- 适用于 Hadoop/HDFS/Hive/HBase/Kafka/ES，**不支持变配**

#### 本地 SSD 型 i 系列（1:4/1:8，配 NVMe SSD 本地盘）
- Granite Rapids：i5g、i5ge、i5e、i5
- Ice Lake：i4、i4g、i4r、i4p（性能增强）
- Cascade Lake：i3g、i3
- Skylake：i2、i2g、i2ne、i2gne
- 适用于 OLTP、NoSQL、ES、大数据存算分离

#### 高主频 hf 系列（主频 3.4–3.8 GHz）
- 推荐（Intel 至强 6 P-core）：hfc9i、hfg9i、hfr9i
- Sapphire Rapids：hfc8i、hfg8i、hfr8i
- Cooper Lake：hfc7、hfg7、hfr7
- 适用于游戏、HPC 科学计算、中大型数据库

#### 增强型变体
- **存储增强（se）**：g8ise、g7se、c7se、r7se — 搭配 ESSD 提升存储 I/O
- **网络增强（ne/nex）**：g8ine、c8ine、g7nex、c7nex、g7ne、g5ne — 高 PPS 场景
- **安全增强（t）**：g9it、r9it、g7t、c7t、r7t、g6t、c6t — 支持 vTPM 可信计算
- **内存增强（re）**：re8、re7p、re6p（持久内存）、re6 — SAP HANA 等大内存场景

---

## 三、入门级 x86 计算规格族

| 规格 | 特点 | 适用场景 |
|---|---|---|
| **e（经济型）** | 推荐 | 中小网站、个人开发 |
| **t6（突发性能）** | 推荐 | CPU 利用率低但有突发需求的场景 |
| s6、t5、v5、xn4/n4/mn4/e4 | 不推荐（售罄备选） | — |

---

## 四、企业级 ARM 计算规格族

| 处理器 | 规格族 | 适用场景 |
|---|---|---|
| 阿里云倚天 710 | g8y、c8y、r8y | 容器、微服务、网站和应用服务器、高性能计算、基于 CPU 的机器学习 |
| Ampere Altra | g6r、c6r | 同上 |

---

## 五、弹性裸金属服务器（ebm）

按通用 g / 计算 c / 内存 r / 高主频 hf / GPU 计算型 gn 分类，命名前缀 `ebm`。例如 ebmg9ae、ebmc9i、ebmr9ae、ebmg8y 等。适用于容器编排（K8s）、传统非虚拟化应用上云、License 敏感场景。

---

## 六、HPC 与 SCC

| 规格 | 特点 |
|---|---|
| **HPC**：hpc9a、hpc8i、hpc8ae、hpc7ip、hpc6id | 物理核无超线程，支持 eRDMA，仅按量付费（可抵扣节省计划），不支持变配 |
| **SCC**：sccg7、sccc7、sccgn7ex | 弹性裸金属 + RDMA 互联，RoCE 达 InfiniBand 级，适用于大规模并行计算 |

---

## 七、异构计算（GPU/FPGA）

| 类型 | 代表规格族 | 适用场景 |
|---|---|---|
| GPU 虚拟化型 | sgn8ia、sgn7i-vws、vgn7i-vws、vgn6i-vws | 云桌面、轻量 GPU 推理 |
| GPU 计算型 | gn9gc、gn8v/gn8v-tee、gn8is、gn7e、gn7i、gn7、gn7r、gn6i、gn6e、gn6v | AI 训练/推理、深度学习、图形图像处理 |
| 异构服务型 | video-trans | 视频转码、图像/视频内容处理、帧图像提取 |

**GPU 选型建议**：深度学习训练 GPU:CPU = 1:8~1:12；通用深度学习 1:4~1:48；图像识别推理 1:4~1:12；语音识别推理 1:16~1:48。

---

## 八、按业务场景快速选型（售前跟客户对号入座）

| 业务场景 | 推荐规格族 | CPU:内存 |
|---|---|---|
| 通用 Web/应用服务器、Java 应用 | g 系列（g7/g8i/g8a/g9i） | 1:4 |
| 高网络收发包（弹幕、负载均衡 Nginx） | g 系列 + ne/nex 后缀，或 c7nex、g5ne | 1:4 |
| 计算密集型（视频编码、批量计算、ML 推理） | c 系列（c7/c8i/c8a/c9i） | 1:2 |
| 高性能计算/科学计算 | hfc 系列（hfc7/hfc8i/hfc9i）或 HPC 系列 | 1:2 |
| 大型多人在线游戏（端游） | hfc 系列（高主频） | 1:2 |
| 手游/页游 | g 系列（g6e/g7） | 1:4 |
| 内存数据库/Redis/Kafka/ES | r 系列（r7/r8i/r8a/r9i） | 1:8 |
| 高性能关系型数据库/NoSQL | i 系列（i4/i4g/i4r） | 1:4/1:8 |
| 中小型数据库 | g 系列 + ESSD | 1:4 |
| Hadoop/HDFS/Hive/HBase | d 系列（d3s/d3c/d2s/d2c） | 1:4 |
| 深度学习训练 | gn7e/gn8v/gn8is（GPU:CPU 1:8~1:12） | — |
| 图像识别推理 | gn7i/gn6i（GPU:CPU 1:4~1:12） | — |
| 容器编排 K8s | 弹性裸金属 ebm 系列 | — |
| 对价格敏感的企业级应用 | U 实例（u1/u2a/u2i） | 多配比 |
| 中小网站/个人开发 | e、t6（入门级） | — |

---

## 九、规格大小命名规则

`ecs.<规格族>.<规格大小>`，规格大小表示 vCPU 核数：
- `small` = 1 vCPU
- `large` = 2 vCPU
- `xlarge` = 4 vCPU
- `2xlarge` = 8 vCPU
- `3xlarge` = 12 vCPU
- `4xlarge` = 16 vCPU，以此类推

例如 `ecs.g8ae.4xlarge` = 通用型 + 第 8 代 + AMD 增强 + 16 vCPU + 64 GiB 内存（1:4）。

---

## 售前沟通要点

1. **先问业务场景**：Web? 数据库? 大数据? AI? 游戏? — 决定大类。
2. **再问性能要求**：CPU 密集还是内存密集? 是否高网络 PPS? 是否高 IOPS? — 决定 g/c/r/i/d/hf。
3. **再问预算**：对价格敏感选 U 实例或入门级；要性能稳定选企业级 g/c/r。
4. **代际选择**：数字越大越新，性价比越高，优先推荐 8/9 代。
5. **厂商选择**：Intel（i）兼容性最好；AMD（a/ae）性价比高；倚天 ARM（y）容器/微服务场景性价比突出。
6. **变配限制**：d 系列、HPC 系列不支持变配；跨厂商变配需检查操作系统兼容性。
7. **精确报价**：用 [ECS 价格计算器](https://www.aliyun.com/price/product?#/commodity/vm) 按地域/规格/时长预估。

⚠️ 此信息基于 2026-07-16 的本地缓存，规格族在售状态和具体规格参数可能随地域变化，建议跟客户确认目标地域后核对最新文档。

---

📖 原文出处：
- [在售实例规格族汇总](https://help.aliyun.com/zh/ecs/user-guide/overview-of-instance-families.md)
- [实例规格分类与命名](https://help.aliyun.com/zh/ecs/user-guide/instance-specification-naming-and-classification.md)
- [ECS 实例规格选型指导](https://help.aliyun.com/zh/ecs/user-guide/best-practices-for-instance-type-selection.md)
- [通用算力型 U 实例](https://help.aliyun.com/zh/ecs/user-guide/general-work-force.md)
- [通用型实例 g 系列](https://help.aliyun.com/zh/ecs/user-guide/general-purpose-instance-families.md)
- [计算型实例 c 系列](https://help.aliyun.com/zh/ecs/user-guide/compute-optimized-instance-families.md)
- [内存型实例 r 系列](https://help.aliyun.com/zh/ecs/user-guide/memory-optimized-instance-families-1.md)
- [大数据型实例 d 系列](https://help.aliyun.com/zh/ecs/user-guide/big-data-instance-families.md)
- [本地盘实例 i 系列](https://help.aliyun.com/zh/ecs/user-guide/instance-families-with-local-ssds.md)
- [高主频实例 hf 系列](https://help.aliyun.com/zh/ecs/user-guide/instance-families-with-high-clock-speeds.md)
- [HPC 优化型实例](https://help.aliyun.com/zh/ecs/user-guide/overview-of-hpc-optimized-instance-families.md)
- [SCC 超级计算集群实例](https://help.aliyun.com/zh/ecs/user-guide/overview-40.md)
