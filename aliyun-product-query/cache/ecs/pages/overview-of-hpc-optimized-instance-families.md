本文介绍云服务器ECS高性能计算优化型实例规格族的特点，并列出了具体的实例规格。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

## **高性能计算优化型实例介绍**
高性能计算优化型实例（以下简称HPC优化实例）是专为提升HPC工作负载性能，同时优化大规模运行成本而打造的最具性价比的实例。采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固：

* 专用硬件卸载虚拟化开销，性能损耗接近零，直接提供物理核，具有超强、超稳的计算能力。

* 高吞吐、低延迟、稳定的eRDMA网络，提供节点间高速通信的能力，提升网络密集型应用的性能。

HPC优化实例主要用于高性能计算、人工智能、机器学习、科学计算、工程计算、数据分析、音视频处理等场景，可以满足超高性能、网络和存储能力的要求。通过[弹性高性能计算E-HPC](https://help.aliyun.com/document_detail/57677.html)，您可以像使用其他ECS实例一样，任意创建HPC优化实例，扩展云上大规模并行任务的计算效率。

使用HPC优化实例时，请注意：

* 不支持规格变配。

* 提供物理内核，为优化性能不支持开启超线程配置。

高性能计算优化型包含以下规格族：

* [高性能计算优化型实例规格族hpc9a](#hpc9a)

* [高性能计算优化型实例规格族hpc8i](#hpc8i)

* [高性能计算优化型实例规格族hpc8ae](#hpc8ae)

* [高性能计算优化型实例规格族hpc7ip](#hpc7ip)

* [高性能计算优化型实例规格族hpc6id](#hpc6id)

## 高性能计算优化型实例规格族hpc9a
* **规格族介绍** ：hpc9a专为芯片设计等需要大量内存容量的HPC工作负载而设计，提供高达1:24的超大处理器与内存配比。采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC^™^ Turin 处理器，采用物理核设计，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：芯片设计、其他高性能计算场景。

* **计算**：

  * 处理器与内存（物理核：内存）配比为1:24。最大支持3072GiB内存。

  * 处理器：采用第五代AMD EPYC^™^ Turin处理器，睿频最高5.0GHz，采用物理核设计，计算性能稳定。

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 3/4。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

hpc9a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>eRDMA网络（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc9a.32xlarge</p></td> <td><p>128</p></td> <td><p>3072</p></td> <td><p>200</p></td> <td><p>200</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

## 高性能计算优化型实例规格族hpc8i
hpc8i正在邀测中，如需使用，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

* **规格族介绍** ：hpc8i实例针对计算密集的应用（如隐式有限元分析、分子动力学和计算化学等）进行了优化，采用最新的Intel^®^Xeon^®^Emerald Rapids处理器，全核睿频3.6 GHz，支持Intel丰富的软件工具生态系统，如Intel数学库和高级矢量扩展（AVX-512）。

* **适用场景**：

  * 工业仿真中计算流体动力学（Computational Fluid Dynamics，CFD）、有限元分析（Finite Element Analysis，FEA）。

  * EDA仿真。

  * 地质勘探。

  * 气象预报。

  * 分子动力学模拟。

  * 其他高性能计算场景。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids处理器，主频不低于2.8 GHz，全核睿频3.6 GHz，计算性能稳定。

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

hpc8i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>eRDMA网络（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc8i.32xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>100</p></td> <td><p>100</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

## 高性能计算优化型实例规格族hpc8ae
* **规格族介绍**：hpc8ae实例专为工业仿真、EDA（Electronic Design Automation）仿真、地质勘探、气象预报、分子动力学模拟等计算和网络密集的紧密耦合的HPC工作负载而设计。提供高达3.75 GHz的最新的第四代EPYC™（Genoa）处理器、64 Gbps的eRDMA节点间网络带宽以及增强的内存带宽能力。

* **适用场景**：

  * 工业仿真中计算流体动力学（Computational Fluid Dynamics，CFD）、有限元分析（Finite Element Analysis，FEA）。

  * EDA仿真。

  * 地质勘探。

  * 气象预报。

  * 分子动力学模拟。

  * 其他高性能计算场景。

* **计算**：

  * 处理器与内存配比为1:4

  * 处理器：3.4 GHz主频的AMD EPYC^TM^Genoa处理器，单核睿频最高3.75 GHz，计算性能稳定

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

hpc8ae包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>eRDMA网络（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc8ae.32xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>64</p></td> <td><p>64</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

## 高性能计算优化型实例规格族hpc7ip
* **规格族介绍：**hpc7ip专为芯片设计等需要大量内存容量的HPC工作负载而设计。依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。提供高达1:32的超大处理器与内存配比，搭配Intel傲腾持久内存介质，极大幅度降低内存型应用单GiB内存的成本。

* **适用场景**：芯片设计、其他高性能计算场景。

* **计算**：

  * 处理器与内存（内存+持久内存）配比约为1:32。

  * 处理器：采用第三代Intel^®^Xeon^®^可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 最大支持2560 GiB内存（512 GiB DRAM内存+2048 GiB Intel ^®^傲腾 ^TM^持久内存）。

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

hpc7ip包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>持久内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc7ip.32xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>2048</p></td> <td><p>64</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

## 高性能计算优化型实例规格族hpc6id
* **规格族介绍**：hpc6id专为芯片设计等需要大量内存容量和本地数据访问的HPC工作负载而设计。依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。提供超大内存和2块3.8 TB本地数据盘，降低内存和数据受限应用的使用成本。

* **适用场景**：芯片设计、地震油藏和结构模拟、其他高性能计算场景。

* **计算**：

  * 处理器与内存配比约为1:38。

  * 处理器：Intel^®^Xeon^®^可扩展处理器（Cascade Lake），基频 3.1 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

hpc6id包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储（GB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc6id.20xlarge</p></td> <td><p>40</p></td> <td><p>1536</p></td> <td><p>2 \* 3840</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

<br />
