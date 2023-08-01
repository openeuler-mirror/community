# Porting-platform-winapp 兴趣小组

[English](./sig-porting-platform-winapp.md) | 简体中文

说明：本 SIG 的内容遵循 openEuler 章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## SIG 组工作目标和范围

工作目标：Porting Platform WinApp SIG 负责 openEuler 社区中 Windows 应用在 openEuler 中应用迁移相关的信息交流和配套软件开发工作。

工作范围包括支撑各类型主流应用对 openEuler 的迁移工作，提供迁移工具实现 Windows 应用向openEuler 平台的无缝衔接，进一步拓展 openEuler 的支持范围，为各类型应用提供高性能的基础软件环境。具体如下：

- 移植工具链
  - VS工程转换工具，VS工程转换助手将提供一种精巧便捷的方式，将原本Visual Studio（VS）的工程转换为跨平台的Qt工程。它旨在满足跨平台软件开发的需求，帮助您快速、无缝地迁移VS项目至Qt框架。
  - 提供 windows app 库依赖分析工具，完善  windows app 需要的依赖。
  - 软件包制作，在 Windows 原有app 在 openEuler 打包发布，支持命令行、图形化安装。
- 针对开发框架（如 winform/WPF/nodejs 等）开发的 Windows 应用：
     1）提供一个评估工具，识别当前 linux 不具备的一些特性及能力，识别开发框架在 linux 下的使用限制。
     2）针对当前 linux 下支持上述框架缺失的能力，补齐在 linux 下控件集合。
- Mono 等 .NET Framework 相关软件包的维护

### Repositories and description managed by this SIG

- 项目名称：vs2qt
- 交付件：Source and tar
- 仓库地址：<https://gitee.com/openeuler/vs2qt>
