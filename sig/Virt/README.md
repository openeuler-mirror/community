# Virt

* 负责openEuler虚拟化相关组件社区技术发展和决策
* 负责openEuler虚拟化相关软件包的规划、升级和维护
* 及时响应openEuler虚拟化产品用户反馈和解决虚拟化相关问题


# 组织会议

- 每双周周五下午2:30-4:30
- 通过邮件申报议题
- [会议纪要归档](https://etherpad.openeuler.org/p/virt-meetings)


# 成员


### Maintainer列表

- zhanghailiang[@zhanghailiang](https://gitee.com/zhanghailiang_lucky)
- fangying[@fangying](https://gitee.com/yorifang)
- xuyandong[@xuyandong](https://gitee.com/xydong)
- wubin[@wubin](https://gitee.com/RootWB)
- wangzhigang[@wangzhigang](https://gitee.com/cellfaint)
- zhendongchen[@zhendongchen](https://gitee.com/zhendongchen)

### Committer列表

- chenqun[@chenqun](https://gitee.com/kuhnchen18)
- xufei[@xufei](https://gitee.com/flyking001)
- zhangliang[@zhangliang](https://gitee.com/zhangliang5)



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
- 21.03 (we are here)
    -
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
        - 轻量级虚拟化：
            - 支持内存弹性
            - 支持arm和X86
            - filebackend的支持
        - 性能优化：
            - 支持iothread
            - IO-QOS增强
            - IO性能优化
        - 标准虚拟化预埋
            - 支持virtio-fs
            - 支持大页
- 21.09
    - StratoVirt：支持标准虚拟化
        - 支持热迁移
        - 支持PCI、ACPI
        - 支持备份与快照
        - 支持极速热启动
- 22.03
    - 虚拟化软硬结合，大幅提升虚拟化性能
    - 支持QEMU用户态热补丁，用户无感知，ms级修复CVE和重大问题


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
- LibcarePlus
    - libcareplus
        - repository地址：https://gitee.com/openeuler/libcareplus
