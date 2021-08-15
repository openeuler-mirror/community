# openEuler RISC-V 兴趣组

[English](./sig-RISC-V.md) | 简体中文

RISC-V 是一个免费开源的指令集（ISA）。RISC-V SIG 组旨在提供 openEuler_RISC-V 版本，并且提供 openEuler_RISC-V 的软件包构建、系统构建等指导，使对 RISC-V 感兴趣的开发者能够参与到开源系统开发中活动中来。

要获取更多信息，RISC-V相关的主仓在这里：

- [openEuler/RISC-V](https://gitee.com/openeuler/RISC-V)

其中有关于openEuler RISC-V移植版的获取、使用文档，并且欢迎参与共同建设openEuler RISC-V移植版的构建。

说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## 组织会议

- 公开的会议时间：每双周一次，周四上午 10:00 - 10:30 。
- 加入方式请联系 Maintainer 。

## 成员

### Maintainer 列表

- Wei Wu [@wuwei_plct](https://gitee.com/wuwei_plct), wuwei2016@iscas.ac.cn
- Xuzhou Zhang [@whoisxxx](https://gitee.com/whoisxxx), zhangxuzhou4@huawei.com
- liqingqing_1229 [@liqingqing_1229](https://gitee.com/liqingqing_1229)
- Junqiang Wang [@wangjunqiangs](https://gitee.com/wangjunqiangs), wangjunqiang@iscas.ac.cn
- Jing Xi [@xijing666](https://gitee.com/xijing666), xijing@nj.iscas.ac.cn
- 黎亮 [@liliang_euler](https://gitee.com/liliang_euler), liliang889@huawei.com

### Committer 列表

- Wei Wu [@wuwei_plct](https://gitee.com/wuwei_plct), wuwei2016@iscas.ac.cn
- Xuzhou Zhang [@whoisxxx](https://gitee.com/whoisxxx), zhangxuzhou4@huawei.com
- Qingqing Li [@liqingqing_1229](https://gitee.com/liqingqing_1229)
- Junqiang Wang [@wangjunqiangs](https://gitee.com/wangjunqiangs), wangjunqiang@iscas.ac.cn
- Jing Xi [@xijing666](https://gitee.com/xijing666), xijing@nj.iscas.ac.cn

## 联系方式

- [邮件列表，目前共用openEuler dev列表](dev@openeuler.org)
- 视频会议
- 微信：加入RISC -V sig的微信群，一起进行讨论，欢迎分享你的想法

<img src="./sig-RISC-V-WeChatGroup.jpg" width="30%" height="30%">

## 项目清单

项目名称：

源码repository地址：

- https://gitee.com/openeuler/RISC-V   RISC-V主仓，包含文档、工具和RISC-V工程配置
- https://gitee.com/src-openeuler/opensbi  openSBI是“Open Source Supervisor Binary Interface”用于引导RISC-V系统的启动
- https://gitee.com/src-openeuler/risc-v-kernel 用于openEuler RISC-V的kernel-5.5 Image 
- https://gitee.com/src-openeuler/NutShell-riscv-pk 支持openEuler面向NutShell(果壳, UCAS)处理器bootloader,内核镜像,DST构建.
- https://gitee.com/src-openeuler/NutShell-Kernel 支持openEuler面向NutShell(果壳, UCAS)处理器的内核源码、驱动、.config内核配置项等.
- https://gitee.com/src-openeuler/NutShell-systemd 支持openEuler OS在NutShell UCAS COOSCA CPU运行，ttyPS0，udev等，处理器仿真环境为Xilinx FPGA PYNQ-Z2.
- https://gitee.com/src-openeuler/NutShell-riscv-glibc 工具链的riscv glibc库，用于编译构建面向NutShell UCAS COOSCA处理器openEuler OS组件.
- https://gitee.com/src-openeuler/firesim    FireSim is an open-source cycle-accurate FPGA-accelerated full-system hardware simulation platform that runs on cloud FPGAs.

RPM Repo和Image地址：

- https://isrc.iscas.ac.cn/mirror/openeuler-sig-riscv/oe-RISCV-repo 面向RISC-V的RPM二进制包、SRPM源码包, 并提供软件包安装更新的repo服务.
- https://isrc.iscas.ac.cn/mirror/openeuler-sig-riscv/images/ 根文件系统rootfs、虚拟磁盘镜像、内核、openSBI、BBL等二进制镜像材料.

硬件平台支持:

- https://isrc.iscas.ac.cn/mirror/openeuler-sig-riscv/images/NutShellUCAS/ 移植支持NutShell(果壳, UCAS) RISC-V处理器支持的镜像资源.
