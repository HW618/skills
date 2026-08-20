突发性能实例是一种面向入门级计算场景，应对突发性能需求的经济型实例规格。其可以利用CPU积分应对突发性能需求，支持打开无性能约束模式，最小实例规格的内存可以低至0.5 GiB，本文主要介绍如何创建突发性能实例。  
**说明**

本文重点介绍在ECS管理控制台上创建突发性能实例时需要特别注意的基础配置项，如果您想了解其他通用配置，请参见[自定义购买实例](https://help.aliyun.com/document_detail/87190.html#task-vwq-5g4-r2b)。

## 操作步骤
1. 前往[实例购买页](https://ecs-buy.aliyun.com/wizard/#/)。

2. 按需选择付费类型、实例规格及镜像等配置。

   <table> <thead> <tr> <td><p><b>配置项</b></p></td> <td><p><b>说明</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p><b>付费类型</b></p></td> <td><p>付费类型影响实例的计费和收费规则，不同付费类型的实例遵循的资源状态变化规则也存在差异。取值范围：</p> <ul> <li><p><a href="https://help.aliyun.com/document_detail/56220.html#subs-china">包年包月</a></p></li> <li><p><a href="https://help.aliyun.com/document_detail/40653.html#Pay-As-You-Go">按量付费</a></p></li> <li><p><a href="https://help.aliyun.com/document_detail/178880.html#concept-1936192">抢占式实例</a></p></li> </ul></td> </tr> <tr> <td><p><b>地域</b></p></td> <td><p>指数据中心所在的地理区域，选择距离近的地域可以降低网络时延，实例创建完成后不支持更改地域。更多信息，请参见<a href="https://help.aliyun.com/document_detail/40654.html#concept-2459516">地域和可用区</a>。</p></td> </tr> <tr> <td><p><b>网络及可用区</b></p></td> <td> <ul> <li><p>推荐您使用专有网络，专有网络之间逻辑上彻底隔离，安全性更高，且支持弹性公网IP（EIP）、弹性网卡、IPv6等功能。</p></li> <li><p>可用区是指在同一地域内，电力和网络互相独立的物理区域。同一可用区内实例之间的网络延时更小，其用户访问速度更快。</p></li> </ul></td> </tr> <tr> <td><p><b>实例</b></p></td> <td><p>选择<b>全部规格</b>页签，在<b>架构</b>行的<b>X86 计算</b>列单击<b>全部分类</b>，选择<b>共享型</b>，选择对应突发性能实例。可选的实例规格与地域等因素有关，您可以前往<span><a href="https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion">ECS实例可购买地域</a></span>查看实例的可购情况。关于突发性能实例规格的更多信息，请参见<a href="https://help.aliyun.com/document_detail/25378.html#concept-sx4-lxv-tdb">实例规格族</a>。</p><p>您可以在创建突发性能实例时选中<b>打开突发性能实例无性能约束模式</b>，也可以在创建后打开无性能约束模式。具体操作，请参见<a href="https://help.aliyun.com/document_detail/90634.html#section-cds-zh0-eh7">打开无性能约束模式</a>。</p></td> </tr> <tr> <td><p><b>镜像</b></p></td> <td><p>镜像提供了运行实例所需的信息，阿里云提供多种镜像来源供您选择，支持的镜像请以页面中的可选情况为准。更多信息，请参见<a href="https://help.aliyun.com/document_detail/111486.html#concept-h44-kwj-dhb">选择镜像</a>。</p></td> </tr> </tbody> </table>
3. 完成存储、带宽和安全组以及管理设置等配置项。

   各配置项详细说明，请参考[配置项说明](https://help.aliyun.com/document_detail/87190.html#a76e4b20ea11c)。
4. 在最终创建实例前，请在页面右侧检查实例的整体配置并配置使用时长等选项，确保各项配置符合您的要求。

5. 阅读并签署《云服务器ECS服务条款》等服务协议（若已签署，则无需重复签署，请以页面提示为准），然后单击**确认下单**。

   **说明**

   购买包年包月实例时，需要阅读并确认《云服务器ECS退订说明》。

   创建实例一般需要3\~5分钟，请您耐心等待。您可前往控制台的实例列表页面查看实例的状态，当实例状态变为**运行中**时，表示实例创建完成。

## 相关文档
创建一台或多台按量付费或者包年包月ECS实例：[RunInstances](https://help.aliyun.com/document_detail/63440.html#doc-api-Ecs-RunInstances)

<br />
