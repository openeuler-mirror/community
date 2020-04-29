
# openEuler RISC-V 兴趣组
[English](./sig-template.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## SIG组工作目标和范围

用描述新申请SIG计划工作的范围和目标，包括但不限于：

 - 编译构建openEuler的RISC-V运行版本

 - 搭建openEuler源码包的RISC-V交叉编译环境，并构建封装交叉编译环境的QEMU/KVM虚拟机镜像

 - 开发维护openEuler的RISC-V版本构建流程脚本

 - SRPM支持RISC-V的补丁维护，并提交PR到openEuler维护相应源码包的sig组仓库

 - 迭代方式构建: 先构建openEuler面向RISC-V的最小可运行版本（约120多个包），然后在社区共同努力下增加支持openEuler大部分包的编译构建（初步估计约2000多个，并会持续跟踪必要的包及时纳入RISC-V版本）

 - 及时响应用户反馈，解决相关问题

 ### 该SIG管理的repository及描述

- 项目名称：
  - 交付件形式：交叉编译环境的脚本、交叉编译环境镜像（QEMU/KVM虚拟机镜像）、openEuler的RISC-V版本构建流程脚本、支持RISC-V的SRPM源码包补丁、说明文档


 ### 跨领域和面向外部的流程

 由该SIG定义和执行的，且跨领域和面向外部的流程和行动：

 - 非内部流程清单
 - 该SIG拥有的面向整个openEulerSIG的组织指导计划等
