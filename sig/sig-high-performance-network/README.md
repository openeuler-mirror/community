***注意：本文档所有的斜体内容，请在完成时删除***

# SIG名称

用描述新申请SIG计划工作的范围和目标，包括但不限于：

- Sig-high-performance-network的必要性
- 1. 网络加速技术：DPDK/RDMA/XDP/EVS独立于内核协议栈，为上层应用提供了更优于内核协议栈的网络协议栈服务。当前这几类网络加速技术已经被广泛使用在各种应用场景。
  2. UMDK(Unified Memory Development Kit)是一套以内存语义为核心的分布式通信软件栈，其目标是设计新一代网络架构，颠覆传统通信形态，构建以内存语义互联为中心的计算原生网络，通过该软件栈可以加速HPC、大数据、数据库以及典型中间件(UCX/Redis/Ceph/Nginx等)性能提升数倍。UMDK的核心功能包含内存语义、消息语义、对象事物语义和URPC功能，以及基于UMDK构建的生态中间件，包括分布式锁、UCX、KBSocket等。
  3. 为了让使用openEuler的厂商、爱好者能够更方便、更准确的使用网络加速技术，openEuler应该维护、开发、优化这几类网络加速技术相关的基础软件包、驱动、语言库软件包、工具软件包、基础服务软件包、应用软件包等。
  4. 通过本sig的持续发展，实现openEuler特色的网络加速技术体系，体现几个特点：易用性、高性能、更好的软件生态。
- Sig-high-performance-network的业务范围
- 1. 维护DPDK/RDMA/XDP相关软件包，包括
  2. - 基础软件包：RDMA-Core、DPDK、DPDK驱动。 
     - 语言库：dpdk-go、libbpf、goebf等
     - 工具包：dpdk-perf、xdp-tools、dpdk-benchmark等
     - 基础服务：libnet、libvma、libkefir等
     - 应用软件包：cilium、lvs-fnat-xdp、kantran、eVS等
  3. 开发openEuler高性能网络服务，包括通用用户态协议栈、高性能LVS、高性能eVS转发等。
  4. 跟踪热点技术相关的应用发展，包括的方向有：XDP改造内核网络基础设施、XDP改造容器/虚拟化网络、DPDK性能优化等几个方向。

# 愿景

请[查看](./Vision.md)

Please [readme](./Vision-en.md)

# 组织会议

- 公开的会议时间：北京时间，双周周四晚上，19:00~20:00



# 成员

*<必选，请在此给出团队成员的列表>*

### Maintainer列表

- luzhihao@huawei.com
- huangliming5@huawei.com
- wuchangye@huawei.com
- liuxin264@huawei.com
- humin29@huawei.com
- liyangyang20@huawei.com
- wuchangsheng2@huawei.com

### Committer列表

- 蒋 恒[@jiangheng12](https://gitee.com/jiangheng12) email: jiangheng14@huawei.com

### 突出贡献者
| gitee昵称 | giteeID | 邮箱 | 姓名(可选)|
|---|---|---|---|
|yyang|yyangoO|yyangoo@outlook.com|杨洋|
|honggangli|honggangli22|honggangli@163.com|黎红刚|

# 联系方式

- 邮件列表 <high-performance-network@openeuler.org> <dev@openeuler.org>  
  [注册邮件列表](https://mailweb.openeuler.org/postorius/lists/high-performance-network.openeuler.org/) [历史邮件](https://mailweb.openeuler.org/hyperkitty/list/high-performance-network@openeuler.org/)
- [IRC公开会议]()
- 视频会议
- 微信  
 ![wechat_QR](./sig-wechat-qr.jpg)



# 项目清单

repository地址：

- https://gitee.com/src-openeuler/dpdk
- https://gitee.com/src-openeuler/rdma-core
- https://gitee.com/src-openeuler/libbpf
- https://gitee.com/src-openeuler/goebpf
- https://gitee.com/src-openeuler/xdp-tools
- https://gitee.com/src-openeuler/libvma
- https://gitee.com/src-openeuler/polycube
- https://gitee.com/src-openeuler/cilium
- https://gitee.com/src-openeuler/katran
- https://gitee.com/src-openeuler/pistache
- https://gitee.com/src-openeuler/libyang
- https://gitee.com/src-openeuler/libtins
- https://gitee.com/src-openeuler/go-bindata
- https://gitee.com/src-openeuler/seastar
- https://gitee.com/src-openeuler/gazelle-cni
- https://gitee.com/openeuler/umdk
- https://gitee.com/openeuler/evs
- https://gitee.com/openeuler/gazelle-cni
- https://gitee.com/src-openeuler/gazelle
- https://gitee.com/openeuler/gazelle
- https://gitee.com/src-openeuler/oncn-bwm
- https://gitee.com/openeuler/oncn-bwm
- https://gitee.com/openeuler/GNFC
- https://gitee.com/src-openeuler/Kmesh
- https://gitee.com/openeuler/Kmesh

