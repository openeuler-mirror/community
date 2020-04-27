## 如何给 openEuler kernel 提补丁?

[参见这里](https://gitee.com/openeuler/kernel/blob/openEuler-1.0-LTS/README)

## 如何下载，编译和安装内核?

```
git clone git@gitee.com:openeuler/kernel.git
cd kernel
git checkout -b openEuler-1.0-LTS    # 切到需要的分支
make openeuler_defconfig
make -j64 
make -j64 modules_install
make install
```

## 在哪里给内核报 bug ?

点[这里](https://gitee.com/openeuler/kernel/issues)

## 内核版本的维护周期?

参见[openEuler的生命周期](http://blog.openeuler.org/post/wangxun/openeuler-lifecycle/)

## 如何使能 SPE?

openEuler 20.03 LTS arm64 版本支持 SPE，如果要使用需求确认一下相关配置：
- 通过启动参数关闭 kpti, kpti=off
- BIOS 需要支持 PPTT 2.0， 并可以上报 SPE

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
