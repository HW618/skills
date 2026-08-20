共享型实例采用非绑定CPU调度模式。每个vCPU会被随机分配到任何空闲CPU超线程上，不同实例vCPU会争抢物理CPU资源，并导致高负载时计算性能波动不稳定，有可用性SLA保证，但无性能SLA保证。与企业级实例相比，共享型实例在资源利用上侧重于资源性能的共享，所以无法保证实例计算性能的稳定，但是成本更低。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

共享型实例主要包括：共享型实例、经济型实例和突发性能型实例。目前在售的共享型实例有：

* [经济型实例规格族e](#e)

* [共享标准型实例规格族s6](#section-wi7-mgt-163)

* [上一代共享型实例规格族xn4、n4、mn4、e4](#section-9zj-1ov-92r)

* [突发性能型（t系列）](https://help.aliyun.com/document_detail/90542.html)

## **经济型实例规格族e**
* **适用场景**：

  * 面向自主任务型智能体的轻载场景，如Claw类项目的云端部署节点，或智能体网关、编排器等。

  * 中小型网站建设、开发测试。

  * 经典轻量级应用。

* **计算**：

  * 支持4:1、2:1、1:1、1:2、1:4多种处理器内存配比

  * 处理器：Intel^®^Xeon^®^Platinum可扩展处理器

    **说明**

    e实例采用非绑定CPU调度模式，每个vCPU会被随机分配到任何空闲CPU超线程上。与企业级实例相比，e实例侧重于资源的共享，但是费用更低。
* **存储**：

  * I/O优化实例

  * 仅支持ESSD Entry云盘（推荐）、ESSD云盘、ESSD AutoPL云盘

    **说明**

    受经济型实例规格限制，PL1、PL2和PL3性能级别的ESSD云盘无法发挥极致性能，建议您选择ESSD Entry云盘或PL0性能级别的ESSD云盘。
* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 仅支持专有网络VPC

  * 实例网络性能与计算规格对应（规格越大网络性能越强）

e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.e-c4m1.large</p></td> <td><p>2</p></td> <td><p>0.5</p></td> <td><p>0.2/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.8万/无</p></td> <td><p>0.4/无</p></td> </tr> <tr> <td><p>ecs.e-c2m1.large</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.2/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.8万/无</p></td> <td><p>0.4/无</p></td> </tr> <tr> <td><p>ecs.e-c1m1.large</p></td> <td><p>2</p></td> <td><p>2.0</p></td> <td><p>0.2/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.8万/无</p></td> <td><p>0.4/无</p></td> </tr> <tr> <td><p>ecs.e-c1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>0.2/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.8万/无</p></td> <td><p>0.4/无</p></td> </tr> <tr> <td><p>ecs.e-c1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>0.4/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> <tr> <td><p>ecs.e-c1m2.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>0.4/最高3</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> <tr> <td><p>ecs.e-c1m4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>0.8/最高4</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> <tr> <td><p>ecs.e-c1m2.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>0.8/最高6</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> <tr> <td><p>ecs.e-c1m4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>1.2/最高6</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> </tbody> </table>  
**说明**

* 实例规格ecs.e-c4m1.large、ecs.e-c2m1.large、ecs.e-c1m1.large、ecs.e-c1m2.large、ecs.e-c1m4.large有以下限制：

  * 不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。

  * 绑定和解绑辅助弹性网卡时，实例必须处于已停止状态。

* 实例规格ecs.e-c4m1.large、ecs.e-c2m1.large仅支持在以下地域中购买：中国香港、新加坡、马来西亚（吉隆坡）、印度尼西亚（雅加达）、菲律宾（马尼拉）、泰国（曼谷）、日本（东京）、韩国（首尔）、英国（伦敦）、德国（法兰克福）、美国（弗吉尼亚）、美国（硅谷）。

## 共享标准型实例规格族s6
* **规格族介绍**：相比上一代共享型实例规格族（xn4、n4、mn4和e4），性价比提升。

* **适用场景**：

  * 中小型网站和Web应用程序。

  * 开发环境、构建服务器、代码存储库、微服务、测试和暂存环境等。

  * 轻量级数据库、缓存。

  * 轻量级企业应用、综合应用服务。

* **计算**：

  * 支持1:1、1:2、1:4多种处理器内存配比。

  * 处理器：2.5 GHz主频的Intel^®^ Xeon^®^ Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定。

  * 搭配DDR4内存。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    受共享型实例规格限制，PL1、PL2和PL3性能级别的ESSD云盘、SSD云盘无法发挥极致性能，建议您选择高效云盘或PL0性能级别的ESSD云盘。
* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 仅支持专有网络VPC。

s6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.s6-c1m1.small</p></td> <td><p>1</p></td> <td><p>1.0</p></td> <td><p>0.1</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m2.small</p></td> <td><p>1</p></td> <td><p>2.0</p></td> <td><p>0.1</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m4.small</p></td> <td><p>1</p></td> <td><p>4.0</p></td> <td><p>0.1</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>0.2</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>0.4</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m2.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>0.4</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>0.8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m2.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>0.8</p></td> <td><p>60</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>1.2</p></td> <td><p>60</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.s6-c1m1.small、ecs.s6-c1m2.large、ecs.s6-c1m2.small、ecs.s6-c1m4.large、ecs.s6-c1m4.small。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

## 上一代共享型实例规格族xn4、n4、mn4、e4
xn4、n4、mn4和e4的特点如下：

* 多种处理器和内存配比。

* 处理器：2.5 GHz主频的Intel^®^ Xeon^®^处理器。

* 搭配DDR4内存。

* I/O优化实例。

* 仅支持IPv4。

<table> <thead> <tr> <td><p><b>规格族</b></p></td> <td><p><b>特点</b></p></td> <td><p><b>vCPU : 内存</b></p></td> <td><p><b>适用场景</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>xn4</p></td> <td><p>共享基本型实例</p></td> <td><p>1:1</p></td> <td> <ul> <li><p>Web应用前端机</p></li> <li><p>轻负载应用、微服务</p></li> <li><p>开发测试压测服务应用</p></li> </ul></td> </tr> <tr> <td><p>n4</p></td> <td><p>共享计算型实例</p></td> <td><p>1:2</p></td> <td> <ul> <li><p>网站和Web应用程序</p></li> <li><p>开发环境、构建服务器、代码存储库、微服务、测试和暂存环境</p></li> <li><p>轻量级企业应用</p></li> </ul></td> </tr> <tr> <td><p>mn4</p></td> <td><p>共享通用型实例</p></td> <td><p>1:4</p></td> <td> <ul> <li><p>网站和Web应用程序</p></li> <li><p>轻量级数据库、缓存</p></li> <li><p>综合应用，轻量级企业服务</p></li> </ul></td> </tr> <tr> <td><p>e4</p></td> <td><p>共享内存型实例</p></td> <td><p>1:8</p></td> <td> <ul> <li><p>大内存应用</p></li> <li><p>轻量级数据库、缓存</p></li> </ul></td> </tr> </tbody> </table>  
共享基本型xn4包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.xn4.small</p></td> <td><p>1</p></td> <td><p>1.0</p></td> <td><p>0.5</p></td> <td><p>5</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，ecs.xn4.small实例规格的实例必须处于已停止状态。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

共享计算型n4包括的实例规格及指标数据如下表所示：。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.n4.small</p></td> <td><p>1</p></td> <td><p>2.0</p></td> <td><p>0.5</p></td> <td><p>5</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n4.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>0.5</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n4.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>0.8</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.n4.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>1.2</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.n4.4xlarge</p></td> <td><p>16</p></td> <td><p>32.0</p></td> <td><p>2.5</p></td> <td><p>40</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.n4.8xlarge</p></td> <td><p>32</p></td> <td><p>64.0</p></td> <td><p>5.0</p></td> <td><p>50</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.n4.small、ecs.n4.large。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

共享通用型mn4包括的实例规格及指标数据如下表所示：。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.mn4.small</p></td> <td><p>1</p></td> <td><p>4.0</p></td> <td><p>0.5</p></td> <td><p>5</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.mn4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>0.5</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.mn4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>0.8</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.mn4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>1.2</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.mn4.4xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>2.5</p></td> <td><p>40</p></td> <td><p>1</p></td> <td><p>8</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.mn4.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>5</p></td> <td><p>50</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>6</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.mn4.small、ecs.mn4.large。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

共享内存型e4包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.e4.small</p></td> <td><p>1</p></td> <td><p>8.0</p></td> <td><p>0.5</p></td> <td><p>5</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.e4.large</p></td> <td><p>2</p></td> <td><p>16.0</p></td> <td><p>0.5</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.e4.xlarge</p></td> <td><p>4</p></td> <td><p>32.0</p></td> <td><p>0.8</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.e4.2xlarge</p></td> <td><p>8</p></td> <td><p>64.0</p></td> <td><p>1.2</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.e4.4xlarge</p></td> <td><p>16</p></td> <td><p>128.0</p></td> <td><p>2.5</p></td> <td><p>40</p></td> <td><p>1</p></td> <td><p>8</p></td> <td><p>6</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.e4.small、ecs.e4.large。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

<br />
