GPU云服务器提供GPU加速计算能力，实现GPU计算资源的即开即用和弹性伸缩。作为阿里云弹性计算家族的一员，GPU云服务器结合了GPU计算力与CPU计算力，满足您在人工智能、高性能计算、专业图形图像处理等场景中的需求。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

<table> <thead> <tr> <td> <p><b>GPU虚拟化型</b></p> </td> <td> <p><b>GPU计算型</b></p> </td> <td> <p><b>不推荐（如果以下规格售罄，建议使用前面的规格）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li> <p><a href="#sgn8ia">GPU虚拟化型实例规格族sgn8ia</a></p> </li> <li> <p><a href="#section-7ae-lxh-zw5">GPU虚拟化型实例规格族sgn7i-vws（共享CPU）</a></p> </li> <li> <p><a href="#vgn7i-vws">GPU虚拟化型实例规格族vgn7i-vws</a></p> </li> <li> <p><a href="#section-dti-hon-urw">GPU虚拟化型实例规格族vgn6i-vws</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#gn9gc">GPU计算型实例规格族gn9gc</a></p> </li> <li> <p><a href="#gn8v">GPU计算型实例规格族gn8v/gn8v-tee</a></p> </li> <li> <p><a href="#gn8is">GPU计算型实例规格族gn8is</a></p> </li> <li> <p><a href="#11b8bc2035lit">GPU计算型实例规格族gn7e</a></p> </li> <li> <p><a href="#1e1b34c035zgf">GPU计算型实例规格族gn7i</a></p> </li> <li> <p><a href="#section-4xh-rvo-jxy">GPU计算型实例规格族gn7</a></p> </li> <li> <p><a href="#gn7r">GPU计算型实例规格族gn7r</a></p> </li> <li> <p><a href="#section-e88-tau-vwf">GPU计算型实例规格族gn6i</a></p> </li> <li> <p><a href="#section-8gr-min-yk3">GPU计算型实例规格族gn6e</a></p> </li> <li> <p><a href="#section-698-e4v-7rh">GPU计算型实例规格族gn6v</a></p> </li> </ul> </td> <td> <ul> <li> <p><a href="#gn7s">GPU计算型实例规格族gn7s</a></p> </li> </ul> </td> </tr> </tbody> </table>

## **GPU虚拟化型实例规格族sgn8ia**
* **规格族介绍：**

  * 依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升，可以更快地存储数据和加载模型。

  * 已包含NVIDIA GRID vWS的软件License，可以为各类专业CAD软件提供认证过的图形加速能力，满足专业级图形设计的需求，也可以作为轻量级GPU计算型实例使用，降低小规模AI推理过程的使用成本。

* **适用场景：**

  * 配备高主频CPU、内存、GPU，可以处理更多并发AI推理任务，适用于图像识别、语音识别、行为识别业务。

  * 支持RTX功能，搭配高主频CPU，提供高性能的3D图形虚拟化能力，适用于远程图形设计、云游戏等高强度图形处理业务。

  * 使用高主频AMD Genoa处理器，主频最高可达3.75 GHz，在影视动漫制作、云游戏、机械设计等领域进行3D建模时，效果更加出色。

* **计算：**

  * 采用NVIDIA Lovelace架构GPU卡。

    * 更大的GPU显存，多种不同的GPU分片。

    * 支持vGPU、RTX、TensorRT等常用加速功能，提供多种业务支撑。

  * 处理器：3.4 GHz\~3.75 GHz的AMD Genoa高主频处理器，为3D建模配备更高算力。

* **存储：**

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络：**

  * 支持IPv4、IPv6。关于IPv6通信，请参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

sgn8ia包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4/IPv6地址数</b></p> </td> <td> <p><b>最大支持云盘数量</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基准BPS（M）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sgn8ia-m2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2 GB</p> </td> <td> <p>2.5</p> </td> <td> <p>100万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15/15</p> </td> <td> <p>9</p> </td> <td> <p>3万</p> </td> <td> <p>244</p> </td> </tr> <tr> <td> <p>ecs.sgn8ia-m4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>4 GB</p> </td> <td> <p>4</p> </td> <td> <p>160万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15/15</p> </td> <td> <p>9</p> </td> <td> <p>4.5万</p> </td> <td> <p>305</p> </td> </tr> <tr> <td> <p>ecs.sgn8ia-m8.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>8 GB</p> </td> <td> <p>7</p> </td> <td> <p>200万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30/30</p> </td> <td> <p>17</p> </td> <td> <p>6万</p> </td> <td> <p>427</p> </td> </tr> <tr> <td> <p>ecs.sgn8ia-m16.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16 GB</p> </td> <td> <p>10</p> </td> <td> <p>300万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30/30</p> </td> <td> <p>33</p> </td> <td> <p>8万</p> </td> <td> <p>610</p> </td> </tr> <tr> <td> <p>ecs.sgn8ia-m24.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>24 GB</p> </td> <td> <p>16</p> </td> <td> <p>450万</p> </td> <td> <p>48</p> </td> <td> <p>8</p> </td> <td> <p>30/30</p> </td> <td> <p>33</p> </td> <td> <p>12万</p> </td> <td> <p>1000</p> </td> </tr> <tr> <td> <p>ecs.sgn8ia-m48.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>48 GB</p> </td> <td> <p>32</p> </td> <td> <p>900万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30/30</p> </td> <td> <p>33</p> </td> <td> <p>24万</p> </td> <td> <p>2000</p> </td> </tr> </tbody> </table>  
**说明**

* 上表中的GPU均为采用vGPU技术切分后的vGPU分片。

* sgn8ia实例的内存和GPU显存均为实例独享，CPU为共享资源，超售比约为1:1.5。如对CPU算力有特殊要求，请购买直通GPU的独享型实例（例如GPU计算型实例gn7i等）。

## GPU虚拟化型实例规格族sgn7i-vws（共享CPU）
* **规格族介绍**：

  * 依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升，可以更快地存储数据和加载模型。

  * 实例的CPU和网络资源采用共享模式提供，最大化利用底层资源。内存和GPU显存采用独享模式提供，为您提供数据隔离和性能保障。

    **说明**

    如果您需要独享的CPU资源，请选择vgn7i-vws。
  * 已包含NVIDIA GRID vWS的软件License，可以为各类专业CAD软件提供认证过的图形加速驱动能力，满足专业级图形设计的需求，也可以作为轻量级GPU计算型实例使用，降低小规模AI推理过程的使用成本。

* **适用场景**：

  * 配备高性能CPU、内存、GPU，可以处理更多并发AI推理任务，适用于图像识别、语音识别、行为识别业务。

  * 支持RTX功能，搭配高主频CPU，提供高性能的3D图形虚拟化能力，适用于远程图形设计、云游戏等高强度图形处理业务。

  * 使用Ice Lake处理器，在影视动漫制作、云游戏、机械设计等领域进行3D建模时，效果更加出色。

* **计算**：

  * 采用NVIDIA A10 GPU卡。

    * 创新的Ampere架构。

    * 支持vGPU、RTX、TensorRT等常用加速功能，提供多种业务支撑。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

sgn7i-vws包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sgn7i-vws-m2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>15.5</p> </td> <td> <p>NVIDIA A10 \* 1/12</p> </td> <td> <p>24GB \* 1/12</p> </td> <td> <p>1.5/5</p> </td> <td> <p>50万</p> </td> <td> <p>4</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sgn7i-vws-m4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>31</p> </td> <td> <p>NVIDIA A10 \* 1/6</p> </td> <td> <p>24GB \* 1/6</p> </td> <td> <p>2.6/10</p> </td> <td> <p>100万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sgn7i-vws-m8.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>62</p> </td> <td> <p>NVIDIA A10 \* 1/3</p> </td> <td> <p>24GB \* 1/3</p> </td> <td> <p>5/20</p> </td> <td> <p>200万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sgn7i-vws-m2s.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>NVIDIA A10 \* 1/12</p> </td> <td> <p>24GB \* 1/12</p> </td> <td> <p>1.5/5</p> </td> <td> <p>50万</p> </td> <td> <p>4</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sgn7i-vws-m4s.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>NVIDIA A10 \* 1/6</p> </td> <td> <p>24GB \* 1/6</p> </td> <td> <p>2.6/10</p> </td> <td> <p>100万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sgn7i-vws-m8s.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>32</p> </td> <td> <p>NVIDIA A10 \* 1/3</p> </td> <td> <p>24GB \* 1/3</p> </td> <td> <p>5/20</p> </td> <td> <p>200万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>  
**说明**

上表中的**GPU**列对应的指标包括GPU卡型号和GPU分片信息。其中，GPU分片表示1块GPU分成多片，每个实例上使用1片。例如：

`NVIDIA A10 * 1/12`中的`NVIDIA A10`表示GPU卡型号；`1/12`表示GPU分片，即1块GPU分成12片，每个实例上使用1片。

## GPU虚拟化型实例规格族vgn7i-vws
* **规格族介绍**：

  * 依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升，可以更快地存储数据和加载模型。

  * 已包含NVIDIA GRID vWS的软件License，可以为各类专业CAD软件提供认证过的图形加速驱动能力，满足专业级图形设计的需求，也可以作为轻量级GPU计算型实例使用，降低小规模AI推理过程的使用成本。

* **适用场景**：

  * 配备高性能CPU、内存、GPU，可以处理更多并发AI推理任务，适用于图像识别、语音识别、行为识别业务。

  * 支持RTX功能，搭配高主频CPU，提供高性能的3D图形虚拟化能力，适用于远程图形设计、云游戏等高强度图形处理业务。

  * 使用Ice Lake处理器，在影视动漫制作、云游戏、机械设计等领域进行3D建模时，效果更加出色。

* **计算**：

  * 采用NVIDIA A10 GPU卡。

    * 创新的Ampere架构。

    * 支持vGPU、RTX、TensorRT等常用加速功能，提供多种业务支撑。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

vgn7i-vws包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.vgn7i-vws-m4.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>30</p> </td> <td> <p>NVIDIA A10 \* 1/6</p> </td> <td> <p>24GB \* 1/6</p> </td> <td> <p>3</p> </td> <td> <p>100万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.vgn7i-vws-m8.2xlarge</p> </td> <td> <p>10</p> </td> <td> <p>62</p> </td> <td> <p>NVIDIA A10 \* 1/3</p> </td> <td> <p>24GB \* 1/3</p> </td> <td> <p>5</p> </td> <td> <p>200万</p> </td> <td> <p>8</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.vgn7i-vws-m12.3xlarge</p> </td> <td> <p>14</p> </td> <td> <p>93</p> </td> <td> <p>NVIDIA A10 \* 1/2</p> </td> <td> <p>24GB \* 1/2</p> </td> <td> <p>8</p> </td> <td> <p>300万</p> </td> <td> <p>8</p> </td> <td> <p>6</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.vgn7i-vws-m24.7xlarge</p> </td> <td> <p>30</p> </td> <td> <p>186</p> </td> <td> <p>NVIDIA A10 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>600万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>  
**说明**

上表中的**GPU**列对应的指标包括GPU卡型号和GPU分片信息。其中，GPU分片表示1块GPU分成多片，每个实例上使用1片。例如：

`NVIDIA A10 * 1/6`中的`NVIDIA A10`表示GPU卡型号；`1/6`表示GPU的分片，即1块GPU分成6片，每个实例上使用1片。

## GPU虚拟化型实例规格族vgn6i-vws
**重要**

* 由于GRID驱动的升级，阿里云对原vgn6i规格族进行了升级，新规格族为vgn6i-vws。新规格族采用最新的GRID驱动，并赠送了GRID vws授权。因此您不再需要从云市场镜像购买收费镜像，而是直接使用云市场镜像中已经集成了最新驱动的免费镜像。创建实例时在云市场镜像中搜索GRID，可直接搜索到预装GRID驱动的免费镜像。

* 如果需要使用其他公共镜像或自定义镜像，由于这些镜像中未包含GRID驱动，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请GRID驱动文件单独安装，阿里云不对GRID驱动额外收取License费用。

* **适用场景**：

  * 云游戏的云端实时渲染。

  * AR和VR的云端实时渲染。

  * AI（DL和ML）推理，适合弹性部署含有AI推理计算应用的互联网业务。

  * 深度学习的教学练习环境。

  * 深度学习的模型实验环境。

* **计算**：

  * 采用NVIDIA T4 GPU计算加速器。

  * 实例包含分片虚拟化后的虚拟GPU。

    * 计算能力支持NVIDIA Tesla T4的1/4和1/2。

    * GPU显存支持4 GB和8 GB。

  * 处理器与内存配比约为1:5。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

vgn6i-vws包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.vgn6i-m4-vws.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>23</p> </td> <td> <p>NVIDIA T4 \* 1/4</p> </td> <td> <p>16GB \* 1/4</p> </td> <td> <p>2</p> </td> <td> <p>50万</p> </td> <td> <p>4/2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.vgn6i-m8-vws.2xlarge</p> </td> <td> <p>10</p> </td> <td> <p>46</p> </td> <td> <p>NVIDIA T4 \* 1/2</p> </td> <td> <p>16GB \* 1/2</p> </td> <td> <p>4</p> </td> <td> <p>80万</p> </td> <td> <p>8/2</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.vgn6i-m16-vws.5xlarge</p> </td> <td> <p>20</p> </td> <td> <p>92</p> </td> <td> <p>NVIDIA T4 \* 1</p> </td> <td> <p>16GB \* 1</p> </td> <td> <p>7.5</p> </td> <td> <p>120万</p> </td> <td> <p>6</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>  
**说明**

上表中的**GPU**列对应的指标包括GPU卡型号和GPU分片信息。其中，GPU分片表示1块GPU分成多片，每个实例上使用1片。例如：

`NVIDIA T4 * 1/4`中的`NVIDIA T4`表示GPU卡型号；`1/4`表示GPU的分片，即1块GPU分成4片，每个实例上使用1片。

## GPU计算型实例规格族gn9gc
**说明**

gn9gc正在邀测中，如需使用，请提交工单申请。

* **规格族介绍**：gn9gc是阿里云推出的第9代高性价比GPU云服务器实例。采用最新一代CIPU 2.0提供云服务能力，采用高主频处理器，并配置适当容量的内存，针对大语言模型生成场景和视频、图像生成场景提供高性价比的实例。同时GPU可以直接提供图形处理能力，支持各类渲染业务需求。

* **适用场景**：

  * 大模型推理：全新一代GPU提供超越8代的全新算力，显存带宽大幅提升，新支持FP4算力全面提升推理性能和性价比。多卡并行推理效率大大提升。

* **计算**：

  * 采用最新的CIPU 2.0云处理器。

    * 第2代CIPU提供更高的云处理算力，提供更强的eRDMA、VPC、EBS组件算力。支持容器（包括但不限于Docker、Clear Container、Pouch等）。

  * 采用全新Blackwell架构专业显卡：

    * 支持OpenGL专业级图形处理功能。

    * 支持RTX、TensorRT等常用加速功能，全新升级支持FP4和PCIe Gen5互联。

  * GPU主要参数：

    <table> <thead> <tr> <td> <p><b>GPU架构</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>计算性能</b></p> </td> <td> <p><b>视频编解码能力</b></p> </td> <td> <p><b>卡间互联</b></p> </td> <td> <p><b>加速APIs</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>NVIDIA Blackwell</p> </td> <td> <ul> <li> <p><b>容量：</b>72 GB</p> </li> <li> <p><b>带宽：</b>1344 GB/s</p> </li> </ul> </td> <td> <ul> <li> <p><b>TF32：</b>126 TFLOPS</p> </li> <li> <p><b>FP32：</b>52 TFLOPS</p> </li> <li> <p><b>FP16/BF16：</b>266 TFLOPS</p> </li> <li> <p><b>FP8/INT8：</b>530 TFLOPS</p> </li> <li> <p><b>FP4：</b>970 TFLOPS</p> </li> <li> <p><b>RT Core：</b>196 TFLOPS</p> </li> </ul> </td> <td> <ul> <li> <p>3 \* Video Encoder</p> </li> <li> <p>3 \* Video Decoder</p> </li> </ul> </td> <td> <ul> <li> <p>PCIe接口：PCIe Gen5 x16</p> </li> <li> <p>带宽：128 GB/s，支持P2P</p> </li> </ul> </td> <td> <p>DX12、OpenGL 4.6、Vulkan 1.3、CUDA 12.8、OpenCL 3.0、DirectCompute</p> </td> </tr> </tbody> </table>
* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，请参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络性能，最大3000万PPS网络收发包能力（8卡实例）。

  * 支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至360 Gbit/s，可用于自驾、具身智能、CV和传统模型的训练业务。

    *  
    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。

gn9gc包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列（主网卡/辅助网卡）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>最大挂载数据盘数</b></p> </td> <td> <p><b>云盘最大带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn9gc.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>72 GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>360万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8/32</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn9gc.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>192</p> </td> <td> <p>72 GB \* 1</p> </td> <td> <p>32</p> </td> <td> <p>750万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16/64</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn9gc-2x.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>384</p> </td> <td> <p>72 GB \* 2</p> </td> <td> <p>65</p> </td> <td> <p>1500万</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32/64</p> </td> <td> <p>15</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.gn9gc-4x.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>768</p> </td> <td> <p>72 GB \* 4</p> </td> <td> <p>131</p> </td> <td> <p>3000万</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>64/64</p> </td> <td> <p>15</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> </tr> <tr> <td> <p>ecs.gn9gc-8x.64xlarge</p> </td> <td> <p>256</p> </td> <td> <p>1536</p> </td> <td> <p>72 GB \* 8</p> </td> <td> <p>204</p> </td> <td> <p>3000万</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>128/64</p> </td> <td> <p>15</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> </tr> </tbody> </table>  
**说明**

gn9gc实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[通过API设置自定义镜像的启动模式为UEFI模式](https://help.aliyun.com/document_detail/2244655.html)。

## GPU计算型实例规格族gn8v/gn8v-tee
该实例目前仅支持海外等部分地域，如有需求，请联系阿里云销售人员。

* **规格族介绍**：

  * **gn8v**：阿里云针对AI模型训练和超大参数量模型推理任务推出的第8代加速计算规格族（GPU计算型实例规格族），针对不同应用需求，为您提供1卡、2卡、4卡和8卡多种机型。

  * **gn8v-tee** ：为了满足您使用大模型进行模型训练和推理的安全性要求，阿里云基于gn8v推出一款具有**机密计算特性**的第8代实例规格族。该实例在GPU计算过程中对数据进行加密，确保用户数据的安全性。

* **适用场景**：

  * 对于70 B以上的LLM模型，进行多卡并行推理计算时性价比较高。

  * 单个GPU提供39.5 TFLOPS FP32算力，在传统AI模型训练和自动驾驶训练业务中性能突出。

  * 8卡之间支持NVLINK互联，适用于中小模型训练场景。

* **产品特色及定位**：

  * **高速\&大容量显存**：每个GPU配备了96 GB容量的HBM3显存，且显存带宽可以达到4 TB/s，大幅加快了模型训练和推理速度。

  * **高卡间带宽**：多个GPU卡之间通过900 GB/s NVLINK互联，多卡训练和推理的效率远超过历代GPU产品。

  * **大模型量化技术**：支持FP8算力，对大规模参数训练和推理过程的算力进行优化，大幅提升训练和推理的计算速度，降低显存占用。

  * **（仅限gn8v-tee系列产品）高安全性**：支持CPU机密计算（Intel TDX）和GPU机密计算（NVIDIA CC）功能，闭环全链路模型推理的机密计算能力。对于模型推理和训练的安全性，开启机密计算能力保障用户推理数据和企业模型的安全。

* **计算**：

  * 采用最新的CIPU 1.0云处理器。

    * 具有解耦计算和存储能力，可以灵活选择所需存储资源。

    * 提供裸金属能力，相对于传统虚拟化实例，可以支持GPU实例之间的P2P通信。

  * 采用Intel第4代Xeon可扩展处理器，全核睿频可达3.1 GHz，基频可达2.8 GHz。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，请参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 超高网络性能，最大3000万PPS网络收发包能力（8卡实例）。

  * 支持ERI（Elastic RDMA Interface）。

    *  
    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。
* **安全** ：支持可信计算（vTPM）特性（仅gn8v支持，gn8v-tee不支持）。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

gn8v包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>队列数量（主）</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>最大支持云盘数量</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn8v.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>96</p> </td> <td> <p>96GB \* 1</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>17</p> </td> <td> <p>10万</p> </td> <td> <p>0.75</p> </td> </tr> <tr> <td> <p>ecs.gn8v.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>128</p> </td> <td> <p>96GB \* 1</p> </td> <td> <p>15</p> </td> <td> <p>8</p> </td> <td> <p>24</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>17</p> </td> <td> <p>12万</p> </td> <td> <p>0.937</p> </td> </tr> <tr> <td> <p>ecs.gn8v-2x.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>192</p> </td> <td> <p>96GB \* 2</p> </td> <td> <p>20</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>25</p> </td> <td> <p>20万</p> </td> <td> <p>1.25</p> </td> </tr> <tr> <td> <p>ecs.gn8v-4x.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>384</p> </td> <td> <p>96GB \* 4</p> </td> <td> <p>20</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>25</p> </td> <td> <p>20万</p> </td> <td> <p>1.25</p> </td> </tr> <tr> <td> <p>ecs.gn8v-2x.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>256</p> </td> <td> <p>96GB \* 2</p> </td> <td> <p>25</p> </td> <td> <p>8</p> </td> <td> <p>48</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>33</p> </td> <td> <p>30万</p> </td> <td> <p>1.50</p> </td> </tr> <tr> <td> <p>ecs.gn8v-8x.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>768</p> </td> <td> <p>96GB \* 8</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>33</p> </td> <td> <p>36万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.gn8v-4x.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>512</p> </td> <td> <p>96GB \* 4</p> </td> <td> <p>50</p> </td> <td> <p>15</p> </td> <td> <p>64</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>49</p> </td> <td> <p>50万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.gn8v-8x.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1024</p> </td> <td> <p>96GB \* 8</p> </td> <td> <p>100</p> </td> <td> <p>15</p> </td> <td> <p>64</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>65</p> </td> <td> <p>100万</p> </td> <td> <p>6</p> </td> </tr> </tbody> </table>

gn8v-tee包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>队列数量（主）</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>最大支持云盘数量</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn8v-tee.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>96</p> </td> <td> <p>96GB \* 1</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>17</p> </td> <td> <p>10万</p> </td> <td> <p>0.75</p> </td> </tr> <tr> <td> <p>ecs.gn8v-tee.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>128</p> </td> <td> <p>96GB \* 1</p> </td> <td> <p>15</p> </td> <td> <p>8</p> </td> <td> <p>24</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>17</p> </td> <td> <p>12万</p> </td> <td> <p>0.937</p> </td> </tr> <tr> <td> <p>ecs.gn8v-tee-8x.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>768</p> </td> <td> <p>96GB \* 8</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>33</p> </td> <td> <p>36万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.gn8v-tee-8x.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1024</p> </td> <td> <p>96GB \* 8</p> </td> <td> <p>100</p> </td> <td> <p>15</p> </td> <td> <p>64</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>65</p> </td> <td> <p>100万</p> </td> <td> <p>6</p> </td> </tr> </tbody> </table>  
**说明**

gn8v-tee规格族当前仅支持Alibaba Cloud Linux 3镜像。若使用基于Alibaba Cloud Linux 3构建的自定义镜像创建实例，请确保其内核版本不低于`5.10.134-18`。

## GPU计算型实例规格族gn8is
该实例目前仅支持海外等部分地域，如有需求，请联系阿里云销售人员。

* **规格族介绍**：gn8is是阿里云针对近期AI生成业务的发展推出的第8代加速计算规格族（GPU计算型实例规格族），针对不同应用需求，采用最新NVIDIA L20 GPU，为您提供1卡、2卡、4卡和8卡机型，以及不同CPU和GPU配比的实例规格。

* **产品特色及定位**：

  * **图形处理**：该产品采用Intel第4代Xeon Scalable高主频处理器，在3D建模场景中，为您提供足够的CPU算力支撑，使得图形的渲染和设计更加顺畅。

  * **推理任务**：采用全新NVIDIA L20，单卡配置48 GB显存来加速推理任务，支持FP8浮点数格式，搭配ACK容器可灵活支持各类AIGC模型的推理，尤其适用于70 B以下LLM模型的推理任务。

* **适用场景**：

  * 结合云市场的GRID镜像使用GRID驱动，启动OpenGL和Direct3D图形能力，提供工作站级图形处理能力，适用于动漫、影视特效制作和渲染。

  * 结合ACK容器化管理能力，更高效、低成本地支撑AIGC图形生成和LLM大模型推理。

  * 其他通用AI识别场景、图像识别、语音识别等。

* **计算**：

  * 采用全新NVIDIA L20企业级GPU。

    * 支持TensorRT等常用加速功能，支持FP8浮点数格式，提升模型推理性能。

    * 显存容量提升至48 GB，多卡情况下，支持70 B及更大模型的单机推理。

    * 支持图形处理能力，例如通过云助手方式或选择云市场镜像方式安装GRID驱动后，图形处理性能相对7代平台提升1倍。

  * NVIDIA L20主要参数：

    <table> <thead> <tr> <td> <p><b>GPU架构</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>计算性能</b></p> </td> <td> <p><b>视频编解码能力</b></p> </td> <td> <p><b>卡间互联</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>NVIDIA Ada Lovelace</p> </td> <td> <ul> <li> <p><b>容量：</b>48 GB</p> </li> <li> <p><b>带宽：</b>864GB/s</p> </li> </ul> </td> <td> <ul> <li> <p><b>FP64: </b>N/A</p> </li> <li> <p><b>FP32: </b>59.3 TFLOPS</p> </li> <li> <p><b>FP16/BF16:</b> 119 TFLOPS</p> </li> <li> <p><b>FP8/INT8: </b>237 TFLOPS</p> </li> </ul> </td> <td> <ul> <li> <p>3 \* Video Encoder（+AV1）</p> </li> <li> <p>3 \* Video Decoder</p> </li> <li> <p>4 \* JPEG Decoder</p> </li> </ul> </td> <td> <ul> <li> <p>PCIe接口：PCIe Gen4 x16</p> </li> <li> <p>带宽：64GB/s</p> </li> </ul> </td> </tr> </tbody> </table>
  * 处理器：采用最新的Intel ^®^ Xeon ^®^高主频处理器，全核睿频可达3.9 GHz，以应对更复杂的3D建模需求。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。

    **说明**

    关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)或[在GPU实例上启用eRDMA](https://help.aliyun.com/document_detail/2248432.html#task-2319308)。
* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

gn8is包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>队列数量（主）</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>最大支持云盘数量</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（GB/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn8is.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>L20 \* 1</p> </td> <td> <p>48GB \* 1</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>17</p> </td> <td> <p>6万</p> </td> <td> <p>0.75</p> </td> </tr> <tr> <td> <p>ecs.gn8is.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>L20 \* 1</p> </td> <td> <p>48GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>17</p> </td> <td> <p>12万</p> </td> <td> <p>1.25</p> </td> </tr> <tr> <td> <p>ecs.gn8is-2x.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>L20 \* 2</p> </td> <td> <p>48GB \* 2</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>33</p> </td> <td> <p>25万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.gn8is-4x.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>L20 \* 4</p> </td> <td> <p>48GB \* 4</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>33</p> </td> <td> <p>45万</p> </td> <td> <p>4</p> </td> </tr> <tr> <td> <p>ecs.gn8is-8x.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>L20 \* 8</p> </td> <td> <p>48GB \* 8</p> </td> <td> <p>100</p> </td> <td> <p>15</p> </td> <td> <p>64</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>65</p> </td> <td> <p>90万</p> </td> <td> <p>8</p> </td> </tr> </tbody> </table>

## GPU计算型实例规格族gn7e
gn7e的特点如下：

* **规格族介绍**：

  * 您可以根据需要选择不同数量的卡和不同CPU资源的规格，灵活适应其不同的AI业务需求。

  * 依托第三代神龙架构，VPC和云盘网络带宽相比上一代平均提升一倍。

* **适用场景**：

  * 中小规模的AI训练业务。

  * 使用CUDA进行加速的HPC业务。

  * 对GPU处理能力或显存容量需求较高的AI推理业务。

  * 深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练应用。

  * 高GPU负载的科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。

  **重要**

  在使用高通信负载的AI训练业务如Transformer等模型时，务必启用NVLink进行GPU间的数据通信，否则可能由于PCIe链路大规模数据传输引起非预期的故障，导致数据受损。如不确定您使用的训练通信链路拓扑，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)由阿里云技术专家为您提供技术支持。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

gn7e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn7e-c16g1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>125</p> </td> <td> <p>80GB \* 1</p> </td> <td> <p>8</p> </td> <td> <p>300万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn7e-c16g1.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>250</p> </td> <td> <p>80GB \* 2</p> </td> <td> <p>16</p> </td> <td> <p>600万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn7e-c16g1.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>500</p> </td> <td> <p>80GB \* 4</p> </td> <td> <p>32</p> </td> <td> <p>1200万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn7e-c16g1.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1000</p> </td> <td> <p>80GB \* 8</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>16</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## GPU计算型实例规格族gn7i
* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 配备高性能CPU、内存、GPU，可以处理更多并发AI推理任务，适用于图像识别、语音识别、行为识别业务。

  * 支持RTX功能，搭配高主频CPU，提供高性能的3D图形虚拟化能力，适用于远程图形设计、云游戏等高强度图形处理业务。

* **计算**：

  * 采用NVIDIA A10 GPU卡。

    * 创新的Ampere架构。

    * 支持RTX、TensorRT等常用加速功能。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），全核睿频3.5 GHz。

  * 最大可提供752 GiB内存，相比gn6i大幅提升。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

gn7i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn7i-c8g1.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>NVIDIA A10 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>160万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> </tr> <tr> <td> <p>ecs.gn7i-c16g1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>60</p> </td> <td> <p>NVIDIA A10 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>300万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-c32g1.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>188</p> </td> <td> <p>NVIDIA A10 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>600万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-c32g1.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>376</p> </td> <td> <p>NVIDIA A10 \* 2</p> </td> <td> <p>24GB \* 2</p> </td> <td> <p>32</p> </td> <td> <p>1200万</p> </td> <td> <p>16</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-c32g1.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>752</p> </td> <td> <p>NVIDIA A10 \* 4</p> </td> <td> <p>24GB \* 4</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-c48g1.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>310</p> </td> <td> <p>NVIDIA A10 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>900万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-c56g1.14xlarge</p> </td> <td> <p>56</p> </td> <td> <p>346</p> </td> <td> <p>NVIDIA A10 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>1000万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-2x.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>NVIDIA A10 \* 2</p> </td> <td> <p>24GB \* 2</p> </td> <td> <p>16</p> </td> <td> <p>600万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-4x.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>NVIDIA A10 \* 4</p> </td> <td> <p>24GB \* 4</p> </td> <td> <p>32</p> </td> <td> <p>600万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-4x.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>NVIDIA A10 \* 4</p> </td> <td> <p>24GB \* 4</p> </td> <td> <p>64</p> </td> <td> <p>1200万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-8x.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>NVIDIA A10 \* 8</p> </td> <td> <p>24GB \* 8</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>32</p> </td> <td> <p>16</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7i-8x.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>NVIDIA A10 \* 8</p> </td> <td> <p>24GB \* 8</p> </td> <td> <p>32</p> </td> <td> <p>1200万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> </tbody> </table>  
**重要**

ecs.gn7i-2x.8xlarge、ecs.gn7i-4x.8xlarge、ecs.gn7i-4x.16xlarge、ecs.gn7i-8x.32xlarge以及ecs.gn7i-8x.16xlarge实例规格支持更改为ecs.gn7i-c8g1.2xlarge或ecs.gn7i-c16g1.4xlarge实例规格，但不支持更改为ecs.gn7i-c32g1.8xlarge等其他实例规格。

## GPU计算型实例规格族gn7s
如需使用gn7s，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。  
* **规格族介绍**：

  * 采用全新的Intel IceLake处理器，同时搭载Nvidia Ampere架构的NVIDIA A30 GPU卡，您可以根据需要选择不同GPU卡数和不同CPU资源的规格，灵活适应不同的AI业务需求。

  * 基于阿里云全新的第三代神龙架构，VPC和云盘网络带宽相比上一代平均提升一倍。

* **适用场景**：配备高性能CPU、内存、GPU，可以处理更多并发AI推理业务需求，适用于图像识别、语音识别、行为识别业务。

* **计算**：

  * 采用NVIDIA A30 GPU卡。

    * 创新的Nvidia Ampere架构。

    * 支持MIG（Multi-Instance GPU）功能、加速功能（基于第二代Tensor Cores加速），提供多种业务支持。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），全核睿频3.5 GHz。

  * 容量内存相比上一代实例规格族大幅提升。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

gn7s包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn7s-c8g1.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>60</p> </td> <td> <p>NVIDIA A30 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>160万</p> </td> <td> <p>5</p> </td> <td> <p>1</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> </tr> <tr> <td> <p>ecs.gn7s-c16g1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>120</p> </td> <td> <p>NVIDIA A30 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>300万</p> </td> <td> <p>5</p> </td> <td> <p>1</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.gn7s-c32g1.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>250</p> </td> <td> <p>NVIDIA A30 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>600万</p> </td> <td> <p>5</p> </td> <td> <p>1</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.gn7s-c32g1.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>500</p> </td> <td> <p>NVIDIA A30 \* 2</p> </td> <td> <p>24GB \* 2</p> </td> <td> <p>32</p> </td> <td> <p>1200万</p> </td> <td> <p>5</p> </td> <td> <p>1</p> </td> <td> <p>16</p> </td> <td> <p>15</p> </td> </tr> <tr> <td> <p>ecs.gn7s-c32g1.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1000</p> </td> <td> <p>NVIDIA A30 \* 4</p> </td> <td> <p>24GB \* 4</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> </tr> <tr> <td> <p>ecs.gn7s-c48g1.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>380</p> </td> <td> <p>NVIDIA A30 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>900万</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.gn7s-c56g1.14xlarge</p> </td> <td> <p>56</p> </td> <td> <p>440</p> </td> <td> <p>NVIDIA A30 \* 1</p> </td> <td> <p>24GB \* 1</p> </td> <td> <p>16</p> </td> <td> <p>1000万</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> </tr> </tbody> </table>

## GPU计算型实例规格族gn7
* **适用场景**：

  * 深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练应用。

  * 高GPU负载的科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。

<!-- -->

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

gn7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn7-c12g1.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>94</p> </td> <td> <p>40GB \* 1</p> </td> <td> <p>4</p> </td> <td> <p>250万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn7-c13g1.13xlarge</p> </td> <td> <p>52</p> </td> <td> <p>378</p> </td> <td> <p>40GB \* 4</p> </td> <td> <p>16</p> </td> <td> <p>900万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> </tr> <tr> <td> <p>ecs.gn7-c13g1.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>756</p> </td> <td> <p>40GB \* 8</p> </td> <td> <p>30</p> </td> <td> <p>1800万</p> </td> <td> <p>16</p> </td> <td> <p>15</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## GPU计算型实例规格族gn7r
* **规格族介绍**：

  * gn7r是阿里云推出的企业级ARM处理器+GPU的多功能规格族产品。以ARM架构为基础开发Android线上应用和云手机、云手游等业务，为其提供云原生底层资源平台。同时，其配备的NVIDIA A16 GPU具备多芯片硬件转码能力，可以作为高性价比的视频转码平台，将成本降低至ASIC类转码平台的水平。同时支持基于CUDA的计算架构，可在解码后直接在GPU上进行AI识别和分析。

  * 基于第三代神龙架构，通过CIPU云处理器进行云端资源管理，提供稳定可预期的超高计算、存储和网络性能。

  * 采用NVIDIA A16 GPU计算加速器提供GPU加速能力，支持图形加速、硬件转码和AI业务。

    **说明**

    每块NVIDIA A16卡包含4个GA 107处理芯片。
* **适用场景**：基于Android提供APP远端服务，例如云业务在线待机、云手游和云手机、Android业务爬虫、视频业务转码、视频识别、审查、视频编辑等。

* **计算**：

  * 处理器：3.0 GHz主频的Ampere ^®^ Altra ^®^ Max处理器，原生ARM计算平台为Android服务器提供高效的性能和优秀的App兼容性。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

gn7r包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn7r-c16g1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>NVIDIA GA107 \* 1</p> </td> <td> <p>8</p> </td> <td> <p>300万</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> </tr> </tbody> </table>

## GPU计算型实例规格族gn6i
* **适用场景**：

  * AI（DL和ML）推理，适合计算机视觉、语音识别、语音合成、NLP、机器翻译、推荐系统。

  * 云游戏云端实时渲染。

  * AR和VR的云端实时渲染。

  * 重载图形计算或图形工作站。

  * GPU加速数据库。

  * 高性能计算。

* **计算**：

  * GPU加速器：T4。

    * 创新的Turing架构。

    * 单GPU显存16 GB（GPU显存带宽320 GB/s）。

    * 单GPU 2560个CUDA Cores。

    * 单GPU多达320个Turing Tensor Cores。

    * 可变精度Tensor Cores支持65 TFLOPS FP16、130 INT8 TOPS以及260 INT4 TOPS。

  * 处理器与内存配比约为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

gn6i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn6i-c4g1.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>NVIDIA T4 \* 1</p> </td> <td> <p>16GB \* 1</p> </td> <td> <p>4</p> </td> <td> <p>250万</p> </td> <td> <p>无</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6i-c8g1.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>31</p> </td> <td> <p>NVIDIA T4 \* 1</p> </td> <td> <p>16GB \* 1</p> </td> <td> <p>5</p> </td> <td> <p>250万</p> </td> <td> <p>无</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6i-c16g1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>62</p> </td> <td> <p>NVIDIA T4 \* 1</p> </td> <td> <p>16GB \* 1</p> </td> <td> <p>6</p> </td> <td> <p>250万</p> </td> <td> <p>无</p> </td> <td> <p>4</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6i-c24g1.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>93</p> </td> <td> <p>NVIDIA T4 \* 1</p> </td> <td> <p>16GB \* 1</p> </td> <td> <p>7.5</p> </td> <td> <p>250万</p> </td> <td> <p>无</p> </td> <td> <p>6</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6i-c40g1.10xlarge</p> </td> <td> <p>40</p> </td> <td> <p>155</p> </td> <td> <p>NVIDIA T4 \* 1</p> </td> <td> <p>16GB \* 1</p> </td> <td> <p>10</p> </td> <td> <p>160万</p> </td> <td> <p>无</p> </td> <td> <p>16</p> </td> <td> <p>10</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6i-c24g1.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>186</p> </td> <td> <p>NVIDIA T4 \* 2</p> </td> <td> <p>16GB \* 2</p> </td> <td> <p>15</p> </td> <td> <p>450万</p> </td> <td> <p>无</p> </td> <td> <p>12</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6i-c24g1.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>372</p> </td> <td> <p>NVIDIA T4 \* 4</p> </td> <td> <p>16GB \* 4</p> </td> <td> <p>30</p> </td> <td> <p>450万</p> </td> <td> <p>25万</p> </td> <td> <p>24</p> </td> <td> <p>8</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## GPU计算型实例规格族gn6e
* **适用场景**：

  * 深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练、推理应用。

  * 科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。

* **计算**：

  * 采用NVIDIA V100（32 GB NVLink）GPU卡。

  * GPU加速器：V100（SXM2封装）。

    * 创新的Volta架构。

    * 单GPU显存32 GB HBM2（GPU显存带宽900 GB/s）。

    * 单GPU 5120个CUDA Cores。

    * 单GPU 640个Tensor Cores。

    * 单GPU支持6个NVLink链路（NVLink属于双向链路），单向链路的带宽为25 Gbit/s，总带宽为6×25×2=300 Gbit/s。

  * 处理器与内存配比约为1:8。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

gn6e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn6e-c12g1.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>92</p> </td> <td> <p>NVIDIA V100 \* 1</p> </td> <td> <p>32GB \* 1</p> </td> <td> <p>5</p> </td> <td> <p>80万</p> </td> <td> <p>8</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6e-c12g1.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>184</p> </td> <td> <p>NVIDIA V100 \* 2</p> </td> <td> <p>32GB \* 2</p> </td> <td> <p>8</p> </td> <td> <p>120万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6e-c12g1.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>368</p> </td> <td> <p>NVIDIA V100 \* 4</p> </td> <td> <p>32GB \* 4</p> </td> <td> <p>16</p> </td> <td> <p>240万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6e-c12g1.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>736</p> </td> <td> <p>NVIDIA V100 \* 8</p> </td> <td> <p>32GB \* 8</p> </td> <td> <p>32</p> </td> <td> <p>450万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

## GPU计算型实例规格族gn6v
* **适用场景**：

  * 深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练、推理应用。

  * 科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。

* **计算**：

  * 采用NVIDIA V100 GPU卡。

  * GPU加速器：V100（SXM2封装） 。

    * 创新的Volta架构。

    * 单GPU显存16 GB HBM2（GPU显存带宽900 GB/s）。

    * 单GPU 5120个CUDA Cores。

    * 单GPU 640个Tensor Cores。

    * 单GPU支持6个NVLink链路（NVLink属于双向链路），单向链路的带宽为25 Git/s，总带宽为6×25×2=300 Git/s。

  * 处理器与内存配比约为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

gn6v包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU</b></p> </td> <td> <p><b>GPU显存</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.gn6v-c8g1.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>NVIDIA V100 \* 1</p> </td> <td> <p>16GB \* 1</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>无</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6v-c8g1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>NVIDIA V100 \* 2</p> </td> <td> <p>16GB \* 2</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>无</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6v-c8g1.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>NVIDIA V100 \* 4</p> </td> <td> <p>16GB \* 4</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>无</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6v-c8g1.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>NVIDIA V100 \* 8</p> </td> <td> <p>16GB \* 8</p> </td> <td> <p>20</p> </td> <td> <p>250万</p> </td> <td> <p>无</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.gn6v-c10g1.20xlarge</p> </td> <td> <p>82</p> </td> <td> <p>336</p> </td> <td> <p>NVIDIA V100 \* 8</p> </td> <td> <p>16GB \* 8</p> </td> <td> <p>35</p> </td> <td> <p>450万</p> </td> <td> <p>25万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>
