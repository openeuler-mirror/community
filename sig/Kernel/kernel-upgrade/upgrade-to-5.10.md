## openEuler 选择 5.10 作为下一个长期维护的内核版本 (公示)

Linux 5.10 预计是 Linux 社区今年的 LTS (long-term support) 版本。openEuler 社区经过多轮沟通，选择 5.10 作为 openEuler 内核的下一个长期维护版本（openEuler Long-term support Kernel, OLK）。openEuler 社区提供不少于4年的维护时间和不少于2年的扩展维护时间。按照规划 openEuler 21.03、21.09 以及 openEuler 22.03 LTS 都将选择该内核版本。 （具体时间以openEuler社区官网公布为准）

### 升级安排：
* v5.10-rc1 版本发布后，openEuler master 分支切换成 5.10。
* 由于主线 rc 版本尚在更新，openeuler_defconfig 暂时在 src-openeuler/kernel 仓库中提供，待 5.10 正式版本发布之后，再提交到源码仓库。
* openeuler_defconfig 基于 openEuler 20.09 的 config 修改适配，后续根据需求进行调整。
* 版本号格式，切换成 5.10.0-<devel_release>.<maintainence_release>。
* 首先支持 arm64 和 x86_64 架构，risc-v 的支持需要 risc-v sig 做适配。
* 上游社区 5.10 正式发布后（预计12月下旬）， openeuler/kernel 正式建立 OLK-5.10 分支 （OLK: openEuler Long-term support Kernel），作为 5.10 的长期维护分支，接受补丁。
* 上游 5.10 正式发布前，如果有补丁需要发送 5.10，可以在 kernel@openeuler.org 中发 RFC 补丁，提前 Review 和讨论。
* 我们也可能提前建立 OLK-5.10 分支，以提前合入部分补丁做验证，但是在上游社区 5.10 正式发布之前，该分支可能会经常做 rebase 和 force push。

### 对 OLK-5.10 或 openEuler 21.03 kernel 的需求
* 需求可以在 https://gitee.com/openeuler/kernel/issues 中提出。
* 如对 defconfig 有诉求也请在上述链接中提 issue。
* openEuler 21.03 计划使用该内核版本，预计2021年1月份之后，将从 OLK-5.10 拉出 openEuler-21.03 维护分支，同时补丁将受限合入 openEuler 21.03。

### 注意事项和说明
* OLK 是 openEuler Long-term support Kernel 的缩写。openEuler LTS 版本和部分创新版本的内核基于 OLK 拉出分支进行维护。
* openEuler 5.10 内核不是基于 openEuler 4.19 内核的演进，而是基于上游社区内核的重新选型，因此如果您之前有合入 openEuler 4.19 的补丁，且这些补丁没有进入上游 5.10 内核，则需要您重新适配后推送到 openEuler 5.10 内核。
* openEuler 5.10 和 openEuler 4.19 两个版本 kabi 不兼容，您在 4.19 编译的 ko 不能直接在 5.10 上安装使用，需要重新适配和编译。
* openEuler 4.19 内核仍然处于维护周期内，如果您正在使用 4.19 内核，也不必紧张，您仍然能收到 4.19 的更新和增强。

### 问题反馈
* kernel 升级期间，如果遇到兼容性、功能等问题，可以在 https://gitee.com/openeuler/kernel/issues 提交 issue。有疑问也可以在 PR 评论中，或者提交 issue 讨论。
* 你也可以发邮件到 kernel@openeuler.org 报议题在 kernel sig 例会中讨论。
* 如果 kernel sig 范围内协调或解决不了的问题，你也可以在 tc 报议题讨论。

## 相关讨论纪要
### kernel-sig 切换 5.10 的会议纪要：

https://mailweb.openeuler.org/hyperkitty/list/kernel@openeuler.org/thread/6XVCHDKO6SOWWNT5S6TV26JURSTC2WOW/?sort=date

### openEuler kernel 版本号在 TC 的议题及会议纪要：

* 议题及讨论记录：

https://mailweb.openeuler.org/hyperkitty/list/tc@openeuler.org/thread/KOHJNCRI376SB6NC5J65MR4JZ3EIIPLU/
https://mailweb.openeuler.org/hyperkitty/list/tc@openeuler.org/thread/VNJQ6E7FBC7EVOFCLERIT6OMYSQS6Y7I/

* 纪要：
https://mailweb.openeuler.org/hyperkitty/list/tc@openeuler.org/thread/ZLAWQE6X2KE7OJ525Q3H33A3X4XAQKB5/