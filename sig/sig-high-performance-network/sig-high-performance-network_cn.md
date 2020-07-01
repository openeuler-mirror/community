
# 新建SIG申请
[English](./sig-high-performance-network.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## SIG组工作目标和范围

用描述新申请SIG计划工作的范围和目标，包括但不限于：

- Sig-high-performance-network的必要性

- 1. 网络加速技术：DPDK/RDMA/XDP独立于内核协议栈，为上层应用提供了更优于内核协议栈的网络协议栈服务。当前这几类网络加速技术已经被广泛使用在各种应用场景。 
  2. 为了让使用openEuler的厂商、爱好者能够更方便、更准确的使用网络加速技术，openEuler应该维护、开发、优化这几类网络加速技术相关的基础软件包、驱动、语言库软件包、工具软件包、基础服务软件包、应用软件包等。
  3. 通过本sig的持续发展，实现openEuler特色的网络加速技术体系，体现几个特点：易用性、高性能、更好的软件生态。

- Sig-high-performance-network的业务范围

- 1. 维护DPDK/RDMA/XDP相关软件包，包括

  2. - 基础软件包：RDMA-Core、DPDK、DPDK驱动。 
     - 语言库：dpdk-go、libbpf、goebf等
     - 工具包：dpdk-perf、xdp-tools、dpdk-benchmark等
     - 基础服务：libnet、libvma、libkefir等
     - 应用软件包：cilium、lvs-fnat-xdp、kantran等

  3. 开发openEuler高性能网络服务，包括通用用户态协议栈、高性能LVS等。

  4. 跟踪热点技术相关的应用发展，包括的方向有：XDP改造内核网络基础设施、XDP改造容器/虚拟化网络、DPDK性能优化等几个方向。



 ### 该SIG管理的repository及描述

- 项目名称：通用用户态协议栈
  - 交付件形式：源码
  - repository名称：openEuler/libnet

- 项目名称：高性能lvs
  - 交付件形式：源码
  - repository名称：openEuler/lvs




 ### 跨领域和面向外部的流程

 由该SIG定义和执行的，且跨领域和面向外部的流程和行动：

 - 非内部流程清单
 - 该SIG拥有的面向整个openEulerSIG的组织指导计划等


