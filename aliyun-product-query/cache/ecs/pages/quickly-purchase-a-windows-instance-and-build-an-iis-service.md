从零开始，通过ECS 控制台购买一台 Windows 实例，搭建 IIS Web 服务，并验证访问是否正常。  

## **操作步骤**
请保证[账号已完成实名认证](https://help.aliyun.com/document_detail/37195.html)，且阿里云账户余额（即现金余额）与代金券的总额不低于100.00元人民币的情况下执行以下操作。  
**重要**

完成实名认证的云服务器ECS新用户，可免费试用ECS 3个月，详细限制参见[云服务器ECS试用攻略](https://help.aliyun.com/document_detail/2839344.html)。

### 步骤一：创建ECS实例

1. 访问[ECS控制台-实例](https://ecs.console.aliyun.com/server/region)，单击**创建实例**。

2. 选择**自定义购买**，完成购买配置。

   > 配置示例值可供参考，未提及配置项按照默认即可。
   <table> <thead> <tr> <td><p><b>配置项</b></p></td> <td><p><b>配置示例值</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p><b>付费类型</b></p></td> <td><p><b>按量付费</b></p></td> </tr> <tr> <td><p><b>地域</b></p></td> <td><p><span>华南2（河源）</span></p></td> </tr> <tr> <td><p><b>网络及可用区</b></p></td> <td><p>专有网络：默认专有网络</p><p>交换机：选择可用区B的默认交换机。</p></td> </tr> <tr> <td><p><b>实例</b></p></td> <td><p>ecs.c9i.large</p> <blockquote> 为保证流畅运行，建议实例规格不低于2 vCPU 4 GiB。 </blockquote></td> </tr> <tr> <td><p><b>镜像</b></p></td> <td><p>选择公共镜像下的 <span>Windows Server 2022 数据中心版 64位中文版。</span></p></td> </tr> <tr> <td><p><b>系统盘</b></p></td> <td><p>类型：ESSD 云盘</p><p>容量：40 GiB</p><p>性能：PL0</p></td> </tr> <tr> <td><p><b>公网IP</b></p></td> <td><p>勾选<b>分配公网 IPv4 地址</b>。</p></td> </tr> <tr> <td><p><b>带宽计费模式</b></p></td> <td><p><b>按使用流量</b></p> <blockquote> 建议 <b>升级至CDT计费</b>，升级后赠送220GB/月公网流量 （中国内地地域20GB/月，非中国内地200GB/月）。 </blockquote></td> </tr> <tr> <td><p><b>安全组</b></p></td> <td><p>选择<b>新建安全组</b>，在<b>普通安全组</b>的<b>开通IPv4端口/协议</b>处，新增勾选<b>HTTP (TCP：80)</b>，允许外部HTTP访问。</p></td> </tr> <tr> <td><p><b>登录凭证</b></p></td> <td><p>选择<b>自定义密码</b>，输入并确认密码。此密码用于远程连接实例。</p></td> </tr> </tbody> </table>
3. 确认配置费用，阅读并勾选服务协议，单击**确认下单**。

### 步骤二：连接ECS实例

1. 返回实例列表，待实例状态为**运行中** ，且**健康状态** 为**正常** 后，单击**操作** 列的**远程连接**。

2. 在对话框中，单击**通过Workbench远程连接** 对应的**立即登录**。

3. 选择**终端连接** ，输入购买时自定义的密码后，单击**登录**。

   > 远程连接会话最久维持6个小时，如果超过6小时没有任何操作，连接会自动断开，需要重新连接。

进入Windows桌面表示登录成功。

### 步骤三：部署 IIS 服务并验证访问

在实例上安装 IIS 服务，部署一个测试页面，从公网验证访问。

1. 在开始菜单中搜索并打开`Windows Powershell`。

2. 安装IIS服务。

   ```
   HELPCODEESCAPE-powershell
   Install-WindowsFeature -name Web-Server -IncludeAllSubFeature -IncludeManagementTools
   ```

   待安装进度到达100%，返回`Success`为`True`表示安装成功。
3. 创建测试页面。将自定义内容写入IIS默认站点目录。

   ```
   HELPCODEESCAPE-powershell
   Set-Content -Path "C:\inetpub\wwwroot\index.html" -Value "<html><body><h1>Hello from Alibaba Cloud ECS</h1></body></html>"
   ```

4. 在本地电脑的浏览器中访问`http://<ECS公网IP地址>/index.html`。

   > `<ECS公网IP地址>`可在实例列表的 **IP地址**列获取。

   页面显示"Hello from Alibaba Cloud ECS"，表示Web部署成功。

## 计费说明
### 计费项

* 系统盘容量费用：40 GiB（云盘容量） × 云盘单价 × 计费时长。

* 公网带宽计费（按流量计费）：出网流量 x 每 GB 流量单价。

  > [升级至CDT计费](https://help.aliyun.com/document_detail/2357716.html#5c4c3530f9bu4)后，将赠送220GB/月公网流量 （中国内地地域20GB/月，非中国内地200GB/月）。
* 实例规格的计算资源费用：实例规格单价 × 计费时长。

> 可通过[配置报价器](https://www.aliyun.com/price/cpq/?sheetId=2202605207553099534)查看价格明细。

### 获取费用明细

登录[费用与成本控制台](https://billing-cost.console.aliyun.com/home)，选择**账单** \> **账单详情**。在**产品名称**筛选框中选择产品名称云服务器ECS，获取费用明细。

## 资源清理
使用完毕后可释放实例，停止计费。  
**重要**

释放后数据不可恢复。

1. 在实例列表，单击目标实例**操作** 列下的**![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0466008571/p1006360.png)** \> **实例状态** \> **释放**。

2. 选择**立即释放** ，单击**下一步**。

3. 确认无**即将保留的关联资源** 信息后，单击**确认**。

## 相关文档
* 创建实例时的安全组配置默认允许所有IP访问，存在安全风险，建议[修改安全组规则](https://help.aliyun.com/document_detail/2973977.html#233050ea35twy)，仅保留必要IP的访问权限。

* [ECS常用操作导航](https://help.aliyun.com/document_detail/25429.html#concept-q3w-45w-wdb)

* 若实例规格无法满足应用需求，可以[变更实例规格](https://help.aliyun.com/document_detail/60051.html)。

* 在ECS中[搭建网站](https://help.aliyun.com/document_detail/151697.html)

* [IIS服务配置多站点](https://help.aliyun.com/document_detail/172508.html)

* [在Windows实例中通过IIS搭建PHP环境](https://help.aliyun.com/document_detail/40973.html)

* [Windows实例IIS Web网站访问故障](https://help.aliyun.com/document_detail/40900.html)
