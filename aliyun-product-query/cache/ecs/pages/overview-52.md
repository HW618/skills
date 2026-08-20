ECS实例是云上的虚拟服务器，包含vCPU、内存、操作系统、网络和磁盘等基本组件。您可以通过阿里云的控制台、API或SDK来创建、管理和释放ECS实例，像使用本地服务器一样进行应用部署和日常运维。与本地服务器相比，ECS实例具备更灵活且稳定的计算、存储能力。  

## **实例基础配置**
实例基础配置决定一台实例所需的基础资源，主要包括：

### 实例规格

实例规格定义了ECS实例在计算性能、存储性能、网络性能等方面的基础属性，但需要同时配合镜像、块存储、网络等配置才能确定一台ECS实例的具体服务形态。

实例规格主要包括vCPU、内存、vGPU（GPU型）、本地存储（本地SSD型、大数据型等）、物理网卡、网络性能（网络带宽、PPS）以及云盘性能（云盘带宽、IOPS）等，您可以结合性能、价格、工作负载等因素，选择合适的实例规格。具体内容，请参见[实例规格指标说明](https://help.aliyun.com/document_detail/2849443.html#section-e9r-xkf-z15)、[实例规格选型指导](https://help.aliyun.com/document_detail/58291.html)。

### 镜像

镜像提供了运行实例所需的信息，包括操作系统、初始化应用数据等。阿里云提供了Windows Server系统镜像和主流的Linux系统镜像供您直接选用，您也可以自行创建和导入包含自定义配置的自定义镜像，节省重复配置的时间。此外，阿里云云市场中的镜像服务商提供了预装各类运行环境或软件应用的镜像，满足建站、应用开发、可视化管理等个性化需求，按具体用途选用更加便捷。更多信息，请参见[镜像概述](https://help.aliyun.com/document_detail/25389.html)。

### 存储

实例通过添加系统盘、数据盘等获得存储能力。实例必须包含系统盘，便于启动实例时基于镜像完成操作系统等初始化配置的安装。

云盘可以用作系统盘和数据盘，本地盘仅部分实例规格配备（例如本地SSD型、大数据型等）且只能用作数据盘。如果实例需要更大存储能力存储业务数据，也可以在创建后扩容已有云盘或者挂载更多云盘。更多信息，请参见[云盘扩容指引](https://help.aliyun.com/document_detail/35095.html#concept-e1g-44g-ydb)、[挂载数据盘](https://help.aliyun.com/document_detail/25446.html#concept-llz-b4c-ydb)。

业务数据是重要资产，云盘采用三副本技术保证数据可用性，但及时备份业务数据同样重要，您可以使用快照功能备份云盘上的数据。如果您使用了本地盘，则需要自行在应用层做数据冗余，保证数据可用性。

### 网络

弹性网卡是一种在专有网络VPC中为ECS实例提供网络接口和IP地址的虚拟网络接口，VPC网络中的每个实例都有默认的弹性网卡，通过弹性网卡，ECS实例能够实现与其他云资源或互联网之间进行内网、公网通信。更多信息，请参见[弹性网卡概述](https://help.aliyun.com/document_detail/58496.html)。

内网通信允许通过私网IP地址、私网域名的方式进行寻址。详细信息，请参见[VPC内网访问](https://help.aliyun.com/document_detail/2856740.html)。

公网通信可以通过为ECS实例开通公网实现，详细信息，请参见[开通公网](https://help.aliyun.com/document_detail/419460.html)。

除基础配置外，您还可以自定义实例的安全组、分组等配置，更多信息，请参见[自定义购买实例](https://help.aliyun.com/document_detail/87190.html#task-vwq-5g4-r2b)。

## 实例生命周期
实例的生命周期指从创建实例开始到释放实例结束，实例所经历的状态。

### 实例状态说明

实例状态按查询位置分为控制台状态和API状态。控制台状态是可以在控制台中查询到的实例状态，具体操作，请参见[查看实例信息](https://help.aliyun.com/document_detail/64296.html)。API状态是通过调用[DescribeInstanceStatus](https://help.aliyun.com/document_detail/25505.html#DescribeInstanceStatus)或[DescribeInstances](https://help.aliyun.com/document_detail/25506.html#DescribeInstances)可以查询到的实例状态。一个API状态可能根据包年包月实例是否过期、账号是否欠费等原因对应多个控制台状态（例如API状态`Stopped`）。

在实例生命周期中可能的状态如下表所示。  
**说明**

* 中间状态：表示实例正处于某种状态的转换过程中，即从一个状态向另一个状态过渡。例如启动中（Starting）。

* 稳定状态：表示实例已处于一种确定的工作模式下，例如运行中（Running）、已停止（Stopped）。

<table> <thead> <tr> <td><p><b>控制台状态</b></p></td> <td><p><b>API状态</b></p></td> <td><p><b>状态属性</b></p></td> <td><p><b>状态说明</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>待启动</p></td> <td><p>Pending</p></td> <td><p>中间状态</p></td> <td><p>新创建实例，实例即将启动。</p></td> </tr> <tr> <td><p>启动中</p></td> <td><p>Starting</p></td> <td><p>中间状态</p></td> <td><p>新创建实例，或者对已有实例执行启动或重启操作，实例即将进入运行中（Running）状态。</p></td> </tr> <tr> <td><p>运行中</p></td> <td><p>Running</p></td> <td><p>稳定状态</p></td> <td><p>实例处于运行中状态。 </p> <div> <div> <i></i> </div> <div> <strong>重要 </strong> <p>实例处于Running状态仅代表实例已经运行，类似于对电脑进行开机，但实例的操作系统并不一定已经运行。只有当实例的操作系统运行起来后，网络服务才能正常工作，才可以通过SSH、RDP等方式进行远程访问。您可以通过查看实例的健康状态，判断实例的操作系统是否已经运行。更多详情，请参见<a href="https://help.aliyun.com/document_detail/106567.html">查看实例健康状态</a>。</p> </div> </div></td> </tr> <tr> <td><p>即将过期</p></td> <td><p>Running</p></td> <td><p>稳定状态</p></td> <td><p>包年包月实例正常运行中，但是即将过期。建议您及时续费实例，更多信息，请参见<a href="https://help.aliyun.com/document_detail/48360.html">如何续费包年包月实例</a>。</p></td> </tr> <tr> <td><p>停止中 </p></td> <td><p>Stopping</p></td> <td><p>中间状态</p></td> <td><p>对实例执行停止或休眠操作，实例即将进入已停止（Stopped）状态。</p></td> </tr> <tr> <td><p>已停止</p></td> <td><p>Stopped</p></td> <td><p>稳定状态</p></td> <td><p>实例已经创建完成等待启动，或者实例已经被停止或休眠。</p> <div> <div> <i></i> </div> <div> <strong>说明 </strong> <p>在控制台上或者调用RunInstances创建实例后，实例会自动启动，您无需手动启动。</p> </div> </div></td> </tr> <tr> <td><p>已过期</p></td> <td><p>Stopped</p></td> <td><p>稳定状态</p></td> <td><p>包年包月实例已经到期，或者按量付费实例因账号欠费而停机，实例即将释放。关于实例的资源保留情况，请参见<span><a href="https://help.aliyun.com/document_detail/56220.html#section-n4y-1zm-7kc">包年包月</a></span>和<span><a href="https://help.aliyun.com/document_detail/40653.html#section-w1c-zw2-zdb">按量付费</a></span>。 </p></td> </tr> <tr> <td><p>已锁定</p></td> <td><p>Stopped</p></td> <td><p>稳定状态</p></td> <td><p>实例存在安全风险被锁定。您可以前往<a href="https://yundun.console.aliyun.com/?spm=5176.ecscore_overview.top-nav.dsc.787c4df5pQZd7U\&amp;p=sc#/sc/punishList">安全管控页面</a>申请解禁。</p></td> </tr> <tr> <td><p>已退款停机</p></td> <td><p>Stopped</p></td> <td><p>稳定状态</p></td> <td><p>包年包月实例已退款。为避免误操作导致数据丢失，相关资源会保留一定时间再释放，规则如下：</p> <ul> <li><p>vCPU、内存、固定公网IP、快照在退款后24小时内释放。</p></li> <li><p>云盘在退款后15天内释放。</p></li> </ul> <div> <div> <i></i> </div> <div> <strong>说明 </strong> <p>以上期限是最长保留时间，实际释放时间可能提前。</p> </div> </div></td> </tr> <tr> <td><p>过期回收中</p></td> <td><p>Stopped</p></td> <td><p>稳定状态</p></td> <td><p>如果包年包月实例的网络类型为专有网络，在到期后释放前会先进入已过期（Stopped）状态，但随时会进入过期回收中（Stopped）状态。</p><p>已过期（Stopped）状态和过期回收中（Stopped）状态下，实例的资源保留情况不同。更多信息，请参见<span><a href="https://help.aliyun.com/document_detail/56220.html#section-n4y-1zm-7kc">包年包月</a></span>。</p></td> </tr> <tr> <td><p>欠费回收中</p></td> <td><p>Stopped</p></td> <td><p>稳定状态</p></td> <td><p>如果按量付费实例的网络类型为专有网络，在欠费停机后释放前会先进入已过期（Stopped）状态，但随时会进入欠费回收中（Stopped）状态。</p><p>已过期（Stopped）状态和欠费回收中（Stopped）状态下，实例的资源保留情况不同。更多信息，请参见<span><a href="https://help.aliyun.com/document_detail/40653.html#section-w1c-zw2-zdb">按量付费</a></span>。</p></td> </tr> <tr> <td><p>等待释放</p></td> <td><p>Stopped</p></td> <td><p>稳定状态</p></td> <td><p>已申请退款提早释放包年包月实例。具体操作，请参见<a href="https://help.aliyun.com/document_detail/37096.html">申请退款</a>。</p></td> </tr> </tbody> </table>

### 实例状态转换说明

下图展示了实例的状态转换流程。若您想查看某个状态的详细说明，可参见[实例状态说明](#82500ee589iso)。
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7562532871/CAEQTxiBgICsleqKkRkiIDk3NzFjMTMwODlkYTQ1N2Q5ZTNkM2RhZTc5MzA2ZTll3963382_20230830144006.372.svg)

管理实例状态的常见操作及说明如下：

* [创建实例](https://help.aliyun.com/document_detail/108442.html#concept-nx2-nzv-wgb)

  实例创建完成后，会先进入待启动（Pending）状态，然后进入启动中（Starting）状态，最终进入运行中（Running）状态。此时您可以连接实例，针对不同的操作系统，使用SSH、RDP、会话管理等工具，即可进入实例进行运维。具体操作，请参见[连接实例](https://help.aliyun.com/document_detail/48428.html)。
* [停止实例](https://help.aliyun.com/document_detail/132239.html#task-1909833)

  在执行一些操作前，您需要先停止实例，例如实例更换操作系统、实例修改私有IP地址、按量付费实例变配实例规格等。操作停止实例后，实例先进入停止中（Stopping）状态，最终进入已停止（Stopped）状态。

  如果在停止按量付费实例时启用节省停机模式，停机后会释放计算资源（vCPU和内存）和固定公网IP并停止收取相关费用，但保留云盘、EIP等其他资源并继续收取相关费用。
* [启动实例](https://help.aliyun.com/document_detail/25441.html#concept-mnp-lsl-xdb)

  在实例处于已停止等无法正常提供服务的状态时，如需使用实例需要先启动实例。操作启动实例后，实例先进入启动中（Starting）状态，最终进入运行中（Running）状态。
* [重启实例](https://help.aliyun.com/document_detail/25440.html#concept-yxw-dwm-xdb)

  重启操作是维护云服务器的一种常用方式，如系统更新、重启保存相关配置等。操作重启实例后，实例先进入停止中（Stopping）状态，然后进入启动中（Starting）状态，最终进入运行中（Running）状态。

  实例在重启后可能被调度到其他宿主机上，如果您需要实例始终部署在指定的宿主机上，可以购买专有云宿主机并为实例启用关联宿主机。
* [释放实例](https://help.aliyun.com/document_detail/25442.html#concept-jfp-wbf-5db)

  当您不再需要某个实例提供服务时，可以释放该实例，以免产生额外的费用。

  实例释放后，实例ID、固定公网IP、系统盘、设置随实例释放的数据盘等数据和资源随之释放且不可恢复，EIP、设置不随实例释放的数据盘等独立的资源自动解绑。请慎重执行释放操作，如果需要规避误操作释放实例，您可以为实例启用释放保护。

## 使用指引
1. 选购实例：

   在正式购买实例之前，您需要提前了解如下信息：
   * 了解目前在售的实例规格族，同时根据您希望购买的地域进行库存查询，详情请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html)、[ECS实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)。

   * 根据业务对实例的消耗情况，合理选择实例计费方式：[包年包月](https://help.aliyun.com/document_detail/108478.html)、[按量付费](https://help.aliyun.com/document_detail/108479.html)、[抢占式实例](https://help.aliyun.com/document_detail/108450.html)，以及是否搭配资源包进行成本优化，如[节省计划](https://help.aliyun.com/document_detail/184084.html)。

2. 购买ECS实例：

   * [快速购买实例一键购买包年包月实例](https://help.aliyun.com/document_detail/611897.html)：可以在几分钟内，以最简单的方式购买一个ECS实例，但仅支持特定的实例规格和镜像，大多数配置无法自定义。

   * [自定义购买实例](https://help.aliyun.com/document_detail/87190.html)：自定义购买可根据业务场景灵活地选择镜像类型、实例规格、存储、带宽、安全组等配置。

3. 远程连接实例：

   * 您可以选择使用[选择ECS远程连接方式](https://help.aliyun.com/document_detail/71529.html#c883a4be3egsg)、[选择ECS远程连接方式](https://help.aliyun.com/document_detail/71529.html#68ff20289069m)、[选择ECS远程连接方式](https://help.aliyun.com/document_detail/71529.html#df096dd0062si)等方式登录到ECS实例进行远程运维，详情请参见[选择ECS远程连接方式](https://help.aliyun.com/document_detail/71529.html)。

   * 如果您在创建ECS实例时未设置密码，或者创建ECS实例后忘记了密码，则需要重新为ECS实例设置登录密码。详情请参见[重置实例登录密码](https://help.aliyun.com/document_detail/25439.html)。

4. 管理实例：

   如果您想对实例进行一些产品的配置与管理操作，请参见[管理实例](https://help.aliyun.com/document_detail/2854629.html)。
5. 部署服务：

   * 如果您想进行基础环境的部署，请参见[搭建环境](https://help.aliyun.com/document_detail/151696.html)。

   * 如果您想部署常用的网站服务，请参见[搭建网站](https://help.aliyun.com/document_detail/151697.html)。

   * 如果您想部署常见的应用服务，如数据库、代码托管平台，请参见[搭建应用](https://help.aliyun.com/document_detail/151698.html)。

   * 如果您想部署自己的业务代码，请参见[部署业务代码至ECS](https://help.aliyun.com/document_detail/2858163.html)。

6. 运维与监控：

   * 若机器出现一些超出预期的故障，如：实例宕机、实例无法启动、实例无法连接等问题，可使用自助排查工具进行在线诊断，详情参见[诊断](https://help.aliyun.com/document_detail/287020.html)。

   * 您也可借助系统运维管理OOS对实例进行定期、批量运维，详情参见[系统运维管理OOS](https://help.aliyun.com/document_detail/125604.html)。

7. 更改ECS实例配置：

   使用ECS实例时，如果当前实例配置无法满足您的业务需求，您可以修改实例规格（vCPU和内存）、公网带宽配置和数据盘计费方式。更多信息，请参见[升降配方式概述](https://help.aliyun.com/document_detail/25437.html)。
8. 释放实例：

   当您不再需要某个实例提供服务时，可以释放该实例，以免产生额外的费用。

   实例释放后，实例ID、固定公网IP、系统盘、设置随实例释放的数据盘等数据和资源随之释放且不可恢复，EIP、设置不随实例释放的数据盘等独立的资源自动解绑。请慎重执行释放操作，如果需要规避误操作释放实例，您可以为实例启用释放保护。更多信息，请参见[释放实例](https://help.aliyun.com/document_detail/25442.html)。

## 安全建议
使用云产品过程中，遵循安全建议可以有效提高云上资源的安全性。例如：

* **权限控制** ：使用访问控制RAM功能，控制哪些用户可以操作实例等资源以及拥有何种权限。更多信息，请参见[身份管理](https://help.aliyun.com/document_detail/2697771.html)。

* **网络安全**：通过专有网络隔离不同安全等级的服务，使用安全组控制实例的入流量和出流量，并仅为必需的实例提供公网访问能力，尽量降低实例等资源受到来自外部网络攻击的风险。

* **数据安全**：

  * 云服务器ECS在数据的完整性方面，通过云盘三副本技术为ECS实例提供数据可靠性保证，数据安全擦除机制实现数据擦除的完整性，并且提供了全链路的数据循环冗余校验CRC（Cyclic Redundancy Check）功能，以确保数据在传输和存储过程中的完整性。更多信息，请参见[保证自身数据的完整性](https://help.aliyun.com/document_detail/2362830.html#fd82a80d24sgf)。

  * 云服务器ECS在存储、传输以及运行态全链路环节上均提供了丰富的安全能力和方案，以保证用户对数据机密性的诉求，例如**数据存储的机密性** 、**数据网络传输的机密性** 、**数据运行态计算环境的机密性** 。更多信息，请参见[在数据的存储、传输、计算环节保证数据机密性](https://help.aliyun.com/document_detail/2362830.html#ba523e8191jl5)。

* **监控与日志：**监控与日志可有效保障您的云服务器ECS资源的可用性、业务的正常运行和健康度。您可以通过对应的监控能力，持续收集监控数据。阿里云提供了各种监控与日志审计相关的服务，例如云监控、配置审计等，帮助您实时监控云资源的使用情况和业务运行状况，并在收到异常报警时及时响应。

更多提高实例安全性的做法，请参见[云服务器ECS安全性](https://help.aliyun.com/document_detail/257799.html#task-2084924)。
