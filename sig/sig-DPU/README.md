
# DPU SIG

## 背景

### 智能网卡

随着后摩尔定律时代到来，CPU算力增长速度与数据中心网络传输速率增长速度差距逐渐拉大，催生了网卡智能化的需求。CPU计算能力增速低于网路传输速率增速，且差距持续增大，将网络功能卸载到可编程硬件的需求愈发急迫。

 - 25G网卡网络数据包处理需要占用约6个CPU

 - 100G网卡约24个

 - 那么400G呢？

为了应对这一变化，我们应该将网络、存储、操作系统中不适合CPU处理的高性能数据处理功能卸载到硬件芯片执行，提升数据处理效率，释放CPU算力；节省的CPU算力将真正用于客户的服务。

### DPU Vs 智能网卡

 - 实现形式上： DPU包括“通用处理器+可编程硬件”，不只卸载数据面，还包括管理面，是更加全面的卸载

 - 功能上：智能网卡专注可卸载，DPU相比智能网卡增加了可编程性，并可以增加安全加解密、存储等更多硬件功能，提供更高的灵活性

 - 适用场景上：DPU适用于更加通用场景下任务的卸载加速和弹性加速，如容器场景。负载均衡、安全和高级定制化网络

DPU是承载了更多功能及硬件能力的板卡（如安全加解密、存储卸载加速），不仅仅聚焦网络卸载加速，更多的是针对数据的处理。

## DPU定位

当前国内外各厂商都在布局DPU能力，DPU作为一种新型可编程处理器需要集合以下要素：

 - 行业标准的、高性能及软件可编程的多核通用处理器

 - 高性能网络接口，高速处理及数据传输

 - 种类多样的，灵活可编程的加速引擎，可以对AI、机器学习、安全、存储等进行卸载加速

各大厂商对DPU的定位及构想也略有不同：

> 负责在数据中心传输和处理数据的数据处理单元（DPU），正与CPU、GPU共同组成“未来计算的三大支柱” - NVIDIA

> 基础设施处理器（IPU），可加速网络基础设施，释放CPU内核，实现应用程序性能的提升。IPU使云服务提供商能够以软件级的速度定制基础实施部署，同时通过灵活安排工作负载，提高数据中心的利用率 - Intel

> 以数据为中心（Data-Centric），一个以数据为中心的世界需要以数据为中心的基础设施 - Fungible

不管是哪一种定位和构想，DPU都将为未来数据中心的不同应用场景中占据越来越重要的地位。

OS或软件一直都是需要跟随硬件的趋势发展的，新的硬件演进需要新的OS抽象，多样化的DPU硬件也需要专用定制化的OS及上层统一接口来发挥硬件的极致性能，并为开发者提供统一的使用视图。

## 参与厂商

 - NVIDIA

 - 中国电信天翼云

 - 中国移动苏州研发中心

 - 华为

## Sig-DPU目标

Sig-DPU希望能够集结国内外各DPU或smartNIC厂商参与，为客户提供DPU驱动及管理工具，鼓励厂商共同参与制定相关标准。

* Customized OS for DPU

为各DPU硬件提供统一定制化openEuler操作系统支持，提供统一的用户使用体验；探索新型DPU硬件下的高性能操作系统方案，为DPU提供统一的底层接口及能力比如跨DPU和HOST的高速通信通道；也可以针对特定DPU提供定制的特性优化。

* 统一的用户编程框架

针对不同的DPU厂商，探索其加速及卸载能力中的公共部分，面向开发者提供统一的接口抽象；使其能够使用统一的编程接口及框架使用DPU硬件。

* 通用的业务DPU卸载能力

为DPU厂商提供管理面及数据面业务DPU卸载的通用能力支持，降低开发者进行业务DPU卸载的难度。

* 加速方案的标准实现

不同DPU具备不同的硬件加速能力，探索如何通过统一的接口及标准实现，为厂商不同硬件加速能力的实现提供底层支持。

* DPU新型使用方式探索

探索DPU的发展趋势和新型实用方式，比如通过抽象层整合DPU与HOST，提供统一的使用视图；未来数据中心的资源池化方案，各类资源以池化方式存在，通过DPU进行池化管理及访问。

我们希望依托openEuler构建开源开放的DPU生态，使能DPU的OS开箱即用，成为创新孵化平台，能力上提供OS标准生态接口，同时扩展应用的可编程、可定制性，以及提供更好的DPU-OS使用体验。

# 组织会议

- 公开的会议时间： 北京时间，按需

# 成员

# Maintainer列表

- lch-lichunhui[@lch-lichunhui](https://gitee.com/lch-lichunhui)
- lic121[@lic121](https://gitee.com/lic121)
- minknov[@minknov](https://gitee.com/minknov)
- victorzoum[@victorzoum](https://gitee.com/victorzoum)
- C0reFast[@C0reFast](https://gitee.com/C0reFast)
- liuhaic[@liuhaic](https://gitee.com/liuhaic)
- chenanqing1985[@chenanqing1985](https://gitee.com/chenanqing1985)

## Committer列表

- lch-lichunhui[@lch-lichunhui](https://gitee.com/lch-lichunhui)
- lic121[@lic121](https://gitee.com/lic121)
- minknov[@minknov](https://gitee.com/minknov)
- victorzoum[@victorzoum](https://gitee.com/victorzoum)
- C0reFast[@C0reFast](https://gitee.com/C0reFast)
- liuhaic[@liuhaic](https://gitee.com/liuhaic)
- chenanqing1985[@chenanqing1985](https://gitee.com/chenanqing1985)
- ryuxin[@ryuxin](https://gitee.com/ryuxin)
- luochenglcs[@luochenglcs](https://gitee.com/luochenglcs)
- superhugepan[@superhugepan](https://gitee.com/superhugepan)
- louhongxiang[@louhongxiang](https://gitee.com/louhongxiang)
- liusirui[@liusirui](https://gitee.com/liusirui)

# 仓库列表

- [dpu-core](https://gitee.com/openeuler/dpu-core)
- [dpu-utilities](https://gitee.com/openeuler/dpu-utilities)
- [dpu-utilities-pkg](https://gitee.com/src-openeuler/dpu-utilities)

# 联系方式

*<如果需要单独申请邮件列表，请再次补充邮箱名称：sig-yoursigname@openeuler.org>*

- [邮件列表](dev@openeuler.org)
- [IRC频道](#openeuler-dev)
- [IRC公开会议](#openeuler-meeting)
