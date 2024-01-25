# openEuler RISC-V 兴趣组

[English](./sig-RISC-V.md) | 简体中文

RISC-V 是一个免费开源的指令集（ISA）。RISC-V SIG 组旨在提供 openEuler_RISC-V 版本，并且提供 openEuler_RISC-V 的软件包构建、系统构建等指导，使对 RISC-V 感兴趣的开发者能够参与到开源系统开发中活动中来。

要获取更多信息，RISC-V相关的主仓在这里：

- [openEuler/RISC-V](https://gitee.com/openeuler/RISC-V)

其中有关于openEuler RISC-V移植版的获取、使用文档，并且欢迎参与共同建设openEuler RISC-V移植版的构建。

说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## 组织会议

- 公开的会议时间：每双周一次，北京时间周四上午 9:30 - 10:00 以公开线上会议形式讨论sig组议题。会议前一天发起sig组相关议题收集，并发出会议时间和会议链接。

- 具体参会方式：

  - 方式一：openEuler官网（https://www.openeuler.org/zh/ ）查看会议列表；
  - 方式二：加入“openEuler RISC-V SIG 技术交流群”查看会议通知（参考下文添加吴伟老师微信入群）

- 会议纪要链接：https://etherpad.openeuler.org/p/sig-RISC-V-meetings

  

## 成员

### Maintainer 列表

- Wei Wu [@wuwei_plct](https://gitee.com/wuwei_plct), wuwei2016@iscas.ac.cn
- Xuzhou Zhang [@whoisxxx](https://gitee.com/whoisxxx), zhangxuzhou4@huawei.com
- liqingqing_1229 [@liqingqing_1229](https://gitee.com/liqingqing_1229)
- 黎亮 [@liliang_euler](https://gitee.com/liliang_euler), liliang889@huawei.com
- Junqiang Wang [@geasscore](https://gitee.com/geasscore), wangjunqiang@iscas.ac.cn
- Jing Xi [@phoebe-xi](https://gitee.com/phoebe-xi), xijing@iscas.ac.cn
- Yang Wang [@wangyangdahai](https://gitee.com/wangyangdahai)，admin@you2.top
- Kai Zhang [@laokz](https://gitee.com/laokz)，laokz@foxmail.com
- Dong Du [@dongduResearcher](https://gitee.com/dongduResearcher)，Dd_nirvana@sjtu.edu.cn

### Committer 列表

- Wei Wu [@wuwei_plct](https://gitee.com/wuwei_plct), wuwei2016@iscas.ac.cn
- Xuzhou Zhang [@whoisxxx](https://gitee.com/whoisxxx), zhangxuzhou4@huawei.com
- Qingqing Li [@liqingqing_1229](https://gitee.com/liqingqing_1229)
- Junqiang Wang [@geasscore](https://gitee.com/geasscore), wangjunqiang@iscas.ac.cn
- Jing Xi [@phoebe-xi](https://gitee.com/phoebe-xi), xijing@iscas.ac.cn
- Yang Wang [@wangyangdahai](https://gitee.com/wangyangdahai)，admin@you2.top
- Kai Zhang [@laokz](https://gitee.com/laokz)，laokz@foxmail.com
- Dong Du [@dongduResearcher](https://gitee.com/dongduResearcher)，Dd_nirvana@sjtu.edu.cn
- Jiacheng Zhou [@jchzhou](https://gitee.com/jchzhou)
- JingWei Wang [@Jingwiw](https://gitee.com/Jingwiw)
- Xin Liu [@misaka00251](https://gitee.com/misaka00251)
- Xiaoqian Lv [@lvxiaoqian](https://gitee.com/lvxiaoqian)
- Jie Wu [@jean9823](https://gitee.com/jean9823)
- Yunxiang Luo [@yunxiangluo](https://gitee.com/yunxiangluo)
- Fuyuan Zhang [@chuachuaa](https://gitee.com/chuachuaa)

更多commiter详见[RISC-V贡献者列表](https://gitee.com/openeuler/RISC-V/contributors?ref=master)



## 联系方式

- 微信：添加wu wei老师微信（**添加请备注 oerv**），加入RISC -V sig的微信群

<img src="./wuwei.jpg" width="30%" height="30%">

- 邮箱：通过maintainer邮箱联系
- [邮件列表](riscv@openeuler.org)



## 项目清单

项目名称：

源码repository地址：

- https://gitee.com/openeuler/RISC-V   RISC-V主仓，包含文档、工具和RISC-V工程配置
- https://gitee.com/openeuler/riscv-kernel   RISC-V内核开发仓库，目标是支持多种RISC-V硬件平台的同源内核
- https://gitee.com/organizations/openeuler-risc-v/projects openEuler-RISC-V 是专门为openeuler RISC-V sig创建的源码仓，用于管理那些在riscv64架构下构建失败需要修复的软件包
- https://gitee.com/src-openeuler/opensbi  openSBI是“Open Source Supervisor Binary Interface”用于引导RISC-V系统的启动
- https://gitee.com/src-openeuler/risc-v-kernel 用于openEuler RISC-V的kernel Image 
