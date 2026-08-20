通用型实例规格族（g系列）处理器与内存配比为1:4，适用于通用互联网应用、数据库、Web网站、Java应用服务、游戏服务、搜索推广等场景。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

<table> <thead> <tr> <td> <p><b>X86</b></p> </td> <td> <p><b>ARM</b></p> </td> <td> <p><b>不推荐（如果以下规格售罄，建议使用前面的规格）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>Intel处理器</b></p> </td> <td> <p><b>AMD处理器</b></p> </td> <td> <p><b>海光</b></p> </td> <td> <p><b>倚天及其他</b></p> </td> </tr> <tr> <td> <ul> <li> <p><a href="#g9i">通用型实例规格族g9i</a></p> </li> <li> <p><a href="#g8i">通用型实例规格族g8i</a></p> </li> <li> <p><a href="#g8ine">网络增强通用型实例规格族g8ine</a></p> </li> <li> <p><a href="#g7">通用型实例规格族g7</a></p> </li> <li> <p><a href="#section-8u6-czr-21b">通用平衡增强型实例规格族g6e</a></p> </li> <li> <p><a href="#section-gck-bi6-q6l">通用型实例规格族g6</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#g9a">通用型实例规格族g9a</a></p> </li> <li> <p><a href="#g9ae">通用型实例规格族g9ae</a></p> </li> <li> <p><a href="#g8a">通用型实例规格族g8a</a></p> </li> <li> <p><a href="#g8ae">通用平衡增强型实例规格族g8ae</a></p> </li> <li> <p><a href="#g7a">通用型实例规格族g7a</a></p> </li> <li> <p><a href="#g6a">通用型实例规格族g6a</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#g9h">海光通用型实例规格族g9h</a></p> </li> <li> <p><a href="#g7h">海光通用型实例规格族g7h</a></p> </li> <li> <p><a href="#g6h">海光通用型实例规格族g6h</a></p> </li> </ul> </td> <td> <blockquote> 倚天710处理器 </blockquote> <ul> <li> <p><a href="#g8y">通用型实例规格族g8y</a></p> </li> </ul> <p></p> <p></p> <blockquote> Ampere <sup>®</sup>Altra <sup>®</sup> </blockquote> <ul> <li> <p><a href="#g6r">通用型实例规格族g6r</a></p> </li> </ul> <p></p> <p></p> </td> <td> <ul> <li> <p><a href="#section-kwi-d9k-sbx">通用型实例规格族g5</a></p> </li> <li> <p><a href="#section-1ki-kxs-w47">通用网络增强型实例规格族sn2ne</a></p> </li> </ul> </td> </tr> </tbody> </table>

## **通用型实例规格族g**9ae
* **规格族介绍** ：采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC^™^ Turin 处理器，采用物理核设计，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：大数据分析（Spark/Flink/ES等），搜索/推荐/广告（ps-worker），核心交易系统，音视频转码，AI训练与推理，通用的企业级应用（Java）等。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高3.7 GHz，采用物理核设计，计算性能稳定。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#6cc7ed4977cxh)。

* **存储**：

  * 支持调整存储基础带宽。

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持调整网络基础带宽。

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持[可信计算（vTPM）特性](https://help.aliyun.com/document_detail/201394.html)。

  * 支持[VPC流量加密](https://help.aliyun.com/document_detail/2932958.html)。

g9ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g9ae.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2.5/最高25</p> </td> <td> <p>最高150万</p> </td> <td> <p>最高50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高20万</p> </td> <td> <p>2.5/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高25</p> </td> <td> <p>最高160万</p> </td> <td> <p>最高50万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高20万</p> </td> <td> <p>3/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高25</p> </td> <td> <p>最高250万</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高20万</p> </td> <td> <p>4/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>10/最高25</p> </td> <td> <p>最高320万</p> </td> <td> <p>最高50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高20万</p> </td> <td> <p>5.5/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/最高25</p> </td> <td> <p>最高500万</p> </td> <td> <p>最高100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高20万</p> </td> <td> <p>8/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>25/无</p> </td> <td> <p>750万</p> </td> <td> <p>150万</p> </td> <td> <p>48</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>15万</p> </td> <td> <p>13/无</p> </td> </tr> <tr> <td> <p>ecs.g9ae.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>1000万</p> </td> <td> <p>200万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g9ae.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>50/无</p> </td> <td> <p>1500万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>30万</p> </td> <td> <p>25/无</p> </td> </tr> <tr> <td> <p>ecs.g9ae.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>400万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>40万</p> </td> <td> <p>32/无</p> </td> </tr> <tr> <td> <p>ecs.g9ae.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>600万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>60万</p> </td> <td> <p>50/无</p> </td> </tr> </tbody> </table>

## 通用型实例规格族g9a
* **规格族介绍** ：采用阿里云全新CIPU架构，搭配AMD最新EPYC^™^ Turin 处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：大中型数据库系统，游戏服务器，金融量化，区块链，网站和应用服务器以及其他通用企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高4.1 GHz，计算性能稳定。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#6cc7ed4977cxh)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持[可信计算（vTPM）特性](https://help.aliyun.com/document_detail/201394.html)。

g9a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g9a.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2.5/最高15</p> </td> <td> <p>最高120万</p> </td> <td> <p>最高50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高11万</p> </td> <td> <p>2/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高15</p> </td> <td> <p>最高140万</p> </td> <td> <p>最高50万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>3/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高15</p> </td> <td> <p>最高200万</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>4/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>12/最高25</p> </td> <td> <p>最高300万</p> </td> <td> <p>最高50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>5/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/最高32</p> </td> <td> <p>最高400万</p> </td> <td> <p>最高80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>8/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>750万</p> </td> <td> <p>150万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>12万</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g9a.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>48/无</p> </td> <td> <p>1000万</p> </td> <td> <p>220万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万</p> </td> <td> <p>24/无</p> </td> </tr> <tr> <td> <p>ecs.g9a.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>1500万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>25万</p> </td> <td> <p>32/无</p> </td> </tr> <tr> <td> <p>ecs.g9a.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>96/无</p> </td> <td> <p>2000万</p> </td> <td> <p>450万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>40万</p> </td> <td> <p>48/无</p> </td> </tr> </tbody> </table>

## 通用型实例规格族g9i
* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，游戏服务器，中小型数据库系统、缓存、搜索集群，搜索推广类应用，网站和应用服务器，数据分析和计算，安全可信计算场景。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，单核最大睿频3.9GHz。

    **说明**

    该实例在系统中可能会存在不同的频率显示，其中单核最高睿频3.9 GHz，属于突发性能，突发能力与物理机CPU整机负载相关，无法作为SLA承诺。
  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

g9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g9i.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2.5/最高15</p> </td> <td> <p>100万</p> </td> <td> <p>最高50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2.5万/最高20万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高15</p> </td> <td> <p>120万</p> </td> <td> <p>最高50万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>2.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高15</p> </td> <td> <p>160万</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>10/最高15</p> </td> <td> <p>240万</p> </td> <td> <p>最高50万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>15/最高25</p> </td> <td> <p>450万</p> </td> <td> <p>60万</p> </td> <td> <p>24</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>12万/最高20万</p> </td> <td> <p>7.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>20/最高32</p> </td> <td> <p>600万</p> </td> <td> <p>80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万/最高30万</p> </td> <td> <p>10/最高12</p> </td> </tr> <tr> <td> <p>ecs.g9i.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>25/最高32</p> </td> <td> <p>900万</p> </td> <td> <p>160万</p> </td> <td> <p>48</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>24万/最高32万</p> </td> <td> <p>12/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9i.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>28/最高36</p> </td> <td> <p>1200万</p> </td> <td> <p>200万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>30万/最高40万</p> </td> <td> <p>16/最高24</p> </td> </tr> <tr> <td> <p>ecs.g9i.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>32/最高48</p> </td> <td> <p>1800万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>35万/最高60万</p> </td> <td> <p>20/最高28</p> </td> </tr> <tr> <td> <p>ecs.g9i.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>36/最高50</p> </td> <td> <p>2000万</p> </td> <td> <p>400万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>40万/最高65万</p> </td> <td> <p>24/最高28</p> </td> </tr> <tr> <td> <p>ecs.g9i.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>600万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>50万/最高80万</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 通用型实例规格族g8a
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**： 通用的企业级应用（Java），内存型或者关系型数据库类应用，大数据类应用（Kafka、ElasticSearch等），Web类应用，AI训练与推理，音视频转码类应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：AMD EPYC^™^ Genoa 9T24处理器，基频2.7 GHz，睿频最高3.7 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
g8a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8a.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.5/12.5</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/11万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2.5/12.5</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>3万/11万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>4/12.5</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4.5万/11万</p> </td> <td> <p>2.5/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>7/12.5</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>6万/11万</p> </td> <td> <p>3.5/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/11万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>16/25</p> </td> <td> <p>450万</p> </td> <td> <p>75万</p> </td> <td> <p>48</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>12万/无</p> </td> <td> <p>8/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>20/25</p> </td> <td> <p>600万</p> </td> <td> <p>100万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/无</p> </td> <td> <p>10/无</p> </td> </tr> <tr> <td> <p>ecs.g8a.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>32/无</p> </td> <td> <p>900万</p> </td> <td> <p>150万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>24万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g8a.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>40/无</p> </td> <td> <p>1200万</p> </td> <td> <p>200万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32万/无</p> </td> <td> <p>20/无</p> </td> </tr> <tr> <td> <p>ecs.g8a.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>64/无</p> </td> <td> <p>1800万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>  
**说明**

* 由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

* ecs.g8a.large、ecs.g8a.xlarge需开启巨型帧（Jumbo frames），才能达到12.5 Gbit/s网络突发带宽。更多详情，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

## 通用平衡增强型实例规格族g8ae
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：人工智能场景（如深度学习与训练、AI推理等），HPC等高性能科学计算场景，大中型数据库系统、缓存、搜索集群，大型在线游戏服务器，其他对性能要求较高的通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：3.4 GHz主频的AMD EPYC™ Genoa处理器，单核睿频最高3.75 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

g8ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>支持vTPM</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8ae.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>3/最高15</p> </td> <td> <p>100万</p> </td> <td> <p>是</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>3万/最高20万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ae.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高15</p> </td> <td> <p>120万</p> </td> <td> <p>是</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>2.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ae.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高15</p> </td> <td> <p>160万</p> </td> <td> <p>是</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ae.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>是</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ae.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>20/最高25</p> </td> <td> <p>600万</p> </td> <td> <p>是</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万/无</p> </td> <td> <p>10/无</p> </td> </tr> <tr> <td> <p>ecs.g8ae.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>900万</p> </td> <td> <p>是</p> </td> <td> <p>150万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>25万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g8ae.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>1800万</p> </td> <td> <p>是</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>  
**说明**

ecs.g8ae.large、ecs.g8ae.xlarge需开启巨型帧，才能达到15 Gbit/s的突发带宽。更多详情，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

## 通用型实例规格族g8i
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，游戏服务器，中小型数据库系统、缓存、搜索集群，搜索推广类应用，网站和应用服务器，数据分析和计算，安全可信计算场景。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

    **说明**

    购买该实例时，系统将随机分配上述两种处理器之一，不支持手动选择。
  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持可信计算（vTPM）特性。更多信息，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

  * 4 vCPU以上规格的实例支持阿里云虚拟化Enclave特性，提供基于虚拟化的机密计算环境。更多信息，请参见[构建Enclave机密计算环境](https://help.aliyun.com/document_detail/203433.html#task-2038130)。

  * 采用英特尔TME（Total Memory Encryption）运行内存加密。

  * 支持CPU机密计算（Intel^®^ TDX），更多信息，[构建TDX机密计算环境](https://help.aliyun.com/document_detail/479090.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
g8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8i.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2.5/最高15</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2.5万/最高20万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高15</p> </td> <td> <p>120万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>2.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高15</p> </td> <td> <p>160万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>10/最高15</p> </td> <td> <p>240万</p> </td> <td> <p>最高30万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>35万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>15/最高25</p> </td> <td> <p>450万</p> </td> <td> <p>50万</p> </td> <td> <p>24</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>12万/最高20万</p> </td> <td> <p>7.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>20/最高25</p> </td> <td> <p>600万</p> </td> <td> <p>80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万/无</p> </td> <td> <p>10/无</p> </td> </tr> <tr> <td> <p>ecs.g8i.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>25/无</p> </td> <td> <p>900万</p> </td> <td> <p>100万</p> </td> <td> <p>48</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>30万/无</p> </td> <td> <p>12/无</p> </td> </tr> <tr> <td> <p>ecs.g8i.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>160万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>36万/无</p> </td> <td> <p>20/无</p> </td> </tr> <tr> <td> <p>ecs.g8i.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>50/无</p> </td> <td> <p>1800万</p> </td> <td> <p>200万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>24/无</p> </td> </tr> <tr> <td> <p>ecs.g8i.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1024</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>400万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>100万/无</p> </td> <td> <p>48/无</p> </td> </tr> </tbody> </table>

## 网络增强通用型实例规格族g8ine
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**： 适用于网络密集型场景，转发、连接性能出色，尤其适用于做网络接入层网关，流量、数据转发或预处理中间件等。作为云上解决方案中的一部分，在大型网站、电商、AI等场景下都可应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多信息，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

g8ine包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>EBS多队列</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8ine.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>4/最高24</p> </td> <td> <p>60万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>2万/最高8万</p> </td> <td> <p>2/最高8</p> </td> </tr> <tr> <td> <p>ecs.g8ine.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>7/最高28</p> </td> <td> <p>120万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>4万/最高8万</p> </td> <td> <p>2.5/最高8</p> </td> </tr> <tr> <td> <p>ecs.g8ine.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>12/最高35</p> </td> <td> <p>200万</p> </td> <td> <p>8</p> </td> <td> <p>6</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>2</p> </td> <td> <p>5万/最高8万</p> </td> <td> <p>4/最高8</p> </td> </tr> <tr> <td> <p>ecs.g8ine.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>23/最高44</p> </td> <td> <p>350万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>2</p> </td> <td> <p>8万/最高10万</p> </td> <td> <p>6/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ine.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>44/无</p> </td> <td> <p>700万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>4</p> </td> <td> <p>10万/无</p> </td> <td> <p>10/无</p> </td> </tr> </tbody> </table>

## 通用型实例规格族g8y
* **规格族介绍**：采用阿里云自研倚天710 ARM架构CPU，依托第四代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：容器、微服务，网站和应用服务器，视频编解码，高性能计算，基于CPU的机器学习。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.75 GHz主频的倚天710处理器，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
g8y包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>最大挂载数据盘数量</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8y.small</p> </td> <td> <p>1</p> </td> <td> <p>4</p> </td> <td> <p>1/10</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>1</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>3</p> </td> <td> <p>5</p> </td> <td> <p>1万/最高11万</p> </td> <td> <p>1/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2/10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>2万/最高11万</p> </td> <td> <p>1.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>3/10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>8</p> </td> <td> <p>4万/最高11万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>5/10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>16</p> </td> <td> <p>5万/最高11万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>40万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>8万/最高11万</p> </td> <td> <p>5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/25</p> </td> <td> <p>500万</p> </td> <td> <p>75万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>12.5万</p> </td> <td> <p>10</p> </td> </tr> <tr> <td> <p>ecs.g8y.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>1000万</p> </td> <td> <p>150万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32</p> </td> <td> <p>25万</p> </td> <td> <p>16</p> </td> </tr> <tr> <td> <p>ecs.g8y.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32</p> </td> <td> <p>50万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

如需使用ecs.g8y.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

## 通用型实例规格族g7a
* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：视频编解码，高网络包收发场景，网站和应用服务器，中小型数据库系统、缓存、搜索集群，游戏服务器，测试开发（例如DevOps），其他通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.55 GHz主频的AMD EPYC^™^ MILAN处理器，单核睿频最高3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g7a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g7a.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1/最高10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>1.25万/最高11万</p> </td> <td> <p>1/最高6</p> </td> </tr> <tr> <td> <p>ecs.g7a.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5/最高10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>2万/最高11万</p> </td> <td> <p>1.5/最高6</p> </td> </tr> <tr> <td> <p>ecs.g7a.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5/最高10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>3万/最高11万</p> </td> <td> <p>2/最高6</p> </td> </tr> <tr> <td> <p>ecs.g7a.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>7/最高12.5</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>6万/最高11万</p> </td> <td> <p>3.7/最高10.5</p> </td> </tr> <tr> <td> <p>ecs.g7a.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/最高10</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>7.5万/最高11万</p> </td> <td> <p>4.1/最高11</p> </td> </tr> <tr> <td> <p>ecs.g7a.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>600万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>15万/无</p> </td> <td> <p>8.2/无</p> </td> </tr> <tr> <td> <p>ecs.g7a-nps1.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>600万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>15万/无</p> </td> <td> <p>8.2/无</p> </td> </tr> <tr> <td> <p>ecs.g7a.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>200万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>30万/无</p> </td> <td> <p>16.4/无</p> </td> </tr> </tbody> </table>  
**说明**

Ubuntu 16或Debian 9操作系统内核不支持AMD EPYC^™^ MILAN处理器，因此当您选用该类实例规格后，请勿搭配Ubuntu 16或Debian 9镜像创建实例，否则实例会启动失败。

## 通用型实例规格族g7
* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**： 高网络包收发场景（例如视频弹幕、电信业务转发等），游戏服务器，中小型数据库系统、缓存、搜索集群，各种类型和规模的企业级应用，网站和应用服务器，数据分析和计算，安全可信计算场景，区块链场景。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

    **说明**

    该规格族的实例可能运行在不同的服务器平台，包括Ice Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Ice Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

  * 支持阿里云虚拟化Enclave特性，提供基于虚拟化的机密计算环境。更多信息，请参见[构建Enclave机密计算环境](https://help.aliyun.com/document_detail/203433.html#task-2038130)。

g7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>支持vTPM</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>最大挂载数据盘数量</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g7.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2/最高12.5</p> </td> <td> <p>110万</p> </td> <td> <p>是</p> </td> <td> <p>最高50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>2万/最高16万</p> </td> <td> <p>1.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>3/最高12.5</p> </td> <td> <p>110万</p> </td> <td> <p>是</p> </td> <td> <p>最高50万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>8</p> </td> <td> <p>4万/最高16万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>5/最高15</p> </td> <td> <p>160万</p> </td> <td> <p>是</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>16</p> </td> <td> <p>5万/最高16万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>8/最高15</p> </td> <td> <p>240万</p> </td> <td> <p>是</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>16</p> </td> <td> <p>7万/最高16万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>10/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>是</p> </td> <td> <p>50万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>8万/最高16万</p> </td> <td> <p>5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>12/最高25</p> </td> <td> <p>450万</p> </td> <td> <p>是</p> </td> <td> <p>55万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>11万/最高16万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.g7.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/最高32</p> </td> <td> <p>600万</p> </td> <td> <p>是</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>24</p> </td> <td> <p>16万/无</p> </td> <td> <p>10/无</p> </td> </tr> <tr> <td> <p>ecs.g7.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>是</p> </td> <td> <p>120万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32</p> </td> <td> <p>36万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g7.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>是</p> </td> <td> <p>240万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32</p> </td> <td> <p>60万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 海光通用型实例规格族g9h
* **规格族介绍**：采用阿里云CIPU架构，搭配海光4号C86-4G平台处理器，可提供稳定的国产化算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：数据库，网络Web类应用，大数据分析（Spark/Flink/ES等），搜索/推荐/广告（ps-worker），核心交易系统，音视频转码，AI训练与推理，通用的企业级应用（Java）等。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用海光4代可扩展处理器Hygon C86-4G，睿频最高3.1 GHz，国产化算力，安全可靠，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

g9h包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4/IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g9h.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.5/12.5</p> </td> <td> <p>90万</p> </td> <td> <p>25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>2万/11万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.g9h.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2.5/12.5</p> </td> <td> <p>100万</p> </td> <td> <p>25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>3万/11万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.g9h.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>4/12.5</p> </td> <td> <p>160万</p> </td> <td> <p>25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>4.5万/11万</p> </td> <td> <p>2.5/10</p> </td> </tr> <tr> <td> <p>ecs.g9h.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>7/12.5</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>6万/11万</p> </td> <td> <p>3.5/10</p> </td> </tr> <tr> <td> <p>ecs.g9h.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>8万/11万</p> </td> <td> <p>5/10</p> </td> </tr> </tbody> </table>

## 海光通用型实例规格族g7h
* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：视频编解码，高网络包收发场景，网站和应用服务器，中小型数据库系统、缓存、搜索集群，测试开发（例如DevOps），其他通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用海光3代可扩展处理器Hygon C86-3G 7390，睿频最高3.0 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ： 支持安全加密虚拟化（China Secure Virtualization，简称CSV），关于CSV的更多信息，请参见[构建CSV机密计算环境](https://help.aliyun.com/document_detail/2507879.html)。

g7h包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS（万）</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>可挂载的云盘数</b></p> </td> <td> <p><b>云盘 IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g7h.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.5/10</p> </td> <td> <p>50</p> </td> <td> <p>25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>16</p> </td> <td> <p>2万/最高10万</p> </td> <td> <p>1/4</p> </td> </tr> <tr> <td> <p>ecs.g7h.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2.5/10</p> </td> <td> <p>90</p> </td> <td> <p>25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>10</p> </td> <td> <p>16</p> </td> <td> <p>3万/最高10万</p> </td> <td> <p>1.5/4</p> </td> </tr> <tr> <td> <p>ecs.g7h.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>3/10</p> </td> <td> <p>120</p> </td> <td> <p>25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>10</p> </td> <td> <p>16</p> </td> <td> <p>4万/最高10万</p> </td> <td> <p>2/4</p> </td> </tr> <tr> <td> <p>ecs.g7h.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>4/10</p> </td> <td> <p>150</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>6万/最高10万</p> </td> <td> <p>3/4</p> </td> </tr> <tr> <td> <p>ecs.g7h.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/无</p> </td> <td> <p>200</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>10万/无</p> </td> <td> <p>4/无</p> </td> </tr> <tr> <td> <p>ecs.g7h.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>400</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>18万/无</p> </td> <td> <p>8/无</p> </td> </tr> </tbody> </table>

## 海光通用型实例规格族g6h
g6h仅支持在金融云中购买。关于如何申请金融云认证，请参见[申请金融云认证](https://help.aliyun.com/document_detail/29856.html)。  
* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：视频编解码，高网络包收发场景，网站和应用服务器，中小型数据库系统、缓存、搜索集群，测试开发（例如DevOps），其他通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用海光2代可扩展处理器7280，基频2.0 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6h包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6h.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.2/5</p> </td> <td> <p>50万</p> </td> <td> <p>25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>1.5万/最高7.5万</p> </td> <td> <p>1/4</p> </td> </tr> <tr> <td> <p>ecs.g6h.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2/8</p> </td> <td> <p>75万</p> </td> <td> <p>25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>2万/最高7.5万</p> </td> <td> <p>1.5/4</p> </td> </tr> <tr> <td> <p>ecs.g6h.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>3/8</p> </td> <td> <p>90万</p> </td> <td> <p>25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>3万/最高7.5万</p> </td> <td> <p>2/4</p> </td> </tr> <tr> <td> <p>ecs.g6h.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>4/8</p> </td> <td> <p>120万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>5万/最高7.5万</p> </td> <td> <p>3/4</p> </td> </tr> <tr> <td> <p>ecs.g6h.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/无</p> </td> <td> <p>200万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>7.5万/无</p> </td> <td> <p>4/无</p> </td> </tr> <tr> <td> <p>ecs.g6h.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>12/无</p> </td> <td> <p>400万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>15万/无</p> </td> <td> <p>8/无</p> </td> </tr> </tbody> </table>

## 通用型实例规格族g6r
* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**： 容器、微服务，测试开发（例如DevOps），网站和应用服务器，游戏服务器，基于CPU的机器学习推理。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.8 GHz主频的Ampere^®^ Altra^®^处理器，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6r包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6r.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1/10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>1.25万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g6r.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5/10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.g6r.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5/10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>3万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.g6r.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5/10</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>6万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.g6r.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/10</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>7.5万</p> </td> <td> <p>4</p> </td> </tr> <tr> <td> <p>ecs.g6r.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>600万</p> </td> <td> <p>90万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>15万</p> </td> <td> <p>8</p> </td> </tr> </tbody> </table>

## 通用型实例规格族g6a
* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 视频编解码。

  * 高网络包收发场景。

  * 网站和应用服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 游戏服务器。

  * 测试开发，例如DevOps。

  * 其他通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.6 GHz主频的AMD EPYC^™^ ROME处理器，睿频3.3 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6a.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1/10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>1.25万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g6a.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5/10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>3</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.g6a.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5/10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>3万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.g6a.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5/10</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>6万</p> </td> <td> <p>3.1</p> </td> </tr> <tr> <td> <p>ecs.g6a.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/10</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>7.5万</p> </td> <td> <p>4.1</p> </td> </tr> <tr> <td> <p>ecs.g6a.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>600万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>15万</p> </td> <td> <p>8.2</p> </td> </tr> <tr> <td> <p>ecs.g6a.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>200万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>16.4</p> </td> </tr> </tbody> </table>

## 通用平衡增强型实例规格族g6e
* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比约为1:4。

  * 处理器：2.5 GHz主频、3.2 GHz睿频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  **说明**

  该规格族不支持FreeBSD 13.2及更早版本，存在兼容性问题，请使用FreeBSD 13.3或更高版本。

  该规格族的实例可能运行在不同的服务器平台，包括 Cascade Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Cascade Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

    **说明**

    不同实例规格族提供的网络性能不同，如果需要更高的并发连接能力和网络收发包能力，建议您选用g7ne。
  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6e.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.2/最高10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>2万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g6e.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2/最高10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>4万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.g6e.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>3/最高10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.g6e.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>6/最高10</p> </td> <td> <p>300万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>8万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.g6e.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10/无</p> </td> <td> <p>600万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>15万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.g6e.13xlarge</p> </td> <td> <p>52</p> </td> <td> <p>192</p> </td> <td> <p>16/无</p> </td> <td> <p>900万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>24万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.g6e.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>384</p> </td> <td> <p>32/无</p> </td> <td> <p>2400万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>48万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>  
**说明**

* 网络能力为单项测试最高能力。例如，单项测试网络带宽能力时，不会对网络收发包能力和其他指标同时做压力测试。

* 如需使用ecs.g6e.26xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

## 通用型实例规格族g6
* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  **说明**

  该规格族不支持FreeBSD 13.2及更早版本，存在兼容性问题，请使用FreeBSD 13.3或更高版本。

  该规格族的实例可能运行在不同的服务器平台，包括 Cascade Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Cascade Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    不同实例规格族的云盘性能上限不同，本规格族的单台实例最高支持20万IOPS。
  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

    **说明**

    不同实例规格族提供的网络性能不同，如果需要更高的并发连接能力和网络收发包能力，建议您选用g7ne。
  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1/最高3</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g6.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5/最高5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.g6.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5/最高8</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.g6.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>4/最高10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.g6.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5/最高10</p> </td> <td> <p>100万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.g6.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>7.5/最高10</p> </td> <td> <p>150万</p> </td> <td> <p>45万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>5万</p> </td> <td> <p>4</p> </td> </tr> <tr> <td> <p>ecs.g6.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10/无</p> </td> <td> <p>200万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.g6.13xlarge</p> </td> <td> <p>52</p> </td> <td> <p>192</p> </td> <td> <p>12.5/无</p> </td> <td> <p>300万</p> </td> <td> <p>90万</p> </td> <td> <p>32</p> </td> <td> <p>7</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>10万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.g6.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>384</p> </td> <td> <p>25/无</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 通用型实例规格族g5
* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）或者8269CY（Cascade Lake），计算性能稳定。

    **说明**

    该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要将实例部署在同一服务器平台，建议您选用g9i。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    不同实例规格族的云盘性能上限不同，本规格族的单台实例最高支持20万IOPS。
* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

    **说明**

    不同实例规格族提供的网络性能不同，如果需要更高的并发连接能力和网络收发包能力，建议您选用g7ne。
  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g5.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>7.5</p> </td> <td> <p>150万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>20</p> </td> <td> <p>400万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## 通用网络增强型实例规格族sn2ne
* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）或Platinum 8163（Skylake）或8269CY（Cascade Lake），计算性能稳定。

    **说明**

    该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要部署在同一服务器平台，建议您选用g9i。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

sn2ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sn2ne.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2</p> </td> <td> <p>100万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>2.5</p> </td> <td> <p>130万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>3</p> </td> <td> <p>160万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>4.5</p> </td> <td> <p>200万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>6</p> </td> <td> <p>250万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.14xlarge</p> </td> <td> <p>56</p> </td> <td> <p>224</p> </td> <td> <p>10</p> </td> <td> <p>450万</p> </td> <td> <p>14</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>
