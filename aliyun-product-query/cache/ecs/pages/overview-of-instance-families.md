本文为您汇总了所有在售的ECS实例规格族，包括每种实例规格族的特点、在售规格和适用场景，供您在ECS实例购买前做规格选型的参考。  
**说明**

* [**查看实例可购买地域**](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)**：**不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。

* [**查看实例规格选型指导**](https://help.aliyun.com/document_detail/58291.html)**：**您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。

* [**查看实例规格指标说明**](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)**：**建议提前阅读以掌握相关实例规格指标的信息。

* [**使用ECS价格计算器**](https://www.aliyun.com/price/product?#/commodity/vm)**：**您可以通过价格计器预估实例费用。

## **索引**
### 企业级x86计算规格族

#### **通用型（g系列）**

<table> <thead> <tr> <td><p><b>Intel处理器</b></p></td> <td><p><b>AMD处理器</b></p></td> <td><p><b>海光处理器</b></p></td> <td><p><b>不推荐（如果以下规格售罄，建议使用前面的规格）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#g9i">通用型实例规格族g9i</a></p></li> <li><p><a href="#g8i">通用型实例规格族g8i</a></p></li> <li><p><a href="#g8ine">网络增强通用型实例规格族g8ine</a></p></li> <li><p><a href="#g7">通用型实例规格族g7</a></p></li> <li><p><a href="#g6e">通用平衡增强型实例规格族g6e</a></p></li> <li><p><a href="#g6">通用型实例规格族g6</a></p></li> </ul><p></p></td> <td> <ul> <li><p><a href="#g9ae">通用型实例规格族g9ae</a></p></li> <li><p><a href="#g9a">通用型实例规格族g9a</a></p></li> <li><p><a href="#g8a">通用型实例规格族g8a</a></p></li> <li><p><a href="#g8ae">通用平衡增强型实例规格族g8ae</a></p></li> <li><p><a href="#g7a">通用型实例规格族g7a</a></p></li> <li><p><a href="#g6a">通用型实例规格族g6a</a></p></li> </ul></td> <td> <ul> <li><p><a href="#g9h">海光通用型实例规格族g9h</a></p></li> <li><p><a href="#g7h">海光通用型实例规格族g7h</a></p></li> <li><p><a href="#g6h">海光通用型实例规格族g6h</a></p></li> </ul></td> <td> <ul> <li><p><a href="#g5">通用型实例规格族g5</a></p></li> <li><p><a href="#sn2ne">通用网络增强型实例规格族sn2ne</a></p></li> </ul></td> </tr> </tbody> </table>

#### **计算型（c系列）**

<table> <thead> <tr> <td><p><b>Intel处理器</b></p></td> <td><p><b>AMD处理器</b></p></td> <td><p><b>不推荐（如果以下规格售罄，建议使用前面的规格）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#c9i">计算型实例规格族c9i</a></p></li> <li><p><a href="#c8i">计算型实例规格族c8i</a></p></li> <li><p><a href="#c8ine">网络增强计算型实例规格族c8ine</a></p></li> <li><p><a href="#c7">计算型实例规格族c7</a></p></li> <li><p><a href="#c6e">计算平衡增强型实例规格族c6e</a></p></li> <li><p><a href="#c6">计算型实例规格族c6</a></p></li> </ul></td> <td> <ul> <li><p><a href="#c9ae">计算型实例规格族c9ae</a></p></li> <li><p><a href="#c9a">计算型实例规格族c9a</a></p></li> <li><p><a href="#c8a">计算型实例规格族c8a</a></p></li> <li><p><a href="#c8ae">计算平衡增强型实例规格族c8ae</a></p></li> <li><p><a href="#c7a">计算型实例规格族c7a</a></p></li> <li><p><a href="#c6a">计算型实例规格族c6a</a></p></li> </ul></td> <td> <ul> <li><p><a href="#ic5">密集计算型实例规格族ic5</a></p></li> <li><p><a href="#c5">计算型实例规格族c5</a></p></li> <li><p><a href="#sn1ne">计算网络增强型实例规格族sn1ne</a></p></li> </ul></td> </tr> </tbody> </table>

#### **内存型（r系列）**

<table> <thead> <tr> <td><p><b>Intel处理器</b></p></td> <td><p><b>AMD处理器</b></p></td> <td><p><b>不推荐（如果以下规格售罄，建议使用前面的规格）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#r9i">内存型实例规格族r9i</a></p></li> <li><p><a href="#r8i">内存型实例规格族r8i</a></p></li> <li><p><a href="#r7p">内存型实例规格族r7p</a></p></li> <li><p><a href="#r7">内存型实例规格族r7</a></p></li> <li><p><a href="#r6e">内存平衡增强型实例规格族r6e</a></p></li> <li><p><a href="#f48bcefcb9xn8">内存型实例规格族r6</a></p></li> </ul></td> <td> <ul> <li><p><a href="#r9ae">内存型实例规格族r9ae</a></p></li> <li><p><a href="#r9a">内存型实例规格族r9a</a></p></li> <li><p><a href="#r8a">内存型实例规格族r8a</a></p></li> <li><p><a href="#r8ae">内存平衡增强型实例规格族r8ae</a></p></li> <li><p><a href="#r7a">内存型实例规格族r7a</a></p></li> <li><p><a href="#r6a">内存型实例规格族r6a</a></p></li> </ul><p></p></td> <td> <ul> <li><p><a href="#r5">内存型实例规格族r5</a></p></li> <li><p><a href="#se1ne">内存网络增强型实例规格族se1ne</a></p></li> <li><p><a href="#se1">内存型实例规格族se1</a></p></li> </ul></td> </tr> </tbody> </table>

#### **通用算力型（U实例）**

[通用算力型实例规格族u2a](#u2a)

[通用算力型实例规格族u2i](#u2i)

[通用算力型实例规格族u1](#u1)

#### **大数据型（d系列）**

<table> <thead> <tr> <td><p><b>推荐</b></p></td> <td><p><b>不推荐（如果售罄，建议使用推荐规格族）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#d3s">大数据存储密集型实例规格族d3s</a></p></li> <li><p><a href="#d3c">大数据计算密集型实例规格族d3c</a></p></li> <li><p><a href="#d2c">大数据计算密集型实例规格族d2c</a></p></li> <li><p><a href="#d2s">大数据存储密集型实例规格族d2s</a></p></li> </ul></td> <td> <ul> <li><p><a href="#d1ne">大数据网络增强型实例规格族d1ne</a></p></li> </ul></td> </tr> </tbody> </table>

#### **本地SSD型（i系列）**

<table> <thead> <tr> <td><p><b>Intel</b><b><sup>®</sup></b><b>\&nbsp;Xeon</b><b><sup>®</sup></b><b>\&nbsp;Granite Rapids处理器</b></p></td> <td><p><b>Intel</b><b><sup>® </sup></b><b>Xeon</b><b><sup>®</sup></b><b>可扩展处理器（Ice Lake ）</b></p></td> <td><p><b>Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>Platinum 8269CY（Cascade Lake ）</b></p></td> <td><p><b>Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>Platinum 8163（Skylake）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#i5g">本地SSD型实例规格族i5g</a></p></li> <li><p><a href="#i5ge">本地SSD型实例规格族i5ge</a></p></li> <li><p><a href="#i5e">本地SSD型实例规格族i5e</a></p></li> <li><p><a href="#i5">本地SSD型实例规格族i5</a></p></li> </ul></td> <td> <ul> <li><p><a href="#i4">本地SSD型实例规格族i4</a></p></li> <li><p><a href="#i4g">本地SSD型实例规格族i4g</a></p></li> <li><p><a href="#i4r">本地SSD型实例规格族i4r</a></p></li> <li><p><a href="#i4p">性能增强型本地盘实例规格族i4p</a></p></li> </ul></td> <td> <ul> <li><p><a href="#i3g">本地SSD型实例规格族i3g</a></p></li> <li><p><a href="#i3">本地SSD型实例规格族i3</a></p></li> </ul></td> <td> <ul> <li><p><a href="#i2">本地SSD型实例规格族i2</a></p></li> <li><p><a href="#i2g">本地SSD型实例规格族i2g</a></p></li> <li><p><a href="#i2ne">本地SSD型实例规格族i2ne</a></p></li> <li><p><a href="#i2gne">本地SSD型实例规格族i2gne</a></p></li> </ul></td> </tr> </tbody> </table>

#### **高主频（hf系列）**

<table> <thead> <tr> <td><p><b> 推荐</b></p></td> <td><p><b>不推荐（如果售罄，建议使用推荐规格族）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p><b>采用P-core（性能核）的英特尔</b><b><sup>®</sup></b><b> 至强</b><b><sup>®</sup></b><b> 6处理器</b></p></td> <td><p><b>第四代Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>可扩展处理器（Sapphire Rapids）</b></p></td> <td><p><b>Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>Cooper Lake处理器</b></p></td> <td><p><b>Intel</b><b><sup>®</sup></b><b>Xeon</b><b><sup>®</sup></b><b>Platinum 8269CY（Cascade Lake）</b></p></td> </tr> <tr> <td> <ul> <li><p><a href="#hfc9i">高主频计算实例规格族hfc9i</a></p></li> <li><p><a href="#hfg9i">高主频通用型实例规格族hfg9i</a></p></li> <li><p><a href="#hfr9i">高主频内存型实例规格族hfr9i</a></p></li> </ul></td> <td> <ul> <li><p><a href="#hfc8i">高主频计算型实例规格族hfc8i</a></p></li> <li><p><a href="#hfg8i">高主频通用型实例规格族hfg8i</a></p></li> <li><p><a href="#hfr8i">高主频内存型实例规格族hfr8i</a></p></li> </ul></td> <td> <ul> <li><p><a href="#hfc7">高主频计算型实例规格族hfc7</a></p></li> <li><p><a href="#hfg7">高主频通用型实例规格族hfg7</a></p></li> <li><p><a href="#hfr7">高主频内存型实例规格族hfr7</a></p></li> </ul></td> <td> <ul> <li><p><a href="#hfc6">高主频计算型实例规格族hfc6</a></p></li> <li><p><a href="#hfg6">高主频通用型实例规格族hfg6</a></p></li> <li><p><a href="#hfr6">高主频内存型实例规格族hfr6</a></p></li> </ul></td> <td> <ul> <li><p><a href="#hfc5">高主频计算型实例规格族hfc5</a></p></li> <li><p><a href="#hfg5">高主频通用型实例规格族hfg5</a></p></li> </ul></td> </tr> </tbody> </table>

<br />

#### 增强型

<table> <thead> <tr> <td><p><b>存储增强型</b></p></td> <td><p><b>网络增强型</b></p></td> <td><p><b>安全增强型</b></p></td> <td><p><b>内存增强型</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#g8ise">存储增强通用型实例规格族g8ise</a></p></li> <li><p><a href="#g7se">存储增强通用型实例规格族g7se</a></p></li> <li><p><a href="#c7se">存储增强计算型实例规格族c7se</a></p></li> <li><p><a href="#r7se">存储增强内存型实例规格族r7se</a></p></li> </ul></td> <td> <ul> <li><p><a href="#g8ine">网络增强通用型实例规格族g8ine</a></p></li> <li><p><a href="#c8ine">网络增强计算型实例规格族c8ine</a></p></li> <li><p><a href="#g7nex">网络增强通用型实例规格族g7nex</a></p></li> <li><p><a href="#c7nex">网络增强计算型实例规格族c7nex</a></p></li> <li><p><a href="#g7ne">网络增强通用型实例规格族g7ne</a></p></li> <li><p><a href="#g5ne">网络增强通用型实例规格族g5ne</a></p></li> </ul></td> <td> <ul> <li><p><a href="#g9it">安全增强通用型实例规格族g9it</a></p></li> <li><p><a href="#r9it">安全增强内存型实例规格族r9it</a></p></li> <li><p><a href="#g7t">安全增强通用型实例规格族g7t</a></p></li> <li><p><a href="#c7t">安全增强计算型实例规格族c7t</a></p></li> <li><p><a href="#r7t">安全增强内存型实例规格族r7t</a></p></li> <li><p><a href="#g6t">安全增强通用型实例规格族g6t</a></p></li> <li><p><a href="#c6t">安全增强计算型实例规格族c6t</a></p></li> </ul></td> <td> <ul> <li><p><b>推荐</b></p> <ul> <li><p><a href="#re8">内存增强型实例规格族re8</a></p></li> <li><p><a href="#re7p">内存增强型实例规格族re7p</a></p></li> <li><p><a href="#re6p">持久内存型实例规格族re6p</a></p></li> <li><p><a href="#re6">内存增强型实例规格族re6</a></p></li> </ul></li> <li><p><b>不推荐（如果售罄，建议使用推荐规格族） </b></p> <ul> <li><p><a href="#re4">内存增强型实例规格族re4</a></p></li> <li><p><a href="#re4e">内存增强型实例规格族re4e</a></p></li> </ul></li> </ul></td> </tr> </tbody> </table>

### 入门级x86计算规格族群

<table> <thead> <tr> <td><p><b>推荐</b></p></td> <td><p><b>不推荐（如果售罄，建议使用推荐规格族）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#e">经济型实例规格族e</a></p></li> <li><p><a href="#t6">突发性能实例规格族t6</a></p></li> </ul></td> <td> <ul> <li><p><a href="#s6">共享标准型实例规格族s6</a></p></li> <li><p><a href="#t5">突发性能实例规格族t5</a></p></li> <li><p><a href="#v5">CPU超分型实例规格族v5</a></p></li> <li><p><a href="#xn4-n4-mn4-e4">上一代共享型实例规格族xn4、n4、mn4、e4</a></p></li> </ul></td> </tr> </tbody> </table>

### 企业级ARM计算规格族

<table> <thead> <tr> <td><p><b>倚天710处理器</b></p></td> <td><p><b>Ampere</b><b><sup>®</sup></b><b>Altra</b><b><sup>®</sup></b><b>处理器</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#g8y">通用型实例规格族g8y</a></p></li> <li><p><a href="#c8y">计算型实例规格族c8y</a></p></li> <li><p><a href="#r8y">内存型实例规格族r8y</a></p></li> </ul></td> <td> <ul> <li><p><a href="#g6r">通用型实例规格族g6r</a></p></li> <li><p><a href="#c6r">计算型实例规格族c6r</a></p></li> </ul></td> </tr> </tbody> </table>

### 弹性裸金属服务器规格族群

<table> <thead> <tr> <td><p><b>推荐</b></p></td> <td><p><b>不推荐（如果售罄，建议使用推荐规格族）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p><b>通用型（g）</b></p></td> <td><p><b>计算型（c）</b></p></td> <td><p><b>内存型（r）</b></p></td> <td><p><b>高主频型（hf）</b></p></td> <td><p><b>GPU计算型（gn）</b></p></td> </tr> <tr> <td> <ul> <li><p><a href="#ebmg9ae">通用型弹性裸金属服务器实例规格族ebmg9ae</a></p></li> <li><p><a href="#ebmg9a">通用型弹性裸金属服务器实例规格族ebmg9a</a></p></li> <li><p><a href="#ebmg9i">通用型弹性裸金属服务器实例规格族ebmg9i</a></p></li> <li><p><a href="#ebmg8a">通用型弹性裸金属服务器实例规格族ebmg8a</a></p></li> <li><p><a href="#ebmg8y">通用型弹性裸金属服务器实例规格族ebmg8y</a></p></li> <li><p><a href="#ebmg8i">通用型弹性裸金属服务器实例规格族ebmg8i</a></p></li> <li><p><a href="#ebmg7se">存储增强型弹性裸金属服务器实例规格族ebmg7se</a></p></li> <li><p><a href="#ebmg7">通用型弹性裸金属服务器实例规格族ebmg7</a></p></li> <li><p><a href="#ebmg7a">通用型弹性裸金属服务器实例规格族ebmg7a</a></p></li> <li><p><a href="#ebmg6a">通用型弹性裸金属服务器实例规格族ebmg6a</a></p></li> <li><p><a href="#ebmg6e">通用型（平衡增强）弹性裸金属服务器实例规格族ebmg6e</a></p></li> <li><p><a href="#ebmg6">通用型弹性裸金属服务器实例规格族ebmg6</a></p></li> </ul></td> <td> <ul> <li><p><a href="#ebmc9ae">计算型弹性裸金属服务器实例规格族ebmc9ae</a></p></li> <li><p><a href="#ebmc9i">计算型弹性裸金属服务器实例规格族ebmc9i</a></p></li> <li><p><a href="#ebmc8a">计算型弹性裸金属服务器实例规格族ebmc8a</a></p></li> <li><p><a href="#ebmc8y">计算型弹性裸金属服务器实例规格族ebmc8y</a></p></li> <li><p><a href="#ebmc8i">计算型弹性裸金属服务器实例规格族ebmc8i</a></p></li> <li><p><a href="#ebmc7">计算型弹性裸金属服务器实例规格族ebmc7</a></p></li> <li><p><a href="#ebmc7a">计算型弹性裸金属服务器实例规格族ebmc7a</a></p></li> <li><p><a href="#ebmc6me">计算型弹性裸金属服务器实例规格族ebmc6me</a></p></li> <li><p><a href="#ebmc6a">计算型弹性裸金属服务器实例规格族ebmc6a</a></p></li> <li><p><a href="#ebmc6e">计算型（平衡增强）弹性裸金属服务器实例规格族ebmc6e</a></p></li> <li><p><a href="#ebmc6">计算型弹性裸金属服务器实例规格族ebmc6</a></p></li> </ul><p></p></td> <td> <ul> <li><p><a href="#ebmr9ae">内存型弹性裸金属服务器实例规格族ebmr9ae</a></p></li> <li><p><a href="#ebmr9i">内存型弹性裸金属服务器实例规格族ebmr9i</a></p></li> <li><p><a href="#ebmr8a">内存型弹性裸金属服务器实例规格族ebmr8a</a></p></li> <li><p><a href="#ebmr8y">内存型弹性裸金属服务器实例规格族ebmr8y</a></p></li> <li><p><a href="#ebmr7">内存型弹性裸金属服务器实例规格族ebmr7</a></p></li> <li><p><a href="#ebmr7a">内存型弹性裸金属服务器实例规格族ebmr7a</a></p></li> <li><p><a href="#ebmr6a">内存型弹性裸金属服务器实例规格族ebmr6a</a></p></li> <li><p><a href="#ebmr6e">内存型（平衡增强）弹性裸金属服务器实例规格族ebmr6e</a></p></li> <li><p><a href="#ebmr6">内存型弹性裸金属服务器实例规格族ebmr6</a></p></li> <li><p><a href="#ebmre7p">持久内存增强型弹性裸金属服务器实例规格族ebmre7p</a></p></li> <li><p><a href="#ebmre6p">持久内存增强型弹性裸金属服务器实例规格族ebmre6p</a></p></li> <li><p><a href="#ebmre6-6t">内存增强型弹性裸金属服务器实例规格族ebmre6-6t</a></p></li> </ul><p></p></td> <td> <ul> <li><p><a href="#ebmhfg7">高主频通用型弹性裸金属服务器实例规格族ebmhfg7</a></p></li> <li><p><a href="#ebmhfc7">高主频计算型弹性裸金属服务器实例规格族ebmhfc7</a></p></li> <li><p><a href="#ebmhfr7">高主频内存型弹性裸金属服务器实例规格族ebmhfr7</a></p></li> <li><p><a href="#ebmhfg6">高主频通用型弹性裸金属服务器实例规格族ebmhfg6</a></p></li> <li><p><a href="#ebmhfc6">高主频计算型弹性裸金属服务器实例规格族ebmhfc6</a></p></li> <li><p><a href="#ebmhfr6">高主频内存型弹性裸金属服务器实例规格族ebmhfr6</a></p></li> </ul></td> <td> <ul> <li><p><a href="#ebmgn9g">GPU计算型弹性裸金属服务器实例规格族ebmgn9g</a></p></li> <li><p><a href="#ebmgn9ge">GPU计算型弹性裸金属服务器实例规格族ebmgn9ge</a></p></li> <li><p><a href="#ebmgn9gc">GPU计算型弹性裸金属服务器实例规格族ebmgn9gc</a></p></li> <li><p><a href="#ebmgn8v">GPU计算型弹性裸金属服务器实例规格族ebmgn8v</a></p></li> <li><p><a href="#ebmgn8ia">GPU计算型弹性裸金属服务器实例规格族ebmgn8ia</a></p></li> <li><p><a href="#ebmgn8is">GPU计算型弹性裸金属服务器实例规格族ebmgn8is</a></p></li> <li><p><a href="#ebmgn7ex">GPU计算型弹性裸金属服务器实例规格族ebmgn7ex</a></p></li> <li><p><a href="#ebmgn7e">GPU计算型弹性裸金属服务器实例规格族ebmgn7e</a></p></li> <li><p><a href="#ebmgn7ix">GPU计算型弹性裸金属服务器实例规格族ebmgn7ix</a></p></li> <li><p><a href="#ebmgn7i">GPU计算型弹性裸金属服务器实例规格族ebmgn7i</a></p></li> <li><p><a href="#ebmgn7">GPU计算型弹性裸金属服务器实例规格族ebmgn7</a></p></li> <li><p><a href="#ebmgn6e">GPU计算型弹性裸金属服务器实例规格族ebmgn6e</a></p></li> <li><p><a href="#ebmgn6v">GPU计算型弹性裸金属服务器实例规格族ebmgn6v</a></p></li> <li><p><a href="#ebmgn6i">GPU计算型弹性裸金属服务器实例规格族ebmgn6i</a></p></li> </ul></td> <td> <ul> <li><p><a href="#ebmc5s">计算网络增强型弹性裸金属服务器ebmc5s</a></p></li> <li><p><a href="#ebmg5s">通用网络增强型弹性裸金属服务器ebmg5s</a></p></li> <li><p><a href="#ebmr5s">内存网络增强型弹性裸金属服务器ebmr5s</a></p></li> <li><p><a href="#ebmg5">通用型弹性裸金属服务器实例规格族ebmg5</a></p></li> </ul></td> </tr> </tbody> </table>

### 高性能计算\&超级计算集群实例规格族群

<table> <thead> <tr> <td><p><b>高性能计算(hpc)</b></p></td> <td><p><b>超级计算集群（SCC）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#hpc9a">高性能计算优化型实例规格族hpc9a</a></p></li> <li><p><a href="#hpc8i">高性能计算优化型实例规格族hpc8i</a></p></li> <li><p><a href="#hpc8ae">高性能计算优化型实例规格族hpc8ae</a></p></li> <li><p><a href="#hpc7ip">高性能计算优化型实例规格族hpc7ip</a></p></li> <li><p><a href="#hpc6id">高性能计算优化型实例规格族hpc6id</a></p></li> </ul><p></p></td> <td> <ul> <li><p><a href="#sccg7">通用型超级计算集群实例规格族sccg7</a></p></li> <li><p><a href="#sccc7">计算型超级计算集群实例规格族sccc7</a></p></li> <li><p><a href="#sccgn7ex">GPU计算型超级计算集群实例规格族sccgn7ex</a></p></li> </ul></td> </tr> </tbody> </table>

### 异构计算规格族群

<table> <thead> <tr> <td><p><b>推荐</b></p></td> <td><p><b>不推荐（如果售罄，建议使用推荐规格族）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <ul> <li><p><a href="#sgn8ia">GPU虚拟化型实例规格族sgn8ia</a></p></li> <li><p><a href="#sgn7i-vws">GPU虚拟化型实例规格族sgn7i-vws（共享CPU）</a></p></li> <li><p><a href="#vgn7i-vws">GPU虚拟化型实例规格族vgn7i-vws</a></p></li> <li><p><a href="#vgn6i-vws">GPU虚拟化型实例规格族vgn6i-vws</a></p></li> <li><p><a href="#gn9gc">GPU计算型实例规格族gn9gc</a></p></li> <li><p><a href="#gn8v">GPU计算型实例规格族gn8v/gn8v-tee</a></p></li> <li><p><a href="#gn8is">GPU计算型实例规格族gn8is</a></p></li> <li><p><a href="#gn7e">GPU计算型实例规格族gn7e</a></p></li> <li><p><a href="#gn7i">GPU计算型实例规格族gn7i</a></p></li> <li><p><a href="#gn7">GPU计算型实例规格族gn7</a></p></li> <li><p><a href="#gn7r">GPU计算型实例规格族gn7r</a></p></li> <li><p><a href="#gn6i">GPU计算型实例规格族gn6i</a></p></li> <li><p><a href="#gn6e">GPU计算型实例规格族gn6e</a></p></li> <li><p><a href="#gn6v">GPU计算型实例规格族gn6v</a></p></li> <li><p><a href="#video-trans">异构服务型实例规格族video-trans</a></p></li> </ul></td> <td> <ul> <li><p><a href="#gn7s">GPU计算型实例规格族gn7s</a></p></li> </ul></td> </tr> </tbody> </table>

## 企业级x86计算规格族群
### 通用型实例规格族g9ae

* **规格族介绍** ：采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC^™^ Turin 处理器，采用物理核设计，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：大数据分析（Spark/Flink/ES等），搜索/推荐/广告（ps-worker），核心交易系统，音视频转码，AI训练与推理，通用的企业级应用（Java）等。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高3.7 GHz，采用物理核设计，计算性能稳定。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#6cc7ed4977cxh)。

* **存储**：

  * 支持调整存储基础带宽。

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持调整网络基础带宽。

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持[可信计算（vTPM）特性](https://help.aliyun.com/document_detail/201394.html)。

  * 支持[VPC流量加密](https://help.aliyun.com/document_detail/2932958.html)。

g9ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g9ae.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2.5/最高25</p> </td> <td> <p>最高150万</p> </td> <td> <p>最高50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高20万</p> </td> <td> <p>2.5/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高25</p> </td> <td> <p>最高160万</p> </td> <td> <p>最高50万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高20万</p> </td> <td> <p>3/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高25</p> </td> <td> <p>最高250万</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高20万</p> </td> <td> <p>4/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>10/最高25</p> </td> <td> <p>最高320万</p> </td> <td> <p>最高50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高20万</p> </td> <td> <p>5.5/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/最高25</p> </td> <td> <p>最高500万</p> </td> <td> <p>最高100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高20万</p> </td> <td> <p>8/最高20</p> </td> </tr> <tr> <td> <p>ecs.g9ae.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>25/无</p> </td> <td> <p>750万</p> </td> <td> <p>150万</p> </td> <td> <p>48</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>15万</p> </td> <td> <p>13/无</p> </td> </tr> <tr> <td> <p>ecs.g9ae.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>1000万</p> </td> <td> <p>200万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g9ae.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>50/无</p> </td> <td> <p>1500万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>30万</p> </td> <td> <p>25/无</p> </td> </tr> <tr> <td> <p>ecs.g9ae.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>400万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>40万</p> </td> <td> <p>32/无</p> </td> </tr> <tr> <td> <p>ecs.g9ae.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>600万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>60万</p> </td> <td> <p>50/无</p> </td> </tr> </tbody> </table>

### 通用型实例规格族g9a

* **规格族介绍** ：采用阿里云全新CIPU架构，搭配AMD最新EPYC^™^ Turin 处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：大中型数据库系统，游戏服务器，金融量化，区块链，网站和应用服务器以及其他通用企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高4.1 GHz，计算性能稳定。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#6cc7ed4977cxh)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持[可信计算（vTPM）特性](https://help.aliyun.com/document_detail/201394.html)。

g9a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g9a.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2.5/最高15</p> </td> <td> <p>最高120万</p> </td> <td> <p>最高50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高11万</p> </td> <td> <p>2/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高15</p> </td> <td> <p>最高140万</p> </td> <td> <p>最高50万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>3/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高15</p> </td> <td> <p>最高200万</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>4/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>12/最高25</p> </td> <td> <p>最高300万</p> </td> <td> <p>最高50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>5/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/最高32</p> </td> <td> <p>最高400万</p> </td> <td> <p>最高80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>8/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9a.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>750万</p> </td> <td> <p>150万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>12万</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g9a.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>48/无</p> </td> <td> <p>1000万</p> </td> <td> <p>220万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万</p> </td> <td> <p>24/无</p> </td> </tr> <tr> <td> <p>ecs.g9a.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>1500万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>25万</p> </td> <td> <p>32/无</p> </td> </tr> <tr> <td> <p>ecs.g9a.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>96/无</p> </td> <td> <p>2000万</p> </td> <td> <p>450万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>40万</p> </td> <td> <p>48/无</p> </td> </tr> </tbody> </table>

### 通用型实例规格族g9i

* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，游戏服务器，中小型数据库系统、缓存、搜索集群，搜索推广类应用，网站和应用服务器，数据分析和计算，安全可信计算场景。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，单核最大睿频3.9GHz。

    **说明**

    该实例在系统中可能会存在不同的频率显示，其中单核最高睿频3.9 GHz，属于突发性能，突发能力与物理机CPU整机负载相关，无法作为SLA承诺。
  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

g9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g9i.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2.5/最高15</p> </td> <td> <p>100万</p> </td> <td> <p>最高50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2.5万/最高20万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高15</p> </td> <td> <p>120万</p> </td> <td> <p>最高50万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>2.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高15</p> </td> <td> <p>160万</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>10/最高15</p> </td> <td> <p>240万</p> </td> <td> <p>最高50万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>15/最高25</p> </td> <td> <p>450万</p> </td> <td> <p>60万</p> </td> <td> <p>24</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>12万/最高20万</p> </td> <td> <p>7.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g9i.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>20/最高32</p> </td> <td> <p>600万</p> </td> <td> <p>80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万/最高30万</p> </td> <td> <p>10/最高12</p> </td> </tr> <tr> <td> <p>ecs.g9i.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>25/最高32</p> </td> <td> <p>900万</p> </td> <td> <p>160万</p> </td> <td> <p>48</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>24万/最高32万</p> </td> <td> <p>12/最高15</p> </td> </tr> <tr> <td> <p>ecs.g9i.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>28/最高36</p> </td> <td> <p>1200万</p> </td> <td> <p>200万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>30万/最高40万</p> </td> <td> <p>16/最高24</p> </td> </tr> <tr> <td> <p>ecs.g9i.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>32/最高48</p> </td> <td> <p>1800万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>35万/最高60万</p> </td> <td> <p>20/最高28</p> </td> </tr> <tr> <td> <p>ecs.g9i.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>36/最高50</p> </td> <td> <p>2000万</p> </td> <td> <p>400万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>40万/最高65万</p> </td> <td> <p>24/最高28</p> </td> </tr> <tr> <td> <p>ecs.g9i.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>600万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>50万/最高80万</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

### 通用型实例规格族g8a

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**： 通用的企业级应用（Java），内存型或者关系型数据库类应用，大数据类应用（Kafka、ElasticSearch等），Web类应用，AI训练与推理，音视频转码类应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：AMD EPYC^™^ Genoa 9T24处理器，基频2.7 GHz，睿频最高3.7 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
g8a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8a.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.5/12.5</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/11万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2.5/12.5</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>3万/11万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>4/12.5</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4.5万/11万</p> </td> <td> <p>2.5/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>7/12.5</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>6万/11万</p> </td> <td> <p>3.5/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/11万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>16/25</p> </td> <td> <p>450万</p> </td> <td> <p>75万</p> </td> <td> <p>48</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>12万/无</p> </td> <td> <p>8/10</p> </td> </tr> <tr> <td> <p>ecs.g8a.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>20/25</p> </td> <td> <p>600万</p> </td> <td> <p>100万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/无</p> </td> <td> <p>10/无</p> </td> </tr> <tr> <td> <p>ecs.g8a.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>32/无</p> </td> <td> <p>900万</p> </td> <td> <p>150万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>24万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g8a.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>40/无</p> </td> <td> <p>1200万</p> </td> <td> <p>200万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32万/无</p> </td> <td> <p>20/无</p> </td> </tr> <tr> <td> <p>ecs.g8a.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>768</p> </td> <td> <p>64/无</p> </td> <td> <p>1800万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>  
**说明**

* 由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

* ecs.g8a.large、ecs.g8a.xlarge需开启巨型帧（Jumbo frames），才能达到12.5 Gbit/s网络突发带宽。更多详情，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

### 通用型实例规格族g8i

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，游戏服务器，中小型数据库系统、缓存、搜索集群，搜索推广类应用，网站和应用服务器，数据分析和计算，安全可信计算场景。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

    **说明**

    购买该实例时，系统将随机分配上述两种处理器之一，不支持手动选择。
  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持可信计算（vTPM）特性。更多信息，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

  * 4 vCPU以上规格的实例支持阿里云虚拟化Enclave特性，提供基于虚拟化的机密计算环境。更多信息，请参见[构建Enclave机密计算环境](https://help.aliyun.com/document_detail/203433.html#task-2038130)。

  * 采用英特尔TME（Total Memory Encryption）运行内存加密。

  * 支持CPU机密计算（Intel^®^ TDX），更多信息，[构建TDX机密计算环境](https://help.aliyun.com/document_detail/479090.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
g8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8i.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2.5/最高15</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2.5万/最高20万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高15</p> </td> <td> <p>120万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>2.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高15</p> </td> <td> <p>160万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>10/最高15</p> </td> <td> <p>240万</p> </td> <td> <p>最高30万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>35万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>15/最高25</p> </td> <td> <p>450万</p> </td> <td> <p>50万</p> </td> <td> <p>24</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>12万/最高20万</p> </td> <td> <p>7.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8i.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>20/最高25</p> </td> <td> <p>600万</p> </td> <td> <p>80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万/无</p> </td> <td> <p>10/无</p> </td> </tr> <tr> <td> <p>ecs.g8i.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>25/无</p> </td> <td> <p>900万</p> </td> <td> <p>100万</p> </td> <td> <p>48</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>30万/无</p> </td> <td> <p>12/无</p> </td> </tr> <tr> <td> <p>ecs.g8i.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>160万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>36万/无</p> </td> <td> <p>20/无</p> </td> </tr> <tr> <td> <p>ecs.g8i.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>384</p> </td> <td> <p>50/无</p> </td> <td> <p>1800万</p> </td> <td> <p>200万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>24/无</p> </td> </tr> <tr> <td> <p>ecs.g8i.48xlarge</p> </td> <td> <p>192</p> </td> <td> <p>1024</p> </td> <td> <p>100/无</p> </td> <td> <p>3000万</p> </td> <td> <p>400万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>50</p> </td> <td> <p>50</p> </td> <td> <p>100万/无</p> </td> <td> <p>48/无</p> </td> </tr> </tbody> </table>

### 网络增强通用型实例规格族g8ine

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**： 适用于网络密集型场景，转发、连接性能出色，尤其适用于做网络接入层网关，流量、数据转发或预处理中间件等。作为云上解决方案中的一部分，在大型网站、电商、AI等场景下都可应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多信息，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

g8ine包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>EBS多队列</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8ine.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>4/最高24</p> </td> <td> <p>60万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>2万/最高8万</p> </td> <td> <p>2/最高8</p> </td> </tr> <tr> <td> <p>ecs.g8ine.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>7/最高28</p> </td> <td> <p>120万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>4万/最高8万</p> </td> <td> <p>2.5/最高8</p> </td> </tr> <tr> <td> <p>ecs.g8ine.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>12/最高35</p> </td> <td> <p>200万</p> </td> <td> <p>8</p> </td> <td> <p>6</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>2</p> </td> <td> <p>5万/最高8万</p> </td> <td> <p>4/最高8</p> </td> </tr> <tr> <td> <p>ecs.g8ine.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>23/最高44</p> </td> <td> <p>350万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>2</p> </td> <td> <p>8万/最高10万</p> </td> <td> <p>6/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ine.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>44/无</p> </td> <td> <p>700万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>4</p> </td> <td> <p>10万/无</p> </td> <td> <p>10/无</p> </td> </tr> </tbody> </table>

### 通用平衡增强型实例规格族g8ae

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：人工智能场景（如深度学习与训练、AI推理等），HPC等高性能科学计算场景，大中型数据库系统、缓存、搜索集群，大型在线游戏服务器，其他对性能要求较高的通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：3.4 GHz主频的AMD EPYC™ Genoa处理器，单核睿频最高3.75 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

g8ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>支持vTPM</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8ae.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>3/最高15</p> </td> <td> <p>100万</p> </td> <td> <p>是</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>3万/最高20万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ae.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>4/最高15</p> </td> <td> <p>120万</p> </td> <td> <p>是</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>2.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ae.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>6/最高15</p> </td> <td> <p>160万</p> </td> <td> <p>是</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ae.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>是</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8ae.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>20/最高25</p> </td> <td> <p>600万</p> </td> <td> <p>是</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>20万/无</p> </td> <td> <p>10/无</p> </td> </tr> <tr> <td> <p>ecs.g8ae.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>900万</p> </td> <td> <p>是</p> </td> <td> <p>150万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>25万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g8ae.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>1800万</p> </td> <td> <p>是</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>50万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>  
**说明**

ecs.g8ae.large、ecs.g8ae.xlarge需开启巨型帧，才能达到15 Gbit/s的突发带宽。更多详情，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

### 通用型实例规格族g7a

* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：视频编解码，高网络包收发场景，网站和应用服务器，中小型数据库系统、缓存、搜索集群，游戏服务器，测试开发（例如DevOps），其他通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.55 GHz主频的AMD EPYC^™^ MILAN处理器，单核睿频最高3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g7a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g7a.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1/最高10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>1.25万/最高11万</p> </td> <td> <p>1/最高6</p> </td> </tr> <tr> <td> <p>ecs.g7a.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5/最高10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>2万/最高11万</p> </td> <td> <p>1.5/最高6</p> </td> </tr> <tr> <td> <p>ecs.g7a.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5/最高10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>3万/最高11万</p> </td> <td> <p>2/最高6</p> </td> </tr> <tr> <td> <p>ecs.g7a.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>7/最高12.5</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>6万/最高11万</p> </td> <td> <p>3.7/最高10.5</p> </td> </tr> <tr> <td> <p>ecs.g7a.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/最高10</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>7.5万/最高11万</p> </td> <td> <p>4.1/最高11</p> </td> </tr> <tr> <td> <p>ecs.g7a.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>600万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>15万/无</p> </td> <td> <p>8.2/无</p> </td> </tr> <tr> <td> <p>ecs.g7a-nps1.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>600万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>15万/无</p> </td> <td> <p>8.2/无</p> </td> </tr> <tr> <td> <p>ecs.g7a.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>200万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>30万/无</p> </td> <td> <p>16.4/无</p> </td> </tr> </tbody> </table>  
**说明**

Ubuntu 16或Debian 9操作系统内核不支持AMD EPYC^™^ MILAN处理器，因此当您选用该类实例规格后，请勿搭配Ubuntu 16或Debian 9镜像创建实例，否则实例会启动失败。

### 通用型实例规格族g7

* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**： 高网络包收发场景（例如视频弹幕、电信业务转发等），游戏服务器，中小型数据库系统、缓存、搜索集群，各种类型和规模的企业级应用，网站和应用服务器，数据分析和计算，安全可信计算场景，区块链场景。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

    **说明**

    该规格族的实例可能运行在不同的服务器平台，包括Ice Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Ice Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

  * 支持阿里云虚拟化Enclave特性，提供基于虚拟化的机密计算环境。更多信息，请参见[构建Enclave机密计算环境](https://help.aliyun.com/document_detail/203433.html#task-2038130)。

g7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>支持vTPM</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>最大挂载数据盘数量</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g7.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2/最高12.5</p> </td> <td> <p>110万</p> </td> <td> <p>是</p> </td> <td> <p>最高50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>2万/最高16万</p> </td> <td> <p>1.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>3/最高12.5</p> </td> <td> <p>110万</p> </td> <td> <p>是</p> </td> <td> <p>最高50万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>8</p> </td> <td> <p>4万/最高16万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>5/最高15</p> </td> <td> <p>160万</p> </td> <td> <p>是</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>16</p> </td> <td> <p>5万/最高16万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>8/最高15</p> </td> <td> <p>240万</p> </td> <td> <p>是</p> </td> <td> <p>最高50万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>16</p> </td> <td> <p>7万/最高16万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>10/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>是</p> </td> <td> <p>50万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>8万/最高16万</p> </td> <td> <p>5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g7.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>12/最高25</p> </td> <td> <p>450万</p> </td> <td> <p>是</p> </td> <td> <p>55万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>11万/最高16万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.g7.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/最高32</p> </td> <td> <p>600万</p> </td> <td> <p>是</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>24</p> </td> <td> <p>16万/无</p> </td> <td> <p>10/无</p> </td> </tr> <tr> <td> <p>ecs.g7.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>是</p> </td> <td> <p>120万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32</p> </td> <td> <p>36万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.g7.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>是</p> </td> <td> <p>240万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32</p> </td> <td> <p>60万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

### 海光通用型实例规格族g9h

* **规格族介绍**：采用阿里云CIPU架构，搭配海光4号C86-4G平台处理器，可提供稳定的国产化算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：数据库，网络Web类应用，大数据分析（Spark/Flink/ES等），搜索/推荐/广告（ps-worker），核心交易系统，音视频转码，AI训练与推理，通用的企业级应用（Java）等。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用海光4代可扩展处理器Hygon C86-4G，睿频最高3.1 GHz，国产化算力，安全可靠，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

g9h包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4/IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g9h.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.5/12.5</p> </td> <td> <p>90万</p> </td> <td> <p>25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>2万/11万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.g9h.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2.5/12.5</p> </td> <td> <p>100万</p> </td> <td> <p>25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>3万/11万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.g9h.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>4/12.5</p> </td> <td> <p>160万</p> </td> <td> <p>25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>4.5万/11万</p> </td> <td> <p>2.5/10</p> </td> </tr> <tr> <td> <p>ecs.g9h.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>7/12.5</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>6万/11万</p> </td> <td> <p>3.5/10</p> </td> </tr> <tr> <td> <p>ecs.g9h.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>8万/11万</p> </td> <td> <p>5/10</p> </td> </tr> </tbody> </table>

### 海光通用型实例规格族g7h

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：视频编解码，高网络包收发场景，网站和应用服务器，中小型数据库系统、缓存、搜索集群，测试开发（例如DevOps），其他通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用海光3代可扩展处理器Hygon C86-3G 7390，睿频最高3.0 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ： 支持安全加密虚拟化（China Secure Virtualization，简称CSV），关于CSV的更多信息，请参见[构建CSV机密计算环境](https://help.aliyun.com/document_detail/2507879.html)。

g7h包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS（万）</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>可挂载的云盘数</b></p> </td> <td> <p><b>云盘 IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g7h.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.5/10</p> </td> <td> <p>50</p> </td> <td> <p>25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>16</p> </td> <td> <p>2万/最高10万</p> </td> <td> <p>1/4</p> </td> </tr> <tr> <td> <p>ecs.g7h.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2.5/10</p> </td> <td> <p>90</p> </td> <td> <p>25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>10</p> </td> <td> <p>16</p> </td> <td> <p>3万/最高10万</p> </td> <td> <p>1.5/4</p> </td> </tr> <tr> <td> <p>ecs.g7h.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>3/10</p> </td> <td> <p>120</p> </td> <td> <p>25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>10</p> </td> <td> <p>16</p> </td> <td> <p>4万/最高10万</p> </td> <td> <p>2/4</p> </td> </tr> <tr> <td> <p>ecs.g7h.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>4/10</p> </td> <td> <p>150</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>6万/最高10万</p> </td> <td> <p>3/4</p> </td> </tr> <tr> <td> <p>ecs.g7h.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/无</p> </td> <td> <p>200</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>10万/无</p> </td> <td> <p>4/无</p> </td> </tr> <tr> <td> <p>ecs.g7h.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>400</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>18万/无</p> </td> <td> <p>8/无</p> </td> </tr> </tbody> </table>

### 海光通用型实例规格族g6h

g6h仅支持在金融云中购买。关于如何申请金融云认证，请参见[申请金融云认证](https://help.aliyun.com/document_detail/29856.html)。  
* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：视频编解码，高网络包收发场景，网站和应用服务器，中小型数据库系统、缓存、搜索集群，测试开发（例如DevOps），其他通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用海光2代可扩展处理器7280，基频2.0 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6h包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6h.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.2/5</p> </td> <td> <p>50万</p> </td> <td> <p>25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>1.5万/最高7.5万</p> </td> <td> <p>1/4</p> </td> </tr> <tr> <td> <p>ecs.g6h.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2/8</p> </td> <td> <p>75万</p> </td> <td> <p>25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>2万/最高7.5万</p> </td> <td> <p>1.5/4</p> </td> </tr> <tr> <td> <p>ecs.g6h.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>3/8</p> </td> <td> <p>90万</p> </td> <td> <p>25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>3万/最高7.5万</p> </td> <td> <p>2/4</p> </td> </tr> <tr> <td> <p>ecs.g6h.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>4/8</p> </td> <td> <p>120万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>5万/最高7.5万</p> </td> <td> <p>3/4</p> </td> </tr> <tr> <td> <p>ecs.g6h.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/无</p> </td> <td> <p>200万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>7.5万/无</p> </td> <td> <p>4/无</p> </td> </tr> <tr> <td> <p>ecs.g6h.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>12/无</p> </td> <td> <p>400万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>15万/无</p> </td> <td> <p>8/无</p> </td> </tr> </tbody> </table>

### 通用型实例规格族g6

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  **说明**

  该规格族不支持FreeBSD 13.2及更早版本，存在兼容性问题，请使用FreeBSD 13.3或更高版本。

  该规格族的实例可能运行在不同的服务器平台，包括 Cascade Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Cascade Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    不同实例规格族的云盘性能上限不同，本规格族的单台实例最高支持20万IOPS。
  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

    **说明**

    不同实例规格族提供的网络性能不同，如果需要更高的并发连接能力和网络收发包能力，建议您选用g7ne。
  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1/最高3</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g6.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5/最高5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.g6.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5/最高8</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.g6.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>4/最高10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.g6.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5/最高10</p> </td> <td> <p>100万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.g6.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>7.5/最高10</p> </td> <td> <p>150万</p> </td> <td> <p>45万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>5万</p> </td> <td> <p>4</p> </td> </tr> <tr> <td> <p>ecs.g6.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10/无</p> </td> <td> <p>200万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.g6.13xlarge</p> </td> <td> <p>52</p> </td> <td> <p>192</p> </td> <td> <p>12.5/无</p> </td> <td> <p>300万</p> </td> <td> <p>90万</p> </td> <td> <p>32</p> </td> <td> <p>7</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>10万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.g6.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>384</p> </td> <td> <p>25/无</p> </td> <td> <p>600万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> <td> <p>20万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

### 通用型实例规格族g6a

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 视频编解码。

  * 高网络包收发场景。

  * 网站和应用服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 游戏服务器。

  * 测试开发，例如DevOps。

  * 其他通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.6 GHz主频的AMD EPYC^™^ ROME处理器，睿频3.3 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6a.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1/10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>1.25万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g6a.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5/10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>3</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.g6a.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5/10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>3万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.g6a.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5/10</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>6万</p> </td> <td> <p>3.1</p> </td> </tr> <tr> <td> <p>ecs.g6a.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/10</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>7.5万</p> </td> <td> <p>4.1</p> </td> </tr> <tr> <td> <p>ecs.g6a.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>600万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>15万</p> </td> <td> <p>8.2</p> </td> </tr> <tr> <td> <p>ecs.g6a.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>200万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>16.4</p> </td> </tr> </tbody> </table>

### 通用平衡增强型实例规格族g6e

* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比约为1:4。

  * 处理器：2.5 GHz主频、3.2 GHz睿频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  **说明**

  该规格族不支持FreeBSD 13.2及更早版本，存在兼容性问题，请使用FreeBSD 13.3或更高版本。

  该规格族的实例可能运行在不同的服务器平台，包括 Cascade Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Cascade Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

    **说明**

    不同实例规格族提供的网络性能不同，如果需要更高的并发连接能力和网络收发包能力，建议您选用g7ne。
  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6e.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.2/最高10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>2万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g6e.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2/最高10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>4万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.g6e.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>3/最高10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.g6e.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>6/最高10</p> </td> <td> <p>300万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>8万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.g6e.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10/无</p> </td> <td> <p>600万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>15万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.g6e.13xlarge</p> </td> <td> <p>52</p> </td> <td> <p>192</p> </td> <td> <p>16/无</p> </td> <td> <p>900万</p> </td> <td> <p>100万</p> </td> <td> <p>32</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>24万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.g6e.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>384</p> </td> <td> <p>32/无</p> </td> <td> <p>2400万</p> </td> <td> <p>180万</p> </td> <td> <p>32</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>48万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>  
**说明**

* 网络能力为单项测试最高能力。例如，单项测试网络带宽能力时，不会对网络收发包能力和其他指标同时做压力测试。

* 如需使用ecs.g6e.26xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 通用型实例规格族g5

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）或者8269CY（Cascade Lake），计算性能稳定。

    **说明**

    该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要将实例部署在同一服务器平台，建议您选用g9i。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    不同实例规格族的云盘性能上限不同，本规格族的单台实例最高支持20万IOPS。
* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

    **说明**

    不同实例规格族提供的网络性能不同，如果需要更高的并发连接能力和网络收发包能力，建议您选用g7ne。
  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g5.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>7.5</p> </td> <td> <p>150万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g5.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>20</p> </td> <td> <p>400万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

### 通用网络增强型实例规格族sn2ne

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）或Platinum 8163（Skylake）或8269CY（Cascade Lake），计算性能稳定。

    **说明**

    该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要部署在同一服务器平台，建议您选用g9i。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

sn2ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sn2ne.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2</p> </td> <td> <p>100万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>2.5</p> </td> <td> <p>130万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>3</p> </td> <td> <p>160万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>4.5</p> </td> <td> <p>200万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>6</p> </td> <td> <p>250万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.sn2ne.14xlarge</p> </td> <td> <p>56</p> </td> <td> <p>224</p> </td> <td> <p>10</p> </td> <td> <p>450万</p> </td> <td> <p>14</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>1</p> </td> </tr> </tbody> </table>

### 计算型实例规格族c9ae

* **规格族介绍** ：采用阿里云全新CIPU架构，搭配AMD最新EPYC^™^ Turin 处理器，采用物理核设计，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：大数据分析（Spark/Flink/ES等），搜索/推荐/广告（ps-worker），核心交易系统，音视频转码，AI训练与推理，通用的企业级应用（Java）等。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高3.7 GHz，采用物理核设计，计算性能稳定。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#6cc7ed4977cxh)。

* **存储**：

  * 支持调整存储基础带宽。

  * I/O优化实例。

  * 支持[NVMe协议](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持调整网络基础带宽。

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持[可信计算（vTPM）特性](https://help.aliyun.com/document_detail/201394.html)。

  * 支持[VPC流量加密](https://help.aliyun.com/document_detail/2932958.html)。

c9ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c9ae.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2.5/最高25</p></td> <td><p>最高150万</p></td> <td><p>最高50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>最高20万</p></td> <td><p>2.5/最高20</p></td> </tr> <tr> <td><p>ecs.c9ae.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4//最高25</p></td> <td><p>最高160万</p></td> <td><p>最高50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>最高20万</p></td> <td><p>3/最高20</p></td> </tr> <tr> <td><p>ecs.c9ae.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>6/最高25</p></td> <td><p>最高250万</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>最高20万</p></td> <td><p>4/最高20</p></td> </tr> <tr> <td><p>ecs.c9ae.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>10/最高25</p></td> <td><p>最高320万</p></td> <td><p>最高50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>最高20万</p></td> <td><p>5.5/最高20</p></td> </tr> <tr> <td><p>ecs.c9ae.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>16/最高25</p></td> <td><p>最高500万</p></td> <td><p>最高100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>最高20万</p></td> <td><p>8/最高20</p></td> </tr> <tr> <td><p>ecs.c9ae.12xlarge</p></td> <td><p>48</p></td> <td><p>96</p></td> <td><p>25/无</p></td> <td><p>750万</p></td> <td><p>150万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万</p></td> <td><p>13/无</p></td> </tr> <tr> <td><p>ecs.c9ae.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>1000万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.c9ae.24xlarge</p></td> <td><p>96</p></td> <td><p>192</p></td> <td><p>50/无</p></td> <td><p>1500万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>25/无</p></td> </tr> <tr> <td><p>ecs.c9ae.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>40万</p></td> <td><p>32/无</p></td> </tr> <tr> <td><p>ecs.c9ae.48xlarge</p></td> <td><p>192</p></td> <td><p>384</p></td> <td><p>100/无</p></td> <td><p>3000万</p></td> <td><p>600万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>60万</p></td> <td><p>50/无</p></td> </tr> </tbody> </table>

### 计算型实例规格族c9a

* **规格族介绍** ：采用阿里云全新CIPU架构，搭配AMD最新EPYC^™^ Turin 处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：大中型数据库系统，游戏服务器，金融量化，区块链，网站和应用服务器以及其他通用企业级应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高4.1 GHz，计算性能稳定。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#6cc7ed4977cxh)。

* **存储**：

  * I/O优化实例。

  * 支持[NVMe协议](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持[可信计算（vTPM）特性](https://help.aliyun.com/document_detail/201394.html)。

c9a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c9a.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2.5/最高15</p></td> <td><p>最高120万</p></td> <td><p>最高50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>最高11万</p></td> <td><p>2/最高15</p></td> </tr> <tr> <td><p>ecs.c9a.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4//最高15</p></td> <td><p>最高140万</p></td> <td><p>最高50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>最高11万</p></td> <td><p>3/最高15</p></td> </tr> <tr> <td><p>ecs.c9a.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>6/最高15</p></td> <td><p>最高200万</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>最高11万</p></td> <td><p>4/最高15</p></td> </tr> <tr> <td><p>ecs.c9a.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>12/最高25</p></td> <td><p>最高300万</p></td> <td><p>最高50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>最高11万</p></td> <td><p>5/最高15</p></td> </tr> <tr> <td><p>ecs.c9a.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>16/最高32</p></td> <td><p>最高400万</p></td> <td><p>最高80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>最高11万</p></td> <td><p>8/最高15</p></td> </tr> <tr> <td><p>ecs.c9a.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>750万</p></td> <td><p>150万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万</p></td> <td><p>16/无</p></td> </tr> </tbody> </table>

### 计算型实例规格族c9i

* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：机器学习推理应用，数据分析、批量计算、视频编码，游戏服务器前端，高性能科学和工程应用，Web前端服务器。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，单核最大睿频3.9GHz。

    **说明**

    该实例在系统中可能会存在不同的频率显示，其中单核最高睿频3.9 GHz，属于突发性能，突发能力与物理机CPU整机负载相关，无法作为SLA承诺。
  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

c9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c9i.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2.5/最高15</p></td> <td><p>100万</p></td> <td><p>最高50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2.5万/最高20万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.c9i.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4/最高15</p></td> <td><p>120万</p></td> <td><p>最高50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/最高10</p></td> </tr> <tr> <td><p>ecs.c9i.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>6/最高15</p></td> <td><p>160万</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/最高10</p></td> </tr> <tr> <td><p>ecs.c9i.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>10/最高15</p></td> <td><p>240万</p></td> <td><p>最高50万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.c9i.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>12/最高25</p></td> <td><p>300万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/最高10</p></td> </tr> <tr> <td><p>ecs.c9i.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>15/最高25</p></td> <td><p>450万</p></td> <td><p>60万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>7.5/最高10</p></td> </tr> <tr> <td><p>ecs.c9i.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>20/最高32</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/最高30万</p></td> <td><p>10/最高12</p></td> </tr> <tr> <td><p>ecs.c9i.12xlarge</p></td> <td><p>48</p></td> <td><p>96</p></td> <td><p>25/最高32</p></td> <td><p>900万</p></td> <td><p>160万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24万/最高32万</p></td> <td><p>12/最高15</p></td> </tr> <tr> <td><p>ecs.c9i.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>28/最高36</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/最高40万</p></td> <td><p>16/最高24</p></td> </tr> <tr> <td><p>ecs.c9i.24xlarge</p></td> <td><p>96</p></td> <td><p>192</p></td> <td><p>32/最高48</p></td> <td><p>1800万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>35万/最高60万</p></td> <td><p>20/最高28</p></td> </tr> <tr> <td><p>ecs.c9i.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>36/最高50</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>40万/最高65万</p></td> <td><p>24/最高28</p></td> </tr> <tr> <td><p>ecs.c9i.48xlarge</p></td> <td><p>192</p></td> <td><p>384</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>600万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/最高80万</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 计算型实例规格族c8a

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**： 大数据类应用，Web类应用，AI训练与推理，音视频转码类应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：AMD EPYC^™^ Genoa处理器，基频2.7 GHz，睿频最高3.7 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
c8a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c8a.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1.5/最高12.5</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高11万</p></td> <td><p>1.5/最高10</p></td> </tr> <tr> <td><p>ecs.c8a.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>2.5/最高12.5</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万/最高11万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.c8a.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>4/最高12.5</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4.5万/最高11万</p></td> <td><p>2.5/最高10</p></td> </tr> <tr> <td><p>ecs.c8a.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>7/最高12.5</p></td> <td><p>200万</p></td> <td><p>30万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>6万/最高11万</p></td> <td><p>3.5/最高10</p></td> </tr> <tr> <td><p>ecs.c8a.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10/最高25</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>8万/最高11万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.c8a.12xlarge</p></td> <td><p>48</p></td> <td><p>96</p></td> <td><p>16/25</p></td> <td><p>450万</p></td> <td><p>75万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/无</p></td> <td><p>8/最高10</p></td> </tr> <tr> <td><p>ecs.c8a.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>20/25</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.c8a.24xlarge</p></td> <td><p>96</p></td> <td><p>192</p></td> <td><p>32/无</p></td> <td><p>900万</p></td> <td><p>150万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.c8a.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>40/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.c8a.48xlarge</p></td> <td><p>192</p></td> <td><p>384</p></td> <td><p>64/无</p></td> <td><p>1800万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>  
**说明**

ecs.c8a.large、ecs.c8a.xlarge需开启巨型帧，才能达到12.5 Gbit/s突发带宽。更多详情，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

### 计算型实例规格族c8i

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**： 机器学习推理应用，数据分析、批量计算、视频编码，游戏服务器前端，高性能科学和工程应用，Web前端服务器。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

    **说明**

    购买该实例时，系统将随机分配上述两种处理器之一，不支持手动选择。
  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

  * 支持vTPM特性，依托TPM/TCM芯片，实现从服务器到实例的启动链可信度量，提供超高安全能力。

  * 4 vCPU以上规格的实例支持阿里云虚拟化Enclave特性，提供基于虚拟化的机密计算环境。更多信息，请参见[构建Enclave机密计算环境](https://help.aliyun.com/document_detail/203433.html#task-2038130)。

  * 采用英特尔TME（Total Memory Encryption）运行内存加密。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
c8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c8i.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2.5/最高15</p></td> <td><p>100万</p></td> <td><p>最高30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2.5万/最高20万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.c8i.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4/最高15</p></td> <td><p>120万</p></td> <td><p>最高30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/最高10</p></td> </tr> <tr> <td><p>ecs.c8i.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>6/最高15</p></td> <td><p>160万</p></td> <td><p>最高30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/最高10</p></td> </tr> <tr> <td><p>ecs.c8i.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>10/最高15</p></td> <td><p>240万</p></td> <td><p>最高30万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.c8i.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>12/最高25</p></td> <td><p>300万</p></td> <td><p>35万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/最高10</p></td> </tr> <tr> <td><p>ecs.c8i.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>15/最高25</p></td> <td><p>450万</p></td> <td><p>50万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>7.5/最高10</p></td> </tr> <tr> <td><p>ecs.c8i.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>20/最高25</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.c8i.12xlarge</p></td> <td><p>48</p></td> <td><p>96</p></td> <td><p>25/无</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.c8i.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>160万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>36万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.c8i.24xlarge</p></td> <td><p>96</p></td> <td><p>192</p></td> <td><p>50/无</p></td> <td><p>1800万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>50万/无</p></td> <td><p>24/无</p></td> </tr> <tr> <td><p>ecs.c8i.48xlarge</p></td> <td><p>192</p></td> <td><p>512</p></td> <td><p>100/无</p></td> <td><p>3000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>100万/无</p></td> <td><p>48/无</p></td> </tr> </tbody> </table>

### 网络增强计算型实例规格族c8ine

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**： 适用于网络密集型场景，转发、连接性能出色，尤其适用于做网络接入层网关，流量、数据转发或预处理中间件等。作为云上解决方案中的一部分，在大型网站、电商、AI等场景下都可应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多信息，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

c8ine包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>EBS多队列</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c8ine.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>4/最高24</p></td> <td><p>60万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万/最高8万</p></td> <td><p>2/最高8</p></td> </tr> <tr> <td><p>ecs.c8ine.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>7/最高28</p></td> <td><p>120万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>4万/最高8万</p></td> <td><p>2.5/最高8</p></td> </tr> <tr> <td><p>ecs.c8ine.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>12/最高35</p></td> <td><p>200万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>2</p></td> <td><p>5万/最高8万</p></td> <td><p>4/最高8</p></td> </tr> <tr> <td><p>ecs.c8ine.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>23/最高44</p></td> <td><p>350万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>8万/最高10万</p></td> <td><p>6/最高10</p></td> </tr> <tr> <td><p>ecs.c8ine.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>44/无</p></td> <td><p>700万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>4</p></td> <td><p>10万/无</p></td> <td><p>10/无</p></td> </tr> </tbody> </table>

### 计算平衡增强型实例规格族c8ae

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 人工智能场景，如深度学习与训练、AI推理等。

  * HPC等高性能科学计算场景。

  * 大中型数据库系统、缓存、搜索集群。

  * 大型在线游戏服务器。

  * 其他对性能要求较高的通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：3.4 GHz主频的AMD EPYC^™^ Genoa处理器，单核睿频最高3.75 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

c8ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c8ae.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>3/最高15</p></td> <td><p>100万</p></td> <td><p>是</p></td> <td><p>最高30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>3万/最高20万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.c8ae.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4/最高15</p></td> <td><p>120万</p></td> <td><p>是</p></td> <td><p>最高30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/最高10</p></td> </tr> <tr> <td><p>ecs.c8ae.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>6/最高15</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>最高30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>3/最高10</p></td> </tr> <tr> <td><p>ecs.c8ae.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>12/最高25</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/最高10</p></td> </tr> <tr> <td><p>ecs.c8ae.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>20/最高25</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.c8ae.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>900万</p></td> <td><p>是</p></td> <td><p>150万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>25万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.c8ae.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>64/无</p></td> <td><p>1800万</p></td> <td><p>是</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>  
**说明**

ecs.c8ae.large、ecs.c8ae.xlarge需开启巨型帧，才能达到15 Gbit/s突发带宽。更多详情，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

### 计算型实例规格族c7a

* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 视频编解码。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 测试开发，例如DevOps。

  * 数据分析、批量计算。

  * 高性能科学和工程应用。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.55 GHz主频的AMD EPYC^™^ MILAN处理器，单核睿频最高3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c7a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c7a.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1/最高10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>1.25万/最高11万</p></td> <td><p>1/最高6</p></td> </tr> <tr> <td><p>ecs.c7a.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1.5/最高10</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>2万/最高11万</p></td> <td><p>1.5/最高6</p></td> </tr> <tr> <td><p>ecs.c7a.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2.5/最高10</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万/最高11万</p></td> <td><p>2/最高6</p></td> </tr> <tr> <td><p>ecs.c7a.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>5/最高10</p></td> <td><p>200万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>6万/最高11万</p></td> <td><p>3/最高6</p></td> </tr> <tr> <td><p>ecs.c7a.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>8/最高10</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万/最高11万</p></td> <td><p>4/最高6</p></td> </tr> <tr> <td><p>ecs.c7a-nps1.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>8/最高10</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万/最高11万</p></td> <td><p>4/最高6</p></td> </tr> <tr> <td><p>ecs.c7a.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万/无</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.c7a-nps1.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>16/无</p></td> <td><p>300万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万/无</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.c7a.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> </tbody> </table>  
**说明**

Ubuntu 16或Debian 9操作系统内核不支持AMD EPYC^™^ MILAN处理器，因此当您选用该类实例规格后，请勿搭配Ubuntu 16或Debian 9镜像创建实例，否则实例会启动失败。

### 计算型实例规格族c7

* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 大型多人在线游戏（MMO）前端。

  * Web前端服务器。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

  * 安全可信计算场景。

  * 各种类型和规模的企业级应用。

  * 区块链场景。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

    **说明**

    该规格族的实例可能运行在不同的服务器平台，包括 Ice Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Ice Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

  * 支持阿里云虚拟化Enclave特性，提供基于虚拟化的机密计算环境。更多信息，请参见[构建Enclave机密计算环境](https://help.aliyun.com/document_detail/203433.html#task-2038130)。

c7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>最大挂载数据盘数量</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c7.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2/最高12.5</p></td> <td><p>110万</p></td> <td><p>是</p></td> <td><p>最高50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>2万/最高16万</p></td> <td><p>1.5/最高10</p></td> </tr> <tr> <td><p>ecs.c7.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>3/最高12.5</p></td> <td><p>110万</p></td> <td><p>是</p></td> <td><p>最高50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8</p></td> <td><p>4万/最高16万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.c7.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>5/最高15</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>5万/最高16万</p></td> <td><p>3/最高10</p></td> </tr> <tr> <td><p>ecs.c7.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>8/最高15</p></td> <td><p>240万</p></td> <td><p>是</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>7万/最高16万</p></td> <td><p>4/最高10</p></td> </tr> <tr> <td><p>ecs.c7.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>10/最高25</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>8万/最高16万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.c7.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>12/最高25</p></td> <td><p>450万</p></td> <td><p>是</p></td> <td><p>55万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>11万/16</p></td> <td><p>6/10</p></td> </tr> <tr> <td><p>ecs.c7.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>16/最高32</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>16万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.c7.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>是</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>36万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.c7.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>是</p></td> <td><p>240万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>60万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 计算型实例规格族c6

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  **说明**

  该规格族不支持FreeBSD 13.2及更早版本，存在兼容性问题，请使用FreeBSD 13.3或更高版本。

  该规格族的实例可能运行在不同的服务器平台，包括 Cascade Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Cascade Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    不同实例规格族的云盘性能上限不同，本规格族的单台实例最高支持20万IOPS。
  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c6.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1/最高3</p></td> <td><p>30万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c6.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1.5/最高5</p></td> <td><p>50万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.c6.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2.5/最高8</p></td> <td><p>80万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.c6.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>4/最高10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.c6.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>5/最高10</p></td> <td><p>100万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.c6.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>7.5/最高10</p></td> <td><p>150万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.c6.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10/无</p></td> <td><p>200万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.c6.13xlarge</p></td> <td><p>52</p></td> <td><p>96</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>90万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.c6.26xlarge</p></td> <td><p>104</p></td> <td><p>192</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 计算型实例规格族c6a

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**： 视频编解码，高网络包收发场景，Web前端服务器，大型多人在线游戏（MMO）前端，测试开发（例如DevOps）。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.6 GHz主频的AMD EPYC^™^ ROME处理器，睿频3.3 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c6a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c6a.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1/10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.25万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c6a.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1.5/10</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.c6a.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2.5/10</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.c6a.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>5/10</p></td> <td><p>200万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>3.1</p></td> </tr> <tr> <td><p>ecs.c6a.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>8/10</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>7.5万</p></td> <td><p>4.1</p></td> </tr> <tr> <td><p>ecs.c6a.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>15万</p></td> <td><p>8.2</p></td> </tr> <tr> <td><p>ecs.c6a.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>16.4</p></td> </tr> </tbody> </table>

### 计算平衡增强型实例规格族c6e

* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比约为1:2。

  * 处理器：2.5 GHz主频、3.2 GHz睿频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  **说明**

  该规格族不支持FreeBSD 13.2及更早版本，存在兼容性问题，请使用FreeBSD 13.3或更高版本。

  该规格族的实例可能运行在不同的服务器平台，包括 Cascade Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Cascade Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

    **说明**

    不同实例规格族提供的网络性能不同，如果需要更高的并发连接能力和网络收发包能力，建议您选用g7ne。
  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c6e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c6e.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1.2/最高10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c6e.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>2/最高10</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.c6e.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>3/最高10</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.c6e.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>6/最高10</p></td> <td><p>300万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>8万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.c6e.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10/无</p></td> <td><p>600万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>15万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.c6e.13xlarge</p></td> <td><p>52</p></td> <td><p>96</p></td> <td><p>16/无</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>24万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.c6e.26xlarge</p></td> <td><p>104</p></td> <td><p>192</p></td> <td><p>32/无</p></td> <td><p>2400万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>48万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 计算型实例规格族c5

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）或者8269CY（Cascade Lake），计算性能稳定。

    **说明**

    该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要将实例部署在同一服务器平台，建议您选用c9i。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    不同实例规格族的云盘性能上限不同，本规格族的单台实例最高支持20万IOPS。
* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c5.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c5.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c5.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2.5</p></td> <td><p>80万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c5.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>4</p></td> <td><p>90万</p></td> <td><p>4</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c5.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>5</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c5.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>7.5</p></td> <td><p>150万</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c5.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10</p></td> <td><p>200万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c5.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>20</p></td> <td><p>400万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> </tbody> </table>

### 密集计算型实例规格族ic5

* **适用场景**：

  * Web前端服务器。

  * 数据分析、批量计算、视频编码。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 大型多人在线游戏（MMO）前端。

* **计算**：

  * 处理器与内存配比为1:1。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）或者8269CY（Cascade Lake），计算性能稳定，全核睿频2.7 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 仅支持IPv4。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

ic5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.ic5.large</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.ic5.xlarge</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.ic5.2xlarge</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>2.5</p></td> <td><p>80万</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.ic5.3xlarge</p></td> <td><p>12</p></td> <td><p>12</p></td> <td><p>4</p></td> <td><p>90万</p></td> <td><p>4</p></td> <td><p>6</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.ic5.4xlarge</p></td> <td><p>16</p></td> <td><p>16</p></td> <td><p>5</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.ic5.6xlarge</p></td> <td><p>24</p></td> <td><p>24</p></td> <td><p>7.5</p></td> <td><p>150万</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.ic5.8xlarge</p></td> <td><p>32</p></td> <td><p>32</p></td> <td><p>10</p></td> <td><p>200万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.ic5.16xlarge</p></td> <td><p>64</p></td> <td><p>64</p></td> <td><p>20</p></td> <td><p>300万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> </tbody> </table>

### 计算网络增强型实例规格族sn1ne

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）或Platinum 8163（Skylake）或8269CY（Cascade Lake），计算性能稳定。

    **说明**

    该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要将实例部署在同一服务器平台，建议您选用c9i。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：仅支持SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

sn1ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.sn1ne.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.sn1ne.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.sn1ne.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.sn1ne.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>2.5</p></td> <td><p>130万</p></td> <td><p>4</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.sn1ne.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>3</p></td> <td><p>160万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.sn1ne.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>4.5</p></td> <td><p>200万</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.sn1ne.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>6</p></td> <td><p>250万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> </tbody> </table>

### 内存型实例规格族r9ae

* **规格族介绍** ：采用阿里云全新CIPU架构，搭配AMD最新EPYC^™^ Turin 处理器，采用物理核设计，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：大数据分析（Spark/Flink/ES等），搜索/推荐/广告（ps-worker），核心交易系统，音视频转码，AI训练与推理，通用的企业级应用（Java）等。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高3.7 GHz，采用物理核设计，计算性能稳定。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#6cc7ed4977cxh)。

* **存储**：

  * 支持调整存储基础带宽。

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持调整网络基础带宽。

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持[可信计算（vTPM）特性](https://help.aliyun.com/document_detail/201394.html)。

  * 支持[VPC流量加密](https://help.aliyun.com/document_detail/2932958.html)。

r9ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r9ae.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2.5/最高25</p></td> <td><p>最高150万</p></td> <td><p>最高50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>最高20万</p></td> <td><p>2.5/最高20</p></td> </tr> <tr> <td><p>ecs.r9ae.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>4//最高25</p></td> <td><p>最高160万</p></td> <td><p>最高50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>最高20万</p></td> <td><p>3/最高20</p></td> </tr> <tr> <td><p>ecs.r9ae.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>6/最高25</p></td> <td><p>最高250万</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>最高20万</p></td> <td><p>4/最高20</p></td> </tr> <tr> <td><p>ecs.r9ae.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>10/最高25</p></td> <td><p>最高320万</p></td> <td><p>最高50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>最高20万</p></td> <td><p>5.5/最高20</p></td> </tr> <tr> <td><p>ecs.r9ae.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>16/最高25</p></td> <td><p>最高500万</p></td> <td><p>最高100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>最高20万</p></td> <td><p>8/最高20</p></td> </tr> <tr> <td><p>ecs.r9ae.12xlarge</p></td> <td><p>48</p></td> <td><p>384</p></td> <td><p>25/无</p></td> <td><p>750万</p></td> <td><p>150万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万</p></td> <td><p>13/无</p></td> </tr> <tr> <td><p>ecs.r9ae.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>32/无</p></td> <td><p>1000万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.r9ae.24xlarge</p></td> <td><p>96</p></td> <td><p>768</p></td> <td><p>50/无</p></td> <td><p>1500万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>25/无</p></td> </tr> <tr> <td><p>ecs.r9ae.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>40万</p></td> <td><p>32/无</p></td> </tr> <tr> <td><p>ecs.r9ae.48xlarge</p></td> <td><p>192</p></td> <td><p>1536</p></td> <td><p>100/无</p></td> <td><p>3000万</p></td> <td><p>600万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>60万</p></td> <td><p>50/无</p></td> </tr> </tbody> </table>

### 内存型实例规格族r9a

* **规格族介绍** ：采用阿里云全新CIPU架构，搭配AMD最新EPYC^™^ Turin 处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：大中型数据库系统，游戏服务器，金融量化，区块链，网站和应用服务器以及其他通用企业级应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：AMD EPYC^™^ Turin处理器，睿频最高4.1 GHz，计算性能稳定。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#6cc7ed4977cxh)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持[可信计算（vTPM）特性](https://help.aliyun.com/document_detail/201394.html)。

r9a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r9a.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2.5/最高15</p></td> <td><p>最高120万</p></td> <td><p>最高50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>最高11万</p></td> <td><p>2/最高15</p></td> </tr> <tr> <td><p>ecs.r9a.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>4//最高15</p></td> <td><p>最高140万</p></td> <td><p>最高50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>最高11万</p></td> <td><p>3/最高15</p></td> </tr> <tr> <td><p>ecs.r9a.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>6/最高15</p></td> <td><p>最高200万</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>最高11万</p></td> <td><p>4/最高15</p></td> </tr> <tr> <td><p>ecs.r9a.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>12/最高25</p></td> <td><p>最高300万</p></td> <td><p>最高50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>最高11万</p></td> <td><p>5/最高15</p></td> </tr> <tr> <td><p>ecs.r9a.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>16/最高32</p></td> <td><p>最高400万</p></td> <td><p>最高80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>最高11万</p></td> <td><p>8/最高15</p></td> </tr> </tbody> </table>

### 内存型实例规格族r9i

* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：数据分析与挖掘、Hadoop、Spark集群以及其他企业大内存需求应用、分布式内存缓存（比如Redis）、网站和应用服务器。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，单核最大睿频3.9GHz。

    **说明**

    该实例在系统中可能会存在不同的频率显示，其中单核最高睿频3.9 GHz，属于突发性能，突发能力与物理机CPU整机负载相关，无法作为SLA承诺。
  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

r9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r9i.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2.5/最高15</p></td> <td><p>100万</p></td> <td><p>最高50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2.5万/最高20万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.r9i.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>4/最高15</p></td> <td><p>120万</p></td> <td><p>最高50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/最高10</p></td> </tr> <tr> <td><p>ecs.r9i.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>6/最高15</p></td> <td><p>160万</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/最高10</p></td> </tr> <tr> <td><p>ecs.r9i.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>10/最高15</p></td> <td><p>240万</p></td> <td><p>最高50万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.r9i.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>12/最高25</p></td> <td><p>300万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/最高10</p></td> </tr> <tr> <td><p>ecs.r9i.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>15/最高25</p></td> <td><p>450万</p></td> <td><p>60万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>7.5/最高10</p></td> </tr> <tr> <td><p>ecs.r9i.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>20/最高32</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/最高30万</p></td> <td><p>10/最高12</p></td> </tr> <tr> <td><p>ecs.r9i.12xlarge</p></td> <td><p>48</p></td> <td><p>384</p></td> <td><p>25/最高32</p></td> <td><p>900万</p></td> <td><p>160万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24万/最高32万</p></td> <td><p>12/最高15</p></td> </tr> <tr> <td><p>ecs.r9i.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>28/最高36</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/最高40万</p></td> <td><p>16/最高24</p></td> </tr> <tr> <td><p>ecs.r9i.24xlarge</p></td> <td><p>96</p></td> <td><p>768</p></td> <td><p>32/最高48</p></td> <td><p>1800万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>35万/最高60万</p></td> <td><p>20/最高28</p></td> </tr> <tr> <td><p>ecs.r9i.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>36/最高50</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>40万/最高65万</p></td> <td><p>24/最高28</p></td> </tr> <tr> <td><p>ecs.r9i.48xlarge</p></td> <td><p>192</p></td> <td><p>1536</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>600万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/最高80万</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 内存型实例规格族r8a

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 对内存容量要求较高的通用企业级应用（Java）。

  * 各种内存型数据库应用（Redis、Memcache）。

  * 大数据类应用（Kafka、ElasticSearch等）。

  * 音视频转码类应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：AMD EPYC™ Genoa处理器，基频2.7 GHz，睿频最高3.7 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
r8a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r8a.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1.5/最高12.5</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高11万</p></td> <td><p>1.5/最高10</p></td> </tr> <tr> <td><p>ecs.r8a.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>2.5/最高12.5</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万/最高11万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.r8a.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>4/最高12.5</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4.5万/最高11万</p></td> <td><p>2.5/最高10</p></td> </tr> <tr> <td><p>ecs.r8a.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>7/最高12.5</p></td> <td><p>200万</p></td> <td><p>30万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>6万/最高11万</p></td> <td><p>3.5/最高10</p></td> </tr> <tr> <td><p>ecs.r8a.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>10/最高25</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>8万/最高11万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.r8a.12xlarge</p></td> <td><p>48</p></td> <td><p>384</p></td> <td><p>16/25</p></td> <td><p>450万</p></td> <td><p>75万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/无</p></td> <td><p>8/最高10</p></td> </tr> <tr> <td><p>ecs.r8a.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>20/25</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.r8a.24xlarge</p></td> <td><p>96</p></td> <td><p>768</p></td> <td><p>32/无</p></td> <td><p>900万</p></td> <td><p>150万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.r8a.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>40/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.r8a.48xlarge</p></td> <td><p>192</p></td> <td><p>1536</p></td> <td><p>64/无</p></td> <td><p>1800万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>  
**说明**

* ecs.r8a.large、ecs.r8a.xlarge需开启巨型帧，才能达到12.5 Gbit/s突发带宽。更多详情，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

* 如需使用ecs.r8a.48xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 内存型实例规格族r8i

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 数据分析与挖掘。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

  * 分布式内存缓存，比如Redis。

  * 网站和应用服务器。

  * 大型多人在线游戏（MMO）服务器。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

  * 4 vCPU以上规格的实例支持阿里云虚拟化Enclave特性，提供基于虚拟化的机密计算环境。更多信息，请参见[构建Enclave机密计算环境](https://help.aliyun.com/document_detail/203433.html#task-2038130)。

  * 采用英特尔TME（Total Memory Encryption）运行内存加密。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
r8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r8i.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2.5/最高15</p></td> <td><p>100万</p></td> <td><p>最高30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2.5万/最高20万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.r8i.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>4/最高15</p></td> <td><p>120万</p></td> <td><p>最高30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/最高10</p></td> </tr> <tr> <td><p>ecs.r8i.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>6/最高15</p></td> <td><p>160万</p></td> <td><p>最高30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/最高10</p></td> </tr> <tr> <td><p>ecs.r8i.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>10/最高15</p></td> <td><p>240万</p></td> <td><p>最高30万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.r8i.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>12/最高25</p></td> <td><p>300万</p></td> <td><p>35万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/最高10</p></td> </tr> <tr> <td><p>ecs.r8i.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>15/最高25</p></td> <td><p>450万</p></td> <td><p>50万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>7.5/最高10</p></td> </tr> <tr> <td><p>ecs.r8i.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>20/最高25</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.r8i.12xlarge</p></td> <td><p>48</p></td> <td><p>384</p></td> <td><p>25/无</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.r8i.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>160万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>36万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.r8i.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>70万/无</p></td> <td><p>40/无</p></td> </tr> </tbody> </table>  
**说明**

如需使用ecs.r8i.16xlarge和ecs.r8i.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 内存平衡增强型实例规格族r8ae

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 人工智能场景，如深度学习与训练、AI推理等。

  * HPC等高性能科学计算场景。

  * 大中型数据库系统、缓存、搜索集群。

  * 大型在线游戏服务器。

  * 其他对性能要求较高的通用类型的企业级应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：3.4 GHz主频的AMD EPYC^™^ Genoa处理器，单核睿频最高3.75 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

r8ae包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r8ae.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>3/最高15</p></td> <td><p>100万</p></td> <td><p>是</p></td> <td><p>最高30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>3万/最高20万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.r8ae.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>4/最高15</p></td> <td><p>120万</p></td> <td><p>是</p></td> <td><p>最高30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/最高10</p></td> </tr> <tr> <td><p>ecs.r8ae.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>6/最高15</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>最高30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>3/最高10</p></td> </tr> <tr> <td><p>ecs.r8ae.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>12/最高25</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/最高10</p></td> </tr> <tr> <td><p>ecs.r8ae.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>20/最高25</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/无</p></td> <td><p>10/无</p></td> </tr> </tbody> </table>  
**说明**

ecs.r8ae.large、ecs.r8ae.xlarge需开启巨型帧，才能达到15 Gbit/s突发带宽。更多详情，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

### 内存型实例规格族r7p

* **规格族介绍**：

  * 基于持久内存技术，提供性价比更高的内存介质。

    **说明**

    本规格族提供的内存混合了普通内存与持久内存。建议您在上线应用前进行充分的测试，必要的时候，需要对应用进行适当改造以获得最佳的性价比。
  * 依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 内存型数据库，例如Redis。关于如何快速部署Redis应用，请参见[在配备持久内存的实例上部署Redis应用](https://help.aliyun.com/document_detail/188250.html#task-1986409)。

  * 需要大容量Page Cache的应用，例如RocketMQ等消息中间件。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop集群、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存（内存+持久内存）配比约为1:12。

  * 处理器：采用第三代Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

r7p包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>持久内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r7p.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>15.75</p></td> <td><p>2/10</p></td> <td><p>90万</p></td> <td><p>25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/11万</p></td> <td><p>1.5/6</p></td> </tr> <tr> <td><p>ecs.r7p.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>31.5</p></td> <td><p>3/10</p></td> <td><p>100万</p></td> <td><p>25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4万/11万</p></td> <td><p>2/6</p></td> </tr> <tr> <td><p>ecs.r7p.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>63</p></td> <td><p>5/10</p></td> <td><p>160万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/11万</p></td> <td><p>3/6</p></td> </tr> <tr> <td><p>ecs.r7p.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>504</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.r7p.32xlarge</p></td> <td><p>128</p></td> <td><p>512</p></td> <td><p>1008</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>200万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>60万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 内存型实例规格族r7a

* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：2.55 GHz主频的AMD EPYC^™^ MILAN处理器，单核睿频最高3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **适用场景**：

  * 高性能数据库、内存数据库。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业级大内存需求应用。

  * 区块链应用。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

r7a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r7a.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1/最高10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>1.25万/最高11万</p></td> <td><p>1/最高6</p></td> </tr> <tr> <td><p>ecs.r7a.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>1.5/最高10</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>2万/最高11万</p></td> <td><p>1.5/最高6</p></td> </tr> <tr> <td><p>ecs.r7a.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>2.5/最高10</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万/最高11万</p></td> <td><p>2/最高6</p></td> </tr> <tr> <td><p>ecs.r7a.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>5/最高10</p></td> <td><p>200万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>6万/最高11万</p></td> <td><p>3/最高6</p></td> </tr> <tr> <td><p>ecs.r7a.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>8/最高10</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万/最高11万</p></td> <td><p>4/最高6</p></td> </tr> <tr> <td><p>ecs.r7a-nps1.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>8/最高10</p></td> <td><p>300万</p></td> <td><p>8/最高10</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万/最高11万</p></td> <td><p>4/最高6</p></td> </tr> <tr> <td><p>ecs.r7a.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万/无</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.r7a-nps1.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万/无</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.r7a.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> </tbody> </table>  
**说明**

Ubuntu 16或Debian 9操作系统内核不支持AMD EPYC^™^ MILAN处理器，因此当您选用该类实例规格后，请勿搭配Ubuntu 16或Debian 9镜像创建实例，否则实例会启动失败。

### 内存型实例规格族r7

* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 高性能数据库、内存数据库。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

  * 安全可信计算场景。

* **计算**：

  * 处理器与内存配比为1:8

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定

  * 支持开启或关闭超线程配置

    **说明**

    该规格族的实例可能运行在不同的服务器平台，包括 Ice Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Ice Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全**：

  * 支持可信计算（vTPM）特性。更多信息，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

  * 支持阿里云虚拟化Enclave特性，提供基于虚拟化的机密计算环境。更多信息，请参见[构建Enclave机密计算环境](https://help.aliyun.com/document_detail/203433.html#task-2038130)。

r7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>最大挂载数据盘数量</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r7.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2/最高12.5</p></td> <td><p>110万</p></td> <td><p>是</p></td> <td><p>最高50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>2万/最高16万</p></td> <td><p>1.5/最高10</p></td> </tr> <tr> <td><p>ecs.r7.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>3/最高12.5</p></td> <td><p>110万</p></td> <td><p>是</p></td> <td><p>最高50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8</p></td> <td><p>4万/最高16万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.r7.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>5/最高15</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>5万/最高16万</p></td> <td><p>3/最高10</p></td> </tr> <tr> <td><p>ecs.r7.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>8/最高15</p></td> <td><p>240万</p></td> <td><p>是</p></td> <td><p>最高50万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>24</p></td> <td><p>7万/最高16万</p></td> <td><p>4/最高10</p></td> </tr> <tr> <td><p>ecs.r7.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>10/最高25</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>8万/最高16万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.r7.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>12/最高25</p></td> <td><p>450万</p></td> <td><p>是</p></td> <td><p>55万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>11万/16万</p></td> <td><p>6/10</p></td> </tr> <tr> <td><p>ecs.r7.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>16/最高32</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>16万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.r7.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>是</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>36万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.r7.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>是</p></td> <td><p>240万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>60万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 内存型实例规格族r6

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  **说明**

  该规格族不支持FreeBSD 13.2及更早版本，存在兼容性问题，请使用FreeBSD 13.3或更高版本。

  该规格族的实例可能运行在不同的服务器平台，包括 Cascade Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Cascade Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    不同实例规格族的云盘性能上限不同，本规格族的单台实例最高支持20万IOPS。
  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

r6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r6.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1/最高3</p></td> <td><p>30万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r6.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>1.5/最高5</p></td> <td><p>50万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.r6.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>2.5/最高8</p></td> <td><p>80万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.r6.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>4/最高10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.r6.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>5/最高10</p></td> <td><p>100万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.r6.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>7.5/最高10</p></td> <td><p>150万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.r6.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>10/无</p></td> <td><p>200万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.r6.13xlarge</p></td> <td><p>52</p></td> <td><p>384</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>90万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.r6.26xlarge</p></td> <td><p>104</p></td> <td><p>768</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 内存型实例规格族r6a

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**： 视频编解码，高网络包收发场景，内存型数据库，Hadoop、Spark等企业级大内存需求应用，测试开发（例如DevOps）。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：2.6 GHz主频的AMD EPYC^TM^ ROME处理器，睿频3.3 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#IXCNq)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

r6a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r6a.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1/10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.25万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r6a.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>1.5/10</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.r6a.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>2.5/10</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.r6a.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>5/10</p></td> <td><p>200万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>3.1</p></td> </tr> <tr> <td><p>ecs.r6a.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>8/10</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>7.5万</p></td> <td><p>4.1</p></td> </tr> <tr> <td><p>ecs.r6a.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>15万</p></td> <td><p>8.2</p></td> </tr> </tbody> </table>

### 内存平衡增强型实例规格族r6e

* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比约为1:8。

  * 处理器：2.5 GHz主频、3.2 GHz睿频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  **说明**

  该规格族不支持FreeBSD 13.2及更早版本，存在兼容性问题，请使用FreeBSD 13.3或更高版本。

  该规格族的实例可能运行在不同的服务器平台，包括 Cascade Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Cascade Lake平台）。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

    **说明**

不同实例规格族提供的网络性能不同，如果需要更高的并发连接能力和网络收发包能力，建议您选用g7ne。  
r6e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r6e.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1.2/最高10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r6e.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>2/最高10</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.r6e.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>3/最高10</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.r6e.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>6/最高10</p></td> <td><p>300万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>8万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.r6e.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>10/无</p></td> <td><p>600万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>15万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.r6e.13xlarge</p></td> <td><p>52</p></td> <td><p>384</p></td> <td><p>16/无</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>24万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.r6e.26xlarge</p></td> <td><p>104</p></td> <td><p>768</p></td> <td><p>32/无</p></td> <td><p>2400万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>48万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 内存型实例规格族r5

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）或者Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），计算性能稳定

    **说明**

    该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要将实例部署在同一服务器平台，建议您选用r9i。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    不同实例规格族的云盘性能上限不同，本规格族的单台实例最高支持20万IOPS。
* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

r5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r5.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r5.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r5.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>2.5</p></td> <td><p>80万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r5.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>4</p></td> <td><p>90万</p></td> <td><p>4</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r5.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>5</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r5.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>7.5</p></td> <td><p>150万</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r5.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>10</p></td> <td><p>200万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.r5.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>20</p></td> <td><p>400万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> </tbody> </table>

### 内存网络增强型实例规格族se1ne

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等

  * 高性能数据库、内存数据库

  * 数据分析与挖掘、分布式内存缓存

  * Hadoop、Spark集群以及其他企业大内存需求应用

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）或Platinum 8163（Skylake）或8269CY（Cascade Lake），计算性能稳定。

    **说明**

    该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要将实例部署在同一服务器平台，建议您选用r9i。
* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：支持SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

se1ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.se1ne.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.se1ne.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.se1ne.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>2</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.se1ne.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>2.5</p></td> <td><p>130万</p></td> <td><p>4</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.se1ne.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>3</p></td> <td><p>160万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.se1ne.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>4.5</p></td> <td><p>200万</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.se1ne.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>6</p></td> <td><p>250万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.se1ne.14xlarge</p></td> <td><p>56</p></td> <td><p>480</p></td> <td><p>10</p></td> <td><p>450万</p></td> <td><p>14</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> </tr> </tbody> </table>

### 内存型实例规格族se1

* **适用场景**：

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ E5-2682 v4（Broadwell）或Platinum 8163（Skylake）或8269CY（Cascade Lake），计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：支持SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 仅支持IPv4。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

se1包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.se1.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>0.5</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.se1.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.se1.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>1.5</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.se1.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>3</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.se1.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>6</p></td> <td><p>80万</p></td> <td><p>3</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.se1.14xlarge</p></td> <td><p>56</p></td> <td><p>480</p></td> <td><p>10</p></td> <td><p>120万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> </tbody> </table>

### 通用算力型实例规格族u2a

* **规格族介绍** ：采用阿里云全新CIPU架构，兼容多代际AMD EPYC^™^ 处理器（支持 AMD Turin 处理器），可提供企业级的算力输出。

* **适用场景**：

  * 中小型数据库（Redis/Mysql等）

  * APP应用服务器

  * 中间件（MQ/Kafka等）

  * 网站或网络接入层（Apache/Nginx等）

  * 其他企业内部系统（如开发测试、邮件系统等）

* **计算**：

  * 支持 CPU 核心数量与内存容量配比为1:1/1:2/1:4的实例规格。

  * 处理器：AMD EPYC^™^ 处理器，睿频最高3.7 GHz。

  * 与操作系统的兼容性说明，请参见[AMD实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/195843.html#33f69521a4b8a)。

* **存储**：

  * I/O优化实例

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD Entry云盘、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

u2a包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.u2a-c1m1.large</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>1.2/最高12.5</p> </td> <td> <p>最高90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.large</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>1.2/最高12.5</p> </td> <td> <p>最高90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1.2/最高12.5</p> </td> <td> <p>最高90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m1.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>2/最高12.5</p> </td> <td> <p>最高100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.6/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>2/最高12.5</p> </td> <td> <p>最高100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.6/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>2/最高12.5</p> </td> <td> <p>最高100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>1.6/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>3.2/最高12.5</p> </td> <td> <p>最高160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>3.2/最高12.5</p> </td> <td> <p>最高160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>2</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>最高11万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>32</p> </td> <td> <p>6/最高12.5</p> </td> <td> <p>最高200万</p> </td> <td> <p>最高25万</p> </td> <td> <p>16</p> </td> <td> <p>4</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>6/最高12.5</p> </td> <td> <p>最高200万</p> </td> <td> <p>最高25万</p> </td> <td> <p>16</p> </td> <td> <p>4</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>48</p> </td> <td> <p>7/最高12.5</p> </td> <td> <p>最高250万</p> </td> <td> <p>最高36万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>3.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>7/最高12.5</p> </td> <td> <p>最高250万</p> </td> <td> <p>最高36万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>3.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>64</p> </td> <td> <p>8/最高25</p> </td> <td> <p>最高300万</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/最高25</p> </td> <td> <p>最高300万</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>4/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>96</p> </td> <td> <p>13/最高25</p> </td> <td> <p>400万</p> </td> <td> <p>60万</p> </td> <td> <p>24</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>6.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>192</p> </td> <td> <p>13/最高25</p> </td> <td> <p>400万</p> </td> <td> <p>60万</p> </td> <td> <p>24</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>6.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m2.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>128</p> </td> <td> <p>16/最高25</p> </td> <td> <p>500万</p> </td> <td> <p>80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>8/最高10</p> </td> </tr> <tr> <td> <p>ecs.u2a-c1m4.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/最高25</p> </td> <td> <p>500万</p> </td> <td> <p>80万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>最高11万</p> </td> <td> <p>8/最高10</p> </td> </tr> </tbody> </table>

### 通用算力型实例规格族u2i

* **规格族介绍**：采用阿里云全新CIPU架构，兼容多代际服务器，支持Intel最新的第五代和第六代至强平台。

* **适用场景**：

  * 中小类型和规模的企业级应用

  * 网站和应用服务器

  * 数据分析和计算

  * 中小型数据库系统、缓存、搜索集群

* **计算**：

  * 处理器与内存配比为1:1/1:2/1:4/1:8

  * 处理器：Intel ^®^ Xeon ^®^ Platinum可扩展处理器

* **存储**：

  * I/O优化实例

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：ESSD Entry云盘、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

u2i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.u2i-c1m1.large</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>2/最高15</p> </td> <td> <p>90万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/最高20万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>3/最高15</p> </td> <td> <p>110万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4万/最高20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>5/最高15</p> </td> <td> <p>130万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>3/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>12</p> </td> <td> <p>8/最高15</p> </td> <td> <p>180万</p> </td> <td> <p>最高30万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>16</p> </td> <td> <p>10/最高25</p> </td> <td> <p>240万</p> </td> <td> <p>最高35万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>24</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>最高40万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m1.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>32</p> </td> <td> <p>16/最高32</p> </td> <td> <p>400万</p> </td> <td> <p>最高60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/最高30万</p> </td> <td> <p>8/12</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.large</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>2/最高15</p> </td> <td> <p>90万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/最高20万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>3/最高15</p> </td> <td> <p>110万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4万/最高20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>5/最高15</p> </td> <td> <p>130万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>3/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>24</p> </td> <td> <p>8/最高15</p> </td> <td> <p>180万</p> </td> <td> <p>最高30万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>32</p> </td> <td> <p>10/最高25</p> </td> <td> <p>240万</p> </td> <td> <p>最高35万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>48</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>最高40万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m2.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>64</p> </td> <td> <p>16/最高32</p> </td> <td> <p>400万</p> </td> <td> <p>最高60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/最高30万</p> </td> <td> <p>8/12</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2/最高15</p> </td> <td> <p>90万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/最高20万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>3/最高15</p> </td> <td> <p>110万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4万/最高20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>5/最高15</p> </td> <td> <p>130万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>3/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>8/最高15</p> </td> <td> <p>180万</p> </td> <td> <p>最高30万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>10/最高25</p> </td> <td> <p>240万</p> </td> <td> <p>最高35万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>最高40万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m4.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/最高32</p> </td> <td> <p>400万</p> </td> <td> <p>最高60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/最高30万</p> </td> <td> <p>8/12</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.large</p> </td> <td> <p>2</p> </td> <td> <p>16</p> </td> <td> <p>2/最高15</p> </td> <td> <p>90万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>2万/最高20万</p> </td> <td> <p>1.5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>3/最高15</p> </td> <td> <p>110万</p> </td> <td> <p>最高30万</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>4万/最高20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>5/最高15</p> </td> <td> <p>130万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>5万/最高20万</p> </td> <td> <p>3/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>96</p> </td> <td> <p>8/最高15</p> </td> <td> <p>180万</p> </td> <td> <p>最高30万</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>6万/最高20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>10/最高25</p> </td> <td> <p>240万</p> </td> <td> <p>最高35万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>8万/最高20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>192</p> </td> <td> <p>12/最高25</p> </td> <td> <p>300万</p> </td> <td> <p>最高40万</p> </td> <td> <p>12</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>10万/最高20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.u2i-c1m8.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>16/最高32</p> </td> <td> <p>400万</p> </td> <td> <p>最高60万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16万/最高30万</p> </td> <td> <p>8/12</p> </td> </tr> </tbody> </table>

### 通用算力型实例规格族u1

* **适用场景**：

  * 中小类型和规模的企业级应用

  * 网站和应用服务器

  * 数据分析和计算

  * 中小型数据库系统、缓存、搜索集群

* **计算**：

  * 处理器与内存配比为1:1/1:2/1:4/1:8

  * 处理器：Intel ^®^ Xeon ^®^ Platinum可扩展处理器

  **说明**

  该规格族的实例在创建时随机部署在不同的服务器平台，在实例的生命周期中也可能迁移到不同的服务器平台，u1实例采用技术手段促进不同平台间实现更好的业务兼容性，但不同平台间可能存在明显业务性能差异。如果您对业务性能一致性有强烈诉求，建议您选用g9i\&c9i\&r9i实例。
* **存储**：

  * I/O优化实例

  * 支持的云盘类型：ESSD Entry云盘、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)和[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

u1包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.u1-c1m1.large</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>2</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.large</p> </td> <td> <p>2</p> </td> <td> <p>4</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>2</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>2</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.large</p> </td> <td> <p>2</p> </td> <td> <p>16</p> </td> <td> <p>1</p> </td> <td> <p>30万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>2</p> </td> <td> <p>6</p> </td> <td> <p>2</p> </td> <td> <p>1万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>16</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>2.5</p> </td> <td> <p>80万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>2.5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>12</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>24</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>48</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>96</p> </td> <td> <p>4</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>6</p> </td> <td> <p>10</p> </td> <td> <p>2</p> </td> <td> <p>3万</p> </td> <td> <p>2.5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>16</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>32</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>5</p> </td> <td> <p>100万</p> </td> <td> <p>最高30万</p> </td> <td> <p>4</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m1.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>32</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m2.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>64</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m4.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.u1-c1m8.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>20</p> </td> <td> <p>2</p> </td> <td> <p>6万</p> </td> <td> <p>5</p> </td> </tr> </tbody> </table>  
**说明**

* 在u1实例上部署DPDK应用可能发生异常，需使用VFIO驱动替代UIO驱动来解决该问题。更多详情，请参见[使用VFIO驱动替代UIO驱动](https://help.aliyun.com/document_detail/310880.html#task-2112980)。

* 有关Universal实例的常见问题，请参见[U1实例FAQ](https://help.aliyun.com/document_detail/2983145.html#03ef52fc1666j)。

### 大数据存储密集型实例规格族d3s

* **规格族介绍**：实例配备12 TB大容量、高吞吐SATA HDD本地盘，辅以最大64 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、HBase等大数据计算和存储业务场景。

  * Spark内存计算、MLlib等机器学习场景。

  * ElasticSearch、Kafka等搜索和日志数据处理场景。

* 支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。

  如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](https://help.aliyun.com/document_detail/107693.html#concept-x5k-24p-tgb)。  
  **重要**

  确认发起坏盘修复流程后，坏盘中的数据不可恢复。
* **计算**：

  * 处理器：2.7 GHz主频的 ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘和ESSD AutoPL云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d3s包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d3s.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>4 \* 11918 GB</p><p>(4 \* 11100 GiB)</p></td> <td><p>10/最高15</p></td> <td><p>200</p></td> <td><p>3/最高5</p></td> </tr> <tr> <td><p>ecs.d3s.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>8 \* 11918 GB</p><p>(8 \* 11100 GiB)</p></td> <td><p>25/无</p></td> <td><p>300</p></td> <td><p>5/无</p></td> </tr> <tr> <td><p>ecs.d3s.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>16 \* 11918 GB</p><p>(16 \* 11100 GiB)</p></td> <td><p>40/无</p></td> <td><p>600</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.d3s.12xlarge</p></td> <td><p>48</p></td> <td><p>192</p></td> <td><p>24 \* 11918 GB</p><p>(24 \* 11100 GiB)</p></td> <td><p>60/无</p></td> <td><p>900</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.d3s.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>32 \* 11918 GB</p><p>(32 \* 11100 GiB)</p></td> <td><p>80/无</p></td> <td><p>1200</p></td> <td><p>16/无</p></td> </tr> </tbody> </table>

### 大数据计算密集型实例规格族d3c

d3c的特点如下：

* **规格族介绍**：实例配备大容量、高吞吐本地盘，辅以最大40 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、HBase等大数据计算和存储业务场景。

  * EMR JindoFS配合OSS实现大数据冷热数据分层和存储计算分离的场景。

  * Spark内存计算、MLlib等机器学习场景。

  * ElasticSearch、Kafka等搜索和日志数据处理场景。

* 支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。

  如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](https://help.aliyun.com/document_detail/107693.html#concept-x5k-24p-tgb)。  
  **重要**

  确认发起坏盘修复流程后，坏盘中的数据不可恢复。
* **计算**：

  * 处理器：采用第三代Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），主频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘和ESSD AutoPL云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d3c包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>云盘IOPS基础/突发（万）</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d3c.3xlarge</p></td> <td><p>14</p></td> <td><p>56.0</p></td> <td><p>1 \* 13743 GB</p><p>(1 \* 12800 GiB)</p></td> <td><p>8/最高10</p></td> <td><p>160</p></td> <td><p>4/无</p></td> <td><p>3/无</p></td> </tr> <tr> <td><p>ecs.d3c.7xlarge</p></td> <td><p>28</p></td> <td><p>112.0</p></td> <td><p>2 \* 13743 GB</p><p>(2 \* 12800 GiB)</p></td> <td><p>16/最高25</p></td> <td><p>250</p></td> <td><p>5/无</p></td> <td><p>4/无</p></td> </tr> <tr> <td><p>ecs.d3c.14xlarge</p></td> <td><p>56</p></td> <td><p>224.0</p></td> <td><p>4 \* 13743 GB</p><p>(4 \* 12800 GiB)</p></td> <td><p>40/无</p></td> <td><p>500</p></td> <td><p>10/无</p></td> <td><p>8/无</p></td> </tr> </tbody> </table>  
**说明**

该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。

### 大数据计算密集型实例规格族d2c

* **规格族介绍**：实例配备大容量、高吞吐SATA HDD本地盘，辅以最大35 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、Hbase等大数据计算和存储业务场景。

  * EMR JindoFS配合OOS实现大数据冷热数据分层和存储计算分离的场景。

  * Spark内存计算、MLlib等机器学习场景。

  * ElasticSearch、Kafka等搜索和日志数据处理场景。

* 支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。

  如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](https://help.aliyun.com/document_detail/107693.html#concept-x5k-24p-tgb)。  
  **重要**

  确认发起坏盘修复流程后，坏盘中的数据不可恢复。
* **计算**：

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d2c包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d2c.6xlarge</p></td> <td><p>24</p></td> <td><p>88.0</p></td> <td><p>3 \* 3972 GB</p><p>(3 \* 3700 GiB)</p></td> <td><p>12.0</p></td> <td><p>160</p></td> </tr> <tr> <td><p>ecs.d2c.12xlarge</p></td> <td><p>48</p></td> <td><p>176.0</p></td> <td><p>6 \* 3972 GB</p><p>(6 \* 3700 GiB)</p></td> <td><p>20.0</p></td> <td><p>200</p></td> </tr> <tr> <td><p>ecs.d2c.24xlarge</p></td> <td><p>96</p></td> <td><p>352.0</p></td> <td><p>12 \* 3972 GB</p><p>(12 \* 3700 GiB)</p></td> <td><p>35.0</p></td> <td><p>450</p></td> </tr> </tbody> </table>

### 大数据存储密集型实例规格族d2s

* **规格族介绍**：实例配备大容量、高吞吐SATA HDD本地盘，辅以最大35 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、Hbase等大数据计算和存储业务场景。

  * Spark内存计算、MLlib等机器学习场景。

  * ElasticSearch、Kafka等搜索和日志数据处理场景。

* 支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。

  如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](https://help.aliyun.com/document_detail/107693.html#concept-x5k-24p-tgb)。  
  **重要**

  确认发起坏盘修复流程后，坏盘中的数据不可恢复。
* **计算**：

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d2s包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d2s.5xlarge</p></td> <td><p>20</p></td> <td><p>88.0</p></td> <td><p>8 \* 7838 GB</p><p>(8 \* 7300 GiB)</p></td> <td><p>12.0</p></td> <td><p>160</p></td> </tr> <tr> <td><p>ecs.d2s.10xlarge</p></td> <td><p>40</p></td> <td><p>176.0</p></td> <td><p>15 \* 7838 GB</p><p>(15 \* 7300 GiB)</p></td> <td><p>20.0</p></td> <td><p>200</p></td> </tr> <tr> <td><p>ecs.d2s.20xlarge</p></td> <td><p>80</p></td> <td><p>352.0</p></td> <td><p>30 \* 7838 GB</p><p>(30 \* 7300 GiB)</p></td> <td><p>35.0</p></td> <td><p>450</p></td> </tr> </tbody> </table>

### 大数据网络增强型实例规格族d1ne

* **规格族介绍**：实例配备大容量、高吞吐SATA HDD本地盘，辅以最大35 Gbit/s实例间网络带宽。

* **适用场景**：

  * Hadoop MapReduce、HDFS、Hive、HBase等。

  * Spark内存计算、MLlib等。

  * ElasticSearch、日志等。

* **计算**：

  * 处理器与内存配比为1:4，为大数据场景设计。

  * 处理器：2.5 GHz主频的Intel^®^ Xeon^®^ E5-2682 v4（Broadwell）或者Intel^®^ Xeon^®^Platinum 8163（Skylake），计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

d1ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.d1ne.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>4 \* 5905 GB</p><p>(4 \* 5500 GiB)</p></td> <td><p>6.0</p></td> <td><p>100</p></td> </tr> <tr> <td><p>ecs.d1ne.4xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>8 \* 5905 GB</p><p>(8 \* 5500 GiB)</p></td> <td><p>12.0</p></td> <td><p>160</p></td> </tr> <tr> <td><p>ecs.d1ne.6xlarge</p></td> <td><p>24</p></td> <td><p>96.0</p></td> <td><p>12 \* 5905 GB</p><p>(12 \* 5500 GiB)</p></td> <td><p>16.0</p></td> <td><p>200</p></td> </tr> <tr> <td><p>ecs.d1ne-c8d3.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>12 \* 5905 GB</p><p>(12 \* 5500 GiB)</p></td> <td><p>20.0</p></td> <td><p>200</p></td> </tr> <tr> <td><p>ecs.d1ne.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>16 \* 5905 GB</p><p>(16 \* 5500 GiB)</p></td> <td><p>20.0</p></td> <td><p>250</p></td> </tr> <tr> <td><p>ecs.d1ne-c14d3.14xlarge</p></td> <td><p>56</p></td> <td><p>160.0</p></td> <td><p>12 \* 5905 GB</p><p>(12 \* 5500 GiB)</p></td> <td><p>35.0</p></td> <td><p>450</p></td> </tr> <tr> <td><p>ecs.d1ne.14xlarge</p></td> <td><p>56</p></td> <td><p>224.0</p></td> <td><p>28 \* 5905 GB</p><p>(28 \* 5500 GiB)</p></td> <td><p>35.0</p></td> <td><p>450</p></td> </tr> </tbody> </table>

### 本地SSD型实例规格族i5g

* **规格族介绍** ：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。采用阿里云全新CIPU架构，搭载英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**：磁盘类KV数据库如RocksDB、ClickHouse；E-MapReduce大数据冷热数据分层、存储计算分离、数据湖；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

i5g包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i5g.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>16/32</p> </td> <td> <p>1000万</p> </td> <td> <p>20万/30万</p> </td> <td> <p>10/12</p> </td> </tr> <tr> <td> <p>ecs.i5g.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>1 \* 3839 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>2000万</p> </td> <td> <p>30万/无</p> </td> <td> <p>16/无</p> </td> </tr> </tbody> </table>

### 本地SSD型实例规格族i5ge

* **规格族介绍** ：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。采用阿里云全新CIPU架构，搭载英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**：磁盘类KV数据库如RocksDB、ClickHouse；大数据计算（本地缓存）；在线交易等场景。

* **计算**：

  * 处理器与内存配比为1:6。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

i5ge包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i5ge.3xlarge</p> </td> <td> <p>12</p> </td> <td> <p>72</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>25/40</p> </td> <td> <p>400万</p> </td> <td> <p>8万/20万</p> </td> <td> <p>5/10</p> </td> </tr> <tr> <td> <p>ecs.i5ge.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>144</p> </td> <td> <p>1 \* 3839 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>50/70</p> </td> <td> <p>800万</p> </td> <td> <p>12万/20万</p> </td> <td> <p>7.5/10</p> </td> </tr> <tr> <td> <p>ecs.i5ge.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>288</p> </td> <td> <p>2 \* 3839 GB</p> <p>(2 \* 3576 GiB)</p> </td> <td> <p>84/无</p> </td> <td> <p>1500万</p> </td> <td> <p>24万/无</p> </td> <td> <p>12/无</p> </td> </tr> <tr> <td> <p>ecs.i5ge.24xlarge</p> </td> <td> <p>96</p> </td> <td> <p>576</p> </td> <td> <p>4 \* 3839 GB</p> <p>(4 \* 3576 GiB)</p> </td> <td> <p> 172/无</p> </td> <td> <p>3000万</p> </td> <td> <p>30万/无</p> </td> <td> <p>20/无</p> </td> </tr> </tbody> </table>

### 本地SSD型实例规格族i5e

* **规格族介绍** ：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。采用阿里云全新CIPU架构，搭载英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**：关系型数据库如MySQL；远端缓存服务、缓存层加速等场景。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频2.9 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

i5e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i5e.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 3840 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>20/40</p> </td> <td> <p>400万</p> </td> <td> <p>6万/20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.i5e.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 7680 GB</p> <p>(1 \* 7152 GiB)</p> </td> <td> <p>40/80</p> </td> <td> <p>700万</p> </td> <td> <p>10万/20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.i5e.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>2 \* 7680 GB</p> <p>(2 \* 7152 GiB)</p> </td> <td> <p>80/120</p> </td> <td> <p>1400万</p> </td> <td> <p>15万/20万</p> </td> <td> <p>10/12</p> </td> </tr> <tr> <td> <p>ecs.i5e.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>4 \* 7680 GB</p> <p>(4 \* 7152 GiB)</p> </td> <td> <p>160</p> </td> <td> <p>2500万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> </tr> <tr> <td> <p>ecs.i5e.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>8 \* 7680 GB</p> <p>(8 \* 7152 GiB)</p> </td> <td> <p>320</p> </td> <td> <p>5000万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

### 本地SSD型实例规格族i5

* **规格族介绍** ：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。采用阿里云全新CIPU架构，搭载英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎。

* **适用场景**：磁盘类KV数据库如RocksDB、ClickHouse、E-MapReduce大数据冷热数据分层、存储计算分离、数据湖；其他频繁将数据写入磁盘的I/O密集型应用，例如消息中间件、容器。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.4 GHz，全核睿频3.8 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

i5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i5.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 960 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>10/20</p> </td> <td> <p>200万</p> </td> <td> <p>4万/20万</p> </td> <td> <p>2/10</p> </td> </tr> <tr> <td> <p>ecs.i5.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>20/40</p> </td> <td> <p>400万</p> </td> <td> <p>6万/20万</p> </td> <td> <p>4/10</p> </td> </tr> <tr> <td> <p>ecs.i5.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 3839 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>40/80</p> </td> <td> <p>700万</p> </td> <td> <p>10万/20万</p> </td> <td> <p>6/10</p> </td> </tr> <tr> <td> <p>ecs.i5.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>2 \* 3839 GB</p> <p>(2 \* 3576 GiB)</p> </td> <td> <p>80/120</p> </td> <td> <p>1400万</p> </td> <td> <p>15万/20万</p> </td> <td> <p>10/12</p> </td> </tr> <tr> <td> <p>ecs.i5.12xlarge</p> </td> <td> <p>48</p> </td> <td> <p>384</p> </td> <td> <p>3 \* 3839 GB</p> <p>(3 \* 3576 GiB)</p> </td> <td> <p>120</p> </td> <td> <p>2000万</p> </td> <td> <p>24万</p> </td> <td> <p>12</p> </td> </tr> <tr> <td> <p>ecs.i5.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>4 \* 3839 GB</p> <p>(4 \* 3576 GiB)</p> </td> <td> <p>160</p> </td> <td> <p>2700万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>

### 本地SSD型实例规格族i4

* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库、NoSQL数据库（例如Cassandra、MongoDB等）、Elasticsearch等搜索场景。

* **计算**：

  * 处理器：2.7 GHz主频的Intel^®^ Xeon^®^ 可扩展处理器（Ice Lake ），全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **与操作系统的兼容性说明** ：更多信息，请参见[本地SSD型i4实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2698334.html)。

i4包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i4.large</p> </td> <td> <p>2</p> </td> <td> <p>16</p> </td> <td> <p>1 \* 479 GB</p> <p>(1 \* 447 GiB)</p> </td> <td> <p>2.5/15</p> </td> <td> <p>90万</p> </td> <td> <p>2万/最高11万</p> </td> <td> <p>1.5/6</p> </td> </tr> <tr> <td> <p>ecs.i4.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>4/15</p> </td> <td> <p>100万</p> </td> <td> <p>4万/最高11万</p> </td> <td> <p>2/6</p> </td> </tr> <tr> <td> <p>ecs.i4.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>6/15</p> </td> <td> <p>160万</p> </td> <td> <p>5万/最高11万</p> </td> <td> <p>3/6</p> </td> </tr> <tr> <td> <p>ecs.i4.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 3839 GB</p> <p>(1 \* 3576 GiB)</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>8万/最高11万</p> </td> <td> <p>5/6</p> </td> </tr> <tr> <td> <p>ecs.i4.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>2 \* 3839 GB</p> <p>(2 \* 3576 GiB)</p> </td> <td> <p>25/无</p> </td> <td> <p>600万</p> </td> <td> <p>15万/无</p> </td> <td> <p>8/无</p> </td> </tr> <tr> <td> <p>ecs.i4.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>4 \* 3839 GB</p> <p>(4 \* 3576 GiB)</p> </td> <td> <p>50/无</p> </td> <td> <p>1200万</p> </td> <td> <p>30万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.i4.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>8 \* 3839 GB</p> <p>(8 \* 3576 GiB)</p> </td> <td> <p>100/无</p> </td> <td> <p>2400万</p> </td> <td> <p>60万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

### 本地SSD型实例规格族i4g

* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘

* **适用场景**：OLTP、高性能关系型数据库；E-MapReduce大数据冷热数据分层、存储计算分离、数据湖等场景；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4，为高性能数据库等场景设计。

  * 处理器：2.7 GHz主频的Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake ），全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

i4g包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i4g.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>8/25</p> </td> <td> <p>300万</p> </td> <td> <p>10万</p> </td> <td> <p>6</p> </td> </tr> <tr> <td> <p>ecs.i4g.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>16/25</p> </td> <td> <p>600万</p> </td> <td> <p>15万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.i4g.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> </tr> <tr> <td> <p>ecs.i4g.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。

### 本地SSD型实例规格族i4r

* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘

* **适用场景**：OLTP、高性能关系型数据库、NoSQL数据库（例如Cassandra、MongoDB等）、Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:8，为高性能数据库等场景设计，是热数据分层、数据湖等应用场景的最佳性价比实例规格。

  * 处理器：2.7 GHz主频的Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake ），全核睿频3.5 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

i4r包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i4r.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>8/25</p> </td> <td> <p>300万</p> </td> <td> <p>10万</p> </td> <td> <p>6</p> </td> </tr> <tr> <td> <p>ecs.i4r.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>16/25</p> </td> <td> <p>600万</p> </td> <td> <p>15万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.i4r.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>30万</p> </td> <td> <p>16</p> </td> </tr> <tr> <td> <p>ecs.i4r.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>60万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

### 性能增强型本地盘实例规格族i4p

* **规格族介绍** ：基于Intel ^®^ 第二代傲腾持久内存（BPS），提供性能极高的本地盘，初始化本地盘的具体操作，请参见[将持久内存初始化为本地盘](https://help.aliyun.com/document_detail/188251.html#section-t66-l5n-e1g)。

* **适用场景**：

  * 基因测序类应用，详情请参见[案例说明](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20220706/misz/客户案例-寻因生物.pdf)。

  * 磁盘类KV型数据库，例如RocksDB、ClickHouse。

  * OLTP、高性能关系型数据库进行WAL优化等。

  * NoSQL数据库，例如Cassandra、MongoDB、HBase。

  * Elasticsearch等搜索场景。

  * 其他频繁将数据写入磁盘的I/O密集型应用，例如消息中间件、容器。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用第三代Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake ），基频2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i4p包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>持久内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i4p.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 126</p> </td> <td> <p>5/10</p> </td> <td> <p>160万</p> </td> <td> <p>5万/11万</p> </td> <td> <p>3/6</p> </td> </tr> <tr> <td> <p>ecs.i4p.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>2 \* 126</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>8万/11万</p> </td> <td> <p>5/6</p> </td> </tr> <tr> <td> <p>ecs.i4p.6xlarge</p> </td> <td> <p>24</p> </td> <td> <p>96</p> </td> <td> <p>3 \* 126</p> </td> <td> <p>12/25</p> </td> <td> <p>450万</p> </td> <td> <p>11万/无</p> </td> <td> <p>6/无</p> </td> </tr> <tr> <td> <p>ecs.i4p.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>4 \* 126</p> </td> <td> <p>16/25</p> </td> <td> <p>600万</p> </td> <td> <p>15万/无</p> </td> <td> <p>8/无</p> </td> </tr> <tr> <td> <p>ecs.i4p.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>1 \* 1008</p> </td> <td> <p>32/无</p> </td> <td> <p>1200万</p> </td> <td> <p>30万/无</p> </td> <td> <p>16/无</p> </td> </tr> <tr> <td> <p>ecs.i4p.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>2 \* 1008</p> </td> <td> <p>64/无</p> </td> <td> <p>2400万</p> </td> <td> <p>60万/无</p> </td> <td> <p>32/无</p> </td> </tr> </tbody> </table>

### 本地SSD型实例规格族i3g

* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake ），睿频3.2 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i3g包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i3g.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 479 GB</p> <p>(1 \* 447 GiB)</p> </td> <td> <p>3/10</p> </td> <td> <p>175万</p> </td> <td> <p>5.25万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.i3g.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>5/10</p> </td> <td> <p>350万</p> </td> <td> <p>8.4万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.i3g.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 959 GB</p> <p>(2 \* 894 GiB)</p> </td> <td> <p>12/无</p> </td> <td> <p>700万</p> </td> <td> <p>15.75万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.i3g.13xlarge</p> </td> <td> <p>52</p> </td> <td> <p>192</p> </td> <td> <p>3 \* 959 GB</p> <p>(3 \* 894 GiB)</p> </td> <td> <p>16/无</p> </td> <td> <p>1200万</p> </td> <td> <p>25.2万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.i3g.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>384</p> </td> <td> <p>6 \* 959 GB</p> <p>(6 \* 894 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>2400万</p> </td> <td> <p>50万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>  
**说明**

该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。

### 本地SSD型实例规格族i3

* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘，并支持在线隔离坏盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake ），睿频3.2 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i3包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s） </b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i3.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>1.5/10</p> </td> <td> <p>100万</p> </td> <td> <p>4万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.i3.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>2.5/10</p> </td> <td> <p>160万</p> </td> <td> <p>5万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.i3.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>5/10</p> </td> <td> <p>300万</p> </td> <td> <p>8万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.i3.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>10/无</p> </td> <td> <p>600万</p> </td> <td> <p>15万</p> </td> <td> <p>5</p> </td> </tr> <tr> <td> <p>ecs.i3.13xlarge</p> </td> <td> <p>52</p> </td> <td> <p>384</p> </td> <td> <p>6 \* 1919 GB</p> <p>(6 \* 1788 GiB)</p> </td> <td> <p>16/无</p> </td> <td> <p>900万</p> </td> <td> <p>24万</p> </td> <td> <p>8</p> </td> </tr> <tr> <td> <p>ecs.i3.26xlarge</p> </td> <td> <p>104</p> </td> <td> <p>768</p> </td> <td> <p>12 \* 1919 GB</p> <p>(12 \* 1788 GiB)</p> </td> <td> <p>32/无</p> </td> <td> <p>2400万</p> </td> <td> <p>48万</p> </td> <td> <p>16</p> </td> </tr> </tbody> </table>  
**说明**

该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。

### 本地SSD型实例规格族i2

* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:8，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i2包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p> <b>云盘带宽（Gbit/s） </b> </p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i2.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>1</p> </td> <td> <p>50万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>2</p> </td> <td> <p>100万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>3</p> </td> <td> <p>150万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>6</p> </td> <td> <p>200万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>8 \* 1919 GB</p> <p>(8 \* 1788 GiB)</p> </td> <td> <p>10</p> </td> <td> <p>400万</p> </td> <td> <p>最高16</p> </td> </tr> </tbody> </table>

### 本地SSD型实例规格族i2g

* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 仅支持IPv4。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

i2g包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i2g.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>（1 \* 894 GiB）</p> </td> <td> <p>2</p> </td> <td> <p>100万</p> </td> </tr> <tr> <td> <p>ecs.i2g.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>3</p> </td> <td> <p>150万</p> </td> </tr> <tr> <td> <p>ecs.i2g.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>6</p> </td> <td> <p>200万</p> </td> </tr> <tr> <td> <p>ecs.i2g.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>10</p> </td> <td> <p>400万</p> </td> </tr> </tbody> </table>

### 本地SSD型实例规格族i2ne

* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:8，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

  * 实例网络带宽最高可达20 Gbit/s。

i2ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>云盘带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i2ne.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>1.5</p> </td> <td> <p>50万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>2.5</p> </td> <td> <p>100万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>5</p> </td> <td> <p>150万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>512</p> </td> <td> <p>8 \* 1919 GB</p> <p>(8 \* 1788 GiB)</p> </td> <td> <p>20</p> </td> <td> <p>400万</p> </td> <td> <p>最高16</p> </td> </tr> <tr> <td> <p>ecs.i2ne.20xlarge</p> </td> <td> <p>80</p> </td> <td> <p>704</p> </td> <td> <p>10 \* 1919 GB</p> <p>(10 \* 1788 GiB)</p> </td> <td> <p>25</p> </td> <td> <p>450万</p> </td> <td> <p>最高16</p> </td> </tr> </tbody> </table>

### 本地SSD型实例规格族i2gne

* **规格族介绍**：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘

* **适用场景**：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。

* **计算**：

  * 处理器与内存配比为1:4，为高性能数据库等场景设计。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

  * 实例网络带宽最高可达20 Gbit/s。

i2gne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>本地存储</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.i2gne.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>1 \* 959 GB</p> <p>(1 \* 894 GiB)</p> </td> <td> <p>2.5</p> </td> <td> <p>100万</p> </td> </tr> <tr> <td> <p>ecs.i2gne.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>1 \* 1919 GB</p> <p>(1 \* 1788 GiB)</p> </td> <td> <p>5</p> </td> <td> <p>150万</p> </td> </tr> <tr> <td> <p>ecs.i2gne.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>2 \* 1919 GB</p> <p>(2 \* 1788 GiB)</p> </td> <td> <p>10</p> </td> <td> <p>200万</p> </td> </tr> <tr> <td> <p>ecs.i2gne.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>4 \* 1919 GB</p> <p>(4 \* 1788 GiB)</p> </td> <td> <p>20</p> </td> <td> <p>400万</p> </td> </tr> </tbody> </table>

### 高主频计算实例规格族hfc9i

* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，数据分析、批量计算、视频编码，大型多人在线游戏（MMO）前端，高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.4 GHz，全核睿频3.8 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfc9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc9i.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2.5/15</p></td> <td><p>100万</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高20万</p></td> <td><p>2/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4/15</p></td> <td><p>120万</p></td> <td><p>50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>8/15</p></td> <td><p>160万</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>10/15</p></td> <td><p>240万</p></td> <td><p>50万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>16/25</p></td> <td><p>300万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>18/25</p></td> <td><p>450万</p></td> <td><p>50万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfc9i.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>20/32</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/最高25万</p></td> <td><p>12/15</p></td> </tr> <tr> <td><p>ecs.hfc9i.12xlarge</p></td> <td><p>48</p></td> <td><p>96</p></td> <td><p>25/32</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>25万/无</p></td> <td><p>15/无</p></td> </tr> <tr> <td><p>ecs.hfc9i.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>36/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>36万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.hfc9i.24xlarge</p></td> <td><p>96</p></td> <td><p>192</p></td> <td><p>48/无</p></td> <td><p>1600万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>40万/无</p></td> <td><p>24/无</p></td> </tr> <tr> <td><p>ecs.hfc9i.36xlarge</p></td> <td><p>144</p></td> <td><p>384</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 高主频计算型实例规格族hfc8i

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能前端服务器集群。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用第四代Intel^®^ Xeon^®^ 可扩展处理器（Sapphire Rapids），基频3.3 GHz，全核睿频3.9 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfc8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc8i.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2.5/15</p></td> <td><p>120万</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>3万/最高20万</p></td> <td><p>3/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4/15</p></td> <td><p>140万</p></td> <td><p>30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>8/15</p></td> <td><p>180万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>10/15</p></td> <td><p>280万</p></td> <td><p>30万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>9万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>16/25</p></td> <td><p>360万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>10/12</p></td> </tr> <tr> <td><p>ecs.hfc8i.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>18/25</p></td> <td><p>550万</p></td> <td><p>80万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.hfc8i.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>32/无</p></td> <td><p>750万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>25万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.hfc8i.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>64/无</p></td> <td><p>1500万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>45万/无</p></td> <td><p>32/无</p></td> </tr> <tr> <td><p>ecs.hfc8i.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>100/无</p></td> <td><p>3000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>90万/无</p></td> <td><p>64/无</p></td> </tr> </tbody> </table>

### 高主频计算型实例规格族hfc7

* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能前端服务器集群。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2

  * 处理器：采用Intel^®^ Xeon^®^ Cooper Lake处理器，全核睿频3.8 GHz，主频不低于3.3 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfc7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc7.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1.2/10</p></td> <td><p>90万</p></td> <td><p>25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfc7.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>2/10</p></td> <td><p>100万</p></td> <td><p>25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfc7.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>3/10</p></td> <td><p>160万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfc7.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>4.5/10</p></td> <td><p>200万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfc7.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>6/10</p></td> <td><p>250万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfc7.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>8/10</p></td> <td><p>300万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>9万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfc7.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10/无</p></td> <td><p>400万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10.5万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfc7.12xlarge</p></td> <td><p>48</p></td> <td><p>96</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfc7.24xlarge</p></td> <td><p>96</p></td> <td><p>192</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 高主频计算型实例规格族hfc6

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Platinum 8269CY（Cascade Lake），睿频3.5 GHz，计算性能稳定。

    **说明**

    本实例规格族处理器提供3.1 GHz主频。由于Intel ISS特性原因，您查看到的主频可能显示为更低的数字。阿里云正在紧急修复该显示问题。该显示问题不影响您购买规格的主频频率。  
    您可以分别运行以下命令，使用turbostat工具来观察CPU运行的主频：

    ```
    HELPCODEESCAPE-shell
    yum install kernel-tools
    ```

    ```
    HELPCODEESCAPE-shell
    turbostat
    ```

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfc6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc6.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1/3</p></td> <td><p>30万</p></td> <td><p>3.5万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfc6.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1.5/5</p></td> <td><p>50万</p></td> <td><p>7万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfc6.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2.5/8</p></td> <td><p>80万</p></td> <td><p>15万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfc6.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>4/10</p></td> <td><p>90万</p></td> <td><p>22万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfc6.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>5/10</p></td> <td><p>100万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfc6.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>7.5/10</p></td> <td><p>150万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfc6.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10/无</p></td> <td><p>200万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfc6.10xlarge</p></td> <td><p>40</p></td> <td><p>96</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfc6.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>20/无</p></td> <td><p>400万</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>12万</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfc6.20xlarge</p></td> <td><p>80</p></td> <td><p>192</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 高主频通用型实例规格族hfg9i

* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，数据分析、批量计算、视频编码，大型多人在线游戏（MMO）前端，高性能科学和工程应用，中大型数据库。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.4 GHz，全核睿频3.8 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfg9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg9i.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>2.5/15</p></td> <td><p>100万</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高20万</p></td> <td><p>2/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>4/15</p></td> <td><p>120万</p></td> <td><p>50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>8/15</p></td> <td><p>160万</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>10/15</p></td> <td><p>240万</p></td> <td><p>50万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>16/25</p></td> <td><p>300万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>18/25</p></td> <td><p>450万</p></td> <td><p>50万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfg9i.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>20/32</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/最高25万</p></td> <td><p>12/15</p></td> </tr> <tr> <td><p>ecs.hfg9i.12xlarge</p></td> <td><p>48</p></td> <td><p>192</p></td> <td><p>25/32</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>25万/无</p></td> <td><p>15/无</p></td> </tr> <tr> <td><p>ecs.hfg9i.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>36/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>36万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.hfg9i.24xlarge</p></td> <td><p>96</p></td> <td><p>384</p></td> <td><p>48/无</p></td> <td><p>1600万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>40万/无</p></td> <td><p>24/无</p></td> </tr> <tr> <td><p>ecs.hfg9i.36xlarge</p></td> <td><p>144</p></td> <td><p>768</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 高主频通用型实例规格族hfg8i

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能前端服务器集群。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

  * 中型数据库系统。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用第四代Intel^®^ Xeon^®^ 可扩展处理器（Sapphire Rapids），基频3.3 GHz，全核睿频3.9 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfg8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>可挂载的云盘数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg8i.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>2.5/15</p></td> <td><p>120万</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>16</p></td> <td><p>3万/最高20万</p></td> <td><p>3/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>4/15</p></td> <td><p>140万</p></td> <td><p>30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>5万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>8/15</p></td> <td><p>180万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>6万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>10/15</p></td> <td><p>280万</p></td> <td><p>30万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>9万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>16/25</p></td> <td><p>360万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>12万/最高20万</p></td> <td><p>10/12</p></td> </tr> <tr> <td><p>ecs.hfg8i.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>18/25</p></td> <td><p>550万</p></td> <td><p>80万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.hfg8i.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>750万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>25万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.hfg8i.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>64/无</p></td> <td><p>1500万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>45万/无</p></td> <td><p>32/无</p></td> </tr> <tr> <td><p>ecs.hfg8i.32xlarge</p></td> <td><p>128</p></td> <td><p>512</p></td> <td><p>100/无</p></td> <td><p>3000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>64</p></td> <td><p>90万/无</p></td> <td><p>64/无</p></td> </tr> </tbody> </table>

### 高主频通用型实例规格族hfg7

* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 高性能科学计算。

  * 视频编码应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Cooper Lake处理器，全核睿频3.8 GHz，主频不低于3.3 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfg7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg7.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1.2/10</p></td> <td><p>90万</p></td> <td><p>25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfg7.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>2/10</p></td> <td><p>100万</p></td> <td><p>25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfg7.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>3/10</p></td> <td><p>160万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfg7.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>4.5/10</p></td> <td><p>200万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfg7.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>6/10</p></td> <td><p>250万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfg7.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>8/10</p></td> <td><p>300万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>9万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfg7.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>10/无</p></td> <td><p>400万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10.5万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfg7.12xlarge</p></td> <td><p>48</p></td> <td><p>192</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfg7.24xlarge</p></td> <td><p>96</p></td> <td><p>384</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 高主频通用型实例规格族hfg6

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Platinum 8269CY（Cascade Lake），睿频3.5 GHz，计算性能稳定。

    **说明**

    本实例规格族处理器提供3.1 GHz主频。由于Intel ISS特性原因，您查看到的主频可能显示为更低的数字。阿里云正在紧急修复该显示问题。该显示问题不影响您购买规格的主频频率。  
    您可以分别运行以下命令，使用turbostat工具来观察CPU运行的主频：

    ```
    HELPCODEESCAPE-shell
    yum install kernel-tools
    ```

    ```
    HELPCODEESCAPE-shell
    turbostat
    ```

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfg6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg6.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1/3</p></td> <td><p>30万</p></td> <td><p>3.5万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfg6.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>1.5/5</p></td> <td><p>50万</p></td> <td><p>7万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfg6.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>2.5/8</p></td> <td><p>80万</p></td> <td><p>15万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfg6.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>4/10</p></td> <td><p>90万</p></td> <td><p>22万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfg6.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>5/10</p></td> <td><p>100万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfg6.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>7.5/10</p></td> <td><p>150万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfg6.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>10/无</p></td> <td><p>200万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfg6.10xlarge</p></td> <td><p>40</p></td> <td><p>192</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfg6.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>20/无</p></td> <td><p>400万</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>12万</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfg6.20xlarge</p></td> <td><p>80</p></td> <td><p>384</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 高主频内存型实例规格族hfr9i

* **规格族介绍** ：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔^®^ 至强^®^ 6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：高网络包收发场景，数据分析与挖掘，分布式内存缓存，高性能数据库、内存数据库，高性能科学和工程应用，Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.4 GHz，全核睿频3.8 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfr9i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfr9i.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2.5/15</p></td> <td><p>100万</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高20万</p></td> <td><p>2/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>4/15</p></td> <td><p>120万</p></td> <td><p>50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高20万</p></td> <td><p>2.5/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>8/15</p></td> <td><p>160万</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>10/15</p></td> <td><p>240万</p></td> <td><p>50万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>5/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>16/25</p></td> <td><p>300万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>18/25</p></td> <td><p>450万</p></td> <td><p>50万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>12万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfr9i.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>20/32</p></td> <td><p>600万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/最高25万</p></td> <td><p>12/15</p></td> </tr> <tr> <td><p>ecs.hfr9i.12xlarge</p></td> <td><p>48</p></td> <td><p>384</p></td> <td><p>25/32</p></td> <td><p>900万</p></td> <td><p>100万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>25万/无</p></td> <td><p>15/无</p></td> </tr> <tr> <td><p>ecs.hfr9i.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>36/无</p></td> <td><p>1200万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>36万/无</p></td> <td><p>20/无</p></td> </tr> <tr> <td><p>ecs.hfr9i.24xlarge</p></td> <td><p>96</p></td> <td><p>768</p></td> <td><p>48/无</p></td> <td><p>1600万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>40万/无</p></td> <td><p>24/无</p></td> </tr> <tr> <td><p>ecs.hfr9i.36xlarge</p></td> <td><p>144</p></td> <td><p>1536</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 高主频内存型实例规格族hfr8i

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能科学和工程应用。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用第四代Intel^®^ Xeon^®^ 可扩展处理器（Sapphire Rapids），基频3.3 GHz，全核睿频3.9 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 与操作系统的兼容性说明，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强） ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

hfr8i包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>可挂载的云盘数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfr8i.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2.5/15</p></td> <td><p>120万</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>16</p></td> <td><p>3万/最高20万</p></td> <td><p>3/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>4/15</p></td> <td><p>140万</p></td> <td><p>30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>5万/最高20万</p></td> <td><p>4/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>8/15</p></td> <td><p>180万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>6万/最高20万</p></td> <td><p>6/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>10/15</p></td> <td><p>280万</p></td> <td><p>30万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>9万/最高20万</p></td> <td><p>8/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>16/25</p></td> <td><p>360万</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>12万/最高20万</p></td> <td><p>10/12</p></td> </tr> <tr> <td><p>ecs.hfr8i.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>18/25</p></td> <td><p>550万</p></td> <td><p>80万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.hfr8i.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>32/无</p></td> <td><p>750万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>25万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.hfr8i.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>64/无</p></td> <td><p>1500万</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>45万/无</p></td> <td><p>32/无</p></td> </tr> <tr> <td><p>ecs.hfr8i.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>100/无</p></td> <td><p>3000万</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>64</p></td> <td><p>90万/无</p></td> <td><p>64/无</p></td> </tr> </tbody> </table>

### 高主频内存型实例规格族hfr7

* **规格族介绍**：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等

  * 高性能数据库、内存数据库

  * 数据分析与挖掘、分布式内存缓存

  * Hadoop、Spark集群以及其他企业大内存需求应用

* **计算**：

  * 处理器与内存配比为1:8

  * 处理器：采用Intel^®^ Xeon^®^ Cooper Lake处理器，全核睿频3.8 GHz，主频不低于3.3 GHz，计算性能稳定

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）

hfr7包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfr7.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1.2/10</p></td> <td><p>90万</p></td> <td><p>25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfr7.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>2/10</p></td> <td><p>100万</p></td> <td><p>25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfr7.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>3/10</p></td> <td><p>160万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfr7.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>4.5/10</p></td> <td><p>200万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfr7.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>6/10</p></td> <td><p>250万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfr7.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>8/10</p></td> <td><p>300万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>9万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfr7.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>10/无</p></td> <td><p>400万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10.5万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfr7.12xlarge</p></td> <td><p>48</p></td> <td><p>384</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfr7.24xlarge</p></td> <td><p>96</p></td> <td><p>768</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 高主频内存型实例规格族hfr6

* **规格族介绍**：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 高性能数据库、内存数据库。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Platinum 8269CY（Cascade Lake），睿频3.5 GHz，计算性能稳定。

    **说明**

    本实例规格族处理器提供3.1 GHz主频。由于Intel ISS特性原因，您查看到的主频可能显示为更低的数字。阿里云正在紧急修复该显示问题。该显示问题不影响您购买规格的主频频率。  
    您可以分别运行以下命令，使用turbostat工具来观察CPU运行的主频：

    ```
    HELPCODEESCAPE-shell
    yum install kernel-tools
    ```

    ```
    HELPCODEESCAPE-shell
    turbostat
    ```

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 超高网络收发包PPS能力。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfr6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfr6.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1/3</p></td> <td><p>30万</p></td> <td><p>3.5万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.hfr6.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>1.5/5</p></td> <td><p>50万</p></td> <td><p>7万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.hfr6.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>2.5/8</p></td> <td><p>80万</p></td> <td><p>15万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.hfr6.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>4/10</p></td> <td><p>90万</p></td> <td><p>22万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2.5</p></td> </tr> <tr> <td><p>ecs.hfr6.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>5/10</p></td> <td><p>100万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.hfr6.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>7.5/10</p></td> <td><p>150万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.hfr6.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>10/无</p></td> <td><p>200万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.hfr6.10xlarge</p></td> <td><p>40</p></td> <td><p>384</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.hfr6.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>20/无</p></td> <td><p>400万</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>12万</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfr6.20xlarge</p></td> <td><p>80</p></td> <td><p>768</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 高主频计算型实例规格族hfc5

* **适用场景**：高性能Web前端服务器；高性能科学和工程应用；MMO游戏、视频编码。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Gold 6149（Skylake）或者8269CY（Cascade Lake），计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 仅支持IPv4。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfc5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfc5.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.hfc5.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfc5.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfc5.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>2.5</p></td> <td><p>130万</p></td> <td><p>4</p></td> <td><p>6</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfc5.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>3</p></td> <td><p>160万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfc5.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>4.5</p></td> <td><p>200万</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfc5.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>6</p></td> <td><p>250万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> </tbody> </table>

### 高主频通用型实例规格族hfg5

* **适用场景**：高性能Web前端服务器；高性能科学和工程应用；MMO游戏、视频编码。

* **计算**：

  * 处理器与内存配比为1:4（56 vCPU规格除外）。

  * 处理器：3.1 GHz主频的Intel^®^ Xeon^®^ Gold 6149（Skylake）或者8269CY（Cascade Lake），计算性能稳定

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 仅支持IPv4。

  * 实例网络性能与计算规格对应（规格越高网络性能越强）。

hfg5包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hfg5.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1</p></td> <td><p>30万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.hfg5.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>1.5</p></td> <td><p>50万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfg5.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>2</p></td> <td><p>100万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfg5.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>2.5</p></td> <td><p>130万</p></td> <td><p>4</p></td> <td><p>6</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.hfg5.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>3</p></td> <td><p>160万</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfg5.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>4.5</p></td> <td><p>200万</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfg5.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>6</p></td> <td><p>250万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> <tr> <td><p>ecs.hfg5.14xlarge</p></td> <td><p>56</p></td> <td><p>160</p></td> <td><p>10</p></td> <td><p>400万</p></td> <td><p>14</p></td> <td><p>8</p></td> <td><p>20</p></td> </tr> </tbody> </table>

### 存储增强通用型实例规格族g8ise

* **规格族介绍**：采用阿里云全新CIPU架构，可提供稳定的算力输出，单位vCPU提供更高的存储IO能力。

* **适用场景**：I/O密集型业务场景（例如中大型OLTP类核心数据库），中大型NoSQL数据库，搜索、实时日志分析，大型企业级商用软件（例如SAP）。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids或者Intel^®^Xeon^®^Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

  * 支持高级矩阵扩展（Intel^®^ AMX）。

    **说明**

    关于Intel^®^ AMX的更多信息，请参见[Tuning Guide for AI on the 4th Generation Intel® Xeon® Scalable Processors](https://www.intel.com/content/www/us/en/developer/articles/technical/tuning-guide-for-ai-on-the-4th-generation.html)。
* 存储：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 最多支持挂载48块数据盘。

    创建实例时最多挂载16块数据盘，如果实例需要更多数据盘，请在创建实例后继续挂载。具体操作，请参见[挂载数据盘](https://help.aliyun.com/document_detail/25446.html#concept-llz-b4c-ydb)。
  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* 网络：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* 安全

  * 支持vTPM特性，依托TPM/TCM芯片，实现从物理服务器到实例的启动链可信度量，提供超高安全能力。

  * 采用英特尔TME（Total Memory Encryption）运行内存加密。

* 与操作系统的兼容性说明：更多信息，请参见[Intel实例规格与操作系统兼容性说明](https://help.aliyun.com/document_detail/2360577.html)。

g8ise包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.g8ise.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>2.5/最高15</p></td> <td><p>100万</p></td> <td><p>最高30万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>4万/最高20万</p></td> <td><p>3/最高12</p></td> </tr> <tr> <td><p>ecs.g8ise.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>4/最高15</p></td> <td><p>120万</p></td> <td><p>最高30万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8万/最高20万</p></td> <td><p>4/最高12</p></td> </tr> <tr> <td><p>ecs.g8ise.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>6/最高15</p></td> <td><p>160万</p></td> <td><p>最高30万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>10万/最高20万</p></td> <td><p>6/最高12</p></td> </tr> <tr> <td><p>ecs.g8ise.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>10/最高15</p></td> <td><p>240万</p></td> <td><p>最高30万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>12万/最高20万</p></td> <td><p>8/最高12</p></td> </tr> <tr> <td><p>ecs.g8ise.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>12/最高25</p></td> <td><p>300万</p></td> <td><p>35万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万/最高20万</p></td> <td><p>10/最高12</p></td> </tr> <tr> <td><p>ecs.g8ise.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>15/最高25</p></td> <td><p>450万</p></td> <td><p>50万</p></td> <td><p>24</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.g8ise.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>20/最高25</p></td> <td><p>500万</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.g8ise.12xlarge</p></td> <td><p>48</p></td> <td><p>192</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>100万</p></td> <td><p>48</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>40万/无</p></td> <td><p>25/无</p></td> </tr> </tbody> </table>

### 存储增强通用型实例规格族g7se

* **规格族介绍**：依托第三代神龙架构，采用Ice Lake处理器，全面优化了存储I/O性能。

* **适用场景**：I/O密集型业务场景（例如中大型OLTP类核心数据库），中大型NoSQL数据库，搜索、实时日志分析，大型企业级商用软件（例如SAP）。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 最多支持挂载64块数据盘。创建实例时最多挂载16块数据盘，如果实例需要更多数据盘，请在创建实例后继续挂载。具体操作，请参见[挂载数据盘](https://help.aliyun.com/document_detail/25446.html#concept-llz-b4c-ydb)。

  * 单实例顺序读写性能最高可达64 Gbit/s，IOPS最高可达100万。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g7se包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>最大挂载数据盘数量</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.g7se.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1.2/最高3</p></td> <td><p>45万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>16</p></td> <td><p>3万/最高15万</p></td> <td><p>3/10</p></td> </tr> <tr> <td><p>ecs.g7se.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>2/最高5</p></td> <td><p>50万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>6万/最高15万</p></td> <td><p>4/10</p></td> </tr> <tr> <td><p>ecs.g7se.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>3/最高8</p></td> <td><p>80万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>10万/最高15万</p></td> <td><p>6/10</p></td> </tr> <tr> <td><p>ecs.g7se.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>4.5/最高10</p></td> <td><p>120万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>12万/最高15万</p></td> <td><p>8/10</p></td> </tr> <tr> <td><p>ecs.g7se.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>6/最高10</p></td> <td><p>150万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>15万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.g7se.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>8/最高10</p></td> <td><p>225万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.g7se.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>10/无</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.g7se.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>56</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 存储增强计算型实例规格族c7se

* **规格族介绍**：依托第三代神龙架构，采用Ice Lake处理器，全面优化了存储I/O性能。

* **适用场景**：I/O密集型业务场景（例如中大型OLTP类核心数据库），中大型NoSQL数据库，搜索、实时日志分析，大型企业级商用软件（例如SAP）。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 最多支持挂载64块数据盘。创建实例时最多挂载16块数据盘，如果实例需要更多数据盘，请在创建实例后继续挂载。具体操作，请参见[挂载数据盘](https://help.aliyun.com/document_detail/25446.html#concept-llz-b4c-ydb)。

  * 单实例顺序读写性能最高可达64 Gbit/s，IOPS最高可达100万。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c7se包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>最大挂载数据盘数量</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c7se.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1.2/最高3</p></td> <td><p>45万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>16</p></td> <td><p>3万/最高15万</p></td> <td><p>3/10</p></td> </tr> <tr> <td><p>ecs.c7se.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>2/最高5</p></td> <td><p>50万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>6万/最高15万</p></td> <td><p>4/10</p></td> </tr> <tr> <td><p>ecs.c7se.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>3/最高8</p></td> <td><p>80万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>10万/最高15万</p></td> <td><p>6/10</p></td> </tr> <tr> <td><p>ecs.c7se.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>4.5/最高10</p></td> <td><p>120万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>12万/最高15万</p></td> <td><p>8/10</p></td> </tr> <tr> <td><p>ecs.c7se.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>6/最高10</p></td> <td><p>150万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>15万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.c7se.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>8/最高10</p></td> <td><p>225万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.c7se.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10/无</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.c7se.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>56</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 存储增强内存型实例规格族r7se

* **规格族介绍**：依托第三代神龙架构，采用Ice Lake处理器，全面优化了存储I/O性能。

* **适用场景**：

  * I/O密集型业务场景，例如中大型OLTP类核心数据库。

  * 中大型NoSQL数据库。

  * 搜索、实时日志分析。

  * 大型企业级商用软件，例如SAP。

  * 容器高密场景。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 最多支持挂载64块数据盘。创建实例时最多挂载16块数据盘，如果实例需要更多数据盘，请在创建实例后继续挂载。具体操作，请参见[挂载数据盘](https://help.aliyun.com/document_detail/25446.html#concept-llz-b4c-ydb)。

  * 单实例顺序读写性能最高可达64 Gbit/s，IOPS最高可达100万。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

r7se包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>最大挂载数据盘数量</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r7se.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>1.2/最高3</p></td> <td><p>45万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>16</p></td> <td><p>3万/最高15万</p></td> <td><p>3/10</p></td> </tr> <tr> <td><p>ecs.r7se.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>2/最高5</p></td> <td><p>50万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>6万/最高15万</p></td> <td><p>4/10</p></td> </tr> <tr> <td><p>ecs.r7se.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>3/最高8</p></td> <td><p>80万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>10万/最高15万</p></td> <td><p>6/10</p></td> </tr> <tr> <td><p>ecs.r7se.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>4.5/最高10</p></td> <td><p>120万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>12万/最高15万</p></td> <td><p>8/10</p></td> </tr> <tr> <td><p>ecs.r7se.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>6/最高10</p></td> <td><p>150万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>15万/无</p></td> <td><p>10/无</p></td> </tr> <tr> <td><p>ecs.r7se.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>8/最高10</p></td> <td><p>225万</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>24</p></td> <td><p>20万/无</p></td> <td><p>12/无</p></td> </tr> <tr> <td><p>ecs.r7se.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>10/无</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.r7se.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>56</p></td> <td><p>50万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 网络增强通用型实例规格族g7nex

* **规格族介绍**：依托第四代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 网络密集型应用场景，例如NFV/SD-WAN、移动互联网、视频弹幕、电信业务转发等。

  * 中小型数据库系统、缓存、搜索集群。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 大幅提升单实例的网络带宽能力和网络收发包能力，单实例最高支持3000万PPS网络收发包能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g7nex包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>EBS多队列</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.g7nex.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>3/最高20</p></td> <td><p>45万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>1万/最高5万</p></td> <td><p>1.5/最高8</p></td> </tr> <tr> <td><p>ecs.g7nex.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>5/最高24</p></td> <td><p>90万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2万/最高5万</p></td> <td><p>2/最高8</p></td> </tr> <tr> <td><p>ecs.g7nex.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>10/最高32</p></td> <td><p>175万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>2</p></td> <td><p>2.5万/最高5万</p></td> <td><p>3/最高8</p></td> </tr> <tr> <td><p>ecs.g7nex.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>20/最高40</p></td> <td><p>300万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>4万/最高5万</p></td> <td><p>5/最高8</p></td> </tr> <tr> <td><p>ecs.g7nex.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>40/无</p></td> <td><p>600万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>4</p></td> <td><p>7.5万/无</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.g7nex.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>80/无</p></td> <td><p>800万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>4</p></td> <td><p>15万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.g7nex.32xlarge</p></td> <td><p>128</p></td> <td><p>512</p></td> <td><p>160/无</p></td> <td><p>1600万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>4</p></td> <td><p>30万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>  
**说明**

对于ecs.g7nex.32xlarge，实例上至少需要绑定两张弹性网卡，每张弹性网卡连接到不同的网卡索引，以实现160 Gbit/s的网络带宽；所有弹性网卡连接到相同的网卡索引，实例最高可达到100 Gbit/s的网络带宽。更多信息，请参见[AttachNetworkInterface](https://help.aliyun.com/document_detail/58515.html#doc-api-Ecs-AttachNetworkInterface)。

### 网络增强计算型实例规格族c7nex

* **规格族介绍**：依托第四代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 网络密集型应用场景，例如NFV/SD-WAN、移动互联网、视频弹幕、电信业务转发等。

  * 中小型数据库系统、缓存、搜索集群。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* 网络：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 大幅提升单实例的网络带宽能力和网络收发包能力，单实例最高支持3000万PPS网络收发包能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c7nex包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>EBS多队列</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c7nex.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>3/最高20</p></td> <td><p>45万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>1万/最高5万</p></td> <td><p>1.5/最高8</p></td> </tr> <tr> <td><p>ecs.c7nex.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>5/最高24</p></td> <td><p>90万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2万/最高5万</p></td> <td><p>2/最高8</p></td> </tr> <tr> <td><p>ecs.c7nex.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>10/最高32</p></td> <td><p>175万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>2</p></td> <td><p>2.5万/最高5万</p></td> <td><p>3/最高8</p></td> </tr> <tr> <td><p>ecs.c7nex.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>20/最高40</p></td> <td><p>300万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>4万/最高5万</p></td> <td><p>5/最高8</p></td> </tr> <tr> <td><p>ecs.c7nex.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>40/无</p></td> <td><p>600万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>4</p></td> <td><p>7.5万/无</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.c7nex.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>80/无</p></td> <td><p>800万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>4</p></td> <td><p>15万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.c7nex.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>160/无</p></td> <td><p>1600万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>4</p></td> <td><p>30万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>  
**说明**

对于ecs.c7nex.32xlarge，实例上至少需要绑定两张弹性网卡，每张弹性网卡连接到不同的网卡索引，以实现160 Gbit/s的网络带宽；所有弹性网卡连接到相同的网卡索引，实例最高可达到100 Gbit/s的网络带宽。更多信息，请参见[AttachNetworkInterface](https://help.aliyun.com/document_detail/58515.html#doc-api-Ecs-AttachNetworkInterface)。

### 网络增强通用型实例规格族g7ne

* **规格族介绍**：大幅提升单实例的网络带宽能力和网络收发包能力，单实例最高支持2400万PPS网络收发包能力。

* **适用场景**：

  * 网络密集型应用场景，例如NFV/SD-WAN、移动互联网、视频弹幕、电信业务转发等。

  * 中小型数据库系统、缓存、搜索集群。

  * 各种类型和规模的企业级应用。

  * 大数据分析和机器学习。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：采用Intel^®^ Xeon^®^ Platinum 8369HB（Cooper Lake）或者Intel^®^ Xeon^®^ Platinum 8369HC（Cooper Lake），睿频3.8 GHz，主频不低于3.3 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g7ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.g7ne.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1.5/10</p></td> <td><p>90万</p></td> <td><p>45万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>10</p></td> <td><p>1万</p></td> <td><p>0.75</p></td> </tr> <tr> <td><p>ecs.g7ne.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>3/10</p></td> <td><p>100万</p></td> <td><p>90万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.g7ne.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>6/15</p></td> <td><p>160万</p></td> <td><p>175万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>2.5万</p></td> <td><p>1.2</p></td> </tr> <tr> <td><p>ecs.g7ne.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>12/25</p></td> <td><p>300万</p></td> <td><p>350万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>4万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.g7ne.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>600万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>7.5万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.g7ne.12xlarge</p></td> <td><p>48</p></td> <td><p>192</p></td> <td><p>40/无</p></td> <td><p>1200万</p></td> <td><p>800万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.g7ne.24xlarge</p></td> <td><p>96</p></td> <td><p>384</p></td> <td><p>80/无</p></td> <td><p>2400万</p></td> <td><p>1600万</p></td> <td><p>48</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>24万</p></td> <td><p>16</p></td> </tr> </tbody> </table>

### 网络增强通用型实例规格族g5ne

* **规格族介绍**：大幅提升单实例的网络吞吐能力和网络包转发能力。

* **适用场景**：

  * DPDK类应用。

  * 网络密集型应用场景，例如NFV/SD-WAN、移动互联网、视频弹幕、电信业务转发等。

  * 中小型数据库系统、缓存、搜索集群。

  * 各种类型和规模的企业级应用。

  * 大数据分析和机器学习。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）或者8269CY（Cascade Lake），计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘、高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 实例网络性能与计算规格对应，规格越高网络性能越强。

    **说明**

建议DPDK类应用优先选择g5ne实例规格进行部署。  
g5ne包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.g5ne.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1</p></td> <td><p>40万</p></td> <td><p>45万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>10</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.g5ne.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>2</p></td> <td><p>75万</p></td> <td><p>90万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>1.5万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.g5ne.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>3.5</p></td> <td><p>150万</p></td> <td><p>175万</p></td> <td><p>8</p></td> <td><p>6</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>3万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.g5ne.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>7</p></td> <td><p>300万</p></td> <td><p>350万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>6万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.g5ne.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>15</p></td> <td><p>600万</p></td> <td><p>700万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>11万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.g5ne.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>30</p></td> <td><p>1200万</p></td> <td><p>1400万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>13万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.g5ne.18xlarge</p></td> <td><p>72</p></td> <td><p>288</p></td> <td><p>33</p></td> <td><p>1350万</p></td> <td><p>1500万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>16万</p></td> <td><p>9</p></td> </tr> </tbody> </table>

### 安全增强通用型实例规格族g9it

* **规格族介绍**：

  * 支持Intel^®^ SGX加密计算，最大支持192 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。

  * 支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。

  * 默认关闭超线程，独享物理核，降低侧信道攻击风险，内存加密算法升级至AES-256。

    **重要**

    如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
  * 依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。

  * 采用阿里云全新CIPU架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。

  * 多方计算中需要共享机密数据。

  * 区块链场景。

  * 机密机器学习。

  * 高安全可信要求场景，例如金融、政务、企业等。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4，其中加密内存在内存中的占比约为50%。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g9it包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>加密内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.g9it.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>4/15</p></td> <td><p>120万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/20万</p></td> <td><p>2.5/10</p></td> </tr> <tr> <td><p>ecs.g9it.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>6/15</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/20万</p></td> <td><p>4/10</p></td> </tr> <tr> <td><p>ecs.g9it.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>16</p></td> <td><p>12/25</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/20万</p></td> <td><p>6/10</p></td> </tr> <tr> <td><p>ecs.g9it.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>32</p></td> <td><p>20/32</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/30万</p></td> <td><p>10/12</p></td> </tr> <tr> <td><p>ecs.g9it.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>64</p></td> <td><p>28/36</p></td> <td><p>1200万</p></td> <td><p>是</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/40万</p></td> <td><p>16/24</p></td> </tr> <tr> <td><p>ecs.g9it.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>128</p></td> <td><p>36/50</p></td> <td><p>2000万</p></td> <td><p>是</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>40万/65万</p></td> <td><p>24/28</p></td> </tr> <tr> <td><p>ecs.g9it.24xlarge</p></td> <td><p>96</p></td> <td><p>384</p></td> <td><p>192</p></td> <td><p>64</p></td> <td><p>2400万</p></td> <td><p>是</p></td> <td><p>600万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/80万</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

* Intel® Xeon® Granite Rapids仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。

* Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。

* 实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](https://help.aliyun.com/document_detail/162751.html#task-2449646)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](https://help.aliyun.com/document_detail/201395.html#task-2038128)。

* 产品处于邀测阶段，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 安全增强内存型实例规格族r9it

* **规格族介绍**：

  * 支持Intel^®^ SGX加密计算，最大支持384 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。

  * 支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。

  * 默认关闭超线程，独享物理核，降低侧信道攻击风险，内存加密算法升级至AES-256。

    **重要**

    如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
  * 依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。

  * 采用阿里云全新CIPU架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。

  * 多方计算中需要共享机密数据。

  * 区块链场景。

  * 机密机器学习。

  * 高安全可信要求场景，例如金融、政务、企业等。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:8，其中加密内存在内存中的占比约为50%。

  * 处理器：采用Intel^®^ Xeon^®^ Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

r9it包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>加密内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r9it.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>4/15</p></td> <td><p>120万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/20万</p></td> <td><p>2.5/10</p></td> </tr> <tr> <td><p>ecs.r9it.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>16</p></td> <td><p>6/15</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>6万/20万</p></td> <td><p>4/10</p></td> </tr> <tr> <td><p>ecs.r9it.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>32</p></td> <td><p>12/25</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>50万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>10万/20万</p></td> <td><p>6/10</p></td> </tr> <tr> <td><p>ecs.r9it.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>64</p></td> <td><p>20/32</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>80万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>20万/30万</p></td> <td><p>10/12</p></td> </tr> <tr> <td><p>ecs.r9it.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>128</p></td> <td><p>28/36</p></td> <td><p>1200万</p></td> <td><p>是</p></td> <td><p>200万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/40万</p></td> <td><p>16/24</p></td> </tr> <tr> <td><p>ecs.r9it.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>256</p></td> <td><p>36/50</p></td> <td><p>2000万</p></td> <td><p>是</p></td> <td><p>400万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>40万/65万</p></td> <td><p>24/28</p></td> </tr> <tr> <td><p>ecs.r9it.24xlarge</p></td> <td><p>96</p></td> <td><p>768</p></td> <td><p>384</p></td> <td><p>64</p></td> <td><p>2400万</p></td> <td><p>是</p></td> <td><p>600万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>50</p></td> <td><p>50万/80万</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

* Intel® Xeon® Granite Rapids仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。

* Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。

* 实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](https://help.aliyun.com/document_detail/162751.html#task-2449646)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](https://help.aliyun.com/document_detail/201395.html#task-2038128)。

* 产品处于邀测阶段，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 安全增强通用型实例规格族g7t

* **规格族介绍**：

  * 支持Intel^®^ SGX加密计算，最大支持256 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。

  * 支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。

    **重要**

    如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
  * 依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。

  * 依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。

  * 多方计算中需要共享机密数据。

  * 区块链场景。

  * 机密机器学习。

  * 高安全可信要求场景，例如金融、政务、企业等。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:4，其中加密内存在内存中的占比约为50%。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g7t包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>加密内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.g7t.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>2/最高10</p></td> <td><p>90万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高11万</p></td> <td><p>1.5/最高6</p></td> </tr> <tr> <td><p>ecs.g7t.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>3/最高10</p></td> <td><p>100万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4万/最高11万</p></td> <td><p>2/最高6</p></td> </tr> <tr> <td><p>ecs.g7t.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>16</p></td> <td><p>5/最高10</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高11万</p></td> <td><p>3/最高6</p></td> </tr> <tr> <td><p>ecs.g7t.3xlarge</p></td> <td><p>12</p></td> <td><p>48</p></td> <td><p>24</p></td> <td><p>8/最高10</p></td> <td><p>240万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>7万/最高11万</p></td> <td><p>4/最高6</p></td> </tr> <tr> <td><p>ecs.g7t.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>32</p></td> <td><p>10/最高25</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>8万/最高11万</p></td> <td><p>5/最高6</p></td> </tr> <tr> <td><p>ecs.g7t.6xlarge</p></td> <td><p>24</p></td> <td><p>96</p></td> <td><p>48</p></td> <td><p>12/最高25</p></td> <td><p>450万</p></td> <td><p>是</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>11万/无</p></td> <td><p>6/无</p></td> </tr> <tr> <td><p>ecs.g7t.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>64</p></td> <td><p>16/最高25</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万/无</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.g7t.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>是</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.g7t.32xlarge</p></td> <td><p>128</p></td> <td><p>512</p></td> <td><p>256</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>是</p></td> <td><p>240万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>60万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>  
**说明**

* Intel Ice Lake仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。

* Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。

* 实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](https://help.aliyun.com/document_detail/162751.html#task-2449646)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](https://help.aliyun.com/document_detail/201395.html#task-2038128)。

* 如需使用ecs.g7t.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 安全增强计算型实例规格族c7t

* **规格族介绍**：

  * 支持Intel^®^ SGX加密计算，最大支持128 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。

  * 支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。

    **重要**

    如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
  * 依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。

  * 依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。

  * 多方计算中需要共享机密数据。

  * 区块链场景。

  * 机密机器学习。

  * 高安全可信要求场景，例如金融、政务、企业等。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:2，其中加密内存在内存中的占比约为50%。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c7t包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>加密内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c7t.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2</p></td> <td><p>2/最高10</p></td> <td><p>90万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高11万</p></td> <td><p>1.5/最高6</p></td> </tr> <tr> <td><p>ecs.c7t.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>3/最高10</p></td> <td><p>100万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4万/最高11万</p></td> <td><p>2/最高6</p></td> </tr> <tr> <td><p>ecs.c7t.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>5/最高10</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高11万</p></td> <td><p>3/最高6</p></td> </tr> <tr> <td><p>ecs.c7t.3xlarge</p></td> <td><p>12</p></td> <td><p>24</p></td> <td><p>12</p></td> <td><p>8/最高10</p></td> <td><p>240万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>7万/最高11万</p></td> <td><p>4/最高6</p></td> </tr> <tr> <td><p>ecs.c7t.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>16</p></td> <td><p>10/最高25</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>8万/最高11万</p></td> <td><p>5/最高6</p></td> </tr> <tr> <td><p>ecs.c7t.6xlarge</p></td> <td><p>24</p></td> <td><p>48</p></td> <td><p>24</p></td> <td><p>12/最高25</p></td> <td><p>450万</p></td> <td><p>是</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>11万/无</p></td> <td><p>6/无</p></td> </tr> <tr> <td><p>ecs.c7t.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>32</p></td> <td><p>16/最高25</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万/无</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.c7t.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>64</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>是</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.c7t.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>128</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>是</p></td> <td><p>240万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>60万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>  
**说明**

* Intel Ice Lake仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。

* Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。

* 实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](https://help.aliyun.com/document_detail/162751.html#task-2449646)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](https://help.aliyun.com/document_detail/201395.html#task-2038128)。

* 如需使用ecs.c7t.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 安全增强内存型实例规格族r7t

* **规格族介绍**：

  * 支持Intel^®^ SGX加密计算，最大支持512 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。

  * 支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。

    **重要**

    如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
  * 依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。

  * 依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。

* **适用场景**：

  * 数据库加密计算应用。

  * 涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。

  * 多方计算中共享机密数据。

  * 区块链场景。

  * 机密机器学习。

  * 高安全可信要求场景，例如金融、政务、企业等。

  * 各种类型和规模的企业级应用。

* **计算**：

  * 处理器与内存配比为1:8，其中加密内存在内存中的占比约为50%。

  * 处理器：采用第三代Intel^®^ Xeon^®^可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

r7t包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>加密内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r7t.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>2/最高10</p></td> <td><p>90万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/最高11万</p></td> <td><p>1.5/最高6</p></td> </tr> <tr> <td><p>ecs.r7t.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>16</p></td> <td><p>3/最高10</p></td> <td><p>100万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4万/最高11万</p></td> <td><p>2/最高6</p></td> </tr> <tr> <td><p>ecs.r7t.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>32</p></td> <td><p>5/最高10</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/最高11万</p></td> <td><p>3/最高6</p></td> </tr> <tr> <td><p>ecs.r7t.3xlarge</p></td> <td><p>12</p></td> <td><p>96</p></td> <td><p>48</p></td> <td><p>8/最高10</p></td> <td><p>240万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>7万/最高11万</p></td> <td><p>4/最高6</p></td> </tr> <tr> <td><p>ecs.r7t.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>64</p></td> <td><p>10/最高25</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>8万/最高11万</p></td> <td><p>5/最高6</p></td> </tr> <tr> <td><p>ecs.r7t.6xlarge</p></td> <td><p>24</p></td> <td><p>192</p></td> <td><p>96</p></td> <td><p>12/最高25</p></td> <td><p>450万</p></td> <td><p>是</p></td> <td><p>45万</p></td> <td><p>12</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>11万/无</p></td> <td><p>6/无</p></td> </tr> <tr> <td><p>ecs.r7t.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>128</p></td> <td><p>16/最高25</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>15万/无</p></td> <td><p>8/无</p></td> </tr> <tr> <td><p>ecs.r7t.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>256</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>是</p></td> <td><p>120万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.r7t.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>512</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>是</p></td> <td><p>240万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>60万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>  
**说明**

* Intel Ice Lake仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。

* Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。

* 实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](https://help.aliyun.com/document_detail/162751.html#task-2449646)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。

* 在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](https://help.aliyun.com/document_detail/201395.html#task-2038128)。

* 如需使用ecs.r7t.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 安全增强通用型实例规格族g6t

g6t的特点如下：

* **规格族介绍**：

  * 依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。

  * 支持vTPM，通过完整性监控，提供IaaS层可信能力。

  * 依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 高安全可信要求场景，例如金融、政务、企业等。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * 各种类型和规模的企业级应用。

  * 网站和应用服务器。

  * 游戏服务器。

  * 中小型数据库系统、缓存、搜索集群。

  * 数据分析和计算。

  * 计算集群、依赖内存的数据处理。

* **计算**：

  * 处理器与内存配比约为1:4。

  * 处理器：2.5 GHz主频、3.2 GHz睿频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6t包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.g6t.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>1.2/最高10</p></td> <td><p>90万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.g6t.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>2/最高10</p></td> <td><p>100万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.g6t.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>3/最高10</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.g6t.4xlarge</p></td> <td><p>16</p></td> <td><p>64</p></td> <td><p>6/最高10</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>8万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.g6t.8xlarge</p></td> <td><p>32</p></td> <td><p>128</p></td> <td><p>10/无</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>15万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.g6t.13xlarge</p></td> <td><p>52</p></td> <td><p>192</p></td> <td><p>16/无</p></td> <td><p>900万</p></td> <td><p>是</p></td> <td><p>90万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>24万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.g6t.26xlarge</p></td> <td><p>104</p></td> <td><p>384</p></td> <td><p>32/无</p></td> <td><p>2400万</p></td> <td><p>是</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>48万</p></td> <td><p>16</p></td> </tr> </tbody> </table>  
**说明**

网络能力为单项测试最高能力。例如，单项测试网络带宽能力时，不会对网络收发包能力和其他指标同时做压力测试。

### 安全增强计算型实例规格族c6t

* **规格族介绍**：

  * 依托TPM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。

  * 支持完整监控，提供IaaS层可信能力。

  * 依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 高安全可信要求场景，例如金融、政务、企业等。

  * 高网络包收发场景，例如视频弹幕、电信业务转发等。

  * Web前端服务器。

  * 大型多人在线游戏（MMO）前端。

  * 数据分析、批量计算、视频编码。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比约为1:2。

  * 处理器：2.5 GHz主频、3.2 GHz睿频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c6t包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>支持vTPM</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c6t.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1.2/最高10</p></td> <td><p>90万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c6t.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>2/最高10</p></td> <td><p>100万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>4万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.c6t.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>3/最高10</p></td> <td><p>160万</p></td> <td><p>是</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.c6t.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>6/最高10</p></td> <td><p>300万</p></td> <td><p>是</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>8万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.c6t.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>10/无</p></td> <td><p>600万</p></td> <td><p>是</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>15万</p></td> <td><p>5</p></td> </tr> <tr> <td><p>ecs.c6t.13xlarge</p></td> <td><p>52</p></td> <td><p>96</p></td> <td><p>16/无</p></td> <td><p>900万</p></td> <td><p>是</p></td> <td><p>90万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>24万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.c6t.26xlarge</p></td> <td><p>104</p></td> <td><p>192</p></td> <td><p>32/无</p></td> <td><p>2400万</p></td> <td><p>是</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>48万</p></td> <td><p>16</p></td> </tr> </tbody> </table>  
**说明**

网络能力为单项测试最高能力。例如，单项测试网络带宽能力时，不会对网络收发包能力和其他指标同时做压力测试。

### 内存增强型实例规格族re8

* **规格族介绍**：采用阿里云全新CIPU架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**： 内存数据库（SAP HANA）、高性能数据库和其他内存密集型企业应用。

* **计算**：

  * 处理器与内存配比为1:17，最大内存容量支持16TB。

  * 处理器：采用Intel ^®^Xeon ^®^Sapphire Rapids处理器，主频1.9 GHz，全核睿频2.9 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)及[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

re8包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.re8.30xlarge</p></td> <td><p>120</p></td> <td><p>2048</p></td> <td><p>32/最高48</p></td> <td><p>750万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>15万/最高30万</p></td> <td><p>12/最高25</p></td> </tr> <tr> <td><p>ecs.re8.60xlarge</p></td> <td><p>240</p></td> <td><p>4096</p></td> <td><p>64</p></td> <td><p>1500万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30万</p></td> <td><p>25</p></td> </tr> <tr> <td><p>ecs.re8.90xlarge</p></td> <td><p>360</p></td> <td><p>6144</p></td> <td><p>96</p></td> <td><p>2250万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>40万</p></td> <td><p>36</p></td> </tr> <tr> <td><p>ecs.re8.120xlarge</p></td> <td><p>480</p></td> <td><p>8192</p></td> <td><p>128</p></td> <td><p>3000万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>40</p></td> <td><p>60万</p></td> <td><p>50</p></td> </tr> <tr> <td><p>ecs.re8.180xlarge</p></td> <td><p>720</p></td> <td><p>12288</p></td> <td><p>192</p></td> <td><p>4500万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>40</p></td> <td><p>90万</p></td> <td><p>75</p></td> </tr> <tr> <td><p>ecs.re8.240xlarge</p></td> <td><p>960</p></td> <td><p>16384</p></td> <td><p>200</p></td> <td><p>5000万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>50</p></td> <td><p>120万</p></td> <td><p>100</p></td> </tr> </tbody> </table>

### 内存增强型实例规格族re7p

* **规格族介绍**：

  * 基于持久内存技术，提供性价比更高的内存介质。

    **说明**

    本规格族提供的内存混合了普通内存与持久内存。建议您在上线应用前进行充分的测试，必要的时候，需要对应用进行适当改造以获得最佳的性价比。
  * 依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

  * 提供高达1:20的超大处理器与内存配比，极大幅度降低内存型应用单GiB内存的成本。

* **适用场景**：

  * 内存型数据库，例如Redis。关于如何快速部署Redis应用，请参见[在配备持久内存的实例上部署Redis应用](https://help.aliyun.com/document_detail/188250.html#task-1986409)。

  * 学习与训练应用下的参数服务器（Parameter Server）。

  * 需要大容量Page Cache的应用，例如RocketMQ等消息中间件。

  * 数据分析与挖掘、分布式内存缓存。

  * Hadoop集群、Spark集群以及其他企业大内存需求应用。

* **计算**：

  * 处理器与内存（内存+持久内存）配比约为1:20。

  * 处理器：采用第三代Intel ^®^ Xeon ^®^ 可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 支持超线程配置。默认开启超线程配置，详情请参见[更改CPU选项](https://help.aliyun.com/document_detail/145895.html#concept-2352963)。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例存储I/O性能具备突发能力

  * 实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强）

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

re7p包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>持久内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.re7p.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>31.5</p></td> <td><p>2/10</p></td> <td><p>90万</p></td> <td><p>25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>2万/11万</p></td> <td><p>1.5/6</p></td> </tr> <tr> <td><p>ecs.re7p.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>63</p></td> <td><p>3/10</p></td> <td><p>100万</p></td> <td><p>25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>4万/11万</p></td> <td><p>2/6</p></td> </tr> <tr> <td><p>ecs.re7p.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>126</p></td> <td><p>5/10</p></td> <td><p>160万</p></td> <td><p>25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>5万/11万</p></td> <td><p>3/6</p></td> </tr> <tr> <td><p>ecs.re7p.16xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>1008</p></td> <td><p>32/无</p></td> <td><p>1200万</p></td> <td><p>100万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>30万/无</p></td> <td><p>16/无</p></td> </tr> <tr> <td><p>ecs.re7p.32xlarge</p></td> <td><p>128</p></td> <td><p>512</p></td> <td><p>2016</p></td> <td><p>64/无</p></td> <td><p>2400万</p></td> <td><p>200万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>60万/无</p></td> <td><p>32/无</p></td> </tr> </tbody> </table>

### 持久内存型实例规格族re6p

有关持久内存型实例的常见问题，请参见[实例FAQ](https://help.aliyun.com/document_detail/108473.html#concept-gqy-fyx-wgb)。  
re6p的特点如下：

* **规格族介绍**：

  * 采用Intel ^®^傲腾 ^TM^持久内存。

    **重要**

    持久内存中数据的可靠性取决于物理服务器和持久内存设备的可靠性，因此存在单点故障风险。建议您在应用层做好数据冗余，将需要长期保存的业务数据存储到云盘上，以保证应用数据的可靠性。
  * 部分实例规格支持设置不同的持久内存使用方式（作为内存或本地SSD盘使用）。

    **说明**

    具体操作，请参见[配置使用持久内存](https://help.aliyun.com/document_detail/188251.html#task-1986683)。
  * 为Redis应用提供专用实例规格ecs.re6p-redis.\<nx\>large。

    **说明**

    ecs.re6p-redis.\<nx\>large是为Redis应用提供的专用实例规格，专用实例规格默认已将持久内存配置为内存使用，不支持重新配置为本地SSD盘使用。关于如何快速部署Redis应用，请参见[在配备持久内存的实例上部署Redis应用](https://help.aliyun.com/document_detail/188250.html#task-1986409)。
* **适用场景**：

  * Redis数据库及其他NoSQL数据库（例如Cassandra、MongoDB等）。

  * 结构化数据库（例如MySQL等）。

  * 电商、游戏、媒体等I/O密集型应用。

  * Elasticsearch搜索。

  * 视频直播、即时通讯、房间式强联网网游。

  * 高性能关系型数据库、联机事务处理（OLTP）系统。

* **计算**：

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

re6p包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>持久内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.re6p.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>31.5</p></td> <td><p>1/3</p></td> <td><p>30万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.re6p.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>63</p></td> <td><p>1.5/5</p></td> <td><p>50万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.re6p.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>126</p></td> <td><p>2.5/无</p></td> <td><p>80万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.re6p.13xlarge</p></td> <td><p>52</p></td> <td><p>192</p></td> <td><p>756</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>90万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.re6p.26xlarge</p></td> <td><p>104</p></td> <td><p>384</p></td> <td><p>1512</p></td> <td><p>25/无</p></td> <td><p>600万</p></td> <td><p>180万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16.4</p></td> </tr> <tr> <td><p>ecs.re6p-redis.large</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>31.5</p></td> <td><p>1/3</p></td> <td><p>30万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.re6p-redis.xlarge</p></td> <td><p>4</p></td> <td><p>16</p></td> <td><p>63</p></td> <td><p>1.5/5</p></td> <td><p>50万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.re6p-redis.2xlarge</p></td> <td><p>8</p></td> <td><p>32</p></td> <td><p>126</p></td> <td><p>2.5/无</p></td> <td><p>80万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.re6p-redis.13xlarge</p></td> <td><p>52</p></td> <td><p>192</p></td> <td><p>756</p></td> <td><p>12.5/无</p></td> <td><p>300万</p></td> <td><p>90万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> </tbody> </table>

### 内存增强型实例规格族re6

re6的特点如下：

* **规格族介绍**：针对高性能数据库、内存数据库和其他内存密集型企业应用程序进行了优化。

* **适用场景**：

  * 高性能数据库、内存型数据库（例如SAP HANA）

  * 内存密集型应用

  * 大数据处理引擎（例如Apache Spark或Presto）

* **计算**：

  * 处理器与内存配比为1:16（部分规格约为1:15），高内存资源占比，最大支持3 TiB内存

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

re6包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.re6.4xlarge</p></td> <td><p>16</p></td> <td><p>256</p></td> <td><p>5</p></td> <td><p>180万</p></td> <td><p>8</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>2.5万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.re6.8xlarge</p></td> <td><p>32</p></td> <td><p>512</p></td> <td><p>10</p></td> <td><p>180万</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.re6.13xlarge</p></td> <td><p>52</p></td> <td><p>768</p></td> <td><p>10</p></td> <td><p>180万</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.re6.16xlarge</p></td> <td><p>64</p></td> <td><p>1024</p></td> <td><p>16</p></td> <td><p>300万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.re6.26xlarge</p></td> <td><p>104</p></td> <td><p>1536</p></td> <td><p>16</p></td> <td><p>300万</p></td> <td><p>32</p></td> <td><p>7</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>10万</p></td> <td><p>8</p></td> </tr> <tr> <td><p>ecs.re6.32xlarge</p></td> <td><p>128</p></td> <td><p>2048</p></td> <td><p>32</p></td> <td><p>600万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.re6.52xlarge</p></td> <td><p>208</p></td> <td><p>3072</p></td> <td><p>32</p></td> <td><p>600万</p></td> <td><p>32</p></td> <td><p>15</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>20万</p></td> <td><p>16</p></td> </tr> </tbody> </table>  
**说明**

如需使用ecs.re6.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 内存增强型实例规格族re4

* **规格族介绍**：

  * 针对高性能数据库、内存数据库和其他内存密集型企业应用程序进行了优化。

  * ecs.re4.20xlarge和ecs.re4.40xlarge规格通过SAP HANA认证。

* **适用场景**：

  * 高性能数据库、内存型数据库（例如SAP HANA）。

  * 内存密集型应用。

  * 大数据处理引擎（例如Apache Spark或Presto）。

* **计算**：

  * 处理器与内存配比为1:12，高内存资源占比，最大支持1920 GiB内存。

  * 处理器：2.2 GHz主频的Intel ^®^ Xeon ^®^ E7 8880 v4（Broadwell），最大睿频2.4 GHz，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：SSD云盘、高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

re4包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.re4.10xlarge</p></td> <td><p>40</p></td> <td><p>480</p></td> <td><p>8</p></td> <td><p>100万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.re4.20xlarge</p></td> <td><p>80</p></td> <td><p>960</p></td> <td><p>15</p></td> <td><p>200万</p></td> <td><p>16</p></td> <td><p>2</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.re4.40xlarge</p></td> <td><p>160</p></td> <td><p>1920</p></td> <td><p>30</p></td> <td><p>400万</p></td> <td><p>16</p></td> <td><p>2</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> </tbody> </table>

### 内存增强型实例规格族re4e

如需使用re4e，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。  
* **规格族介绍**：针对高性能数据库、内存数据库和其他内存密集型企业应用程序进行了优化

* **计算**：

  * 处理器与内存配比为1:24，高内存资源占比，最大支持3840 GiB内存

  * 处理器：2.2 GHz主频的Intel ^®^ Xeon ^®^ E7 8880 v4（Broadwell），最大睿频2.4 GHz，计算性能稳定

* **适用场景**：

  * 高性能数据库、内存型数据库（例如SAP HANA）

  * 内存密集型应用

  * 大数据处理引擎（例如Apache Spark或Presto）

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：SSD云盘、高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

re4e包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡私有IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.re4e.40xlarge</p></td> <td><p>160</p></td> <td><p>3840</p></td> <td><p>30</p></td> <td><p>450万</p></td> <td><p>16</p></td> <td><p>15</p></td> <td><p>10</p></td> <td><p>1</p></td> </tr> </tbody> </table>

## 入门级x86计算规格族群
### 经济型实例规格族e

* **适用场景**：

  * 面向自主任务型智能体的轻载场景，如Claw类项目的云端部署节点，或智能体网关、编排器等。

  * 中小型网站建设、开发测试。

  * 经典轻量级应用。

* **计算**：

  * 支持4:1、2:1、1:1、1:2、1:4多种处理器内存配比

  * 处理器：Intel^®^Xeon^®^Platinum可扩展处理器

    **说明**

    e实例采用非绑定CPU调度模式，每个vCPU会被随机分配到任何空闲CPU超线程上。与企业级实例相比，e实例侧重于资源的共享，但是费用更低。
* **存储**：

  * I/O优化实例

  * 仅支持ESSD Entry云盘（推荐）、ESSD云盘、ESSD AutoPL云盘

    **说明**

    受经济型实例规格限制，PL1、PL2和PL3性能级别的ESSD云盘无法发挥极致性能，建议您选择ESSD Entry云盘或PL0性能级别的ESSD云盘。
* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 仅支持专有网络VPC

  * 实例网络性能与计算规格对应（规格越大网络性能越强）

e包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.e-c4m1.large</p></td> <td><p>2</p></td> <td><p>0.5</p></td> <td><p>0.2/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.8万/无</p></td> <td><p>0.4/无</p></td> </tr> <tr> <td><p>ecs.e-c2m1.large</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.2/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.8万/无</p></td> <td><p>0.4/无</p></td> </tr> <tr> <td><p>ecs.e-c1m1.large</p></td> <td><p>2</p></td> <td><p>2.0</p></td> <td><p>0.2/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.8万/无</p></td> <td><p>0.4/无</p></td> </tr> <tr> <td><p>ecs.e-c1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>0.2/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>0.8万/无</p></td> <td><p>0.4/无</p></td> </tr> <tr> <td><p>ecs.e-c1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>0.4/最高2</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> <tr> <td><p>ecs.e-c1m2.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>0.4/最高3</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> <tr> <td><p>ecs.e-c1m4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>0.8/最高4</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> <tr> <td><p>ecs.e-c1m2.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>0.8/最高6</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> <tr> <td><p>ecs.e-c1m4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>1.2/最高6</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.6万/无</p></td> <td><p>0.8/无</p></td> </tr> </tbody> </table>  
**说明**

* 实例规格ecs.e-c4m1.large、ecs.e-c2m1.large、ecs.e-c1m1.large、ecs.e-c1m2.large、ecs.e-c1m4.large有以下限制：

  * 不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。

  * 绑定和解绑辅助弹性网卡时，实例必须处于已停止状态。

* 实例规格ecs.e-c4m1.large、ecs.e-c2m1.large仅支持在以下地域中购买：中国香港、新加坡、马来西亚（吉隆坡）、印度尼西亚（雅加达）、菲律宾（马尼拉）、泰国（曼谷）、日本（东京）、韩国（首尔）、英国（伦敦）、德国（法兰克福）、美国（弗吉尼亚）、美国（硅谷）。

### 突发性能实例规格族t6

t6的特点如下：

* vCPU持续提供基准性能，可突然提速，但受到CPU积分的限制

* 相比上一代突发性能实例规格族t5，性价比进一步提升

* 计算：

  * 处理器：2.5 GHz主频的最新一代Intel ^®^ Xeon ^®^服务器级别Cascade Lake处理器，睿频3.2 GHz

  * 搭配DDR4内存

* 存储：

  * I/O优化实例

  * 仅支持ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘

    **重要**

    受突发型实例规格限制，PL2和PL3性能级别的ESSD云盘无法发挥极致性能。建议您选择企业级的实例规格或者低性能级别的ESSD云盘。
* 网络：

  * 支持IPv4、IPv6

  * 仅支持专有网络VPC

* 适用场景：

  * Web应用服务器

  * 轻负载应用、微服务

  * 开发测试压测服务应用

t6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>平均基准CPU计算性能</b></p></td> <td><p><b>CPU积分/小时</b></p></td> <td><p><b>最大CPU积分余额</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.t6-c4m1.large</p></td> <td><p>2</p></td> <td><p>0.5</p></td> <td><p>5%</p></td> <td><p>6</p></td> <td><p>144</p></td> <td><p>0.08/最高0.4</p></td> <td><p>4万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c2m1.large</p></td> <td><p>2</p></td> <td><p>1.0</p></td> <td><p>10%</p></td> <td><p>12</p></td> <td><p>288</p></td> <td><p>0.08/最高0.6</p></td> <td><p>6万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m1.large</p></td> <td><p>2</p></td> <td><p>2.0</p></td> <td><p>20%</p></td> <td><p>24</p></td> <td><p>576</p></td> <td><p>0.08/最高1</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>20%</p></td> <td><p>24</p></td> <td><p>576</p></td> <td><p>0.08/最高1</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>30%</p></td> <td><p>36</p></td> <td><p>864</p></td> <td><p>0.08/最高1</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>40%</p></td> <td><p>96</p></td> <td><p>2304</p></td> <td><p>0.16/最高2</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t6-c1m4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>40%</p></td> <td><p>192</p></td> <td><p>4608</p></td> <td><p>0.32/最高4</p></td> <td><p>40万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.t6-c1m1.large、ecs.t6-c1m2.large、ecs.t6-c1m4.large、ecs.t6-c2m1.large、ecs.t6-c4m1.large。

* 您可以前往[ECS实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)，查看实例在各地域的可购情况。

* 指标的含义请参见[实例规格指标说明](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)。

### 突发性能实例规格族t5

t5实例热销中，详细信息请参见[t5实例产品页](https://promotion.aliyun.com/ntms/act/creditinstancet5.html)。  
t5的特点如下：

* vCPU持续提供基准性能，可突然提速，但受到CPU积分的限制

* 计算、内存和网络资源的平衡

* 计算：

  * 多种处理器和内存配比

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ 处理器

  * 搭配DDR4内存

* 存储：仅支持高效云盘和SSD云盘

* 网络：

  * 支持IPv4、IPv6

  * 仅支持专有网络VPC

* 适用场景：

  * Web应用服务器

  * 轻负载应用、微服务

  * 开发测试压测服务应用

t5包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>平均基准CPU计算性能</b></p></td> <td><p><b>CPU积分/小时</b></p></td> <td><p><b>最大CPU积分余额</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.t5-lc2m1.nano</p></td> <td><p>1</p></td> <td><p>0.5</p></td> <td><p>20%</p></td> <td><p>12</p></td> <td><p>288</p></td> <td><p>0.1</p></td> <td><p>4万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-lc1m1.small</p></td> <td><p>1</p></td> <td><p>1.0</p></td> <td><p>20%</p></td> <td><p>12</p></td> <td><p>288</p></td> <td><p>0.2</p></td> <td><p>6万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-lc1m2.small</p></td> <td><p>1</p></td> <td><p>2.0</p></td> <td><p>20%</p></td> <td><p>12</p></td> <td><p>288</p></td> <td><p>0.2</p></td> <td><p>6万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-lc1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>20%</p></td> <td><p>24</p></td> <td><p>576</p></td> <td><p>0.4</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-lc1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>20%</p></td> <td><p>24</p></td> <td><p>576</p></td> <td><p>0.4</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m1.large</p></td> <td><p>2</p></td> <td><p>2.0</p></td> <td><p>25%</p></td> <td><p>30</p></td> <td><p>720</p></td> <td><p>0.5</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>25%</p></td> <td><p>30</p></td> <td><p>720</p></td> <td><p>0.5</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>25%</p></td> <td><p>30</p></td> <td><p>720</p></td> <td><p>0.5</p></td> <td><p>10万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m1.xlarge</p></td> <td><p>4</p></td> <td><p>4.0</p></td> <td><p>25%</p></td> <td><p>60</p></td> <td><p>1440</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m2.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>25%</p></td> <td><p>60</p></td> <td><p>1440</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>25%</p></td> <td><p>60</p></td> <td><p>1440</p></td> <td><p>0.8</p></td> <td><p>20万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m1.2xlarge</p></td> <td><p>8</p></td> <td><p>8.0</p></td> <td><p>25%</p></td> <td><p>120</p></td> <td><p>2880</p></td> <td><p>1.2</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m2.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>25%</p></td> <td><p>120</p></td> <td><p>2880</p></td> <td><p>1.2</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>25%</p></td> <td><p>120</p></td> <td><p>2880</p></td> <td><p>1.2</p></td> <td><p>40万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m1.4xlarge</p></td> <td><p>16</p></td> <td><p>16.0</p></td> <td><p>25%</p></td> <td><p>240</p></td> <td><p>5760</p></td> <td><p>1.2</p></td> <td><p>60万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.t5-c1m2.4xlarge</p></td> <td><p>16</p></td> <td><p>32.0</p></td> <td><p>25%</p></td> <td><p>240</p></td> <td><p>5760</p></td> <td><p>1.2</p></td> <td><p>60万</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.t5-lc2m1.nano、ecs.t5-c1m1.large、ecs.t5-c1m2.large、ecs.t5-c1m4.large、ecs.t5-lc1m1.small、ecs.t5-lc1m2.large、ecs.t5-lc1m2.small、ecs.t5-lc1m4.large。

* 您可以前往[ECS实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)，查看实例在各地域的可购情况。

* 指标的含义请参见[实例规格指标说明](https://help.aliyun.com/document_detail/2849443.html#ad60bb6239ts8)。

### 共享标准型实例规格族s6

* **规格族介绍**：相比上一代共享型实例规格族（xn4、n4、mn4和e4），性价比提升。

* **适用场景**：

  * 中小型网站和Web应用程序。

  * 开发环境、构建服务器、代码存储库、微服务、测试和暂存环境等。

  * 轻量级数据库、缓存。

  * 轻量级企业应用、综合应用服务。

* **计算**：

  * 支持1:1、1:2、1:4多种处理器内存配比。

  * 处理器：2.5 GHz主频的Intel^®^ Xeon^®^ Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定。

  * 搭配DDR4内存。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

    **说明**

    受共享型实例规格限制，PL1、PL2和PL3性能级别的ESSD云盘、SSD云盘无法发挥极致性能，建议您选择高效云盘或PL0性能级别的ESSD云盘。
* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 仅支持专有网络VPC。

s6包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.s6-c1m1.small</p></td> <td><p>1</p></td> <td><p>1.0</p></td> <td><p>0.1</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m2.small</p></td> <td><p>1</p></td> <td><p>2.0</p></td> <td><p>0.1</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m4.small</p></td> <td><p>1</p></td> <td><p>4.0</p></td> <td><p>0.1</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>0.2</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>0.4</p></td> <td><p>20</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m2.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>0.4</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>0.8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m2.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>0.8</p></td> <td><p>60</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.s6-c1m4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>1.2</p></td> <td><p>60</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> <td><p>1</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.s6-c1m1.small、ecs.s6-c1m2.large、ecs.s6-c1m2.small、ecs.s6-c1m4.large、ecs.s6-c1m4.small。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

### CPU超分型实例规格族v5

v5的特点如下：

* 仅支持通过专有宿主机创建v5实例

  **说明**

  其它支持通过专有宿主机创建的实例规格，请参见[规格介绍](https://help.aliyun.com/document_detail/68564.html#concept-h3g-zzm-tdb)。
* 计算：

  * 支持1:1、1:2、1:4、1:8多种处理器内存配比

  * 处理器：2.5 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8163（Skylake）

* 存储：

  * I/O优化实例

  * 支持ESSD云盘、SSD云盘和高效云盘

* 网络：

  * 支持IPv6

* 适用场景：

  * 从线下虚拟化环境迁移至阿里云

  * 中低CPU负载或突发CPU负载业务

v5包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IP</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.v5-c1m1.large</p></td> <td><p>2</p></td> <td><p>2.0</p></td> <td><p>2.0</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.v5-c1m1.xlarge</p></td> <td><p>4</p></td> <td><p>4.0</p></td> <td><p>2.0</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m1.2xlarge</p></td> <td><p>8</p></td> <td><p>8.0</p></td> <td><p>3.0</p></td> <td><p>40</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m1.3xlarge</p></td> <td><p>12</p></td> <td><p>12.0</p></td> <td><p>3.0</p></td> <td><p>40</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m1.4xlarge</p></td> <td><p>16</p></td> <td><p>16.0</p></td> <td><p>4.0</p></td> <td><p>50</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m1.8xlarge</p></td> <td><p>32</p></td> <td><p>32.0</p></td> <td><p>4.0</p></td> <td><p>50</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m2.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>2.0</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.v5-c1m2.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>2.0</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m2.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>3.0</p></td> <td><p>40</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m2.3xlarge</p></td> <td><p>12</p></td> <td><p>24.0</p></td> <td><p>3.0</p></td> <td><p>40</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m2.4xlarge</p></td> <td><p>16</p></td> <td><p>32.0</p></td> <td><p>4.0</p></td> <td><p>50</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m2.8xlarge</p></td> <td><p>32</p></td> <td><p>64.0</p></td> <td><p>4.0</p></td> <td><p>50</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>2.0</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.v5-c1m4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>2.0</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>3.0</p></td> <td><p>40</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m4.3xlarge</p></td> <td><p>12</p></td> <td><p>48.0</p></td> <td><p>3.0</p></td> <td><p>40</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m4.4xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>4.0</p></td> <td><p>50</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m4.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>4.0</p></td> <td><p>50</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m8.large</p></td> <td><p>2</p></td> <td><p>16.0</p></td> <td><p>2.0</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.v5-c1m8.xlarge</p></td> <td><p>4</p></td> <td><p>32.0</p></td> <td><p>2.0</p></td> <td><p>30</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m8.2xlarge</p></td> <td><p>8</p></td> <td><p>64.0</p></td> <td><p>3.0</p></td> <td><p>40</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m8.3xlarge</p></td> <td><p>12</p></td> <td><p>96.0</p></td> <td><p>3.0</p></td> <td><p>40</p></td> <td><p>4</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m8.4xlarge</p></td> <td><p>16</p></td> <td><p>128.0</p></td> <td><p>4.0</p></td> <td><p>50</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.v5-c1m8.8xlarge</p></td> <td><p>32</p></td> <td><p>256.0</p></td> <td><p>4.0</p></td> <td><p>50</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>6</p></td> </tr> </tbody> </table>  
**说明**

指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。

### 上一代共享型实例规格族xn4、n4、mn4、e4

xn4、n4、mn4和e4的特点如下：

* 多种处理器和内存配比。

* 处理器：2.5 GHz主频的Intel^®^ Xeon^®^处理器。

* 搭配DDR4内存。

* I/O优化实例。

* 仅支持IPv4。

<table> <thead> <tr> <td><p><b>规格族</b></p></td> <td><p><b>特点</b></p></td> <td><p><b>vCPU : 内存</b></p></td> <td><p><b>适用场景</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>xn4</p></td> <td><p>共享基本型实例</p></td> <td><p>1:1</p></td> <td> <ul> <li><p>Web应用前端机</p></li> <li><p>轻负载应用、微服务</p></li> <li><p>开发测试压测服务应用</p></li> </ul></td> </tr> <tr> <td><p>n4</p></td> <td><p>共享计算型实例</p></td> <td><p>1:2</p></td> <td> <ul> <li><p>网站和Web应用程序</p></li> <li><p>开发环境、构建服务器、代码存储库、微服务、测试和暂存环境</p></li> <li><p>轻量级企业应用</p></li> </ul></td> </tr> <tr> <td><p>mn4</p></td> <td><p>共享通用型实例</p></td> <td><p>1:4</p></td> <td> <ul> <li><p>网站和Web应用程序</p></li> <li><p>轻量级数据库、缓存</p></li> <li><p>综合应用，轻量级企业服务</p></li> </ul></td> </tr> <tr> <td><p>e4</p></td> <td><p>共享内存型实例</p></td> <td><p>1:8</p></td> <td> <ul> <li><p>大内存应用</p></li> <li><p>轻量级数据库、缓存</p></li> </ul></td> </tr> </tbody> </table>  
共享基本型xn4包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.xn4.small</p></td> <td><p>1</p></td> <td><p>1.0</p></td> <td><p>0.5</p></td> <td><p>5</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，ecs.xn4.small实例规格的实例必须处于已停止状态。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

共享计算型n4包括的实例规格及指标数据如下表所示：。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.n4.small</p></td> <td><p>1</p></td> <td><p>2.0</p></td> <td><p>0.5</p></td> <td><p>5</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n4.large</p></td> <td><p>2</p></td> <td><p>4.0</p></td> <td><p>0.5</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.n4.xlarge</p></td> <td><p>4</p></td> <td><p>8.0</p></td> <td><p>0.8</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.n4.2xlarge</p></td> <td><p>8</p></td> <td><p>16.0</p></td> <td><p>1.2</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.n4.4xlarge</p></td> <td><p>16</p></td> <td><p>32.0</p></td> <td><p>2.5</p></td> <td><p>40</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.n4.8xlarge</p></td> <td><p>32</p></td> <td><p>64.0</p></td> <td><p>5.0</p></td> <td><p>50</p></td> <td><p>2</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.n4.small、ecs.n4.large。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

共享通用型mn4包括的实例规格及指标数据如下表所示：。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.mn4.small</p></td> <td><p>1</p></td> <td><p>4.0</p></td> <td><p>0.5</p></td> <td><p>5</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.mn4.large</p></td> <td><p>2</p></td> <td><p>8.0</p></td> <td><p>0.5</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.mn4.xlarge</p></td> <td><p>4</p></td> <td><p>16.0</p></td> <td><p>0.8</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.mn4.2xlarge</p></td> <td><p>8</p></td> <td><p>32.0</p></td> <td><p>1.2</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.mn4.4xlarge</p></td> <td><p>16</p></td> <td><p>64.0</p></td> <td><p>2.5</p></td> <td><p>40</p></td> <td><p>1</p></td> <td><p>8</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.mn4.8xlarge</p></td> <td><p>32</p></td> <td><p>128.0</p></td> <td><p>5</p></td> <td><p>50</p></td> <td><p>2</p></td> <td><p>8</p></td> <td><p>6</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.mn4.small、ecs.mn4.large。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

共享内存型e4包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS（万）</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.e4.small</p></td> <td><p>1</p></td> <td><p>8.0</p></td> <td><p>0.5</p></td> <td><p>5</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.e4.large</p></td> <td><p>2</p></td> <td><p>16.0</p></td> <td><p>0.5</p></td> <td><p>10</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.e4.xlarge</p></td> <td><p>4</p></td> <td><p>32.0</p></td> <td><p>0.8</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.e4.2xlarge</p></td> <td><p>8</p></td> <td><p>64.0</p></td> <td><p>1.2</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>3</p></td> <td><p>6</p></td> </tr> <tr> <td><p>ecs.e4.4xlarge</p></td> <td><p>16</p></td> <td><p>128.0</p></td> <td><p>2.5</p></td> <td><p>40</p></td> <td><p>1</p></td> <td><p>8</p></td> <td><p>6</p></td> </tr> </tbody> </table>  
**说明**

* 本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.e4.small、ecs.e4.large。

* 指标的含义请参见[实例规格族](https://help.aliyun.com/document_detail/25378.html#section-e9r-xkf-z15)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。

## 企业级ARM计算规格族群
### 通用型实例规格族g8y

* **规格族介绍**：采用阿里云自研倚天710 ARM架构CPU，依托第四代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：容器、微服务，网站和应用服务器，视频编解码，高性能计算，基于CPU的机器学习。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.75 GHz主频的倚天710处理器，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
g8y包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>最大挂载数据盘数量</b></p> </td> <td> <p><b>云盘IOPS基础/突发</b></p> </td> <td> <p><b>云盘带宽基础/突发（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g8y.small</p> </td> <td> <p>1</p> </td> <td> <p>4</p> </td> <td> <p>1/10</p> </td> <td> <p>50万</p> </td> <td> <p>最高25万</p> </td> <td> <p>1</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>3</p> </td> <td> <p>5</p> </td> <td> <p>1万/最高11万</p> </td> <td> <p>1/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>2/10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>6</p> </td> <td> <p>8</p> </td> <td> <p>2万/最高11万</p> </td> <td> <p>1.5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>3/10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>8</p> </td> <td> <p>4万/最高11万</p> </td> <td> <p>2/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>5/10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>15</p> </td> <td> <p>16</p> </td> <td> <p>5万/最高11万</p> </td> <td> <p>3/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>10/25</p> </td> <td> <p>300万</p> </td> <td> <p>40万</p> </td> <td> <p>16</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>8万/最高11万</p> </td> <td> <p>5/最高10</p> </td> </tr> <tr> <td> <p>ecs.g8y.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>16/25</p> </td> <td> <p>500万</p> </td> <td> <p>75万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>16</p> </td> <td> <p>12.5万</p> </td> <td> <p>10</p> </td> </tr> <tr> <td> <p>ecs.g8y.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>32/无</p> </td> <td> <p>1000万</p> </td> <td> <p>150万</p> </td> <td> <p>64</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32</p> </td> <td> <p>25万</p> </td> <td> <p>16</p> </td> </tr> <tr> <td> <p>ecs.g8y.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>512</p> </td> <td> <p>64/无</p> </td> <td> <p>2000万</p> </td> <td> <p>300万</p> </td> <td> <p>64</p> </td> <td> <p>15</p> </td> <td> <p>30</p> </td> <td> <p>30</p> </td> <td> <p>32</p> </td> <td> <p>50万</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>  
**说明**

如需使用ecs.g8y.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 计算型实例规格族c8y

* **规格族介绍**：采用阿里云自研倚天710 ARM架构CPU，依托第四代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**： 容器、微服务，网站和应用服务器，视频编解码，高性能计算，基于CPU的机器学习。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.75 GHz主频的倚天710处理器，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)）。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
c8y包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>最大挂载数据盘数量</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c8y.small</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>1/10</p></td> <td><p>50万</p></td> <td><p>最高25万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>3</p></td> <td><p>5</p></td> <td><p>1万/最高11万</p></td> <td><p>1/最高10</p></td> </tr> <tr> <td><p>ecs.c8y.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>2/10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>2万/最高11万</p></td> <td><p>1.5/最高10</p></td> </tr> <tr> <td><p>ecs.c8y.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>3/10</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8</p></td> <td><p>4万/最高11万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.c8y.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>5/10</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>5万/最高11万</p></td> <td><p>3/最高10</p></td> </tr> <tr> <td><p>ecs.c8y.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>10/25</p></td> <td><p>300万</p></td> <td><p>40万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>8万/最高11万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.c8y.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>16/25</p></td> <td><p>500万</p></td> <td><p>75万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>12.5万</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.c8y.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>32/无</p></td> <td><p>1000万</p></td> <td><p>150万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>25万</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.c8y.32xlarge</p></td> <td><p>128</p></td> <td><p>256</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>50万</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

如需使用ecs.c8y.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 内存型实例规格族r8y

* **规格族介绍**：采用阿里云自研倚天710 ARM架构CPU，依托第四代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**： 容器、微服务，网站和应用服务器，视频编解码，高性能计算，基于CPU的机器学习。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：2.75 GHz主频的倚天710处理器，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

* **安全** ：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](https://help.aliyun.com/document_detail/201394.html)。

* **性能加速**：

选择**性能加速** 及应用后，在您购买的实例里会自动部署选择的应用，并使用KeenTune针对该应用的业务特点进行全栈的专家知识性能调优。更多信息，请参见[应用性能加速](https://help.aliyun.com/document_detail/2409267.html)。  
r8y包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>最大挂载数据盘数量</b></p></td> <td><p><b>云盘IOPS基础/突发</b></p></td> <td><p><b>云盘带宽基础/突发（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.r8y.small</p></td> <td><p>1</p></td> <td><p>8</p></td> <td><p>1/10</p></td> <td><p>50万</p></td> <td><p>最高25万</p></td> <td><p>1</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>3</p></td> <td><p>5</p></td> <td><p>1万/最高11万</p></td> <td><p>1/最高10</p></td> </tr> <tr> <td><p>ecs.r8y.large</p></td> <td><p>2</p></td> <td><p>16</p></td> <td><p>2/10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>6</p></td> <td><p>8</p></td> <td><p>2万/最高11万</p></td> <td><p>1.5/最高10</p></td> </tr> <tr> <td><p>ecs.r8y.xlarge</p></td> <td><p>4</p></td> <td><p>32</p></td> <td><p>3/10</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>8</p></td> <td><p>4万/最高11万</p></td> <td><p>2/最高10</p></td> </tr> <tr> <td><p>ecs.r8y.2xlarge</p></td> <td><p>8</p></td> <td><p>64</p></td> <td><p>5/10</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>15</p></td> <td><p>16</p></td> <td><p>5万/最高11万</p></td> <td><p>3/最高10</p></td> </tr> <tr> <td><p>ecs.r8y.4xlarge</p></td> <td><p>16</p></td> <td><p>128</p></td> <td><p>10/25</p></td> <td><p>300万</p></td> <td><p>40万</p></td> <td><p>16</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>8万/最高11万</p></td> <td><p>5/最高10</p></td> </tr> <tr> <td><p>ecs.r8y.8xlarge</p></td> <td><p>32</p></td> <td><p>256</p></td> <td><p>16/25</p></td> <td><p>500万</p></td> <td><p>75万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>16</p></td> <td><p>12.5万</p></td> <td><p>10</p></td> </tr> <tr> <td><p>ecs.r8y.16xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>32/无</p></td> <td><p>1000万</p></td> <td><p>150万</p></td> <td><p>64</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>25万</p></td> <td><p>16</p></td> </tr> <tr> <td><p>ecs.r8y.32xlarge</p></td> <td><p>128</p></td> <td><p>1024</p></td> <td><p>64/无</p></td> <td><p>2000万</p></td> <td><p>300万</p></td> <td><p>64</p></td> <td><p>15</p></td> <td><p>30</p></td> <td><p>30</p></td> <td><p>32</p></td> <td><p>50万</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

如需使用ecs.r8y.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

### 通用型实例规格族g6r

* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**： 容器、微服务，测试开发（例如DevOps），网站和应用服务器，游戏服务器，基于CPU的机器学习推理。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.8 GHz主频的Ampere^®^ Altra^®^处理器，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

g6r包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络带宽基础/突发（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>连接数</b></p> </td> <td> <p><b>多队列</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> <td> <p><b>单网卡私有IPv4地址数</b></p> </td> <td> <p><b>单网卡IPv6地址数</b></p> </td> <td> <p><b>云盘基础IOPS</b></p> </td> <td> <p><b>云盘基础带宽（Gbit/s）</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.g6r.large</p> </td> <td> <p>2</p> </td> <td> <p>8</p> </td> <td> <p>1/10</p> </td> <td> <p>90万</p> </td> <td> <p>最高25万</p> </td> <td> <p>2</p> </td> <td> <p>3</p> </td> <td> <p>6</p> </td> <td> <p>1</p> </td> <td> <p>1.25万</p> </td> <td> <p>1</p> </td> </tr> <tr> <td> <p>ecs.g6r.xlarge</p> </td> <td> <p>4</p> </td> <td> <p>16</p> </td> <td> <p>1.5/10</p> </td> <td> <p>100万</p> </td> <td> <p>最高25万</p> </td> <td> <p>4</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>2万</p> </td> <td> <p>1.5</p> </td> </tr> <tr> <td> <p>ecs.g6r.2xlarge</p> </td> <td> <p>8</p> </td> <td> <p>32</p> </td> <td> <p>2.5/10</p> </td> <td> <p>160万</p> </td> <td> <p>最高25万</p> </td> <td> <p>8</p> </td> <td> <p>4</p> </td> <td> <p>15</p> </td> <td> <p>1</p> </td> <td> <p>3万</p> </td> <td> <p>2</p> </td> </tr> <tr> <td> <p>ecs.g6r.4xlarge</p> </td> <td> <p>16</p> </td> <td> <p>64</p> </td> <td> <p>5/10</p> </td> <td> <p>200万</p> </td> <td> <p>30万</p> </td> <td> <p>8</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>6万</p> </td> <td> <p>3</p> </td> </tr> <tr> <td> <p>ecs.g6r.8xlarge</p> </td> <td> <p>32</p> </td> <td> <p>128</p> </td> <td> <p>8/10</p> </td> <td> <p>300万</p> </td> <td> <p>60万</p> </td> <td> <p>16</p> </td> <td> <p>7</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>7.5万</p> </td> <td> <p>4</p> </td> </tr> <tr> <td> <p>ecs.g6r.16xlarge</p> </td> <td> <p>64</p> </td> <td> <p>256</p> </td> <td> <p>16/无</p> </td> <td> <p>600万</p> </td> <td> <p>90万</p> </td> <td> <p>32</p> </td> <td> <p>8</p> </td> <td> <p>30</p> </td> <td> <p>1</p> </td> <td> <p>15万</p> </td> <td> <p>8</p> </td> </tr> </tbody> </table>

### 计算型实例规格族c6r

* **规格族介绍**：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。

* **适用场景**：

  * 容器、微服务。

  * 测试开发，例如DevOps。

  * 网站和应用服务器。

  * 基于CPU的机器学习推理。

  * 高性能科学和工程应用。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.8 GHz主频的Ampere^®^ Altra^®^处理器，计算性能稳定。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

  * 实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储I/O性能](https://help.aliyun.com/document_detail/147898.html#concept-2367327)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 小规格实例网络带宽具备突发能力。

  * 实例网络性能与实例规格对应，规格越高网络性能越强。

c6r包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>vCPU</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络带宽基础/突发（Gbit/s）</b></p></td> <td><p><b>网络收发包PPS</b></p></td> <td><p><b>连接数</b></p></td> <td><p><b>多队列</b></p></td> <td><p><b>弹性网卡</b></p></td> <td><p><b>单网卡私有IPv4地址数</b></p></td> <td><p><b>单网卡IPv6地址数</b></p></td> <td><p><b>云盘基础IOPS</b></p></td> <td><p><b>云盘基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.c6r.large</p></td> <td><p>2</p></td> <td><p>4</p></td> <td><p>1/10</p></td> <td><p>90万</p></td> <td><p>最高25万</p></td> <td><p>2</p></td> <td><p>3</p></td> <td><p>6</p></td> <td><p>1</p></td> <td><p>1.25万</p></td> <td><p>1</p></td> </tr> <tr> <td><p>ecs.c6r.xlarge</p></td> <td><p>4</p></td> <td><p>8</p></td> <td><p>1/10</p></td> <td><p>100万</p></td> <td><p>最高25万</p></td> <td><p>4</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>2万</p></td> <td><p>1.5</p></td> </tr> <tr> <td><p>ecs.c6r.2xlarge</p></td> <td><p>8</p></td> <td><p>16</p></td> <td><p>2/10</p></td> <td><p>160万</p></td> <td><p>最高25万</p></td> <td><p>8</p></td> <td><p>4</p></td> <td><p>15</p></td> <td><p>1</p></td> <td><p>3万</p></td> <td><p>2</p></td> </tr> <tr> <td><p>ecs.c6r.4xlarge</p></td> <td><p>16</p></td> <td><p>32</p></td> <td><p>5/10</p></td> <td><p>200万</p></td> <td><p>30万</p></td> <td><p>8</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>6万</p></td> <td><p>3</p></td> </tr> <tr> <td><p>ecs.c6r.8xlarge</p></td> <td><p>32</p></td> <td><p>64</p></td> <td><p>8/10</p></td> <td><p>300万</p></td> <td><p>60万</p></td> <td><p>16</p></td> <td><p>7</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>7.5万</p></td> <td><p>4</p></td> </tr> <tr> <td><p>ecs.c6r.16xlarge</p></td> <td><p>64</p></td> <td><p>128</p></td> <td><p>16/无</p></td> <td><p>600万</p></td> <td><p>90万</p></td> <td><p>32</p></td> <td><p>8</p></td> <td><p>30</p></td> <td><p>1</p></td> <td><p>15万</p></td> <td><p>8</p></td> </tr> </tbody> </table>

## 弹性裸金属服务器规格族群
### GPU计算型弹性裸金属服务器实例规格族ebmgn9g

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn9ge

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn9gc

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn8v

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn8ia

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn8is

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn7ex

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn7e

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn7ix

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn7i

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn7

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn6e

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn6v

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

### GPU计算型弹性裸金属服务器实例规格族ebmgn6i

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

### 计算型弹性裸金属服务器实例规格族ebmc9ae

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

### 计算型弹性裸金属服务器实例规格族ebmc9i

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

### 通用型弹性裸金属服务器实例规格族ebmc8a

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

### 计算型弹性裸金属服务器实例规格族ebmc8y

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

### 计算型弹性裸金属服务器实例规格族ebmc8i

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

### 计算型弹性裸金属服务器实例规格族ebmc7

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

### 计算型弹性裸金属服务器实例规格族ebmc7a

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

### 计算型弹性裸金属服务器实例规格族ebmc6me

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

### 计算型弹性裸金属服务器实例规格族ebmc6a

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

### 计算型（平衡增强）弹性裸金属服务器实例规格族ebmc6e

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

### 计算型弹性裸金属服务器实例规格族ebmc6

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

### 通用型弹性裸金属服务器实例规格族ebmg9ae

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

### 通用型弹性裸金属服务器实例规格族ebmg9a

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

### 通用型弹性裸金属服务器实例规格族ebmg9i

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

### 通用型弹性裸金属服务器实例规格族ebmg8a

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

### 通用型弹性裸金属服务器实例规格族ebmg8y

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

### 通用型弹性裸金属服务器实例规格族ebmg8i

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

### 存储增强型弹性裸金属服务器实例规格族ebmg7se

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

### 通用型弹性裸金属服务器实例规格族ebmg7

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

### 通用型弹性裸金属服务器实例规格族ebmg7a

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

### 通用型弹性裸金属服务器实例规格族ebmg6a

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

### 通用型（平衡增强）弹性裸金属服务器实例规格族ebmg6e

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

### 通用型弹性裸金属服务器实例规格族ebmg6

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

### 内存型弹性裸金属服务器实例规格族ebmr9ae

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

### 内存型弹性裸金属服务器实例规格族ebmr9i

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

### 通用型弹性裸金属服务器实例规格族ebmr8a

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

### 内存型弹性裸金属服务器实例规格族ebmr8y

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

### 内存型弹性裸金属服务器实例规格族ebmr8y

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

### 内存型弹性裸金属服务器实例规格族ebmr7

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

### 内存型弹性裸金属服务器实例规格族ebmr7a

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

### 内存型弹性裸金属服务器实例规格族ebmr6a

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

### 内存型（平衡增强）弹性裸金属服务器实例规格族ebmr6e

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

### 内存型弹性裸金属服务器实例规格族ebmr6

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

### 持久内存型弹性裸金属服务器实例规格族ebmre7p

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

### 持久内存型弹性裸金属服务器实例规格族ebmre6p

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

### 内存增强型弹性裸金属服务器实例规格族ebmre6-6t

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

### 高主频通用型弹性裸金属服务器实例规格族ebmhfg7

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

### 高主频计算型弹性裸金属服务器实例规格族ebmhfc7

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

### 高主频内存型弹性裸金属服务器实例规格族ebmhfr7

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

### 高主频通用型弹性裸金属服务器实例规格族ebmhfg6

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

### 高主频计算型弹性裸金属服务器实例规格族ebmhfc6

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

### 高主频内存型弹性裸金属服务器实例规格族ebmhfr6

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

## 高性能计算\&超级计算集群（SCC）实例规格族群
### 高性能计算优化型实例规格族hpc9a

* **规格族介绍** ：hpc9a专为芯片设计等需要大量内存容量的HPC工作负载而设计，提供高达1:24的超大处理器与内存配比。采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC^™^ Turin 处理器，采用物理核设计，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。

* **适用场景**：芯片设计、其他高性能计算场景。

* **计算**：

  * 处理器与内存（物理核：内存）配比为1:24。最大支持3072GiB内存。

  * 处理器：采用第五代AMD EPYC^™^ Turin处理器，睿频最高5.0GHz，采用物理核设计，计算性能稳定。

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 3/4。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

hpc9a包括的实例规格及指标数据如下表所示：
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>eRDMA网络（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc9a.32xlarge</p></td> <td><p>128</p></td> <td><p>3072</p></td> <td><p>200</p></td> <td><p>200</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

### 高性能计算优化型实例规格族hpc8i

hpc8i正在邀测中，如需使用，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

* **规格族介绍** ：hpc8i实例针对计算密集的应用（如隐式有限元分析、分子动力学和计算化学等）进行了优化，采用最新的Intel^®^Xeon^®^Emerald Rapids处理器，全核睿频3.6 GHz，支持Intel丰富的软件工具生态系统，如Intel数学库和高级矢量扩展（AVX-512）。

* **适用场景**：

  * 工业仿真中计算流体动力学（Computational Fluid Dynamics，CFD）、有限元分析（Finite Element Analysis，FEA）。

  * EDA仿真。

  * 地质勘探。

  * 气象预报。

  * 分子动力学模拟。

  * 其他高性能计算场景。

* **计算**：

  * 处理器与内存配比为1:8。

  * 处理器：采用Intel^®^Xeon^®^Emerald Rapids处理器，主频不低于2.8 GHz，全核睿频3.6 GHz，计算性能稳定。

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[弹性临时盘](https://help.aliyun.com/document_detail/2716262.html)、[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

  * 支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](https://help.aliyun.com/document_detail/200512.html#section-vtb-klu-z5y)。

hpc8i包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>eRDMA网络（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc8i.32xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>100</p></td> <td><p>100</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

### 高性能计算优化型实例规格族hpc8ae

* **规格族介绍**：hpc8ae实例专为工业仿真、EDA（Electronic Design Automation）仿真、地质勘探、气象预报、分子动力学模拟等计算和网络密集的紧密耦合的HPC工作负载而设计。提供高达3.75 GHz的最新的第四代EPYC™（Genoa）处理器、64 Gbps的eRDMA节点间网络带宽以及增强的内存带宽能力。

* **适用场景**：

  * 工业仿真中计算流体动力学（Computational Fluid Dynamics，CFD）、有限元分析（Finite Element Analysis，FEA）。

  * EDA仿真。

  * 地质勘探。

  * 气象预报。

  * 分子动力学模拟。

  * 其他高性能计算场景。

* **计算**：

  * 处理器与内存配比为1:4

  * 处理器：3.4 GHz主频的AMD EPYC^TM^Genoa处理器，单核睿频最高3.75 GHz，计算性能稳定

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用eRDMA](https://help.aliyun.com/document_detail/336853.html#task-2128004)。

hpc8ae包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> <td><p><b>eRDMA网络（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc8ae.32xlarge</p></td> <td><p>64</p></td> <td><p>256</p></td> <td><p>64</p></td> <td><p>64</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

### 高性能计算优化型实例规格族hpc7ip

* **规格族介绍：**hpc7ip专为芯片设计等需要大量内存容量的HPC工作负载而设计。依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。提供高达1:32的超大处理器与内存配比，搭配Intel傲腾持久内存介质，极大幅度降低内存型应用单GiB内存的成本。

* **适用场景**：芯片设计、其他高性能计算场景。

* **计算**：

  * 处理器与内存（内存+持久内存）配比约为1:32。

  * 处理器：采用第三代Intel^®^Xeon^®^可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 最大支持2560 GiB内存（512 GiB DRAM内存+2048 GiB Intel ^®^傲腾 ^TM^持久内存）。

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

hpc7ip包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>持久内存（GiB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc7ip.32xlarge</p></td> <td><p>64</p></td> <td><p>512</p></td> <td><p>2048</p></td> <td><p>64</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

### 高性能计算优化型实例规格族hpc6id

* **规格族介绍**：hpc6id专为芯片设计等需要大量内存容量和本地数据访问的HPC工作负载而设计。依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。提供超大内存和2块3.8 TB本地数据盘，降低内存和数据受限应用的使用成本。

* **适用场景**：芯片设计、地震油藏和结构模拟、其他高性能计算场景。

* **计算**：

  * 处理器与内存配比约为1:38。

  * 处理器：Intel^®^Xeon^®^可扩展处理器（Cascade Lake），基频 3.1 GHz，全核睿频3.5 GHz，计算性能稳定。

  * 不支持开启超线程配置。

  * 与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。

* **存储**：

  * I/O优化实例。

  * 支持NVMe协议。详情参见[NVMe协议概述](https://help.aliyun.com/document_detail/450574.html)。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 具备超高网络收发包PPS能力。

hpc6id包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td><p><b>实例规格</b></p></td> <td><p><b>物理内核</b></p></td> <td><p><b>内存（GiB）</b></p></td> <td><p><b>本地存储（GB）</b></p></td> <td><p><b>网络基础带宽（Gbit/s）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>ecs.hpc6id.20xlarge</p></td> <td><p>40</p></td> <td><p>1536</p></td> <td><p>2 \* 3840</p></td> <td><p>32</p></td> </tr> </tbody> </table>  
**说明**

该规格族支持Rocky Linux 8、Rocky Linux 9镜像。

### 通用型超级计算集群实例规格族sccg7

* **规格族介绍** ：具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* **适用场景**： 大规模机器学习训练；大规模高性能科学计算和仿真计算；大规模数据分析、批量计算、视频编码。

* **计算**：

  * 处理器与内存配比为1:4。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8369（Ice lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信。

sccg7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>物理内核</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>RoCE网络（Gbit/s）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sccg7.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>64</p> </td> <td> <p>512.0</p> </td> <td> <p>100</p> </td> <td> <p>2400万</p> </td> <td> <p>200</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

### 计算型超级计算集群实例规格族sccc7

* **规格族介绍** ：具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](https://help.aliyun.com/document_detail/60576.html#concept-lnh-hv2-5db)。

* **适用场景**： 大规模机器学习训练；大规模高性能科学计算和仿真计算；大规模数据分析、批量计算、视频编码。

* **计算**：

  * 处理器与内存配比为1:2。

  * 处理器：2.9 GHz主频的Intel ^®^ Xeon ^®^ Platinum 8369（Ice lake），全核睿频3.5 GHz。

* **存储**：

  * I/O优化实例。

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)、[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信。

sccc7包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>物理内核</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>RoCE网络（Gbit/s）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sccc7.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>64</p> </td> <td> <p>256.0</p> </td> <td> <p>100</p> </td> <td> <p>2400万</p> </td> <td> <p>200</p> </td> <td> <p>32</p> </td> </tr> </tbody> </table>

### GPU计算型超级计算集群实例规格族sccgn7ex

* **规格族介绍**：sccgn7ex是阿里云为了面对日益增长的大规模AI训练需求开发的高带宽超算集群实例。多台裸金属服务器之间采用第三代RDMA SCC网络互联，支持800 G的互联带宽。您可以根据训练需求弹性选择线上集群数量，快速满足大规模AI参数训练的需求。

* **适用场景**：超大规模AI训练场景。

* **计算**：

  * 支持NVSwitch，算力高达312T（TF32）。

  * 处理器与内存配比为1:8。

  * 处理器：采用第三代Intel^®^ Xeon^®^ 8369可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，支持PCIe 4.0接口。

* **存储**：

  * I/O优化实例

  * 支持的云盘类型：[ESSD云盘](https://help.aliyun.com/document_detail/122389.html)、[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)和[ESSD同城冗余云盘](https://help.aliyun.com/document_detail/2803814.html)。更多云盘信息，请参见[块存储概述](https://help.aliyun.com/document_detail/63136.html)。

* **网络**：

  * 支持IPv4、IPv6。关于IPv6通信，参见[IPv6通信](https://help.aliyun.com/document_detail/98719.html)。

  * 仅支持专有网络VPC。

  * 超高网络性能，2400万PPS网络收发包能力。

  * sccgn7ex实例间支持800 Gbit/s的互联带宽（4 \* 双口100 Gbit/s RDMA），支持GPUDirect，每颗GPU直连一个100 Gbit/s网口。

sccgn7ex包括的实例规格及指标数据如下表所示。
<table> <thead> <tr> <td> <p><b>实例规格</b></p> </td> <td> <p><b>vCPU</b></p> </td> <td> <p><b>内存（GiB）</b></p> </td> <td> <p><b>GPU显存（GB）</b></p> </td> <td> <p><b>网络基础带宽（Gbit/s）</b></p> </td> <td> <p><b>网络收发包PPS</b></p> </td> <td> <p><b>RoCE网络（Gbit/s）</b></p> </td> <td> <p><b>弹性网卡</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p>ecs.sccgn7ex.32xlarge</p> </td> <td> <p>128</p> </td> <td> <p>1024</p> </td> <td> <p>80 GB \* 8</p> </td> <td> <p>64</p> </td> <td> <p>2400万</p> </td> <td> <p>800</p> </td> <td> <p>15</p> </td> </tr> </tbody> </table>

### 计算网络增强型弹性裸金属服务器实例规格族ebmc5s

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

### 通用网络增强型弹性裸金属服务器实例规格族ebmg5s

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

### 内存网络增强型弹性裸金属服务器实例规格族ebmr5s

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

### 通用型弹性裸金属服务器实例规格族ebmg5

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

## 异构计算规格族群
### GPU虚拟化型实例规格族sgn8ia

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

### GPU虚拟化型实例规格族sgn7i-vws（共享CPU）

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

### GPU虚拟化型实例规格族vgn7i-vws

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

### GPU虚拟化型实例规格族vgn6i-vws

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

### GPU计算型实例规格族gn9gc

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

### GPU计算型实例规格族gn8v/gn8v-tee

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

### GPU计算型实例规格族gn8is

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

### GPU计算型实例规格族gn7e

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

### GPU计算型实例规格族gn7i

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

### GPU计算型实例规格族gn7s

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

### GPU计算型实例规格族gn7

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

### GPU计算型实例规格族gn7r

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

### GPU计算型实例规格族gn6i

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

### GPU计算型实例规格族gn6e

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

### GPU计算型实例规格族gn6v

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

### video-trans

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
