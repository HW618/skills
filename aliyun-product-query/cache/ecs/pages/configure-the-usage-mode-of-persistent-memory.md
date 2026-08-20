持久内存支持的使用方式和实例规格有关，本文介绍如何将持久内存配置为本地盘以及可以配置为本地盘的持久内存型实例（ecs.re6p规格和ecs.i4p规格）使用llpl库分配内存池失败的解决方案。  

## 前提条件
持久内存适用于特定的实例规格和镜像版本，要求如下：

* 实例规格

  * 作为内存使用的规格：ecs.re6p-redis、ecs.re7p、ecs.r7p

    **重要**

    作为内存使用时：
    * 购买后无需进行初始化即可使用。

    * 无持久化特性，停机或重启后，数据会丢失。

  * 作为本地盘使用的规格：ecs.re6p、ecs.i4p

    **重要**

    作为本地盘使用时：
    * 购买后需要进行盘的初始化，具体操作，请参见[将持久内存配置为一块本地盘](#section-t66-l5n-e1g)。

    * 具备持久化特性，但作为本地盘存储数据有丢失数据的风险，建议您做好必要的数据备份。关于本地盘的更多信息，请参见[本地盘](https://help.aliyun.com/document_detail/63138.html)。

* 镜像：

  * Alibaba Cloud Linux 2

  * CentOS 7.6及更高版本

  * Ubuntu 18.04、Ubuntu 20.04

## 背景信息
持久内存的访问速度比普通内存慢，但性价比更高，可以作为本地存储使用。作为本地存储使用时，在停机或重启后，持久内存中的数据不会丢失。持久内存的使用方式：

* 作为内存使用：您可以将部分原本存放在普通内存中的数据存放到持久内存中，例如对访问速度要求较低的非热点数据。持久内存容量大，单GiB价格更实惠，可以帮助您大幅降低单GiB内存的整体拥有成本（TCO）。

* 作为本地盘使用：支持块数据读写，IO性能极高，读写延时低至170 ns。因此，您可以为需要更高稳定RT（响应时间）的核心应用数据库选用持久内存。您也可以将原有的NVMe SSD盘换成基于持久内存的本地盘，提升IOPS和带宽、降低延时，解决性能瓶颈。

**重要**

持久内存中数据的可靠性取决于物理服务器和持久内存设备的可靠性，因此存在单点故障风险。建议您在应用层做好数据冗余，将需要长期保存的业务数据存储到云盘上，以保证应用数据的可靠性。

## 将持久内存配置为一块本地盘
本文示例中使用的配置如下：

* 实例规格：ecs.re6p.2xlarge

* 镜像：Alibaba Cloud Linux 2.1903 LTS 64位

1. 登录已创建的ECS实例。

   具体操作，请参见[使用Workbench工具以SSH协议登录Linux实例](https://help.aliyun.com/document_detail/147650.html)。
2. 分别执行以下命令，安装持久内存管理工具并清理namespace和label配置。

   ```
   HELPCODEESCAPE-shell
   sudo yum install -y ndctl daxctl
   sudo ndctl disable-namespace all && sudo ndctl destroy-namespace all #清理namespace
   sudo ndctl disable-region all && sudo ndctl zero-labels all && sudo ndctl enable-region all #清理label配置
   ```

3. 查看持久内存大小。

   ```
   HELPCODEESCAPE-shell
   ndctl list -R
   ```

   如下图所示，size值即为持久内存大小。

   ![查询持久内存大小](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5699449761/p607605.png)
4. 将使用模式配置为fsdax。

   ```
   HELPCODEESCAPE-shell
   sudo ndctl create-namespace --reconfig=namespace0.0 -m fsdax --size={region-size} --force
   ```

   **说明**

   {region-size}请替换成上一步查询的size值。

   ![11.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3526360071/p740415.png)
5. 分别执行以下命令，格式化并挂载磁盘。

   ```
   HELPCODEESCAPE-shell
   sudo mkfs -t ext4 /dev/pmem0
   sudo mkdir /mnt/sdb
   sudo mount -o dax,noatime /dev/pmem0 /mnt/sdb
   ```

6. 查看已挂载的磁盘。

   ```
   HELPCODEESCAPE-shell
   df -h
   ```

   ![pmem-as-ssd](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2850549761/p179010.png)

   挂载完成后，您可以使用磁盘性能测试工具测试磁盘性能。

   关于如何在i4p/re6p实例中测试本地盘性能，请参见[测试i4p实例本地盘性能](#f2279652e4llf)。

## 测试i4p实例本地盘性能
本文示例中使用的配置如下：

* 实例规格：ecs.i4p.2xlarge

* 镜像：Alibaba Cloud Linux 2.1903 LTS 64位

* 测试工具：fio，[FIO](https://linux.die.net/man/1/fio)（Flexible I/O Tester）是一个开源的、强大的I/O性能测试工具，可以用来对存储设备进行随机读写、顺序读写等负载测试。

1. 直接使用FIO压测会导致数据丢失。因此在测试本地盘性能前，请确保不要将含有数据的本地盘作为测试对象。

2. 在测试本地盘性能前，请确保已经对测试对象进行数据备份。具体操作，请参见[备份本地盘文件](https://help.aliyun.com/document_detail/2837735.html)。

3. 远程连接ECS实例。

   具体操作，请参见[使用Workbench工具以SSH协议登录Linux实例](https://help.aliyun.com/document_detail/147650.html)。
4. 运行以下命令，安装测试工具FIO。

   ```
   HELPCODEESCAPE-shell
   sudo yum install -y ndctl daxctl ipmctl libpmem librpmem libpmemblk libpmemlog libpmemobj libpmempool pmempool fio
   ```

5. 测试本地盘性能。

   * 测试命令示例，请参见[测试IOPS](#section-bt4-a5w-hjf)，[测试吞吐量](#section-tm5-phs-8u1)，[测试访问时延](#section-0oi-wwa-0h8)。

     **重要**

     如果连续测试，请在每次测试后执行`sudo rm /mnt/sdb/* -rf`命令清理本地盘上一轮遗留的测试结果，以便为下一轮测试准备干净的环境。
   * 基于持久内存的本地盘与本地NVMe SSD盘、ESSD云盘的性能对比如下表所示。

     **说明**

     表中列出的性能级别供您参考，单次测试的具体结果请以您自行测试时的结果为准。
     <table> <thead> <tr> <td><p><b>指标</b></p></td> <td><p><b>持久内存（容量128 GiB）</b></p></td> <td><p><b>NVMe SSD（容量1788 GiB）</b></p></td> <td><p><b>ESSD云盘（容量800 GiB，性能级别PL1）</b></p></td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td><p>读带宽</p></td> <td><p>8\~10 GByte/s级别</p></td> <td><p>2\~3 GByte/s级别</p></td> <td><p>0.2\~0.3 GByte/s级别</p></td> </tr> <tr> <td><p>读写带宽</p></td> <td><p>8～10 GByte/s级别</p></td> <td><p>1\~2 GByte/s级别</p></td> <td><p>0.2\~0.3 GByte/s级别</p></td> </tr> <tr> <td><p>写带宽</p></td> <td><p>2\~3 GByte/s级别</p></td> <td><p>1～2 GByte/s级别</p></td> <td><p>0.2\~0.3 GByte/s级别</p></td> </tr> <tr> <td><p>读IOPS</p></td> <td><p>100万级别</p></td> <td><p>50万级别</p></td> <td><p>2\~3万级别</p></td> </tr> <tr> <td><p>读写IOPS</p></td> <td><p>100万级别</p></td> <td><p>30万级别</p></td> <td><p>2\~3万级别</p></td> </tr> <tr> <td><p>写IOPS</p></td> <td><p>100万级别</p></td> <td><p>30万级别</p></td> <td><p>2\~3万级别</p></td> </tr> <tr> <td><p>读延时</p></td> <td><p>300\~400纳秒级别</p></td> <td><p>100000纳秒级别</p></td> <td><p>250000纳秒级别</p></td> </tr> <tr> <td><p>写延时</p></td> <td><p>300\~400纳秒级别</p></td> <td><p>20000纳秒级别</p></td> <td><p>150000纳秒级别</p></td> </tr> </tbody> </table>

### 测试IOPS

* 顺序读

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=8 --numjobs=8 --iodepth=1 --rw=read --bs=4k --size=8GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

* 顺序写

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=8 --numjobs=8 --iodepth=1 --rw=write --bs=4k --size=1GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

* 随机读

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=8 --numjobs=8 --iodepth=1 --rw=randread --bs=4k --size=8GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

* 随机写

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=8 --numjobs=8 --iodepth=1 --rw=randwrite --bs=4k --size=1GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

### 测试吞吐量

* 顺序读

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=8 --numjobs=96 --iodepth=1 --rw=read --bs=64k --size=1GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

* 顺序写

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=1 --numjobs=8 --iodepth=1 --rw=write --bs=64k --size=1GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

* 随机读

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=8 --numjobs=96 --iodepth=1 --rw=randread --bs=64k --size=1GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

* 随机写

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=8 --numjobs=96 --iodepth=1 --rw=randwrite --bs=64k --size=1GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

### 测试访问时延

* 顺序读

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=1 --numjobs=1 --iodepth=1 --rw=read --bs=4k --size=8GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

* 顺序写

  ```
  HELPCODEESCAPE-shell
  sudo fio --name=test --directory=/mnt/sdb --ioengine=libpmem --direct=1 --thread=1 --numjobs=1 --iodepth=1 --rw=write --bs=4k --size=8GB --norandommap=1 --randrepeat=0 --invalidate=1 --iodepth_batch=1 --sync=1 --scramble_buffers=0 --numa_cpu_nodes=0 --numa_mem_policy=bind:0 --cpus_allowed_policy=split
  ```

## 使用llpl库分配内存池失败
### 问题现象

可以配置为本地盘的ECS持久内存型实例（ecs.re7p规格和ecs.i4p规格）使用llpl库分配内存池失败，提示`Failed to create heap. Cannot read unsafe shutdown count**`错误信息。![问题现象](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7088532661/p485844.png)

### 可能原因

llpl源码默认启用`unsafe shutdown detection`，而非易失性存储器NVM虚拟化后不支持启用，导致问题出现。更多信息，请参见[llpl](https://github.com/pmem/llpl)。

### 解决方案

在llpl源码中关闭`unsafe shutdown detection`，操作步骤如下：

1. 在llpl源码的src/main/cpp/com_intel_pmem_llpl_AnyHeap.cpp文件中添加如下代码。

   ```
   HELPCODEESCAPE-shell
   int sds_write_value=0;
   pmemobj_ctl_set(NULL,"sds.at_create",&sds_write_value)
   ```

   代码添加完毕后，结果如下图所示。

   ![AnyHeap](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6088532661/p485852.png)
2. 登录ECS实例。

   具体操作，请参见[使用Workbench工具以SSH协议登录Linux实例](https://help.aliyun.com/document_detail/147650.html)。
3. 执行如下命令，使用llpl库运行测试用例。

   ```
   HELPCODEESCAPE-shell
   mvn clean && mvn test -Dtest.heap.path=/mnt/sdb
   ```

   如果未出现该错误提示，表示您可以继续分配内存池。
