# Industrial-Control

## 概述
Industrial-Control SIG组主要致力于将openEuler打造成适用于工业控制领域或嵌入式领域的实时操作系统。


## 工作职责
 - 制定Xenomai实时方案相关软件包的版本生命周期
 - 对常见开源工业控制现场总线，如Modbus、CANopen、EtherCAT等进行迁移、适配和优化
 - 移植实时相关或适用于工业控制领域的虚拟化方案
 - 移植RTOS系统，如Zephyr
 - 复用embedded SIG组成果，为嵌入式系统提供实时方案
 - 回馈上游社区
 - 及时响应用户反馈，解决相关问题
 - 引入其他工业控制相关特性及新技术
 - Preempt_RT实时性内核维护
 - Preempt_RT工具集维护
 - 实时性操作系统发布与维护

## 目标
​        本SIG组将会把强实时Xenomai方案引入openEuler社区中，并对常见的工业控制现场总线进行迁移、适配和优化，将openEuler打造成可以应用于工业控制领域的操作系统。

​        另一方面，随着硬件技术的发展，实时特性的硬件虚拟化也将会成为未来发展方向，本SIG组将致力于实时虚拟化方向的研究，让常见的RTOS，如Zephyr、RTEMS、FreeRTOS等系统可同时与openEuler运行在同一平台上，满足某几个核心运行实时任务，其他核心运行通用任务的新型工业控制相关领域的需求。

## ROADMAP

- 2022年12月完成对飞腾嵌入式E2000芯片的适配
- 2023年1月完成Jailhouse引入
- 2023年3月完成openEuler实时性多场景、高负载情况下实时性的提升，并配合2303版本发布
- 2023年3月完成基于openeuler embedded版本新增meta-AMP（meta-Jailhouse）
- 2023年6月完成基于openeuler embedded版本新增meta-FreeRTOS，完成FreeRTOS虚拟化
- 2023年9月基于openEuler内核，完成龙芯或RISC-V平台的Preempt_RT支持
- 2023年9月完成GearOS基于openeuler embedded版本的重构，配合openEuler2309发布
- 2023年10月完成基于Zephyr版本新增meta-Zephyr，完成Zephyr虚拟化
- 2023年12月完成基于openeuler embedded版本新增meta-Industrail（工控协议）
- 2023年12月开始引入国际已有实时相关开源项目

# 组织会议
- 公开的会议时间：北京时间，每双周四下午

# 成员

### Maintainer列表
| Maintainer                                              | 邮箱                     |
| ------------------------------------------------------- | ------------------------ |
| 郭皓[@guohaoc2c2](https://gitee.com/guohaocs2c)         | guohao@kylinos.cn        |
| 吴春光[@wuchunguang](https://gitee.com/wuchunguang)     | wuchunguang@kylinos.cn   |
| 马玉昆[@kylin-mayukun](https://gitee.com/kylin-mayukun) | mayukun@kylinos.cn       |
| 张远航[@zhangyh1992](https://gitee.com/zhangyh1992)     | zhangyuanhang@kylinos.cn |
| 张玉[@zhangyuge001](https://gitee.com/zhangyuge001)     | zhangyu4@kylinos.cn      |
| 李钰磊[@r2018](https://gitee.com/r2018)                 | liyulei@kylinos.cn       |
| 廖元垲[@liao-yuankai](https://gitee.com/liao-yuankai)   | yuankai.liao@cdjrlc.com  |
| 廖茂益[@ixr](https://gitee.com/ixr)                     | liaomaoyi@cdjrlc.com     |
| 王伟[@wangwei622](https://gitee.com/wangwei622)         | wangwei@cdjrlc.com       |
| 黎亮[@liliang_euler](https://gitee.com/liliang_euler)   | liliang889@huawei.com    |
| 张攀[@SuperHugePan](https://gitee.com/SuperHugePan)     | zhangpan26@huawei.com    |

### Committer列表


# 联系方式
- [邮件列表](dev@openeuler.org)
- [IRC频道](#openeuler-dev)
- [IRC公开会议](#openeuler-meeting)

# 项目清单

项目名称：Industrial-Control

repository 地址：

###### GearOS

- https://gitee.com/openeuler/GearOS

###### Preempt_RT

- https://gitee.com/openeuler/Preempt_RT
- https://gitee.com/src-openeuler/kernel
- https://gitee.com/src-openeuler/rtcheck
- https://gitee.com/src-openeuler/rteval
- https://gitee.com/src-openeuler/rt-tests

###### Xenomai

- https://gitee.com/openeuler/xenomai
- https://gitee.com/src-openeuler/Xenomai4
- https://gitee.com/src-openeuler/xenomai
- https://gitee.com/src-openeuler/ipipe
- https://gitee.com/src-openeuler/canfestival-xenomai
- https://gitee.com/src-openeuler/canfestival
- https://gitee.com/src-openeuler/igh-ethercat-xenomai
- https://gitee.com/src-openeuler/ethercat-igh
- https://gitee.com/src-openeuler/libmodbus-xenomai
- https://gitee.com/src-openeuler/libmodbus
- https://gitee.com/src-openeuler/canopennode
- https://gitee.com/src-openeuler/libnetconf2
- https://gitee.com/src-openeuler/libyang1
- https://gitee.com/src-openeuler/netopeer2
- https://gitee.com/src-openeuler/soem
- https://gitee.com/src-openeuler/soes
- https://gitee.com/src-openeuler/sysrepo

###### Jailhouse

- https://gitee.com/src-openeuler/Jailhouse