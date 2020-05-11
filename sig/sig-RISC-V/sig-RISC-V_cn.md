
# openEuler RISC-V 兴趣组
[English](./sig-template.md) | 简体中文

RISC-V 是一个免费开源的指令集（ISA）。RISC-V SIG 组旨在提供 openEuler_RISC-V 版本，并且提供 openEuler_RISC-V 的软件包构建、系统构建等指导，使对 RISC-V 感兴趣的开发者能够参与到开源系统开发中活动中来。

说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## RISC-V SIG组工作目标和范围

工作目标：

 - 构建 openEuler 支持 RISC-V 架构（包括模拟器和硬件平台）

 - 源代码在 gitee 上开源，保持 openEuler_RISC-V 源码与 openEuler 主线保持一致，定期推送/回合 RISC-V 补丁到openEuler主线；
 
 - 提供可直接获取的 openEuler_RISC-V 的 rpm repo 以及 系统镜像

 - 提供用于构建 openEuler_RISC-V 系统的工具

 - 提供友好的文档用于指导构建与定制 openEuler_RISC-V 

 - 维护 openEuler_RISC-V 每日构建工程以及测试验证系统，提供自动化构建服务

 - 相应用户反馈，解决相应问题

 - 根据 RISC-V 指令集特点引入软件包，推动 openEuler 软件包数量扩容

 工作范围：

 - 制定 RISC-V SIG 组的工作流程、软件包规划、路线图等
 
 - 利用 openEuler 开源代码构建 openEuler_RISC-V 版本、

 - 识别 RISC-V 相关的补丁和修改，保持源码与 openEuler 主线保持一致

 - 制作用于半自动构建的工具 

 - 维护 openEuler_RISC-V 相关的文档、会议、邮件列表、IRC管理

 - 维护托管 openEuler_RISC-V 的 repo


 交付件：

 - RPM repo 源，openEuler_RISC-V 系统镜像，构建手册，自动化构建服务

 ### 该SIG管理的repository及描述
此处列出来的包为已构建成功的 RISC-V 版本软件包
这里的软件包版本策略为：
```
 1. 优先使用 openEuler 主线代码
 2. 若需要修改，RISC-V 补丁 合入 openEuler 主线，完成合入之前在个人仓
 3. 若版本不同，代码在个人仓托管，在引入时需要指定：
    a. 版本策略（回合/升级/不回合）
    b. 制定 回合/升级 的deadline ，在 deadline 之前需要进入状态2 
```

- 项目名称：RISC-V

  - 构建工具和 RISC-V 文档
    - https://gitee.com/openeuler/autobuild-openeuler4riscv
    - https://gitee.com/openeuler/RISC-V-wiki

```
  └── openEuler
     ├── autobuild-openeuler4riscv
     │   └── mk-rootfs
     └── RISC-V-wiki
         ├── core-list
         ├── custom.md
         └── run-RISC-V.md
```

  - openEuler 主线代码
    - https://gitee.com/src-openeuler/audit
    - https://gitee.com/src-openeuler/gawk

  - 尚未合入 openEuler 主线的代码
    - https://gitee.com/zhoupeng01/libffi 
    - https://gitee.com/whoisxxx/systemd 
    
    - https://gitee.com/zhoupeng01/linux-5.4 
    - https://gitee.com/whoisxxx/openSBI-Image

  - 外部引入的软件包 
    - gcc-8.2.1  
    - glibc-2.29.9000
    - gdb-8.3.1 


 ### 跨领域和面向外部的流程

 由该SIG定义和执行的，且跨领域和面向外部的流程和行动：

 - 非内部流程清单
 - 该SIG拥有的面向整个openEulerSIG的组织指导计划等
