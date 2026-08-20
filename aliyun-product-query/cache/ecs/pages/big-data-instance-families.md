大数据型实例规格（d系列）处理器与内存配比为1:4（部分规格不为1:4），适用于Hadoop MapReduce、HDFS、Hive、HBase等大数据计算和存储业务场景，以及Elasticsearch、Kafka等搜索和日志数据处理场景。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

<table> <thead> <tr> <td><p><b>推荐</b></p></td> <td><p><b>不推荐（如果以下规格售罄，建议使用前面的规格）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#d3s">大数据存储密集型实例规格族d3s</a></p></li> <li><p><a href="#section-9in-q1s-mqb">大数据计算密集型实例规格族d3c</a></p></li> <li><p><a href="#section-g5o-ipf-viq">大数据计算密集型实例规格族d2c</a></p></li> <li><p><a href="#section-eum-nil-2ui">大数据存储密集型实例规格族d2s</a></p></li> </ul></td> <td> <ul> <li><p><a href="#section-0yv-1sx-xyf">大数据网络增强型实例规格族d1ne</a></p></li> </ul></td> </tr> </tbody> </table>

## 大数据型实例规格族介绍
**警告**

本地盘的数据可靠性取决于物理机的可靠性，存在单点故障风险。使用本地盘存储数据有丢失数据的风险，请勿在本地盘上存储需要长期保存的业务数据。更多信息，请参见[本地盘](https://help.aliyun.com/document_detail/63138.html)。

大数据型实例规格族旨在解决大数据时代下海量业务数据的云上计算和存储难题，适用于Hadoop分布式计算、海量日志处理和大型数据仓库等需要海量数据存储和离线计算的业务场景，充分满足以Hadoop为代表的分布式计算业务对实例存储性能、容量和内网带宽等方面要求。

大数据型实例规格族适合有大数据计算与存储分析需求的行业客户，例如互联网行业、金融行业等。同时，结合以Hadoop为代表的分布式计算业务的高可用架构，大数据型实例采用本地存储的设计，保证海量存储空间、高存储性能。  
大数据实例具有以下特点：

* 基于企业级架构提供稳定计算能力，为高效处理计算作业提供保障。

* 网络性能更高（包括单实例最大内网带宽和最大小包转发率），满足业务高峰期实例间的数据交互需求，例如MapReduce计算框架下的Shuffle过程。

使用大数据实例时请注意：

* 不支持变配。

* 本地盘与特定规格的实例相绑定，本地盘的数量和容量由您选择的实例规格决定。不支持单独购买本地盘，不支持将本地盘卸载并挂载到另一台实例上使用。

* 本地盘不支持快照功能。如果您需要为本地盘实例创建包含系统盘和数据盘的镜像，建议通过组合系统盘快照和数据盘（仅限云盘）快照的方式来创建。

* 不支持基于实例ID创建包含系统盘和数据盘的镜像。

* 支持挂载SSD云盘，挂载的云盘支持扩容。

* 操作本地盘实例可能对本地盘数据产生影响，更多详情，请参见[实例操作对本地盘数据的影响](https://help.aliyun.com/document_detail/63138.html#section-vdp-m2w-ydb)。

## 大数据实例文件系统挂载最佳实践
使用ext4等文件系统，首次执行mount操作时需要初始化inode table。在Linux的2.6.37及更高的内核版本中，默认启用了lazyinit特性，导致inode table初始化会延迟到mount后，且本地盘在初始化时会占用较大吞吐量（例如30个本地盘的吞吐量可能高达600 MB/s），影响业务稳定性。4.x版本内核中增加了lazyinit并发度，可以缓解该问题，详情请参见[社区](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=e22834f0248d0fa841ead6436d6c19f65539dc9c)。ECS推荐以下最佳实践，使您在相对较快的时间内完成初始化：

1. 获取所有SATA HDD本地盘列表。

2. 运行以下命令，为每个本地盘开启独立的后台初始化。

   本示例中，在设备名为/dev/vdb的本地盘上创建ext4文件系统。

   ```
   HELPCODEESCAPE-shell
   mkfs.ext4 -E lazy_itable_init=0,lazy_journal_init=0 /dev/vdb &
   ```

3. 等待所有本地盘完成初始化，并运行iostat -x 5，直至所有本地盘的I/O活动显示为0。

4. 批量执行mount操作。

## 大数据存储密集型实例规格族d3s
* **规格族介绍**：实例配备12 TB大容量、高吞吐SATA HDD本地盘，辅以最大64 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、HBase等大数据计算和存储业务场景。

  * Spark内存计算、MLlib等机器学习场景。

  * ElasticSearch、Kafka等搜索和日志数据处理场景。

* 支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。

  如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](https://help.aliyun.com/document_detail/107693.html#concept-x5k-24p-tgb)。  
  **重要**

  确认发起坏盘修复流程后，坏盘中的数据不可恢复。
* **计算**：

  * 处理器：2.7 GHz主频的 ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘和ESSD AutoPL云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d3s包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d3s.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>4 \* 11918 GB</p><p>(4 \* 11100 GiB)</p></td> <td><p>10/最高15</p></td> <td><p>200</p></td> <td><p>3/最高5</p></td> </tr> <tr> <td><p>ecs.d3s.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>8 \* 11918 GB</p><p>(8 \* 11100 GiB)</p></td> <td><p>25/无</p></td> <td><p>300</p></td> <td><p>5/无</p></td> </tr> <tr> <td><p>ecs.d3s.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>16 \* 11918 GB</p><p>(16 \* 11100 GiB)</p></td> <td><p>40/无</p></td> <td><p>600</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.d3s.12xlarge</p></td> <td><p>48</p></td> <td><p>192</p></td> <td><p>24 \* 11918 GB</p><p>(24 \* 11100 GiB)</p></td> <td><p>60/无</p></td> <td><p>900</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.d3s.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>32 \* 11918 GB</p><p>(32 \* 11100 GiB)</p></td> <td><p>80/无</p></td> <td><p>1200</p></td> <td><p>16/无</p></td> </tr> </tbody> </table>

## 大数据计算密集型实例规格族d3c
d3c的特点如下：

* **规格族介绍**：实例配备大容量、高吞吐本地盘，辅以最大40 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、HBase等大数据计算和存储业务场景。

  * EMR JindoFS配合OSS实现大数据冷热数据分层和存储计算分离的场景。

  * Spark内存计算、MLlib等机器学习场景。

  * ElasticSearch、Kafka等搜索和日志数据处理场景。

* 支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。

  如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](https://help.aliyun.com/document_detail/107693.html#concept-x5k-24p-tgb)。  
  **重要**

  确认发起坏盘修复流程后，坏盘中的数据不可恢复。
* **计算**：

  * 处理器：采用第三代Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），主频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘和ESSD AutoPL云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d3c包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>云盘IOPS基础/突发（万）</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d3c.3xlarge</p></td> <td><p>14</p></td> <td><p>56.0</p></td> <td><p>1 \* 13743 GB</p><p>(1 \* 12800 GiB)</p></td> <td><p>8/最高10</p></td> <td><p>160</p></td> <td><p>4/无</p></td> <td><p>3/无</p></td> </tr> <tr> <td><p>ecs.d3c.7xlarge</p></td> <td><p>28</p></td> <td><p>112.0</p></td> <td><p>2 \* 13743 GB</p><p>(2 \* 12800 GiB)</p></td> <td><p>16/最高25</p></td> <td><p>250</p></td> <td><p>5/无</p></td> <td><p>4/无</p></td> </tr> <tr> <td><p>ecs.d3c.14xlarge</p></td> <td><p>56</p></td> <td><p>224.0</p></td> <td><p>4 \* 13743 GB</p><p>(4 \* 12800 GiB)</p></td> <td><p>40/无</p></td> <td><p>500</p></td> <td><p>10/无</p></td> <td><p>8/无</p></td> </tr> </tbody> </table>  
**说明**

该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。

## 大数据计算密集型实例规格族d2c
* **规格族介绍**：实例配备大容量、高吞吐SATA HDD本地盘，辅以最大35 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、Hbase等大数据计算和存储业务场景。

  * EMR JindoFS配合OOS实现大数据冷热数据分层和存储计算分离的场景。

  * Spark内存计算、MLlib等机器学习场景。

  * ElasticSearch、Kafka等搜索和日志数据处理场景。

* 支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。

  如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](https://help.aliyun.com/document_detail/107693.html#concept-x5k-24p-tgb)。  
  **重要**

  确认发起坏盘修复流程后，坏盘中的数据不可恢复。
* **计算**：

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d2c包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d2c.6xlarge</p></td> <td><p>24</p></td> <td><p>88.0</p></td> <td><p>3 \* 3972 GB</p><p>(3 \* 3700 GiB)</p></td> <td><p>12.0</p></td> <td><p>160</p></td> </tr> <tr> <td><p>ecs.d2c.12xlarge</p></td> <td><p>48</p></td> <td><p>176.0</p></td> <td><p>6 \* 3972 GB</p><p>(6 \* 3700 GiB)</p></td> <td><p>20.0</p></td> <td><p>200</p></td> </tr> <tr> <td><p>ecs.d2c.24xlarge</p></td> <td><p>96</p></td> <td><p>352.0</p></td> <td><p>12 \* 3972 GB</p><p>(12 \* 3700 GiB)</p></td> <td><p>35.0</p></td> <td><p>450</p></td> </tr> </tbody> </table>

## 大数据存储密集型实例规格族d2s
* **规格族介绍**：实例配备大容量、高吞吐SATA HDD本地盘，辅以最大35 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、Hbase等大数据计算和存储业务场景。

  * Spark内存计算、MLlib等机器学习场景。

  * ElasticSearch、Kafka等搜索和日志数据处理场景。

* 支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。

  如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](https://help.aliyun.com/document_detail/107693.html#concept-x5k-24p-tgb)。  
  **重要**

  确认发起坏盘修复流程后，坏盘中的数据不可恢复。
* **计算**：

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d2s包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d2s.5xlarge</p></td> <td><p>20</p></td> <td><p>88.0</p></td> <td><p>8 \* 7838 GB</p><p>(8 \* 7300 GiB)</p></td> <td><p>12.0</p></td> <td><p>160</p></td> </tr> <tr> <td><p>ecs.d2s.10xlarge</p></td> <td><p>40</p></td> <td><p>176.0</p></td> <td><p>15 \* 7838 GB</p><p>(15 \* 7300 GiB)</p></td> <td><p>20.0</p></td> <td><p>200</p></td> </tr> <tr> <td><p>ecs.d2s.20xlarge</p></td> <td><p>80</p></td> <td><p>352.0</p></td> <td><p>30 \* 7838 GB</p><p>(30 \* 7300 GiB)</p></td> <td><p>35.0</p></td> <td><p>450</p></td> </tr> </tbody> </table>

## 大数据网络增强型实例规格族d1ne
* **规格族介绍**：实例配备大容量、高吞吐SATA HDD本地盘，辅以最大35 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、HBase等。

  * Spark内存计算、MLlib等。

  * ElasticSearch、日志等。

* **计算**：

  * 处理器与内存配比为1:4，为大数据场景设计。

  * 处理器：2.5 GHz主频的Intel^®^ Xeon^®^ E5-2682 v4（Broadwell）或者Intel^®^ Xeon^®^Platinum 8163（Skylake），计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d1ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d1ne.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>4 \* 5905 GB</p><p>(4 \* 5500 GiB)</p></td> <td><p>6.0</p></td> <td><p>100</p></td> </tr> <tr> <td><p>ecs.d1ne.4xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>8 \* 5905 GB</p><p>(8 \* 5500 GiB)</p></td> <td><p>12.0</p></td> <td><p>160</p></td> </tr> <tr> <td><p>ecs.d1ne.6xlarge</p></td> <td><p>24</p></td> <td><p>96.0</p></td> <td><p>12 \* 5905 GB</p><p>(12 \* 5500 GiB)</p></td> <td><p>16.0</p></td> <td><p>200</p></td> </tr> <tr> <td><p>ecs.d1ne-c8d3.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>12 \* 5905 GB</p><p>(12 \* 5500 GiB)</p></td> <td><p>20.0</p></td> <td><p>200</p></td> </tr> <tr> <td><p>ecs.d1ne.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>16 \* 5905 GB</p><p>(16 \* 5500 GiB)</p></td> <td><p>20.0</p></td> <td><p>250</p></td> </tr> <tr> <td><p>ecs.d1ne-c14d3.14xlarge</p></td> <td><p>56</p></td> <td><p>160.0</p></td> <td><p>12 \* 5905 GB</p><p>(12 \* 5500 GiB)</p></td> <td><p>35.0</p></td> <td><p>450</p></td> </tr> <tr> <td><p>ecs.d1ne.14xlarge</p></td> <td><p>56</p></td> <td><p>224.0</p></td> <td><p>28 \* 5905 GB</p><p>(28 \* 5500 GiB)</p></td> <td><p>35.0</p></td> <td><p>450</p></td> </tr> </tbody> </table>
