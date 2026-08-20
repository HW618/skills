高主频型实例规格处理器与内存配比为1:2、1:4、1:8，适用于大型多人在线游戏、HPC等高性能科学计算场景，以及中大型数据库系统等。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

<table> <thead> <tr> <td><p><b>采用P-core（性能核）的英特尔</b><b><sup>®</sup></b><b> 至强</b><b><sup>®</sup></b><b> 6处理器</b></p></td> <td><p><b>第四代Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>可扩展处理器（Sapphire Rapids）</b></p></td> <td><p><b>Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>Cooper Lake处理器</b></p></td> <td><p><b>Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>Platinum 8269CY（Cascade Lake）</b></p></td> <td><p><b>不推荐（如果以下规格售罄，建议使用前面的规格）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#hfc9i">高主频计算实例规格族hfc9i</a></p></li> <li><p><a href="#hfg9i">高主频通用型实例规格族hfg9i</a></p></li> <li><p><a href="#hfr9i">高主频内存型实例规格族hfr9i</a></p></li> </ul></td> <td> <ul> <li><p><a href="#hfc8i">高主频计算型实例规格族hfc8i</a></p></li> <li><p><a href="#hfg8i">高主频通用型实例规格族hfg8i</a></p></li> <li><p><a href="#hfr8i">高主频内存型实例规格族hfr8i</a></p></li> </ul></td> <td> <ul> <li><p><a href="#section-hdo-beh-gsf">高主频计算型实例规格族hfc7</a></p></li> <li><p><a href="#section-ms1-d4s-fmi">高主频通用型实例规格族hfg7</a></p></li> <li><p><a href="#section-nzd-6dq-556">高主频内存型实例规格族hfr7</a></p></li> </ul><p></p></td> <td> <ul> <li><p><a href="#section-stc-a50-sco">高主频计算型实例规格族hfc6</a></p></li> <li><p><a href="#section-xgq-3wb-9ak">高主频通用型实例规格族hfg6</a></p></li> <li><p><a href="#section-205-hfc-ekc">高主频内存型实例规格族hfr6</a></p></li> </ul></td> <td> <ul> <li><p><a href="#section-kkg-4hf-rkf">高主频计算型实例规格族hfc5</a></p></li> <li><p><a href="#section-rjm-jmo-yll">高主频通用型实例规格族hfg5</a></p></li> </ul></td> </tr> </tbody> </table>

## 高主频计算实例规格族hfc9i
* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，数据分析、批量计算、视频编码，大型多人在线游戏（MMO）前端，高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.4 GHz，全核睿频3.8 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfc9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc9i.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2.5/15</p></td> <td><p>100万</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高20万</p></td> <td><p>2/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4/15</p></td> <td><p>120万</p></td> <td><p>50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>8/15</p></td> <td><p>160万</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>10/15</p></td> <td><p>240万</p></td> <td><p>50万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>16/25</p></td> <td><p>300万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>18/25</p></td> <td><p>450万</p></td> <td><p>50万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>20/32</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/最高25万</p></td> <td><p>12/15</p></td> </tr> <tr> <td><p>ecs.hfc9i.12xlarge</p></td> <td><p>48</p></td> <td><p>96</p></td> <td><p>25/32</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>25万/无</p></td> <td><p>15/无</p></td> </tr> <tr> <td><p>ecs.hfc9i.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>36/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>36万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.hfc9i.24xlarge</p></td> <td><p>96</p></td> <td><p>192</p></td> <td><p>48/无</p></td> <td><p>1600万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>40万/无</p></td> <td><p>24/无</p></td> </tr> <tr> <td><p>ecs.hfc9i.36xlarge</p></td> <td><p>144</p></td> <td><p>384</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

## 高主频通用型实例规格族hfg9i
* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，数据分析、批量计算、视频编码，大型多人在线游戏（MMO）前端，高性能科学和工程应用，中大型数据库。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.4 GHz，全核睿频3.8 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfg9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg9i.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>2.5/15</p></td> <td><p>100万</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高20万</p></td> <td><p>2/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>4/15</p></td> <td><p>120万</p></td> <td><p>50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>8/15</p></td> <td><p>160万</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>10/15</p></td> <td><p>240万</p></td> <td><p>50万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>16/25</p></td> <td><p>300万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>18/25</p></td> <td><p>450万</p></td> <td><p>50万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>20/32</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/最高25万</p></td> <td><p>12/15</p></td> </tr> <tr> <td><p>ecs.hfg9i.12xlarge</p></td> <td><p>48</p></td> <td><p>192</p></td> <td><p>25/32</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>25万/无</p></td> <td><p>15/无</p></td> </tr> <tr> <td><p>ecs.hfg9i.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>36/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>36万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.hfg9i.24xlarge</p></td> <td><p>96</p></td> <td><p>384</p></td> <td><p>48/无</p></td> <td><p>1600万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>40万/无</p></td> <td><p>24/无</p></td> </tr> <tr> <td><p>ecs.hfg9i.36xlarge</p></td> <td><p>144</p></td> <td><p>768</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

## 高主频内存型实例规格族hfr9i
* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，数据分析与挖掘，分布式内存缓存，高性能数据库、内存数据库，高性能科学和工程应用，Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.4 GHz，全核睿频3.8 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfr9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfr9i.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2.5/15</p></td> <td><p>100万</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高20万</p></td> <td><p>2/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>4/15</p></td> <td><p>120万</p></td> <td><p>50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>8/15</p></td> <td><p>160万</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>10/15</p></td> <td><p>240万</p></td> <td><p>50万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>16/25</p></td> <td><p>300万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>18/25</p></td> <td><p>450万</p></td> <td><p>50万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>20/32</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/最高25万</p></td> <td><p>12/15</p></td> </tr> <tr> <td><p>ecs.hfr9i.12xlarge</p></td> <td><p>48</p></td> <td><p>384</p></td> <td><p>25/32</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>25万/无</p></td> <td><p>15/无</p></td> </tr> <tr> <td><p>ecs.hfr9i.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>36/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>36万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.hfr9i.24xlarge</p></td> <td><p>96</p></td> <td><p>768</p></td> <td><p>48/无</p></td> <td><p>1600万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>40万/无</p></td> <td><p>24/无</p></td> </tr> <tr> <td><p>ecs.hfr9i.36xlarge</p></td> <td><p>144</p></td> <td><p>1536</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

## 高主频计算型实例规格族hfc8i
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能前端服务器集群。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用第四代Intel^®^ Xeon^®^ 可扩展处理器（Sapphire Rapids），基频3.3 GHz，全核睿频3.9 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfc8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc8i.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2.5/15</p></td> <td><p>120万</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>3万/最高20万</p></td> <td><p>3/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4/15</p></td> <td><p>140万</p></td> <td><p>30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>8/15</p></td> <td><p>180万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>10/15</p></td> <td><p>280万</p></td> <td><p>30万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>9万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>16/25</p></td> <td><p>360万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>10/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>18/25</p></td> <td><p>550万</p></td> <td><p>80万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.hfc8i.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>32/无</p></td> <td><p>750万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>25万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.hfc8i.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>64/无</p></td> <td><p>1500万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>45万/无</p></td> <td><p>32/无</p></td> </tr> <tr> <td><p>ecs.hfc8i.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>100/无</p></td> <td><p>3000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>90万/无</p></td> <td><p>64/无</p></td> </tr> </tbody> </table>

## 高主频通用型实例规格族hfg8i
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能前端服务器集群。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

  * 中型数据库系统。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用第四代Intel^®^ Xeon^®^ 可扩展处理器（Sapphire Rapids），基频3.3 GHz，全核睿频3.9 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfg8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>可挂载的云盘数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg8i.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>2.5/15</p></td> <td><p>120万</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>16</p></td> <td><p>3万/最高20万</p></td> <td><p>3/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>4/15</p></td> <td><p>140万</p></td> <td><p>30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>5万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>8/15</p></td> <td><p>180万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>6万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>10/15</p></td> <td><p>280万</p></td> <td><p>30万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>9万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>16/25</p></td> <td><p>360万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>12万/最高20万</p></td> <td><p>10/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>18/25</p></td> <td><p>550万</p></td> <td><p>80万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.hfg8i.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>750万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>25万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.hfg8i.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>64/无</p></td> <td><p>1500万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>45万/无</p></td> <td><p>32/无</p></td> </tr> <tr> <td><p>ecs.hfg8i.32xlarge</p></td> <td><p>128</p></td> <td><p>512</p></td> <td><p>100/无</p></td> <td><p>3000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>64</p></td> <td><p>90万/无</p></td> <td><p>64/无</p></td> </tr> </tbody> </table>

## 高主频内存型实例规格族hfr8i
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能科学和工程应用。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用第四代Intel^®^ Xeon^®^ 可扩展处理器（Sapphire Rapids），基频3.3 GHz，全核睿频3.9 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强） ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfr8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>可挂载的云盘数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfr8i.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2.5/15</p></td> <td><p>120万</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>16</p></td> <td><p>3万/最高20万</p></td> <td><p>3/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>4/15</p></td> <td><p>140万</p></td> <td><p>30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>5万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>8/15</p></td> <td><p>180万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>6万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>10/15</p></td> <td><p>280万</p></td> <td><p>30万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>9万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>16/25</p></td> <td><p>360万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>12万/最高20万</p></td> <td><p>10/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>18/25</p></td> <td><p>550万</p></td> <td><p>80万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.hfr8i.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>32/无</p></td> <td><p>750万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>25万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.hfr8i.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>64/无</p></td> <td><p>1500万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>45万/无</p></td> <td><p>32/无</p></td> </tr> <tr> <td><p>ecs.hfr8i.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>100/无</p></td> <td><p>3000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>64</p></td> <td><p>90万/无</p></td> <td><p>64/无</p></td> </tr> </tbody> </table>

## 高主频计算型实例规格族hfc7
* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能前端服务器集群。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2

  * 处理器：采用Intel^®^ Xeon^®^ Cooper Lake处理器，全核睿频3.8 GHz，主频不低于3.3 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfc7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc7.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1.2/10</p></td> <td><p>90万</p></td> <td><p>25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfc7.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>2/10</p></td> <td><p>100万</p></td> <td><p>25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfc7.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>3/10</p></td> <td><p>160万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfc7.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>4.5/10</p></td> <td><p>200万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfc7.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>6/10</p></td> <td><p>250万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfc7.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>8/10</p></td> <td><p>300万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>9万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfc7.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10/无</p></td> <td><p>400万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10.5万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfc7.12xlarge</p></td> <td><p>48</p></td> <td><p>96</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfc7.24xlarge</p></td> <td><p>96</p></td> <td><p>192</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

## 高主频通用型实例规格族hfg7
* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 高性能科学计算。

  * 视频编码应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Cooper Lake处理器，全核睿频3.8 GHz，主频不低于3.3 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfg7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg7.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1.2/10</p></td> <td><p>90万</p></td> <td><p>25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfg7.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>2/10</p></td> <td><p>100万</p></td> <td><p>25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfg7.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>3/10</p></td> <td><p>160万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfg7.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>4.5/10</p></td> <td><p>200万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfg7.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>6/10</p></td> <td><p>250万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfg7.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>8/10</p></td> <td><p>300万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>9万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfg7.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>10/无</p></td> <td><p>400万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10.5万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfg7.12xlarge</p></td> <td><p>48</p></td> <td><p>192</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfg7.24xlarge</p></td> <td><p>96</p></td> <td><p>384</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

## 高主频内存型实例规格族hfr7
* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等

  * 高性能数据库、内存数据库

  * 数据分析与挖掘、分布式内存缓存

  * Hadoop、Spark集群以及其他企业大内存需求应用

* **计算**：

  * 处理器与内存配比为1:8

  * 处理器：采用Intel^®^ Xeon^®^ Cooper Lake处理器，全核睿频3.8 GHz，主频不低于3.3 GHz，计算性能稳定

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

hfr7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfr7.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1.2/10</p></td> <td><p>90万</p></td> <td><p>25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfr7.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>2/10</p></td> <td><p>100万</p></td> <td><p>25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfr7.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>3/10</p></td> <td><p>160万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfr7.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>4.5/10</p></td> <td><p>200万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfr7.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>6/10</p></td> <td><p>250万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfr7.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>8/10</p></td> <td><p>300万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>9万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfr7.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>10/无</p></td> <td><p>400万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10.5万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfr7.12xlarge</p></td> <td><p>48</p></td> <td><p>384</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfr7.24xlarge</p></td> <td><p>96</p></td> <td><p>768</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

## 高主频计算型实例规格族hfc6
* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Platinum 8269CY（Cascade Lake），睿频3.5 GHz，计算性能稳定。

    **说明**

    本实例规格族处理器提供3.1 GHz主频。由于Intel ISS特性原因，您查看到的主频可能显示为更低的数字。阿里云正在紧急修复该显示问题。该显示问题不影响您购买规格的主频频率。  
    您可以分别运行以下命令，使用turbostat工具来观察CPU运行的主频：

    ```
    HELPCODEESCAPE-shell
    yum install kernel-tools
    ```

    ```
    HELPCODEESCAPE-shell
    turbostat
    ```

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfc6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc6.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1/3</p></td> <td><p>30万</p></td> <td><p>3.5万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfc6.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1.5/5</p></td> <td><p>50万</p></td> <td><p>7万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfc6.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2.5/8</p></td> <td><p>80万</p></td> <td><p>15万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfc6.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>4/10</p></td> <td><p>90万</p></td> <td><p>22万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfc6.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>5/10</p></td> <td><p>100万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfc6.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>7.5/10</p></td> <td><p>150万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfc6.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10/无</p></td> <td><p>200万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfc6.10xlarge</p></td> <td><p>40</p></td> <td><p>96</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfc6.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>20/无</p></td> <td><p>400万</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>12万</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfc6.20xlarge</p></td> <td><p>80</p></td> <td><p>192</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

## 高主频通用型实例规格族hfg6
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

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Platinum 8269CY（Cascade Lake），睿频3.5 GHz，计算性能稳定。

    **说明**

    本实例规格族处理器提供3.1 GHz主频。由于Intel ISS特性原因，您查看到的主频可能显示为更低的数字。阿里云正在紧急修复该显示问题。该显示问题不影响您购买规格的主频频率。  
    您可以分别运行以下命令，使用turbostat工具来观察CPU运行的主频：

    ```
    HELPCODEESCAPE-shell
    yum install kernel-tools
    ```

    ```
    HELPCODEESCAPE-shell
    turbostat
    ```

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfg6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg6.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1/3</p></td> <td><p>30万</p></td> <td><p>3.5万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfg6.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>1.5/5</p></td> <td><p>50万</p></td> <td><p>7万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfg6.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>2.5/8</p></td> <td><p>80万</p></td> <td><p>15万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfg6.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>4/10</p></td> <td><p>90万</p></td> <td><p>22万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfg6.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>5/10</p></td> <td><p>100万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfg6.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>7.5/10</p></td> <td><p>150万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfg6.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>10/无</p></td> <td><p>200万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfg6.10xlarge</p></td> <td><p>40</p></td> <td><p>192</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfg6.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>20/无</p></td> <td><p>400万</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>12万</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfg6.20xlarge</p></td> <td><p>80</p></td> <td><p>384</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

## 高主频内存型实例规格族hfr6
* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Platinum 8269CY（Cascade Lake），睿频3.5 GHz，计算性能稳定。

    **说明**

    本实例规格族处理器提供3.1 GHz主频。由于Intel ISS特性原因，您查看到的主频可能显示为更低的数字。阿里云正在紧急修复该显示问题。该显示问题不影响您购买规格的主频频率。  
    您可以分别运行以下命令，使用turbostat工具来观察CPU运行的主频：

    ```
    HELPCODEESCAPE-shell
    yum install kernel-tools
    ```

    ```
    HELPCODEESCAPE-shell
    turbostat
    ```

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfr6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfr6.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1/3</p></td> <td><p>30万</p></td> <td><p>3.5万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfr6.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>1.5/5</p></td> <td><p>50万</p></td> <td><p>7万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfr6.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>2.5/8</p></td> <td><p>80万</p></td> <td><p>15万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfr6.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>4/10</p></td> <td><p>90万</p></td> <td><p>22万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfr6.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>5/10</p></td> <td><p>100万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfr6.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>7.5/10</p></td> <td><p>150万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfr6.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>10/无</p></td> <td><p>200万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfr6.10xlarge</p></td> <td><p>40</p></td> <td><p>384</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfr6.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>20/无</p></td> <td><p>400万</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>12万</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfr6.20xlarge</p></td> <td><p>80</p></td> <td><p>768</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

## 高主频计算型实例规格族hfc5
* **适用场景**：高性能Web前端服务器；高性能科学和工程应用；MMO游戏、视频编码。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Gold 6149（Skylake）或者8269CY（Cascade Lake），计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 仅支持IPv4。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfc5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc5.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.hfc5.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfc5.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfc5.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>2.5</p></td> <td><p>130万</p></td> <td><p>4</p></td> <td><p>6</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfc5.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>3</p></td> <td><p>160万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfc5.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>4.5</p></td> <td><p>200万</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfc5.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>6</p></td> <td><p>250万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> </tbody> </table>

## 高主频通用型实例规格族hfg5
* **适用场景**：高性能Web前端服务器；高性能科学和工程应用；MMO游戏、视频编码。

* **计算**：

  * 处理器与内存配比为1:4（56 vCPU规格除外）。

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Gold 6149（Skylake）或者8269CY（Cascade Lake），计算性能稳定

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 仅支持IPv4。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfg5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg5.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.hfg5.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfg5.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>2</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfg5.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>2.5</p></td> <td><p>130万</p></td> <td><p>4</p></td> <td><p>6</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfg5.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>3</p></td> <td><p>160万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfg5.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>4.5</p></td> <td><p>200万</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfg5.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>6</p></td> <td><p>250万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfg5.14xlarge</p></td> <td><p>56</p></td> <td><p>160</p></td> <td><p>10</p></td> <td><p>400万</p></td> <td><p>14</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> </tbody> </table>
