## 背景
MPAM 特性是 ARM v8.4 引入的 Cache QoS, 和 内存带宽 QoS 特性. 目前业界与之最接近的是 intel 的 RDT 特性。
Intel RDT 在 Linux 内核中的使用接口是 resctrl。这是一个基于 kernfs 实现的操作接口。为支持 MPAM 特性, 我们
的目标也是实现类似 intel rdt 的 resctrl 用户接口。

社区当前还没有ARM64 resctrl 接口的实现(arm公司在做, 还没有发开源社区)。

## Quick Start

Hi620 CS 2P 为例, 其基本情况:
* 共2P, 4 DIE, 32 clusters, 128 cores, 或 24 clusters, 96 cores
* 每个 cluster 对应一个 L3T (L3 Cache Tag)
* 每个 L3T 可以单独配置
* L3TALL 可以广播配置, 即 L3TALL 可以看做是整 DIE 的配置接口, 即配置 L3TALL, 相当于同时配置 L3T0 ~ L3T7

MPAM 的基本数据
* Cache 共有 15 个 way
* 内存带宽的限制的最小粒度是 1/64

### linux kernel 使能 mpam 特性
openEuler 中 mpam 是 preview 特性, 当前版本暂不支持商用, 默认没有使能。
如果想在1620 CS 2P 板子上验证 mpam 特性, 需要在启动参数中加 mpam 使能。
由于 BIOS 没有通过 ACPI 上报 mpam 资源, 现在版本中 mapm 地址映射信息是
写死的, 只支持 1620 2P. 如果在 1P 上使能, 内核会启动失败; 如果在3P或4P上使能,
预期内核能启动成功, mpam 则只能识别其中2P。

openEuler 上使能 mpam, 需要在 /boot/grub2/grub.cfg 或 /boot/efi/EFI/openEuler/grub.cfg
中添加 mpam 启动参数.

### 挂载 resctrl
系统启动后, 需要手动 mount resctrl 才能使用。
```
mount -t resctrl resctrl /sys/fs/resctrl
cd /sys/fs/resctrl
```

### 配置和使用资源组
#### 为 L3 Cache 的 PARTID 1 分配 4 个 Cache way
```
# 每个目录表示对于的 L3T
cd /sys/fs/resctrl

# 先选择某个 PARTID, 在为其设定 mask, mask 就是对应的 cache way
# 这里选 partid=1, mask=f, 即为 partid 1 分了 0-3  计4条way (共15条way)
mkdir p1
cd p1
echo "L3:0=f;1=f;2=f;3=f" > schemata
cat schemata        # 查看设置情况
cd ..               # 返回上次目录

# 更多的例子
# partid = 2, N0 (way 5,6), N1 (way 5-8), N2 (way 5,6), N3 (way 5-15)
# mask 16进制 
mkdir p2
cd p2
echo "L3:0=30;1=f0;2=30;3=f0" > schemata
cat schemata        # 查看设置情况
cd ..               # 返回上次目录
```

说明: Cache 和 内存带宽的 partid 数量不同, 但是 resctrl 接口当前又是Cache和partid同时操作的, 所以当前实现时已最小的为准

#### 为 Cache/memory bandwidth 设置 monitor, 并观察期使用情况
由于 monitor 数量较少, 所以在创建分组的时候没有默认开启, 需要手动开启。
```
# p1 分组已存在, 开启 monitor
echo 1 > /sys/fs/resctrl/p1/ctrlmon
# 观察该组资源的使用情况
# L3 Cache 的单位是 Bytes, 表明当前 Cache 被占用这么多;
# Memory Bandwidth 单位是MB/s (架构要求的是 MB/s, 1620 看具体实现)
grep . /sys/fs/resctrl/p1/mon_data/*
```

#### 为进程/线程分配分组(让进程/线程只使用某个 part 的资源)
```
# task 19 将使用 partid 1 限定的资源 (pmg 在监控的时候用, pmg 和 partid 都匹配, 才进行统计监控使用情况)
# 将 task 19 move 到 p1 资源组中
# 新创建的子进程, 将继承父进程的 partid 和 pmg 信息
# move 进程时, 已创建的子进程不影响
echo 19 > /sys/fs/resctrl/p1/tasks

# 设置当前 shell 使用那个组的Cache资源 ($$ 表示当前 shell 的 PID)
echo $$ > /sys/fs/resctrl/p1/tasks

# 查看 task 的设置情况
cat /sys/fs/resctrl/p1/tasks
```

#### 为 cpu 分配分组(让指定的 cpu 只使用某个 part 的资源) 
即, 该 cpu 上发出的所有请求都是要改资源组限定的资源(cache, memory bandwidth)
```
# task 1 将使用 partid 2 限定的资源 (pmg 在监控的时候用, pmg 和 partid 都匹配, 才进行统计监控使用情况)
# 将 cpu 1 move 到 p2 资源组中
echo 1 > /sys/fs/resctrl/p2/cpus_list

# 查看 task 的设置情况
cat /sys/fs/resctrl/p2/cpus                   # 掩码方式显示
cat /sys/fs/resctrl/p2/cpus_list              # 列表方式显示
```

### 内存带宽资源划分
HHA 的设置和 L3T 类似, 每个 DIE 有两个HHA, 分别是 HHA0 和 HHA1; HHAALL 表示同时设置和读取两个 HHA;

#### 为 PART 1 设置内存带宽的上限
```
# PART 1, 最多使用约 50% 的带宽;
# 0,1,2,3 分别表示 4 个 numa node, 即 4 个 DIE.
# 带宽按照百分比进行设置, 最小粒度是 5% 对齐.
echo "MB:0=50;1=50;2=50;3=50" > /sys/fs/resctrl/p1/schemata
```
说明:配置 HHAALL 就相当于同时配置了 HHA0 和 HHA1

## 更多的例子
### 划分 L3 Cache, 使用 lat_mem_rd 测试时延的完整例子
步骤:
* 挂载 resctrl
* cache 资源划分
* 设置 monitor
* 起测试程序 (假设 lat_mem_rd 程序在 /root 目录下面, 其他随便什么程序都一样)

```
# 挂载 resctrl
mount -t resctrl resctrl /sys/fs/resctrl
cd /sys/fs/resctrl

# 使用 part 1, 为其分配 4 个way (4 个 node 采用相同的设置)
# partid=1, mask=f
mkdir p1
echo "L3:0=f;1=f;2=f;3=f" > schemata

# 使用 monitor 1 来监控 part 1 的 cache 使用情况
# monitor=1, pmg=1, partid=1
echo 1 > p1/ctrlmon

# 设置当前 shell 进程使用 partid 1 (task 使用哪个 part, 在子进程创建时会继承父进程的)
# 两个 $$ 代表当前 shell 的pid
echo $$ > p1/tasks

# 在后台跑测试程序, 测试结果记录到 result.log 中
cd /root
/root/lat_mem_rd -P 1 -N 1 512M 64 > result.log 2 > &1 &

# lat_mem_rd 测试完成后查看结果.
```

如果想再测 8 way 的情况, 则只需改 CPBM 的 mask 即可:
```
echo "L3:0=ff;1=ff;2=ff;3=ff" > schemata
```

测试过程中如果想观察每个 L3T Cache 的使用情况
```
grep . /sys/fs/resctrl/p1/mon_data/L3*
```

### 限制内存带宽的例子
步骤:

* 挂载 resctrl
* 限制资源划分
* 设置 monitor
* 起测试程序
```
mount -t resctrl resctrl /sys/fs/resctrl
cd /sys/fs/resctrl

# 0/100 表示不限制
# 其他数值表示最大带宽设置的百分比(硬件限制的粒度是 1/64, 软件上近似对应成百分比, 最小按5%对齐)。
mkdir p1
echo "MB:0=30;1=30;2=30;3=30" > p1/schemata
echo 1 > p1/ctrlmon

# 设置当前 shell 进程使用 partid 1 (task 使用哪个 part, 在子进程创建时会继承父进程的)
# 两个 $$ 代表当前 shell 的pid
echo $$ > /sys/fs/resctrl/p1/tasks
# 在后台跑测试程序, 测试结果记录到 result.log 中
cd /root
/root/bw_mem -P 1 -N 1 512M rd > result.log 2 > &1 &

# 观察monitor情况
cd /sys/fs/resctrl
# monitor=1
grep . /sys/fs/resctrl/p1/mon_data/MB*
```