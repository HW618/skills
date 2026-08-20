突发性能实例（t5/t6）支持性能约束模式和无性能约束模式，可以满足不同业务场景的需求。本文介绍如何查看和打开/关闭无性能约束模式。  

## 背景信息
* **性能约束模式**：突发性能实例的性能受CPU积分的约束，在初始CPU积分和CPU积分余额消耗完毕后，将无法超过基准性能。

* **无性能约束模式**：突发性能实例可以突破可用CPU积分的约束，通过透支或付费使用CPU积分在任意时间段保持高于基准性能的CPU使用率。

**重要**

在无性能约束模式下，突发性能实例可能产生额外费用。更多信息，请参见[额外费用](https://help.aliyun.com/document_detail/90581.html#section-lqi-vqf-dsc)。

在以下情况中，系统自动为突发性能实例选择性能模式：

* 创建突发性能实例时**默认使用性能约束模式**。

* 如果一台突发性能实例处于**已停止**状态，并且启用了节省停机模式，则该实例在启动后默认进入性能约束模式。

* 如果一台突发性能实例处于**已停止**状态，并且未启用节省停机模式，则该实例在启动后的性能模式与停机前保持一致。

* 如果您的账号欠费，突发性能实例将自动关闭无性能约束模式，待结清账单后再自动打开无性能约束模式。

## 查看性能模式
1. 访问[ECS控制台-实例](https://ecs.console.aliyun.com/server/region)。

2. 在页面左侧顶部，选择目标资源所在的资源组和地域。![地域](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5587314271/p680076.png)

3. **（可选）：** 如果**实例** 页面中未显示**无性能约束模式**列，则需要自定义列表项。

   1. 单击页面右上角的![自定义列表项](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4420748161/p96779.png)图标。

      ![自定义列表项入口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4425809661/p96781.png)
   2. 在**实例列表设置** 对话框的**未显示** 区域，单击**无性能约束模式** 右侧的![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192822071/p745842.png)图标，然后单击**继续**。

4. 在**无性能约束模式**列查看突发性能实例所处的模式。

   * **已关闭**：表示该实例处于性能约束模式。

   * **已开启**：表示该实例处于无性能约束模式。

## 打开无性能约束模式
当您的业务偶尔有突发高CPU使用率的场景时，您可以为该实例打开无性能约束模式。  
**说明**

请确保突发性能实例处于**运行中**状态，否则无法切换性能模式。

1. 登录[ECS管理控制台](https://ecs.console.aliyun.com)。

2. 在左侧导航栏，选择**实例与镜像** \> **实例**。

3. 找到处于性能约束模式的突发性能实例，选择一种方式打开无性能约束模式。

   * 一台突发性能实例：在**操作** 列，单击**![icon1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8834070661/p477856.png)** \> **实例属性** \> **打开无性能约束模式**。![打开性能](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7746043761/p549624.png)

   * 一台或多台突发性能实例：选中突发性能实例，在实例列表底部，选择**更多** \> **实例属性** \> **打开无性能约束模式**。

4. 在**打开无性能约束模式** 对话框中，选中**我已知晓以上费用风险** 。然后单击**确定** 。![打开性能确定](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9246043761/p549623.png)

## 关闭无性能约束模式
当当前实例的基准性能CPU已满足您的业务需求，您可以关闭该实例的无性能约束模式。  
**说明**

请确保突发性能实例处于**运行中**状态，否则无法切换性能模式。

1. 登录[ECS管理控制台](https://ecs.console.aliyun.com)。

2. 在左侧导航栏，选择**实例与镜像** \> **实例**。

3. 找到处于无性能约束模式的突发性能实例，选择一种方式关闭无性能约束模式。

   * 一台突发性能实例：在**操作** 列，单击**![icon1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8834070661/p477856.png)** \> **实例属性** \> **关闭无性能约束模式**。![关闭突发性能](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9246043761/p549617.png)

   * 一台或多台突发性能实例：选中突发性能实例，在实例列表底部，选择**更多** \> **实例属性** \> **关闭无性能约束模式**。

4. 在**关闭无性能约束模式** 对话框中，单击**确定** 。![关闭性能确定](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9246043761/p549620.png)

<br />

## 常见问题
### 如何查看CPU积分变化？

您可以在突发性能实例（t5/t6）的实例详情页，单击**监控** 页签，查看**已消耗CPU积分** 、**累积CPU积分** 、**超额CPU积分** 、**预支CPU积分** **。**

开启无性能约束模式后，部分情况下还需要支付额外费用。收取费用情况说明如下：

* 如果实例将预支CPU积分消耗完毕后，继续消耗了超额CPU积分。超额CPU积分按小时出账单并收取费用。

* 如果实例消耗了预支CPU积分，并在预支CPU积分恢复完毕前停止（节省停机模式）、变配或释放实例，或者切换到性能约束模式，则会一次性收取预支CPU积分的费用。

更多计费说明，请参见[突发性能实例计费](https://help.aliyun.com/document_detail/90581.html#section-lqi-vqf-dsc)。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192822071/p745994.png)

### 如何查看什么时间开启了无性能约束模式？

您可以在[云服务器ECS操作日志](https://ecs.console.aliyun.com/log/region/cn-hangzhou)页面，**操作名称** 选择**ModifyInstanceAttribute** ，然后单击具体事件的**查看详情**，操作详情中的CreditSpecification参数为Unlimited，表示已开启无性能约束模式。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192822071/p746015.png)
