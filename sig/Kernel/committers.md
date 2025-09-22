# openEuler kernel Committer List

## kernel core

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ------ | -------------------------- | --------------------------------- |
| kernel | kernel/\*                   | [@xiexiuqi](https://gitee.com/xiexiuqi) [@zqiao216](https://gitee.com/zqiao216) |
| mm     | mm/                        | [@wkf](https://gitee.com/wkfxxx)                           |
| kvm    | Documentation/virt/kvm/<br/>include/asm-generic/kvm\*<br/>include/kvm/<br/>include/linux/kvm\*<br/>include/trace/events/kvm.h<br/>include/uapi/asm-generic/kvm\*<br/>include/uapi/linux/kvm\*<br/>tools/kvm/<br/>tools/testing/selftests/kvm/<br/>virt/kvm/<br/>arch/\*/include/asm/kvm\*<br/>arch/\*/include/uapi/asm/kvm\*<br/>arch/\*/kvm/ | [@yuzenghui](https://gitee.com/yuzenghui) [@kevinzhu1](https://gitee.com/kevinzhu1)             |
| bpf    | kernel/bpf/<br/>net/bpf/   | [@xukuohai](https://gitee.com/xukuohai) [@yeweihua](https://gitee.com/yeweihua999) |
| cgroup | kernel/cgroup              | [@lujialin2](https://gitee.com/lujialin2)                        |
| sched  | include/linux/preempt.h<br/>include/linux/sched.h<br/>include/linux/wait.h<br/>include/uapi/linux/sched.h<br/>kernel/sched/              | [@zqiao216](https://gitee.com/zqiao216) |
| PGO    | kernel/gcov/gcc_4_7.c<br/>kernel/gcov/gcc_base.c | [@li-yancheng](https://gitee.com/li-yancheng) [@eastb233](https://gitee.com/eastb233) |
| irq    | drivers/irqchip/irq-gic\*    | [@chris_zjh](https://gitee.com/chris_zjh) |
| debugging | kernel/printk<br/>/kernel/trace<br/>kernel/kexec.c<br/>kernel/kexec_core.c<br/>kernel/watchdog.c<br/>kernel/kernel/watchdog_hld.c | [@yeweihua](https://gitee.com/yeweihua999) |
| livepatch | kernel/livepatch        | [@xukuohai](https://gitee.com/xukuohai) [@yeweihua](https://gitee.com/yeweihua999) |


## arch

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ------ | ------------------------------------------------------------ | ------------ |
| 鲲鹏   | kunpeng platform  | [@alvin](https://gitee.com/alvin-ling) |
| intel  | intel platform    | [@x56Jason](https://gitee.com/x56Jason) [@juntianlinux](https://gitee.com/juntianlinux) |
| 龙芯   | arch/loongarch/<br/>tools/arch/loongarch/<br/>drivers/gpu/drm/loongson/<br/>tools/perf/arch/loongarch/<br/>drivers/irqchip/irq-loongson-\*<br/>drivers/irqchip/irq-loongarch-\*<br/>drivers/spi/spi-loongson.c<br/>drivers/char/ipmi/btlock.h<br/>drivers/char/ipmi/ipmi_si.h<br/>drivers/char/ipmi/ipmi_si_intf.c<br/>drivers/char/ipmi/ipmi_si_ls2k500.c<br/>drivers/char/ipmi/kcs_bmc_ls2k500.h<br/>drivers/gpio/gpio-loongson.c<br/>drivers/i2c/busses/i2c-loongson.c<br/>drivers/pci/controller/pci-loongson.c<br/>drivers/input/serio/i8042-loongsonio.h<br/>drivers/cpufreq/loongson3-acpi-cpufreq.c<br/>drivers/firmware/efi/libstub/loongarch-stub.c<br/>drivers/net/ethernet/stmicro/stmmac/dwmac-loongson.c<br/>drivers/platform/loongarch/loongson_generic_laptop.c | [@lixuefeng-loongson](https://gitee.com/lixuefeng-loongson) [@maobibo](https://gitee.com/maobibo) [@Hongchen_Zhang](https://gitee.com/Hongchen_Zhang) | 
| 兆芯   | zhaoxin platform    | [@leoliu-oc](https://gitee.com/leoliu-oc) |
| 海光   | hygon platform      | [@hanliyang](https://gitee.com/hanliyang) [@allen-shi](https://gitee.com/allen-shi) |
| 飞腾   | phytium platform     | [@mao-hongbo](https://gitee.com/mao-hongbo) [@shuaijiakun](https://gitee.com/shuaijiakun)  |
| 树莓派 | raspberrypi-kernel                                | [@woqidaideshi](https://gitee.com/woqidaideshi) |
| ACPI   | drivers/acpi/                                                | [@hanjun_guo](https://gitee.com/hanjun_guo) [@stkid](https://gitee.com/stkid) [@wangxiongfeng](https://gitee.com/wangxiongfeng) |
| MPAM   | arch/arm64/kernel/mpam<br/>drivers/acpi/arm64/mpam<br/>fs/resctrlfs | [@jentlestea](https://gitee.com/jentlestea)   |
| risc-v | arch/risc-v/\*                                                | [@whoisxxx](https://gitee.com/whoisxxx)  [@xingmz](https://gitee.com/xingmz)    |
| smmu   | drivers/iommu/arm/arm-smmu\*<br />drivers/iommu/io-pgtable-arm\*   | [@qinirao](https://gitee.com/qinirao)       |
| arm    | arch/arm/\*<br/>arch/arm64/\*    | [@chris_zjh](https://gitee.com/chris_zjh) |
| powerpc | arch/powerpc/\*    | [@chris_zjh](https://gitee.com/chris_zjh) |
| amd    | amd platform        | [@kile2009](https://gitee.com/kile2009) [@sming56_admin](https://gitee.com/sming56_admin) |
| 申威   | arch/sw64/\*       | [@guzitao](https://gitee.com/guzitao) |

## Kunpeng

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| SoC PCIe  | drivers/hwtracing/ptt<br/>drivers/pci<br/>drivers/acpi/pci\*<br/>arch/arm64/kernel/pci.c | [@Young1c](https://gitee.com/Young1c) |
| SoC IP    | drivers/i2c/busses/i2c-hisi.c<br/>drivers/spi/spi-hisi-\*<br/>drivers/gpio/gpio-hisi.c | [@Young1c](https://gitee.com/Young1c) |


## HISILICON

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| ACCELERATOR Controller DRIVER | Documentation/ABI/testing/debugfs-hisi-zip<br/>Documentation/ABI/testing/debugfs-hisi-sec<br/>Documentation/ABI/testing/debugfs-hisi-hpre<br/>drivers/crypto/hisilicon/<br/>include/linux/hisi_acc_qm.h<br/>drivers/vfio/pci/hisilicon/<br/>drivers/misc/uacce/ | [@liulongfang](https://gitee.com/liulongfang) | 
| PMU DRIVER | Documentation/admin-guide/perf/hisi-pcie-pmu.rst<br/>Documentation/admin-guide/perf/hisi-pmu.rst<br/>drivers/perf/hisilicon/ | [@youngersun](https://gitee.com/youngersun)  |
| NETWORK SUBSYSTEM 3 DRIVER (HNS3)| drivers/net/ethernet/hisilicon/hns3/<br/>drivers/perf/hisilicon/hns3_pmu.c | [@WangBoe2022](https://gitee.com/WangBoe2022) | 
| ROCE DRIVER | Documentation/devicetree/bindings/infiniband/hisilicon-hns-roce.txt<br/>include/uapi/rdma/hns-abi.h<br/>drivers/infiniband/hw/hns/ | [@hellotcc](https://gitee.com/hellotcc) |
| ROH DRIVER | drivers/roh/core<br/>drivers/roh/hw/hns3 | [@chenke1978](https://gitee.com/chenke1978) |
| SAS/SATE DRIVER | Documentation/devicetree/bindings/scsi/hisilicon-sas.txt<br/>drivers/scsi/hisi_sas/<br/>drivers/ata/ahci.c | [@LiYihang226](https://gitee.com/LiYihang226) |
| KUNPENG_HCCS DRIVER | Documentation/ABI/testing/sysfs-devices-platform-kunpeng_hccs<br/>drivers/soc/hisilicon/kunpeng_hccs.h<br/>drivers/soc/hisilicon/kunpeng_hccs.c | [@li-huisong](https://gitee.com/li-huisong) |

## filesystem & storage

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| ext3/ext4 | fs/ext4 | [@zhangyi](https://gitee.com/zhangyi089) |
| xfs       | fs/xfs | [@zhangyi](https://gitee.com/zhangyi089) |
| btrfs     | Documentation/filesystems/btrfs.txt<br/>fs/btrfs/\*<br/>include/linux/btrfs\*<br/>include/uapi/linux/btrfs\* |[@jiaoff](https://gitee.com/jiaoff)|
| eulerfs   | fs/eulerfs                                                   | [@htforge](https://gitee.com/htforge)            |
| nvme      | drivers/nvme/host/<br/>include/linux/nvme.h<br/>include/uapi/linux/nvme_ioctl.h | [@htforge](https://gitee.com/htforge) |
| bcache    | drivers/md/bcache/ | [@Coly Li](https://gitee.com/colyli) |
| enfs      | /fs/nfs/enfs       | [@mingqian218472](https://gitee.com/mingqian218472) |

## network & net drivers

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| -------- | ----------------------------------- | -------------- |
| network  | net/                                | [@yuehaibing](https://gitee.com/yuehaibing)       |
| hns/hns3 | drivers/net/ethernet/hisilicon/hns\* | [@lingmingqiang](https://gitee.com/lingmingqiang) |
| txgbe    | drivers/net/ethernet/netswift/txgbe | [@zhenpengzheng](https://gitee.com/zhenpengzheng) |
| hinic    | drivers/net/ethernet/huawei/hinic   | [@chiqijun](https://gitee.com/chiqijun)           |
| hifc     | drivers/scsi/huawei/hifc            | [@chenguangli](https://gitee.com/chenguangli)     |
| nebula-matrix | Documentation/networking/device_drivers/ethernet/nebula-matrix/<br/>drivers/net/ethernet/nebula-matrix/ | open@nebula-matrix.com | 
| smc      | net/smc/\*            | [@giree2](https://gitee.com/giree2)     |


## Security

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| security | security/integrity/\*  | [@lujialin2](https://gitee.com/lujialin2) [@zhujianwei](https://gitee.com/zhujianwei001) |
| cve | \*  | [@lujialin2](https://gitee.com/lujialin2)  [@zhengzengkai](https://gitee.com/zhengzengkai) |


## packaging

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ------------------------------------------------------------ | ---------------------- |
| packaging | src-openeuler/kernel/\*                                       | [@wuxu](https://gitee.com/wuxu_buque)            |
| configs   | arch/x86/configs/openeuler_defconfig<br/>arch/arm64/configs/openeuler_defconfig | [@SuperSix173](https://gitee.com/SuperSix173) |

## drivers

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ---- | ------------------------------- | ------------ |
| bma  | drivers/net/ethernet/huawei/bma | [@gasonchen](https://gitee.com/gasonchen) |
| ub   | drivers/net/ethernet/ub/<br/>drivers/ub<br/>drivers/iommu/hisilicon<br/>drivers/ubus<br/>drivers/vfio/ubus<br/>net/ubl | [@gasonchen](https://gitee.com/gasonchen) [@hu-chunzhi](https://gitee.com/hu-chunzhi) [@wsoydl](https://gitee.com/wsoydl) [@JerryHZ](https://gitee.com/JerryHZ) [@yunshenglin](https://gitee.com/yunshenglin)|
| sssraid  | Documentation/scsi/sssraid.rst<br/>drivers/scsi/sssraid/| steven.song@3snic.com |
| sssnic   | Documentation/networking/device_drivers/ethernet/3snic/sssnic/sssnic.rst<br/>drivers/net/ethernet/3snic/sssnic| steven.song@3snic.com |
| ras   | drivers/ras/<br/>drivers/acpi/apei/<br/>drivers/firmware/efi/cper.c| [@hunan4222](https://gitee.com/hunan4222) |
| ccp hygon   | drivers/crypto/ccp/hygon<br/>include/uapi/linux/psp-hygon.h  | [@hanliyang](https://gitee.com/hanliyang) |
| lpfc     | drivers/scsi/lpfc           | [@yonghu_4dc5](https://gitee.com/yonghu_4dc5) |
| qla2xxx  | drivers/scsi/qola2xxx       | [@yonghu_4dc5](https://gitee.com/yonghu_4dc5) |
| mpt3sas  | drivers/scsi/mpt3sas        | [@yonghu_4dc5](https://gitee.com/yonghu_4dc5) |
| motorcomm | drivers/net/ethernet/motorcomm/<br/>drivers/net/phy/motorcomm.c| [@Frank_Sae](https://gitee.com/Frank_Sae) |


## tools
| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ---- | ------------------------------- | ------------ |
| perf   | tools/perf<br/>tools/lib/perf\*    | [@SuperSix173](https://gitee.com/SuperSix173) [@xukuohai](https://gitee.com/xukuohai) [@stavewu](https://gitee.com/stavewu) |

## coda

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ---- | ------------------------------- | ------------ |
| coda | drivers/coda/* | [@hjx_gitff](https://gitee.com/hjx_gitff) |
| smmu | drivers/iommu/arm/arm-smmu-v3/arm-s-smmu-v3.c<br/>drivers/iommu/arm/arm-smmu-v3/arm-s-smmu-v3.h | [@hjx_gitff](https://gitee.com/hjx_gitff) |
| arm  | arch/arm64/include/asm/kvm_tmi.h<br/>arch/arm64/include/asm/kvm_tmm.h<br/>arch/arm64/include/asm/virtcca_cvm_host.h<br/>arch/arm64/kernel/virtcca_cvm_host.c<br/>arch/arm64/kvm/tmi.c<br/>arch/arm64/kvm/virtcca_cvm.c<br/>arch/arm64/kvm/virtcca_cvm_exit.c<br/>arch/arm64/include/asm/virtcca_cvm_guest.h<br/>arch/arm64/include/asm/virtcca_cvm_smc.h<br/>arch/arm64/include/uapi/asm/virtcca_cvm_tsi.h<br/>arch/arm64/kernel/virtcca_cvm_guest.c<br/>arch/arm64/kernel/virtcca_cvm_tsi.c<br/> | [@hjx_gitff](https://gitee.com/hjx_gitff) |

## Notes
* Linux 内核很庞大，社区需要更多的 Committer 参与开发和维护。
* 非常期望有更多人参与细分子模块的开发和维护，成为各模块的 Committer。
