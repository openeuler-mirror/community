# Intel Arch SIG
[English](./README.md) | 简体中文

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

# 成员

### Maintainer列表

- 田俊 [@juntianlinux](https://gitee.com/juntianlinux)，jun.j.tian@intel.com
- 江国庆 [@gjiang](https://gitee.com/gjiang)，guoqing.jiang@suse.com
- 唐葛亮 [@geliangtang](https://gitee.com/geliangtang)，geliang.tang@suse.com
- 杨军 [@junyang-suse](https://gitee.com/junyang-suse)，jun.yang@suse.com
- 毛晨曦 [@chenxi-mao](https://gitee.com/chenxi-mao)，chenxi.mao@suse.com
- Jason Zeng [@x56Jason](https://gitee.com/x56Jason)，jason.zeng@intel.com
- 施爱春 [@allen-shi](https://gitee.com/allen-shi)，aichun.shi@intel.com

# 联系方式

- [邮件列表](mailto:sig-intel-arch@openeuler.org)

# 项目清单

- 代码及软件包
  - [intel-kernel](https://gitee.com/openeuler/Intel-kernel): Intel arch支持相关的内核代码开发仓库。会以合适的节奏将代码推送到openEuler kernel主仓库。

  - [intel-qemu](https://gitee.com/openeuler/intel-qemu): Intel arch支持相关的Qemu代码开发仓库。会以合适的节奏将代码推送到openEuler Qemu主仓库。

  - [intel-lkvs](https://gitee.com/openeuler/intel-lkvs): Intel arch支持相关的Linux Kernel测试集lkvs代码开发仓库。

  - [intel-ice](https://gitee.com/openeuler/intel-ice): Intel E810 以太网卡驱动程序。

  - [intel-iavf](https://gitee.com/openeuler/intel-iavf): Intel E810 以太网卡 Virtual Function 驱动程序。

  - [intel-oneapi](https://gitee.com/openeuler/intel-oneapi): Intel oneAPI在openEuler的仓库入口

  - [accel-config](https://gitee.com/src-openeuler/accel-config): Intel DSA(Data Streaming Accelerator)和IAA(Intel Analytics Accelerator)配置工具库

  - [level-zero](https://gitee.com/src-openeuler/level-zero): Intel oneAPI Level Zero头文件规范及硬件加载程序

  - [intel-gmmlib](https://gitee.com/src-openeuler/intel-gmmlib): Intel图形卡内存管理库

  - [intel-graphics-compiler](https://gitee.com/src-openeuler/intel-graphics-compiler): Intel图形卡编译器

  - [intel-metee](https://gitee.com/src-openeuler/intel-metee): Intel ME TEE库

  - [intel-gsc](https://gitee.com/src-openeuler/intel-gsc): Intel图形卡系统控制器的固件更新库

  - [intel-cm-compiler](https://gitee.com/src-openeuler/intel-cm-compiler): Intel C for Metal编译器

  - [intel-compute-runtime](https://gitee.com/src-openeuler/intel-compute-runtime): Intel图形卡计算运行时程序

  - [intel-qatlib](https://gitee.com/src-openeuler/intel-qatlib): Intel QuickAssist Technology库

- 文档
  - [intel-docs](https://gitee.com/openeuler/intel-docs): 关于openEuler的Intel arch支持相关的文档，如现状、规划、目标等等。
