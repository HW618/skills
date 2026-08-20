与快速购买实例相比，自定义购买可根据业务场景灵活地选择配置，如镜像类型、实例规格、存储、带宽、安全组等。本文介绍如何自定义购买实例。  
**重要**

如果您刚接触ECS不久，想要快速上手购买并使用ECS实例，我们为您准备了一个较简单的示例，请参见[控制台自定义购买并使用ECS实例](https://help.aliyun.com/document_detail/2850861.html)，它将帮助您更直观地理解整个流程。在初步了解ECS后，您可以通过阅读本文，了解自定义购买实例时更加详细的配置说明。

## 前提条件
* 注册中国站阿里云账号，并完成实名认证。具体操作，请参见[阿里云账号注册流程](https://help.aliyun.com/document_detail/37195.html)。

* 开通按量付费ECS资源时，您的阿里云账户余额（即现金余额）和代金券的总值不得小于100.00元人民币。具体充值操作，请参见[在线充值](https://help.aliyun.com/document_detail/112258.html)。

## 操作步骤
1. 前往[实例购买页](https://ecs-buy.aliyun.com/wizard/#/)。

2. 选择**自定义购买**页签。

3. 选择付费类型、地域、实例规格、镜像等配置。

   各配置项详细说明，请参考[配置项说明](#a76e4b20ea11c)。
4. 在最终创建实例前，请在页面右侧检查实例的整体配置并配置使用时长等选项，确保符合您的要求。

5. 阅读并签署**《云服务器ECS服务条款》** 等服务协议（若已签署，则无需重复签署，请以页面提示为准），然后单击**确认下单**。

   创建实例一般需要3\~5分钟，请您耐心等待。您可前往控制台的实例列表页面查看实例的状态，当实例状态变为**运行中**时，表示实例创建完成。

## 配置项说明
### 付费类型

付费类型影响实例的计费和收费规则，不同付费类型的实例遵循的资源状态变化规则也存在差异。
<table> <thead> <tr> <td> <p><b>付费模式</b></p> </td> <td> <p><b>说明</b></p> </td> <td> <p><b>相关文档</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>包年包月</b></p> </td> <td> <p>先付费后使用<span>，最短可以按周购买</span>。适用于长期稳定的业务，如7\*24的Web服务、数据库服务等。</p> </td> <td> <p><a href="https://help.aliyun.com/document_detail/56220.html#subs-china">包年包月</a></p> </td> </tr> <tr> <td> <p><b>按量付费</b></p> </td> <td> <p>先使用后付费，计费周期精确到秒，方便您按需购买和释放资源。适用于有大幅波动的场景，如临时扩展、测试、电商抢购等。</p> <div> <div> <i></i> </div> <div> <strong>说明 </strong> <p>推荐搭配使用<span>节省计划、</span>预留实例券优化成本。</p> </div> </div> </td> <td> <ul> <li> <p><a href="https://help.aliyun.com/document_detail/40653.html#Pay-As-You-Go">按量付费</a></p> </li> <li> <p><a href="https://help.aliyun.com/document_detail/184083.html#concept-1950739">什么是节省计划</a></p> </li> <li> <p><a href="https://help.aliyun.com/document_detail/100371.html#concept-t2m-n4q-dgb">什么是预留实例券</a></p> </li> </ul> </td> </tr> <tr> <td> <p><b>抢占式实例</b></p> </td> <td> <p>先使用后付费，相对于按量付费实例能最高节约90%的实例成本，但可能因市场价格变化或实例规格库存不足而自动释放实例。适用于无状态、容错能力强、中断容忍度高的业务场景，如测试、实时分析等。</p> </td> <td> <p><a href="https://help.aliyun.com/document_detail/178880.html#concept-1936192">抢占式实例</a></p> </td> </tr> </tbody> </table>

### 地域

地域指数据中心所在的地理区域，选择距离近的地域可以降低网络时延，**实例创建完成后不支持更改地域** 。更多信息，请参见[地域和可用区](https://help.aliyun.com/document_detail/40654.html#concept-2459516)。

### 网络及可用区

推荐您使用专有网络，专有网络之间逻辑上彻底隔离，安全性更高，且支持弹性公网IP（EIP）、弹性网卡、IPv6等功能。

可用区是指在同一地域内，电力和网络互相独立的物理区域。同一可用区内实例之间的网络延时更小，其用户访问速度更快。
<table> <thead> <tr> <td> <p><b>网络类型</b></p> </td> <td> <p><b>说明</b></p> </td> <td> <p><b>相关文档</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>专有网络</b></p> </td> <td> <p>专有网络是您在阿里云自己定义的一个隔离网络环境，您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等。</p> <p>如果在创建实例时不需要自定义专有网络配置，您可以跳过本步骤，系统会自动创建默认专有网络和交换机。</p> <div> <p>选择已有的专有网络和交换机，或者单击<b>创建专有网络</b>、<b>创建交换机</b>前往专有网络控制台即时创建专有网络和交换机。创建完成后，返回ECS实例创建向导并单击<img>图标，查看专有网络和交换机列表。</p> <div> <div> <i></i> </div> <div> <strong>说明 </strong> <p>如果您需要为实例分配IPv6地址，请选择已开通IPv6网段的专有网络和交换机。</p> </div> </div> </div> </td> <td> <ul> <li> <p><a href="https://help.aliyun.com/document_detail/34217.html#concept-kbk-cpz-ndb">什么是专有网络VPC</a></p> </li> <li> <p><a href="https://help.aliyun.com/document_detail/65398.html#section-znz-rbv-vrx">创建专有网络和交换机</a></p> </li> <li> <p><a href="https://help.aliyun.com/document_detail/65387.html#section-ts9-t3s-8vw">创建交换机</a></p> </li> <li> <p><a href="https://help.aliyun.com/document_detail/98918.html#section-ucc-t6j-xv6">为VPC开启IPv6</a></p> </li> <li> <p><a href="https://help.aliyun.com/document_detail/98922.html#section-xz0-9p6-jlk">为已有交换机开通IPv6网段</a></p> </li> </ul> </td> </tr> </tbody> </table>

### 实例和镜像

实例规格和镜像定义了一台实例的基本属性：vCPU、内存和操作系统等基础资源。

#### **实例规格**

可选的实例规格和地域等因素有关，您可以前往[ECS实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)查看实例的可购情况。

如果您有特定的配置需求，例如需要挂载多张弹性网卡、使用ESSD云盘、使用本地盘等，请确认实例规格是否支持。关于实例规格的特点、适用场景、指标数据等信息，请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#concept-sx4-lxv-tdb)。  
如果选择**付费类型** 为**抢占式实例**，配置使用时长和上限价格。

* **实例使用时长**：使用时长指抢占式实例的保护期，超出保护期后可能因市场价格变化或实例规格库存不足而自动释放实例。

  <table> <thead> <tr> <td> <p><b>实例使用时长</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>设定实例使用1小时</b></p> </td> <td> <p>抢占式实例创建后有1小时保护期，在保护期内不会被自动释放。</p> </td> </tr> <tr> <td> <p><b>无确定使用时长</b></p> </td> <td> <p>抢占式实例创建后没有保护期，但比有保护期的抢占式实例更优惠。</p> </td> </tr> </tbody> </table>
* **单台实例上限价格**：

  <table> <thead> <tr> <td> <p><b>单台实例上限价格</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>使用自动出价</b></p> </td> <td> <p>始终使用实例规格的实时市场价格，该市场价格不会超过对应按量付费实例的价格。使用自动出价可以避免抢占式实例因实时市场价格超过上限被自动释放，但不能避免因实例规格的库存不足被自动释放。</p> </td> </tr> <tr> <td> <p><b>设置单台上限价</b></p> </td> <td> <p>自行输入明确的价格上限，实例规格的实时市场价格超出该上限或者库存不足时，抢占式实例都会被自动释放。</p> </td> </tr> </tbody> </table>

#### **镜像**

镜像提供了运行实例所需的信息，阿里云提供多种镜像来源供您方便地获取镜像，如下表所示。
<table> <thead> <tr> <td> <p><b>镜像来源</b></p> </td> <td> <p><b>说明</b></p> </td> <td> <p><b>相关文档</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>公共镜像</b></p> </td> <td> <p>阿里云官方提供的基础镜像，均已获得正版授权，涵盖Windows Server系统镜像和主流的Linux系统镜像。</p> <div> <div> <i></i> </div> <div> <strong>说明 </strong> <p>当您选择倚天实例规格族g8y/c8y/r8y以及Alibaba Cloud Linux镜像时，即可为实例配置应用加速功能，实现不同程度的性能提升。更多信息，请参见<a href="https://help.aliyun.com/document_detail/2409267.html">应用性能加速</a>。</p> </div> </div> </td> <td> <p><a href="https://help.aliyun.com/document_detail/108393.html#concept-x4k-22r-wgb">公共镜像</a></p> </td> </tr> <tr> <td> <p><b>自定义镜像</b></p> </td> <td> <p>您自行创建或导入的镜像，包含了初始系统环境、应用环境、软件配置等信息，可以节省重复配置的时间。</p> </td> <td> <p><a href="https://help.aliyun.com/document_detail/172789.html#concept-2553000">自定义镜像</a></p> </td> </tr> <tr> <td> <p><b>共享镜像</b></p> </td> <td> <p>其他阿里云账号共享的自定义镜像，方便跨账号使用同一镜像创建实例。</p> </td> <td> <p><a href="https://help.aliyun.com/document_detail/25463.html#concept-e1j-jgm-xdb">共享自定义镜像</a></p> </td> </tr> <tr> <td> <p><b>云市场镜像</b></p> </td> <td> <p>云市场镜像中的镜像均经过严格审核，种类丰富，方便您一键部署用于建站、应用开发等场景的云服务器。</p> </td> <td> <p><a href="https://help.aliyun.com/document_detail/52224.html#concept-spg-mct-xdb">云市场镜像</a></p> </td> </tr> <tr> <td> <p><b>社区镜像</b></p> </td> <td> <p>社区镜像是一种完全公开的镜像。您可以将制作好的自定义镜像发布为社区镜像供他人使用，也可以获取并使用他人发布的社区镜像。</p> </td> <td> <p><a href="https://help.aliyun.com/document_detail/208369.html#concept-2056865">社区镜像</a></p> </td> </tr> </tbody> </table> 您也可以通过镜像全局搜索更精细地查找和筛选目标镜像，单击![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5178585271/p846082.png)时会弹出**镜像目录** 对话框，在镜像目录中查找所需镜像来创建ECS实例。更多信息，请参见[镜像目录](https://help.aliyun.com/document_detail/2574204.html)。

<br />

**说明**

创建ECS实例时可能因为镜像与实例规格的特性不匹配、镜像与实例规格处理器不兼容等问题看不到某些镜像（包括自定义镜像），处理建议请参见[为什么创建ECS实例时看不到某些镜像？](https://help.aliyun.com/document_detail/2834411.html)

### 存储

实例通过添加系统盘、数据盘、弹性临时盘和文件存储NAS获得存储能力，云服务器ECS提供了云盘和本地盘，以满足不同场景的需求。

* 云盘可以用作系统盘和数据盘，包括ESSD云盘、SSD云盘、高效云盘等类型。更多信息，请参见[云盘概述](https://help.aliyun.com/document_detail/25383.html#concept-n1s-rzb-wdb)。

  **说明**

  随实例一起创建的云盘和实例的付费模式相同。
* 本地盘只能用作数据盘，如果实例规格配备了本地盘（例如本地SSD型、大数据型等），页面中会显示本地盘的信息。更多信息，请参见[本地盘](https://help.aliyun.com/document_detail/63138.html#concept-g3w-qzv-tdb)。

  **说明**

  不支持自行为实例挂载本地盘。

#### **系统盘**

系统盘用于安装操作系统，默认容量为40 GiB，但实际可设置的最低容量和镜像类型有关，如下表所示。
<table> <thead> <tr> <td> <p><b>镜像</b></p> </td> <td> <p><b>系统盘容量范围（GiB）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>Linux（不包括FreeBSD和Red Hat）</p> </td> <td> <p>\[max{20, 镜像文件大小}, 2048\]</p> </td> </tr> <tr> <td> <p>FreeBSD</p> </td> <td> <p>\[max{30, 镜像文件大小}, 2048\]</p> </td> </tr> <tr> <td> <p>Red Hat</p> </td> <td> <p>\[max{40, 镜像文件大小}, 2048\]</p> </td> </tr> <tr> <td> <p>Windows</p> </td> <td> <p>\[max{40, 镜像文件大小}, 2048\]</p> </td> </tr> </tbody> </table>

#### **（可选）数据盘**

数据盘用于存储应用数据，选择数据盘时，您还可以加密云盘满足数据安全或法规合规等场景的要求。关于数据加密的介绍，请参见[加密云盘](https://help.aliyun.com/document_detail/59643.html#concept-2383230)。  
**说明**

单台实例支持挂载的数据盘存在数量限制。更多信息，请参见[块存储使用限制](https://help.aliyun.com/document_detail/25412.html#BlockStorageQuota)。

#### **（可选）快照服务**

快照是云盘在某一时间点数据状态的备份文件，用快照创建云盘便于快速导入数据。创建实例时即可为云盘开启自动备份，有效应对数据误删等风险。

选择已有的自动快照策略，或者单击**创建自动快照策略** 前往快照页面即时创建自动快照策略。具体操作，请参见[创建自动快照策略](https://help.aliyun.com/document_detail/127767.html#task-1443510)。创建完成后，返回ECS实例创建向导并单击![refresh](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0575702261/p278001.png)图标，查看自动快照策略列表。  
**重要**

使用快照会产生费用，更多详情，请参见[快照计费](https://help.aliyun.com/document_detail/56159.html)。

#### **（可选）弹性临时盘**

弹性临时盘是一款可灵活随实例创建或单独创建的、您可以自定义选择容量大小的块存储设备，作为临时数据存储使用，为ECS实例提供临时数据存储，具备高性能、高性价比等特点。更多信息，请参见[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)。

#### **（可选）文件存储NAS**

如果您有较多数据需要供多台实例共享访问，推荐使用NAS文件系统，可以节约大量拷贝与同步成本。

选择已有的NAS文件系统，或者单击**创建文件系统** 前往NAS文件系统控制台即时创建NAS文件系统。具体操作，请参见[通过控制台创建通用型NAS文件系统](https://help.aliyun.com/document_detail/27530.html#section-5jo-0kj-jn5)。创建完成后，返回ECS实例创建向导并单击![refresh](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0575702261/p278001.png)图标，查看NAS文件系统列表。关于挂载NAS文件系统时的注意事项，请参见[新购ECS时挂载NAS文件系统](https://help.aliyun.com/document_detail/162688.html#task-2480876)。

### 带宽和安全组

网络和安全组配置提供了公网以及与其他阿里云资源通信的能力，并保障实例在网络中的安全。

#### **（可选）公网IP**

如果实例需要进行公网通信，必须分配公网IP。您可以在创建实例时选择自动分配一个固定公网IP，或者在创建实例后自行配置，通过EIP、NAT网关等方式进行公网通信。EIP、NAT网关需要自行购买，更多信息，请参见[什么是弹性公网IP](https://help.aliyun.com/document_detail/32321.html#concept-zmv-hd3-vdb)和[什么是 NAT 网关](https://help.aliyun.com/document_detail/32322.html#concept-wpm-kfy-ydb)。

选中**分配公网 IPv4 地址** ，设置**带宽计费模式** 和**带宽值** 或**带宽峰值**。  
关于公网带宽计费的详细规则，请参见[公网带宽计费](https://help.aliyun.com/document_detail/25411.html#publicIP-china)。
<table> <thead> <tr> <td> <p><b>带宽计费模式</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>按固定带宽</b></p> </td> <td> <p><b>按指定的带宽值收费</b>，实际的出网带宽不会高于指定的带宽值。</p> <ul> <li> <p>适用于对网络带宽要求比较稳定的业务场景。</p> </li> <li> <p>如果云服务器使用率较高，需长时间使用带宽，或带宽利用率高于10%，建议选择按固定带宽计费。</p> </li> </ul> </td> </tr> <tr> <td> <p><b>按使用流量</b></p> </td> <td> <p><b>按实际产生的网络带宽流量收费</b>。为避免产生高额的带宽流量费，可先设置出网带宽峰值。</p> <ul> <li> <p>适用于对网络带宽需求变化较大的业务场景。</p> </li> <li> <p>如果公网带宽利用率不高于10%，平时没什么流量，在某个高峰时段流量波动较大，建议选择按使用流量计费。</p> </li> </ul> <p><b>（可选）：</b>选中<b>升级至CDT计费</b>。CDT以灵活计费、提供免费流量、阶梯价格优惠及多产品统一计费等优势，为公网带宽费用管理提供高效经济的解决方案。相对于按量付费，有一定的折扣优惠。更多信息，请参见<a href="https://help.aliyun.com/document_detail/2357716.html">什么是云数据传输CDT</a>。</p> <div> <div> <i></i> </div> <div> <strong>重要 </strong> <ul> <li> <p>自2024年12月12日0时起，您无需额外操作即可直接使用云数据传输（CDT），享受高效服务。</p> </li> <li> <p>升级为CDT计费后，所有存量和新增的按流量计费实例将通过CDT统一计费和出账，按带宽计费的实例继续在原来的云产品上统计费用和出账。您可以前往费用与成本，在账单详情页面查看CDT的账单情况。</p> </li> <li> <p>开通CDT即可获得 220 GB/月公网流量免费额度，<span>其中20 GB/月可用于<b>中国内地地域</b>，200 GB/月可用于<b>非中国内地地域</b>。</span></p> </li> </ul> </div> </div> </td> </tr> </tbody> </table>

#### **安全组**

安全组是一种虚拟防火墙，用于控制安全组内实例的入流量和出流量。更多信息，请参见[安全组概述](https://help.aliyun.com/document_detail/25387.html#concept-o2y-mqw-ydb)。

当选择的VPC下没有安全组时，系统会自动创建默认安全组。默认安全组入方向放行22端口、3389端口及ICMP协议，您也可以根据需求，放行80、443端口，或者在创建完成后修改安全组配置。

您也可以根据业务需要，选择**已有安全组** 或**新建安全组** ，新建安全组时，需配置**安全组名称** 、**安全组类型** 、**开通IPv4端口/协议**。  
**说明**

关于安全组各项配置的详细说明，请参见[创建安全组](https://help.aliyun.com/document_detail/25468.html#concept-ocl-bvz-xdb)。

#### **（可选）弹性网卡**

弹性网卡分为主网卡和辅助网卡。主网卡不支持从实例解绑，只能随实例一起创建和释放。辅助网卡支持自由绑定至实例和从实例解绑，方便您在实例之间切换网络流量。如需随实例一起创建辅助网卡，请单击![add-nic](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0579352261/p278943.png)图标，然后选择辅助网卡所属的交换机。  
**说明**

创建实例时只能添加1块辅助网卡，您也可以在实例创建完成后单独创建辅助网卡并绑定至实例。关于各实例规格支持绑定的弹性网卡的数量，请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#concept-sx4-lxv-tdb)。

#### **（可选）配置IPv6**

开通了IPv6后，IPv6的地址数量不仅能解决网络地址资源数量的问题，而且也解决了多种接入设备连入互联网的障碍。

选中**免费分配 IPv6 地址** 。分配IPv6地址后，您需要登录实例并在操作系统内部进行IPv6地址相关的配置，才能正常使用IPv6地址。具体操作，请参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

### 管理设置

管理设置包括登录凭证和标签，用于远程连接实例和方便地检索和管理资源。

#### **登录凭证**

**登录凭证** 用于安全地登录实例，关于实例连接方式的介绍，请参见[选择ECS远程连接方式](https://help.aliyun.com/document_detail/71529.html#concept-tmr-pgx-wdb)。
<table> <thead> <tr> <td> <p><b>登录凭证</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>密钥对</b></p> <div> <div> <i></i> </div> <div> <strong>说明 </strong> <p>仅Linux实例支持使用密钥对登录认证。</p> </div> </div> </td> <td> <p>选择登录实例的用户名和已有的密钥对，或者单击<b>创建密钥对</b>即时创建密钥对。创建完成后，返回ECS实例创建向导并单击<img>图标，查看密钥对列表。具体操作，请参见<a href="https://help.aliyun.com/document_detail/51793.html#concept-wy4-th1-ydb">创建SSH密钥对</a>。</p> <div> <p>用户名支持设置为<b>root</b>或<b>ecs-user</b>。</p> <div> <div> <i></i> </div> <div> <strong>警告 </strong> <p>root具有操作系统的最高权限，使用root作为用户名可能会导致安全风险，建议您使用普通用户ecs-user作为用户名。</p> </div> </div> </div> </td> </tr> <tr> <td> <p><b>使用镜像预设密码</b></p> <div> <div> <i></i> </div> <div> <strong>说明 </strong> <p>仅<b>自定义镜像</b>和<b>共享镜像</b>支持此认证方式。</p> </div> </div> </td> <td> <p>可以直接使用所选镜像的预设密码进行登录认证。为了保证您的正常使用，请确保所选镜像中已经设置了密码。</p> </td> </tr> <tr> <td> <p><b>自定义密码</b></p> </td> <td> <p>输入并确认密码。使用登录名和密码登录实例时，用户名信息如下：</p> <ul> <li> <p>Linux实例：支持设置为<b>root</b>或<b>ecs-user</b>。</p> <div> <div> <i></i> </div> <div> <strong>警告 </strong> <p>root具有操作系统的最高权限，使用root作为用户名可能会导致安全风险，建议您使用普通用户ecs-user作为用户名。</p> </div> </div> </li> <li> <p>Windows实例：默认为<b>administrator</b>。</p> </li> </ul> </td> </tr> <tr> <td> <p><b>创建后设置</b></p> </td> <td> <p>在实例创建完成后，自行绑定密钥对或者重置实例密码。具体操作，请参见<a href="https://help.aliyun.com/document_detail/51796.html#concept-zzt-nl1-ydb">绑定SSH密钥对</a>和<a href="https://help.aliyun.com/document_detail/25439.html#concept-qct-gfl-xdb">重置实例登录密码</a>。</p> </td> </tr> </tbody> </table>

#### **（可选）标签**

**标签** 由一对键值（Key-Value）组成，用来标识创建的实例、云盘、弹性网卡主网卡，便于检索和管理资源。可选择已有的标签，或者填写标签键和标签值即时创建标签。关于标签的更多信息，请参见[标签](https://help.aliyun.com/document_detail/25477.html#concept-jzp-qtd-zdb)。

### （可选）高级选项

高级选项包括主机名、实例元数据、实例自定义数据等，用于定制实例在控制台和操作系统内显示的信息或使用方式。
<table> <thead> <tr> <td> <p><b>参数</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>实例名称</b>、<b>描述</b>、<b>主机名</b>、<b>有序后缀</b></p> </td> <td> <p>创建多台实例时，设置有序的实例名称和主机名称便于从名称了解实例的批次等信息。关于设置有序名称的规则，请参见<a href="https://help.aliyun.com/document_detail/196048.html#concept-2004153">批量设置有序的实例名称或主机名称</a>。</p> </td> </tr> <tr> <td> <p><b>实例RAM角色</b></p> </td> <td> <p>实例通过实例RAM角色获得该角色拥有的权限，可以基于临时安全令牌STS（Security Token Service）访问指定云服务的API和操作指定的云资源，安全性更高。</p> <p>选择已有的实例RAM角色，或者单击<b>创建实例RAM角色</b>前往RAM控制台即时创建实例RAM角色。创建完成后，返回ECS实例创建向导并单击<img>图标，查看实例RAM角色列表。具体操作，请参见<a href="https://help.aliyun.com/document_detail/61175.html#concept-v3v-zct-xdb">创建实例RAM角色并为角色授予权限</a>。</p> </td> </tr> <tr> <td> <p><b>元数据访问模式</b></p> </td> <td> <p>实例元数据（metadata）包含了实例在阿里云系统中的信息，您可以在运行中的实例内方便地查看实例元数据，并基于实例元数据配置或管理实例。关于如何查看实例元数据，请参见<a href="https://help.aliyun.com/document_detail/108460.html#concept-dwj-y1x-wgb">实例元数据</a>。</p> </td> </tr> <tr> <td> <p><b>自定义数据</b></p> </td> <td> <p>实例自定义数据可以作为实例自定义脚本在启动实例时执行，实现自动化配置实例，或者仅作为普通数据传入实例。更多信息，请参见<a href="https://help.aliyun.com/document_detail/49121.html">自定义实例初始化配置</a>。</p> <p>在输入框输入您准备的实例自定义数据。如果实例自定义数据已进行Base64编码，请选中<b>输入已采用 Base64 编码</b>。</p> </td> </tr> <tr> <td> <p><b>资源组</b></p> </td> <td> <p>资源组供您从业务角度管理跨地域、跨产品的资源，并支持针对资源组管理权限。更多信息，请参见<a href="https://help.aliyun.com/document_detail/100034.html#concept-fdn-wtm-cgb">资源组</a>。</p> <p>选择已有的资源组，或者单击<b>创建资源组</b>前往资源管理控制台即时创建资源组。创建完成后，返回ECS实例创建向导并单击<img>图标，查看资源组列表。具体操作，请参见<a href="https://help.aliyun.com/document_detail/94485.html#task-xpl-kjm-4fb">创建资源组</a>。</p> </td> </tr> <tr> <td> <p><b>部署集</b></p> </td> <td> <p>部署集支持高可用策略，部署集内实例会严格分散在不同的物理服务器上，保证业务的高可用性和底层容灾能力。</p> <p>选择已有的部署集，或者单击<b>管理部署集</b>即时创建部署集。创建完成后，返回ECS实例创建向导并单击<img>图标，查看部署集列表。具体操作，请参见<a href="https://help.aliyun.com/document_detail/91258.html">部署集</a>。</p> </td> </tr> <tr> <td> <p><b>专有宿主机</b></p> </td> <td> <p>专有宿主机是一台由单租户独享物理资源的云主机，具有满足严格的安全合规要求、允许自带许可证（BYOL）上云等优势。</p> <p>选择已有的专有宿主机，或者单击<b>创建专有宿主机</b>即时创建专有宿主机。创建完成后，返回ECS实例创建向导并单击<img>图标，查看专有宿主机列表。具体操作，请参见<a href="https://help.aliyun.com/document_detail/68984.html#task-fbz-5mn-tdb">创建DDH</a>。</p> </td> </tr> <tr> <td> <p><b>私有池类型</b></p> </td> <td> <p>创建弹性保障或容量预定后，系统会自动生成私有池，预留特定属性特定数量的实例。从关联的私有池中创建这一类实例，可以提供资源确定性保障。更多信息，请参见<a href="https://help.aliyun.com/document_detail/193626.html#concept-1997477">资源管家概述</a>。</p> <div> <div> <i></i> </div> <div> <strong>说明 </strong> <p>弹性保障和容量预定仅支持为按量付费实例保障资源供应确定性。</p> </div> </div> <ul> <li> <p><b>开放</b>：优先使用开放类型私有池的容量，如果开放类型私有池无可用容量，则尝试使用公共池的容量。</p> </li> <li> <p><b>不使用 </b>：不使用任何私有池的容量。</p> </li> <li> <p><b>指定</b>：继续指定一个专用或开放类型私有池的ID，使用其容量创建实例。如果该私有池没有可用容量，则创建失败。</p> </li> </ul> </td> </tr> </tbody> </table>

## 后续步骤
* **连接实例**

  支持通过多种方式连接实例，包括Workbench、VNC和第三方客户端工具。更多信息，请参见[选择ECS远程连接方式](https://help.aliyun.com/document_detail/71529.html)。
* **初始化数据盘**

  如果您随实例创建了数据盘，必须先对数据盘进行分区格式化才能正常使用。具体操作，请参见[初始化数据盘（Linux）](https://help.aliyun.com/document_detail/25426.html#concept-jl1-qzd-wdb)和[初始化数据盘（Windows）](https://help.aliyun.com/document_detail/25418.html)。
* **部署环境、搭建网站、搭建应用**

  创建实例后，您可以使用ECS实例部署环境、搭建网站和应用等。更多信息，请参见[搭建环境](https://help.aliyun.com/document_detail/151696.html)、[搭建网站](https://help.aliyun.com/document_detail/151697.html)、[搭建应用](https://help.aliyun.com/document_detail/151698.html)。

## 相关文档
* [RunInstances](https://help.aliyun.com/document_detail/63440.html#doc-api-Ecs-RunInstances)：创建一台或多台按量付费或者包年包月ECS实例。

* [实例FAQ](https://help.aliyun.com/document_detail/108473.html#concept-gqy-fyx-wgb)

* 获取价格折扣信息

  您可以调用[DescribePrice](https://help.aliyun.com/document_detail/2679957.html)接口查询云服务器ECS资源的最新价格，例如活动规则、价格、折扣等信息。

  CLI命令参考如下。例如，查询在华东1（杭州）地域创建一个实例规格为`ecs.c6.xlarge`的最新价格信息。

  ```
  HELPCODEESCAPE-shell
  aliyun ecs DescribePrice --region cn-hangzhou --RegionId 'cn-hangzhou' --ResourceType instance --InstanceType 'ecs.c6.xlarge'
  ```

<br />
