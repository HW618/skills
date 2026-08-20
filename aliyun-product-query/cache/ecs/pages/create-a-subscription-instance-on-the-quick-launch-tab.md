快速购买提供了四种配置多种套餐的实例规格。您可以在几分钟内，以最简单的方式购买一个ECS实例，提高配置效率。本文介绍如何快速购买ECS实例。  
**重要**

如果您刚接触ECS不久，想要快速上手购买并使用ECS实例，我们为您准备了一个较简单的示例，请参见[控制台购买 Windows 实例并搭建 IIS Web服务](https://help.aliyun.com/document_detail/2851432.html)，它将帮助您更直观地理解整个流程。在初步了解ECS后，您可以通过阅读本文，了解快速购买实例时更加详细的配置说明。

## 前提条件
* 注册中国站阿里云账号，并完成实名认证。具体操作，请参见[阿里云账号注册流程](https://help.aliyun.com/document_detail/37195.html)。

* 开通按量付费ECS资源时，您的阿里云账户余额（即现金余额）和代金券的总值不得小于100.00元人民币。具体充值操作，请参见[在线充值](https://help.aliyun.com/document_detail/112258.html)。

## 默认配置
快速购买ECS实例时，为了减少配置参数时间，部分参数由系统自动分配。默认分配的参数如下表所示。
<table> <thead> <tr> <td><p><b>参数</b></p></td> <td><p><b>默认配置</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>可用区</p></td> <td><p>系统随机分配，不能修改。</p></td> </tr> <tr> <td><p>网络类型</p></td> <td><p>默认专有网络，不能修改。更多信息，请参见<a href="https://help.aliyun.com/document_detail/65402.html">默认专有网络和交换机</a>。</p></td> </tr> <tr> <td><p>安全组</p></td> <td><p>默认安全组，实例创建后可修改，具体操作，请参见<a href="https://help.aliyun.com/document_detail/25443.html">为实例（主网卡）关联安全组</a>。</p></td> </tr> <tr> <td><p>专有网络</p></td> <td><p>默认专有网络交换机，更多信息，请参见<a href="https://help.aliyun.com/document_detail/65402.html">默认专有网络和交换机</a>。</p></td> </tr> <tr> <td><p>密码</p></td> <td><p>无密码，您需要在实例创建成功后重置密码，具体操作，请参见<a href="https://help.aliyun.com/document_detail/25439.html">重置实例登录密码</a>。</p></td> </tr> <tr> <td><p>实例名称</p></td> <td><p>系统命名，实例创建后可修改。</p></td> </tr> </tbody> </table>

## 操作步骤
1. 前往[实例购买页](https://ecs-buy.aliyun.com/wizard/#/)。

2. 在实例创建页，单击左上角的**快速购买** 页签。

   <br />

3. 根据界面提示，配置ECS实例参数。

   <table> <thead> <tr> <td><p><b>参数</b></p></td> <td><p><b>说明</b></p></td> <td><p><b>示例</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p><b>实例规格</b></p></td> <td><p>实例规格包括CPU型号、核数和内存大小，以套餐的形式提供，包含基础配置、标准配置、专业配置和增强配置四个套餐。</p></td> <td><p>基础配置（2vCPU 2GiB）</p></td> </tr> <tr> <td><p><b>镜像</b></p></td> <td><p>纯净的操作系统镜像，提供了运行实例所需的信息，快速购买支持Alibaba Cloud Linux、CentOS、Windows Server、Ubuntu四种操作系统。快速购买不支持选择自定义镜像或云市场镜像，如需更多镜像，可前往<a href="https://ecs-buy.aliyun.com/ecs#/custom/prepay/">自定义购买</a>。</p> <blockquote> 已购买的实例可以通过 <a href="https://help.aliyun.com/document_detail/25436.html">更换操作系统（更换系统盘）</a>的方式更换为目标镜像。 </blockquote></td> <td><p>Alibaba Cloud Linux 3.2104 LTS 64位</p></td> </tr> <tr> <td><p><b>预装应用</b></p></td> <td><p>支持基于不同的操作系统，安装预装应用。实例启动后，安装预装应用需耗时3-5分钟。</p></td> <td><p>按需选择</p></td> </tr> <tr> <td><p><b>付费类型</b></p></td> <td> <ul> <li><p><b>包年包月</b>：先付费再使用，适用于长期稳定的业务，例如Web服务。</p></li> <li><p><b>按量付费</b>：先使用再付费，适用于有大幅波动的场景，例如临时扩展、临时测试、科学计算。</p> <div> <div> <i></i> </div> <div> <strong>重要 </strong> <p>当您不再使用按量付费实例时，请尽快释放实例，否则ECS资源会持续扣费。</p> </div> </div></li> </ul></td> <td><p>包年包月</p></td> </tr> <tr> <td><p><b>地域</b></p></td> <td><p>选择距离近的地域可以降低网络时延，实例创建完成后不支持更改地域和可用区。更多信息，请参见<a href="https://help.aliyun.com/document_detail/40654.html">地域和可用区</a>。</p></td> <td><p>华东1（杭州）</p></td> </tr> <tr> <td><p><b>公网IP</b></p></td> <td><p>如果实例需要进行公网通信，必须分配公网IP。</p></td> <td><p>选中分配公网IPv4地址</p></td> </tr> <tr> <td><p><b>带宽计费模式</b></p></td> <td> <ul> <li><p><b>按固定带宽</b>：按您选择的带宽值计费，实际的出网带宽不会高于指定的带宽值，适用于对网络带宽有稳定要求的场景。</p></li> <li><p><b>按使用流量</b>：按实际使用的流量计费，适用于对网络带宽要求变化大的场景。为避免产生高额的带宽流量费，可先设置出网带宽峰值。</p><p><b>（可选）：</b>选中<b>升级至CDT计费</b>。CDT以灵活计费、提供免费流量、阶梯价格优惠及多产品统一计费等优势，为公网带宽费用管理提供高效经济的解决方案。相对于按量付费，有一定的折扣优惠。更多信息，请参见<a href="https://help.aliyun.com/document_detail/2357716.html">什么是云数据传输CDT</a>。</p> <div> <div> <i></i> </div> <div> <strong>重要 </strong> <ul> <li> <p>自2024年12月12日0时起，您无需额外操作即可直接使用云数据传输（CDT），享受高效服务。</p> </li> <li> <p>升级为CDT计费后，所有存量和新增的按流量计费实例将通过CDT统一计费和出账，按带宽计费的实例继续在原来的云产品上统计费用和出账。您可以前往费用与成本，在账单详情页面查看CDT的账单情况。</p> </li> <li> <p>开通CDT即可获得 220 GB/月公网流量免费额度，<span>其中20 GB/月可用于<b>中国内地地域</b>，200 GB/月可用于<b>非中国内地地域</b>。</span></p> </li> </ul> </div> </div></li> </ul></td> <td><p>按固定带宽</p></td> </tr> <tr> <td><p><b>带宽值/带宽峰值</b></p></td> <td><p>选择<b>按固定带宽</b>的<b>带宽值</b>或<b>按使用流量</b>的<b>带宽峰值</b>，实际的出网带宽不会高于指定的<b>带宽值/带宽峰值</b>。</p></td> <td><p>1 Mbps</p></td> </tr> <tr> <td><p><b>购买实例数量</b></p></td> <td><p>购买实例的数量。</p></td> <td><p>1</p></td> </tr> <tr> <td><p><b>购买时长</b></p></td> <td><p>购买实例的使用时长。</p><p><b>付费类型</b>为<b>包年包月</b>时，需配置此参数。</p></td> <td><p>1个月</p></td> </tr> <tr> <td><p><b>自动续费</b></p></td> <td><p>自动续费可以减少手动续费的管理成本，避免因忘记手动续费而导致ECS实例服务中断。</p><p><b>付费类型</b>为<b>包年包月</b>时，才能选择此参数。</p></td> <td><p>选中启用自动续费</p></td> </tr> </tbody> </table>
4. 在页面右侧的**配置概要** 面板，确认选择的实例配置，并阅读页面底部的《**产品服务协议** 》和《**服务等级协议** 》，如无疑问，单击**确认下单**。

## 后续步骤
快速购买不支持设置实例登录凭证，创建实例成功后，您可以在ECS管理控制台重置密码。具体操作，请参见[重置实例登录密码](https://help.aliyun.com/document_detail/25439.html)。
