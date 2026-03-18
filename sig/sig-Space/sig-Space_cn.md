
# 新建SIG申请
[English](./sig-Space.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## SIG组工作目标和范围

SIG-Space面向航天、低空全域空间智能场景，致力于基于openEuler构建高可靠、强实时、智能化的全场景协同空间计算开源生态，覆盖航天（卫星星座、深空探测）与低空（无人机、eVTOL）领域。

 - 为什么需要在openEuler里创建一个这样的新SIG：商业航天与低空经济的爆发性增长，对统一、开源的空间计算操作系统基座提出了迫切需求。当前空间星载/机载软件多为垂直封闭体系，硬件绑定深，生态碎片化严重，阻碍了快速创新。

 - 该SIG的业务范围：空间级操作系统基线定义、高可靠系统加固（单粒子翻转防护、抗瞬时掉电）、实时内核优化（PREEMPT_RT、混合关键性）、异构硬件平台抽象层与BSP、嵌入式AI使能、空间协议中间件（CCSDS、DDS）。

 - 该SIG需要得到openEuler内哪些SIG的支持：Embedded SIG（硬件抽象协作）、AI SIG（推理框架优化协同）、Kernel SIG（实时内核补丁）。


 ### 该SIG管理的repository及描述

- 项目名称：TODO（待确定）
  - 交付件形式：源码、tar包或兼而有之


 ### 跨领域和面向外部的流程

 由该SIG定义和执行的，且跨领域和面向外部的流程和行动：

 - 向上游社区贡献：Linux内核、U-Boot、AI框架
 - 与Embedded SIG紧密合作硬件抽象
 - 与AI SIG协同优化推理框架
 - 产学研用联合：高校与研究机构参与前沿探索，商业公司贡献场景需求与适配
