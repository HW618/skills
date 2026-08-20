云服务器ECS（Elastic Compute Service）是阿里云提供的性能卓越、稳定可靠、弹性扩展的IaaS（Infrastructure as a Service）级别云计算服务。云服务器ECS免去了您采购IT硬件的前期准备，让您像使用水、电、天然气等公共资源一样便捷、高效地使用服务器，实现计算资源的即开即用和弹性伸缩。阿里云ECS持续提供创新型服务器，解决多种业务需求，助力您的业务发展。  
[视频地址](http://cloud.video.taobao.com/play/u/3897629815/p/1/e/6/t/1/301659704826.mp4)

## **前置概念**
阅读本文前，您可能需要了解如下概念：

* [什么是云计算？](https://help.aliyun.com/document_detail/2669774.html)

* [什么是虚拟化？](https://help.aliyun.com/document_detail/2669777.html)

* [什么是IaaS？](https://help.aliyun.com/document_detail/2669780.html)

## 为什么选择云服务器ECS
* **多样化计算能力**：阿里云服务器支持主流的x86、Arm处理器架构，覆盖CPU、GPU、弹性裸金属及超级计算集群等服务器类型，提供了上百种实例规格族，满足不同规模和类型用户的需求。

* **便捷易用**：无需自建机房，分钟级交付，并提供了行业通用标准API、性能监控框架和主动运维体系，支持Terraform、系统运维、资源编排等多种运维能力，提高易用性和适用性。

* **成本优化**：提供了按量付费、包年包月、抢占式实例等多种计费方式，以满足不同应用场景需求，并可结合节省计划、预留实例券等优惠策略，以及弹性伸缩、弹性供应能力，保障稳定计算力的同时，最大程度优化资源使用成本。

* **弹性灵活**：支持根据业务量的增减情况灵活升级或降低计算、存储和网络带宽配置，同时可配合阿里云的弹性伸缩定时定量或根据业务负载进行弹性扩缩容。

* **稳定可靠：**单实例可用性达99.975%，多可用区多实例可用性达99.995%；云盘采用多副本，数据安全可靠性达99.9999999%；支持快照备份，自动告警等多种安全保障。

* **安全保障**：通过高标准数据中心安全、物理基础设施保护等措施确保平台本身的安全性。同时，提供了硬件加密、虚拟防火墙、访问控制、DDoS防护、漏洞扫描、数据加密等多重保障，加强操作系统安全、访问安全、网络安全、应用安全等，全面保护用户云上业务安全。

更多选择理由，请参见[特性与优势](https://help.aliyun.com/document_detail/51704.html)和[应用场景](https://help.aliyun.com/document_detail/25371.html#topic-9547)。

## 产品架构
云服务器ECS主要包含实例、镜像、[块存储](https://help.aliyun.com/document_detail/2669790.html)、快照、[安全组](https://help.aliyun.com/document_detail/2703256.html)、网络等功能组件。图中涉及的功能组件基本概念请参见[基本概念](https://help.aliyun.com/document_detail/260296.html#concept-2087383)。
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9793036771/CAEQORiBgIC33tze5xgiIDczMTkzZjMyYTM5YzQ2MjY4YjkxZGYyYTViZjZmMjcx3974248_20230905103052.317.svg)

## 产品计费
云服务器ECS的资源中，计算资源（vCPU和内存）、镜像、块存储、公网带宽、快照等资源涉及计费。

常见的计费方式包括：

* 包年包月：按一定时长购买资源，先付费后使用。

* 按量付费：按需开通和释放资源，先使用后付费。

* 抢占式实例：通过竞价模式抢占库存充足的计算资源，相对按量付费实例有一定的折扣，但是存在回收机制。

* 预留实例券：搭配按量付费实例使用的抵扣券，承诺使用指定配置的实例（包括实例规格、地域、[可用区](https://help.aliyun.com/document_detail/2709079.html)等），以折扣价抵扣计算资源的账单。

* 节省计划：搭配按量付费实例使用的折扣权益计划，承诺使用稳定数量的资源（以元/小时为单位衡量），以折扣价抵扣计算资源、系统盘等资源的账单。

* 存储容量单位包：搭配按量付费存储产品使用的资源包，承诺使用指定容量的存储资源，以折扣价抵扣块存储、NAS、OSS等资源的账单。

* OSS存储包：OSS标准（LRS）存储包可自动按容量抵扣快照费用。

详细的计费规则，请参见[计费概述](https://help.aliyun.com/document_detail/25398.html#concept-isb-scd-5db)。详细的价格信息，请参见[云产品定价页](https://www.aliyun.com/price/product#/ecs/detail)。如果想了解最新的活动，请参见[云服务器ECS产品详情页](https://www.aliyun.com/product/ecs)。

## 如何使用云服务器ECS
通过注册阿里云账号，您可以通过阿里云提供的以下途径创建、使用或者释放云服务器ECS：

* ECS管理控制台：具有交互式操作的Web服务页面。关于管理控制台的操作，请参见[常用操作导航](https://help.aliyun.com/document_detail/25429.html)。

* ECS [API](https://help.aliyun.com/document_detail/2669842.html)：支持GET和POST请求的RPC风格API。关于API说明，请参见[API参考](https://help.aliyun.com/document_detail/25484.html#EcsApiWelcome)。以下为调用云服务器ECS API的常用开发者工具：

  * [命令行工具CLI](https://help.aliyun.com/document_detail/163468.html)

  * [OpenAPI开发者门户](https://next.api.aliyun.com/api/Ecs/2014-05-26)：提供快速检索接口、在线调用API和动态生成SDK示例代码等服务。

  * [阿里云SDK](https://next.api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26)：提供Java、Python、PHP等多种编程语言的SDK。

* [资源编排服务ROS](https://help.aliyun.com/document_detail/28852.html#concept-28852-zh)：通过创建一个描述您所需的所有阿里云资源的模板，然后资源编排将根据模板，自动创建和配置资源。

* [系统运维管理OOS](https://help.aliyun.com/document_detail/125604.html#concept-1181174)：自动化管理和执行运维任务。您可以在执行模板中定义执行任务、执行顺序、执行输入和输出等，通过执行模板达到自动化完成运维任务的目的。

* [Terraform参考](https://help.aliyun.com/document_detail/92339.html)：能够通过配置文件在阿里云以及其他支持Terraform的云商平台调用计算资源，并对其进行版本控制的开源工具。

* [阿里云客户端](https://help.aliyun.com/document_detail/438476.html#concept-2230009)：阿里云官方推出的客户端工具，目前提供了对云服务器ECS、弹性容器实例ECI、 轻量应用服务器、阿里云托管实例的资源浏览、查找、远程连接等功能。

* 阿里云App：移动端类型的管理工具。

* [Alibaba Cloud Toolkit](https://help.aliyun.com/document_detail/29968.html)：阿里云针对IDE平台为开发者提供的一款插件，用于帮助您高效开发并部署适合在云端运行的应用。

## 部署建议
您可以从以下维度考虑如何启动并使用云服务器ECS：

* **地域和可用区**

  地域指阿里云数据中心的地理区域，地域和可用区决定了ECS实例所在的物理位置。一旦成功创建实例后，其元数据（仅[专有网络VPC](https://help.aliyun.com/document_detail/2669800.html)类型ECS实例支持获取元数据）将确定下来，并无法更换地域。您可以根据用户地理位置、阿里云产品发布情况、应用可用性以及是否需要内网通信等因素选择地域和可用区。例如，如果您需要通过阿里云内网使用[云数据库](https://help.aliyun.com/document_detail/2669814.html)RDS，RDS实例和ECS实例必须处于同一地域中。更多详情，请参见[地域和可用区](https://help.aliyun.com/document_detail/40654.html#concept-2459516)。
* **高可用性**

  为保证业务处理的正确性和服务不中断，建议您通过快照实现[数据备份](https://help.aliyun.com/document_detail/2702031.html)，通过跨可用区、部署集、[负载均衡](https://help.aliyun.com/document_detail/2669803.html)（Server Load Balancer）等实现应用容灾。
* **网络规划**

  阿里云推荐您使用专有网络VPC，可自行规划私网IP，全面支持新功能和新型实例规格。此外，专有网络VPC支持多业务系统隔离和多地域部署系统的使用场景。更多详情，请参见[专有网络（Virtual Private Cloud）](https://help.aliyun.com/document_detail/34217.html#concept-kbk-cpz-ndb)。
* **安全方案**

  * 您可以免费使用云服务器ECS的安全组，控制ECS实例的出入网访问策略以及端口监听状态。更多信息，请参见[安全组概述](https://help.aliyun.com/document_detail/25387.html#concept-o2y-mqw-ydb)。

  * 对于部署在云服务器ECS上的应用，阿里云为您提供了免费的DDoS基础防护和基础安全服务。更多信息，请参见[DDoS基础防护](https://help.aliyun.com/document_detail/55256.html#concept-j1h-3rw-ydb)和[基础安全服务](https://help.aliyun.com/document_detail/121691.html#concept-610245)。

    * DDoS基础防护默认开启无需购买，为您提供不超过5 Gbps的DDoS基础防护能力。如果您需要更高的防护能力来确保云服务器ECS业务的安全性，您可以购买DDoS高防。更多信息，请参见[DDoS高防文档](https://help.aliyun.com/document_detail/153308.html#concept-2417452)。

    * 基础安全服务为免费服务，不收取服务费用，为您提供基础的安全加固能力，包括异常登录检测、漏洞扫描、基线配置核查等。如果您需要升级为防病毒版、高级版或者企业版云安全中心来保障云服务器ECS业务的安全性，您可以购买服务。更多信息，请参见[云安全中心文档](https://help.aliyun.com/document_detail/42302.html#concept-bjv-y5w-ydb)。
