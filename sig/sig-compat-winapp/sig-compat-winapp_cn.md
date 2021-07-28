
# Compat-winapp SIG

[English](./sig-compat-winapp.md) | 简体中文

说明：本 SIG 的 Charter 内容遵循 openEuler 章程 [README](/zh/governance/README.md) 中描述的约定，使用 [SIG-governance](/zh/technical-committee/governance/SIG-governance.md) 中概述的角色和组织管理。

Compatibility Winapp SIG 组致力于将 X86 平台下海量的 Windows 应用引入 X86/ARM 等架构的 openEuler 系统中，通过提供完善的构建解决方案和指引文档，让更多对此感兴趣的人加入其中。

## SIG组工作目标和范围

### 工作目标

信息产业国产化替代的大潮中，大量 X86 Windows 应用在 Linux 平台没有优秀替代产品但又不可或缺，这不但严重阻碍了用户使用国产化系统的意愿，同时极大的影响了用户的使用体验，在解决这个这个问题的过程中，我们已经使用 Wine 完成了大量 X86 Windows 应用移植兼容，跨硬件平台方面我们也多有研究。为了回馈开源社区，同时秉持众人拾柴火焰高的 openEuler 社区精神，我们希望创建该 SIG 组以 openEuler 社区为基石，携手更多有志于应用兼容方面的朋友共同促进国产系统平台向更加易用的方向发展。

本 SIG 组将会把我们的 Wine 方案引入 openEuler 社区中，同时结合 Qemu/Box86/Exagear 等模拟器技术让 X86 Windows 应用能够运行在更多硬件平台上。

### 工作范围

- 引入 Wine 方案，解决应用适配过程中的各种 bug
- 研究 qemu、box86 等实现跨硬件平台程序解决方案
- 回馈上游社区
- 及时响应用户反馈，解决相关问题

### 交付物

- 源码或 tar 包

### 该 SIG 管理的 repository 及描述

- https://gitee.com/openeuler/compat-winapp
- https://gitee.com/openeuler/wine-app
- https://gitee.com/src-openeuler/wine

### 跨领域和面向外部的流程

暂无
