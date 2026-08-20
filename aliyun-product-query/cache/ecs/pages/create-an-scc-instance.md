超级计算集群SCC（Super Computing Cluster）在弹性裸金属服务器基础上，加入高速RDMA（Remote Direct Memory Access）互联支持，大幅提升网络性能，提高大规模集群加速比。本文介绍如何创建超级计算集群（SCC）实例。  

## 背景信息
本文重点介绍创建SCC实例时需要特别注意的基础配置项，如果您想了解其他通用配置，请参见[自定义购买实例](https://help.aliyun.com/document_detail/87190.html#task-vwq-5g4-r2b)。

如果您不仅需要使用RDMA功能，还需要使用HPC调度器以及集群扩容缩容服务，可以通过[E-HPC 控制台](https://ehpc.console.aliyun.com/)创建SCC集群来创建SCC实例，具体操作请参见[使用向导创建集群](https://help.aliyun.com/document_detail/57937.html)。

## 操作步骤
1. 前往[实例购买页](https://ecs-buy.aliyun.com/wizard/#/)。

2. 按需选择付费类型、实例规格及镜像等配置。

   <table> <thead> <tr> <td> <p><b>配置项</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>付费类型</b></p> </td> <td> <p>付费类型影响实例的计费和收费规则，不同付费类型的实例遵循的资源状态变化规则也存在差异。取值范围：</p> <ul> <li> <p><a href="https://help.aliyun.com/document_detail/56220.html#subs-china">包年包月</a></p> </li> <li> <p><a href="https://help.aliyun.com/document_detail/40653.html#Pay-As-You-Go">按量付费</a></p> </li> <li> <p><a href="https://help.aliyun.com/document_detail/178880.html#concept-1936192">抢占式实例</a></p> </li> </ul> </td> </tr> <tr> <td> <p><b>地域</b></p> </td> <td> <p>指数据中心所在的地理区域，选择距离近的地域可以降低网络时延，实例创建完成后不支持更改地域。更多信息，请参见<a href="https://help.aliyun.com/document_detail/40654.html#concept-2459516">地域和可用区</a>。</p> </td> </tr> <tr> <td> <p><b>网络及可用区</b></p> </td> <td> <ul> <li> <p>推荐您使用专有网络，专有网络之间逻辑上彻底隔离，安全性更高，且支持弹性公网IP（EIP）、弹性网卡、IPv6等功能。</p> </li> <li> <p>可用区是指在同一地域内，电力和网络互相独立的物理区域。同一可用区内实例之间的网络延时更小，其用户访问速度更快。</p> </li> </ul> </td> </tr> <tr> <td> <p><b>实例</b></p> </td> <td> <p>在<b>架构</b>行的<b>高性能计算</b>列选择<b>超级计算集群</b>，然后选择SCC实例规格。可选的实例规格和地域等因素有关，您可以前往<span><a href="https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion">ECS实例可购买地域</a></span>查看实例的可购情况。关于SCC实例规格的更多信息，请参见<a href="https://help.aliyun.com/document_detail/25378.html#concept-sx4-lxv-tdb">实例规格族</a>。</p> <p>选择SCC实例规格后，您需要在<b>超级计算集群</b>的<b>已有集群</b>页签下选择已创建的超级计算集群进行扩容创建，或者在<b>新建集群</b>页签下填写名称和描述。</p> <div> <div> <i></i> </div> <div> <strong>重要 </strong> <p>不是相同集群ID的服务器间无法互相联通，请慎重填写超级集群ID信息，如不确定，可以通过<a href="https://ecs.console.aliyun.com/?spm=5176.ecsnewbuy.customBuy_hpcCluster.1.6d1c36756HSg3P#/cluster/region/cn-hangzhou">超级计算集群</a>页面选定集群ID后进行扩容创建。</p> </div> </div> </td> </tr> <tr> <td> <p><b>镜像</b></p> </td> <td> <p>镜像提供了运行实例所需的信息，阿里云提供多种镜像来源供您选择，支持的镜像请以页面中的可选情况为准。</p> </td> </tr> </tbody> </table>
3. 完成存储、带宽和安全组以及管理设置等配置项。

   各配置项详细说明，请参考[配置项说明](https://help.aliyun.com/document_detail/87190.html#a76e4b20ea11c)。
4. 在最终创建实例前，请在页面右侧检查实例的整体配置并配置使用时长等选项，确保各项配置符合您的要求。

5. 阅读并确认**《云服务器 ECS 服务条款》** 和**《云服务器ECS退订说明》** ，单击**确认下单**。

   **说明**

   仅购买包年包月实例时，才需要阅读并确认**《云服务器ECS退订说明》**。

   创建实例一般需要3\~5分钟，请您耐心等待。您可前往控制台的实例列表页面查看实例的状态，当实例状态变为**运行中**时，表示实例创建完成。

## 相关文档
创建一台或多台按量付费或者包年包月ECS实例：[RunInstances](https://help.aliyun.com/document_detail/63440.html#doc-api-Ecs-RunInstances)
