弹性裸金属服务器适合上云部署传统非虚拟化场景的应用，通过与阿里云产品家族中的其他产品（例如存储、网络、数据库等）无缝对接，可以更多元化地结合您的业务场景进行资源构建。本文介绍云服务器ECS弹性裸金属服务器实例规格族的优势和特点，并列出了具体的实例规格。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

* 推荐规格族：

  <table> <thead> <tr> <td> <p><b>通用型（ebmg）</b></p> </td> <td> <p><b>计算型（ebmc）</b></p> </td> <td> <p><b>内存型（ebmr）</b></p> </td> <td> <p><b>高主频型（ebmhf）</b></p> </td> <td> <p><b>GPU计算型（ebmgn）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li> <p><a href="#ebmg9ae">通用型弹性裸金属服务器实例规格族ebmg9ae</a></p> </li> <li> <p><a href="#ebmg9a">通用型弹性裸金属服务器实例规格族ebmg9a</a></p> </li> <li> <p><a href="#ebmg9i">通用型弹性裸金属服务器实例规格族ebmg9i</a></p> </li> <li> <p><a href="#ebmg8a">通用型弹性裸金属服务器实例规格族ebmg8a</a></p> </li> <li> <p><a href="#ebmg8y">通用型弹性裸金属服务器实例规格族ebmg8y</a></p> </li> <li> <p><a href="#ebmg8i">通用型弹性裸金属服务器实例规格族ebmg8i</a></p> </li> <li> <p><a href="#ebmg7se">存储增强型弹性裸金属服务器实例规格族ebmg7se</a></p> </li> <li> <p><a href="#section-yrg-v9v-sbl">通用型弹性裸金属服务器实例规格族ebmg7</a></p> </li> <li> <p><a href="#section-sic-hrt-8mc">通用型弹性裸金属服务器实例规格族ebmg7a</a></p> </li> <li> <p><a href="#section-vk4-ake-dah">通用型弹性裸金属服务器实例规格族ebmg6a</a></p> </li> <li> <p><a href="#section-69g-hx0-psw">通用型（平衡增强）弹性裸金属服务器实例规格族ebmg6e</a></p> </li> <li> <p><a href="#section-qkb-ez6-9c5">通用型弹性裸金属服务器实例规格族ebmg6</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#ebmc9ae">计算型弹性裸金属服务器实例规格族ebmc9ae</a></p> </li> <li> <p><a href="#ebmc9i">计算型弹性裸金属服务器实例规格族ebmc9i</a></p> </li> <li> <p><a href="#ebmc8a">计算型弹性裸金属服务器实例规格族ebmc8a</a></p> </li> <li> <p><a href="#ebmc8y">计算型弹性裸金属服务器实例规格族ebmc8y</a></p> </li> <li> <p><a href="#ebmc8i">计算型弹性裸金属服务器实例规格族ebmc8i</a></p> </li> <li> <p><a href="#section-r40-6zy-4ht">计算型弹性裸金属服务器实例规格族ebmc7</a></p> </li> <li> <p><a href="#section-r3x-f34-xvy">计算型弹性裸金属服务器实例规格族ebmc7a</a></p> </li> <li> <p><a href="#ebmc6me">计算型弹性裸金属服务器实例规格族ebmc6me</a></p> </li> <li> <p><a href="#section-m8p-b2e-yqq">计算型弹性裸金属服务器实例规格族ebmc6a</a></p> </li> <li> <p><a href="#section-mdc-24m-q3e">计算型（平衡增强）弹性裸金属服务器实例规格族ebmc6e</a></p> </li> <li> <p><a href="#section-zec-q52-xn9">计算型弹性裸金属服务器实例规格族ebmc6</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#ebmr9ae">内存型弹性裸金属服务器实例规格族ebmr9ae</a></p> </li> <li> <p><a href="#ebmr9i">内存型弹性裸金属服务器实例规格族ebmr9i</a></p> </li> <li> <p><a href="#ebmr8a">内存型弹性裸金属服务器实例规格族ebmr8a</a></p> </li> <li> <p><a href="#ebmr8y">内存型弹性裸金属服务器实例规格族ebmr8y</a></p> </li> <li> <p><a href="#section-lyd-sd1-iuv">内存型弹性裸金属服务器实例规格族ebmr7</a></p> </li> <li> <p><a href="#section-fiw-22f-fpk">内存型弹性裸金属服务器实例规格族ebmr7a</a></p> </li> <li> <p><a href="#section-qwd-bje-kuu">内存型弹性裸金属服务器实例规格族ebmr6a</a></p> </li> <li> <p><a href="#section-ltv-trm-b0o">内存型（平衡增强）弹性裸金属服务器实例规格族ebmr6e</a></p> </li> <li> <p><a href="#section-yv1-t65-log">内存型弹性裸金属服务器实例规格族ebmr6</a></p> </li> <li> <p><a href="#ebmre7p">持久内存型弹性裸金属服务器实例规格族ebmre7p</a></p> </li> <li> <p><a href="#section-xli-oah-7tq">持久内存型弹性裸金属服务器实例规格族ebmre6p</a></p> </li> <li> <p><a href="#section-6kk-g42-kgh">内存增强型弹性裸金属服务器实例规格族ebmre6-6t</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#section-w8p-4nu-o5m">高主频通用型弹性裸金属服务器实例规格族ebmhfg7</a></p> </li> <li> <p><a href="#section-44h-4rq-5bd">高主频计算型弹性裸金属服务器实例规格族ebmhfc7</a></p> </li> <li> <p><a href="#section-1ja-58l-yiv">高主频内存型弹性裸金属服务器实例规格族ebmhfr7</a></p> </li> <li> <p><a href="#section-czp-w4q-mb8">高主频通用型弹性裸金属服务器实例规格族ebmhfg6</a></p> </li> <li> <p><a href="#section-s0v-ihb-z5x">高主频计算型弹性裸金属服务器实例规格族ebmhfc6</a></p> </li> <li> <p><a href="#section-sns-ot8-a1r">高主频内存型弹性裸金属服务器实例规格族ebmhfr6</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#ebmgn9g">GPU计算型弹性裸金属服务器实例规格族ebmgn9g</a></p> </li> <li> <p><a href="#ebmgn9ge">GPU计算型弹性裸金属服务器实例规格族ebmgn9ge</a></p> </li> <li> <p><a href="#ebmgn9gc">GPU计算型弹性裸金属服务器实例规格族ebmgn9gc</a></p> </li> <li> <p><a href="#ebmgn8v">GPU计算型弹性裸金属服务器实例规格族ebmgn8v</a></p> </li> <li> <p><a href="#ebmgn8ia">GPU计算型弹性裸金属服务器实例规格族ebmgn8ia</a></p> </li> <li> <p><a href="#ebmgn8is">GPU计算型弹性裸金属服务器实例规格族ebmgn8is</a></p> </li> <li> <p><a href="#ebmgn7ex">GPU计算型弹性裸金属服务器实例规格族ebmgn7ex</a></p> </li> <li> <p><a href="#section-w3a-unf-ttk">GPU计算型弹性裸金属服务器实例规格族ebmgn7e</a></p> </li> <li> <p><a href="#section-kh7-gh5-lzu">GPU计算型弹性裸金属服务器实例规格族ebmgn7ix</a></p> </li> <li> <p><a href="#ebmgn7i">GPU计算型弹性裸金属服务器实例规格族ebmgn7i</a></p> </li> <li> <p><a href="#section-71m-cxy-5ct">GPU计算型弹性裸金属服务器实例规格族ebmgn7</a></p> </li> <li> <p><a href="#section-xyl-5bo-wez">GPU计算型弹性裸金属服务器实例规格族ebmgn6e</a></p> </li> <li> <p><a href="#section-lke-80h-kzu">GPU计算型弹性裸金属服务器实例规格族ebmgn6v</a></p> </li> <li> <p><a href="#section-slz-oyd-k1t">GPU计算型弹性裸金属服务器实例规格族ebmgn6i</a></p> </li> </ul> </td> </tr> </tbody> </table>

<!-- -->

* 不推荐（如果售罄，建议使用推荐规格族）

  * [通用网络增强型弹性裸金属服务器实例规格族ebmg5s](#section-qiz-xda-sce)

  * [通用型弹性裸金属服务器实例规格族ebmg5](#section-nii-o5k-4t2)

  * [计算网络增强型弹性裸金属服务器实例规格族ebmc5s](#section-pnq-v2c-u07)

  * [内存网络增强型弹性裸金属服务器实例规格族ebmr5s](#section-v7p-ot4-f4n)

## 弹性裸金属服务器介绍
弹性裸金属服务器（ECS Bare Metal Instance）是基于阿里云完全自主研发的下一代虚拟化技术而打造的新型计算类服务器产品，兼具虚拟机的弹性和物理机的性能及功能特性。与上一代虚拟化技术相比，下一代虚拟化技术不仅保留了普通云服务器的弹性体验，而且保留了物理机的性能与特性，全面支持嵌套虚拟化技术。  
**说明**

弹性裸金属服务器二次虚拟化能力默认开启。

弹性裸金属服务器融合了物理机与云服务器的优势，实现超强超稳的计算能力。通过阿里云自主研发的虚拟化2.0技术 ，您的业务应用可以直接访问弹性裸金属服务器的处理器和内存，无任何虚拟化开销。弹性裸金属服务器具备物理机级别的完整处理器特性（例如Intel VT-x），以及物理机级别的资源隔离优势，特别适合上云部署传统非虚拟化场景的应用。

弹性裸金属服务器是阿里云通过自研芯片、自研Hypervisor系统以及重新定义服务器硬件架构等软硬件技术打造的深度融合了物理机和虚拟机特性的创新型计算产品。弹性裸金属服务器开创了一种新型的云服务器形式，它能与阿里云产品家族中的其他产品（例如存储、网络、数据库等）无缝对接，并完全兼容ECS云服务器实例的镜像系统，从而可更多元化地结合您的业务场景进行资源构建。  
使用弹性裸金属服务器时，请注意：

* 不支持规格变配。

* 当弹性裸金属服务器发生硬件故障时，支持故障转移，数据都保留在云盘中。

* 暂无法获取EBM弹性裸金属实例的CPU基础监控信息，您可通过安装云监控插件获取CPU监控信息。具体操作，请参见[安装云监控插件](https://help.aliyun.com/document_detail/183482.html)。

## 产品优势
弹性裸金属服务器通过技术创新实现客户价值。具体而言，弹性裸金属服务器具有以下优势：

* 用户独占计算资源

  作为一款云端弹性计算类产品，弹性裸金属服务器具备了物理机级的性能和隔离性。您可以独占计算资源，并且没有虚拟化性能开销和特性损失。在CPU规格选择上支持80核、96核、104核、128核、192核等多个规格实例。
* 加密计算

  在安全性方面，弹性裸金属服务器除了具备物理隔离特性外，为了更好地保障您云上数据的安全性，弹性裸金属服务器采用了芯片级可信执行环境（Intel ^®^ SGX），能确保加密数据只能在安全可信的环境中计算。芯片级的硬件安全保障相当于为您云上的数据提供了一个保险箱功能，您可以自己掌控数据加密和密钥保护的全部流程。详情请参见[安装SGX](https://help.aliyun.com/document_detail/208095.html#section-utn-xc1-656)。
* 兼容多种专有云

  弹性裸金属服务器可以进一步解决您对高性能计算的强需求，更好地帮助您搭建新型混合云。弹性裸金属服务器不仅具有虚拟机的灵活性和弹性，同时具备物理机的一切特性和优势，因此也具备再次虚拟化的能力，线下的私有云均可无缝平移到阿里云上，而不用担心嵌套虚拟化带来的性能开销，为您上云提供一种新途径。
* 异构指令集处理器支持

  弹性裸金属服务器采用阿里云完全自主研发的虚拟化2.0技术，支持ARM等其他指令集处理器。

## 机型对比
相比同配置的物理机，弹性裸金属服务器的性能大幅提升。在双十一大促中，弹性裸金属服务器提供了数百万vCPU计算能力，顺利承载双十一流量洪峰。

弹性裸金属服务器与物理机、虚拟机的对比如下表所示。其中，Y表示支持，N表示不支持，N/A表示无数据。
<table> <thead> <tr> <td> <p><b>功能分类</b></p> </td> <td> <p><b>功能</b></p> </td> <td> <p><b>弹性裸金属服务器</b></p> </td> <td> <p><b>物理机</b></p> </td> <td> <p><b>虚拟机</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>运维自动化</p> </td> <td> <p>分钟级交付</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>计算</p> </td> <td> <p>免性能损失</p> </td> <td> <p>Y</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> </tr> <tr> <td> <p>免特性损失</p> </td> <td> <p>Y</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> </tr> <tr> <td> <p>免资源争抢</p> </td> <td> <p>Y</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> </tr> <tr> <td> <p>存储</p> </td> <td> <p>完全兼容ECS云盘系统</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>使用云盘（系统盘）启动</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>系统盘快速重置</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>使用云服务器ECS的镜像</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>物理机和虚拟机之间相互冷迁移</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>免操作系统安装</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>免本地RAID，提供更高云盘数据保护</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>网络</p> </td> <td> <p>完全兼容专有网络VPC</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>物理机集群和虚拟机集群间VPC无通信瓶颈</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>管控</p> </td> <td> <p>完全兼容ECS现有管控系统</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>VNC等用户体验和虚拟机保持一致</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>Y</p> </td> </tr> <tr> <td> <p>带外网络安全</p> </td> <td> <p>Y</p> </td> <td> <p>N</p> </td> <td> <p>N/A</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg9ae
* **规格族介绍** ：采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC^™^ Turin 处理器，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高3.7 GHz，采用物理核设计，计算性能稳定。

* **存储**：

  * 支持调整存储基础带宽。

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持调整网络基础带宽。

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmg9ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg9ae.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>600万</p> </td> <td> <p>64</p> </td> <td> <p>38</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>60万</p> </td> <td> <p>50/无</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg9a
* **规格族介绍** ：采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC^™^ Turin 处理器，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高4.1 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmg9a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg9a.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>1152</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>600万</p> </td> <td> <p>64</p> </td> <td> <p>38</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>50万</p> </td> <td> <p>64/无</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg9i
* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmg9i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg9i.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>600万</p> </td> <td> <p>64（主网卡）/16（辅助网卡）</p> </td> <td> <p>32</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>50万/80万</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg8a
* **规格族介绍** ：采用阿里云全新CIPU架构，搭配AMD EPYC^™^ Genoa 处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：AMD EPYC^™^ Genoa处理器，睿频最高3.7 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

ebmg8a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg8a.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>64/无</p> </td> <td> <p>1800万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>38</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg8y
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频点播、直播场景。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 数据分析和计算。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器：采用阿里云自研倚天710 ARM架构CPU，主频不低于2.75 GHz，无超线程，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmg8y包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg8y.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>300万</p> </td> <td> <p>64（主网卡）/32（辅助网卡）</p> </td> <td> <p>38</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg8i
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

    **说明**

    购买该实例时，系统将随机分配上述两种处理器之一，不支持手动选择。
  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmg8i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg8i.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1024</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>400万</p> </td> <td> <p>64（主网卡）/16（辅助网卡）</p> </td> <td> <p>72</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>100万/无</p> </td> <td> <p>48/无</p> </td> </tr> </tbody> </table>

## 存储增强型弹性裸金属服务器实例规格族ebmg7se
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 需要支持云盘多重挂载功能的高可用工作负载。

  * I/O密集型业务场景，例如中大型OLTP类核心数据库、中大型NoSQL数据库。

  * 搜索、实时日志分析。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.9 GHz主频的Intel^®^ Xeon^®^ Platinum 8369B（Ice Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 单实例顺序读写性能最高可达64 Gbit/s，IOPS最高可达100万。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，1200万PPS网络收发包能力。

ebmg7se包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>最大挂载数据盘数量</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg7se.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>32</p> </td> <td> <p>1200万</p> </td> <td> <p>240万</p> </td> <td> <p>16</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>32</p> </td> <td> <p>100万</p> </td> <td> <p>64</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg7
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求

  * 容器（包括但不限于Docker、Clear Container、Pouch等）

  * 高网络包收发场景，例如视频弹幕、电信业务转发等

  * 各种类型和规模的企业级应用

  * 网站和应用服务器

  * 游戏服务器

  * 中小型数据库系统、缓存、搜索集群

  * 数据分析和计算

  * 高性能科学和工程应用

* **计算**：

  * 处理器与内存配比为1:4

  * 处理器：2.9 GHz主频的Intel^®^ Xeon^®^Platinum 8369B（Ice Lake），全核睿频3.5 GHz

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmg7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg7.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>240万</p> </td> <td> <p>32</p> </td> <td> <p>20</p> </td> <td> <p>20</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg7a
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* 适用场景：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 计算集群、依赖内存的数据处理。

  * 视频编解码、渲染等。

  * 数据分析和计算。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.55 GHz主频的AMD EPYC™ MILAN处理器，单核睿频最高3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmg7a包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg7a.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>1024</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>400万</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

* 基于该实例规格的ECS实例，所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请保证该自定义镜像的启动模式已经设置为UEFI模式。设置自定义镜像启动模式的具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

* Ubuntu 18或Debian 9操作系统内核不支持AMD EPYC^TM^ MILAN处理器，因此当您选用该实例规格后，请勿搭配Ubuntu 18或Debian 9镜像创建实例，否则实例会启动失败。

## 通用型弹性裸金属服务器实例规格族ebmg6a
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频编解码、渲染等。

  * 计算集群、依赖内存的数据处理。

  * 数据分析和计算。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.6 GHz主频的AMD EPYC^™^ROME处理器，睿频3.3 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmg6a包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg6a.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>1024</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

基于该实例规格族的ECS实例，所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请保证该自定义镜像的启动模式已经设置为UEFI模式。设置自定义镜像启动模式的具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

## 通用型（平衡增强）弹性裸金属服务器实例规格族ebmg6e
ebmg6e的特点如下：

* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比约为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.2 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmg6e包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg6e.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>384</p> </td> <td> <p>32</p> </td> <td> <p>2400万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>48万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg6
ebmg6的特点如下：

* **规格族介绍**：提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频编解码、渲染等。

  * 中大型企业等重量级数据库应用。

  * 计算集群、依赖内存的数据处理。

  * 数据分析和计算。

* **计算**：

  * 处理器与内存配比约为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.2 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，600万PPS网络收发包能力。

ebmg6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg6.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>384</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>  
**说明**

暂无法获取EBM弹性裸金属实例的CPU基础监控信息，您可通过安装云监控插件获取CPU监控信息。具体操作，请参见[安装云监控插件](https://help.aliyun.com/document_detail/183482.html)。

## 计算型弹性裸金属服务器实例规格族ebmc9ae
* **规格族介绍** ：采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC^™^ Turin 处理器，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高3.7 GHz，采用物理核设计，计算性能稳定。

* **存储**：

  * 支持调整存储基础带宽。

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持调整网络基础带宽。

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmc9ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc9ae.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>384</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>600万</p> </td> <td> <p>64</p> </td> <td> <p>38</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>60万</p> </td> <td> <p>50/无</p> </td> </tr> </tbody> </table>

## 计算型弹性裸金属服务器实例规格族ebmc9i
* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmc9i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc9i.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>384</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>600万</p> </td> <td> <p>64（主网卡）/16（辅助网卡）</p> </td> <td> <p>32</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>50万/80万</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmc8a
* **规格族介绍** ：采用阿里云全新CIPU架构，搭配AMD EPYC^™^ Genoa 处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：AMD EPYC^™^ Genoa处理器，睿频最高3.7 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

ebmc8a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc8a.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>384</p> </td> <td> <p>64/无</p> </td> <td> <p>1800万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>38</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 计算型弹性裸金属服务器实例规格族ebmc8y
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频点播、直播场景。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 数据分析和计算。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器：采用阿里云自研倚天710 ARM架构CPU，主频不低于2.75 GHz，无超线程，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmc8y包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc8y.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>256</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>300万</p> </td> <td> <p>64（主网卡）/32（辅助网卡）</p> </td> <td> <p>38</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 计算型弹性裸金属服务器实例规格族ebmc8i
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

    **说明**

    购买该实例时，系统将随机分配上述两种处理器之一，不支持手动选择。
  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmc8i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc8i.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>512</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>400万</p> </td> <td> <p>64（主网卡）/16（辅助网卡）</p> </td> <td> <p>72</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>100万/无</p> </td> <td> <p>48/无</p> </td> </tr> </tbody> </table>

## 计算型弹性裸金属服务器实例规格族ebmc7
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.9 GHz主频的Intel^®^ Xeon^®^Platinum 8369B（Ice Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmc7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc7.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>256</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>240万</p> </td> <td> <p>32</p> </td> <td> <p>20</p> </td> <td> <p>20</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 计算型弹性裸金属服务器实例规格族ebmc7a
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频编解码、渲染等。

  * 数据分析和计算。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.55 GHz主频的AMD EPYC^TM^ MILAN处理器，单核睿频最高3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmc7a包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc7a.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>512</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>400万</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

* 基于该实例规格的ECS实例，所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请保证该自定义镜像的启动模式已经设置为UEFI模式。设置自定义镜像启动模式的具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

* Ubuntu 18或Debian 9操作系统内核不支持AMD EPYC MILAN处理器，因此当您选用该实例规格后，请勿搭配Ubuntu 18或Debian 9镜像创建实例，否则实例会启动失败。

## 计算型弹性裸金属服务器实例规格族ebmc6me
* **规格族介绍：**提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频编解码、渲染等。

  * 大型多人在线游戏（MMO）前端。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比约为1:3

  * 处理器：2.3 GHz主频的Intel ^®^ Xeon ^®^ Gold 5218（Cascade Lake），睿频3.9 GHz

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，600万PPS网络收发包能力。

ebmc6me包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc6me.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>192</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 计算型弹性裸金属服务器实例规格族ebmc6a
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频编解码、渲染等。

  * 数据分析和计算。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.6 GHz主频的AMD EPYC^TM^ ROME处理器，睿频3.3 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmc6a包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc6a.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>512</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

基于该实例规格族的ECS实例，所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请保证该自定义镜像的启动模式已经设置为UEFI模式。设置自定义镜像启动模式的具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

## 计算型（平衡增强）弹性裸金属服务器实例规格族ebmc6e
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比约为1:2。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.2 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmc6e包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc6e.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>192</p> </td> <td> <p>32</p> </td> <td> <p>2400万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>48万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 计算型弹性裸金属服务器实例规格族ebmc6
* **规格族介绍：**提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频编解码、渲染等。

  * 大型多人在线游戏（MMO）前端。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比约为1:2。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.2 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，600万PPS网络收发包能力。

ebmc6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc6.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>192</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 内存型弹性裸金属服务器实例规格族ebmr9ae
* **规格族介绍** ：采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC^™^ Turin 处理器，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高3.7 GHz，采用物理核设计，计算性能稳定。

* **存储**：

  * 支持调整存储基础带宽。

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持调整网络基础带宽。

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmr9ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr9ae.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1536</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>600万</p> </td> <td> <p>64</p> </td> <td> <p>38</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>60万</p> </td> <td> <p>50/无</p> </td> </tr> </tbody> </table>

## 内存型弹性裸金属服务器实例规格族ebmr9i
* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmr9i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr9i.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1536</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>600万</p> </td> <td> <p>64（主网卡）/16（辅助网卡）</p> </td> <td> <p>32</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>50万/80万</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmr8a
* **规格族介绍** ：采用阿里云全新CIPU架构，搭配AMD EPYC^™^ Genoa 处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：AMD EPYC^™^ Genoa处理器，睿频最高3.7 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

ebmr8a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr8a.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1536</p> </td> <td> <p>64/无</p> </td> <td> <p>1800万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>38</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 内存型弹性裸金属服务器实例规格族ebmr8y
**说明**

如需使用ebmr8y，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。  
* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频点播、直播场景。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 数据分析和计算。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器：采用阿里云自研倚天710 ARM架构CPU，主频不低于2.75 GHz，无超线程，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

ebmr8y包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr8y.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>300万</p> </td> <td> <p>64（主网卡）/32（辅助网卡）</p> </td> <td> <p>38</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

## 内存型弹性裸金属服务器实例规格族ebmr7
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：2.9 GHz主频的Intel^®^ Xeon^®^Platinum 8369B（Ice Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmr7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr7.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>240万</p> </td> <td> <p>32</p> </td> <td> <p>20</p> </td> <td> <p>20</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 内存型弹性裸金属服务器实例规格族ebmr7a
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业级大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8

  * 处理器：2.55 GHz主频的AMD EPYC^TM^ MILAN处理器，单核睿频最高3.5 GHz，计算性能稳定

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmr7a包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr7a.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>2048</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>400万</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

* 基于该实例规格的ECS实例，所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请保证该自定义镜像的启动模式已经设置为UEFI模式。设置自定义镜像启动模式的具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

* Ubuntu 18或Debian 9操作系统内核不支持AMD EPYC^TM^ MILAN处理器，因此当您选用该实例规格后，请勿搭配Ubuntu 18或Debian 9镜像创建实例，否则实例会启动失败。

## 内存型弹性裸金属服务器实例规格族ebmr6a
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业级大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8

  * 处理器：2.6 GHz主频的AMD EPYC^TM^ ROME处理器，睿频3.3 GHz，计算性能稳定

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmr6a包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr6a.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>2048</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

基于该实例规格族的ECS实例，所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请保证该自定义镜像的启动模式已经设置为UEFI模式。设置自定义镜像启动模式的具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

## 内存型（平衡增强）弹性裸金属服务器实例规格族ebmr6e
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比约为1:8。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.2 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmr6e包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr6e.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>768</p> </td> <td> <p>32</p> </td> <td> <p>2400万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>48万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 内存型弹性裸金属服务器实例规格族ebmr6
* **规格族介绍：**提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用**。**

* **计算**：

  * 处理器与内存配比约为1:8。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.2 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，600万PPS网络收发包能力。

ebmr6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr6.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>768</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 持久内存型弹性裸金属服务器实例规格族ebmre7p
* **规格族介绍：**提供专属硬件资源和物理隔离。

* **适用场景**：

  * 内存型数据库，例如Redis。

  * 高性能数据库，例如SAP HANA。

  * 其他内存密集型应用，例如AI应用、智能搜索应用。

* **计算**：

  * 采用Intel ^®^傲腾 ^TM^持久内存，针对Redis应用进行了全链路优化，性价比超高。

  * 最大支持2560 GiB内存（512 GiB DRAM内存+2048 GiB Intel ^®^傲腾 ^TM^持久内存），CPU与内存配比接近1:20，满足内存密集型应用的需求。

  * 处理器：采用第三代Intel^®^Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，2400万PPS网络收发包能力。

ebmre7p包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>持久内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmre7p.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>2048</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 持久内存型弹性裸金属服务器实例规格族ebmre6p
如需使用ebmre6p，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。  
* **规格族介绍：**提供专属硬件资源和物理隔离。

* **适用场景**：

  * 内存型数据库，例如Redis。

  * 高性能数据库，例如SAP HANA。

  * 其他内存密集型应用，例如AI应用、智能搜索应用。

* **计算**：

  * 采用Intel ^®^傲腾 ^TM^持久内存，针对Redis应用进行了全链路优化，性价比超高。

  * 最大支持1920 GiB内存（384 GiB DRAM内存+1536 GiB Intel^®^ 傲腾^TM^持久内存），CPU与内存配比接近1:20，满足内存密集型应用的需求。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.2 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，600万PPS网络收发包能力。

ebmre6p包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>持久内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmre6p.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>384</p> </td> <td> <p>1536</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>31</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 内存增强型弹性裸金属服务器实例规格族ebmre6-6t
如需使用ebmre6-6t，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。  
* **规格族介绍：**提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 高性能数据库、内存数据库（例如SAP HANA）。

  * 内存密集型应用。

  * 大数据处理引擎（例如Apache Spark、Presto）。

* **计算**：

  * 处理器与内存配比约为1:30。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269（Cascade Lake），全核睿频3.2 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，600万PPS网络收发包能力。

ebmre6-6t包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmre6-6t.52xlarge</p> </td> <td> <p>208</p> </td> <td> <p>6144</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 高主频通用型弹性裸金属服务器实例规格族ebmhfg7
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 高性能科学计算。

  * 视频编码应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：第三代Intel^®^ Xeon^®^可扩展处理器（Cooper Lake架构），基频不低于3.3 GHz，全核睿频3.8 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmhfg7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmhfg7.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 高主频计算型弹性裸金属服务器实例规格族ebmhfc7
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能前端服务器集群。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：第三代Intel ^®^ Xeon ^®^可扩展处理器（Cooper Lake架构），基频不低于3.3 GHz，全核睿频3.8 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmhfc7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmhfc7.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>384</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 高主频内存型弹性裸金属服务器实例规格族ebmhfr7
* **规格族介绍：**

  * 依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。

  * 提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：第三代Intel^®^ Xeon^®^可扩展处理器（Cooper Lake架构），基频不低于3.3 GHz，全核睿频3.8 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmhfr7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmhfr7.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1536</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

## 高主频通用型弹性裸金属服务器实例规格族ebmhfg6
* **规格族介绍**：提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 中大型企业等重量级数据库应用。

  * 视频编解码、渲染等。

* **计算**：

  * 处理器与内存配比为1:4.8。

  * 处理器：3.1 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，600万PPS网络收发包能力。

ebmhfg6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmhfg6.20xlarge</p> </td> <td> <p>80</p> </td> <td> <p>384</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 高主频计算型弹性裸金属服务器实例规格族ebmhfc6
* **规格族介绍**：提供专属硬件资源和物理隔离。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频编解码、渲染等**。**

* **计算**：

  * 处理器与内存配比为1:2.4

  * 处理器：3.1 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.5 GHz

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，600万PPS网络收发包能力。

ebmhfc6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmhfc6.20xlarge</p> </td> <td> <p>80</p> </td> <td> <p>192</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 高主频内存型弹性裸金属服务器实例规格族ebmhfr6
* **规格族介绍**：提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:9.6。

  * 处理器：3.1 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，600万PPS网络收发包能力。

ebmhfr6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmhfr6.20xlarge</p> </td> <td> <p>80</p> </td> <td> <p>768</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## GPU计算型弹性裸金属服务器实例规格族ebmgn9g
**重要**

ebmgn9g正在邀测中，如需使用，请提交工单申请。

* **规格族介绍：**ebmgn9g是阿里云推出的第9代全功能高性价比GPU裸金属实例。采用最新一代CIPU2.0提供云服务能力，搭配高主频CPU，大容量内存和全新Blackwell架构专业显卡，为自动驾驶/具身智能训练，大模型推理，影视动漫渲染，元宇宙/云游戏服务等各类GPU加速场景提供高性价比的GPU云服务能力。

* **适用场景及产品特色：**

  * **自动驾驶/具身智能：**   
    提供256vCPU，CPU全核最高工作于4.2GHz以上，搭配2.3T大容量内存，支撑自动驾驶/具身智能训练中的数据处理业务需求。  

  * **搜索推荐：**   
    搭配的Blackwell GPU提供123T高性能TF32算力，平均每张GPU搭配32vCPU和153GB/s内存带宽，为搜索，广告业务提供最佳的配置组合。  

  * **大模型推理：**   
    全新一代GPU提供超越8代的全新算力，显存带宽提升至1344GB/s，新支持FP4算力全面提升推理性能和性价比。8张GPU基于PCIe Gen5互联，带宽达到128GB/s，多卡并行推理效率大大提升。  

  * **云游戏/渲染/元宇宙：**   
    CPU最高可达5GHz高主频，是3D建模的顶级选择，GPU原生支持图形能力，提供通过专业设计认证的工作站级图形驱动，支持OpenGL全功能加速，是高端影视动漫开发，CAD设计的最优选择。  

* **采用最新的CIPU 2.0云处理器：**

  第2代CIPU提供更高的云处理算力，提供更强的eRDMA，VPC，EBS组件算力。裸金属实例可直接访问物理资源，或者需要License绑定硬件等要求的工作负载。支持容器（包括但不限于Docker、Clear Container、Pouch等）。
* **计算：**

  * 采用全新Blackwell架构专业显卡：

    * 支持OpenGL 专业级图形处理功能

    * 支持RTX、TensorRT等常用加速功能，全新升级支持FP4和PCIe Gen5互联。

    * 采用PCIe Switch互联，相比直连CPU方案，其NCCL性能提升36%，多卡分片大模型推理时，性能最大提升9%。

  * GPU主要参数：

    <table> <thead> <tr> <td> <p><b>GPU架构</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>计算性能</b></p> </td> <td> <p><b>视频编解码能力</b></p> </td> <td> <p><b>卡间互联</b></p> </td> <td> <p><b>加速APIs</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>Blackwell</p> </td> <td> <ul> <li> <p>容量：48 GB</p> </li> <li> <p>带宽：1344GB/s</p> </li> </ul> </td> <td> <ul> <li> <p>TF32: 123 TFLOPS</p> </li> <li> <p>FP32:\&nbsp;52 TFLOPS</p> </li> <li> <p>FP16/BF16:\&nbsp;261 TFLOPS</p> </li> <li> <p>FP8/INT8:\&nbsp;533 TFLOPS</p> </li> <li> <p>FP4: 970 TFLOPS</p> </li> <li> <p>RT core: 196 TFLOPS</p> </li> </ul> </td> <td> <ul> <li> <p>3 \* Video Encoder</p> </li> <li> <p>3 \* Video Decoder</p> </li> </ul> </td> <td> <ul> <li> <p>PCIe Gen5 x16: 128GB/s</p> </li> <li> <p>支持P2P</p> </li> </ul> </td> <td> <p>支持DX12、</p> <p>OpenGL4.6、Vulkan1.3、CUDA12.8、Open CL3.0、DirectCompute</p> </td> </tr> </tbody> </table>
  * **处理器**：3.3GHz-5GHz主频的 AMD Turin-C 处理器，全核最高可达4.2GHz。

* 存储：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* 网络：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，3000万PPS网络收发包能力。

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至360 Gbit/s，可用于自动驾驶，具身智能，CV和传统模型的训练业务。

    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。

ebmgn9g包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列（主网卡/辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>最大挂载数据盘数</b></p> </td> <td> <p><b>云盘最大带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn9g.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>2304</p> </td> <td> <p>48GB \* 8</p> </td> <td> <p>360（180 \* 2）</p> </td> <td> <p>3000万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>64/16</p> </td> <td> <p>38</p> </td> <td> <p>33</p> </td> <td> <p>8</p> </td> </tr> </tbody> </table>  
**说明**

ebmgn9g实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html)。

## GPU计算型弹性裸金属服务器实例规格族ebmgn9ge
**重要**

ebmgn9ge正在邀测中，如需使用，请提交工单申请。

* **规格族介绍：**ebmgn9ge是阿里云推出的第9代全功能高性价比GPU裸金属实例。采用最新一代CIPU2.0提供云服务能力，搭配高主频CPU，大容量内存和全新Blackwell架构专业显卡，为自动驾驶/具身智能训练，大模型推理，影视动漫渲染，元宇宙/云游戏服务等各类GPU加速场景提供高性价比的GPU云服务能力。

* **适用场景及产品特色：**

  * **自动驾驶/具身智能：**   
    提供256vCPU，CPU全核最高工作于4.2GHz以上，搭配2.3T大容量内存，支撑自动驾驶/具身智能训练中的数据处理业务需求。  

  * **搜索推荐：**   
    搭配的Blackwell GPU提供126T高性能TF32算力，平均每张GPU搭配32vCPU和153GB/s内存带宽，为搜索，广告业务提供最佳的配置组合。  

  * **大模型推理：**

    ebmgn9ge专为大语言模型提供单卡72G大显存算力，同时显存带宽达到1344GB/s，为LLM场景提供高性能推理算力，配合全新FP4计算架构，和128GB/s的第5代PCIe带宽，可以支持8卡并行671B以上的大模型推理。
  * **云游戏/渲染/元宇宙：**   
    CPU最高可达5GHz高主频，是3D建模的顶级选择，GPU原生支持图形能力，提供通过专业设计认证的工作站级图形驱动，支持OpenGL全功能加速，是高端影视动漫开发，CAD设计的最优选择。  

* **采用最新的CIPU 2.0云处理器：**

  第2代CIPU提供更高的云处理算力，提供更强的eRDMA、VPC、EBS组件算力。裸金属实例可直接访问物理资源，或者需要License绑定硬件等要求的工作负载。支持容器（包括但不限于Docker、Clear Container、Pouch等）。
* **计算：**

  * 采用全新Blackwell架构专业显卡：

    * 支持OpenGL 专业级图形处理功能

    * 支持RTX、TensorRT等常用加速功能，全新升级支持FP4和PCIe Gen5互联。

    * 采用PCIe Switch互联，相比直连CPU方案，其NCCL性能提升36%，多卡分片大模型推理时，性能最大提升9%。

  * GPU主要参数：

    <table> <thead> <tr> <td> <p><b>GPU架构</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>计算性能</b></p> </td> <td> <p><b>视频编解码能力</b></p> </td> <td> <p><b>卡间互联</b></p> </td> <td> <p><b>加速APIs</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>Blackwell</p> </td> <td> <ul> <li> <p>容量：72 GB</p> </li> <li> <p>带宽：1344GB/s</p> </li> </ul> </td> <td> <ul> <li> <p>TF32: 126 TFLOPS</p> </li> <li> <p>FP32:\&nbsp;52 TFLOPS</p> </li> <li> <p>FP16/BF16:\&nbsp;266 TFLOPS</p> </li> <li> <p>FP8/INT8:\&nbsp;530 TFLOPS</p> </li> <li> <p>FP4: 971 TFLOPS</p> </li> <li> <p>RT core: 196 TFLOPS</p> </li> </ul> </td> <td> <ul> <li> <p>3 \* Video Encoder</p> </li> <li> <p>3 \* Video Decoder</p> </li> </ul> </td> <td> <ul> <li> <p>PCIe Gen5 x16: 128GB/s</p> </li> <li> <p>支持P2P</p> </li> </ul> </td> <td> <p>支持DX12、</p> <p>OpenGL4.6、Vulkan1.3、CUDA12.8、Open CL3.0、DirectCompute</p> </td> </tr> </tbody> </table>
  * **处理器**：3.3GHz-5GHz主频的 AMD Turin-C 处理器，全核最高可达4.2GHz。

* 存储：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* 网络：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，3000万PPS网络收发包能力。

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至360 Gbit/s，可用于自动驾驶，具身智能，CV和传统模型的训练业务。

    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。

ebmgn9ge包括的实例规格及指标数据如下表所示。  
**说明**

如需更小内存的低成本版本，可选用[ebmgn9gc](https://help.aliyun.com/document_detail/25378.html#ebmgn9gc)。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列（主网卡/辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>最大挂载数据盘数</b></p> </td> <td> <p><b>云盘最大带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn9ge.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>2304</p> </td> <td> <p>72GB \* 8</p> </td> <td> <p>360（180 \* 2）</p> </td> <td> <p>3000万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>64/16</p> </td> <td> <p>38</p> </td> <td> <p>33</p> </td> <td> <p>8</p> </td> </tr> </tbody> </table>  
**说明**

ebmgn9ge实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html)。

## GPU计算型弹性裸金属服务器实例规格族ebmgn9gc
**重要**

ebmgn9gc正在邀测中，如需使用，请提交工单申请。

* **规格族介绍：**ebmgn9gc是阿里云推出的第9代全功能高性价比GPU裸金属实例。采用最新一代CIPU2.0提供云服务能力，搭配高主频CPU，大容量内存和全新Blackwell架构专业显卡，为自动驾驶/具身智能训练，大模型推理，影视动漫渲染，元宇宙/云游戏服务等各类GPU加速场景提供高性价比的GPU云服务能力。

* **适用场景及产品特色：**

  * **自动驾驶/具身智能：**   
    提供256vCPU，CPU主频3.3-5GHz，全核基本可稳定在4.2GHz以上，搭配1.5T大容量内存，支撑自动驾驶/具身智能训练中的数据处理业务需求。  

  * **搜索推荐：**   
    搭配的Blackwell GPU提供126T高性能TF32算力，平均每张GPU搭配32vCPU和153GB/s内存带宽，为搜索，广告业务提供最佳的配置组合。  

  * **大模型推理：**

    ebmgn9gc专为大语言模型提供单卡72G大显存算力，同时显存带宽达到1344GB/s，为LLM场景提供高性能推理算力，配合全新FP4计算架构，和128GB/s的第5代PCIe带宽，可以支持8卡并行671B以上的大模型推理。
  * **云游戏/渲染/元宇宙：**   
    CPU最高可达5GHz高主频，是3D建模的顶级选择，GPU原生支持图形能力，提供通过专业设计认证的工作站级图形驱动，支持OpenGL全功能加速，是高端影视动漫开发，CAD设计的最优选择。  

* **采用最新的CIPU 2.0云处理器：**

  第2代CIPU提供更高的云处理算力，提供更强的eRDMA、VPC、EBS组件算力。裸金属实例可直接访问物理资源，或者需要License绑定硬件等要求的工作负载。支持容器（包括但不限于Docker、Clear Container、Pouch等）。
* **计算：**

  * 采用全新Blackwell架构专业显卡：

    * 支持OpenGL 专业级图形处理功能

    * 支持RTX、TensorRT等常用加速功能，全新升级支持FP4和PCIe Gen5互联。

    * 采用PCIe Switch互联，相比直连CPU方案，其NCCL性能提升36%，多卡分片大模型推理时，性能最大提升9%。

  * GPU主要参数：

    <table> <thead> <tr> <td> <p><b>GPU架构</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>计算性能</b></p> </td> <td> <p><b>视频编解码能力</b></p> </td> <td> <p><b>卡间互联</b></p> </td> <td> <p><b>加速APIs</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>Blackwell</p> </td> <td> <ul> <li> <p>容量：72 GB</p> </li> <li> <p>带宽：1344GB/s</p> </li> </ul> </td> <td> <ul> <li> <p>TF32: 126 TFLOPS</p> </li> <li> <p>FP32:\&nbsp;52 TFLOPS</p> </li> <li> <p>FP16/BF16:\&nbsp;266 TFLOPS</p> </li> <li> <p>FP8/INT8:\&nbsp;530 TFLOPS</p> </li> <li> <p>FP4: 971 TFLOPS</p> </li> <li> <p>RT core: 196 TFLOPS</p> </li> </ul> </td> <td> <ul> <li> <p>3 \* Video Encoder</p> </li> <li> <p>3 \* Video Decoder</p> </li> </ul> </td> <td> <ul> <li> <p>PCIe Gen5 x16: 128GB/s</p> </li> <li> <p>支持P2P</p> </li> </ul> </td> <td> <p>支持DX12、</p> <p>OpenGL4.6、Vulkan1.3、CUDA12.8、Open CL3.0、DirectCompute</p> </td> </tr> </tbody> </table>
  * **处理器**：3.3GHz-5GHz主频的 AMD Turin-C 处理器，全核最高可达4.2GHz。

* 存储：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* 网络：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，3000万PPS网络收发包能力。

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至360 Gbit/s，可用于自动驾驶，具身智能，CV和传统模型的训练业务。

    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。

ebmgn9gc包括的实例规格及指标数据如下表所示。  
**说明**

如需更大内存的版本，可选用[ebmgn9ge](https://help.aliyun.com/document_detail/25378.html#ebmgn9ge)。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列（主网卡/辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>最大挂载数据盘数</b></p> </td> <td> <p><b>云盘最大带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn9gc.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>1536</p> </td> <td> <p>72GB \* 8</p> </td> <td> <p>360（180 \* 2）</p> </td> <td> <p>3000万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>64/16</p> </td> <td> <p>38</p> </td> <td> <p>33</p> </td> <td> <p>8</p> </td> </tr> </tbody> </table>  
**说明**

ebmgn9gc实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html)。

## GPU计算型弹性裸金属服务器实例规格族ebmgn8v
该实例目前仅支持海外等部分地域，如有需求，请联系阿里云销售人员。

* **规格族介绍：**ebmgn8v是阿里云为AI模型训练和超大参数量模型推出的第8代加速计算规格族（弹性裸金属实例规格族），每个实例是1台采用了8个GPU卡裸金属主机。

* **适用场景**：

  * 对于70 B以上的LLM模型，进行多卡并行推理计算时性价比较高。

  * 单个GPU提供39.5 TFLOPS FP32算力，在传统AI模型训练和自动驾驶训练业务中性能突出。

  * 8卡之间支持NVLINK互联，适用于中小模型训练场景。

* **产品特色及定位：**

  * **高速\&大容量显存**：每个GPU配备了96 GB容量的HBM3显存，显存带宽达到4 TB/s，大幅加快了模型训练和推理速度。

  * **高卡间带宽**：多GPU卡之间通过900 GB/s NVLINK互联，多卡训练和推理的效率远超过历代GPU产品。

  * **大模型量化技术**：支持FP8算力，对大规模参数训练和推理过程的算力进行优化，大幅提升训练和推理的计算速度，降低显存占用。

* **计算**：

  * 采用最新的CIPU 1.0云处理器：

    * 具有解耦计算和存储能力，可以灵活选择所需存储资源。相对于第七代GPU实例，该实例规格的机器间带宽提升至160 Gbit/s，可以更快地完成数据传输和处理。

    * CIPU提供裸金属能力，相对于传统虚拟化实例，可以支持GPU实例之间的P2P通信。

  * 采用Intel第4代Xeon可扩展处理，提供192个vCPU，全核睿频可达3.1 GHz。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，3000万PPS网络收发包能力。

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至160 Gbit/s，可用于CV和传统模型的训练业务。

    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。

ebmgn8v包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列（主网卡\&amp;辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>最大挂载数据盘数</b></p> </td> <td> <p><b>云盘最大带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn8v.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1024</p> </td> <td> <p>96GB\*8</p> </td> <td> <p>170（85 \* 2）</p> </td> <td> <p>3000万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>64</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>6</p> </td> </tr> </tbody> </table>  
**说明**

ebmgn8V实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

## GPU计算型弹性裸金属服务器实例规格族ebmgn8ia
该实例目前仅支持海外等部分地域，如有需求，请联系阿里云销售人员。

* **规格族介绍：**ebmgn8ia是阿里云针对搜索推荐、仿真和其他GPU计算稀疏类（平均每颗GPU需要配备比较多的vCPU资源）业务的发展推出的第8代加速计算规格族（弹性裸金属实例规格族），采用最新NVIDIA L20 GPU，每个实例为一台采用了2颗高主频CPU和4个GPU计算卡的裸金属主机。

* **产品特色及适用场景：**

  * **高主频**：该产品配置了2颗AMD EPYC™ Genoa 9T34处理器，每颗处理有64个物理核，整机提供256个vCPU，主频高达3.4-3.75GHz。大幅提高CPU单核性能，适用于CAD建模，并提升CAE仿真的前期预处理速度。

  * **稀疏资源配比**：平均GPU配置了64 vCPU和384 GiB内存，平均每个GPU的内存带宽达到230 GB/s, 适合高I/O吞吐的GPU计算场景，如广告、搜索、推荐以及传统CAE仿真，部分采用CPU渲染的影视制作等。

* **采用最新的CIPU 1.0云处理器：**

  * 具有解耦计算和存储能力，可以灵活选择所需存储资源。相对于上一代，该实例规格的机器间带宽提升至160 Gbit/s，可以更快地完成数据传输和处理。

  * CIPU提供裸金属能力，相对于传统虚拟化实例，可以支持GPU实例之间的PCIe P2P通信。

* **计算：**

  * 采用全新NVIDIA L20企业级GPU：

    * 支持vGPU、RTX、TensorRT等常用加速功能。

    * 支持FP8精度，提升计算效率。

  * NVIDIA L20主要参数：

    <table> <thead> <tr> <td> <p><b>GPU架构</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>计算性能</b></p> </td> <td> <p><b>视频编解码能力</b></p> </td> <td> <p><b>卡间互联</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>NVIDIA Ada Lovelace</p> </td> <td> <ul> <li> <p><b>容量：</b>48 GB</p> </li> <li> <p><b>带宽：</b>864 GB/s</p> </li> </ul> </td> <td> <ul> <li> <p><b>FP64: </b>N/A</p> </li> <li> <p><b>FP32: </b>59.3 TFLOPS</p> </li> <li> <p><b>FP16/BF16:</b> 119 TFLOPS</p> </li> <li> <p><b>FP8/INT8: </b>237 TFLOPS</p> </li> </ul> </td> <td> <ul> <li> <p>3 \* Video Encoder（+AV1）</p> </li> <li> <p>3 \* Video Decoder</p> </li> <li> <p>4 \* JPEG Decoder</p> </li> </ul> </td> <td> <ul> <li> <p>PCIe接口：PCIe Gen4 x16</p> </li> <li> <p>带宽：64 GB/s</p> </li> </ul> </td> </tr> </tbody> </table>
  * 处理器：3.4 GHz\~3.75 GHz的AMD EPYC™ Genoa 9T34处理器。

* **存储：**

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，3000万PPS网络收发包能力。

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至160 Gbit/s，可用于CV和传统模型的训练业务。

    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。

ebmgn8ia包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列（主网卡/辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>最大挂载数据盘数</b></p> </td> <td> <p><b>云盘最大带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn8ia.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>1536</p> </td> <td> <p>L20 \* 4</p> </td> <td> <p>48GB\*4</p> </td> <td> <p>160（80 \* 2）</p> </td> <td> <p>3000万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>64/16</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>6</p> </td> </tr> </tbody> </table>  
**说明**

ebmgn8ia实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

## GPU计算型弹性裸金属服务器实例规格族ebmgn8is
该实例目前仅支持海外等部分地域，如有需求，请联系阿里云销售人员。

* **规格族介绍：**ebmgn8is是阿里云针对近期AI生成业务的发展推出的第8代加速计算规格族（弹性裸金属实例规格族），采用最新NVIDIA L20 GPU，每个实例为一台采用了8个GPU计算卡的裸金属主机。

* **产品特色及定位：**

  * **图形处理**：该产品采用Intel第4代Xeon Scalable高主频处理器，在3D建模场景，为您提供足够的CPU算力支撑，使得图形的渲染和设计更加顺畅。

  * **推理任务**：采用全新NVIDIA L20，单卡配置48 GB显存来加速推理任务，支持FP8浮点数格式，搭配ACK容器可灵活支持各类AIGC模型的推理，尤其适用于70 B以下LLM模型的推理任务。

  * **训练任务**：该实例提供高性价比的计算能力，FP32计算性能相比7代推理实例提升1倍，特别适用于基于FP32开发的CV类模型和其他各类中小模型的训练。

* **适用场景：**

  * 结合云市场的GRID镜像使用GRID图形驱动，启动OpenGL和Direct3D图形能力，提供工作站级图形处理能力，适用于动漫、影视特效制作和渲染

  * 结合ACK容器化管理能力，更高效、低成本地支撑AIGC图形生成和LLM大模型推理（最大支持130 B）

  * 其他通用AI识别场景、图像识别、语音识别等

* **采用最新的CIPU 1.0云处理器：**

  * 具有解耦计算和存储能力，可以灵活选择所需存储资源。相对于上一代，该实例规格的机器间带宽提升至160 Gbit/s，可以更快地完成数据传输和处理。

  * CIPU提供裸金属能力，相对于传统虚拟化实例，可以支持GPU实例之间的PCIE P2P通信。

* **计算：**

  * 采用全新NVIDIA L20企业级GPU：

    * 支持vGPU、RTX、TensorRT等常用加速功能。

    * 采用PCIe Switch互联，相比直连CPU方案，其NCCL性能提升36％，多卡分片推理大模型时，推理性能最大提升9%。

  * NVIDIA L20主要参数：

    <table> <thead> <tr> <td> <p><b>GPU架构</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>计算性能</b></p> </td> <td> <p><b>视频编解码能力</b></p> </td> <td> <p><b>卡间互联</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>NVIDIA Ada Lovelace</p> </td> <td> <ul> <li> <p><b>容量：</b>48 GB</p> </li> <li> <p><b>带宽：</b>864 GB/s</p> </li> </ul> </td> <td> <ul> <li> <p><b>FP64: </b>N/A</p> </li> <li> <p><b>FP32: </b>59.3 TFLOPS</p> </li> <li> <p><b>FP16/BF16:</b> 119 TFLOPS</p> </li> <li> <p><b>FP8/INT8: </b>237 TFLOPS</p> </li> </ul> </td> <td> <ul> <li> <p>3 \* Video Encoder（+AV1）</p> </li> <li> <p>3 \* Video Decoder</p> </li> <li> <p>4 \* JPEG Decoder</p> </li> </ul> </td> <td> <ul> <li> <p>PCIe接口：PCIe Gen4 x16</p> </li> <li> <p>带宽：64 GB/s</p> </li> </ul> </td> </tr> </tbody> </table>
  * 处理器：3.4 GHz主频的Intel ^®^ Xeon ^®^可扩展处理器（SPR），全核睿频可达3.9 GHz。

* **存储：**

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，3000万PPS网络收发包能力。

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至160 Gbit/s，可用于CV和传统模型的训练业务。

    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。

ebmgn8is包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列（主网卡/辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>最大挂载数据盘数</b></p> </td> <td> <p><b>云盘最大带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn8is.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>L20 \* 8</p> </td> <td> <p>48GB\*8</p> </td> <td> <p>160（80 \* 2）</p> </td> <td> <p>3000万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>64/16</p> </td> <td> <p>32</p> </td> <td> <p>31</p> </td> <td> <p>6</p> </td> </tr> </tbody> </table>  
**说明**

ebmgn8is实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

## GPU计算型弹性裸金属服务器实例规格族ebmgn7ex
* **规格族介绍：**ebmgn7ex是阿里云为了应对日益增长的大规模AI训练需求开发的高带宽实例。ebmgn7ex依托第四代神龙架构，采用阿里云全新CIPU架构，多台裸金属之间通过eRDMA网络互联，在160 Gbit/s的互联带宽下实现RDMA通信。打开eRDMA后，您可以根据训练需求弹性选择集群中的机器数量，快速满足大规模AI训练的需求。

* **适用场景：**

  * 各类深度学习训练开发业务。

  * HPC加速计算和仿真。

  **重要**

  在使用高通信负载的AI训练业务如Transformer等模型时，务必启用NVLink进行GPU间的数据通信，否则可能由于PCIe链路大规模数据传输引起非预期的故障，导致数据受损。如不确定您使用的训练通信链路拓扑，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)由阿里云技术专家为您提供技术支持。
* **计算：**
  * 处理器：基于Intel ^®^ 第三代 Xeon ^®^Scalable计算平台（Icelake），2.9 GHz主频，全核睿频3.5 GHz，支持PCIe 4.0接口。

* **存储：**

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持物理网卡。

  * 超高网络性能，2400万PPS网络收发包能力。

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联。实例上绑定两张弹性RDMA网卡（Elastic RDMA Interface，简称ERI），每张弹性网卡连接到不同的网卡索引，可以实现160 Gbit/s的网络带宽；所有ERI连接到相同的网卡索引，实例最高可达到100 Gbit/s的网络带宽。更多信息，请参见[AttachNetworkInterface](https://help.aliyun.com/document_detail/58515.html#doc-api-Ecs-AttachNetworkInterface)。

    **说明**

关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或者[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。  
ebmgn7ex包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>物理网卡数</b></p> </td> <td> <p><b>多队列（主网卡/辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn7ex.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>80GB \* 8</p> </td> <td> <p>160（80 \* 2）</p> </td> <td> <p>2400万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>2</p> </td> <td> <p>32/32</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>  
**说明**

ebmgn7ex实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

## GPU计算型弹性裸金属服务器实例规格族ebmgn7e
* **规格族介绍：**ebmgn7e是基于神龙架构，实现软件定义硬件计算，灵活弹性与强悍性能兼备的实例规格族。

* **适用场景：**

  * 各类深度学习训练开发业务。

  * HPC加速计算和仿真。

  **重要**

  在使用高通信负载的AI训练业务如Transformer等模型时，务必启用NVLink进行GPU间的数据通信，否则可能由于PCIe链路大规模数据传输引起非预期的故障，导致数据受损。如不确定您使用的训练通信链路拓扑，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)由阿里云技术专家为您提供技术支持。
* **计算：**
  * 处理器：基于Intel ^®^ Xeon ^®^Scalable计算平台，2.9 GHz主频，全核睿频3.5 GHz，支持PCIe 4.0接口。

* **存储：**

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmgn7e包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列（主网卡/辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn7e.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>80GB \* 8</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32/12</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

MIG（Multi-Instance GPU）功能需要您在ebmgn7e实例启动后自行检查并决定是否开启或关闭，系统无法保证MIG（Multi-Instance GPU）功能是开启或关闭状态。关于MIG（Multi-Instance GPU）的更多信息，请参见[NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#supported-gpus)。

ebmgn7e实例是否支持开启MIG功能的说明如下所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>是否支持开启MIG功能</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn7e.32xlarge</p> </td> <td> <p>是</p> </td> <td> <p>ebmgn7e裸金属实例支持开启MIG功能。</p> </td> </tr> </tbody> </table>

## GPU计算型弹性裸金属服务器实例规格族ebmgn7ix
<br />

* **规格族介绍：**

  * ebmgn7ix是阿里云基于近期AI生成业务的发展推出的一款新型弹性裸金属实例规格族，每个实例为一台采用了8个A10 GPU计算卡的裸金属主机。

  * 采用最新的CIPU 1.0云处理器，解耦计算和存储能力，可以灵活选择所需存储资源。相对于上一代，该实例规格的机器间带宽提升至160 Gbit/s，可以更快地完成数据传输和处理，并应对小规模的多机训练业务。

  * 提供了裸金属规格能力，相对于传统虚拟化实例，可以支持GPU实例之间的P2P通信，大幅提升多GPU的计算效率。

* **适用场景：**

  * 结合云市场的GRID镜像启动A10的图形能力，提供高效的图形处理能力，适用于动漫、影视特效制作和渲染。

  * 结合ACK容器化管理能力，更高效、低成本地支撑AIGC图形生成和LLM大模型推理（最大支持130 B）。

  * 其他通用AI识别场景、图像识别、语音识别等。

* **计算：**

  * 采用NVIDIA A10 GPU计算卡：

    * 创新的Ampere架构。

    * 支持vGPU、RTX、TensorRT等常用加速功能。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^可扩展处理器（Ice Lake），全核睿频3.5 GHz。

* **存储：**

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至160 Gbit/s。

    **说明**

关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。  
ebmgn7ix包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列（主网卡/辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn7ix.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>NVIDIA A10 \* 8</p> </td> <td> <p>160</p> </td> <td> <p>2400万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32/32</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>  
**说明**

ebmgn7ix实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[实例启动模式](https://help.aliyun.com/document_detail/2244655.html#589d06745c7w0)。

## GPU计算型弹性裸金属服务器实例规格族ebmgn7i
* **规格族介绍：**ebmgn7i是基于神龙架构，实现软件定义硬件计算，灵活弹性与强悍性能兼备的实例规格族。

* **适用场景：**

  * 配备高性能CPU、内存、GPU，可以处理更多并发AI推理任务，适用于图像识别、语音识别、行为识别业务。

  * 支持RTX功能，搭配高主频CPU，提供高性能的3D图形虚拟化能力，适用于远程图形设计、云游戏等高强度图形处理业务。

  * 支持RTX功能，搭配高网络带宽和云盘带宽，适用于搭建高性能渲染农场。

  * 配备多个GPU，搭配高网络带宽，适用于小规模深度学习训练业务。

* **计算：**

  * 采用NVIDIA A10 GPU计算卡：

    * 创新的Ampere架构。

    * 支持vGPU、RTX、TensorRT等常用加速功能。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^可扩展处理器（Ice Lake），全核睿频3.5 GHz。

* **存储：**

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，2400万PPS网络收发包能力。

ebmgn7i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn7i.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>768</p> </td> <td> <p>NVIDIA A10 \* 4</p> </td> <td> <p>24GB \* 4</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## GPU计算型弹性裸金属服务器实例规格族ebmgn7
* **规格族介绍：**ebmgn7基于神龙架构，实现软件定义硬件计算，灵活弹性与强悍性能兼备的实例规格族。

* **适用场景：**

  * 深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练应用。

  * 高GPU负载的科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。

* **计算：**

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake）。

* **存储：**

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

ebmgn7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn7.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>768</p> </td> <td> <p>40GB\*8</p> </td> <td> <p>30</p> </td> <td> <p>1800万</p> </td> <td> <p>16</p> </td> <td> <p>15</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## GPU计算型弹性裸金属服务器实例规格族ebmgn6e
* **规格族介绍：**

  * ebmgn6e是基于神龙架构，实现软件定义硬件计算，灵活弹性与强悍性能兼备的实例规格族。

  * 采用NVIDIA V100（32 GB NVLink） GPU计算卡。

  * GPU加速器为V100（SXM2封装） ，特点如下：

    * 创新的Volta架构。

    * 单GPU显存32 GB HBM2（GPU显存带宽900 GB/s）。

    * 单GPU 5120个CUDA Cores。

    * 单GPU 640个Tensor Cores。

    * 单GPU支持6个NVLink链路（NVLink属于双向链路），单向链路的带宽为25 GB/s，总带宽为6×25×2=300 GB/s。

* **适用场景：**

  * 深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练以及推理应用。

  * 科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。

* **计算：**

  * 处理器与内存配比为1:8。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储：**

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

ebmgn6e包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn6e.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>768</p> </td> <td> <p>NVIDIA V100 \* 8</p> </td> <td> <p>32GB \* 8</p> </td> <td> <p>32</p> </td> <td> <p>480万</p> </td> <td> <p>16</p> </td> <td> <p>15</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## GPU计算型弹性裸金属服务器实例规格族ebmgn6v
* **规格族介绍：**

  * ebmgn6v是基于神龙架构，实现软件定义硬件计算，灵活弹性与强悍性能兼备的实例规格族。

  * 采用NVIDIA V100 GPU计算卡

  * GPU加速器为V100（SXM2封装） ，特点如下：

    * 创新的Volta架构

    * 单GPU显存16 GB HBM2（GPU显存带宽900 GB/s）

    * 单GPU 5120个CUDA Cores

    * 单GPU 640个Tensor Cores

    * 单GPU支持6个NVLink链路（NVLink属于双向链路），单向链路的带宽为25 GB/s，总带宽为6×25×2=300 GB/s

* **适用场景：**

  * 深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练以及推理应用

  * 科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。

* **计算：**

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储：**

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

ebmgn6v包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn6v.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>NVIDIA V100 \* 8</p> </td> <td> <p>16GB \* 8</p> </td> <td> <p>30</p> </td> <td> <p>450万</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## GPU计算型弹性裸金属服务器实例规格族ebmgn6i
* **规格族介绍：**

  * ebmgn6i是基于神龙架构，实现软件定义硬件计算，灵活弹性与强悍性能兼备的实例规格族。

  * GPU加速器为T4 ，特点如下：

    * 创新的Turing架构

    * 单GPU显存16 GB（GPU显存带宽320 GB/s）

    * 单GPU 2560个CUDA Cores

    * 单GPU多达320个Turing Tensor Cores

    * 可变精度Tensor Cores支持65 TFLOPS FP16、130 INT8 TOPS以及260 INT4 TOPS

* **适用场景：**

  * AI（DL/ML）推理，适合计算机视觉、语音识别、语音合成、NLP、机器翻译、推荐系统。

  * 云游戏云端实时渲染。

  * AR/VR的云端实时渲染。

  * 重载图形计算或图形工作站。

  * GPU加速数据库。

  * 高性能计算。

* **计算：**

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储：**

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

ebmgn6i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmgn6i.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>NVIDIA T4 \* 4</p> </td> <td> <p>16GB \* 4</p> </td> <td> <p>30</p> </td> <td> <p>450万</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## 通用网络增强型弹性裸金属服务器实例规格族ebmg5s
* **规格族介绍**：提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 中大型企业等重量级数据库应用。

  * 视频编码。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake），全核睿频2.7 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，450万PPS网络收发包能力。

ebmg5s包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg5s.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>32</p> </td> <td> <p>450万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 通用型弹性裸金属服务器实例规格族ebmg5
* **规格族介绍**：提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 中大型企业等重量级数据库应用 。

  * 视频编码。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake），全核睿频2.7 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 仅支持IPv4。

  * 高网络性能，400万PPS网络收发包能力。

ebmg5包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmg5.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>10</p> </td> <td> <p>450万</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> </tr> </tbody> </table>

## 计算网络增强型弹性裸金属服务器实例规格族ebmc5s
* **规格族介绍**：提供专属硬件资源和物理隔离。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 视频编解码、渲染等。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake），全核睿频2.7 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 高网络性能，450万PPS网络收发包能力。

ebmc5s包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmc5s.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>192</p> </td> <td> <p>32</p> </td> <td> <p>450万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 内存网络增强型弹性裸金属服务器实例规格族ebmr5s
* **规格族介绍**：提供专属硬件资源和物理隔离。

* **适用场景**：

  * 需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。

  * 兼容第三方Hypervisor，满足混合云和多云部署诉求。

  * 容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：2.5 GHz主频的Intel^®^ Xeon^®^ Platinum 8163（Skylake），全核睿频2.7 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 仅支持IPv4。

  * 高网络性能，450万PPS网络收发包能力。

ebmr5s包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.ebmr5s.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>768</p> </td> <td> <p>32</p> </td> <td> <p>450万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

## 计费方式
弹性裸金属服务器支持按量付费和包年包月。不同计费方式的区别，请参见[计费方式概述](https://help.aliyun.com/document_detail/25370.html#billingMethod-china)。
