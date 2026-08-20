为实现应用环境的批量部署或服务器的快速复制，可使用自定义或共享镜像直接创建ECS实例，以此简化配置流程，确保环境一致性并提高运维效率。  

## **地域限制**
待创建实例的地域必须与镜像所在地域一致。

## 操作步骤
## 控制台
1. 访问[ECS控制台-镜像](https://ecs.console.aliyun.com/image)，在页面左侧顶部，选择目标资源所在的资源组和地域。

2. 在**自定义镜像** 或**共享镜像** 页签找到待使用的自定义镜像，在**操作** 列中，单击**创建实例**。

3. 在自定义购买页，系统将自动填充地域与镜像信息，根据界面提示完成其他[配置项](https://help.aliyun.com/document_detail/87190.html#a76e4b20ea11c)后单击**确认下单**。

## CLI
在通过[RunInstances](https://help.aliyun.com/document_detail/2679677.html)或[CreateInstance](https://help.aliyun.com/document_detail/2679678.html)创建实例时，可通过配置`ImageId`为对应自定义镜像的ID。命令示例如下：
> 执行该命令后，会创建一台使用自定义镜像（ID为 `m-bp1******pi`）的实例。

```
HELPCODEESCAPE-shell
aliyun ecs RunInstances \
--region cn-hangzhou \
--RegionId 'cn-hangzhou' \
--ImageId 'm-bp1******pi' \
--InstanceType 'ecs.g7.large' \
--VSwitchId 'vsw-bp1******trg' \
--SecurityGroupId 'sg-bp1******dgl' \
--SystemDisk.Size 40 \
--SystemDisk.Category cloud_essd \
```

## API
在通过[RunInstances](https://help.aliyun.com/document_detail/2679677.html)或[CreateInstance](https://help.aliyun.com/document_detail/2679678.html)创建实例时，可配置`ImageId`为需要使用的自定义镜像的ID。

## 后续操作
* 若创建实例时增加了**数据盘** 的大小，实例创建成功后，必须登录ECS实例扩容分区和文件系统才能使新增的容量生效。[Linux实例指引](https://help.aliyun.com/document_detail/2949817.html#bb3b1f02e51pj)、[Windows实例指引](https://help.aliyun.com/document_detail/2932233.html#a9f9b78f3fujb)。

  > 增加了 **系统盘** 大小，系统盘会自动扩容，若自动扩容失败，需手动扩容分区和文件系统使新增的容量生效。 [Linux实例指引](https://help.aliyun.com/document_detail/2949817.html#bb3b1f02e51pj)、 [Windows实例指引](https://help.aliyun.com/document_detail/2932233.html#a9f9b78f3fujb)。
* 若创建实例时，手动添加了新数据盘，实例创建成功后，必须先[初始化](https://help.aliyun.com/document_detail/108498.html)该新数据盘才能正常使用。

## 计费说明
基于付费商业镜像制作的镜像创建ECS实例时会产生[额外费用](https://help.aliyun.com/document_detail/179021.html)。

## 常见问题
#### **自定义镜像不在当前账号或地域中，如何处理？**

<table> <thead> <tr> <td><p><b>场景</b></p></td> <td><p><b>解决方法</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>自定义镜像在本地设备上</p></td> <td><p>将本地镜像<a href="https://help.aliyun.com/document_detail/127285.html#concept-1375343">导入</a>为阿里云自定义镜像。</p></td> </tr> <tr> <td><p>自定义镜像在其他地域</p></td> <td><p>将自定义镜像<a href="https://help.aliyun.com/document_detail/25462.html#concept-a3m-5dm-xdb">复制</a>到需要创建实例的地域。</p></td> </tr> <tr> <td><p>自定义镜像在其他阿里云账号</p></td> <td><p>将自定义镜像<a href="https://help.aliyun.com/document_detail/25463.html#concept-e1j-jgm-xdb">共享</a>给需要创建实例的账号。</p></td> </tr> </tbody> </table>

#### **为什么创建ECS实例时看不到某些镜像（包括自定义镜像）？**

* **镜像与实例规格的特性不匹配** ：支持NVMe的实例规格只能选择支持NVMe的镜像，因此请确保镜像已安装NVMe驱动，并将镜像的**NVMe驱动** 属性[修改](https://help.aliyun.com/document_detail/25461.html#section-ssu-76z-kov)为**支持**，该镜像才会显示在镜像列表中；仅支持UEFI启动模式的实例规格只能选择UEFI版本的镜像，若为自定义镜像可更换镜像启动模式解决。

* **操作系统与实例规格处理器不兼容**：部分实例规格（如8代实例）对支持的操作系统有限制。

  * [AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#concept-2008303)

  * [Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)

  * [倚天处理器实例兼容的操作系统](https://help.aliyun.com/document_detail/463010.html)

* **Windows操作系统版本对CPU核数和内存大小有限制**：使用Windows镜像时，实例规格内存需大于等于1 GiB。内存低于1 GiB的实例只能选择Linux镜像。

* **Red Hat镜像只能匹配经过红帽官方认证的实例规格**。

* **部分裸金属、本地SSD型等实例对操作系统的驱动程序、内核有限制**：需选择与实例规格处理器匹配的镜像。

更多详情，请参见[为什么创建ECS实例时看不到某些镜像？](https://help.aliyun.com/document_detail/2834411.html)
