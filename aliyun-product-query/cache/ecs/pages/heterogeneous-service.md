云服务器ECS异构服务型实例video-trans适用于视频转码、图像与视频内容处理以及帧图像提取等场景。通过本文您可以具体了解该实例的特点以及包含的实例规格和指标数据等。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

## video-trans
* **规格族介绍**：

  * 提供专属硬件资源和物理隔离

  * 高密度转码，例如显示格式1080P、帧速率30 FPS、编码格式HEVC时，硬件支持84路码流

  * 支持主流H.264、H.265码流，分辨率最大支持8192\*4096

  * 面向视频转码应用配备了ASIC转码专用加速器，大幅提升转码速度并降低成本

* **适用场景**：

  * 视频格式、码流转换

  * 图像与视频内容处理

  * 图像识别前的帧图像提取

* **计算** ：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定

* **存储**：

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

video-trans包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>硬件转码单元</b></p></td> <td><p><b>网络带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>支持IPv6</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.video-trans.26xhevc</p></td> <td><p>104</p></td> <td><p>192.0</p></td> <td><p>12</p></td> <td><p>30.0</p></td> <td><p>1800</p></td> <td><p>是</p></td> <td><p>16</p></td> <td><p>15</p></td> </tr> </tbody> </table>
