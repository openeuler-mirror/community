
# 新建SIG申请
[English](./sig-Hygon.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## SIG组工作目标和范围

### 工作目标

- openEuler对Hygon新的硬件能力和平台的支持。

- 加速Hygon平台相关的软件栈的支持和优化方案在openEuler上的落地。

- 协调和尽量匹配Hygon平台硬件和openEuler发布线路图。

- 构建Hygon安全功能的软件生态，包括国密、可信计算、机密计算和虚拟化等。

- 促进openEuler的内核、虚拟化、工具链、基础库、SDK工具及用户案例在Hygon平台上的创新演进。

- 反馈openEuler的用户需求从而促进Hygon平台的创新和对openEuler进一步的支持。

### 工作范围

- 联合内核、虚拟化、工具链、基础库和SDK工具集等重点SIG/开发组，完成上游代码到openEuler版本间的移植工作和创新性项目的落地。

- 促进非上游代码的上游化过程。

- 支持Hygon各类软件栈在openEuler上的落地，比如各类加速器、AI框架、orchestration、安全可信栈等。

- 联合Compatibility、CICD等SIG组，增强openEuler在各类硬件平台上的兼容性测试过程。

- 联合Release等SIG组，建立openEuler版本发布的Hygon硬件支持目标。

- 促进CPU/芯片组/整机厂商与openEuler社区的技术交流。

- 响应用户反馈和解决问题。

## 交付物

- 源代码

- 工具集

- 文档

## 该SIG管理的repository及描述

- 代码
  - [hygon-kernel](https://gitee.com/openeuler/hygon-kernel): Hygon arch支持相关的内核代码开发仓库。会以合适的节奏将代码推送到openEuler kernel主仓库。

  - [hygon-qemu](https://gitee.com/openeuler/hygon-qemu): Hygon arch支持相关的Qemu代码开发仓库。会以合适的节奏将代码推送到openEuler Qemu主仓库。

  - [hygon-edk2](https://gitee.com/openeuler/hygon-edk2): Hygon arch支持相关的Edk2代码开发仓库。

  - [hygon-devkit](https://gitee.com/openeuler/hygon-devkit): Hygon arch支持相关的SDK, 二进制安装包和示例代码存放仓库。
