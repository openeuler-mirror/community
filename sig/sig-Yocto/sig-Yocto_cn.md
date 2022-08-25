
# Yocto SIG

说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## Yocto SIG组工作目标和范围

### 工作目标

本SIG致力于开发和维护广泛应用于嵌入式系统的构建系统Yocto,  使得openeuler的相关成果能够延申到嵌入式领域。
由于嵌入式系统应用受到多个因素的约束，如资源、功耗、多样性等，使得面向服务器领域的Linux及相应的构建系统很难满足相应的要求，而Yocto提供模板、工具和方法帮助开发者创建定制的Linux系统和嵌入式产品，而无需关心硬件体系。同时Yocto不限于Linux的定制化的构建，也可以用于其他嵌入式软件如实时操作系统的构建.

### 工作范围

 - Yocto核心组件的维护和开发：poky, pesudo, opkg-utils

 - 面向嵌入式领域，基于Yocto的openeuler定制化构建，包括Linux内核和软件包

 - 基于yocto的扩展，包括模板、工具和方法等

 ### 该SIG管理的repository及描述

- 项目名称：Yocto
  - 交付件形式：源码、tar包或兼而有之
  - Yocto核心组件：
    - poky: https://gitee.com/openeuler/yocto-poky
    - pseudo: https://gitee.com/src-openeuler/yocto-pseudo
    - opkg-utils: https://gitee.com/src-openeuler/yocto-opkg-utils
  - 核心开发工具：
    - yocto-embedded-tools: https://gitee.com/openeuler/yocto-embedded-tools
  - 构建模板和方法:
    - yocto-meta-openeuler: https://gitee.com/openeuler/yocto-meta-openeuler
