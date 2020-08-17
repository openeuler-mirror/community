***注意：本文档所有的斜体内容，请在完成时删除***

# SIG名称

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



# 组织会议

- 公开的会议时间：北京时间，每周六下午，14点~15点



# 成员

*<必选，请在此给出团队成员的列表>*

### Maintainer列表

- 419673572@qq.com
- zwfeng@huawei.com
- wangxp006@163.com
- zhuhengbo1@huawei.com
- zhouxudong8@huawei.com
- geffrey.guo@huawei.com
- luzhihao@huawei.com


### Committer列表

- name[@giteeID](giteeID链接)



# 联系方式

*<如果需要单独申请邮件列表，请在此补充邮箱名称：sig-yousigname@openeuler.org。如果不需要，请写上开发邮箱名称：dev@openeuler.org>*

- [邮件列表](dev@openeuler.org)
- [IRC公开会议]()
- 视频会议





# 项目清单

*<可选，如果在申请SIG的时候，就有新项目，请完善此处内容。项目名称和申请表格一致，repository地址和repository.yaml内的申请地址一致>*

项目名称：

repository地址：

- 
- 