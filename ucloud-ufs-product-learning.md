# UCloud UFS 产品学习手册

竞品已确认：阿里云 **文件存储 NAS（Network Attached Storage）**  
资料来源：UCloud 官方 UFS 文档、阿里云官方 NAS 文档。

## 1. 产品概述

- **产品定位**：UFS（UCloud File Storage）是 UCloud 的分布式文件系统产品，为 UCloud 公有云、物理云、托管云上的主机提供高可用、高可靠、可扩展的共享文件存储能力。来源：[UCloud UFS 产品文档](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)
- **核心价值**：让多台主机通过文件系统方式共享同一份数据，适合数据备份、AI 数据分析、高性能 Web 站点、容器数据共享等场景。来源：[UCloud UFS 产品文档](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)
- **产品类型**：
  - 容量型：使用 SATA 介质，强调低成本、大容量。
  - 性能型：使用 SSD（Solid State Drive）介质，强调低延迟 IO（Input/Output）。
- **协议支持**：支持基于 TCP（Transmission Control Protocol）的 NFS（Network File System）和 SMB（Server Message Block）协议。来源：[UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)

## 2. 产品功能

| 功能 | 说明 | 售前关注点 | 来源 |
| --- | --- | --- | --- |
| 共享文件存储 | 多台主机可通过挂载点访问同一个文件系统 | 适合多节点共享数据、容器共享目录、Web 内容共享 | [UCloud UFS](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 容量型/性能型 | 容量型偏成本和容量，性能型偏低延迟 | 根据客户是“便宜存大量文件”还是“低延迟访问”选型 | [UCloud UFS](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 在线扩容 | 文件系统支持扩容，业务对扩容无感知 | 适合容量持续增长业务，但要提醒“不支持缩容” | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| VPC 内访问 | 挂载点位于 VPC 内，通过 VPC 控制访问范围 | 客户跨项目组、跨地域访问时，需要提前确认网络打通方案 | [UCloud UFS FAQ](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 回收站 | 文档包含回收站能力 | 可作为误删恢复能力沟通点，但具体能力边界需以当前控制台和文档为准 | [UCloud UFS 产品文档](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |

## 3. 产品特点

- **文件级共享**：区别于云硬盘这类块存储，UFS 面向多个主机共享访问同一文件系统。
- **协议兼容**：支持 NFS 和 SMB，能够兼容 Linux、Windows 及基于 POSIX（Portable Operating System Interface）语义的应用。来源：[UCloud UFS 产品优势](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)
- **容量弹性**：单文件系统可扩容，容量型与性能型分别服务不同负载。
- **VPC 网络隔离**：访问基于 VPC 设计，强调传输路径内的安全可靠。来源：[UCloud UFS 产品概述](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)

## 4. 产品优势

| 优势 | 说明 | 售前解读 | 来源 |
| --- | --- | --- | --- |
| 可靠性 | 三副本机制，副本跨机柜部署，数据可靠性 99.999999% | 适合对共享文件数据可靠性有要求的业务，但可用性 SLA 需单独确认 | [UCloud UFS 产品优势](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 高弹性 | 支持弹性扩容，最大可到百 PB 级别，具体受产品限制约束 | 面向数据持续增长业务时可强调扩容能力 | [UCloud UFS 产品概述](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 共享性 | 不限制可挂载单个文件系统的主机数量 | 多节点并发读取共享数据是核心卖点 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 易用性 | 支持 NFS/SMB 和 POSIX 语义，文件系统工具可直接使用 | 应用迁移成本较低，适合传统应用上云 | [UCloud UFS 产品优势](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |

## 5. 产品性能

| 性能维度 | UCloud UFS 文档信息 | 售前解读 | 来源 |
| --- | --- | --- | --- |
| 容量型吞吐 | 单 TB 吞吐峰值 120 Mbps；吞吐随容量线性增长；上限 20 Gbps | 容量型不是低延迟优先，更适合备份、日志、归档、低延迟要求不高的 Web | [UCloud UFS 产品性能](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 容量型吞吐公式 | `吞吐(Mbps)=20Mbps/TB*(容量-1TB)+120Mbps` | 需要根据客户容量估算可获得吞吐，不要只按容量判断性能 | [UCloud UFS 产品性能](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 性能型吞吐 | 最高可达 10 Gbps | 面向低延迟和较高 IO 场景，但更高吞吐需联系技术支持 | [UCloud UFS 产品性能](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 性能型 4K 随机读 | 平均延迟 5 ms，IOPS 23K | 可用于小文件随机读较多场景的初步性能参考 | [UCloud UFS 产品性能](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 性能型 4K 随机写 | 平均延迟 8 ms，IOPS 17K | 写密集场景需要结合业务压测验证 | [UCloud UFS 产品性能](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |

## 6. 产品规格

| 规格维度 | UCloud UFS 文档信息 | 选型意义 | 来源 |
| --- | --- | --- | --- |
| 单账号实例数 | 单账号可创建文件系统实例 100 个 | 多业务线、多环境隔离时要评估实例数量 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 容量型最大购买容量 | 100 TB；更大空间需联系技术支持 | 大容量项目要提前确认区域和商务支持 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 性能型最大购买容量 | 20 TB；更大空间需联系技术支持 | 性能型不适合只追求极大容量的低成本场景 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 单文件大小 | 最大 1 TB | 大模型文件、超大备份包、视频素材等要确认单文件大小 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| inode 数 | 单文件系统 100,000,000 | 海量小文件场景必须重点评估 inode | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 挂载点数量 | 单文件系统最多 5 个挂载点 | 多 VPC 访问要规划挂载点和网络架构 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |

## 7. 使用限制与使用说明

| 限制/说明 | 影响 | 售前提醒 | 来源 |
| --- | --- | --- | --- |
| 只支持扩容，不支持缩容 | 购买过大后无法缩小容量 | 前期容量规划要保守，结合增长曲线分阶段扩容 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 不支持按需使用 | 需要预先购买容量 | 对比阿里云 NAS 时，计费灵活性要单独说明 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| NFSv3 不支持 ACL 和 LOCK | 可能影响权限控制和文件锁场景 | 老应用迁移前需确认协议依赖 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| NFSv4.0 不支持部分属性、OP 和 Delegation | 某些高级 NFS 语义不可用 | 对文件系统语义敏感的应用要做兼容性验证 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| SMB 不支持创建大小写同名文件/目录 | Windows 或混合系统场景可能遇到兼容性问题 | 跨平台文件共享要提前确认命名规范 | [UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |
| 跨地域访问会增加延迟和可能的费用 | 影响体验和成本 | 强烈建议文件系统与主机同地域部署 | [UCloud UFS FAQ](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf) |

## 8. 应用场景

### 场景一：备份、日志、归档类共享存储

- **场景特点**：数据量大、写入持续、访问频率不一定高，对极低延迟要求通常较弱。
- **客户需求**：希望多个业务节点统一写入日志或备份文件，减少本地磁盘管理。
- **客户痛点**：本地盘容量分散、扩容麻烦、跨节点同步复杂。
- **选型关注点**：容量、成本、吞吐、扩容方式、是否需要缩容。
- **UCloud 适配点**：UFS 容量型使用 SATA 介质，文档推荐用于日志备份、数据库备份、数据归档等。来源：[UCloud UFS 应用场景](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)
- **售前提醒**：UFS 不支持按需使用和缩容，容量规划要注意。来源：[UCloud UFS 产品限制](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)

### 场景二：AI 数据分析与大数据共享

- **场景特点**：多节点读取同一批训练数据或分析数据，常见于 AI、数据分析、大数据处理。
- **客户需求**：多台计算节点共享数据集，减少数据复制。
- **客户痛点**：对象存储改造成本高，本地盘无法天然共享，数据分发耗时。
- **选型关注点**：吞吐、IOPS（Input/Output Operations Per Second）、小文件性能、延迟、并发客户端数量。
- **UCloud 适配点**：UFS 性能型面向低延迟场景，文档推荐用于 AI 数据分析、大数据处理、多节点数据共享。来源：[UCloud UFS 应用场景](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)
- **售前提醒**：如果客户明确要求百万级 IOPS 或亚毫秒延迟，要谨慎承诺，建议联合技术团队压测。

### 场景三：容器数据共享

- **场景特点**：容器调度位置不固定，需要 Pod 迁移后仍能访问原数据。
- **客户需求**：容器应用需要 Persistent Volume（PV，持久卷）或共享配置、共享上传目录。
- **客户痛点**：本地存储与节点绑定，容器漂移后数据访问困难。
- **UCloud 适配点**：UFS 文档推荐性能型用于面向容器的数据共享。来源：[UCloud UFS 应用场景](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)
- **阿里云参考**：阿里云 NAS 明确支持容器 PV 场景，并提供加速客户端、目录配额、回收站等能力。来源：[阿里云 NAS 应用场景](https://help.aliyun.com/zh/nas/product-overview/scenarios)
- **售前提醒**：容器生产系统要重点确认并发、目录配额、误删恢复、性能抖动。

### 场景四：Web 内容管理与共享站点目录

- **场景特点**：多台 Web 服务器共享静态资源、上传文件、模板文件。
- **客户需求**：扩容 Web 节点时无需同步文件。
- **客户痛点**：多节点文件一致性、发布同步、共享目录权限。
- **UCloud 适配点**：UFS 容量型可用于对延迟要求较低的 Web 站点，性能型可用于低延迟要求的 Web 站点。来源：[UCloud UFS 应用场景](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)
- **售前提醒**：高并发小文件访问需结合性能型和缓存架构评估。

## 9. 与阿里云文件存储 NAS 的对比

| 对比维度 | UCloud UFS | 阿里云 NAS | 售前分析 | 来源 |
| --- | --- | --- | --- | --- |
| 产品定位 | 分布式文件系统，为 UCloud 公有云、物理云、托管云主机提供共享文件存储 | 面向 ECS、E-HPC、容器等计算节点的共享文件存储 | 二者定位高度相似，都是云上共享文件存储 | [UCloud](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)、[阿里云](https://help.aliyun.com/zh/nas/product-overview/what-is-nas) |
| 协议 | TCP NFSv4.0、NFSv3、SMB | NFS、SMB，兼容 POSIX 文件语义 | 都覆盖主流 Linux/Windows 文件共享协议 | [UCloud](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)、[阿里云](https://help.aliyun.com/zh/nas/product-overview/what-is-nas) |
| 产品类型 | 容量型、性能型 | 通用容量型、通用高级型、通用性能型、极速型等 | 阿里云产品层次更细；UCloud 结构更简单，售前讲解成本低 | [UCloud](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)、[阿里云选型](https://help.aliyun.com/zh/nas/product-overview/how-do-i-select-file-systems) |
| 数据可靠性 | 99.999999% 数据可靠性 | 99.999999999% 数据持久性、99.95% 服务可用性 | 阿里云公开指标更完整；UCloud 需补充确认服务可用性 SLA | [UCloud](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)、[阿里云](https://help.aliyun.com/zh/nas/product-overview/what-is-nas) |
| 容量上限 | 容量型最大购买 100 TB，性能型最大购买 20 TB，更大需联系技术支持 | 通用容量型 10 PiB，通用高级/性能型 1 PiB，极速型 256 TiB | 大容量项目对比时阿里云公开规格更高，UCloud 需提前确认扩容商务和技术支持 | [UCloud](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)、[阿里云限制](https://help.aliyun.com/zh/nas/product-overview/limits) |
| 单文件上限 | 1 TB | 32 TiB | 超大单文件场景阿里云公开规格优势明显 | [UCloud](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)、[阿里云限制](https://help.aliyun.com/zh/nas/product-overview/limits) |
| 挂载客户端 | 单文件系统允许挂载主机数量不限制 | 单文件系统同一时刻可挂载计算节点 1000 个 | UCloud 文档表达更宽松，但实际项目仍建议确认业务并发和性能 | [UCloud](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)、[阿里云限制](https://help.aliyun.com/zh/nas/product-overview/limits) |
| 企业级能力 | 文档显示支持回收站、容量告警等；ACL/LOCK 有协议限制 | 生命周期、ACL、目录配额、加密、备份、回收站、日志分析等能力较完整 | 若客户重视治理、权限、安全、成本分层，需重点补齐 UCloud 能力确认 | [UCloud](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)、[阿里云功能](https://help.aliyun.com/zh/nas/product-overview/product-function-node-nas) |

## 10. UCloud 实操实验建议

这些是学习验证建议，不写具体操作步骤。

| 实验方向 | 学习目标 | 建议观察点 |
| --- | --- | --- |
| 容量型 UFS 多主机挂载 | 理解共享文件系统基本行为 | 多主机读写一致性、权限表现、目录结构 |
| 性能型 UFS 小文件读写 | 体验性能型低延迟场景 | 4K 随机读写延迟、IOPS、并发下是否抖动 |
| 在线扩容 | 验证扩容对业务无感知 | 扩容前后容量变化、业务是否中断 |
| NFS 与 SMB 协议对比 | 理解 Linux/Windows 访问差异 | 文件权限、大小写、锁、客户端兼容性 |
| 跨 VPC/跨项目组访问验证 | 理解网络边界 | 挂载点、VPC 打通、访问延迟、权限范围 |
| 容器共享存储 | 理解 UFS 在容器 PV 场景的价值 | Pod 漂移后数据是否可访问、并发读写表现 |

## 11. 术语与英文缩写

| 缩写/术语 | 英文全称 | 中文说明 |
| --- | --- | --- |
| UFS | UCloud File Storage | UCloud 文件存储 |
| NAS | Network Attached Storage | 网络附加存储/文件存储 |
| NFS | Network File System | 常用于 Linux 的网络文件系统协议 |
| SMB | Server Message Block | 常用于 Windows 文件共享的协议 |
| TCP | Transmission Control Protocol | 传输控制协议 |
| VPC | Virtual Private Cloud | 私有网络 |
| POSIX | Portable Operating System Interface | 可移植操作系统接口，常用于描述类 Unix 文件系统语义 |
| SSD | Solid State Drive | 固态硬盘 |
| SATA | Serial Advanced Technology Attachment | 常见磁盘接口/介质类型，此处代表容量型存储介质 |
| IOPS | Input/Output Operations Per Second | 每秒输入输出操作次数 |
| PV | Persistent Volume | Kubernetes 持久卷 |
| ACL | Access Control List | 访问控制列表 |
| SLA | Service Level Agreement | 服务等级协议 |
| MTTR | Mean Time To Repair | 平均修复时间 |

## 12. 参考资料

- UCloud：[文件存储 UFS 产品文档 PDF](https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf)
- 阿里云：[什么是文件存储 NAS](https://help.aliyun.com/zh/nas/product-overview/what-is-nas)
- 阿里云：[NAS 功能特性](https://help.aliyun.com/zh/nas/product-overview/product-function-node-nas)
- 阿里云：[NAS 使用限制](https://help.aliyun.com/zh/nas/product-overview/limits)
- 阿里云：[NAS 应用场景](https://help.aliyun.com/zh/nas/product-overview/scenarios)
- 阿里云：[NAS 选型指导](https://help.aliyun.com/zh/nas/product-overview/how-do-i-select-file-systems)
