# 阿里云产品别名映射

用户可能用各种名称指代阿里云产品，需映射到标准 product key（用于 `cache/<key>/` 目录和 `https://help.aliyun.com/zh/<key>/llms.txt` URL）。

## 计算类

| 用户说法 | product key | 产品全名 |
|---|---|---|
| 云主机/云服务器/ECS | `ecs` | 云服务器 ECS |
| 轻量服务器/轻量应用服务器/SWAS | `simple-application-server` | 轻量应用服务器 |
| 裸金属/弹性裸金属/EBM | `ebm` | 弹性裸金属服务器 |
| GPU 云服务器/GPU | `ecs`（GPU 实例属 ECS 规格族） | GPU 云服务器 |
| 弹性容器实例/ECI | `eci` | 弹性容器实例 ECI |
| 弹性高性能计算/EHPC | `ehpc` | 弹性高性能计算 E-HPC |
| 函数计算/FC | `fc` | 函数计算 FC |
| Web 应用托管/WHY | `webx5` | Web 应用托管 |
| 批量计算/BC | `batchcompute` | 批量计算 Batch Compute |

## 存储类

| 用户说法 | product key | 产品全名 |
|---|---|---|
| 云盘/磁盘/块存储/EBS | `ecs`（云盘属 ECS 块存储） | 云盘（ECS 块存储） |
| NAS/文件存储 | `nas` | 文件存储 NAS |
| OSS/对象存储 | `oss` | 对象存储 OSS |
| 表格存储/Tablestore | `tablestore` | 表格存储 Tablestore |
| 归档/冷归档 | `oss`（属 OSS 存储类型） | 对象存储 OSS |
| 快照 | `ecs`（快照属 ECS） | 快照（ECS） |
| 混合云存储/HCS | `hgw` | 混合云存储 |

## 网络类

| 用户说法 | product key | 产品全名 |
|---|---|---|
| VPC/专有网络 | `vpc` | 专有网络 VPC |
| EIP/弹性公网 IP | `eip` | 弹性公网 IP |
| SLB/负载均衡/CLB | `slb` | 负载均衡 SLB（传统型） |
| ALB/应用型负载均衡 | `alb` | 应用型负载均衡 ALB |
| NLB/网络型负载均衡 | `nlb` | 网络型负载均衡 NLB |
| NAT 网关 | `nat` | NAT 网关 |
| CDN | `cdn` | CDN |
| DCDN/全站加速 | `dcdn` | 全站加速 DCDN |
| 高速通道/专线 | `express-connect` | 高速通道 |
| CEN/云企业网 | `cen` | 云企业网 CEN |
| 共享带宽 | `vpc`（属 VPC） | 共享带宽 |
| IPv6 网关 | `vpc`（属 VPC） | IPv6 网关 |

## 数据库类

| 用户说法 | product key | 产品全名 |
|---|---|---|
| RDS/云数据库 | `rds` | 云数据库 RDS |
| RDS MySQL | `rds` | 云数据库 RDS MySQL 版 |
| RDS PostgreSQL | `rds` | 云数据库 RDS PostgreSQL 版 |
| RDS SQL Server | `rds` | 云数据库 RDS SQL Server 版 |
| RDS MariaDB | `rds` | 云数据库 RDS MariaDB 版 |
| PolarDB | `polardb` | 云数据库 PolarDB |
| PolarDB MySQL | `polardb` | 云数据库 PolarDB MySQL |
| PolarDB PostgreSQL | `polardb` | 云数据库 PolarDB PostgreSQL |
| Redis/云数据库 Redis | `redis` | 云数据库 Redis |
| MongoDB/云数据库 Mongo | `mongodb` | 云数据库 MongoDB |
| 分析型数据库/AnalyticDB | `adb` | 分析型数据库 AnalyticDB |
| 图数据库/GDB | `gdb` | 图数据库 GDB |
| Tair/持久内存 | `tair` | 云数据库 Tair（持久内存版） |
| 数据库备份/DBS | `dbs` | 数据库备份 DBS |
| DMS/数据管理 | `dms` | 数据管理 DMS |
| DTS/数据传输 | `dts` | 数据传输 DTS |

## 安全类

| 用户说法 | product key | 产品全名 |
|---|---|---|
| 云盾/安全中心 | `sas` | 云安全中心 |
| WAF/Web 应用防火墙 | `waf` | Web 应用防火墙 |
| DDoS 高防 | `ddos` | DDoS 防护 |
| 抗 DDoS | `ddos` | DDoS 防护 |
| 云防火墙 | `cloudfirewall` | 云防火墙 |

## 使用说明

- **产品 key 不确定时**：读 `cache/_index/navigation.md` 搜索产品名，URL 中的 path 段即为 key。
- **一个产品有多个别名指向同一 key**：如"云盘""磁盘""块存储"都指向 `ecs`，因为云盘是 ECS 的块存储组件。
- **子产品归属父产品**：如 GPU 实例、云盘、快照都属 ECS；共享带宽属 VPC。查询时用父产品 key。
- **新增产品**：若导航页有但本表没有，以导航页 URL 的 path 段为准。
