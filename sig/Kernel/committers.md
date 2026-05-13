# openEuler kernel Committer List

## kernel core

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ------ | -------------------------- | --------------------------------- |
| kernel | kernel/\*                   | [@xiexiuqi](https://atomgit.com/oekernel) [@zqiao216](https://atomgit.com/zqiao216) |
| mm     | mm/                        | [@wkf](https://atomgit.com/wkfxxx)                           |
| kvm    | Documentation/virt/kvm/<br/>include/asm-generic/kvm\*<br/>include/kvm/<br/>include/linux/kvm\*<br/>include/trace/events/kvm.h<br/>include/uapi/asm-generic/kvm\*<br/>include/uapi/linux/kvm\*<br/>tools/kvm/<br/>tools/testing/selftests/kvm/<br/>virt/kvm/<br/>arch/\*/include/asm/kvm\*<br/>arch/\*/include/uapi/asm/kvm\*<br/>arch/\*/kvm/ | [@yuzenghui](https://atomgit.com/yuzenghui1) [@kevinzhu1](https://atomgit.com/kevinzhu1)             |
| bpf    | kernel/bpf/<br/>net/bpf/   | [@xukuohai](https://atomgit.com/xukuohai) [@yeweihua](https://atomgit.com/yeweihua999) |
| cgroup | kernel/cgroup              | [@lujialin2](https://atomgit.com/lujialin2)                        |
| sched  | include/linux/preempt.h<br/>include/linux/sched.h<br/>include/linux/wait.h<br/>include/uapi/linux/sched.h<br/>kernel/sched/              | [@zqiao216](https://atomgit.com/zqiao216) |
| PGO    | kernel/gcov/gcc_4_7.c<br/>kernel/gcov/gcc_base.c | [@li-yancheng](https://gitee.com/li-yancheng) [@eastb233](https://gitee.com/eastb233) |
| irq    | drivers/irqchip/irq-gic\*    | [@chris_zjh](https://atomgit.com/chriszjh) |
| debugging | kernel/printk<br/>/kernel/trace<br/>kernel/kexec.c<br/>kernel/kexec_core.c<br/>kernel/watchdog.c<br/>kernel/kernel/watchdog_hld.c | [@yeweihua](https://atomgit.com/yeweihua999) |
| livepatch | kernel/livepatch        | [@xukuohai](https://atomgit.com/xukuohai) [@yeweihua](https://atomgit.com/yeweihua999) |
| sched_ext | include/linux/sched/ext.h<br/>kernel/sched/ext\*<br/>tools/sched_ext<br/>tools/testing/selftests/sched_ext | [@cheliequan](https://gitcode.com/jackknight) [@zichengqu](https://gitcode.com/zichengqu) |


## arch

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ------ | ------------------------------------------------------------ | ------------ |
| 鲲鹏   | kunpeng platform  | [@alvin](https://gitee.com/alvin-ling) |
| intel  | intel platform    | [@x56Jason](https://atomgit.com/zeng_zhaorong) [@juntianlinux](https://atomgit.com/juntianlinux) |
| 龙芯   | arch/loongarch/<br/>tools/arch/loongarch/<br/>drivers/gpu/drm/loongson/<br/>tools/perf/arch/loongarch/<br/>drivers/irqchip/irq-loongson-\*<br/>drivers/irqchip/irq-loongarch-\*<br/>drivers/spi/spi-loongson.c<br/>drivers/char/ipmi/btlock.h<br/>drivers/char/ipmi/ipmi_si.h<br/>drivers/char/ipmi/ipmi_si_intf.c<br/>drivers/char/ipmi/ipmi_si_ls2k500.c<br/>drivers/char/ipmi/kcs_bmc_ls2k500.h<br/>drivers/gpio/gpio-loongson.c<br/>drivers/i2c/busses/i2c-loongson.c<br/>drivers/pci/controller/pci-loongson.c<br/>drivers/input/serio/i8042-loongsonio.h<br/>drivers/cpufreq/loongson3-acpi-cpufreq.c<br/>drivers/firmware/efi/libstub/loongarch-stub.c<br/>drivers/net/ethernet/stmicro/stmmac/dwmac-loongson.c<br/>drivers/platform/loongarch/loongson_generic_laptop.c | [@lixuefeng-loongson](https://gitee.com/lixuefeng-loongson) [@maobibo](https://gitee.com/maobibo) [@robinorg](https://atomgit.com/robinorg) | 
| 兆芯   | zhaoxin platform    | [@leoliu-oc](https://atomgit.com/leoliu-oc) |
| 海光   | hygon platform      | [@hanliyang](https://atomgit.com/hanliyang) [@allen-shi](https://atomgit.com/allen-shi) |
| 飞腾   | phytium platform     | [@mao-hongbo](https://gitee.com/mao-hongbo) [@shuaijiakun](https://atomgit.com/shuaijiakun)  |
| 树莓派 | raspberrypi-kernel                                | [@woqidaideshi](https://atomgit.com/woqidaideshi) |
| ACPI   | drivers/acpi/                                                | [@hanjun_guo](https://gitee.com/hanjun_guo) [@stkid](https://atomgit.com/stkid) |
| MPAM   | arch/arm64/kernel/mpam<br/>drivers/acpi/arm64/mpam<br/>fs/resctrlfs | [@jentlestea](https://gitee.com/jentlestea)   |
| risc-v | arch/risc-v/\*                                                | [@whoisxxx](https://atomgit.com/whoisxxx)  [@xingmz](https://atomgit.com/xingmz1)    |
| smmu   | drivers/iommu/arm/arm-smmu\*<br />drivers/iommu/io-pgtable-arm\*   | [@chen-jun-hw](https://atomgit.com/chen-jun-hw)       |
| arm    | arch/arm/\*<br/>arch/arm64/\*    | [@chris_zjh](https://atomgit.com/chriszjh) |
| powerpc | arch/powerpc/\*    | [@chris_zjh](https://atomgit.com/chriszjh) |
| amd    | amd platform        | [@kile2009](https://atomgit.com/kile2009) [@sming56_admin](https://atomgit.com/sming56_admin) |
| 申威   | arch/sw64/\*       | [@guzitao](https://atomgit.com/guzitao) |

## Kunpeng

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| SoC PCIe  | drivers/hwtracing/ptt<br/>drivers/pci<br/>drivers/acpi/pci\*<br/>arch/arm64/kernel/pci.c | [@Young1c](https://gitee.com/Young1c) |
| SoC IP    | drivers/i2c/busses/i2c-hisi.c<br/>drivers/spi/spi-hisi-\*<br/>drivers/gpio/gpio-hisi.c | [@Young1c](https://gitee.com/Young1c) |


## HISILICON

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| ACCELERATOR Controller DRIVER | Documentation/ABI/testing/debugfs-hisi-zip<br/>Documentation/ABI/testing/debugfs-hisi-sec<br/>Documentation/ABI/testing/debugfs-hisi-hpre<br/>drivers/crypto/hisilicon/<br/>include/linux/hisi_acc_qm.h<br/>drivers/vfio/pci/hisilicon/<br/>drivers/misc/uacce/ | [@liulongfang](https://atomgit.com/liulongfang) | 
| PMU DRIVER | Documentation/admin-guide/perf/hisi-pcie-pmu.rst<br/>Documentation/admin-guide/perf/hisi-pmu.rst<br/>drivers/perf/hisilicon/ | [@youngersun](https://atomgit.com/young-sun)  |
| NETWORK SUBSYSTEM 3 DRIVER (HNS3)| drivers/net/ethernet/hisilicon/hns3/<br/>drivers/perf/hisilicon/hns3_pmu.c | [@WangBoe2022](https://atomgit.com/wangboe2022) | 
| ROCE DRIVER | Documentation/devicetree/bindings/infiniband/hisilicon-hns-roce.txt<br/>include/uapi/rdma/hns-abi.h<br/>drivers/infiniband/hw/hns/ | [@hellotcc](https://atomgit.com/hellotcc) |
| ROH DRIVER | drivers/roh/core<br/>drivers/roh/hw/hns3 | [@chenke1978](https://atomgit.com/chenke2026) |
| SAS/SATE DRIVER | Documentation/devicetree/bindings/scsi/hisilicon-sas.txt<br/>drivers/scsi/hisi_sas/<br/>drivers/ata/ahci.c | [@liyihang0226](https://atomgit.com/liyihang0226) |
| KUNPENG_HCCS DRIVER | Documentation/ABI/testing/sysfs-devices-platform-kunpeng_hccs<br/>drivers/soc/hisilicon/kunpeng_hccs.h<br/>drivers/soc/hisilicon/kunpeng_hccs.c | [@li-huisong](https://atomgit.com/li-huisong) |
| HIBMC DRIVER | drivers/gpu/drm/hisilicon/hibmc | [@baratta](https://atomgit.com/baratta) |
| IPMI DRIVER | drivers/char/ipmi/hisi_ipmi_pso.c | [@hewanhan](https://atomgit.com/hewanhan) |

## filesystem & storage

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| ext3/ext4 | fs/ext4 | [@zhangyi](https://atomgit.com/zhangyi089) |
| xfs       | fs/xfs | [@zhangyi](https://atomgit.com/zhangyi089) |
| btrfs     | Documentation/filesystems/btrfs.txt<br/>fs/btrfs/\*<br/>include/linux/btrfs\*<br/>include/uapi/linux/btrfs\* |[@jiaoff](https://gitee.com/jiaoff)|
| eulerfs   | fs/eulerfs                                                   | [@htforge](https://atomgit.com/htforge)            |
| nvme      | drivers/nvme/host/<br/>include/linux/nvme.h<br/>include/uapi/linux/nvme_ioctl.h | [@htforge](https://atomgit.com/htforge) |
| bcache    | drivers/md/bcache/ | [@Coly Li](https://gitee.com/colyli) |
| enfs      | /fs/nfs/enfs       | [@mingqian218472](https://atomgit.com/mingqian218472) |

## network & net drivers

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| -------- | ----------------------------------- | -------------- |
| network  | net/                                | [@yuehaibing](https://gitee.com/yuehaibing)       |
| hns/hns3 | drivers/net/ethernet/hisilicon/hns\* | [@lingmingqiang](https://gitee.com/lingmingqiang) |
| txgbe    | drivers/net/ethernet/netswift/txgbe | [@zhenpengzheng](https://gitee.com/zhenpengzheng) |
| hinic    | drivers/net/ethernet/huawei/hinic   | [@chiqijun](https://atomgit.com/chiqijun)           |
| hifc     | drivers/scsi/huawei/hifc            | [@chenguangli](https://gitee.com/chenguangli)     |
| nebula-matrix | Documentation/networking/device_drivers/ethernet/nebula-matrix/<br/>drivers/net/ethernet/nebula-matrix/ | open@nebula-matrix.com | 
| smc      | net/smc/\*            | [@giree2](https://gitee.com/giree2)     |


## Security

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| security | security/integrity/\*  | [@lujialin2](https://atomgit.com/lujialin2) [@zhujianwei](https://atomgit.com/zhujianwei001) |
| cve | \*  | [@lujialin2](https://atomgit.com/lujialin2)  [@zhengzengkai](https://atomgit.com/zhengzengkai) |


## packaging

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ------------------------------------------------------------ | ---------------------- |
| packaging | src-openeuler/kernel/\*                                       | [@wuxu](https://gitee.com/wuxu_buque)            |
| configs   | arch/x86/configs/openeuler_defconfig<br/>arch/arm64/configs/openeuler_defconfig | [@SuperSix173](https://atomgit.com/SuperSix173) |

## drivers

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ---- | ------------------------------- | ------------ |
| bma  | drivers/net/ethernet/huawei/bma | [@gasonchen](https://atomgit.com/chenjiesong) |
| sssraid  | Documentation/scsi/sssraid.rst<br/>drivers/scsi/sssraid/| steven.song@3snic.com |
| sssnic   | Documentation/networking/device_drivers/ethernet/3snic/sssnic/sssnic.rst<br/>drivers/net/ethernet/3snic/sssnic| steven.song@3snic.com |
| ras   | drivers/ras/<br/>drivers/acpi/apei/<br/>drivers/firmware/efi/cper.c| [@hunan4222](https://atomgit.com/hunan4222) |
| ccp hygon   | drivers/crypto/ccp/hygon<br/>include/uapi/linux/psp-hygon.h  | [@hanliyang](https://atomgit.com/hanliyang) |
| lpfc     | drivers/scsi/lpfc           | [@yonghu_4dc5](https://atomgit.com/yonghu_4dc5) |
| qla2xxx  | drivers/scsi/qola2xxx       | [@yonghu_4dc5](https://atomgit.com/yonghu_4dc5) |
| mpt3sas  | drivers/scsi/mpt3sas        | [@yonghu_4dc5](https://atomgit.com/yonghu_4dc5) |
| motorcomm | drivers/net/ethernet/motorcomm/<br/>drivers/net/phy/motorcomm.c| [@Frank_Sae](https://atomgit.com/Frank_Sae) |
| pci | drivers/virtio       | [@wenzhiwei11](https://atomgit.com/wenzhiwei11) |


## tools
| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ---- | ------------------------------- | ------------ |
| perf   | tools/perf<br/>tools/lib/perf\*    | [@SuperSix173](https://atomgit.com/SuperSix173) [@xukuohai](https://atomgit.com/xukuohai) [@stavewu](https://atomgit.com/stavewu) |

## coda

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ---- | ------------------------------- | ------------ |
| coda | drivers/coda/* | [@hjx_gitff](https://atomgit.com/hjx_gitff) |
| smmu | drivers/iommu/arm/arm-smmu-v3/arm-s-smmu-v3.c<br/>drivers/iommu/arm/arm-smmu-v3/arm-s-smmu-v3.h | [@hjx_gitff](https://atomgit.com/hjx_gitff) |
| arm  | arch/arm64/include/asm/kvm_tmi.h<br/>arch/arm64/include/asm/kvm_tmm.h<br/>arch/arm64/include/asm/virtcca_cvm_host.h<br/>arch/arm64/kernel/virtcca_cvm_host.c<br/>arch/arm64/kvm/tmi.c<br/>arch/arm64/kvm/virtcca_cvm.c<br/>arch/arm64/kvm/virtcca_cvm_exit.c<br/>arch/arm64/include/asm/virtcca_cvm_guest.h<br/>arch/arm64/include/asm/virtcca_cvm_smc.h<br/>arch/arm64/include/uapi/asm/virtcca_cvm_tsi.h<br/>arch/arm64/kernel/virtcca_cvm_guest.c<br/>arch/arm64/kernel/virtcca_cvm_tsi.c<br/> | [@hjx_gitff](https://atomgit.com/hjx_gitff) |

## ub

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ---- | ------------------------------- | ------------ |
| obmm     | drivers/ub/obmm<br/>     include/uapi/ub/obmm.h                                      | [@GaoChao](https://atomgit.com/TrueAI) [@李睿霖](https://atomgit.com/kazero00) |
| udev      | drivers/ub/ubus<br/>     drivers/ub/ubfi<br/>     drivers/vfio/ubus<br/>     include/ub/ubus<br/>     include/ub/ubfi<br/>     include/uapi/ub/ubus | [@junlong-zheng](https://atomgit.com/junlong-zheng)     [@rock_hw](https://atomgit.com/rock_hw) |
| udma     | drivers/ub/urma/hw/udma<br/>     include/uapi/ub/urma/udma<br/>     include/ub/urma/udma | [@hu-chunzhi](https://atomgit.com/hu-chunzhi)     [@shu-shengming](https://atomgit.com/shu-shengming) |
| cdma     | drivers/ub/cdma<br/>     include/uapi/ub/cdma<br/>     include/ub/cdma | [@rock_hw](https://atomgit.com/rock_hw)     [@hongwu-wang](https://atomgit.com/hongwu-wang) |
| unic     | drivers/net/ub<br/>     drivers/ub/ubase<br/>     include/net/ub<br/>     include/ub/ubase | [@chenjunxin1992](https://atomgit.com/chenjunxin1992)     [@fanghaiqinghw](https://atomgit.com/fanghaiqinghw) |
| ub_fwctl | drivers/fwctl/ub                                             | [@hu-chunzhi](https://atomgit.com/hu-chunzhi)     [@caixu-blue](https://atomgit.com/caixu-blue) |
| ummu     | drivers/iommu/hisilicon<br/>     include/linux/ummu_core.h<br/>     include/uapi/linux/ummu_core.h<br/>     drivers/perf/hisilicon/ummu_pmu.c | [@Tankll2021](https://atomgit.com/Tankll2021)     [@fangfeng123](https://atomgit.com/fangfeng123) [@gongleihuawei](https://atomgit.com/gongleihuawei)|
| sentry     | drivers/ub/sentry | [@jiayi0118](https://atomgit.com/jiayi0118) |
| ubdevshm     | drivers/ub/ubdevshm | [@Tankll2021](https://atomgit.com/Tankll2021) |
| ubmempfd     | drivers/ub/ubmempfd | [@Tankll2021](https://atomgit.com/Tankll2021) |
| ub       | drivers/ub                                                   | [@mufengyan](https://atomgit.com/mufengyan)     [@yunshenglin](https://atomgit.com/linyunsheng) |

## Notes
* Linux 内核很庞大，社区需要更多的 Committer 参与开发和维护。
* 非常期望有更多人参与细分子模块的开发和维护，成为各模块的 Committer。
