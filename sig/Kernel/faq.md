## 如何给 openEuler kernel 提补丁?

[参见这里](https://gitee.com/openeuler/kernel/blob/openEuler-1.0-LTS/README)

## 如何下载，编译和安装内核?

```
git clone git@gitee.com:openeuler/kernel.git
cd kernel
git checkout -b openEuler-1.0-LTS    # 切到需要的分支， 参见“kernel 的分支”
make openeuler_defconfig
make -j64 
make -j64 modules_install
make install
```

issues: #I1F6G1

## kernel 的分支

- 开发分支：有较多的补丁合入，以及新特性合入，供测试、调试、验证，不作为正式版本发布；
- 维护分支：openEuler 发布后，对应版本的维护分支，补丁及新特性合入较少；

|分支名|类型|说明|状态|
|-----|----|----|----|
|kernel-4.19|开发分支|基于社区 linux 4.19 的开发分支|开发中|
|openEuler-1.0-LTS(*)|维护分支|openEuler 20.03 LTS 的维护分支|维护中|
|openEuler-1.0|维护分支|openEuler-1.0-base 的维护分支|停止维护|
|master|上游开发主线|上游开发主线|跟踪中|

```(*) 由于历史原因 kernel 的分支名与 openEuler 发行版本命名不一致。但为保持源码仓库的持久一致性，这里不做修改，仅做说明。```

## 开发者可以做哪些事情

- 使用和测试 openEuler kernel
- 还没有进社区主线的特性，开发者可以在 Linux 上游社区协助测试、讨论并推动早日合入主线（持续更新中）；

|特性名称|状态|补丁链接|
|-------|----|-------|
|support kdump on memory above 4G|社区讨论中|[补丁链接](https://patchwork.kernel.org/cover/11308463/)|
|perf tools: Add support for some spe events and precise ip|社区讨论中|[补丁链接](https://patchwork.kernel.org/cover/11348573/)|
|[PATCH v10 0/5] Add NUMA-awareness to qspinlock|社区讨论中|[补丁链接](https://lkml.org/lkml/2020/4/3/1022)|
|[v10,00/25] arm64: provide pseudo NMI with GICv3|社区讨论中|[补丁链接](https://patchwork.kernel.org/cover/10790737/)|

- 重点模块的维护和bugfix

|模块名称|模块说明|诉求|
|-------|-------|----|
|arm64|arm64 架构|回合高版本bugfix，性能优化，回合主线新特性|
|x86|x86 架构|回合高版本bugfix，性能优化，回合主线新特性|
|smmu|System MMU (SMMU)|性能优化|
|kernel|kernel core|回合高版本bugfix，性能优化，回合主线新特性|
|nvme|NVM Express device driver|回合高版本bugfix，性能优化，回合主线新特性|
|xfs|XFS filesystem|回合高版本bugfix，性能优化，回合主线新特性|

- fix 社区 issue 以及解答相关疑问和问题

参见 https://gitee.com/openeuler/kernel/issues

## 在哪里给内核报 bug ?

在[这里](https://gitee.com/openeuler/kernel/issues)

## 内核版本的维护周期?

参见[openEuler的生命周期](http://blog.openeuler.org/post/wangxun/openeuler-lifecycle/)

## 如何使能 SPE?

openEuler 20.03 LTS arm64 版本支持 SPE，如果要使用需求确认一下相关配置：
- 通过启动参数关闭 kpti, kpti=off
- BIOS 需要支持 PPTT 2.0， 并可以上报 SPE

## 如何在鲲鹏服务器上使用 perf c2c

- 确保使能 SPE (参见如何使能 SPE?)
- 使用 openEuler 的 perf tools
```
perf spe-c2c record -p pid
perf spe-c2c report
```

## 如何使能 MPAM?

- 在内核启动参数中增加 mpam, 即在openEuler内核使能了 MPAM 驱动

注意事项：
- 确认 BIOS 版本已使能 MPAM：如果 BIOS 没有使能的话，只 kernel 使能，会导致系统 crash
- 下个版本会改进该问题：以 BIOS 上报 MPAM 表格为准，如果上报 MPAM 表格，则 kernel 可以使能 MPAM，否则即使设定了 mpam 启动参数，也不使能 MPAM 驱动。（当前OS与BIOS尚没有标准接口，openEuler先通过此方式来规避。）

## MPAM 当前的开发状态?

- openEuler kernel 当前支持鲲鹏 920 的 2P 服务器，后续 kernel 版本计划支持1P、4P等不同规格的服务器；
- [主线版本的 MPAM 驱动正在开发中](http://www.linux-arm.org/git?p=linux-jm.git;a=summary)；
- 主线版本的 MPAM 驱动在鲲鹏服务器上的验证和适配正在进行，近期会将适配过的分支提交到 openEuler 社区，供感兴趣的团队测试和试用；

## openEuler 使能和完善 MPAM 应用生态的思路?
- 使能鲲鹏芯片 MPAM
- 完善配套工具
- 推动和协助 MPAM 在实际场景应用
- 根据应用场景的诉求改进 MPAM
- 探索 MPAM 的新场景
- 通过更多的应用和测试，推动 MPAM驱动进入上游内核社区

## openEuler kabi 兼容性策略

kabi （kernel abi）