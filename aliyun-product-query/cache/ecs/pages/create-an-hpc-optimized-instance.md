高性能计算优化型实例（简称HPC优化实例）是专为提升HPC工作负载性能，同时优化大规模运行成本而打造的最具性价比的实例。  

## 操作步骤
1. 前往[实例购买页](https://ecs-buy.aliyun.com/wizard/#/)。

2. 按需选择付费类型、实例规格及镜像等配置。

   此处重点介绍创建高性能计算优化实例时需要特别注意的基础配置项。如果您想了解其他通用配置，请参见[自定义购买实例](https://help.aliyun.com/document_detail/87190.html#task-vwq-5g4-r2b)。
   <table> <thead> <tr> <td> <p><b>配置项</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>付费类型</b></p> </td> <td> <p>高性能计算优化型实例仅支持按量付费，您也可以使用节省计划来抵扣按量付费账单。不同计费方式的区别，请参见<a href="https://help.aliyun.com/document_detail/25370.html#billingMethod-china">计费方式概述</a>。</p> </td> </tr> <tr> <td> <p><b>地域</b></p> </td> <td> <p>指数据中心所在的地理区域，选择距离近的地域可以降低网络时延，实例创建完成后不支持更改地域。更多信息，请参见<a href="https://help.aliyun.com/document_detail/40654.html#concept-2459516">地域和可用区</a>。</p> </td> </tr> <tr> <td> <p><b>网络及可用区</b></p> </td> <td> <ul> <li> <p>推荐您使用专有网络，专有网络之间逻辑上彻底隔离，安全性更高，且支持弹性公网IP（EIP）、弹性网卡、IPv6等功能。</p> </li> <li> <p>可用区是指在同一地域内，电力和网络互相独立的物理区域。同一可用区内实例之间的网络延时更小，其用户访问速度更快。</p> </li> </ul> </td> </tr> <tr> <td> <p><b>实例</b></p> </td> <td> <p>选择<b>全部规格</b>页签，在<b>高性能计算</b>列单击<b>全部分类</b>，选择<b>高性能计算优化型</b>。更多信息，请参见<a href="https://help.aliyun.com/document_detail/25378.html#concept-sx4-lxv-tdb">实例规格族</a>。</p> <div> <div> <i></i> </div> <div> <strong>说明 </strong> <p>可选的实例规格与地域等因素有关，您可以前往<a href="https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion">ECS实例可购买地域</a>查看实例的可购情况。</p> </div> </div> </td> </tr> <tr> <td> <p><b>镜像</b></p> </td> <td> <p>镜像提供了运行实例所需的信息，阿里云提供多种镜像来源供您选择，支持的镜像请以页面中的可选情况为准。</p> </td> </tr> </tbody> </table>
3. 完成**存储** 、**带宽和安全组** 以及**管理设置**等配置项。

   各配置项详细说明，请参考[配置项说明](https://help.aliyun.com/document_detail/87190.html#a76e4b20ea11c)。
4. 在最终创建实例前，请在页面右侧检查实例的整体配置并配置使用时长等选项，确保各项配置符合您的要求。

5. 阅读并签署《云服务器ECS服务条款》等服务协议（若已签署，则无需重复签署，请以页面提示为准），然后单击**确认下单**。

   创建实例一般需要3\~5分钟，请您耐心等待。您可前往控制台的实例列表页面查看实例的状态，当实例状态变为**运行中**时，表示实例创建完成。

## 相关文档
创建一台或多台按量付费或者包年包月ECS实例：[RunInstances](https://help.aliyun.com/document_detail/63440.html#doc-api-Ecs-RunInstances)

<br />
