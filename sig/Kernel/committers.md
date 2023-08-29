# openEuler kernel Committer List

## kernel core

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ------ | -------------------------- | --------------------------------- |
| kernel | kernel/\*                   | [@xiexiuqi](https://gitee.com/xiexiuqi)  [@gatieme](https://gitee.com/gatieme) [@zhengzucheng](https://gitee.com/zhengzucheng) |
| mm     | mm/                        | [@wkf](https://gitee.com/wkfxxx)                           |
| kvm    | Documentation/virt/kvm/<br/>include/asm-generic/kvm\*<br/>include/kvm/<br/>include/linux/kvm\*<br/>include/trace/events/kvm.h<br/>include/uapi/asm-generic/kvm\*<br/>include/uapi/linux/kvm\*<br/>tools/kvm/<br/>tools/testing/selftests/kvm/<br/>virt/kvm/<br/>arch/\*/include/asm/kvm\*<br/>arch/\*/include/uapi/asm/kvm\*<br/>arch/\*/kvm/ | [@yuzenghui](https://gitee.com/yuzenghui) [@kevinzhu1](https://gitee.com/kevinzhu1)             |
| bpf    | kernel/bpf/<br/>net/bpf/   | [@xukuohai](https://gitee.com/xukuohai)                         |
| cgroup | kernel/cgroup              | [@lujialin](https://gitee.com/lujialin2)                        |
| sched  | include/linux/preempt.h<br/>include/linux/sched.h<br/>include/linux/wait.h<br/>include/uapi/linux/sched.h<br/>kernel/sched/              | [@oskernel0719](https://gitee.com/oskernel0719) |
| PGO    | kernel/gcov/gcc_4_7.c<br/>kernel/gcov/gcc_base.c | liyancheng@huawei.com xiezhiheng@huawei.com |

## arch

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ------ | ------------------------------------------------------------ | ------------ |
| 鲲鹏   | kunpang platform  | [@alvin](https://gitee.com/alvin-ling) |
| intel  | intel platform    | [@zhengzengkai](https://gitee.com/zhengzengkai) [@Jackie Liu](https://gitee.com/newbeats)  |
| 龙芯   | arch/loongarch/<br/>tools/arch/loongarch/<br/>drivers/gpu/drm/loongson/<br/>tools/perf/arch/loongarch/<br/>drivers/irqchip/irq-loongson-\*<br/>drivers/irqchip/irq-loongarch-\*<br/>drivers/spi/spi-loongson.c<br/>drivers/char/ipmi/btlock.h<br/>drivers/char/ipmi/ipmi_si.h<br/>drivers/char/ipmi/ipmi_si_intf.c<br/>drivers/char/ipmi/ipmi_si_ls2k500.c<br/>drivers/char/ipmi/kcs_bmc_ls2k500.h<br/>drivers/gpio/gpio-loongson.c<br/>drivers/i2c/busses/i2c-loongson.c<br/>drivers/pci/controller/pci-loongson.c<br/>drivers/input/serio/i8042-loongsonio.h<br/>drivers/cpufreq/loongson3-acpi-cpufreq.c<br/>drivers/firmware/efi/libstub/loongarch-stub.c<br/>drivers/net/ethernet/stmicro/stmmac/dwmac-loongson.c<br/>drivers/platform/loongarch/loongson_generic_laptop.c | [@lixuefeng-loongson](https://gitee.com/lixuefeng-loongson) [@maobibo](https://gitee.com/maobibo) [@Hongchen_Zhang](https://gitee.com/Hongchen_Zhang) | 
| 兆芯   | zhaoxin platform    | [@liuxin](https://gitee.com/liuxinux) |
| 海光   | hygon platform      | [@zhengzengkai](https://gitee.com/zhengzengkai)  |
| 飞腾   | phytium platform     | [@zhengzengkai](https://gitee.com/zhengzengkai)  |
| 树莓派 | raspberrypi-kernel                                | [@woqidaideshi](https://gitee.com/woqidaideshi) |
| ACPI   | drivers/acpi/                                                | [@guohanjun](https://gitee.com/hanjun_guo) [@wangxiongfeng](https://gitee.com/wangxiongfeng) |
| MPAM   | arch/arm64/kernel/mpam<br/>drivers/acpi/arm64/mpam<br/>fs/resctrlfs | [@jentlestea](https://gitee.com/jentlestea)   |
| risc-v | arch/risc-v/\*                                                | [@whoisxxx](https://gitee.com/whoisxxx)  [@xingmz](https://gitee.com/xingmz)    |
| smmu   | drivers/iommu/arm-smmu\*<br />drivers/iommu/io-pgtable-arm\*   | [@ThunderTown](https://gitee.com/ThunderTown)       |

## Kunpeng
| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| SoC PCIe  | drivers/hwtracing/ptt<br/>drivers/pci<br/>drivers/acpi/pci\*<br/>arch/arm64/kernel/pci.c | [@Young1c](https://gitee.com/Young1c) |
| SoC IP    | drivers/i2c/busses/i2c-hisi.c<br/>drivers/spi/spi-hisi-\*<br/>drivers/gpio/gpio-hisi.c | [@Young1c](https://gitee.com/Young1c) |


## HISILICON
| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| ACCELERATOR Controller DRIVER | Documentation/ABI/testing/debugfs-hisi-zip<br/>Documentation/ABI/testing/debugfs-hisi-sec<br/>Documentation/ABI/testing/debugfs-hisi-hpre<br/>drivers/crypto/hisilicon/<br/>include/linux/hisi_acc_qm.h | [@youngersun](https://gitee.com/youngersun) | 
| PMU DRIVER | Documentation/admin-guide/perf/hisi-pcie-pmu.rst<br/>Documentation/admin-guide/perf/hisi-pmu.rst<br/>drivers/perf/hisilicon/ | [@youngersun](https://gitee.com/youngersun)  |
| NETWORK SUBSYSTEM 3 DRIVER (HNS3)| drivers/net/ethernet/hisilicon/hns3/<br/>drivers/perf/hisilicon/hns3_pmu.c | [@WangBoe2022](https://gitee.com/WangBoe2022) | 
| ROCE DRIVER | Documentation/devicetree/bindings/infiniband/hisilicon-hns-roce.txt<br/>include/uapi/rdma/hns-abi.h<br/>drivers/infiniband/hw/hns/ | [@hellotcc](https://gitee.com/hellotcc) |
| ROH DRIVER | drivers/roh/core<br/>drivers/roh/hw/hns3 | [@chenke1978](https://gitee.com/chenke1978) |
| SAS/SATE DRIVER | Documentation/devicetree/bindings/scsi/hisilicon-sas.txt<br/>drivers/scsi/hisi_sas/<br/>drivers/ata/ahci.c | [@LiYihang226](https://gitee.com/LiYihang226) |


## filesystem & storage

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| ext3/ext4 | fs/ext4 | [@zhangyi](https://gitee.com/zhangyi089) |
| xfs       | fs/xfs | [@koulihong](https://gitee.com/koulihong) |
| btrfs     | Documentation/filesystems/btrfs.txt<br/>fs/btrfs/\*<br/>include/linux/btrfs\*<br/>include/uapi/linux/btrfs\* |[@jiaoff](https://gitee.com/jiaoff)|
| eulerfs   | fs/eulerfs                                                   | [@htforge](https://gitee.com/htforge)            |
| nvme      | drivers/nvme/host/<br/>include/linux/nvme.h<br/>include/uapi/linux/nvme_ioctl.h | [@htforge](https://gitee.com/htforge)  @lengchao |
| bcache    | drivers/md/bcache/ | [@Coly Li](https://gitee.com/colyli) |

## network & net drivers

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| -------- | ----------------------------------- | -------------- |
| network  | net/                                | [@yuehaibing](https://gitee.com/yuehaibing)       |
| hns/hns3 | drivers/net/ethernet/hisilicon/hns\* | [@lingmingqiang](https://gitee.com/lingmingqiang) |
| txgbe    | drivers/net/ethernet/netswift/txgbe | [@zhenpengzheng](https://gitee.com/zhenpengzheng) |
| hinic    | drivers/net/ethernet/huawei/hinic   | [@chiqijun](https://gitee.com/chiqijun)           |
| hifc     | drivers/scsi/huawei/hifc            | [@chenguangli](https://gitee.com/chenguangli)     |
| nebula-matrix | Documentation/networking/device_drivers/ethernet/nebula-matrix/<br/>drivers/net/ethernet/nebula-matrix/ | open@nebula-matrix.com | 


## Security

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| security | security/integrity/\*  | [@xiujianfeng](https://gitee.com/xiujianfeng) [@zhujianwei](https://gitee.com/zhujianwei001) |
| cve | \*  | [@xiujianfeng](https://gitee.com/xiujianfeng) [@gatieme](https://gitee.com/gatieme) [@zhengzengkai](https://gitee.com/zhengzengkai) |


## packaging

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ------------------------------------------------------------ | ---------------------- |
| packaging | src-openeuler/kernel/\*                                       | [@wuxu](https://gitee.com/wuxu_buque)            |
| configs   | arch/x86/configs/openeuler_defconfig<br/>arch/arm64/configs/openeuler_defconfig | [@xiexiuqi](https://gitee.com/xiexiuqi)  [@wuxu](https://gitee.com/wuxu_buque) |

## drivers

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ---- | ------------------------------- | ------------ |
| bma  | drivers/net/ethernet/huawei/bma | [@chenjiesong](https://gitee.com/gasonchen) |
| ub   | drivers/net/ethernet/ub/<br/>drivers/ub<br/>drivers/iommu/hisilicon<br/>drivers/ubus<br/>drivers/vfio/ubus<br/>net/ubl | [@chenjiesong](https://gitee.com/gasonchen) [@hucz](https://gitee.com/hucz) [@wsoydl](https://gitee.com/wsoydl) [@JerryHZ](https://gitee.com/JerryHZ)|
| sssraid  | Documentation/scsi/sssraid.rst<br/>drivers/scsi/sssraid/| steven.song@3snic.com |
| sssnic   | Documentation/networking/device_drivers/ethernet/3snic/sssnic/sssnic.rst<br/>drivers/net/ethernet/3snic/sssnic| steven.song@3snic.com |
| ras   | drivers/ras/<br/>drivers/acpi/apei/<br/>drivers/firmware/efi/cper.c| [@hunan4222](https://gitee.com/hunan4222) |



## Notes
* Linux 内核很庞大，社区需要更多的 Committer 参与开发和维护。
* 非常期望有更多人参与细分子模块的开发和维护，成为各模块的 Committer。
