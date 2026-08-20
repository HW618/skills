为进一步优化神龙架构GPU服务器的网络性能，阿里云推出了GPU计算型超级计算集群实例规格族，即sccgn系列实例，该系列机型具备了超强的计算能力和网络通信能力。本文为您介绍sccgn系列实例的使用说明及性能验证。  

## 使用说明
sccgn系列机型同时配备了GPU计算卡和Mellanox高性能网卡，具备超强的计算能力和网络通信能力。适用于如深度学习、高性能计算等高强度计算和密集通信兼备的应用场景。使用sccgn系列实例的几点说明：

* 如果您只需使用RDMA功能，在创建sccgn系列实例（例如sccgn7ex实例规格族）的选择镜像阶段，需要选中**安装RDMA软件栈**。

* 如果您的业务需要使用GPUDirect RDMA功能，在创建sccgn系列实例的选择镜像阶段，您需要选中**安装GPU驱动**，来快速安装所需软件栈及工具包。

  **说明**

  GPUDirect RDMA是英伟达自Kepler级别GPU和CUDA 5.0以来引入的一种数据直通技术，其使用PCIe数据总线的标准功能，为GPU和第三方对等设备（例如GPU之间、网络接口、视频采集设备、存储适配器）之间提供直接的数据通路。更多信息，请参见[英伟达官方文档](https://docs.nvidia.com/cuda/gpudirect-rdma/index.html)。
* 如果您实例所安装的网卡驱动为OFED开源版本（[下载地址](https://network.nvidia.com/products/infiniband-drivers/linux/mlnx_ofed/)），您可以在安装网卡驱动后，再安装GPU驱动及CUDA。

  **说明**

  CUDA 11.4和R470之后版本已包含了nvidia_peermem模块，您无需单独安装nv_peer_mem模块。更多信息，请参见[nv_peer_memory](https://github.com/Mellanox/nv_peer_memory)。

## 功能通过性验证及带宽验证
## 功能通过性验证
该验证用于检查sccgn系列实例的RDMA软件栈安装和配置是否正确。

执行以下命令，检验RDMA软件栈的安装情况。  
**说明**

如果在检查过程中遇到一些问题需要解决，请参见[常见问题](#section-s9x-nxt-5kg)。

```
HELPCODEESCAPE-shell
rdma_qos_check -V
```

如果回显类似如下内容，表示RDMA软件栈已正确安装。

```
HELPCODEESCAPE-shell
===========================================================
*    rdma_qos_check
-----------------------------------------------------------
* ITEM          DETAIL                               RESULT
===========================================================
* link_up       eth1: yes                                ok
* mlnx_device   eth1: 1                                  ok
* drv_ver       eth1: 5.2-2.2.3                          ok
...
* pci           0000:c5:00.1                             ok
* pci           0000:e1:00.0                             ok
* pci           0000:e1:00.1                             ok
===========================================================
```

## 带宽验证
该验证用于检查RDMA网络带宽是否符合对应硬件的预期要求。

* 服务器端命令

  ```
  HELPCODEESCAPE-shell
  ib_read_bw -a -q 20 --report_gbits -d mlx5_bond_0
  ```

  类似回显信息如下：

  ```
  HELPCODEESCAPE-shell
  ---------------------------------------------------------------------------------------
                      RDMA_Read BW Test
   Dual-port       : OFF        Device         : mlx5_bond_0
   Number of qps   : 20        Transport type : IB
   Connection type : RC        Using SRQ      : OFF
   PCIe relax order: ON
   ibv_wr* API     : ON
   CQ Moderation   : 100
   Mtu             : 1024[B]
   Link type       : Ethernet
   GID index       : 3
   Outstand reads  : 16
   rdma_cm QPs     : OFF
   Data ex. method : Ethernet
  ---------------------------------------------------------------------------------------
   local address: LID 0000 QPN 0x11ca PSN 0x6302b0 OUT 0x10 RKey 0x17fddc VAddr 0x007f88e1e5d000
   GID: 00:00:00:00:00:00:00:00:00:00:255:255:200:00:46:14
   local address: LID 0000 QPN 0x11cb PSN 0x99aeda OUT 0x10 RKey 0x17fddc VAddr 0x007f88e265d000
   GID: 00:00:00:00:00:00:00:00:00:00:255:255:200:00:46:14
   local address: LID 0000 QPN 0x11cc PSN 0xf0d01c OUT 0x10 RKey 0x17fddc VAddr 0x007f88e2e5d000
   ...
    remote address: LID 0000 QPN 0x11dd PSN 0x8efe92 OUT 0x10 RKey 0x17fddc VAddr 0x007f672004b000
   GID: 00:00:00:00:00:00:00:00:00:00:255:255:200:00:45:14
  ---------------------------------------------------------------------------------------
   #bytes     #iterations    BW peak[Gb/sec]    BW average[Gb/sec]   MsgRate[Mpps]
   8388608    20000            165.65             165.63            0.002468
  ---------------------------------------------------------------------------------------
  ```

* 客户端命令

  ```
  HELPCODEESCAPE-shell
  ib_read_bw -a -q 20 --report_gbits -d mlx5_bond_0 {server_ip}
  ```

  类似回显信息如下：

  ```
  HELPCODEESCAPE-shell
  ---------------------------------------------------------------------------------------
                      RDMA_Read BW Test
   Dual-port       : OFF        Device         : mlx5_bond_0
   Number of qps   : 20        Transport type : IB
   Connection type : RC        Using SRQ      : OFF
   PCIe relax order: ON
   ibv_wr* API     : ON
   TX depth        : 128
   CQ Moderation   : 100
   Mtu             : 1024[B]
   Link type       : Ethernet
   GID index       : 3
   Outstand reads  : 16
   rdma_cm QPs     : OFF
   Data ex. method : Ethernet
  ---------------------------------------------------------------------------------------
   local address: LID 0000 QPN 0x11ca PSN 0x787f05 OUT 0x10 RKey 0x17fddc VAddr 0x007f671684b000
   GID: 00:00:00:00:00:00:00:00:00:00:255:255:200:00:45:14
   local address: LID 0000 QPN 0x11cb PSN 0x467042 OUT 0x10 RKey 0x17fddc VAddr 0x007f671704b000
   GID: 00:00:00:00:00:00:00:00:00:00:255:255:200:00:45:14
   local address: LID 0000 QPN 0x11cc PSN 0xac262e OUT 0x10 RKey 0x17fddc VAddr 0x007f671784b000
   ...
    remote address: LID 0000 QPN 0x11dd PSN 0xeb1c3f OUT 0x10 RKey 0x17fddc VAddr 0x007f88eb65d000
   GID: 00:00:00:00:00:00:00:00:00:00:255:255:200:00:46:14
  ---------------------------------------------------------------------------------------
   #bytes     #iterations    BW peak[Gb/sec]    BW average[Gb/sec]   MsgRate[Mpps]
  Conflicting CPU frequency values detected: 800.000000 != 3177.498000. CPU Frequency is not max.
   2          20000           0.058511            0.058226            3.639132
  Conflicting CPU frequency values detected: 799.996000 != 3384.422000. CPU Frequency is not max.
  ...
  Conflicting CPU frequency values detected: 800.000000 != 3166.731000. CPU Frequency is not max.
   4194304    20000            165.55             165.55            0.004934
  Conflicting CPU frequency values detected: 800.000000 != 2967.226000. CPU Frequency is not max.
   8388608    20000            165.65             165.63            0.002468
  ---------------------------------------------------------------------------------------
  ```

运行以上命令时，可通过`rdma_monitor -s -t -G`命令在ECS控制台观察对应网卡各端口的实际带宽。类似回显信息如下：

```
HELPCODEESCAPE-shell
------
2022-2-18 09:48:59 CST
tx_rate: 81.874 (40.923/40.951)
rx_rate: 0.092 (0.055/0.037)
tx_pause: 0 (0/0)
rx_pause: 0 (0/0)
tx_pause_duration: 0 (0/0)
rx_pause_duration: 0 (0/0)
np_cnp_sent: 0
rp_cnp_handled: 4632
num_of_qp: 22
np_ecn_marked: 0
rp_cnp_ignored: 0
out_of_buffer: 0
out_of_seq: 0
packet_seq_err: 0
tx_rate_prio0: 0.000 (0.000/0.000)
rx_rate_prio0: 0.000 (0.000/0.000)
tcp_segs_retrans: 0
tcp_retrans_rate: 0
cpu_usage: 0.35%
free_mem: 1049633300 kB

------
```

## nccl-tests用例
为测试和验证配备RDMA网络的机型在应用中的实际表现，下文以nccl-tests用例为例，展示如何使用sccgn系列实例的RDMA功能加速您的应用。nccl-tests示例如下：  
**说明**

关于nccl-tests的更多信息，请参见[nccl-tests](https://github.com/NVIDIA/nccl-tests)。

```
HELPCODEESCAPE-shell
#!/bin/sh
# 使用的操作系统为 Alibaba Cloud Linux 2
# 安装openmpi及编译器
yum install -y gcc-c++
wget http://mirrors.cloud.aliyuncs.com/opsx/ecs/linux/binary/rdma/sccgn7ex/Alinux2/openmpi-4.1.3.tar.gz
tar -xzf openmpi-4.1.3.tar.gz
cd openmpi-4.1.3
./configure --prefix=/usr/local/openmpi
make -j && make install


# 修改~/.bashrc
export PATH=/usr/local/cuda/bin:/usr/local/openmpi/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/lib:/usr/local/openmpi/lib:$LD_LIBRARY_PATH

# 下载测试代码并编译
git clone https://github.com/NVIDIA/nccl-tests
cd nccl-tests/
make MPI=1 CUDA_HOME=/usr/local/cuda

# 将 host1, host2 替换为你对应的 IP 地址
mpirun --allow-run-as-root -np 16 -npernode 8 -H {host1}:{host2}  \
  --bind-to none \
  -mca btl_tcp_if_include bond0 \
  -x PATH \
  -x CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
  -x NCCL_SOCKET_IFNAME=bond0 \
  -x NCCL_IB_HCA=mlx5 \
  -x NCCL_IB_DISABLE=0 \
  -x NCCL_DEBUG=INFO \
  -x NCCL_NSOCKS_PERTHREAD=8 \
  -x NCCL_SOCKET_NTHREADS=8 \
  -x NCCL_IB_GID_INDEX=3 \
  -x NCCL_DEBUG_SUBSYS=NET,GRAPH \
  -x NCCL_IB_QPS_PER_CONNECTION=4 \
  ./build/all_reduce_perf -b 4M -e 4M -f 2 -g 1 -t 1 -n 20
```

## 常见问题
### 执行命令`rdma_qos_check -V`时，系统报错：drv_fw_ver eth1: 5.2-2.2.3/22.29.1016 fail

**问题原因**：此报错表示Mellanox网卡固件未更新。

**解决方案**：

* 在Alibaba Cloud Linux 2或CentOS 8.3系统中，执行以下命令刷新服务器网卡固件。

  ```
  HELPCODEESCAPE-shell
  /usr/share/nic-drivers-mellanox-rdma/sources/alifwmanager-22292302 --force --yes
  ```

* 在Debian-based的系统中，下载固件刷新程序，然后执行以下命令来刷新服务器的网卡固件。

  ```
  HELPCODEESCAPE-shell
  wget http://mirrors.cloud.aliyuncs.com/opsx/ecs/linux/binary/rdma/sccgn7ex/Debian10u10/alifwmanager-22312902
  ./alifwmanager-22312902 --force --yes
  ```

### 执行命令`rdma_qos_check -V`时，系统报错：\* roce_ver : 0 fail

**问题原因**：此报错表示缺少configfs、rdma_cm等内核模块。

**解决方案** ：您可以执行`modprobe mlx5_ib && modprobe configfs && modprobe rdma_cm`命令加载对应内核模块。  

### 在Debian系统中，执行命令`systemctl start networking`启动网络服务时，系统提示找不到bond

**问题原因**：此报错可能由于mlx5_ib内核模块未加载。

**解决方案** ：您可以执行`modprobe mlx5_ib`加载此内核模块。  

### 执行命令rdma_qos_check -V或命令ib_read_bw时，系统报错：ERROR: RoCE tos isn't correct on mlx5_bond_3

您可以执行命令`rdma_qos_init`对网络进行初始化。  

### 执行命令rdma_qos_check -V时，系统报错：cm_tos mlx5_bond_1: 0 fail

在Alibaba Cloud Linux 2中，重启服务器后，执行验证命令`rdma_qos_check -V`出现报错时，您可以执行命令`rdma_qos_init`对网络进行初始化。  

### 执行命令rdma_qos_check -V时，系统报错：trust_mod eth1: pcp fail

在CentOS 8.3系统中，重启服务器后，执行验证命令`rdma_qos_check -V`出现报错时，您可以执行命令`rdma_qos_init`对网络进行初始化。  

### RDMA网络接口bond\*出现获取不到bond ip的情况

您可以执行命令`ifdown bond*`和`ifup bond*`获取到bond ip。  
**说明**

请将`*`替换为对应网络接口的序号。
