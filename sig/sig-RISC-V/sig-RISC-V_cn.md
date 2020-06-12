
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


 ### News

 _9 Jun 2020_ 大部分src-openEuler 主线代码支持RISC-V；增加自动化制作openEuler-RISC-V rootfs image 工具；
 增加[最小系统包范围定义](https://gitee.com/whoisxxx/autobuild-openeuler4riscv/blob/master/assets/Core_openEuler-20.03-LTS.list)；
 使能rv64g 编码工具链进行第二轮bootstrap 构建

 _18 may 2020_ stage1 阶段第一轮构建完成，通过[这里](https://isrc.iscas.ac.cn/mirror/openeuler-sig-riscv/)访问；建立openEuler4riscv[自动化构建工具仓](https://gitee.com/openeuler/autobuild-openeuler4riscv/commits/master)

 _28 Apr 2020_ The [OpenEuler SIG](https://gitee.com/openeuler/community/tree/master/sig/sig-RISC-V) set up.

 ### 该SIG管理的repository及描述
- 当前项目RISC-V 所包含的软件包 总数：896
  
  尽管大部分软件包已经支持RISC-V架构或者与底层架构无关从而能够运行在RISC-V架构上，但是仍有一些软件包的社区主线版本并不明确支持RISC-V，例如 valgrind，docker 等。
  这里我们的策略是：

  - 对于社区版本能够支持RISC-V的软件包，我们会配合openEuler的版本策略，在gitee 的[src-openEuler](https://gitee.com/src-openeuler)仓升级、合入补丁以支持RISC-V；
  - 部分软件包需要对spec文件进行修改以适配RISC-V架构的rpm包构建；
  - 对于那些社区主线仍然未支持RISC-V架构的软件包，我们会根据需求选择一些软件包，对RISC-V的支持上做出尝试，**也欢迎感兴趣的你加入进来，我们一起努力**；对于未提及的软件包，尚无明确的支持计划。

- 涉及到修改的软件包 总数：19

  - 社区主线支持，需要升级、合入补丁的软件包：


  | 软件包名称    | 状态   | 详情  | 链接  |
  | ------------ | ----- | --------- | ---- | 
  | LinuxKernel   |  待新开分支<br>5.5?<br>| 1. 4.19支持不完善<br>2. kernel仓开一分支，未来收编<br>3. defconfig 暂时使用arch/riscv/config默认<br>4. 暂时只使用源码仓不使用构建仓 | https://gitee.com/openeuler/kernel/issues/I1JE44#note_2639660                                     |
  | gcc           |  待新开分支            | 1.  默认使用 rv64g 编码 <br> 2.  应用工具链的二进制进行自举构建 <br> 3. 代码开源节奏仍在讨论中                                                                  | 已单点讨论，尚未在社区讨论                                                                        |
  | glibc         | 2.28-> 2.31 ?                | 1. glibc 期望升级，现有2.28 需要大量回合工作                                                                                                           | 已单点讨论，尚未在社区讨论                                                                        |
  | gdb           |                            | 同上                                                                                                                                                   | 同上                                                                                              |
  | libseccomp    | 待升级 <br> 2.4.1->2.4.3 <br>       | 1. libseccomp 2.4.3 为2020.03发布，尚未包含RISC-V支持；<br> 2. master分支已包含支持；<br>3. 需要升级并回合补丁 | 已单点讨论，issue跟踪<br>https://gitee.com/src-openeuler/libseccomp/issues/I1JEGY?from=project-issue |
  | grub2         | 待升级 <br> 2.02->2.04 <br> 暑期任务 | 1. grub2 从2.04 之后支持RISC-V <br> 2. 目前启动方式为 openSBI+ flatten Image ，未使用grub引导 <br>3. 已提交暑期任务 为openEuler - RISC-V 添加grub的引导启动方式 | https://gitee.com/openeuler/marketing/issues/I1I1TS                                               |


  - 社区主线不支持RISC-V，我们试图支持：

  | 软件包名称    | 状态   | 详情  | 链接  |
  | ------------ | ----- | --------- | ---- | 
  | golang        | 暑期任务                   | 1. golang 尚未支持RISC-V                                                                                                                               | https://gitee.com/openeuler/marketing/issues/I1IKOI                                               |
  | docker/iSulad | 暑期任务                   | 1. RISC-V上尚没有可用的容器引擎                                                                                                                        | https://gitee.com/openeuler/marketing/issues/I1IKQO                                               |

  - 修改spec文件以适配RISC-V架构的rpm包构建：

  | 软件包名称    | 状态   | 详情  | 链接  |
  | ------------ | ----- | --------- | ---- | 
  | systemd       | PR待合入                   | systemd-243中riscv不支持gnu-EFI启动，需要修改configure；<br> 并且spec文件中打包的过程要根据架构去掉相应的文件    | https://gitee.com/src-openeuler/systemd/pulls/31                                                  |
  | openssh       | PR待合入                   | disable seccomp_filter                                                                                                                              | https://gitee.com/src-openeuler/openssh/pulls/10                                                  |
  | pcre          | PR待合入                   | disable jit                                                                                                                                            | https://gitee.com/src-openeuler/pcre/pulls/6                                                      |
  | pcre2         | PR待合入                   | disable jit                                                                                                                                            | https://gitee.com/src-openeuler/pcre2/pulls/5                                                     |
  | libsecret     | PR待合入                   | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/libsecret/pulls/1                                                 |
  | star          | PR待合入                   | %prep阶段增加riscv配置                                                                                                                                 | https://gitee.com/src-openeuler/star/pulls/3                                                      |
  | python2     | PR待合入                   | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/python2/pulls/16                                                  |
  | diffutils     | PR待合入                   | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/diffutils/pulls/3                                                 |
  | libffi        | PR待合入                   | disable-multi-os-directory                                                                                                                             | https://gitee.com/src-openeuler/libffi/pulls/12                                                   |
  | libtasn1      | 已合入                     | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/libtasn1/pulls/3                                                  |
  | libmodulemd   | 已合入                     | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/libmodulemd/pulls/1                                               |

- 使用src-openEuler 主线的软件包 数量：878
```
  在此不一一列举，请参考openEuler-RISC-V repo，持续扩展中
  
  https://isrc.iscas.ac.cn/mirror/openeuler-sig-riscv/
  
```

 ### 跨领域和面向外部的流程

 由该SIG定义和执行的，且跨领域和面向外部的流程和行动：

 - 非内部流程清单
 - 该SIG拥有的面向整个openEulerSIG的组织指导计划等
