通用算力型Universal实例（U实例）提供均衡的计算、内存和网络资源，支持多种处理器和多种处理器内存配比。该类型实例依托阿里云资源池化技术和智能调度算法进行动态资源管理，为您的应用提供持续的算力保障、稳定性保障、供应及弹性保障，可以满足大多数场景下的应用需求，是一款具有高性价比的企业级实例。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

## 通用算力型实例规格族u2a
* **规格族介绍** ：采用阿里云全新CIPU架构，兼容多代际AMD EPYC^™^ 处理器（支持 AMD Turin 处理器），可提供企业级的算力输出。

* **适用场景**：

  * 中小型数据库（Redis/Mysql等）

  * APP应用服务器

  * 中间件（MQ/Kafka等）

  * 网站或网络接入层（Apache/Nginx等）

  * 其他企业内部系统（如开发测试、邮件系统等）

* **计算**：

  * 支持 CPU 核心数量与内存容量配比为1:1/1:2/1:4的实例规格。

  * 处理器：AMD EPYC^™^ 处理器，睿频最高3.7 GHz。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#33f69521a4b8a)。

* **存储**：

  * I/O优化实例

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD Entry云盘、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

u2a包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.u2a-c1m1.large</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>1.2/最高12.5</p> </td> <td> <p>最高90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.large</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>1.2/最高12.5</p> </td> <td> <p>最高90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.2/最高12.5</p> </td> <td> <p>最高90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m1.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>2/最高12.5</p> </td> <td> <p>最高100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.6/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>2/最高12.5</p> </td> <td> <p>最高100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.6/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2/最高12.5</p> </td> <td> <p>最高100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.6/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>3.2/最高12.5</p> </td> <td> <p>最高160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>3.2/最高12.5</p> </td> <td> <p>最高160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>32</p> </td> <td> <p>6/最高12.5</p> </td> <td> <p>最高200万</p> </td> <td> <p>最高25万</p> </td> <td> <p>16</p> </td> <td> <p>4</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>6/最高12.5</p> </td> <td> <p>最高200万</p> </td> <td> <p>最高25万</p> </td> <td> <p>16</p> </td> <td> <p>4</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>48</p> </td> <td> <p>7/最高12.5</p> </td> <td> <p>最高250万</p> </td> <td> <p>最高36万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>3.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>7/最高12.5</p> </td> <td> <p>最高250万</p> </td> <td> <p>最高36万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>3.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>64</p> </td> <td> <p>8/最高25</p> </td> <td> <p>最高300万</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/最高25</p> </td> <td> <p>最高300万</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>96</p> </td> <td> <p>13/最高25</p> </td> <td> <p>400万</p> </td> <td> <p>60万</p> </td> <td> <p>24</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>6.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>13/最高25</p> </td> <td> <p>400万</p> </td> <td> <p>60万</p> </td> <td> <p>24</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>6.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>128</p> </td> <td> <p>16/最高25</p> </td> <td> <p>500万</p> </td> <td> <p>80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>8/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/最高25</p> </td> <td> <p>500万</p> </td> <td> <p>80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>8/最高10</p> </td> </tr> </tbody> </table>

## 通用算力型实例规格族u2i
* **规格族介绍**：采用阿里云全新CIPU架构，兼容多代际服务器，支持Intel最新的第五代和第六代至强平台。

* **适用场景**：

  * 中小类型和规模的企业级应用

  * 网站和应用服务器

  * 数据分析和计算

  * 中小型数据库系统、缓存、搜索集群

* **计算**：

  * 处理器与内存配比为1:1/1:2/1:4/1:8

  * 处理器：Intel ^®^ Xeon ^®^ Platinum可扩展处理器

* **存储**：

  * I/O优化实例

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD Entry云盘、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

u2i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.u2i-c1m1.large</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>2/最高15</p> </td> <td> <p>90万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/最高20万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>3/最高15</p> </td> <td> <p>110万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4万/最高20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>5/最高15</p> </td> <td> <p>130万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>3/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>12</p> </td> <td> <p>8/最高15</p> </td> <td> <p>180万</p> </td> <td> <p>最高30万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>16</p> </td> <td> <p>10/最高25</p> </td> <td> <p>240万</p> </td> <td> <p>最高35万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>24</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>最高40万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>32</p> </td> <td> <p>16/最高32</p> </td> <td> <p>400万</p> </td> <td> <p>最高60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/最高30万</p> </td> <td> <p>8/12</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.large</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>2/最高15</p> </td> <td> <p>90万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/最高20万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>3/最高15</p> </td> <td> <p>110万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4万/最高20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>5/最高15</p> </td> <td> <p>130万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>3/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>24</p> </td> <td> <p>8/最高15</p> </td> <td> <p>180万</p> </td> <td> <p>最高30万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>32</p> </td> <td> <p>10/最高25</p> </td> <td> <p>240万</p> </td> <td> <p>最高35万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>48</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>最高40万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>64</p> </td> <td> <p>16/最高32</p> </td> <td> <p>400万</p> </td> <td> <p>最高60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/最高30万</p> </td> <td> <p>8/12</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2/最高15</p> </td> <td> <p>90万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/最高20万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>3/最高15</p> </td> <td> <p>110万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4万/最高20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>5/最高15</p> </td> <td> <p>130万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>3/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>8/最高15</p> </td> <td> <p>180万</p> </td> <td> <p>最高30万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>10/最高25</p> </td> <td> <p>240万</p> </td> <td> <p>最高35万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>最高40万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/最高32</p> </td> <td> <p>400万</p> </td> <td> <p>最高60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/最高30万</p> </td> <td> <p>8/12</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.large</p> </td> <td> <p>2</p> </td> <td> <p>16</p> </td> <td> <p>2/最高15</p> </td> <td> <p>90万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/最高20万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>3/最高15</p> </td> <td> <p>110万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4万/最高20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>5/最高15</p> </td> <td> <p>130万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>3/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>96</p> </td> <td> <p>8/最高15</p> </td> <td> <p>180万</p> </td> <td> <p>最高30万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>10/最高25</p> </td> <td> <p>240万</p> </td> <td> <p>最高35万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>192</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>最高40万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>16/最高32</p> </td> <td> <p>400万</p> </td> <td> <p>最高60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/最高30万</p> </td> <td> <p>8/12</p> </td> </tr> </tbody> </table>

## 通用算力型实例规格族u1
* **适用场景**：

  * 中小类型和规模的企业级应用

  * 网站和应用服务器

  * 数据分析和计算

  * 中小型数据库系统、缓存、搜索集群

* **计算**：

  * 处理器与内存配比为1:1/1:2/1:4/1:8

  * 处理器：Intel ^®^ Xeon ^®^ Platinum可扩展处理器

  **说明**

  该规格族的实例在创建时随机部署在不同的服务器平台，在实例的生命周期中也可能迁移到不同的服务器平台，u1实例采用技术手段促进不同平台间实现更好的业务兼容性，但不同平台间可能存在明显业务性能差异。如果您对业务性能一致性有强烈诉求，建议您选用g9i\&c9i\&r9i实例。
* **存储**：

  * I/O优化实例

  * 支持的云盘类型：ESSD Entry云盘、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)和[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

u1包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.u1-c1m1.large</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>2</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.large</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>2</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>2</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.large</p> </td> <td> <p>2</p> </td> <td> <p>16</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>2</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>12</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>24</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>96</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>16</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>32</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>64</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> </tbody> </table>  
**说明**

* 在u1实例上部署DPDK应用可能发生异常，需使用VFIO驱动替代UIO驱动来解决该问题。更多详情，请参见[使用VFIO驱动替代UIO驱动](https://help.aliyun.com/document_detail/310880.html#task-2112980)。

* 有关Universal实例的常见问题，请参见[U1实例FAQ](https://help.aliyun.com/document_detail/2983145.html#03ef52fc1666j)。
