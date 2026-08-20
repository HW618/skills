配备持久内存的实例（例如re7p、r7p、re6p-redis）提供超大CPU内存配比，在此种实例上运行Redis应用可大幅降低单GiB内存成本。本文以部分操作系统为例，介绍如何在这类实例上快速部署Redis应用。  

## 背景信息
本文中快速部署Redis应用的步骤适用于特定的实例规格和镜像版本，要求如下：

* 实例规格：

  * [re7p](https://help.aliyun.com/document_detail/25378.html#re7p)：ecs.re7p.large、ecs.re7p.xlarge、ecs.re7p.2xlarge、ecs.re7p.16large、ecs.re7p.32xlarge

  * [r7p](https://help.aliyun.com/document_detail/25378.html#r7p)：ecs.r7p.large、ecs.r7p.xlarge、ecs.r7p.2xlarge、ecs.r7p.16large、ecs.r7p.32xlarge

  * [re6p](https://help.aliyun.com/document_detail/25378.html#re6p)：ecs.re6p-redis.large、ecs.re6p-redis.xlarge、ecs.re6p-redis.2xlarge、ecs.re6p-redis.4xlarge、ecs.re6p-redis.13xlarge

* 镜像：

  * Alibaba Cloud Linux 2

  * CentOS 7.6及更高版本

  * Ubuntu 18.04、Ubuntu 20.04

## 在Alibaba Cloud Linux 2中部署Redis应用
Alibaba Cloud Linux 2针对Redis应用进行了专项调优，相比社区版操作系统，Redis应用整体性能提升20%以上。

Alibaba Cloud Linux 2内置Redis 6.0.5和Redis 3.2.12的yum源，执行sudo yum install命令即可部署Redis 6.0.5和Redis 3.2.12。您也可以手动部署其他版本的Redis应用，具体操作，请参见[在CentOS中部署Redis应用](#section-gx2-rzq-8rk)和[在Ubuntu中部署Redis应用](#section-1wv-dbw-s9f)。  
本步骤中相关资源的配置如下：

* 实例规格：ecs.re6p-redis.2xlarge

* 镜像：Alibaba Cloud Linux 2.1903 LTS 64位

1. 购买持久内存实例。

   具体操作，请参见[自定义购买实例](https://help.aliyun.com/document_detail/87190.html#task-vwq-5g4-r2b)。请注意以下配置：
   * **实例** ：单击**x86 计算** 架构下的**内存型**，并选中名称为ecs.re6p-redis.2xlarge的实例规格。

   * **镜像**：选择Alibaba Cloud Linux 2.1903 LTS 64位。

2. 登录实例。

   具体操作，请参见[选择ECS远程连接方式](https://help.aliyun.com/document_detail/71529.html#concept-tmr-pgx-wdb)。
3. 根据需要部署Redis 6.0.5或Redis 3.2.12。

   * 部署Redis 6.0.5：

     ```
     HELPCODEESCAPE-shell
     sudo yum install -y alinux-release-experimentals && \
     sudo yum install -y redis-6.0.5
     ```

   * 部署Redis 3.2.12：

     ```
     HELPCODEESCAPE-shell
     sudo yum install -y alinux-release-experimentals && \
     sudo yum install -y redis-3.2.12
     ```

4. 启动Redis应用（配置默认使用的普通内存和持久内存容量）。

   示例命令如下：
   * 普通内存与持久内存的推荐配比为1:4。

     ```
     HELPCODEESCAPE-shell
     export MEMKIND_DAX_KMEM_NODES=1 && \
     sudo redis-server /etc/redis.conf --port 8369 --memory-alloc-policy ratio --dram-pmem-ratio 1 4 --hashtable-on-dram yes --daemonize yes --logfile /tmp/redis_8369.log --protected-mode no --bind 0.0.0.0
     ```

   * 您也可以自定义普通内存与持久内存的配比，保留部分普通内存以运行其他应用，例如配比为1:16、分配内存34 GiB（其中普通内存2 GiB、持久内存32 GiB）。

     ```
     HELPCODEESCAPE-shell
     export MEMKIND_DAX_KMEM_NODES=1 && \
     sudo redis-server /etc/redis.conf --port 8369 --memory-alloc-policy ratio --dram-pmem-ratio 1 16 --maxmemory 34G
     ```

## 在CentOS中部署Redis应用
本步骤中使用的资源和软件配置如下：

* 实例规格：ecs.re6p-redis.2xlarge

* 镜像：CentOS 7.6

* Redis：Redis 4.0.14

* memkind：memkind 1.10.1-rc2

**说明**

请确保从（https://github.com/）下载资源成功后再进行后续操作。如果下载失败，请重复执行相关命令直至下载成功。

1. 购买持久内存实例。

   具体操作，请参见[自定义购买实例](https://help.aliyun.com/document_detail/87190.html#task-vwq-5g4-r2b)。请注意以下配置：
   * **实例** ：单击**x86 计算** 架构下的**内存型**，并选中名称为ecs.re6p-redis.2xlarge的实例规格。

   * **镜像**：选择CentOS 7.6 64位。

2. 登录实例。

   具体操作，请参见[选择ECS远程连接方式](https://help.aliyun.com/document_detail/71529.html#concept-tmr-pgx-wdb)。
3. 准备编译环境。

   ```
   HELPCODEESCAPE-shell
   export MEMKIND_DAX_KMEM_NODES=1 && \
   sudo yum -y install numactl-devel.x86_64 && \
   sudo yum -y groupinstall 'Development Tools'
   ```

4. 准备Redis 4.0.14源码。

   ```
   HELPCODEESCAPE-shell
   sudo wget https://github.com/redis-io/redis/archive/4.0.14.tar.gz && \
   sudo wget https://github.com/redis/redis/compare/4.0.14...tieredmemdb:4.0.14-devel.diff -O redis_4.0.14_diff_tieredmemdb.patch && \
   tar xzvf 4.0.14.tar.gz && \
   cd redis-4.0.14 && \
   git apply --ignore-whitespace ../redis_4.0.14_diff_tieredmemdb.patch
   ```

   **说明**

   patch用于使能持久内存，不同Redis版本使用的patch不同。更多信息，请参见[下载使能持久内存的patch](#section-7l0-0ys-dm0)。
5. 准备memkind源码。

   memkind是内存管理工具，用于分配管理持久内存。
   1. 下载memkind源码。

      ```
      HELPCODEESCAPE-shell
      sudo wget https://github.com/memkind/memkind/archive/v1.10.1-rc2.tar.gz && \
      tar xzvf v1.10.1-rc2.tar.gz && \
      mv memkind-1.10.1-rc2/* ./deps/memkind
      ```

   2. **可选：**调整makefile。

      **说明**

      您可以先运行`ldd --version`查看glibc版本。如果glibc版本低于2.17，请升级glibc版本。具体操作，请参见[查看和升级glibc版本](https://help.aliyun.com/document_detail/441403.html#section-51o-dl0-jh3)。如果glibc版本等于或高于2.17，可以跳过以下操作直接开始编译Redis。

      ```
      HELPCODEESCAPE-shell
      cd ./deps/memkind && \
      sudo wget https://github.com/memKeyDB/memKeyDB/wiki/files/0001-Use-secure_getenv-when-possible.patch && \
      git apply --ignore-whitespace 0001-Use-secure_getenv-when-possible.patch && \
      cd ../../
      ```

      **说明**

      如果patch下载失败，再执行命令时无需包括`cd ./deps/memkind && \`。
6. 编译安装Redis。

   ```
   HELPCODEESCAPE-shell
   make clean && \
   make distclean && \
   make MALLOC=memkind -j 4 && \
   sudo make install
   ```

7. 启动Redis应用（配置默认使用的普通内存和持久内存容量）。

   示例命令如下：  
   **说明**

   /home/user请替换成实际的用户目录。
   * 普通内存与持久内存的推荐配比为1:4。

     ```
     HELPCODEESCAPE-shell
     redis-server /home/user/redis-4.0.14/redis.conf --port 8369 --memory-alloc-policy ratio --dram-pmem-ratio 1 4 --hashtable-on-dram yes --daemonize yes --logfile /tmp/redis_8369.log --protected-mode no --bind 0.0.0.0
     ```

   * 您也可以自定义普通内存与持久内存的配比，保留部分普通内存以运行其他应用，例如配比为1:16、分配内存34 GiB（其中普通内存2 GiB、持久内存32 GiB）。

     ```
     HELPCODEESCAPE-shell
     redis-server /home/user/redis-4.0.14/redis.conf --port 8369 --memory-alloc-policy ratio --dram-pmem-ratio 1 16 --maxmemory 34G
     ```

## 在Ubuntu中部署Redis应用
本步骤中相关资源和软件的配置如下：

* 实例规格：ecs.re6p-redis.2xlarge

* 镜像：Ubuntu 20.04

* Redis：Redis 6.2.5

* memkind：memkind 1.10.1-rc2

**说明**

请确保从（https://github.com/）下载资源成功后再进行后续操作。如果下载失败，请重复执行相关命令直至下载成功。

1. 购买持久内存实例。

   具体操作，请参见[自定义购买实例](https://help.aliyun.com/document_detail/87190.html#task-vwq-5g4-r2b)。请注意以下配置：
   * **实例** ：单击**x86 计算** 架构下的**内存型**，并选中名称为ecs.re6p-redis.2xlarge的实例规格。

   * **镜像**：选择Ubuntu 20.04 64位。

2. 登录实例。

   具体操作，请参见[选择ECS远程连接方式](https://help.aliyun.com/document_detail/71529.html#concept-tmr-pgx-wdb)。
3. 准备编译环境。

   ```
   HELPCODEESCAPE-shell
   export MEMKIND_DAX_KMEM_NODES=1 && \
   sudo apt update && \
   sudo apt -y install git && \
   sudo apt install -y libnuma-dev && \
   sudo apt install -y numactl
   ```

4. 准备Redis 6.2.5源码。

   ```
   HELPCODEESCAPE-shell
   sudo wget https://download.redis.io/releases/redis-6.2.5.tar.gz && \
   sudo wget https://github.com/redis/redis/compare/6.2.5...tieredmemdb:6.2.5-devel.diff -O redis_6.2.5_diff_tieredmemdb.patch && \
   tar xzf redis-6.2.5.tar.gz && \
   cd redis-6.2.5 && \
   git apply --ignore-whitespace ../redis_6.2.5_diff_tieredmemdb.patch
   ```

   **说明**

   patch用于使能持久内存，不同Redis版本使用的patch不同。更多信息，请参见[下载使能持久内存的patch](#section-7l0-0ys-dm0)。
5. 准备memkind源码。

   memkind是内存管理工具，用于分配管理持久内存。
   1. 下载memkind源码。

      ```
      HELPCODEESCAPE-shell
      sudo wget https://github.com/memkind/memkind/archive/v1.10.1-rc2.tar.gz && \
      tar xzvf v1.10.1-rc2.tar.gz && \
      mv memkind-1.10.1-rc2/* ./deps/memkind/
      ```

   2. 调整makefile。

      **说明**

      您可以先运行`ldd --version`查看glibc版本。如果glibc版本低于2.17，请升级glibc版本。具体操作，请参见[查看和升级glibc版本](https://help.aliyun.com/document_detail/441403.html#section-51o-dl0-jh3)。如果glibc版本等于或高于2.17，可以跳过以下操作直接开始编译Redis。

      ```
      HELPCODEESCAPE-shell
      cd ./deps/memkind && \
      sudo wget --no-check-certificate https://github.com/memKeyDB/memKeyDB/wiki/files/0001-Use-secure_getenv-when-possible.patch && \
      git apply --ignore-whitespace 0001-Use-secure_getenv-when-possible.patch && \
      cd ../../
      ```

      **说明**

      如果patch下载失败，再执行命令时无需包括`cd ./deps/memkind && \`。
6. 编译安装Redis。

   ```
   HELPCODEESCAPE-shell
   make clean && \
   make distclean && \
   make MALLOC=memkind -j 4 && \
   sudo make install
   ```

7. 启动Redis应用（配置默认使用的普通内存和持久内存容量）。

   示例命令如下：  
   **说明**

   /home/user请替换成实际的用户目录。
   * 普通内存与持久内存的推荐配比为1:4。

     ```
     HELPCODEESCAPE-shell
     redis-server /home/user/redis-6.2.5/redis.conf --port 8369 --memory-alloc-policy ratio --dram-pmem-ratio 1 4 --hashtable-on-dram yes --daemonize yes --logfile /tmp/redis_8369.log --protected-mode no --bind 0.0.0.0
     ```

   * 您也可以自定义普通内存与持久内存的配比，保留部分普通内存以运行其他应用，例如配比为1:16、分配内存34 GiB（其中普通内存2 GiB、持久内存32 GiB）。

     ```
     HELPCODEESCAPE-shell
     redis-server /home/user/redis-6.2.5/redis.conf --port 8369 --memory-alloc-policy ratio --dram-pmem-ratio 1 16 --maxmemory 34G
     ```

## 下载使能持久内存的patch
替换示例命令中的下载地址以及文件名中对应的版本号即可，例如下载Redis 6.2.5适用的patch的命令如下：

```
HELPCODEESCAPE-shell
sudo wget https://github.com/redis/redis/compare/6.2.5...tieredmemdb:6.2.5-devel.diff -O redis_6.2.5_diff_tieredmemdb.patch
```

目前支持的patch的下载地址如下所示：

* Redis 6.2

  <https://github.com/redis/redis/compare/6.2.5...tieredmemdb:6.2.5-devel.diff>
* Redis 6.0

  * <https://github.com/redis/redis/compare/6.0.9...tieredmemdb:6.0.9-devel.diff>

  * <https://github.com/redis/redis/compare/6.0.5...tieredmemdb:6.0.5-devel.diff>

  * <https://github.com/redis/redis/compare/6.0.3...tieredmemdb:6.0.3-devel.diff>

  * <https://github.com/redis/redis/compare/6.0.0...tieredmemdb:6.0.0-devel.diff>

* Redis 5.0

  * <https://github.com/redis/redis/compare/5.0.9...tieredmemdb:5.0.9-devel.diff>

  * <https://github.com/redis/redis/compare/5.0.2...tieredmemdb:5.0.2-devel.diff>

  * <https://github.com/redis/redis/compare/5.0.0...tieredmemdb:5.0.0-devel.diff>

* Redis 4.0

  * <https://github.com/redis/redis/compare/4.0.14...tieredmemdb:4.0.14-devel.diff>

  * <https://github.com/redis/redis/compare/4.0.9...tieredmemdb:4.0.9-devel.diff>

  * <https://github.com/redis/redis/compare/4.0.2...tieredmemdb:4.0.2-devel.diff>

  * <https://github.com/redis/redis/compare/4.0.0...tieredmemdb:4.0.0-devel.diff>

* Redis 3.0

  <https://github.com/redis/redis/compare/3.2.12...tieredmemdb:3.2.diff>
