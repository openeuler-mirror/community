# Virt

* 愿景：打造面向全场景、支撑多样性算力的虚拟化解决方案
* 负责openEuler虚拟化相关组件社区技术发展和决策
* 负责openEuler虚拟化相关软件包的规划、升级和维护
* 及时响应openEuler虚拟化产品用户反馈和解决虚拟化相关问题


# 组织会议

- 每双周周五下午14:30-16:00
- 通过邮件申报议题
- [会议纪要归档](https://etherpad.openeuler.org/p/Virt-meetings)


# 成员

### OutStanding Contributor List

- 张海亮[@zhanghailiang_lucky](https://gitee.com/zhanghailiang_lucky)
- 吴斌[@RootWB](https://gitee.com/RootWB)
- 王志钢[@cellfaint](https://gitee.com/cellfaint)

### Maintainer List

- 陈振东[@zhendongchen](https://gitee.com/zhendongchen)
- 邢超超[@imxcc](https://gitee.com/imxcc)
- 郑川[@Chuan-Zheng](https://gitee.com/Chuan-Zheng)
- 朱科潜[@kevinzhu1](https://gitee.com/kevinzhu1)
- 杨杰[@frankyj915](https://gitee.com/frankyj915)
- 叶增软[@yezengruan](https://gitee.com/yezengruan)
- 张波[@ooorz](https://gitee.com/ooorz)

### Committer List

- 徐飞[@flyking001](https://gitee.com/flyking001)
- 张亮[@zhangliang5](https://gitee.com/zhangliang5)
- 李佳杰[@lijiajie128](https://gitee.com/lijiajie128)

### Additional Contributors List

- 顾志峰[@ranygu](https://gitee.com/ranygu)
- 张浩[@sebastian2020](https://gitee.com/sebastian2020)
- 黎思恒[@lisiheng](https://gitee.com/lisiheng)
- 侯英乐[@leohou1400](https://gitee.com/leohou1400)
- 李昆山[@liksh](https://gitee.com/liksh)
- 贺毅涛[@friendpalm](https://gitee.com/friendpalm)
- 仇大玉[@michael_qiu](https://gitee.com/Michael_Qiu)
- 曲维杰[@huayun-quweijie](https://gitee.com/huayun-quweijie)
- 陈涛[@bobychen](https://gitee.com/bobychen)
- 汤中睿[@tom0392](https://gitee.com/tom0392)


# 联系方式

- [邮件列表](https://mailweb.openeuler.org/postorius/lists/virt.openeuler.org/): virt@openeuler.org
- [IM](#openeuler-dev)


# 项目路标

- 20.03
    - 中断虚拟化优化：IRQfd路径注入中断优化，大幅提升高性能直通设备（网卡、SSD磁盘等）性能
    - 内存虚拟化优化：借助鲲鹏硬件特性，提升虚拟机启动内存加载速度
    - 存储虚拟化优化：iSCSI模块kworker的NUMA亲和性自绑定优化，提升IPSAN磁盘的IO性能
- 20.09
    - QEMU+KVM
        - 通过双层调度和Hypervisor感知VM调度，优化VM锁抢占，提升多核超分场景性能
        - 通过Guest-Idle-Haltpoll机制优化IPI中断性能，提升数据库业务性能
        - 针对ARM平台虚拟化特性，支持CPU/内存热插、支持KVM CPU可配置为custom模式，提高资源配置灵活性
        - 运维工具VMTOP，支持虚拟机陷入陷出等性能指标快速采集
        - PMU NMI watchdog特性使能hardlockup检测
        - 支持安全启动和可信启动，提高虚拟机安全性
    - StratoVirt：安全、轻量、高性能、低损耗的，组件灵活拆分，面向全场景的可信虚拟化平台
        - 采用Rust语言，支持seccomp，支持多租户隔离，提供可信安全运行环境
        - 具备<50ms的启动性能，<4M的内存底噪，极致性能和轻量，适用端、边、云等多样场景
        - X86 VT，鲲鹏Kunpeng-V等多体系硬件加速虚拟引擎支持
        - ms级设备扩缩能力，为轻量化负载提供灵活的资源伸缩能力
        - 设备模型可扩展，支持PCI等复杂设备规范，兼容Qemu软件生态
        - 多种计算、网络，存储加速方案支持，异构算力灵活协同
- 21.03
    - QEMU+KVM
        - 热迁移PRO
            - 热迁移脏页频率统计
            - 热迁移tls支持multifd
            - 热迁移支持压缩
        - 可靠行&可维护性增强
            - vmtop增强，支持X86
            - QEMU支持IO悬挂
        - QEMU适配内核5.10
    - StratoVirt：增强轻量虚拟化
        - 轻量级虚拟化
            - 支持内存弹性
            - 支持ARM和X86
        - 性能优化
            - 支持iothread，增强IO性能
            - 支持磁盘QoS
        - 标准虚拟化预埋
            - 支持大页
- 21.09
    - StratoVirt：支持标准虚拟化最小集
        - 支持edk2的UEFI启动（ACPI/PCI/PCIe/virtio-pci）
        - 北向兼容libvirt
        - 支持VFIO直通
        - 极速热启动
        - 轻量级虚拟化支持安全管理框架


# 项目清单

- KVM + QEMU
    - kvm
        - repository地址：https://gitee.com/openeuler/kernel
    - qemu
        - repository地址：https://gitee.com/openeuler/qemu
    - libvirt
        - repository地址：https://gitee.com/openeuler/libvirt
    - edk2
        - repository地址：https://gitee.com/src-openeuler/edk2
    - vmtop
        - repository地址：https://gitee.com/openeuler/vmtop
- StratoVirt
    - stratovirt
        - repository地址：https://gitee.com/openeuler/stratovirt
- Capsule
    - capsule
        - repository地址：https://gitee.com/openeuler/capsule
- LibcarePlus
    - libcareplus
        - repository地址：https://gitee.com/openeuler/libcareplus
- Skylark
    - skylark
        - repository地址：https://gitee.com/openeuler/skylark
