社区镜像是一种完全公开的镜像，您可以使用社区镜像快速部署与业务需求匹配的操作系统、应用程序和数据的ECS实例。本文介绍如何使用社区镜像创建ECS实例。  

## **前提条件**
* 在需要创建实例的账号和地域中已经有社区镜像。有关社区镜像的更多信息，请参见[社区镜像概述](https://help.aliyun.com/document_detail/208369.html)。

* 开通按量付费ECS资源时，您的阿里云账户余额（即现金余额）和代金券的总值不得小于100.00元人民币。具体充值操作，请参见[在线充值](https://help.aliyun.com/document_detail/112258.html)。

## 费用说明
* 社区镜像本质上是自定义镜像公开共享的镜像。如果该自定义镜像的最终来源为付费镜像，则使用社区镜像创建ECS实例时会收取镜像License费用。更多信息，请参见[镜像计费](https://help.aliyun.com/document_detail/179021.html)。

* 使用社区镜像创建ECS实例时，还需支付其他资源产生的费用，如vCPU、内存、存储、公网带宽和快照等。计费详情，请参见[计费概述](https://help.aliyun.com/document_detail/25398.html)。

## 方式一：在ECS实例购买页选择社区镜像
1. 前往[ECS实例创建页面](https://ecs-buy.aliyun.com/wizard/#/)。

2. 选择**自定义购买**页签。

3. 按需选择付费类型、地域、实例规格等配置。

   各配置项的详细说明，请参见[自定义购买实例](https://help.aliyun.com/document_detail/87190.html)。
4. 在镜像配置区域，选择**社区镜像** 页签，并单击**查看全部社区镜像**。

   页面会跳转至当前实例所在地域的社区镜像列表页面。
5. 在社区镜像列表页面，在搜索框输入关键词（例如CentOS），并单击![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2234474861/p673226.png)图标进行搜索。

6. 找到目标操作系统版本的社区镜像，将鼠标悬浮至镜像ID，然后单击![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2234474861/p673228.png)图标复制镜像ID。

7. 返回ECS购买页面，将镜像ID粘贴到填写镜像ID处，并选中镜像使用协议，继续购买ECS实例。

   **说明**
   * 仅在社区镜像的**发布者认证名称**为空，且第一次购买社区镜像时，需要签署社区镜像协议。

   * 如果输入社区镜像ID后，提示**社区镜像不存在或不支持选定的实例规格，请重新输入**，则有如下两种可能原因。此时请您尝试更换满足条件的镜像。

     * 社区镜像所在地域和您选择ECS购买的地域不一致。

     * 社区镜像和您选择的实例规格约束不匹配。

## 方式二：在社区镜像列表创建ECS实例
1. 访问[ECS控制台-镜像](https://ecs.console.aliyun.com/image)。

2. 在页面左侧顶部，选择目标资源所在的资源组和地域。

3. 在**镜像** 页面，选择**社区镜像**页签。

4. 在社区镜像列表页面，在搜索框输入关键词（例如CentOS），并单击![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2234474861/p673226.png)图标进行搜索。

5. 找到目标操作系统版本的社区镜像，在**操作** 列单击**创建实例**。

6. 在ECS购买页面，配置实例信息并完成实例创建。

   地域和社区镜像ID已自动填充，请根据业务需要配置其他信息。各配置项的详细说明，请参见[自定义购买实例](https://help.aliyun.com/document_detail/87190.html)。

## 相关文档
* 如果您在创建ECS实例时，添加了新的数据盘，数据盘必须初始化后才能正常使用。具体操作，请参见[初始化数据盘](https://help.aliyun.com/document_detail/108498.html)。

* 使用社区镜像创建ECS实例后，如果当前使用的社区镜像不能满足业务需求，您可以为ECS实例更换新的操作系统。具体操作，请参见[更换操作系统（更换系统盘）](https://help.aliyun.com/document_detail/25436.html)。

* 有关社区镜像的镜像族系说明，请参见[镜像族系概述](https://help.aliyun.com/document_detail/174241.html)。
