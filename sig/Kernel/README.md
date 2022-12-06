# openEuler kernel

openEuler 是一个开源、免费的Linux发行版，将通过开放的社区形式与全球的开发者共同构建一个开放、多元和架构包容的软件生态体系。同时，openEuler也是一个创新的平台，鼓励任何人在该平台上提出新想法、开拓新思路、实践新方案。
openEuler kernel 是 openEuler 社区维护的 Linux 内核，其源于上游 [Linux Kernel  社区](http://www.kernel.org)，并在此基础上，合入众多高版本新特性、新硬件架构支持、性能优化、可靠性增强等补丁，希望在社区的共同努力下，功能更丰富、质量更稳定、更安全、更可靠，为 openEuler 以及下游OS发行版提供安全、稳定、可靠的内核基座。让openEuler 以及下游OS发行版能更聚焦业务，简化OS版本的构建和维护，减少在内核上的重复投入。

![image-20201013160330489](images/image-20201013160330489.png)

openEuler kernel 的宗旨：

* 源于社区，贡献社区
* 开放、多元和架构包容
* 社区化开发和维护

## Quick Start

### 如何下载，编译和安装内核?

```
git clone git@gitee.com:openeuler/kernel.git
cd kernel
git checkout -b openEuler-1.0-LTS    # 切到需要的分支， 参见“kernel 的分支”
make openeuler_defconfig
make -j64 
make -j64 modules_install
make install
```

### 如何给 openEuler kernel 提补丁?

① 提 issue：https://gitee.com/openeuler/kernel/issues

​     issue 类型根据实际情况填写，可以是缺陷/Bug, 可以是需求/特性。一个BUG或需求可以对应多个补丁。

② 发补丁到邮件列表： kernel@openeuler.org

​     由于存在多个不同的分支，补丁发送时，需要在 patch 标题

③ 参与讨论和Review，也可以在 kernel sig 例会上申报议题进行讨论&决策

④ 修改后发新版本补丁

⑤ Review OK 合入补丁

⑥ 验证

⑦ 验证OK后关闭 issue

**Notes**:

* [如何发送补丁参见这里](https://gitee.com/openeuler/kernel/blob/openEuler-1.0-LTS/README)

## kernel 的分支

- 长期维护分支(OLK: openEuler Long-term support Kernel)：持续维护分支，及时合入社区 stable 补丁，回合高版本特性，为 openEuler 发行版提供内核候选版本。该分支作为 openEuler kernel 的主线，不维护 kabi 兼容性。

| 分支名                 | 类型         | 说明                                             | EOM     |
| ---------------------- | ------------ | ------------------------------------------------ | ------- |
| kernel-4.19(OLK-4.19)  | 长期维护分支 | 基于Linux 4.19 的openEuler kernel 长期维护分支   | 2026.03 |
| kernel-5.5<sup>1</sup> | 短期维护分支 | 仅用于支持 openEuler 20.09 RISC-V 版本，受限使用 | 2021.03 |
| OLK-5.10               | 长期维护分支 | 基于Linux 5.10 的openEuler kernel 长期维护分支   | 2028.03 |

- openEuler 版本分支：选取某个OLK子版本，用于openEuler发行版，维护周期与对应的openEuler版本相同，发布之后以安全稳定为主，补丁合入须有明确的需求，以合入CVE和Bugfix为主。
- openEuler LTS 的SP版本：年度SP版本，一般选最近的OLK版本子版本，该版本一般包含最近的社区更新，包含较新的特性和优化。

| 分支                          | 维护人         | 发布时间   | EOM 时间            | 状态     |
| ----------------------------- | -------------- | ---------- | ------------------- | -------- |
| openEuler-1.0                 | Yang Yingliang | 2020-01-14 | 2020-03             | 停止维护 |
| openEuler-1.0-LTS<sup>2</sup> | Yang Yingliang | 2020-03-12 | 2024-03<sup>3</sup> | 维护中   |
| openEuler-20.09               | Yang Yingliang | 2020-09-30 | 2021-03             | 维护中   |
| openEuler-21.03               |                |            |                     | TBD.     |

```
Notes:
  1 仅用于支持openEuler 20.09 RISC-V 版本，受限使用，请不要用于生产环境。
  2 由于历史原因 kernel 的分支名与 openEuler 发行版本命名不一致。但为保持源码仓库的持久一致性，这里不做修改，仅做说明。
  3 LTS 版本的维护时间包含了SP版本的维护时间。
```

* 上游/upstream

| 分支名 | 类型         | 说明         | 状态   |
| ------ | ------------ | ------------ | ------ |
| master | 上游开发主线 | 上游开发主线 | 跟踪中 |

* 所有合入openEuler LTS 发行版的特性、新开发、以及bugfix的补丁，都首先合入长期维护分支 （当前是 kernel-4.19)
* 然后根据需要，合入对应的维护分支 （openEuler-* 等分支）

![](images/image-20201015225233915.png)

(草图/示意图，具体日程/生命周期/版本名称以 https://openeuler.org 公布为准)

### 创新版本和稳定版本（LTS）

openEuler 发行版分为创新版本和稳定版本（也说长期维护版本，或简称 LTS)。相应的openEuler内核也分为创新版本和稳定版本。

* 创新版本：提供新技术验证的平台，加速技术成熟和应用。
* 稳定版本：成熟、稳定、可靠，为众多OS发行版提供底座

|          | **创新版本**                     | **稳定版本（LTS）**                        |
| -------- | -------------------------------- | ------------------------------------------ |
| 目的     | 新技术验证；为稳定版本做技术储备 | 质量与稳定优先                             |
| 版本选型 | 上游较新的  LTS 版本             | 稳定版本维护时间较长，可能版本比较老       |
| 维护周期 | 较短，一般不超过1年              | 较长，社区目前暂定4年                      |
| 维护内容 | 严重的安全漏洞和Bugfix           | 优化、增强、硬件支持、安全漏洞、Bugfix  等 |
| 质量目标 | 功能可用, 不要用于生产环境       | 兼顾安全、稳定、可靠                       |
| 维护补丁 | 较少                             | 较多                                       |
| KABI     | 不维护                           | 维护白名单                                 |

### 关于长期维护版本（openEuler Long-term support Kernel）

在openEuler社区中，每隔几年， kernel sig 会选取一个上游社区的 LTS 内核作为openEuler社区长期维护的内核版本，至少维护4年（具体以openEuler社区正式公布为准）。openEuler 的LTS发行版所使用的内核都会基于openEuler kernel 的长期维护版本（简称 OLK), openEuler Longterm support Kernel)，部分创新版本也会使用 OLK。 

当前 openEuler Long-term support Kernel 版本是 4.19，该版本至少维护到2024年3月份。下一个 OLK 版本预计是 5.10，预计openEuler 21.03、21.09、22.09 三个创新版本和openEuler 22.03 LTS 都会使用该版本。

（该章节所说的版本周期或日程用于描述openEuler kernel 的生命周期思路，具体以openEuler正式发布为准）

除了上述所说的长期维护版本，openEuler 社区还会有一些短周期的维护版本，这些版本主要用于新技术验证或体验，比如当前的 5.5, 是短期维护版本，用来支持 risc-v 的开发和验证，后续会升级到 5.10，之后 5.5 便不再维护。未来可能会有部分openEuler的创新版本使用短期维护版本，用来体验或验证新技术。

### 哪些补丁可以合入 openEuler Longterm Support kernel

* 问题修复或安全漏洞修复
* 性能优化的特性
* 主线回合的 Bugfix、优化或有用的特性
* 可靠性、安全性、可维护性增强的补丁、特性
* 新架构支持或增强
* 新设备

### 开发者可以做哪些事情

- 使用和测试 openEuler kernel，包括
  - 搭建 CI 测试环境，帮助 openEuler 测试
  - 每日构建测试
  - 预发布版本的测试
  - 专项测试等
- 搭建测试环境，能在不同设备上进行测试
- fix 社区 issue 以及解答相关疑问和问题, 参见 https://gitee.com/openeuler/kernel/issues
- 完善 kernel 相关文档，提交 PR, https://gitee.com/openeuler/community/tree/master/sig/Kernel
- 承担重点模块的维护和 bugfix
  - 如果想承担某个模块、子系统、或驱动的维护，最简单的方法是可以直接发补丁
  - 可以发邮件到 kernel@openeuler.org 报 kernel sig 例会的议题，说明维护思路
  - kernel sig 达成一致后，可以更新到下面 committer 列表中

| 模块名 | 模块说明                                                    | 文件路径                                                     |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------ |
| arm64  | arm64 架构                                                  | arch/arm64/*                                                 |
| x86    | x86 架构                                                    | arch/x86/*                                                   |
| smmu   | System MMU (SMMU)                                           | drivers/iommu/*                                              |
| kernel | kernel core                                                 | kernel/*                                                     |
| mm     | memory managerment                                          | mm/*                                                         |
| ixgbe  | Intel ethernet drivers                                      | drivers/net/ethernet/intel/<br/>drivers/net/ethernet/intel/*/<br/>include/linux/avf/virtchnl.h |
| nvme   | NVM Express device driver                                   | drivers/nvme/host/*                                          |
| xfs    | XFS filesystem                                              | fs/xfs/*                                                     |
| tipc   | The Transparent Inter Process Communication (TIPC) protocol | net/tipc/*                                                   |

### 在哪里给内核报 bug ?

在[这里](https://gitee.com/openeuler/kernel/issues)

### 内核版本的维护周期?

参见[openEuler的生命周期](http://blog.openeuler.org/post/wangxun/openeuler-lifecycle/)

## Kernel Features

### 架构支持

* 支持 Intel x86 series
* 支持鲲鹏 920，支持 ARM v8 通用特性

* 支持海光CPU-Hygon Dhyana
  * 海光的Peng Wu向openEuler贡献了Hygon CPU的支持补丁集，通过这个补丁集，新增了Hygon CPU 的ACPI, cppufreq，perf，KVM，NTB以及Hygon CPU的识别等支持，通过这个补丁集，openEuler完整支持海光x86 CPU。
* 支持昇腾芯片
  * 包括CPU和AI CPU共享虚拟地址的SVM（shared vitual memory）特性，以及芯片的硬件支持。

* 支持鲲鹏PC平台
  * 鲲鹏PC CPU基于鲲鹏920,8核。20.09版本内核加入了对PC的休眠支持（架构特性），以及I2C控制器等支持。

### 调测特性增强

- 支持内核热补丁（ARM64）

  支持ARM64内核热补丁，可以不用重启内核修复内核 BUG。

- ARM64 kdump 增强

  Arm64 Linux 主线，kdump只支持在4G以下预留内存，存在如下问题：如果在4G以下没有足够的可用连续系统内存，则会导致kdump预留内存失败, kdump服务启动失败; 如果kdump在4G以上预留内存，第一个内核启动时，内存虽然可以预留成功，kdump服务可以正常启动, 但是，kdump在第二个内核启动过程中会失败，这是因为，第二个内核在启动过程中可能需要一些低端内存(dma、swiotlb)，从而导致kdump第二个内核启动失败。

  openEuler 内核支持对4G以上内存的预留。该特性正在[推Linux社区主线](https://lkml.org/lkml/2019/12/23/411)。

- ARM64 NMI Watchdog 支持
  - 支持基于 PMU (Performance Monitoring Unit)  的 NMI Watchdog
  - 支持基于 SDEI (Software Delegated Exception Interface) 的 NMI Watchdog

- ARM64 RAS 增强
  - 支持 ARM v8.2 RAS 扩展
  - 支持执行路径上内存ECC错误恢复

- 支持 SAS 盘暴力热插拔
- 支持 Statistical Profiling Extension 解析增强

  通过解析 SPE 事件，支持精确跟踪和记录 branch miss，LL cache miss，tlb miss等事件，增强perf调优功能。

  * 如何使能 SPE?

    openEuler 20.03 LTS arm64 版本支持 SPE，如果要使用需求确认一下相关配置：

    * 通过启动参数关闭 kpti, kpti=off
    * BIOS 需要支持 PPTT 2.0， 并可以上报 SPE

  * 如何在鲲鹏服务器上使用 perf c2c
    * 确保使能 SPE (参见如何使能 SPE?)
    * 使用 openEuler 的 perf tools

  ```
  perf spe-c2c record -p pid
  perf spe-c2c report
  ```


### 系统性能优化

- 系统扩展性（Scale Out）

  - Numa Aware Qspinlock
    对现有的qspinlock做增强，将锁的等待队列分成两个，本地NUMA节点等待队列和远程NUMA节点等待队列，本地NUMA节点等待队列的线程有限获取锁，减少跨NUMA节点的Cache/总线冲突，从而提升性能.

- MMU gather,  减少TLB flush，从而提升性能

- IO 性能优化

  ARM64服务上，IO性能的瓶颈主要在SMMU开启后，在IOVA页表查找、IOVA释放页表时的TLBi以及SYNC操作耗时导致的性能下降，因此在IOMMU子系统做了多个优化来提升性能.  通过优化 IOVA 页表查找算法，和优化页表释放
  - 支持SMMU的non-strict mode

    每次unmap时并不立即释放IOVA，而是延迟释放，每个页分别执行一次无效TLB操作改为集中执行一次无效TLB_ALL操作，之后再释放各个IOVA。

  - 减少关键结构体的cache false sharing，提升性能

  - 优化IOVA查找效率

- CRC32 和 checksum 加速

  根据 ARM64 指令以及流水线特点，优化 CRC32 及 checksum 实现，大幅提升数据校验性能。

- sched Task Steal

  回合社区的Task Steal特性，通过提升CPU利用率，替身MySQL数据库mix场景的性能10%+；

* REFCOUNT_FULL以及CMPXCHG_LOOP()优化

  通过atomic_fetch_*操作来降低cmpxchg()带来的性能开销，从而提升refcount机制性能，带来文件读写等场景的性能提升，在ARM64服务器上尤其明显，空文件读写的benchmark 20+提升。

* percpu refcount for pagecache

  pagecache的生命周期管理是通过refcount来管理的，在多核并发压力下，读取文件cache的atomic操作成为瓶颈，因此引入percpu refcount mechanism来提升性能，针对nginx http测试，性能有1倍+的提升。

* ARM64 clear_page()性能优化

  通过‘stnp’代替'dc zva'指令，提升clear_page()的性能，在鲲鹏920上，针对hugetlb测试，有53%的性能提升。

* 调度，优化关键进程的抢占时延，提升响应速度

  对 SCHED_IDLE 策略的优化，之前选核的时候只选择 idle 的CPU，现在是如果那个CPU上运行的是SCHED_IDLE 的进程，也可以选择到，由于运行SCHED_IDLE进程的CPU并不是idle，没有唤醒时延，能提升响应速度。

### 资源管控

- Cache与内存带宽的分配与监控

   支持 ARM v8.4 MPAM（Memory System Resource Partitioning and Monitoring）特性。

  * 如何使能 MPAM?
    * 在内核启动参数中增加 mpam, 即在openEuler内核使能了 [MPAM](./mpam.md) 驱动
    * [鲲鹏 920 服务器上如何使用和测试 mpam](./mpam.md)

  * 注意事项：
    * 确认 BIOS 版本已使能 MPAM：如果 BIOS 没有使能的话，只 kernel 使能，会导致系统 crash
    * 下个版本会改进该问题：以 BIOS 上报 MPAM 表格为准，如果上报 MPAM 表格，则 kernel 可以使能 MPAM，否则即使设定了 mpam 启动参数，也不使能 MPAM 驱动。（当前OS与BIOS尚没有标准接口，openEuler先通过此方式来规避。）

  * MPAM 当前的开发状态?
    * openEuler kernel 当前支持鲲鹏 920 的 2P 服务器，后续 kernel 版本计划支持1P、4P等不同规格的服务器；
    * [主线版本的 MPAM 驱动正在开发中](http://www.linux-arm.org/git?p=linux-jm.git;a=summary)；
    * 主线版本的 MPAM 驱动在鲲鹏服务器上的验证和适配正在进行，近期会将适配过的分支提交到 openEuler 社区，供感兴趣的团队测试和试用；

  * openEuler 使能和完善 MPAM 应用生态的思路?
    * 使能鲲鹏芯片 MPAM
    * 完善配套工具
    * 推动和协助 MPAM 在实际场景应用
    * 根据应用场景的诉求改进 MPAM
    * 探索 MPAM 的新场景
    * 通过更多的应用和测试，推动 MPAM驱动进入上游内核社区

- 内存热添加,支持动态添加虚拟内存。
- CPU热插拔, 支持限制 page cache 占用内存的比例。
- 支持限制 page cache 占用内存的比例，避免系统因Page Cache 过多而影响业务的性能或者 OOM。
- 支持 Cgroup file limit，通过cgroup限制打开文件数目。

### 支持鲲鹏处理器相关的驱动：

- 支持 HiSilicon SAS 驱动
- 支持 HNS 和 HNS3 板载网卡
- 支持 hinic 智能网卡

### 新介质以及新驱动支持

* ARM64支持persistence memory
  * ARMv8.2引入新的指令支持persistent memory，鲲鹏920处理器完整支持该特性，通过打开内核的ACPI NFIT以及libnvdimm的配置文件，就能在鲲鹏上完美支持NVDIMM介质内存。

* 华为1822网卡支持ax86架构

* 3408/3416 RAID卡规避
  * 3408iMR/3416iMRraid卡在ARM64平台上（ARM64生态问题）使用存在问题，开启SMMU后，会存在不兼容，通过SMMU 设备bypass特性，规避不兼容问题。
* Huawei BMA驱动, 与BMC通信的驱动支持

### 存储/IO特性支持

* bcache稳定性提升
  * bcache Maintainer Coly回合了大量bcache的bugfix以及特性，大幅提升bcache稳定性和可用性
* RAID 卡支持64K内存页
  * Linux Kernel 软RAID模块，最小空间管理单元以PAGE_SIZE来管理，在4K RAID5 随机模型测试下，相对正常读写数据，数据最大放大16倍，占用大量磁盘带宽，对SSD寿命也造成很大影响。

### 虚拟化特性增强

- 中断虚拟化优化：IRQfd路径注入中断优化，大幅提升高性能直通设备（网卡、SSD磁盘等）性能
- 内存虚拟化优化：借助鲲鹏硬件特性，提升虚拟机启动内存加载速度
- 存储虚拟化优化：iSCSI模块kworker的NUMA亲和性自绑定优化，提升IPSAN磁盘的IO性能
- 支持双层调度：双层调度就是让Hypervisor的调度器感知到VM的VCPU上跑什么应用。让VM的调度器感知到Hypervisor层物理CPU压力。两层调度感知，整机达到最好的业务性能。
- 支持 PMU nmi watchdog
- 支持 Smart Poll

### 安全特性

* CPU安全
  * Special Register Buffer Data Sampling (SRBDS) mitigation
  * ARM64在ERET后加SB，防止可能的侧信道攻击

* 支持AppArmor。
  
* AppArmor相比Selinux使用起来简单，但之前版本未开启AppArmor支持。20.09版本支持AppArmor，但默认的安全策略依然是Selinux，需要在启动参数传入security=apparmor使能
  
* IMA摘要列表增强
  * 相比内核社区原生 IMA 机制，IMA 摘要列表扩展从安全性、性能、易用性三个方面进行了改良，助力完整性保护机制在生产场景下落地，并具有三大优势：

  * 极致安全

    原生 IMA 机制要求在现网环境下预先生成并标记文件扩展属性，访问文件时将文件扩展属性作为参考 值，信任链不完整。摘要列表扩展将文件参考摘要值保存在内核空间中，构建阶段通过摘要列表的形式携带在发布的 rpm 包中，安装 rpm 包的同时导入摘要列表并执行验签，确保了参考值来自于软件发行商，实现了完整的信任链。 

  * 惊艳的性能表现

    IMA 度量场景下，摘要列表扩展在确保安全性的前提下，减少了不必要的 PCR 扩展操作，开启度量时 性能损失小于 5%，相比原生 IMA 度量性能提升高达 50%。
    IMA 评估场景下，摘要列表扩展将签名验证统一移动到启动阶段进行，避免每次访问文件时都执行验 签，相比原生 IMA 评估场景提升运行阶段文件访问的性能约 20%。

  * 快速部署，平滑升级 
    原生 IMA 机制在初次部署或每次更新软件包时，需要切换到 ﬁx 模式手动标记文件扩展属性后再重启进 入 enforce 模式，才能正常访问安装的程序。 摘要列表扩展可实现安装完成后开箱即用，且允许直接在 enforce 模式下安装或升级 rpm 包，无需重 启和手动标记即可使用，实现了用户感知最小化，适合现网环境下快速批量部署

## 组织会议

- 公开的会议时间：北京时间，双周上午，10:00 - 12:00

## 成员

###  Maintainer列表

openeuler/kernel
- 成坚 @gatieme
- 谢秀奇 @xiexiuqi
- 杨颖梁 @yangyingliang

openeuler/kbuild-standalone
- WangNan @pi3orama

openeuler/TCP_option_address
- jiaofenfang @jiaoff

### Committer列表

参见 [openEuler kernel Committer List](committers.md)

## 联系方式

- 邮件列表：[kernel@openeuler.org](mailto:kernel@openeuler.org)

## 项目清单

项目名称：

repository地址：
- https://gitee.com/openeuler/kernel
- https://gitee.com/src-openeuler/kernel
- https://gitee.com/openeuler/kconfigDetector
- https://gitee.com/src-openeuler/kconfigDetector
