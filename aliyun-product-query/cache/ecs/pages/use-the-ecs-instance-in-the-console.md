WordPress 是一款主流的开源建站工具。使用 ECS 部署WordPress 后，可以快速搭建网站并发布文章。  

## **操作步骤**
请保证[账号已完成实名认证](https://help.aliyun.com/document_detail/37195.html)，且阿里云账户余额（即现金余额）与代金券的总额不低于100.00元人民币的情况下执行以下操作。  
**重要**

完成实名认证的云服务器ECS新用户，可免费试用ECS 3个月，详细限制参见[云服务器ECS试用攻略](https://help.aliyun.com/document_detail/2839344.html)。

### 步骤一：创建ECS实例

1. 访问[ECS控制台-实例](https://ecs.console.aliyun.com/server/region)，单击**创建实例**。

2. 选择**自定义购买**，完成购买配置。

   > 配置示例值可供参考，未提及配置项按照默认即可。
   <table> <thead> <tr> <td><p><b>配置项</b></p></td> <td><p><b>配置示例值</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p><b>付费类型</b></p></td> <td><p><b>按量付费</b></p></td> </tr> <tr> <td><p><b>地域</b></p></td> <td><p><span>华南2（河源）</span></p></td> </tr> <tr> <td><p><b>网络及可用区</b></p></td> <td><p>专有网络：默认专有网络</p><p>交换机：选择可用区B的默认交换机。</p></td> </tr> <tr> <td><p><b>实例</b></p></td> <td><p>ecs.c9i.large</p> <blockquote> 为保证流畅运行，建议实例规格不低于2 vCPU 4 GiB。 </blockquote></td> </tr> <tr> <td><p><b>镜像</b></p></td> <td><p>选择公共镜像下 Alibaba Cloud Linux 3.2104 LTS 64位。</p></td> </tr> <tr> <td><p><b>系统盘</b></p></td> <td><p>类型：ESSD 云盘</p><p>容量：40 GiB</p></td> </tr> <tr> <td><p><b>公网IP</b></p></td> <td><p>勾选<b>分配公网 IPv4 地址</b>。</p></td> </tr> <tr> <td><p><b>带宽计费模式</b></p></td> <td><p><b>按使用流量</b></p> <blockquote> 建议 <b>升级至CDT计费</b>，升级后赠送220GB/月公网流量（中国内地地域20GB/月，非中国内地200GB/月）。 </blockquote></td> </tr> <tr> <td><p><b>安全组</b></p></td> <td><p>选择<b>新建安全组</b>，在<b>普通安全组</b>的<b>开通IPv4端口/协议</b>处，新增勾选<b>HTTP (TCP：80)</b>和<b>SSH (TCP:22)</b>，允许外部HTTP访问。</p></td> </tr> <tr> <td><p><b>登录凭证</b></p></td> <td><p>选择<b>创建后设置</b>。</p></td> </tr> </tbody> </table>
3. 确认配置费用，阅读并勾选服务协议，单击**确认下单**。

### 步骤二：连接ECS实例

1. 返回实例列表，待实例状态为**运行中** ，且**健康状态** 为**正常** 后，单击**操作** 列的**远程连接**。

2. 在对话框中，单击**通过Workbench远程连接** 对应的**立即登录**。

3. 选择**免密连接** 后，单击**登录**。

   > 远程连接会话最久维持6个小时，如果超过6小时没有任何操作，连接会自动断开，需要重新连接。

看到命令行即表示连接成功。

### 步骤三：搭建WordPress

1. 部署 LNMP 环境。

   执行以下脚本一键部署 Wordpress 所需的 LNMP 环境（Linux + Nginx + MySQL + PHP）。执行前将`MYSQL_PASSWORD`替换为自定义的MySQL root密码 ，后续搭建 Wordpress 数据库时需要使用。
   > 密码长度须为8至30个字符，且必须同时包含大小写英文字母、数字和特殊符号，其中特殊符号包含 ``()` ~!@#$%^&*-+=|{}[]:;'<>,.?/``。

   ```
   HELPCODEESCAPE-shell
   curl -fsSL https://help-static-aliyun-doc.aliyuncs.com/install-script/deploy-lnmp-acl3_2.sh | MYSQL_ROOT_PASS='MYSQL_PASSWORD' bash
   ```

   > 脚本仅适用于Alibaba Cloud Linux 3.2104 LTS 64位。
2. 登录 MySQL，创建 WordPress 专用数据库和用户。

   * `MYSQL_PASSWORD`：填写为[上一步](#a8b09613a92bu)设置的MySQL密码。

   * `WORDPRESS_PASSWORD`：自定义WordPress的用户密码。

     > 密码长度须为8至30个字符，且必须同时包含大小写英文字母、数字和特殊符号，其中特殊符号包含 ``()` ~!@#$%^&*-+=|{}[]:;'<>,.?/``。

   ```
   HELPCODEESCAPE-shell
   mysql -u root -p'MYSQL_PASSWORD' <<EOF
   CREATE DATABASE wordpress;
   CREATE USER 'wordpress_user'@'localhost' IDENTIFIED BY 'WORDPRESS_PASSWORD';
   GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress_user'@'localhost';
   FLUSH PRIVILEGES;
   EOF
   ```

   指令将创建一个名为`wordpress`的数据库和一个具有该数据库全部权限的`wordpress_user`用户。
3. 下载并解压 WordPress。

   ```
   HELPCODEESCAPE-shell
   cd /usr/share/nginx/html && sudo wget https://cn.wordpress.org/wordpress-6.4.4-zh_CN.zip && sudo yum install unzip -y && sudo unzip wordpress-6.4.4-zh_CN.zip
   ```

4. 配置数据库连接。

   1. 备份默认配置。

      ```
      HELPCODEESCAPE-shell
      sudo cp /usr/share/nginx/html/wordpress/wp-config-sample.php /usr/share/nginx/html/wordpress/wp-config.php
      ```

   2. 编辑 `wp-config.php`，将`WORDPRESS_PASSWORD`替换为设置的 [WordPress 用户密码](#e87f27d9e95x6)。

      ```
      HELPCODEESCAPE-shell
      sudo sed -i "s/database_name_here/wordpress/" /usr/share/nginx/html/wordpress/wp-config.php && \sudo sed -i "s/username_here/wordpress_user/" /usr/share/nginx/html/wordpress/wp-config.php && \sudo sed -i "s/password_here/WORDPRESS_PASSWORD/" /usr/share/nginx/html/wordpress/wp-config.php
      ```

5. 更新 Nginx 站点根目录并重启。

   ```
   HELPCODEESCAPE-shell
   sudo sed -i 's|root /usr/share/nginx/html;|root /usr/share/nginx/html/wordpress;|' /etc/nginx/conf.d/default.conf && sudo nginx -t && sudo systemctl restart nginx
   ```

### 步骤四：安装WordPress并发布第一篇文章

1. 安装并登录Wordpress。

   1. 在本地浏览器中访问 `http://<ECS公网IP>`，进入 WordPress 安装页面。

      > `<ECS公网IP地址>`可在实例列表的 **IP地址**列获取。
   2. 填写站点标题、管理员用户名、密码和邮箱，单击**安装WordPress**。

   3. 安装完成后，单击**登录**，输入上一步设置的用户名和密码。

2. 发布文章验证访问。

   1. 在左侧导航栏，单击**文章** \> **新增文章**。

   2. 输入标题（如"Hello from Alibaba Cloud ECS"），单击右上角**发布** ，在确认弹窗中再次单击**发布**。

   3. 复制并打开**文章地址**，页面显示刚才发布的文章，表示网站已对外可用。

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

* [重置实例登录密码](https://help.aliyun.com/document_detail/25439.html)

* [ECS常用操作导航](https://help.aliyun.com/document_detail/25429.html#concept-q3w-45w-wdb)

* [搭建FTP站点（Linux）](https://help.aliyun.com/document_detail/92048.html)上传WordPress主题或者插件。

* 直接使用IP地址访问网站不专业且不安全，建议为网站[绑定域名并启用HTTPS加密](https://help.aliyun.com/document_detail/151691.html#72882c529dyyb)。

* [手动部署LNMP环境](https://help.aliyun.com/document_detail/97251.html)。

* 若实例规格无法满足应用需求，可以[变更实例规格](https://help.aliyun.com/document_detail/60051.html)。

* 通过ROS，云市场镜像或Terraform[快速搭建WordPress](https://help.aliyun.com/document_detail/2858754.html)。

* [在Docker中部署WordPress](https://help.aliyun.com/document_detail/51853.html#783faa2042ufb)。

* 在宝塔面板中安装WordPress，请参见[手动部署宝塔面板](https://help.aliyun.com/document_detail/2846544.html)。
