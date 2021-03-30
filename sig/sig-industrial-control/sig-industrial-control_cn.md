
# 新建SIG申请
[English](./sig-industrial-control.md) | 简体中文

说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

Industrial Control SIG组主要致力于将openEuler打造成适用于工业控制领域或嵌入式领域的实时操作系统。

## Industrial-Control SIG组工作目标和范围

### 工作目标
 国外实时操作系统如RTAI、RTLinux、Xenomai等系统已经发展多年，而国内相关的实时操作系统社区却较为落后，为提高实时操作系统的社区活跃度，并面向国内工业控制等相关领域，我们希望参与openEuler社区，以openEuler社区为基石进行实时系统的研究，以应用于工业控制相关领域或嵌入式领域。
 
 本SIG组将会把强实时Xenomai方案引入openEuler社区中，并对常见的工业控制现场总线进行迁移、适配和优化，将openEuler打造成可以应用于工业控制领域的操作系统。
 
 另一方面，随着硬件技术的发展，实时特性的硬件虚拟化也将会成为未来发展方向，本SIG组将致力于实时虚拟化方向的研究，让常见的RTOS，如Zephyr、RTEMS、FreeRTOS等系统可同时与openEuler运行在同一平台上，满足某几个核心运行实时任务，其他核心运行通用任务的新型工业控制相关领域的需求。
 
### 工作范围
 - 制定Xenomai实时方案相关软件包的版本生命周期
 - 对常见开源工业控制现场总线，如Modbus、CANopen、EtherCAT等进行迁移、适配和优化
 - 移植实时相关或适用于工业控制领域的虚拟化方案
 - 移植RTOS系统，如Zephyr
 - 复用embedded SIG组成果，为嵌入式系统提供实时方案
 - 回馈上游社区
 - 及时响应用户反馈，解决相关问题
 - 引入其他工业控制相关特性及新技术

### 交付物
 - 源码和tar包

### 该SIG管理的repository及描述
  - https://gitee.com/openeuler/xenomai
  - https://gitee.com/src-openeuler/xenomai
  - https://gitee.com/src-openeuler/ipipe
  - https://gitee.com/src-openeuler/linux-stable-rt
  - https://gitee.com/src-openeuler/rt-setup
  - https://gitee.com/src-openeuler/rt-tests
  - https://gitee.com/src-openeuler/rt-check
  - https://gitee.com/src-openeuler/rt-ctl
  - https://gitee.com/src-openeuler/rteval
  - https://gitee.com/src-openeuler/rteval-loads
  - https://gitee.com/src-openeuler/tuned
  - https://gitee.com/src-openeuler/libmodbus
  - https://gitee.com/src-openeuler/soem
  - https://gitee.com/src-openeuler/soes
  - https://gitee.com/src-openeuler/canopennode
  - https://gitee.com/src-openeuler/igh-ethercat-xenomai
  - https://gitee.com/src-openeuler/libmodbus-xenomai
  - https://gitee.com/src-openeuler/canfestival-xenomai

 
### 跨领域和面向外部的流程
 暂无
