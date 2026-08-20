本文介绍云服务器ECS超级计算集群实例规格族的特点，并列出了具体的实例规格。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

## 超级计算集群介绍
超级计算集群SCC（Super Computing Cluster）在弹性裸金属服务器基础上，加入高速RDMA（Remote Direct Memory Access）互联支持，大幅提升网络性能，提高大规模集群加速比。因此SCC在提供高带宽、低延迟优质网络的同时，还具备弹性裸金属服务器的所有优点。

SCC主要用于高性能计算和人工智能、机器学习、科学计算、工程计算、数据分析、音视频处理等场景。在集群内，各节点间通过RDMA网络互联，提供高带宽低延迟的网络，保证了高性能计算和人工智能、机器学习等应用的高度并行需求。同时，RoCE（RDMA over Converged Ethernet）网络速度达到InfiniBand网络级别的性能，且能支持更广泛的基于Ethernet的应用。

SCC与阿里云ECS、GPU云服务器等计算类产品一起，为[阿里云弹性高性能计算平台E-HPC](https://help.aliyun.com/document_detail/57677.html)提供了极高性能的并行计算资源，实现真正的云上超算。

高性能计算优化型包含以下规格族：

* [通用型超级计算集群实例规格族sccg7](#sccg7)

* [计算型超级计算集群实例规格族sccc7](#sccc7)

* [GPU计算型超级计算集群实例规格族sccgn7ex](#sccgn7ex)

## 机型对比
SCC与物理机、虚拟机的对比如下表所示。其中，Y表示支持，N表示不支持，N/A表示无数据。
<table> <thead> <tr> <td> <p><b>功能分类</b></p> </td> <td> <p><b>功能</b></p> </td> <td> <p><b>SCC</b></p> </td> <td> <p><b>物理机</b></p> </td> <td> <p><b>虚拟机</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>运维自动化</p> </td> <td> <p>分钟级交付</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>计算</p> </td> <td> <p>免性能损失</p> </td> <td> <p>Y</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> </tr> <tr> <td> <p>免特性损失</p> </td> <td> <p>Y</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> </tr> <tr> <td> <p>免资源争抢</p> </td> <td> <p>Y</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> </tr> <tr> <td> <p>存储</p> </td> <td> <p>完全兼容ECS云盘系统</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>使用云盘（系统盘）启动</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>系统盘快速重置</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>使用云服务器ECS的镜像</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>物理机和虚拟机之间相互冷迁移</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>免操作系统安装</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>免本地RAID，提供更高云盘数据保护</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>网络</p> </td> <td> <p>完全兼容ECS VPC网络</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>物理机集群和虚拟机集群间VPC无通信瓶颈</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>管控</p> </td> <td> <p>完全兼容ECS现有管控系统</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>VNC等用户体验和虚拟机保持一致</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>带外网络安全</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>N/A</p> </td> </tr> </tbody> </table>

## 通用型超级计算集群实例规格族sccg7
* **规格族介绍** ：具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* **适用场景**： 大规模机器学习训练；大规模高性能科学计算和仿真计算；大规模数据分析、批量计算、视频编码。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8369（Ice lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信。

sccg7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>物理内核</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>RoCE网络（Gbit/s）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sccg7.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>64</p> </td> <td> <p>512.0</p> </td> <td> <p>100</p> </td> <td> <p>2400万</p> </td> <td> <p>200</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 计算型超级计算集群实例规格族sccc7
* **规格族介绍** ：具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* **适用场景**： 大规模机器学习训练；大规模高性能科学计算和仿真计算；大规模数据分析、批量计算、视频编码。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8369（Ice lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信。

sccc7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>物理内核</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>RoCE网络（Gbit/s）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sccc7.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>64</p> </td> <td> <p>256.0</p> </td> <td> <p>100</p> </td> <td> <p>2400万</p> </td> <td> <p>200</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## GPU计算型超级计算集群实例规格族sccgn7ex
* **规格族介绍**：sccgn7ex是阿里云为了面对日益增长的大规模AI训练需求开发的高带宽超算集群实例。多台裸金属服务器之间采用第三代RDMA SCC网络互联，支持800 G的互联带宽。您可以根据训练需求弹性选择线上集群数量，快速满足大规模AI参数训练的需求。

* **适用场景**：超大规模AI训练场景。

* **计算**：

  * 支持NVSwitch，算力高达312T（TF32）。

  * 处理器与内存配比为1:8。

  * 处理器：采用第三代Intel^®^ Xeon^®^ 8369可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，支持PCIe 4.0接口。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 仅支持专有网络VPC。

  * 超高网络性能，2400万PPS网络收发包能力。

  * sccgn7ex实例间支持800 Gbit/s的互联带宽（4 \* 双口100 Gbit/s RDMA），支持GPUDirect，每颗GPU直连一个100 Gbit/s网口。

sccgn7ex包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存（GB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>RoCE网络（Gbit/s）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sccgn7ex.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>80 GB \* 8</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>800</p> </td> <td> <p>15</p> </td> </tr> </tbody> </table>

## 计费方式
SCC支持按量付费和包年包月。不同计费方式的区别，请参见[计费方式概述](https://help.aliyun.com/document_detail/25370.html#billingMethod-china)。
