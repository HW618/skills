本文所列实例规格在中国站已全部停售，其中，sn2、sn1、n1、n2和e3在国际站（International）仍然在售。  
* [高主频计算型超级计算集群实例规格族scchfc6](#scchfc6)

* [高主频通用型超级计算集群实例规格族scchfg6](#scchfg6)

* [高主频内存型超级计算集群实例规格族scchfr6](#scchfr6)

* [视觉计算型实例规格族ebmgi6s](#16b238382aqq1)

* [GPU计算型弹性裸金属服务器实例规格族ebmgn7vx](#ebmgn7vx)

* [GPU计算型弹性裸金属服务器实例规格族ebmgn6ia](#section-cig-esp-uiv)

* [本地SSD型弹性裸金属服务器实例规格族ebmi2g](#ebmi2g)

* [存储增强型实例规格族g5se](#section-buc-jpg-gho)

* [通用型实例规格族sn2](#section-e1p-ttg-4gb)

* [RDMA增强型实例规格族c7re](#c7re)

* [计算型实例规格族sn1](#section-d3f-11h-4gb)

* [高主频计算型实例规格族c4、ce4、cm4](#section-gpl-n1h-4gb)

* [GPU虚拟化型实例规格族vgn6i](#vgn6i)

* [GPU计算型实例规格族gn5](#gn5)

* [GPU计算型实例规格族gn5i](#gn5i)

* [GPU虚拟化型实例规格族vgn5i](#vgn5i)

* [GPU计算型实例规格族gn4](#section-b7i-gkz-z29)

* [GPU可视化计算型实例规格族ga1](#section-262-apr-whm)

* [计算型弹性裸金属服务器实例规格族ebmc4](#ebmc4)

* [高主频型弹性裸金属服务器实例规格族ebmhfg5](#section-56x-o2v-udt)

* [GPU计算型超级计算集群实例规格族sccgn6](#sccgn6)

* [GPU计算型超级计算集群实例规格族sccgn6e](#sccgn6e)

* [通用型超级计算集群实例规格族sccg5](#sccg5)

* [高主频型超级计算集群实例规格族scch5](#title-7bi-n4i-672)

* [GPU计算型超级计算集群实例规格族sccgn6ne](#section-98a-fyd-u9j)

* [大数据型实例规格族d1](#title-8kl-fnk-q8w)

* [本地SSD型实例规格族i1](#title-2ls-t3f-e9k)

* [共享型实例n1、n2、e3](#section-z2t-5ch-4gb)

* [系列I实例规格](#section-ilt-c3h-4gb)

## 变配说明
如果您持有已停售规格的实例，建议变配至其他在售规格。关于实例规格之间支持变配的情况，请参见[规格变更限制与自检](https://help.aliyun.com/document_detail/89743.html#concept-mdh-2rb-1fb)。

## 高主频计算型超级计算集群实例规格族scchfc6
* **规格族介绍** ：具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* **适用场景**： 大规模机器学习训练；大规模高性能科学计算和仿真计算；大规模数据分析、批量计算、视频编码。

* **计算**：

  * 处理器与内存配比为1:2.4。

  * 处理器：3.1 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269（Cascade Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信。

scchfc6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>RoCE网络（Gbit/s）</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.scchfc6.20xlarge</p></td> <td><p>80</p></td> <td><p>40</p></td> <td><p>192.0</p></td> <td><p>30</p></td> <td><p>600万</p></td> <td><p>50</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

ecs.scchfc6.20xlarge在40个物理内核上提供80个逻辑处理器。

## 高主频通用型超级计算集群实例规格族scchfg6
* **规格族介绍** ：具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* **适用场景**： 大规模机器学习训练；大规模高性能科学计算和仿真计算；大规模数据分析、批量计算、视频编码。

* **计算**：

  * 处理器与内存配比为1:4.8。

  * 处理器：3.1 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269（Cascade Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信。

scchfg6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>RoCE网络（Gbit/s）</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.scchfg6.20xlarge</p></td> <td><p>80</p></td> <td><p>40</p></td> <td><p>384.0</p></td> <td><p>30</p></td> <td><p>600万</p></td> <td><p>50</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

ecs.scchfg6.20xlarge在40个物理内核上提供80个逻辑处理器。

## 高主频内存型超级计算集群实例规格族scchfr6
* **规格族介绍** ：具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* **适用场景**： 大规模机器学习训练；大规模高性能科学计算和仿真计算；大规模数据分析、批量计算、视频编码。

* **计算**：

  * 处理器与内存配比为1:9.6。

  * 处理器：3.1 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269（Cascade Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信。

scchfr6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>RoCE网络（Gbit/s）</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.scchfr6.20xlarge</p></td> <td><p>80</p></td> <td><p>40</p></td> <td><p>768.0</p></td> <td><p>30</p></td> <td><p>600万</p></td> <td><p>50</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

ecs.scchfr6.20xlarge在40个物理内核上提供80个逻辑处理器。

## 视觉计算型实例规格族ebmgi6s
* **规格族介绍**：

  * 基于阿里云神龙架构及Intel^®^ Server GPU，为您提供快速弹性扩展的安全架构及最新高密度云手游渲染实例。

  * 可安装适配的安卓容器镜像AIC（Android in Container），提供如原生般的安卓容器环境，同时支持高密度安卓云游戏渲染和视频流处理，满足安卓云高视频编解码要求。

* **适用场景**：

  * 安卓云手游场景，对比传统手机阵列方式，拥有云上的灵活性及快速部署能力。

  * 使用高密度Intel^®^ Server GPU计算卡，提供渲染能力，同时还兼顾视频编解码能力，具有更优性能。

  * 基于英特尔平台上运行安卓容器（AIC）方案，可满足如原生般安卓环境的解决方案，有助于实现高流密度，提供优化云渲染技术。

* **计算**：

  * 处理器与内存配比为1:4

  * 采用Intel^®^ Server GPU计算卡，基于Intel^®^ Xe 可扩展架构，更高密度核心设计，大幅优化单位每路安卓游戏成本

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络** ：支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

ebmgi6s包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.ebmgi6s.24xlarge</p></td> <td><p>96</p></td> <td><p>384.0</p></td> <td><p>Intel<sup> ®</sup> Server GPU \* 1</p></td> <td><p>32 GB \* 1</p></td> <td><p>32.0</p></td> <td><p>450</p></td> <td><p>32</p></td> <td><p>32</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> </tbody> </table>

## GPU计算型弹性裸金属服务器实例规格族ebmgn7vx
ebmgn7vx的特点如下：

* ebmgn7vx依托第四代神龙架构，采用阿里云全新CIPU架构，多台裸金属之间通过eRDMA网络互联，在160 Gbit/s的互联带宽下实现RDMA通信。打开eRDMA后，您可以根据训练需求弹性选择集群中的机器数量，快速满足大规模AI训练的需求。

* 计算

  * 处理器：基于Intel ^®^第三代 Xeon ^®^Scalable计算平台（Icelake），2.9 GHz主频，全核睿频3.5 GHz，支持PCIe 4.0接口

* 存储

  * I/O优化实例

  * 仅支持ESSD云盘和ESSD AutoPL云盘

* 网络

  * 支持IPv4、IPv6

  * 支持物理网卡

  * 超高网络性能，2400万PPS网络收发包能力

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至160 Gbit/s

    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或者[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。
* 适用场景

  * 各类深度学习训练开发业务

  * HPC加速计算和仿真

    **说明**

    在使用高通信负载的AI训练业务如Transformer等模型时，务必启用NVLink进行GPU间的数据通信，否则可能由于PCIe链路大规模数据传输引起非预期的故障，导致数据受损。如不确定您使用的训练通信链路拓扑，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)由阿里云技术专家为您提供技术支持。

ebmgn7vx包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>网络带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>单网卡IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>物理网卡数</b></p></td> <td><p><b>多队列（主网卡/辅助网卡）</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.ebmgn7vx.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>80GB \* 8</p></td> <td><p>160（80 \* 2）</p></td> <td><p>2400万</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>32/32</p></td> <td><p>16</p></td> </tr> </tbody> </table>  
**说明**

* 您可以前往[ECS实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)，查看实例在各地域的可购情况。

* ebmgn7vx实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[通过API设置自定义镜像的启动模式为UEFI模式](https://help.aliyun.com/document_detail/324257.html)。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

* 暂无法获取EBM弹性裸金属实例的CPU基础监控信息，您可通过安装云监控插件获取CPU监控信息。具体操作，请参见[安装云监控插件](https://help.aliyun.com/document_detail/183482.html)。

## GPU计算型弹性裸金属服务器实例规格族ebmgn6ia
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 采用NVIDIA T4 GPU计算加速器提供GPU加速能力，助力图形和AI业务，搭配容器技术可以提供60路以上虚拟Android终端，并对每路终端显示进行硬件视频转码加速。

* **适用场景：**

  * 基于Android提供App远端服务，例如云业务在线待机、云手游和云手机、Android业务爬虫。

* **计算：**

  * 处理器与内存配比约为1:3。

  * 处理器：2.8 GHz主频的Ampere^®^ Altra^®^处理器，睿频3.0 GHz，原生ARM计算平台为Android服务器提供高效的性能和优秀的App兼容性。

* **存储：**

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

ebmgn6ia包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.ebmgn6ia.20xlarge</p></td> <td><p>80</p></td> <td><p>256</p></td> <td><p>NVIDIA T4 \* 2</p></td> <td><p>16GB \* 2</p></td> <td><p>32</p></td> <td><p>2400万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> </tbody> </table>  
**说明**

Ampere^®^ Altra^®^处理器对操作系统内核版本有一定要求。当您使用该实例规格创建ECS实例时，可以直接选用Alibaba Cloud Linux 3和CentOS 8.4及以上版本的操作系统镜像（建议您使用Alibaba Cloud Linux 3镜像）。如果您需要使用其他操作系统版本，请参见[Ampere Altra (TM) Linux Kernel Porting Guide](https://github.com/mmarmm/ampere-centos-kernel/wiki/Ampere-Altra--(TM)-Linux-Kernel-Porting-Guide)，在指定操作系统的ECS实例中为内核打上相应的补丁，完成之后基于该ECS实例创建自定义镜像，然后通过自定义镜像创建新的ECS实例时选择该实例规格。

## 本地SSD型弹性裸金属服务器实例规格族ebmi2g
ebmi2g的特点如下：

* 提供专属硬件资源和物理隔离

* 计算：

  * 处理器与内存配比为1:4

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake），全核睿频2.7 GHz

* 存储：

  * I/O优化实例

  * 仅支持ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘

* 网络：

  * 支持IPv4、IPv6

  * 仅支持专有网络VPC

  * 高网络性能，600万PPS网络收发包能力

* 适用场景：

  * OLTP、高性能关系型数据库

  * NoSQL数据库（例如Cassandra、MongoDB等）

  * Elasticsearch等搜索场景

ebmi2g包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.ebmi2g.24xlarge</p></td> <td><p>96</p></td> <td><p>384</p></td> <td><p>4\*1788</p></td> <td><p>32</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>10</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

## 存储增强型实例规格族g5se
g5se的特点如下：

* 仅支持通过专有宿主机创建g5se实例

  **说明**

  其他支持通过专有宿主机创建的实例规格，请参见[规格介绍](https://help.aliyun.com/document_detail/68564.html#concept-h3g-zzm-tdb)。
* 挂载ESSD云盘时，单实例随机读写性能最高可达100万IOPS，顺序读写性能最高可达32 Gbit/s

* 计算：

  * 处理器与内存配比为1:4

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake），计算性能稳定

* 存储：

  * I/O优化实例

  * 支持ESSD云盘、SSD云盘和高效云盘

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强）

    **说明**

    全新一代企业级实例规格族的存储I/O性能表，请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。
* 网络：

  * 支持IPv6

* 适用场景：

  * I/O密集型业务场景，例如中大型OLTP类核心数据库

  * 中大型NoSQL数据库

  * 搜索、实时日志分析

  * 大型企业级商用软件，例如SAP

g5se包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.g5se.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>1.0</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>3.0万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.g5se.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6.0万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.g5se.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>2.0</p></td> <td><p>80万</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>8.5万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.g5se.4xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>4.0</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>10</p></td> <td><p>15.0万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.g5se.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>7.0</p></td> <td><p>200万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>10</p></td> <td><p>30.0万</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.g5se.16xlarge</p></td> <td><p>64</p></td> <td><p>256.0</p></td> <td><p>14.0</p></td> <td><p>300万</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>10</p></td> <td><p>75.0万</p></td> <td><p>25</p></td> </tr> <tr> <td><p>ecs.g5se.18xlarge</p></td> <td><p>70</p></td> <td><p>336.0</p></td> <td><p>16.0</p></td> <td><p>400万</p></td> <td><p>16</p></td> <td><p>15</p></td> <td><p>10</p></td> <td><p>100.0万</p></td> <td><p>32</p></td> </tr> </tbody> </table>

## 通用型实例规格族sn2
sn2的特点如下：

* 处理器与内存配比为1:4

* 处理器：2.5 GHz主频的Intel Xeon E5-2682 v4（Broadwell）或E5-2680 v3（Haswell）或Platinum 8163（Skylake）或8269CY（Cascade Lake），计算性能稳定

  **说明**

  该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要将实例部署在同一服务器平台，建议您选用g6、g6e、g7。
* 实例网络性能与计算规格对应（规格越高网络性能强）

* 适用场景：

  * 各种类型和规模的企业级应用

  * 中小型数据库系统、缓存、搜索集群

  * 数据分析和计算

sn2包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.sn2.medium</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>0.5</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.sn2.large</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.sn2.xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>1.5</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.sn2.3xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>3.0</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.sn2.7xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>6.0</p></td> <td><p>80万</p></td> <td><p>3</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.sn2.13xlarge</p></td> <td><p>56</p></td> <td><p>224.0</p></td> <td><p>10.0</p></td> <td><p>120万</p></td> <td><p>4</p></td> <td><p>8</p></td> </tr> </tbody> </table>

## RDMA增强型实例规格族c7re
c7re的特点如下：

* c7re是一款专门支持eRDMA特性的规格族，支持ERI（Elastic RDMA Interface）。ERI是基于神龙架构实现的实例的一种网络接口，使实例可以在VPC网络下实现RDMA直通加速互联，具有低延迟、可云上规模部署、弹性扩展的优势。ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

* 计算：

  * 处理器与内存配比为1:2

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定

  * 支持开启或关闭超线程配置

* 存储：

  * I/O优化实例

  * 仅支持ESSD云盘

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强）

* 网络：

  * 支持IPv6

  * 支持ERI（Elastic RDMA Interface）

  * 超高网络收发包PPS能力

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

* 适用场景：

  * 大数据场景应用，例如Spark、Hadoop

  * 高性能科学计算和仿真计算

  * 各种通用类型的企业应用，例如Redis

c7re包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>弹性eRDMA网卡（ERI）</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c7re.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>10/25</p></td> <td><p>150万</p></td> <td><p>10万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>1</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>8万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.c7re.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>12/25</p></td> <td><p>200万</p></td> <td><p>15万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>1</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>11万</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.c7re.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>16/25</p></td> <td><p>300万</p></td> <td><p>20万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>1</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.c7re.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>600万</p></td> <td><p>40万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>1</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.c7re.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>64/无</p></td> <td><p>1200万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>60万</p></td> <td><p>32</p></td> </tr> </tbody> </table>

## 计算型实例规格族sn1
sn1的特点如下：

* 处理器与内存配比为1:2

* 处理器：2.5 GHz主频的Intel Xeon E5-2682 v4（Broadwell）或E5-2680 v3（Haswell）或Platinum 8163（Skylake）或8269CY（Cascade Lake），计算性能稳定

  **说明**

  该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要将实例部署在同一服务器平台，建议您选用c6、c6e、c7。
* 实例网络性能与计算规格对应（规格越高网络性能强）

* 适用场景：

  * Web 前端服务器

  * 大型多人在线游戏（MMO）前端

  * 数据分析、批量计算、视频编码

  * 高性能科学和工程应用

sn1包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.sn1.medium</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>0.5</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.sn1.large</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.sn1.xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>1.5</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.sn1.3xlarge</p></td> <td><p>16</p></td> <td><p>32.0</p></td> <td><p>3.0</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.sn1.7xlarge</p></td> <td><p>32</p></td> <td><p>64.0</p></td> <td><p>6.0</p></td> <td><p>80万</p></td> <td><p>3</p></td> <td><p>8</p></td> </tr> </tbody> </table>

## 高主频计算型实例规格族c4、ce4、cm4
c4、ce4、cm4的特点如下：

* 处理器：3.2 GHz主频的Intel Xeon E5-2667 v4（Broadwell）处理器

* 计算性能稳定

* I/O优化实例

* 仅支持SSD云盘和高效云盘

* 实例网络性能与计算规格对应（规格越高网络性能越强）

* 适用场景：

  * 高性能Web前端服务器

  * 高性能科学和工程应用

  * MMO游戏、视频编码

c4包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c4.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>1.5</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.c4.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>3.0</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.c4.3xlarge</p></td> <td><p>12</p></td> <td><p>24.0</p></td> <td><p>4.5</p></td> <td><p>60万</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.c4.4xlarge</p></td> <td><p>16</p></td> <td><p>32.0</p></td> <td><p>6.0</p></td> <td><p>80万</p></td> <td><p>2</p></td> <td><p>8</p></td> </tr> </tbody> </table>  
ce4包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.ce4.xlarge</p></td> <td><p>4</p></td> <td><p>32.0</p></td> <td><p>1.5</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.ce4.2xlarge</p></td> <td><p>8</p></td> <td><p>64.0</p></td> <td><p>3.0</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>3</p></td> </tr> </tbody> </table>  
cm4包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.cm4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>1.5</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.cm4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>3.0</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.cm4.3xlarge</p></td> <td><p>12</p></td> <td><p>48.0</p></td> <td><p>4.5</p></td> <td><p>60万</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.cm4.4xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>6.0</p></td> <td><p>80万</p></td> <td><p>2</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.cm4.6xlarge</p></td> <td><p>24</p></td> <td><p>96.0</p></td> <td><p>10.0</p></td> <td><p>120万</p></td> <td><p>4</p></td> <td><p>8</p></td> </tr> </tbody> </table>

## GPU虚拟化型实例规格族vgn6i
vgn6i的特点如下：

* 计算：

  * 采用NVIDIA T4 GPU计算加速器

  * 实例包含分片虚拟化后的虚拟GPU

    * 计算能力支持NVIDIA Tesla T4的1/4和1/2

    * GPU显存支持4 GB和8 GB

  * 处理器与内存配比约为1:5

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）

* 存储：

  * I/O优化实例

  * 仅支持SSD云盘和高效云盘

* 网络：

  * 支持IPv6

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

* 适用场景：

  * 云游戏的云端实时渲染

  * AR和VR的云端实时渲染

  * AI（DL和ML）推理，适合弹性部署含有AI推理计算应用的互联网业务

  * 深度学习的教学练习环境

  * 深度学习的模型实验环境

vgn6i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列（主网卡/辅网卡）</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.vgn6i-m4.xlarge</p></td> <td><p>4</p></td> <td><p>23</p></td> <td><p>NVIDIA T4 \* 1/4</p></td> <td><p>16GB \* 1/4</p></td> <td><p>2</p></td> <td><p>50万</p></td> <td><p>4/2</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.vgn6i-m8.2xlarge</p></td> <td><p>10</p></td> <td><p>46</p></td> <td><p>NVIDIA T4 \* 1/2</p></td> <td><p>16GB \* 1/2</p></td> <td><p>4</p></td> <td><p>80万</p></td> <td><p>8/2</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> </tbody> </table>

## GPU计算型实例规格族gn5
* **适用场景**：

  * 深度学习。

  * 科学计算，例如计算流体动力学、计算金融学、基因组学研究、环境分析。

  * 高性能计算、渲染、多媒体编解码及其他服务器端GPU计算工作负载。

* **计算**：

  * 采用NVIDIA P100 GPU卡。

  * 多种处理器与内存配比。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）。

* **存储**：

  * 配备高性能NVMe SSD本地盘。

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 仅支持IPv4

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

gn5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>本地存储（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.gn5-c4g1.xlarge</p></td> <td><p>4</p></td> <td><p>30</p></td> <td><p>NVIDIA P100 \* 1</p></td> <td><p>16GB \* 1</p></td> <td><p>440</p></td> <td><p>3</p></td> <td><p>30万</p></td> <td><p>1</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.gn5-c8g1.2xlarge</p></td> <td><p>8</p></td> <td><p>60</p></td> <td><p>NVIDIA P100 \* 1</p></td> <td><p>16GB \* 1</p></td> <td><p>440</p></td> <td><p>3</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.gn5-c4g1.2xlarge</p></td> <td><p>8</p></td> <td><p>60</p></td> <td><p>NVIDIA P100 \* 2</p></td> <td><p>16GB \* 2</p></td> <td><p>880</p></td> <td><p>5</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.gn5-c8g1.4xlarge</p></td> <td><p>16</p></td> <td><p>120</p></td> <td><p>NVIDIA P100 \* 2</p></td> <td><p>16GB \* 2</p></td> <td><p>880</p></td> <td><p>5</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.gn5-c28g1.7xlarge</p></td> <td><p>28</p></td> <td><p>112</p></td> <td><p>NVIDIA P100 \* 1</p></td> <td><p>16GB \* 1</p></td> <td><p>440</p></td> <td><p>5</p></td> <td><p>225万</p></td> <td><p>7</p></td> <td><p>8</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.gn5-c8g1.8xlarge</p></td> <td><p>32</p></td> <td><p>240</p></td> <td><p>NVIDIA P100 \* 4</p></td> <td><p>16GB \* 4</p></td> <td><p>1760</p></td> <td><p>10</p></td> <td><p>200万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.gn5-c28g1.14xlarge</p></td> <td><p>56</p></td> <td><p>224</p></td> <td><p>NVIDIA P100 \* 2</p></td> <td><p>16GB \* 2</p></td> <td><p>880</p></td> <td><p>10</p></td> <td><p>450万</p></td> <td><p>14</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.gn5-c8g1.14xlarge</p></td> <td><p>54</p></td> <td><p>480</p></td> <td><p>NVIDIA P100 \* 8</p></td> <td><p>16GB \* 8</p></td> <td><p>3520</p></td> <td><p>25</p></td> <td><p>400万</p></td> <td><p>14</p></td> <td><p>8</p></td> <td><p>10</p></td> </tr> </tbody> </table>

## GPU计算型实例规格族gn5i
* **适用场景**： 深度学习推理、多媒体编解码等服务器端GPU计算工作负载。

* 计算：

  * 采用NVIDIA P4 GPU卡。

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）。

* 存储：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* 网络：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

gn5i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.gn5i-c2g1.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>NVIDIA P4 \* 1</p></td> <td><p>8GB \* 1</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.gn5i-c4g1.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>NVIDIA P4 \* 1</p></td> <td><p>8GB \* 1</p></td> <td><p>1.5</p></td> <td><p>20万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.gn5i-c8g1.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>NVIDIA P4 \* 1</p></td> <td><p>8GB \* 1</p></td> <td><p>2</p></td> <td><p>40万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.gn5i-c16g1.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>NVIDIA P4 \* 1</p></td> <td><p>8GB \* 1</p></td> <td><p>3</p></td> <td><p>80万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.gn5i-c16g1.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>NVIDIA P4 \* 2</p></td> <td><p>8GB \* 2</p></td> <td><p>6</p></td> <td><p>120万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.gn5i-c28g1.14xlarge</p></td> <td><p>56</p></td> <td><p>224</p></td> <td><p>NVIDIA P4 \* 2</p></td> <td><p>8GB \* 2</p></td> <td><p>10</p></td> <td><p>200万</p></td> <td><p>14</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> </tbody> </table>

## GPU虚拟化型实例规格族vgn5i
vgn5i的特点如下：

* 计算：

  * 采用NVIDIA P4 GPU计算加速器

  * 实例包含分片虚拟化后的虚拟GPU

    * 计算能力支持NVIDIA Tesla P4的1/8、1/4、1/2和1:1

    * GPU显存支持1 GB、2 GB、4 GB和8 GB

  * 处理器与内存配比为1:3

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）

* 存储：

  * I/O优化实例

  * 仅支持SSD云盘和高效云盘

* 网络：

  * 支持IPv6

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

* 适用场景：

  * 云游戏的云端实时渲染

  * AR和VR的云端实时渲染

  * AI（DL和ML）推理，适合弹性部署含有AI推理计算应用的互联网业务

  * 深度学习的教学练习环境

  * 深度学习的模型实验环境

vgn5i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.vgn5i-m1.large</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>NVIDIA P4 \* 1/8</p></td> <td><p>8GB \* 1/8</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.vgn5i-m2.xlarge</p></td> <td><p>4</p></td> <td><p>12</p></td> <td><p>NVIDIA P4 \* 1/4</p></td> <td><p>8GB \* 1/4</p></td> <td><p>2</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.vgn5i-m4.2xlarge</p></td> <td><p>8</p></td> <td><p>24</p></td> <td><p>NVIDIA P4 \* 1/2</p></td> <td><p>8GB \* 1/2</p></td> <td><p>3</p></td> <td><p>80万</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.vgn5i-m8.4xlarge</p></td> <td><p>16</p></td> <td><p>48</p></td> <td><p>NVIDIA P4 \* 1</p></td> <td><p>8GB \* 1</p></td> <td><p>5</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>5</p></td> <td><p>20</p></td> </tr> </tbody> </table>  
**说明**

上表中的**GPU**列对应的指标包括GPU卡型号和GPU分片信息。其中，GPU分片表示1块GPU分成多片，每个实例上使用1片。例如：

`NVIDIA P4 * 1/8`中的`NVIDIA P4`表示GPU卡型号；`1/8`表示GPU的分片，即1块GPU分成8片，每个实例上使用1片。

## GPU计算型实例规格族gn4
gn4的特点如下：

* 采用NVIDIA M40 GPU计算卡

* 计算：

  * 多种处理器与内存配比

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）

* 存储：

  * I/O优化实例

  * 仅支持SSD云盘和高效云盘

* 网络：

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

* 适用场景：

  * 深度学习

  * 科学计算，例如计算流体动力学、计算金融学、基因组学研究、环境分析

  * 高性能计算、渲染、多媒体编解码及其他服务器端GPU计算工作负载

gn4包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.gn4-c4g1.xlarge</p></td> <td><p>4</p></td> <td><p>30.0</p></td> <td><p>NVIDIA M40 \* 1</p></td> <td><p>12GB \* 1</p></td> <td><p>3.0</p></td> <td><p>30万</p></td> <td><p>1</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.gn4-c8g1.2xlarge</p></td> <td><p>8</p></td> <td><p>30.0</p></td> <td><p>NVIDIA M40 \* 1</p></td> <td><p>12GB \* 1</p></td> <td><p>3.0</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.gn4.8xlarge</p></td> <td><p>32</p></td> <td><p>48.0</p></td> <td><p>NVIDIA M40 \* 1</p></td> <td><p>12GB \* 1</p></td> <td><p>6.0</p></td> <td><p>80万</p></td> <td><p>3</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.gn4-c4g1.2xlarge</p></td> <td><p>8</p></td> <td><p>60.0</p></td> <td><p>NVIDIA M40 \* 2</p></td> <td><p>12GB \* 2</p></td> <td><p>5.0</p></td> <td><p>50万</p></td> <td><p>1</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.gn4-c8g1.4xlarge</p></td> <td><p>16</p></td> <td><p>60.0</p></td> <td><p>NVIDIA M40 \* 2</p></td> <td><p>12GB \* 2</p></td> <td><p>5.0</p></td> <td><p>50万</p></td> <td><p>1</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.gn4.14xlarge</p></td> <td><p>56</p></td> <td><p>96.0</p></td> <td><p>NVIDIA M40 \* 2</p></td> <td><p>12GB \* 2</p></td> <td><p>10.0</p></td> <td><p>120万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> </tbody> </table>

## GPU可视化计算型实例规格族ga1
ga1的特点如下：

* 采用AMD S7150 GPU计算卡

* 配备高性能NVMe SSD本地盘

* 计算：

  * 处理器与内存配比为1:2.5

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）

* 存储：

  * I/O优化实例

  * 仅支持SSD云盘和高效云盘

* 网络：

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

* 适用场景：

  * 渲染、多媒体编解码

  * 机器学习、高性能计算、高性能数据库

  * 其他需要强大并行浮点计算能力的服务器端业务

ga1包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.ga1.xlarge</p></td> <td><p>4</p></td> <td><p>10.0</p></td> <td><p>1 \* 87</p></td> <td><p>AMD S7150 \* 1/4</p></td> <td><p>8GB \* 1/4</p></td> <td><p>1.0</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.ga1.2xlarge</p></td> <td><p>8</p></td> <td><p>20.0</p></td> <td><p>1 \* 175</p></td> <td><p>AMD S7150 \* 1/2</p></td> <td><p>8GB \* 1/2</p></td> <td><p>1.5</p></td> <td><p>30万</p></td> <td><p>1</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.ga1.4xlarge</p></td> <td><p>16</p></td> <td><p>40.0</p></td> <td><p>1 \* 350</p></td> <td><p>AMD S7150 \* 1</p></td> <td><p>8GB \* 1</p></td> <td><p>3.0</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.ga1.8xlarge</p></td> <td><p>32</p></td> <td><p>80.0</p></td> <td><p>1 \* 700</p></td> <td><p>AMD S7150 \* 2</p></td> <td><p>8GB \* 2</p></td> <td><p>6.0</p></td> <td><p>80万</p></td> <td><p>3</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.ga1.14xlarge</p></td> <td><p>56</p></td> <td><p>160.0</p></td> <td><p>1 \* 1400</p></td> <td><p>AMD S7150 \* 4</p></td> <td><p>8GB \* 4</p></td> <td><p>10.0</p></td> <td><p>120万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> </tbody> </table>

## 计算型弹性裸金属服务器实例规格族ebmc4
ebmc4的特点如下：

* 提供专属硬件资源和物理隔离

* 计算

  * 处理器与内存配比为1:2

  * 处理器：2.5 GHz主频Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell），睿频3.0 GHz

* 存储

  * 均为I/O优化实例

  * 仅支持SSD云盘和高效云盘

* 网络

  * 仅支持专有网络VPC

  * 高网络性能，400万PPS网络收发包能力

* 适用场景

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求

  * 容器（包括但不限于Docker、Clear Container、Pouch等）

  * 中大型企业等重量级数据库应用

  * 视频编码

ebmc4包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.ebmc4.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10</p></td> <td><p>400万</p></td> <td><p>12</p></td> <td><p>10</p></td> </tr> </tbody> </table>

## 高主频型弹性裸金属服务器实例规格族ebmhfg5
ebmhfg5的特点如下：

* 提供专属硬件资源和物理隔离

* 支持Intel ^®^ SGX加密计算

* 不支持宕机迁移

  您可以调用API[ModifyInstanceMaintenanceAttributes](https://help.aliyun.com/document_detail/150089.html#doc-api-Ecs-ModifyInstanceMaintenanceAttributes)修改维护动作，将ActionOnMaintenance设置为AutoRedeploy即可启用宕机迁移。
* 处理器与内存配比为1:4

* 处理器：3.7 GHz主频的Intel ^®^ Xeon ^®^ E3-1240v6（Skylake），睿频4.1 GHz

* 均为I/O优化实例

* 仅支持SSD云盘和高效云盘

* 仅支持专有网络VPC

* 高网络性能，200万PPS网络收发包能力

* 适用场景：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载

  * 游戏和金融等高性能应用

  * 高性能Web服务器

  * 高性能数据库等企业级应用

ebmhfg5包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.ebmhfg5.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>6</p></td> <td><p>200万</p></td> <td><p>6</p></td> <td><p>8</p></td> </tr> </tbody> </table>

## GPU计算型超级计算集群实例规格族sccgn6
sccgn6的特点如下：

* 具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* 计算：

  * GPU加速器：V100（SXM2封装）

    * 创新的Volta架构

    * GPU显存16 GB HBM2

    * CUDA Cores 5120

    * Tensor Cores 640

    * GPU显存带宽900 GB/s

    * GPU支持6个NVLink链路（NVLink属于双向链路），单向链路的带宽为25 Git/s，总带宽为6×25×2=300 Git/s

  * 处理器与内存配比为1:4

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake），计算性能稳定

* 存储：

  * I/O优化实例

  * 仅支持ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘

  * 支持高性能并行文件系统CPFS

* 网络：

  * 支持IPv6

  * 支持专有网络VPC

  * 支持RoCE V2网络，用于低延迟的RDMA通信

* 适用场景：

  * 超大规模机器学习集群训练场景

  * 大规模高性能科学计算和仿真计算

  * 大规模数据分析、批量计算、视频编码

sccgn6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>RoCE网络（Gbit/s）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.sccgn6.24xlarge</p></td> <td><p>96</p></td> <td><p>384.0</p></td> <td><p>NVIDIA V100 \* 8</p></td> <td><p>30</p></td> <td><p>450万</p></td> <td><p>50</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>10</p></td> </tr> </tbody> </table>

## GPU计算型超级计算集群实例规格族sccgn6e
sccgn6e的特点如下：

* 具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* 计算：

  * GPU加速器：

    * 创新的Volta架构

    * GPU显存32 GB HBM2

    * CUDA Cores 5120

    * Tensor Cores 640

    * GPU显存带宽900 GB/s

    * 单GPU支持6个NVLink链路（NVLink属于双向链路），单向链路的带宽为25 Git/s，总带宽为6×25×2=300 Git/s

  * 处理器与内存配比为1:8

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake），计算性能稳定

* 存储：

  * I/O优化实例

  * 仅支持ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘

  * 支持高性能并行文件系统CPFS

* 网络：

  * 支持IPv6

  * 支持专有网络VPC

  * 支持RoCE V2网络，用于低延迟的RDMA通信

* 适用场景：

  * 超大规模机器学习集群训练场景

  * 大规模高性能科学计算和仿真计算

  * 大规模数据分析、批量计算、视频编码

sccgn6e包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存（GB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>RoCE网络（Gbit/s）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.sccgn6e.24xlarge</p></td> <td><p>96</p></td> <td><p>768.0</p></td> <td><p>NVIDIA V100 \* 8</p></td> <td><p>32GB \* 8</p></td> <td><p>32</p></td> <td><p>480万</p></td> <td><p>50</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>10</p></td> </tr> </tbody> </table>

## 通用型超级计算集群实例规格族sccg5
sccg5的特点如下：

* 具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* 计算：

  * 处理器与内存配比为1:4

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake），计算性能稳定

* 存储：

  * 均为I/O优化实例

  * 仅支持SSD云盘和高效云盘

* 网络：

  * 同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信

* 适用场景：

  * 大规模机器学习训练

  * 大规模高性能科学计算和仿真计算

  * 大规模数据分析、批量计算、视频编码

sccg5包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>RoCE网络（Gbit/s）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.sccg5.24xlarge</p></td> <td><p>96</p></td> <td><p>48</p></td> <td><p>384.0</p></td> <td><p>10</p></td> <td><p>450万</p></td> <td><p>50</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>10</p></td> </tr> </tbody> </table>

## 高主频型超级计算集群实例规格族scch5
* **规格族介绍** ：具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* **适用场景**： 大规模机器学习训练；大规模高性能科学计算和仿真计算；大规模数据分析、批量计算、视频编码。

* **计算**：

  * 处理器与内存配比为1:3

  * 处理器：3.1 GHz主频的Intel ^®^ Xeon ^®^ Gold 6149（Skylake）

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 仅支持IPv4。

  * 同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信。

scch5包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>RoCE网络（Gbit/s）</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.scch5.16xlarge</p></td> <td><p>64</p></td> <td><p>32</p></td> <td><p>192.0</p></td> <td><p>10</p></td> <td><p>450万</p></td> <td><p>50</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

ecs.scch5.16xlarge在32个物理内核上提供64个逻辑处理器。

## GPU计算型超级计算集群实例规格族sccgn6ne
sccgn6ne的特点如下：

* 具备弹性裸金属服务器的所有特性

* 计算：

  * GPU加速器：V100（SXM2封装）

    * 创新的Volta架构

    * GPU显存32 GB HBM2

    * CUDA Cores 5120

    * Tensor Cores 640

    * GPU显存带宽900 GB/s

    * 支持6个NVLink链路，每个25 GB/s，总共300 GB/s

  * 处理器与内存配比为1:4

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake），计算性能稳定

* 存储：

  * I/O优化实例

  * 支持ESSD云盘、SSD云盘和高效云盘

  * 支持高性能并行文件系统CPFS

* 网络：

  * 支持IPv6

  * 支持专有网络VPC

  * 支持RoCE V2网络，用于低延迟的RDMA通信

* 适用场景：

  * 超大规模机器学习集群训练场景

  * 大规模高性能科学计算和仿真计算

  * 大规模数据分析、批量计算、视频编码

sccgn6ne包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>GPU</b></p></td> <td><p><b>GPU显存</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>RoCE网络（Gbit/s）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.sccgn6ne.24xlarge</p></td> <td><p>96</p></td> <td><p>768.0</p></td> <td><p>NVIDIA V100 \* 8</p></td> <td><p>32GB \* 8</p></td> <td><p>32.0</p></td> <td><p>480万</p></td> <td><p>100</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> </tbody> </table>

## 大数据型实例规格族d1
* **规格族介绍**：实例配备大容量、高吞吐SATA HDD本地盘，辅以最大17 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、HBase等。

  * Spark内存计算、MLlib等。

  * 互联网行业、金融行业等有大数据计算与存储分析需求的行业客户，进行海量数据存储和计算的业务场景。

  * ElasticSearch、日志等。

* **计算**：

  * 处理器与内存配比为1:4，为大数据场景设计。

  * 处理器：2.5 GHz主频的Intel^®^ Xeon^®^ E5-2682 v4（Broadwell）或者Intel^®^ Xeon^®^Platinum 8163（Skylake），计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 仅支持IPv4。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d1包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d1.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>4 \* 5905 GB</p><p>(4 \* 5500 GiB)</p></td> <td><p>3.0</p></td> <td><p>30</p></td> </tr> <tr> <td><p>ecs.d1.3xlarge</p></td> <td><p>12</p></td> <td><p>48.0</p></td> <td><p>6 \* 5905 GB</p><p>(6 \* 5500 GiB)</p></td> <td><p>4.0</p></td> <td><p>40</p></td> </tr> <tr> <td><p>ecs.d1.4xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>8 \* 5905 GB</p><p>(8 \* 5500 GiB)</p></td> <td><p>6.0</p></td> <td><p>60</p></td> </tr> <tr> <td><p>ecs.d1.6xlarge</p></td> <td><p>24</p></td> <td><p>96.0</p></td> <td><p>12 \* 5905 GB</p><p>(12 \* 5500 GiB)</p></td> <td><p>8.0</p></td> <td><p>80</p></td> </tr> <tr> <td><p>ecs.d1-c8d3.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>12 \* 5905 GB</p><p>(12 \* 5500 GiB)</p></td> <td><p>10.0</p></td> <td><p>100</p></td> </tr> <tr> <td><p>ecs.d1.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>16 \* 5905 GB</p><p>(16 \* 5500 GiB)</p></td> <td><p>10.0</p></td> <td><p>100</p></td> </tr> <tr> <td><p>ecs.d1-c14d3.14xlarge</p></td> <td><p>56</p></td> <td><p>160.0</p></td> <td><p>12 \* 5905 GB</p><p>(12 \* 5500 GiB)</p></td> <td><p>17.0</p></td> <td><p>180</p></td> </tr> <tr> <td><p>ecs.d1.14xlarge</p></td> <td><p>56</p></td> <td><p>224.0</p></td> <td><p>28 \* 5905 GB</p><p>(28 \* 5500 GiB)</p></td> <td><p>17.0</p></td> <td><p>180</p></td> </tr> </tbody> </table>

## 本地SSD型实例规格族i1
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel^®^ Xeon^®^ E5-2682 v4（Broadwell）或者Intel^®^ Xeon^®^Platinum 8163（Skylake），计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 仅支持IPv4

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i1包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.i1.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>2 \* 111 GB</p><p>(2 \* 104 GiB)</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> </tr> <tr> <td><p>ecs.i1.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>2 \* 223 GB</p><p>(2 \* 208 GiB)</p></td> <td><p>1.5</p></td> <td><p>40万</p></td> </tr> <tr> <td><p>ecs.i1.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>2 \* 335 GB</p><p>(2 \* 312 GiB)</p></td> <td><p>2</p></td> <td><p>40万</p></td> </tr> <tr> <td><p>ecs.i1.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>2 \* 446 GB</p><p>(2 \* 416 GiB)</p></td> <td><p>3</p></td> <td><p>50万</p></td> </tr> <tr> <td><p>ecs.i1-c5d1.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>2 \* 1563 GB</p><p>(2 \* 1456 GiB)</p></td> <td><p>3</p></td> <td><p>40万</p></td> </tr> <tr> <td><p>ecs.i1.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>2 \* 670 GB</p><p>(2 \* 624 GiB)</p></td> <td><p>4.5</p></td> <td><p>60万</p></td> </tr> <tr> <td><p>ecs.i1.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>2 \* 893 GB</p><p>(2 \* 832 GiB)</p></td> <td><p>6</p></td> <td><p>80万</p></td> </tr> <tr> <td><p>ecs.i1-c10d1.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>2 \* 1563 GB</p><p>(2 \* 1456 GiB)</p></td> <td><p>6</p></td> <td><p>80万</p></td> </tr> <tr> <td><p>ecs.i1.14xlarge</p></td> <td><p>56</p></td> <td><p>224</p></td> <td><p>2 \* 1563 GB</p><p>(2 \* 1456 GiB)</p></td> <td><p>10</p></td> <td><p>120万</p></td> </tr> </tbody> </table>

## 共享型实例n1、n2、e3
n1、n2、e3的特点如下：

* 处理器：2.5 GHz主频的Intel Xeon E5-2680 v3（Haswell）或E5-2680 v3（Haswell）或Platinum 8163（Skylake）或8269CY（Cascade Lake）

* 均为I/O优化实例

* 支持SSD云盘和高效云盘

* 实例网络性能与计算规格对应（规格越高网络性能强）

<table> <thead> <tr> <td><p><b>规格族</b></p></td> <td><p><b>特点</b></p></td> <td><p><b>vCPU：内存</b></p></td> <td><p><b>适用场景</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>n1</p></td> <td><p>共享计算型实例</p></td> <td><p>1:2</p></td> <td> <ul> <li><p>中小型Web服务器</p></li> <li><p>批量处理</p></li> <li><p>分布式分析</p></li> <li><p>广告服务</p></li> </ul></td> </tr> <tr> <td><p>n2</p></td> <td><p>共享通用型实例</p></td> <td><p>1:4</p></td> <td> <ul> <li><p>中型Web服务器</p></li> <li><p>批量处理</p></li> <li><p>分布式分析</p></li> <li><p>广告服务</p></li> <li><p>Hadoop集群</p></li> </ul></td> </tr> <tr> <td><p>e3</p></td> <td><p>共享内存型实例</p></td> <td><p>1:8</p></td> <td> <ul> <li><p>Cache/Redis</p></li> <li><p>搜索类</p></li> <li><p>内存数据库</p></li> <li><p>高I/O的数据库如Oracle、MongoDB</p></li> <li><p>Hadoop集群</p></li> <li><p>大量的数据处理加工场景</p></li> </ul></td> </tr> </tbody> </table>  
n1包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.n1.tiny</p></td> <td><p>1</p></td> <td><p>1.0</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.n1.small</p></td> <td><p>1</p></td> <td><p>2.0</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.n1.medium</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.n1.large</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n1.xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n1.3xlarge</p></td> <td><p>16</p></td> <td><p>32.0</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n1.7xlarge</p></td> <td><p>32</p></td> <td><p>64.0</p></td> <td><p>2</p></td> </tr> </tbody> </table>  
n2包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.n2.small</p></td> <td><p>1</p></td> <td><p>4.0</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.n2.medium</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.n2.large</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n2.xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n2.3xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n2.7xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>2</p></td> </tr> </tbody> </table>  
e3包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.e3.small</p></td> <td><p>1</p></td> <td><p>8.0</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.e3.medium</p></td> <td><p>2</p></td> <td><p>16.0</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.e3.large</p></td> <td><p>4</p></td> <td><p>32.0</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.e3.xlarge</p></td> <td><p>8</p></td> <td><p>64.0</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.e3.3xlarge</p></td> <td><p>16</p></td> <td><p>128.0</p></td> <td><p>2</p></td> </tr> </tbody> </table>

## 系列I实例规格
系列I实例规格包括：t1、s1、s2、s3、m1、m2、c1、c2。系列I实例规格均为旧有的共享型实例规格，按照1核、2核、4核、8核、16核的方式分型分组，对规格族不敏感。  
系列I实例规格的特点如下：

* 采用不低于1.9 GHz主频的Intel Xeon E5-2420处理器

* 最新一代DDR3内存

* I/O优化与非I/O优化可选

I/O优化实例规格支持SSD云盘和高效云盘，包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>规格分类</b></p></td> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>Standard</p></td> <td><p>ecs.s2.large</p></td> <td><p>2</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.s2.xlarge</p></td> <td><p>2</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.s2.2xlarge</p></td> <td><p>2</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.s3.medium</p></td> <td><p>4</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.s3.large</p></td> <td><p>4</p></td> <td><p>8</p></td> </tr> <tr> <td><p>High Memory</p></td> <td><p>ecs.m1.medium</p></td> <td><p>4</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.m2.medium</p></td> <td><p>4</p></td> <td><p>32</p></td> </tr> <tr> <td><p>ecs.m1.xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> </tr> <tr> <td><p>High CPU</p></td> <td><p>ecs.c1.small</p></td> <td><p>8</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.c1.large</p></td> <td><p>8</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.c2.medium</p></td> <td><p>16</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.c2.large</p></td> <td><p>16</p></td> <td><p>32</p></td> </tr> <tr> <td><p>ecs.c2.xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> </tr> </tbody> </table>  
非I/O优化实例规格仅支持普通云盘，包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>规格分类</b></p></td> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>Tiny</p></td> <td><p>ecs.t1.small</p></td> <td><p>1</p></td> <td><p>1</p></td> </tr> <tr> <td><p>Standard</p></td> <td><p>ecs.s1.small</p></td> <td><p>1</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.s1.medium</p></td> <td><p>1</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.s1.large</p></td> <td><p>1</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.s2.small</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.s2.large</p></td> <td><p>2</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.s2.xlarge</p></td> <td><p>2</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.s2.2xlarge</p></td> <td><p>2</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.s3.medium</p></td> <td><p>4</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.s3.large</p></td> <td><p>4</p></td> <td><p>8</p></td> </tr> <tr> <td><p>High Memory</p></td> <td><p>ecs.m1.medium</p></td> <td><p>4</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.m2.medium</p></td> <td><p>4</p></td> <td><p>32</p></td> </tr> <tr> <td><p>ecs.m1.xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> </tr> <tr> <td><p>High CPU</p></td> <td><p>ecs.c1.small</p></td> <td><p>8</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.c1.large</p></td> <td><p>8</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.c2.medium</p></td> <td><p>16</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.c2.large</p></td> <td><p>16</p></td> <td><p>32</p></td> </tr> <tr> <td><p>ecs.c2.xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> </tr> </tbody> </table>
