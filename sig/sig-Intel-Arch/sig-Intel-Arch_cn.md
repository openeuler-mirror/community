
# 新建SIG申请
[English](./sig-Intel-Arch.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## SIG组工作目标和范围

### 工作目标

- openEuler对Intel新的硬件能力和平台的支持。

- 加速Intel平台相关的软件栈的支持和优化方案在openEuler上的落地。

- 协调和尽量匹配Intel平台硬件和openEuler发布线路图。

- 促进openEuler的内核、虚拟化、工具链、基础库、SDK工具及用户案例在Intel平台上的创新演进。

- 反馈openEuler的用户需求从而促进Intel平台的创新和对openEuler进一步的支持。

### 工作范围

- 联合内核、虚拟化、工具链、基础库和SDK工具集等重点SIG/开发组，完成上游代码到openEuler版本间的移植工作和创新性项目的落地。

- 促进非上游代码的上游化过程。

- 支持Intel各类软件栈在openEuler上的落地，比如各类加速器、AI框架、orchestration、安全可信栈等。

- 联合Compatibility、CICD等SIG组，增强openEuler在各类硬件平台上的兼容性测试过程。

- 联合Release等SIG组，建立openEuler版本发布的Intel硬件支持目标。

- 促进CPU/芯片组/整机厂商与openEuler社区的技术交流。

- 响应用户反馈和解决问题。

## 交付物

- 源代码

- 工具集

- 文档

## 该SIG管理的repository及描述

- 代码
  - [Intel-kernel](https://gitee.com/openeuler/Intel-kernel): Intel arch支持相关的内核代码开发仓库。会以合适的节奏将代码推送到openEuler kernel主仓库。

  - [Intel-gcc](https://gitee.com/openeuler/Intel-gcc): Intel arch支持相关的gcc代码开发仓库。会以合适的节奏将代码推送到openEuler gcc主仓库。

  - [Intel-glibc](https://gitee.com/openeuler/Intel-glibc): Intel arch支持相关的glibc代码开发仓库。会以合适的节奏将代码推送到openEuler gcc主仓库。

  - [Intel-qemu](https://gitee.com/openeuler/intel-qemu): Intel arch支持相关的Qemu代码开发仓库。会以合适的节奏将代码推送到openEuler Qemu主仓库。

  - [Intel-lkvs](https://gitee.com/openeuler/intel-lkvs): Intel arch支持相关的lkvs代码开发仓库。

  - [Intel-ice](https://gitee.com/openeuler/intel-ice): Intel E810 以太网卡驱动程序。

  - [Intel-iavf](https://gitee.com/openeuler/intel-iavf): Intel E810 以太网卡 Virtual Function 驱动程序。


- 文档
  - [Intel-Arch-doc](https://gitee.com/openeuler/Intel-Arch-doc): 关于openEuler的Intel arch支持相关的文档，如现状、规划、目标等等。
