购买ECS实例之前，您需要结合性能、价格、工作负载等因素，做出性价比与稳定性最优的决策。本文主要介绍如何结合实际业务场景选购阿里云云服务器ECS。  

## **了解实例规格族**
在进行规格选型之前，您需要提前了解以下信息：

1. [实例规格分类与命名](https://help.aliyun.com/document_detail/2849443.html)：帮助您更好地理解实例规格族的命名及分类信息。

2. [实例规格族](https://help.aliyun.com/document_detail/25378.html)：了解在售实例规格族的详细信息。

## 实例适用场景
### 企业级实例

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4133513471/CAEQTxiBgMCevsqMkRkiIDllNDg2MTQ2OWI0ZTRhZTBiMDU3NTlhNDRlZDJlZjg43963382_20230830144006.372.svg)  

### 异构计算实例

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4133513471/CAEQVRiBgIDdjqjarhkiIDAwMDczOWUxYjU0MDQ3NWRiNTlmZjM0OTA4ODZmYjUx3963382_20230830144006.372.svg)

## 根据预装软件选型
根据您需要在系统预装软件推荐实例规格族。
<table> <thead> <tr> <td><p><b>应用类型</b></p></td> <td><p><b>常用应用</b></p></td> <td><p><b>选型原则</b></p></td> <td><p><b>推荐实例规格族</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>负载均衡</p></td> <td><p>Nginx</p></td> <td><p>应用特点：需要支持高频率的新建连接操作。</p> <ul> <li><p>CPU计算能力：要求较高。</p></li> <li><p>内存：要求不高。</p></li> </ul></td> <td><p>c8i、c7、c7nex、g5ne</p></td> </tr> <tr> <td><p>RPC产品</p></td> <td> <ul> <li><p>SOFA</p></li> <li><p>Dubbo</p></li> </ul></td> <td><p>应用特点：网络链接密集型；进程运行时需要消耗较高的内存。</p></td> <td><p>g8a、g7nex、g8i、g7</p></td> </tr> <tr> <td><p>缓存</p></td> <td> <ul> <li><p>Redis</p></li> <li><p>Memcache</p></li> <li><p>Solo</p></li> </ul></td> <td> <ul> <li><p>CPU计算能力：要求不高。</p></li> <li><p>内存：要求较高。</p></li> </ul></td> <td><p>r8i、r8a、r7、r7a</p></td> </tr> <tr> <td><p>配置中心</p></td> <td><p>ZooKeeper</p></td> <td><p>在应用启动协商时会有大量I/O读写操作。</p> <ul> <li><p>CPU计算能力：要求不高。</p></li> <li><p>内存：要求不高。</p></li> </ul></td> <td><p>c8a、c7、c8i、u1</p></td> </tr> <tr> <td><p>消息队列</p></td> <td> <ul> <li><p>Kafka</p></li> <li><p>RabbitMQ</p></li> </ul></td> <td><p>从消息完整性方面考虑，存储优先选用云盘。</p> <ul> <li><p>CPU计算能力：要求不高。</p></li> <li><p>内存和vCPU配比通常为1:1。</p></li> <li><p>存储：要求不高。</p></li> </ul></td> <td><p>c8a、c7、c8i、u1</p></td> </tr> <tr> <td><p>容器编排</p></td> <td><p>Kubernetes</p></td> <td><p>通过弹性裸金属服务器和容器的组合，可以最大限度地挖掘计算潜能。</p></td> <td><p>ebmc6e、ebmg6e、ebmc6、ebmg6、ebmc6a、ebmc7a、ebmg6a、ebmg7a系列</p></td> </tr> <tr> <td><p>大表存储</p></td> <td><p>HBase</p></td> <td> <ul> <li><p>一般可以选择d系列。</p></li> <li><p>如果业务存在超高IOPS（Input/Output Operations Per Second）需求，可以选择i系列。</p></li> </ul></td> <td><p>d3c、d3s、i4</p></td> </tr> <tr> <td><p>数据库</p></td> <td> <ul> <li><p>MySQL</p></li> <li><p>NoSQL</p></li> </ul></td> <td> <ul> <li><p>对于存储有弹性扩展的需求，可以选择ECS和ESSD。</p></li> <li><p>对于I/O敏感型业务的需求，优先选择i系列。</p></li> </ul></td> <td><p>g8a、g7、g8i、i4,</p></td> </tr> <tr> <td><p>SQLServer</p></td> <td> <ul> <li><p>由于Windows的I/O单通道特性，对I/O读写能力要求较高，优先选择ESSD。</p></li> <li><p>ECS的逻辑和物理扇区设置为4 K。</p></li> </ul></td> <td><p>g8a、g7、r7、r8i、g8i</p></td> </tr> <tr> <td><p>文本搜索</p></td> <td><p>Elasticsearch</p></td> <td> <ul> <li><p>选用内存与vCPU配比较大的ECS规格。</p></li> <li><p>日常需要将数据库数据导出成ES文件，对I/O读写有要求。</p></li> </ul></td> <td><p>i4、i4r、i3、i2</p></td> </tr> <tr> <td><p>实时计算</p></td> <td> <ul> <li><p>Flink</p></li> <li><p>Blink</p></li> </ul></td> <td><p>基于存储量可以选择ECS通用规格和云盘，也可以选择d系列。</p></td> <td><p>i4g、i4、d3c</p></td> </tr> <tr> <td><p>离线计算</p></td> <td> <ul> <li><p>Hadoop</p></li> <li><p>HDFS</p></li> <li><p>CDH</p></li> </ul></td> <td><p>优先选择d系列。</p></td> <td><p>d3s、d3c</p></td> </tr> <tr> <td><p>视频转码</p></td> <td> <ul> <li><p>点播</p></li> <li><p>直播</p></li> </ul></td> <td> <ul> <li><p>CPU计算能力：要求高</p></li> <li><p>内存：要求不高</p></li> <li><p>IO：要求不高</p></li> </ul><p></p></td> <td><p>c8y<span>、hfc8i</span></p></td> </tr> <tr> <td><p>大数据</p></td> <td> <ul> <li><p>Spark</p></li> <li><p>Hive</p></li> </ul></td> <td> <ul> <li><p>CPU计算能力：要求高</p></li> <li><p>内存：内存带宽要求高</p></li> <li><p>IO：存储带宽要求高</p></li> </ul></td> <td><p>g8y、r8y</p></td> </tr> </tbody> </table>

## 根据细分业务场景选型
### 通用应用、游戏服务、视频直播场景推荐

在该类场景中，性能需求表现为CPU计算密集型，您需要相对均衡的处理器与内存资源配比，通常选用CPU与内存配比1:2、系统盘和数据盘选用ESSD云盘。如果业务需要更强的网络性能，如视频弹幕等，您可以选用同系列中更高规格的实例规格，提高网络收发包能力（PPS）。
<table> <thead> <tr> <td><p><b>场景分类</b></p></td> <td><p><b>场景细分</b></p></td> <td><p><b>推荐规格族</b></p></td> <td><p><b>性能需求</b></p></td> <td><p><b>处理器与内存比</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>通用应用</p></td> <td><p>均衡性能应用，后台应用</p></td> <td><p>g系列，如g7</p></td> <td><p>中主频，计算密集型</p></td> <td><p>1:4</p></td> </tr> <tr> <td><p>高网络收发包应用</p></td> <td><p>g系列，如g7</p></td> <td><p>高网络PPS，计算密集型</p></td> <td><p>1:4</p></td> </tr> <tr> <td><p>高性能计算</p></td> <td><p>hfc系列，如hfc7</p></td> <td><p>高主频，计算密集型</p></td> <td><p>1:2</p></td> </tr> <tr> <td><p>游戏应用</p></td> <td><p>高性能端游</p></td> <td><p>hfc系列，如hfc7</p></td> <td><p>高主频</p></td> <td><p>1:2</p></td> </tr> <tr> <td><p>手游、页游</p></td> <td><p>g系列，如g6e</p></td> <td><p>中主频</p></td> <td><p>1:4</p></td> </tr> <tr> <td><p>视频直播</p></td> <td><p>视频转发</p></td> <td><p>g系列，如g7</p></td> <td><p>中主频，计算密集型</p></td> <td><p>1:4</p></td> </tr> <tr> <td><p>直播弹幕</p></td> <td><p>g系列，如g7</p></td> <td><p>高网络PPS，计算密集型</p></td> <td><p>1:4</p></td> </tr> </tbody> </table>

### Hadoop、Spark、Kafka大数据场景推荐

在该类场景中，由于涉及不同的节点，性能需求表现较为复杂，您需要均衡各个节点的性能表现，包括计算、存储吞吐量、网络性能等。

* 管理节点：当作通用场景处理，推荐使用g系列。

* 计算节点：当作通用场景处理，推荐使用g系列。根据集群规模的不同，需要选择的实例规格不同。例如100个节点以下可以选用ecs.g7.4xlage，100个节点以上可以选用ecs.g7.8xlage。

* 缓存节点：用于存储热数据或部署RSS，侧重磁盘和网络IO性能，推荐使用i4g、i2g。

* 计算缓存节点：用于计算和缓存，兼备计算性能和IO性能、磁盘容量，推荐使用i4、i4r、d3c。

  **说明**

  计算节点在计费模式上可以采用抢占式实例，实现性价比最优化。更多信息，请参见[什么是抢占式实例](https://help.aliyun.com/document_detail/52088.html#concept-t3p-gv2-5db)。
* 数据节点：需要高存储吞吐、高网络吞吐、均衡的处理器与内存配比，推荐您使用大数据型（d系列）规格族。例如MapReduce/Hive可选择ecs.d2s.5xlarge、ecs.d3s.4xlarge等，Spark/Mlib可选择ecs.d2s.10xlarge。

### 数据库、缓存、搜索场景推荐

在该类场景中，实例规格的处理器与内存配比一般要求高于1:4，部分软件对存储I/O读写能力及时延性能较为敏感，建议您选用单位内存性价比较高的规格族。
<table> <thead> <tr> <td><p><b>场景分类</b></p></td> <td><p><b>场景细分</b></p></td> <td><p><b>推荐规格族</b></p></td> <td><p><b>处理器与内存比</b></p></td> <td><p><b>数据盘</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>关系型数据库</p></td> <td><p>高性能，依赖应用层高可用</p></td> <td><p>i系列</p></td> <td><p>1:4</p></td> <td><p>本地SSD存储、高效云盘、SSD云盘</p></td> </tr> <tr> <td><p>中小型数据库</p></td> <td><p>g系列，或其他内存占比为1:4的规格族</p></td> <td><p>1:4</p></td> <td><p>高效云盘、SSD云盘</p></td> </tr> <tr> <td><p>高性能数据库</p></td> <td><p>i、r系列</p></td> <td><p>1:8</p></td> <td><p>高效云盘、SSD云盘</p></td> </tr> <tr> <td><p>分布式缓存</p></td> <td><p>中内存消耗场景</p></td> <td><p>g系列，或其他内存占比为1:4的规格族</p></td> <td><p>1:4</p></td> <td><p>高效云盘、SSD云盘</p></td> </tr> <tr> <td><p>高内存消耗场景</p></td> <td><p>r系列、i系列</p></td> <td><p>1:8</p></td> <td><p>高效云盘、SSD云盘</p></td> </tr> <tr> <td><p>NoSQL数据库</p></td> <td><p>高性能，应用层高可用</p></td> <td><p>i系列</p></td> <td><p>1:4</p></td> <td><p>本地SSD存储、高效云盘、SSD云盘</p></td> </tr> <tr> <td><p>中小型数据库</p></td> <td><p>g系列，或其他内存占比为1:4的规格族</p></td> <td><p>1:4</p></td> <td><p>高效云盘、SSD云盘</p></td> </tr> <tr> <td><p>高性能数据库</p></td> <td><p>i4、i4r系列</p></td> <td><p>1:8</p></td> <td><p>高效云盘、SSD云盘、本地SSD存储</p></td> </tr> <tr> <td><p>ElasticSearch</p></td> <td><p>小集群，靠云盘保证数据高可用</p></td> <td><p>g系列，或其他内存占比为1:4的规格族</p></td> <td><p>1:4</p></td> <td><p>高效云盘、SSD云盘</p></td> </tr> <tr> <td><p>大集群，高可用</p></td> <td><p>d系列</p></td> <td><p>1:4</p></td> <td><p>本地SSD存储、高效云盘、SSD云盘</p></td> </tr> </tbody> </table>  
以数据库为例，在传统方式中，业务系统直接对接OLTP数据库，数据冗余大多通过RAID磁盘阵列实现。选择云服务器ECS，您的轻载、重载数据库都能实现灵活部署。

* 轻载数据库：采用i4r、i4g系列实例搭配云盘使用，性价比更高。

* 重载数据库：需要高存储IOPS和低读写延时，推荐您使用本地SSD型i系列实例规格族（搭配了高I/O型本地NVMeSSD本地盘），满足大型重载数据库的要求。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4133513471/CAEQTxiBgIDT7JONkRkiIDVhZTNjNzI5MTM4YzQ4ZWU5ODBmNDBkNWRkM2RkMzE44688803_20240924165958.403.svg)

### 深度学习、图像处理场景推荐

在该类场景中，应用需要高性能的GPU加速器，在GPU和CPU配比方面有如下建议。

* 深度学习训练：GPU与CPU比例推荐为1:8到1:12之间。

* 通用深度学习：GPU与CPU比例推荐为1:4到1:48之间。

* 图像识别推理：GPU与CPU比例推荐为1:4到1:12之间。

* 语音识别与合成推理：GPU与CPU比例推荐为1:16到1:48之间。

常见场景的GPU选型推荐如下图所示。
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4133513471/CAEQTxiBgMCxyOCOkRkiIGY3ZjZkYTNmYTA5ODQzMDViZjRmODZlOTJmNDU5YmI34688803_20240924170954.635.svg)

## 验证与调整
当您完成选型并开始使用云服务器ECS实例后，建议您根据一段时间的性能监控信息，验证所选实例规格是否合适。  
假设您选择了ecs.g8i.xlarge，通过监控发现实例CPU使用率一直较低，建议您检查是否是由于实例内存占用率较高所致。查询方法如下：

* [通过ECS控制台查看监控信息](https://help.aliyun.com/document_detail/25482.html#section-o2c-nxz-xdb)

* [查看云盘监控信息](https://help.aliyun.com/document_detail/25453.html#concept-hvt-zkj-ydb)

如果内存占用较高，您可以将当前实例调整为处理器与内存配比更合适的实例规格。更多信息可参考：

* [升降配方式概述](https://help.aliyun.com/document_detail/25437.html#concept-anb-bbf-5db)

* [支持变配的实例规格](https://help.aliyun.com/document_detail/89743.html#concept-mdh-2rb-1fb)
