突发性能实例是一种面向入门级计算场景，应对突发性能需求的经济型实例规格。本文介绍突发性能实例规格族的特点和应用场景，以及基准性能、CPU积分、性能模式等概念，并列出了具体的实例规格。  

## 什么是突发性能实例
突发性能实例是一种通过CPU积分来保证计算性能的实例规格，适用于平时CPU使用率低，但偶尔有突发高CPU使用率的场景。突发性能实例在创建后可以持续获得CPU积分，在性能无法满足负载要求时，通过消耗更多CPU积分来无缝提高计算性能，不会影响部署在实例上的环境和应用。较之其他实例规格，突发性能实例的CPU使用更加灵活且成本较低。

通过CPU积分，您可以从整体业务角度分配计算资源，将业务平峰期的计算能力转移到高峰期使用，以节约使用成本。如果偶尔会出现计划外的高性能需求，您还可以选择为突发性能实例打开无性能约束模式。  
突发性能实例规格包括以下两类：

* [突发性能实例规格族t6](#section-6gl-pk7-f56)

* [突发性能实例规格族t5](#section-mq2-x7y-0jl)

**说明**

突发性能实例是一种特殊的共享型实例，其他共享型实例规格族，请参见[共享型](https://help.aliyun.com/document_detail/108489.html#concept-ycf-pzy-wgb)。  
基准性能、CPU积分和性能模式是突发性能实例的基本概念，相关说明如下表所示。
<table> <thead> <tr> <td><p><b>基本概念</b></p></td> <td><p><b>说明</b></p></td> <td><p><b>详情及示例</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>基准性能</p></td> <td><p>实例可以持续稳定地提供的CPU性能，由实例规格决定。</p></td> <td><p><a href="#section-dpw-65z-7kv">基准性能</a></p></td> </tr> <tr> <td><p>初始CPU积分</p></td> <td><p>创建突发性能实例时一次性获得的CPU积分，固定为每vCPU 30个积分。</p></td> <td><p><a href="#section-h4n-jgr-6b4">CPU积分</a></p></td> </tr> <tr> <td><p>CPU积分余额</p></td> <td><p>突发性能实例持续获得的CPU积分超过消耗的CPU积分，即转化为CPU积分余额，用于将CPU使用率提升到基准性能以上。</p></td> <td><p><a href="#section-h4n-jgr-6b4">CPU积分</a></p></td> </tr> <tr> <td><p>最大CPU积分余额</p></td> <td><p>一台突发性能实例24小时可以获得的CPU积分，CPU积分余额最多保存24小时，保持动态平衡。对指定实例规格来说，CPU积分获得速度是固定的，因此CPU积分余额有上限。</p></td> <td><p><a href="#section-h4n-jgr-6b4">CPU积分</a></p></td> </tr> <tr> <td><p>性能模式</p></td> <td> <div> <p>分为性能约束模式和无性能约束模式。</p> <ul> <li><p>在性能约束模式下，如果没有可用的CPU积分，CPU使用率将无法超过基准性能。</p></li> <li><p>在无性能约束模式下，突发性能实例可以透支或付费使用CPU积分，在任意时间段保持高于基准性能的CPU使用率，但是可能会产生相应额外费用。</p></li> </ul> </div></td> <td><p><a href="#section-svb-w9d-dju">性能模式</a></p></td> </tr> <tr> <td><p>预支CPU积分</p></td> <td><p>未来24小时可以获得的CPU积分，可能产生额外费用。仅在打开无性能约束模式时可以透支使用。</p></td> <td><p><a href="#section-svb-w9d-dju">性能模式</a></p></td> </tr> <tr> <td><p>超额CPU积分</p></td> <td><p>预支CPU积分消耗完毕后，继续维持高于基准性能的CPU使用率会消耗CPU积分，会产生额外费用。仅在打开无性能约束模式时可以使用。</p></td> <td><p><a href="#section-svb-w9d-dju">性能模式</a></p></td> </tr> </tbody> </table>

## 突发性能实例应用场景
在购买企业级等类型的实例后，您拥有实例vCPU的完全使用权，同时这意味着无论CPU使用率是0%还是100%，您都需要为整个vCPU付费。如果您的业务场景规律，仅在特定的时段有较高的CPU性能需求，那么在其他时段您也在为未能使用的计算资源付费。这种情况下，您可以选择突发性能实例，以打造高性价比、经济实用的服务器。  
突发性能实例适用于在某些时段对计算性能有突发性要求的场景，例如开发测试压测服务应用、轻负载应用、微服务、Web应用服务器等。购买前请评估业务在平峰期和高峰期的实例性能需求，至少选择基准性能满足平峰期需求的实例规格，选择得当可以在满足整体性能需求的同时节省成本。  
**说明**

* 如果您在使用过程中发现所选突发性能实例规格无法满足需求，也可以进行变配操作。更多信息，请参见[变配说明](#section-vg2-yxn-ore)。

* Windows应用负载、图形UI对CPU占用要求较高，选用突发型t系列实例规格可能会出现卡顿或宕机现象，建议您根据实际情况调整实例规格，例如选择通用型g系列、计算型c系列、内存型r系列等实例规格。

## 基准性能
突发性能实例的基准性能由实例规格决定，基准性能是实例可以持续稳定地提供的CPU性能。您可以从实例规格指标数据的平均基准CPU计算性能列查看不同实例规格的基准性能。

## CPU积分
CPU积分可以视为您持有的计算能力，决定突发性能实例实际可以达到的计算性能。相关概念和示例如下：

### 初始CPU积分

为保证您开机后拥有CPU积分完成部署，创建一台突发性能实例后，每个vCPU会获得30个CPU积分，即初始CPU积分。

例如，ecs.t5-lc1m2.large配有2个vCPU，新建实例拥有60个初始CPU积分。ecs.t5-c1m1.xlarge配有4个vCPU，新建实例拥有120个初始CPU积分。

### 获取积分速度

实例开机后即消耗CPU积分维持计算性能，同时按固定速度获得CPU积分，CPU积分的获得速度由实例规格决定，请参见实例规格指标数据的CPU积分/小时列，该指标为单台实例所有vCPU每小时可以获得的CPU积分。

例如，ecs.t5-c1m1.large实例的基准性能为25%，表示每小时单vCPU持续获得CPU积分，可以供该vCPU以使用率25%运行1小时，以使用率100%运行15分钟（60\*25%）。与基准性能对应，每个vCPU每小时获得15个CPU积分，ecs.t5-c1m1.large实例有2个vCPU，因此每小时获得30个CPU积分。

### CPU积分余额

如果获得的CPU积分大于消耗的CPU积分，多出的部分会保留，即CPU积分余额，CPU积分余额最多保存24小时，保持动态平衡。对指定实例规格来说，CPU积分获得速度是固定的，因此CPU积分余额有上限。CPU积分余额上限为指定实例规格24小时可以获得的CPU积分数，请参见实例规格指标数据的最大CPU积分余额列。

例如，ecs.t5-c1m1.large实例每小时可以获得30个CPU积分，则CPU最大积分余额为720（30\*24）。

### 消耗CPU积分

CPU积分的消耗速度和突发性能实例的vCPU数、CPU使用率和工作时间有关。例如，以下三种情况都会消耗掉1个CPU积分：

* 1个vCPU以100%使用率运行1分钟

* 1个vCPU以50%使用率运行2分钟

* 2个vCPU以25%使用率运行2分钟

突发性能实例开机后即消耗CPU积分维持计算性能，优先消耗初始CPU积分，初始CPU积分消耗完毕后不会恢复，之后只可消耗获得的CPU积分。

* 当CPU使用率低于基准性能时，消耗的CPU积分少于获得的CPU积分，CPU积分余额逐渐增加。

* 当CPU使用率等于基准性能时，消耗的CPU积分等于获得的CPU积分，CPU积分余额保持不变。

* 当CPU使用率高于基准性能时，消耗的CPU积分大于获得的CPU积分，CPU积分余额逐渐减少。

**说明**

CPU积分消耗所基于的CPU使用率是在物理机层面采集的（包含了云服务器内部特权指令的模拟开销），您可以登录云监控管理控制台，在**主机监控** 页面单击实例ID，然后在**基础监控** 页签中查看相关数据。更多信息，请参见[主机监控概览](https://help.aliyun.com/document_detail/43503.html#concept-ypb-thv-vdb)。  

### 停机可能对获得CPU积分的影响

* 按量付费实例停机（普通停机模式），当前CPU积分余额保留，并继续获得CPU积分。

* 按量付费实例停机（节省停机模式），当前CPU积分余额失效，不会继续获得CPU积分。重启实例后获得初始CPU积分，并开始获得CPU积分。

* 按量付费实例欠费停机，当前CPU积分余额保留，但不会继续获得CPU积分。结清按量付费账单后继续获得CPU积分。

* 包年包月实例到期后停机，当前CPU积分余额保留，但不会继续获得CPU积分。重启后继续获得CPU积分。

* 包年包月实例未到期停机，当前CPU积分余额保留，并继续获得CPU积分。

## 性能模式
突发性能实例的运行模式分为性能约束模式和无性能约束模式。

### 性能约束模式

在性能约束模式下，突发性能实例的性能受CPU积分的约束。初始CPU积分和CPU积分余额消耗完毕后，实例性能将无法超过基准性能。但在CPU积分余额较少时，实例性能将在15分钟内逐渐下降到基准性能水平，保证CPU积分余额消耗完毕后，实例性能不会急剧下降。

性能约束模式适用于负载稳定，CPU使用率不会长时间超过基准性能，偶尔需要提高计算性能完成工作的场景，例如轻量级的Web服务器、开发测试环境、中低性能数据库等。

### 无性能约束模式

在无性能约束模式下，突发性能实例可以突破可用CPU积分的约束，通过透支或付费使用CPU积分在任意时间段保持高于基准性能的CPU使用率。初始CPU积分和CPU积分余额消耗完毕后，如果实例的CPU使用率仍然高于基准性能，将开始消耗预支CPU积分和超额CPU积分。

* 预支CPU积分：未来24小时可以获得的CPU积分，可能会产生额外费用。

* 超额CPU积分：预支CPU积分消耗完毕后，继续维持高于基准性能的CPU使用率会消耗的CPU积分，并产生额外费用。

**说明**

消耗预支CPU积分和超额CPU积分时产生额外费用的情况和收费标准，请参见[额外费用](https://help.aliyun.com/document_detail/90581.html#section-lqi-vqf-dsc)。  
无性能约束模式下，CPU积分变化的示意图如下所示。
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0558995771/CAEQNBiBgMDZt5no4BgiIGM3Y2U3OTNjYWRkODQ5YWJiMTQ3ZDBiZDM1ZGE3MGNi3963382_20230830144006.372.svg)  
**说明**

如果实例消耗了预支CPU积分，并在预支CPU积分恢复完毕前停止（节省停机模式）、变配或释放实例，或者切换到性能约束模式，会一次性收取预支CPU积分的费用。  
无性能约束模式适用于对CPU性能有突发使用，并且CPU积分余额无法满足需求，可能需要消耗预支CPU积分甚至超额CPU积分的场景。例如：

* 产品新功能发布、电商平台大促、网站承载推广活动等可预见会承接大量访问，并且必须在特定时间段内保持高性能的场景。您可以临时打开无性能约束模式，待高峰期结束后再关闭无性能约束模式降低成本。

* 某些网站应用负载高峰集中在固定时间段，但平均到24小时CPU使用率仍然低于基准性能的场景。您可以保持开启无性能约束模式，保证在高峰期的访问体验。如果在低访问量时段获得的CPU积分可以补齐消耗的预支CPU积分，就可以在保证网站整体访问体验的同时无需支付额外费用。

创建突发性能实例时，默认使用性能约束模式。如果您想要使用无性能约束模式，请参见[打开无性能约束模式](https://help.aliyun.com/document_detail/90634.html#section-cds-zh0-eh7)。

不同性能模式下CPU积分的变化情况示例，请参见[CPU积分变化示例](https://help.aliyun.com/document_detail/90635.html#concept-fl1-tl4-cfb)。

## 变配说明
如果您在监控突发性能实例时发现CPU使用率长期高于或者低于基准性能，说明该规格无法满足或者一直超过业务需求。建议您重新评估当前实例规格是否合适，并在需要时更换为其他实例规格。变配操作和计费方式有关，更多信息，请参见[升降配方式概述](https://help.aliyun.com/document_detail/25437.html#concept-anb-bbf-5db)。

## 突发性能实例规格族t6
t6的特点如下：

* vCPU持续提供基准性能，可突然提速，但受到CPU积分的限制

* 相比上一代突发性能实例规格族t5，性价比进一步提升

* 计算：

  * 处理器：2.5 GHz主频的最新一代Intel ^®^ Xeon ^®^服务器级别Cascade Lake处理器，睿频3.2 GHz

  * 搭配DDR4内存

* 存储：

  * I/O优化实例

  * 仅支持ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘

    **重要**

    受突发型实例规格限制，PL2和PL3性能级别的ESSD云盘无法发挥极致性能。建议您选择企业级的实例规格或者低性能级别的ESSD云盘。
* 网络：

  * 支持IPv4、IPv6

  * 仅支持专有网络VPC

* 适用场景：

  * Web应用服务器

  * 轻负载应用、微服务

  * 开发测试压测服务应用

t6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>平均基准CPU计算性能</b></p></td> <td><p><b>CPU积分/小时</b></p></td> <td><p><b>最大CPU积分余额</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.t6-c4m1.large</p></td> <td><p>2</p></td> <td><p>0.5</p></td> <td><p>5%</p></td> <td><p>6</p></td> <td><p>144</p></td> <td><p>0.08/最高0.4</p></td> <td><p>4万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c2m1.large</p></td> <td><p>2</p></td> <td><p>1.0</p></td> <td><p>10%</p></td> <td><p>12</p></td> <td><p>288</p></td> <td><p>0.08/最高0.6</p></td> <td><p>6万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m1.large</p></td> <td><p>2</p></td> <td><p>2.0</p></td> <td><p>20%</p></td> <td><p>24</p></td> <td><p>576</p></td> <td><p>0.08/最高1</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>20%</p></td> <td><p>24</p></td> <td><p>576</p></td> <td><p>0.08/最高1</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>30%</p></td> <td><p>36</p></td> <td><p>864</p></td> <td><p>0.08/最高1</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>40%</p></td> <td><p>96</p></td> <td><p>2304</p></td> <td><p>0.16/最高2</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>40%</p></td> <td><p>192</p></td> <td><p>4608</p></td> <td><p>0.32/最高4</p></td> <td><p>40万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.t6-c1m1.large、ecs.t6-c1m2.large、ecs.t6-c1m4.large、ecs.t6-c2m1.large、ecs.t6-c4m1.large。

* 您可以前往[ECS实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)，查看实例在各地域的可购情况。

* 指标的含义请参见[实例规格指标说明](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)。

## 突发性能实例规格族t5
t5实例热销中，详细信息请参见[t5实例产品页](https://promotion.aliyun.com/ntms/act/creditinstancet5.html)。  
t5的特点如下：

* vCPU持续提供基准性能，可突然提速，但受到CPU积分的限制

* 计算、内存和网络资源的平衡

* 计算：

  * 多种处理器和内存配比

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ 处理器

  * 搭配DDR4内存

* 存储：仅支持高效云盘和SSD云盘

* 网络：

  * 支持IPv4、IPv6

  * 仅支持专有网络VPC

* 适用场景：

  * Web应用服务器

  * 轻负载应用、微服务

  * 开发测试压测服务应用

t5包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>平均基准CPU计算性能</b></p></td> <td><p><b>CPU积分/小时</b></p></td> <td><p><b>最大CPU积分余额</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.t5-lc2m1.nano</p></td> <td><p>1</p></td> <td><p>0.5</p></td> <td><p>20%</p></td> <td><p>12</p></td> <td><p>288</p></td> <td><p>0.1</p></td> <td><p>4万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-lc1m1.small</p></td> <td><p>1</p></td> <td><p>1.0</p></td> <td><p>20%</p></td> <td><p>12</p></td> <td><p>288</p></td> <td><p>0.2</p></td> <td><p>6万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-lc1m2.small</p></td> <td><p>1</p></td> <td><p>2.0</p></td> <td><p>20%</p></td> <td><p>12</p></td> <td><p>288</p></td> <td><p>0.2</p></td> <td><p>6万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-lc1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>20%</p></td> <td><p>24</p></td> <td><p>576</p></td> <td><p>0.4</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-lc1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>20%</p></td> <td><p>24</p></td> <td><p>576</p></td> <td><p>0.4</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m1.large</p></td> <td><p>2</p></td> <td><p>2.0</p></td> <td><p>25%</p></td> <td><p>30</p></td> <td><p>720</p></td> <td><p>0.5</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>25%</p></td> <td><p>30</p></td> <td><p>720</p></td> <td><p>0.5</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>25%</p></td> <td><p>30</p></td> <td><p>720</p></td> <td><p>0.5</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m1.xlarge</p></td> <td><p>4</p></td> <td><p>4.0</p></td> <td><p>25%</p></td> <td><p>60</p></td> <td><p>1440</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m2.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>25%</p></td> <td><p>60</p></td> <td><p>1440</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>25%</p></td> <td><p>60</p></td> <td><p>1440</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m1.2xlarge</p></td> <td><p>8</p></td> <td><p>8.0</p></td> <td><p>25%</p></td> <td><p>120</p></td> <td><p>2880</p></td> <td><p>1.2</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m2.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>25%</p></td> <td><p>120</p></td> <td><p>2880</p></td> <td><p>1.2</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>25%</p></td> <td><p>120</p></td> <td><p>2880</p></td> <td><p>1.2</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m1.4xlarge</p></td> <td><p>16</p></td> <td><p>16.0</p></td> <td><p>25%</p></td> <td><p>240</p></td> <td><p>5760</p></td> <td><p>1.2</p></td> <td><p>60万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m2.4xlarge</p></td> <td><p>16</p></td> <td><p>32.0</p></td> <td><p>25%</p></td> <td><p>240</p></td> <td><p>5760</p></td> <td><p>1.2</p></td> <td><p>60万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.t5-lc2m1.nano、ecs.t5-c1m1.large、ecs.t5-c1m2.large、ecs.t5-c1m4.large、ecs.t5-lc1m1.small、ecs.t5-lc1m2.large、ecs.t5-lc1m2.small、ecs.t5-lc1m4.large。

* 您可以前往[ECS实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)，查看实例在各地域的可购情况。

* 指标的含义请参见[实例规格指标说明](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)。
