# UCloud 与阿里云产品参考映射

Use this file before live searching for an Alibaba Cloud competitor. Match by UCloud product name, alias, or docs path. The mapping is a first recommendation for user confirmation, not a final authority. If the user rejects a mapping, search official documentation again and propose one revised Alibaba Cloud product.

The navigation URLs in this file are search entry points for building product index files such as `index-uhost.md`. Verify that a navigation URL opens successfully before using it; replace stale or invalid links with current official documentation URLs. Do not cite navigation URLs as final evidence when a more specific index URL exists.

Sources to refresh this file:

- UCloud product docs index: `https://docs.ucloud.cn/`
- UCloud product README pattern: `https://docs.ucloud.cn/{product-path}/README`
- Alibaba Cloud docs: `https://help.aliyun.com/`

## Mapping Table

| UCloud 产品 | 常见别名/关键词 | UCloud docs path | 建议阿里云竞品 | 阿里云文档入口 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| UHost 云主机 | 云服务器、CVM、虚拟机 | `uhost`; 导航页：`https://docs.ucloud.cn/uhost/README` | 云服务器 ECS（Elastic Compute Service） | 导航页：`https://help.aliyun.com/zh/ecs/` | 高 | 标准云服务器对标；已建立 `index-uhost.md` |
| GPU 云主机 | GPU、AI 训练、图形计算 | `gpu` / `uhost` | GPU 云服务器 | `https://help.aliyun.com/zh/ecs/user-guide/gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families` | 中 | 以 ECS GPU 实例族为主 |
| ULightHost 轻量云主机 | 轻量应用服务器 | `ulh` | 轻量应用服务器 Simple Application Server | `https://help.aliyun.com/zh/simple-application-server/` | 高 | 轻量级建站和开发测试场景 |
| UPHost 物理云主机 | 裸金属、物理机 | `uphost` | 弹性裸金属服务器 EBM / ECS 裸金属实例 | `https://help.aliyun.com/zh/ecs/user-guide/ebm-instances` | 中 | 需按客户是否强调裸金属性能确认 |
| UAS 高性能计算 | HPC、批量计算 | `uas` | 弹性高性能计算 E-HPC | `https://help.aliyun.com/zh/e-hpc/` | 中 | HPC 场景对标 |
| UK8S 容器云 | Kubernetes、K8s | `uk8s` | 容器服务 Kubernetes 版 ACK | `https://help.aliyun.com/zh/ack/` | 高 | 托管 Kubernetes 对标 |
| 容器实例 | Serverless 容器、弹性容器 | `cube` | 弹性容器实例 ECI | `https://help.aliyun.com/zh/eci/` | 中 | 按 UCloud 具体产品名确认 |
| UHub 镜像仓库 | 容器镜像 | `uhub` | 容器镜像服务 ACR | `https://help.aliyun.com/zh/acr/` | 高 | 镜像仓库对标 |
| VPC 私有网络 | UVPC、私有网络 | `vpc` | 专有网络 VPC | `https://help.aliyun.com/zh/vpc/` | 高 | 私有网络基础产品 |
| EIP 弹性 IP | 弹性公网 IP | `eip` | 弹性公网 IP EIP | `https://help.aliyun.com/zh/eip/` | 高 | 公网 IP 对标 |
| ULB 负载均衡 | 传统负载均衡 | `ulb` | 负载均衡 SLB（CLB/ALB/NLB） | `https://help.aliyun.com/zh/slb/` | 中 | 根据四层/七层/高性能需求细分 CLB、ALB、NLB |
| NAT 网关 | SNAT、DNAT | `natgw` | NAT 网关 | `https://help.aliyun.com/zh/nat-gateway/` | 高 | 出入口 NAT 对标 |
| VPN 网关 | IPsec VPN | `vpn` | VPN 网关 | `https://help.aliyun.com/zh/vpn-gateway/` | 高 | 混合云 VPN 对标 |
| UDPN 高速通道 | 内网专线、跨地域内网 | `udpn` | 云企业网 CEN / 高速通道 Express Connect | `https://help.aliyun.com/zh/cen/` | 中 | 按跨地域组网或专线接入确认 |
| UGN 全球网络 | 全球网络、跨境互联 | `ugn` | 云企业网 CEN / 全球加速 GA | `https://help.aliyun.com/zh/ga/` | 中 | 按全球接入或企业组网确认 |
| UDNS | DNS、域名解析 | `udns` | 云解析 DNS | `https://help.aliyun.com/zh/dns/` | 高 | 公网 DNS 解析对标 |
| 私有域名解析 | PrivateZone | `privatezone` | 云解析 PrivateZone | `https://help.aliyun.com/zh/pvtz/` | 高 | VPC 内私有域名解析 |
| UDisk 云硬盘 | 块存储、云盘 | `udisk` | 块存储云盘 ESSD / ESSD AutoPL | `https://help.aliyun.com/zh/ecs/user-guide/block-storage-devices` | 高 | 云主机块存储对标 |
| UFS 文件存储 | NAS、NFS、SMB | `ufs` | 文件存储 NAS | `https://help.aliyun.com/zh/nas/` | 高 | 共享文件系统对标 |
| UPFS 高性能文件存储 | 并行文件系统、HPC 文件存储 | `upfs` | 文件存储 CPFS | `https://help.aliyun.com/zh/cpfs/` | 中 | 高性能并行文件系统场景 |
| US3 对象存储 | UFile、对象存储、Bucket | `ufile` / `us3` | 对象存储 OSS | `https://help.aliyun.com/zh/oss/` | 高 | 对象存储对标 |
| UArchive 归档存储 | 冷数据、归档 | `uarchive` | OSS 归档/冷归档存储类型 | `https://help.aliyun.com/zh/oss/user-guide/storage-classes` | 中 | 以 OSS 存储类型对标 |
| UDB MySQL | 云数据库 MySQL | `udb` | 云数据库 RDS MySQL | `https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/` | 高 | 托管 MySQL 对标 |
| UDB PostgreSQL | 云数据库 PostgreSQL | `udb` | 云数据库 RDS PostgreSQL | `https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/` | 高 | 托管 PostgreSQL 对标 |
| UDB SQL Server | 云数据库 SQL Server | `udb` | 云数据库 RDS SQL Server | `https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/` | 高 | 托管 SQL Server 对标 |
| UDB MongoDB | MongoDB、文档数据库 | `mongodb` / `udb` | 云数据库 MongoDB 版 | `https://help.aliyun.com/zh/mongodb/` | 高 | 托管 MongoDB 对标 |
| UMem Redis | Redis、缓存 | `umem` | 云数据库 Redis 版 | `https://help.aliyun.com/zh/redis/` | 高 | Redis 缓存对标 |
| UMem Memcached | Memcache、缓存 | `umem` | 云数据库 Memcache 版 | `https://help.aliyun.com/zh/memcache/` | 中 | 阿里云产品可用性需实时确认 |
| UDDB | 分布式数据库、水平拆分 | `uddb` | PolarDB-X | `https://help.aliyun.com/zh/polardb/polardb-for-xscale/` | 中 | 分布式关系型数据库对标 |
| TiDB / UTiDB | 分布式 HTAP 数据库 | `tidb` | PolarDB-X / AnalyticDB for MySQL | `https://help.aliyun.com/zh/polardb/polardb-for-xscale/` | 低 | 需按 OLTP/HTAP 诉求重新确认 |
| UTSDB | 时序数据库 | `utsdb` | 时间序列数据库 TSDB | `https://help.aliyun.com/zh/tsdb/` | 中 | 产品可用性和替代方案需实时确认 |
| UES Elasticsearch | 搜索、日志检索 | `ues` | Elasticsearch Serverless / Elasticsearch | `https://help.aliyun.com/zh/es/` | 高 | 搜索分析对标 |
| UHadoop | Hadoop、大数据集群 | `uhadoop` | E-MapReduce EMR | `https://help.aliyun.com/zh/emr/` | 高 | 托管大数据集群对标 |
| UKafka | Kafka、消息队列 | `ukafka` | 云消息队列 Kafka 版 | `https://help.aliyun.com/zh/alikafka/` | 高 | Kafka 托管服务对标 |
| UMQ | 消息队列 | `umq` | 云消息队列 RocketMQ 版 / RabbitMQ 版 | `https://help.aliyun.com/zh/apsaramq-for-rocketmq/` | 中 | 按协议和模型确认 |
| UCDN 内容分发网络 | CDN | `ucdn` | CDN | `https://help.aliyun.com/zh/cdn/` | 高 | CDN 对标 |
| ULive 云直播 | 直播、推流 | `ulive` | 视频直播 ApsaraVideo Live | `https://help.aliyun.com/zh/live/` | 高 | 直播服务对标 |
| UMedia 云点播 | 点播、媒资 | `umedia` | 视频点播 ApsaraVideo VOD | `https://help.aliyun.com/zh/vod/` | 高 | 点播服务对标 |
| URTC 实时音视频 | RTC、音视频通话 | `urtc` | 音视频通信 RTC | `https://help.aliyun.com/zh/rtc/` | 高 | 实时音视频对标 |
| USSL 证书 | SSL、TLS 证书 | `ussl` | 数字证书管理服务 | `https://help.aliyun.com/zh/ssl-certificate/` | 高 | 证书管理对标 |
| UWAF Web 应用防火墙 | WAF | `uwaf` | Web 应用防火墙 WAF | `https://help.aliyun.com/zh/waf/` | 高 | Web 防护对标 |
| Anti-DDoS | DDoS 防护、高防 | `ddos` | DDoS 防护 | `https://help.aliyun.com/zh/anti-ddos/` | 高 | DDoS 防护对标 |
| 堡垒机 | 运维审计、Bastion | `bastionhost` | 堡垒机 | `https://help.aliyun.com/zh/bh/` | 高 | 运维审计对标 |
| 日志服务 | 日志采集、分析 | `ulog` | 日志服务 SLS | `https://help.aliyun.com/zh/sls/` | 中 | 按 UCloud 具体产品能力确认 |
| 云监控 | 监控告警 | `umon` | 云监控 CloudMonitor | `https://help.aliyun.com/zh/cms/` | 高 | 监控告警对标 |
| IAM / 访问控制 | 权限、子账号 | `iam` | 访问控制 RAM | `https://help.aliyun.com/zh/ram/` | 高 | 身份权限对标 |
| KMS 密钥管理 | 密钥、加密 | `kms` | 密钥管理服务 KMS | `https://help.aliyun.com/zh/kms/` | 高 | 密钥管理对标 |

## Usage Rules

- Recommend only one Alibaba Cloud competitor to the user for confirmation.
- If multiple Alibaba Cloud products are plausible, choose the highest-confidence general product and mention the ambiguity briefly.
- If the user's UCloud product is not in this table, live-search UCloud docs first, then Alibaba Cloud docs.
- Refresh this table when repeated user corrections reveal a better mapping.
