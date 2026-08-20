本地SSD型实例规格（i系列）处理器与内存配比为1:4、1:8，适用于OLTP、高性能关系型数据库、NoSQL数据库（例如Cassandra、MongoDB等）、Elasticsearch等搜索场景以及EMR大数据存算分离场景。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

<table> <thead> <tr> <td> <p><b>Intel</b><b><sup>®</sup></b><b>\&nbsp;Xeon</b><b><sup>®</sup></b><b>\&nbsp;Granite Rapids处理器</b></p> </td> <td> <p><b>Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>可扩展处理器（Ice Lake）</b></p> </td> <td> <p><b>Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>Platinum 8269CY（Cascade Lake）处理器</b></p> </td> <td> <p><b>Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>Platinum 8163（Skylake）处理器</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li> <p><a href="#i5g">本地SSD型实例规格族i5g</a></p> </li> <li> <p><a href="#i5ge">本地SSD型实例规格族i5ge</a></p> </li> <li> <p><a href="#i5e">本地SSD型实例规格族i5e</a></p> </li> <li> <p><a href="#i5">本地SSD型实例规格族i5</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#i4">本地SSD型实例规格族i4</a></p> </li> <li> <p><a href="#i4g">本地SSD型实例规格族i4g</a></p> </li> <li> <p><a href="#i4r">本地SSD型实例规格族i4r</a></p> </li> <li> <p><a href="#section-694-4fv-0rj">性能增强型本地盘实例规格族i4p</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#section-o4u-ofu-2f5">本地SSD型实例规格族i3g</a></p> </li> <li> <p><a href="#section-ogb-jlc-y4v">本地SSD型实例规格族i3</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#section-y55-6f0-568">本地SSD型实例规格族i2</a></p> </li> <li> <p><a href="#section-0xx-a83-xv8">本地SSD型实例规格族i2g</a></p> </li> <li> <p><a href="#section-yum-us8-tq0">本地SSD型实例规格族i2ne</a></p> </li> <li> <p><a href="#section-lze-1l0-mtl">本地SSD型实例规格族i2gne</a></p> </li> </ul> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族介绍
**警告**

本地盘的数据可靠性取决于物理机的可靠性，存在单点故障风险。使用本地盘存储数据有丢失数据的风险，请勿在本地盘上存储需要长期保存的业务数据。更多信息，请参见[本地盘](https://help.aliyun.com/document_detail/63138.html)。

本地SSD型实例属于高I/O型本地盘存储实例，适用于对存储I/O性能有极高要求，同时具备应用层高可用架构的业务场景，例如NoSQL非关系型数据库、MPP数据仓库、分布式文件系统等。

本地SSD型实例适合网络游戏、电商、视频直播、媒体等提供在线业务的行业客户，满足I/O密集型应用对块存储的低时延和高I/O性能需求。  
本地SSD型实例具有以下特点：

* 在大型数据库业务场景下，具备每秒数万至数十万次低时延随机IOPS读写能力。

* 在大数据、并行计算等大型数据集业务场景下，具备高达数GiB的顺序读写吞吐能力。

* 基于本地NVMe SSD磁盘资源，在提供高达数十万随机I/O读写能力的同时，时延水平保持在μs级别。

使用本地SSD型实例时请注意：

* 不支持变配。

* 本地盘与特定规格的实例相绑定，本地盘的数量和容量由您选择的实例规格决定。不支持单独购买本地盘，不支持将本地盘卸载并挂载到另一台实例上使用。

* 本地盘不支持快照功能。如果您需要为本地盘实例创建包含系统盘和数据盘的镜像，建议通过组合系统盘快照和数据盘（仅限云盘）快照的方式来创建。

* 不支持基于实例ID创建包含系统盘和数据盘的镜像。

* 支持挂载SSD云盘，挂载的云盘支持扩容。

* 操作本地盘实例可能对本地盘数据产生影响，更多详情，请参见[实例操作对本地盘数据的影响](https://help.aliyun.com/document_detail/63138.html#section-vdp-m2w-ydb)。

## 本地SSD型实例规格族i5g
* **规格族介绍** ：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。采用阿里云全新CIPU架构，搭载英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**：磁盘类KV数据库如RocksDB、ClickHouse；E-MapReduce大数据冷热数据分层、存储计算分离、数据湖；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

i5g包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i5g.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>16/32</p> </td> <td> <p>1000万</p> </td> <td> <p>20万/30万</p> </td> <td> <p>10/12</p> </td> </tr> <tr> <td> <p>ecs.i5g.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>1 \* 3839 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>2000万</p> </td> <td> <p>30万/无</p> </td> <td> <p>16/无</p> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族i5ge
* **规格族介绍** ：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。采用阿里云全新CIPU架构，搭载英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**：磁盘类KV数据库如RocksDB、ClickHouse；大数据计算（本地缓存）；在线交易等场景。

* **计算**：

  * 处理器与内存配比为1:6。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

i5ge包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i5ge.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>72</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>25/40</p> </td> <td> <p>400万</p> </td> <td> <p>8万/20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.i5ge.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>144</p> </td> <td> <p>1 \* 3839 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>50/70</p> </td> <td> <p>800万</p> </td> <td> <p>12万/20万</p> </td> <td> <p>7.5/10</p> </td> </tr> <tr> <td> <p>ecs.i5ge.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>288</p> </td> <td> <p>2 \* 3839 GB</p> <p>(2 \* 3576 GiB)</p> </td> <td> <p>84/无</p> </td> <td> <p>1500万</p> </td> <td> <p>24万/无</p> </td> <td> <p>12/无</p> </td> </tr> <tr> <td> <p>ecs.i5ge.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>576</p> </td> <td> <p>4 \* 3839 GB</p> <p>(4 \* 3576 GiB)</p> </td> <td> <p> 172/无</p> </td> <td> <p>3000万</p> </td> <td> <p>30万/无</p> </td> <td> <p>20/无</p> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族i5e
* **规格族介绍** ：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。采用阿里云全新CIPU架构，搭载英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**：关系型数据库如MySQL；远端缓存服务、缓存层加速等场景。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频2.9 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

i5e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i5e.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 3840 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>20/40</p> </td> <td> <p>400万</p> </td> <td> <p>6万/20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.i5e.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 7680 GB</p> <p>(1 \* 7152 GiB)</p> </td> <td> <p>40/80</p> </td> <td> <p>700万</p> </td> <td> <p>10万/20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.i5e.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>2 \* 7680 GB</p> <p>(2 \* 7152 GiB)</p> </td> <td> <p>80/120</p> </td> <td> <p>1400万</p> </td> <td> <p>15万/20万</p> </td> <td> <p>10/12</p> </td> </tr> <tr> <td> <p>ecs.i5e.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>4 \* 7680 GB</p> <p>(4 \* 7152 GiB)</p> </td> <td> <p>160</p> </td> <td> <p>2500万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> </tr> <tr> <td> <p>ecs.i5e.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>8 \* 7680 GB</p> <p>(8 \* 7152 GiB)</p> </td> <td> <p>320</p> </td> <td> <p>5000万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族i5
* **规格族介绍** ：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。采用阿里云全新CIPU架构，搭载英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**：磁盘类KV数据库如RocksDB、ClickHouse、E-MapReduce大数据冷热数据分层、存储计算分离、数据湖；其他频繁将数据写入磁盘的I/O密集型应用，例如消息中间件、容器。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.4 GHz，全核睿频3.8 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

i5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i5.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 960 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>10/20</p> </td> <td> <p>200万</p> </td> <td> <p>4万/20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.i5.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>20/40</p> </td> <td> <p>400万</p> </td> <td> <p>6万/20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.i5.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 3839 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>40/80</p> </td> <td> <p>700万</p> </td> <td> <p>10万/20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.i5.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>2 \* 3839 GB</p> <p>(2 \* 3576 GiB)</p> </td> <td> <p>80/120</p> </td> <td> <p>1400万</p> </td> <td> <p>15万/20万</p> </td> <td> <p>10/12</p> </td> </tr> <tr> <td> <p>ecs.i5.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>384</p> </td> <td> <p>3 \* 3839 GB</p> <p>(3 \* 3576 GiB)</p> </td> <td> <p>120</p> </td> <td> <p>2000万</p> </td> <td> <p>24万</p> </td> <td> <p>12</p> </td> </tr> <tr> <td> <p>ecs.i5.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>4 \* 3839 GB</p> <p>(4 \* 3576 GiB)</p> </td> <td> <p>160</p> </td> <td> <p>2700万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族i4
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库、NoSQL数据库（例如Cassandra、MongoDB等）、Elasticsearch等搜索场景。

* **计算**：

  * 处理器：2.7 GHz主频的Intel^®^ Xeon^®^ 可扩展处理器（Ice Lake ），全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **与操作系统的兼容性说明** ：更多信息，请参见[本地SSD型i4实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2698334.html)。

i4包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i4.large</p> </td> <td> <p>2</p> </td> <td> <p>16</p> </td> <td> <p>1 \* 479 GB</p> <p>(1 \* 447 GiB)</p> </td> <td> <p>2.5/15</p> </td> <td> <p>90万</p> </td> <td> <p>2万/最高11万</p> </td> <td> <p>1.5/6</p> </td> </tr> <tr> <td> <p>ecs.i4.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>4/15</p> </td> <td> <p>100万</p> </td> <td> <p>4万/最高11万</p> </td> <td> <p>2/6</p> </td> </tr> <tr> <td> <p>ecs.i4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>6/15</p> </td> <td> <p>160万</p> </td> <td> <p>5万/最高11万</p> </td> <td> <p>3/6</p> </td> </tr> <tr> <td> <p>ecs.i4.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 3839 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>8万/最高11万</p> </td> <td> <p>5/6</p> </td> </tr> <tr> <td> <p>ecs.i4.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>2 \* 3839 GB</p> <p>(2 \* 3576 GiB)</p> </td> <td> <p>25/无</p> </td> <td> <p>600万</p> </td> <td> <p>15万/无</p> </td> <td> <p>8/无</p> </td> </tr> <tr> <td> <p>ecs.i4.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>4 \* 3839 GB</p> <p>(4 \* 3576 GiB)</p> </td> <td> <p>50/无</p> </td> <td> <p>1200万</p> </td> <td> <p>30万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.i4.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>8 \* 3839 GB</p> <p>(8 \* 3576 GiB)</p> </td> <td> <p>100/无</p> </td> <td> <p>2400万</p> </td> <td> <p>60万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族i4g
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘

* **适用场景**：OLTP、高性能关系型数据库；E-MapReduce大数据冷热数据分层、存储计算分离、数据湖等场景；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4，为高性能数据库等场景设计。

  * 处理器：2.7 GHz主频的Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake ），全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

i4g包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i4g.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>8/25</p> </td> <td> <p>300万</p> </td> <td> <p>10万</p> </td> <td> <p>6</p> </td> </tr> <tr> <td> <p>ecs.i4g.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>16/25</p> </td> <td> <p>600万</p> </td> <td> <p>15万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.i4g.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> </tr> <tr> <td> <p>ecs.i4g.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。

## 本地SSD型实例规格族i4r
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘

* **适用场景**：OLTP、高性能关系型数据库、NoSQL数据库（例如Cassandra、MongoDB等）、Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:8，为高性能数据库等场景设计，是热数据分层、数据湖等应用场景的最佳性价比实例规格。

  * 处理器：2.7 GHz主频的Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake ），全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

i4r包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i4r.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>8/25</p> </td> <td> <p>300万</p> </td> <td> <p>10万</p> </td> <td> <p>6</p> </td> </tr> <tr> <td> <p>ecs.i4r.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>16/25</p> </td> <td> <p>600万</p> </td> <td> <p>15万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.i4r.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> </tr> <tr> <td> <p>ecs.i4r.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 性能增强型本地盘实例规格族i4p
* **规格族介绍** ：基于Intel ^®^ 第二代傲腾持久内存（BPS），提供性能极高的本地盘，初始化本地盘的具体操作，请参见[将持久内存初始化为本地盘](https://help.aliyun.com/document_detail/188251.html#section-t66-l5n-e1g)。

* **适用场景**：

  * 基因测序类应用，详情请参见[案例说明](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20220706/misz/客户案例-寻因生物.pdf)。

  * 磁盘类KV型数据库，例如RocksDB、ClickHouse。

  * OLTP、高性能关系型数据库进行WAL优化等。

  * NoSQL数据库，例如Cassandra、MongoDB、HBase。

  * Elasticsearch等搜索场景。

  * 其他频繁将数据写入磁盘的I/O密集型应用，例如消息中间件、容器。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用第三代Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake ），基频2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i4p包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>持久内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i4p.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 126</p> </td> <td> <p>5/10</p> </td> <td> <p>160万</p> </td> <td> <p>5万/11万</p> </td> <td> <p>3/6</p> </td> </tr> <tr> <td> <p>ecs.i4p.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>2 \* 126</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>8万/11万</p> </td> <td> <p>5/6</p> </td> </tr> <tr> <td> <p>ecs.i4p.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>3 \* 126</p> </td> <td> <p>12/25</p> </td> <td> <p>450万</p> </td> <td> <p>11万/无</p> </td> <td> <p>6/无</p> </td> </tr> <tr> <td> <p>ecs.i4p.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>4 \* 126</p> </td> <td> <p>16/25</p> </td> <td> <p>600万</p> </td> <td> <p>15万/无</p> </td> <td> <p>8/无</p> </td> </tr> <tr> <td> <p>ecs.i4p.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>1 \* 1008</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>30万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.i4p.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>2 \* 1008</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>60万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族i3g
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake ），睿频3.2 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i3g包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i3g.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 479 GB</p> <p>(1 \* 447 GiB)</p> </td> <td> <p>3/10</p> </td> <td> <p>175万</p> </td> <td> <p>5.25万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.i3g.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>5/10</p> </td> <td> <p>350万</p> </td> <td> <p>8.4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.i3g.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 959 GB</p> <p>(2 \* 894 GiB)</p> </td> <td> <p>12/无</p> </td> <td> <p>700万</p> </td> <td> <p>15.75万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.i3g.13xlarge</p> </td> <td> <p>52</p> </td> <td> <p>192</p> </td> <td> <p>3 \* 959 GB</p> <p>(3 \* 894 GiB)</p> </td> <td> <p>16/无</p> </td> <td> <p>1200万</p> </td> <td> <p>25.2万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.i3g.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>384</p> </td> <td> <p>6 \* 959 GB</p> <p>(6 \* 894 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>2400万</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>  
**说明**

该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。

## 本地SSD型实例规格族i3
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘，并支持在线隔离坏盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake ），睿频3.2 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i3包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i3.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>1.5/10</p> </td> <td> <p>100万</p> </td> <td> <p>4万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.i3.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>2.5/10</p> </td> <td> <p>160万</p> </td> <td> <p>5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.i3.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>5/10</p> </td> <td> <p>300万</p> </td> <td> <p>8万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.i3.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>10/无</p> </td> <td> <p>600万</p> </td> <td> <p>15万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.i3.13xlarge</p> </td> <td> <p>52</p> </td> <td> <p>384</p> </td> <td> <p>6 \* 1919 GB</p> <p>(6 \* 1788 GiB)</p> </td> <td> <p>16/无</p> </td> <td> <p>900万</p> </td> <td> <p>24万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.i3.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>768</p> </td> <td> <p>12 \* 1919 GB</p> <p>(12 \* 1788 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>2400万</p> </td> <td> <p>48万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>  
**说明**

该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。

## 本地SSD型实例规格族i2
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:8，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i2包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p> <b>云盘带宽（Gbit/s） </b> </p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>1</p> </td> <td> <p>50万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>2</p> </td> <td> <p>100万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>3</p> </td> <td> <p>150万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>6</p> </td> <td> <p>200万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>8 \* 1919 GB</p> <p>(8 \* 1788 GiB)</p> </td> <td> <p>10</p> </td> <td> <p>400万</p> </td> <td> <p>最高16</p> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族i2g
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 仅支持IPv4。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i2g包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i2g.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>（1 \* 894 GiB）</p> </td> <td> <p>2</p> </td> <td> <p>100万</p> </td> </tr> <tr> <td> <p>ecs.i2g.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>3</p> </td> <td> <p>150万</p> </td> </tr> <tr> <td> <p>ecs.i2g.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>6</p> </td> <td> <p>200万</p> </td> </tr> <tr> <td> <p>ecs.i2g.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>10</p> </td> <td> <p>400万</p> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族i2ne
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:8，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

  * 实例网络带宽最高可达20 Gbit/s。

i2ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i2ne.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>2.5</p> </td> <td> <p>100万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>5</p> </td> <td> <p>150万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>8 \* 1919 GB</p> <p>(8 \* 1788 GiB)</p> </td> <td> <p>20</p> </td> <td> <p>400万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.20xlarge</p> </td> <td> <p>80</p> </td> <td> <p>704</p> </td> <td> <p>10 \* 1919 GB</p> <p>(10 \* 1788 GiB)</p> </td> <td> <p>25</p> </td> <td> <p>450万</p> </td> <td> <p>最高16</p> </td> </tr> </tbody> </table>

## 本地SSD型实例规格族i2gne
* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

  * 实例网络带宽最高可达20 Gbit/s。

i2gne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i2gne.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>2.5</p> </td> <td> <p>100万</p> </td> </tr> <tr> <td> <p>ecs.i2gne.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>5</p> </td> <td> <p>150万</p> </td> </tr> <tr> <td> <p>ecs.i2gne.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> </tr> <tr> <td> <p>ecs.i2gne.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>20</p> </td> <td> <p>400万</p> </td> </tr> </tbody> </table>
