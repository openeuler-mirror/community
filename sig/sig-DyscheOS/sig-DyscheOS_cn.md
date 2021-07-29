
# DyscheOS SIG
[English](./sig-DyscheOS.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## SIG组工作目标和范围

宏内核众核可扩展性受到限制，而微内核性能无法满足预期，未来操作系统向什么方向发展仍未可知。

未来计算机系统的形态可能是大量小型计算节点组成的集群，也可能是单个性能怪兽划分成更小的运行实体，或是异构计算场景，CPU在系统中承担更少的计算任务，由智能硬件进行处理。面对这些硬件趋势，操作系统要如何演进？学术界正在探索这些课题，其中有一些非常颠覆性的设计（如来自ETH Zurich的Barrelfish），也有基于现有系统的微创新（如Popcorn linux）。

### 工作目标

我们希望能够利用现有的成熟系统，通过一定的技术方案，在众核异构的大型系统上提供一种可动态伸缩的异构操作系统（DYnamic SCalable HEterogeneous Operating System） - DyscheOS

### 工作范围

- 硬件资源的灵活划分
- 部署多OS的能力，基于划分好的资源部署运行任意OS或baremetal程序
- 多OS间资源隔离，OS独立运行，相互隔离
- OS之间的高效通信，通过共享内存和中断提供一套跨OS的高性能通信机制
- 共有资源的有限共享，系统中存在一些不可划分的特殊设备，需要能够实现此类设备在各OS间的共享
- 多OS协同，借鉴distributed OS相关技术，实现大型业务在多OS之间的高效协同工作

### 交付件
- 源码
- 脚本
- 安装部署指导

## SIG基本信息

### 项目简介

https://gitee.com/openeuler/community/tree/master/sig/sig-DyscheOS/

### Maintainers
- liliang_euler
- minknov
- TrueAI
- hw-chuang

### Committers

### 邮件列表
- dev@openeuler.org

### IRC频道
- #openeuler-dev

### 对外联络人
- minknov
