# openEuler kernel Committer List

## kernel core

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ------ | -------------------------- | --------------------------------- |
| kernel | kernel/*                   | [@xiexiuqi](https://gitee.com/xiexiuqi)  [@gatieme](https://gitee.com/gatieme) [@zhengzucheng](https://gitee.com/zhengzucheng) |
| mm     | mm/                        | [@wkf](https://gitee.com/wkfxxx)                           |
| kvm    | virt/kvm/<br/>tools/kvm/* | [@yuzenghui](https://gitee.com/yuzenghui) [@kevinzhu](https://gitee.com/kevinzhu1)             |
| bpf    | kernel/bpf/<br/>net/bpf/   | [@xukuohai](https://gitee.com/xukuohai)                         |
| cgroup | kernel/cgroup              | [@lujialin](https://gitee.com/lujialin2)                        |

## arch

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ------ | ------------------------------------------------------------ | ------------ |
| 鲲鹏   | kunpang platform  | [@alvin](https://gitee.com/alvin-ling) |
| intel  | intel platform    | [@zhengzengkai](https://gitee.com/zhengzengkai) [@Jackie Liu](https://gitee.com/newbeats)  |
| 兆芯   | zhaoxin platform    | [@liuxin](https://gitee.com/liuxinux) |
| 海光   | hygon platform      | [@zhengzengkai](https://gitee.com/zhengzengkai)  |
| 飞腾   | phytium platform     | [@zhengzengkai](https://gitee.com/zhengzengkai)  |
| 树莓派 | raspberrypi-kernel                                | [@woqidaideshi](https://gitee.com/woqidaideshi) |
| ACPI   | drivers/acpi/                                                | [@guohanjun](https://gitee.com/hanjun_guo) [@wangxiongfeng](https://gitee.com/wangxiongfeng) |
| MPAM   | arch/arm64/kernel/mpam<br/>drivers/acpi/arm64/mpam<br/>fs/resctrlfs | [@jentlestea](https://gitee.com/jentlestea)   |
| risc-v | arch/risc-v/*                                                | [@whoisxxx](https://gitee.com/whoisxxx)  [@xingmz](https://gitee.com/xingmz)    |
| smmu   | drivers/iommu/arm-smmu*<br />drivers/iommu/io-pgtable-arm*   | [@ThunderTown](https://gitee.com/ThunderTown)       |


## filesystem & storage

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| ext3/ext4 | fs/ext4 | [@zhangyi](https://gitee.com/zhangyi089) |
| xfs       | fs/xfs | [@koulihong](https://gitee.com/koulihong) |
| btrfs     | Documentation/filesystems/btrfs.txt<br/>fs/btrfs/*<br/>include/linux/btrfs*<br/>include/uapi/linux/btrfs* |[@jiaoff](https://gitee.com/jiaoff)|
| eulerfs   | fs/eulerfs                                                   | [@htforge](https://gitee.com/htforge)            |
| nvme      | drivers/nvme/host/<br/>include/linux/nvme.h<br/>include/uapi/linux/nvme_ioctl.h | [@htforge](https://gitee.com/htforge)  @lengchao |
| bcache    | drivers/md/bcache/ | [@Coly Li](https://gitee.com/colyli) |

## network & net drivers

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| -------- | ----------------------------------- | -------------- |
| network  | net/                                | [@yuehaibing](https://gitee.com/yuehaibing)       |
| hns/hns3 | drivers/net/ethernet/hisilicon/hns* | [@lingmingqiang](https://gitee.com/lingmingqiang) |
| txgbe    | drivers/net/ethernet/netswift/txgbe | [@zhenpengzheng](https://gitee.com/zhenpengzheng) |
| hinic    | drivers/net/ethernet/huawei/hinic   | [@chiqijun](https://gitee.com/chiqijun)           |
| hifc     | drivers/scsi/huawei/hifc            | [@chenguangli](https://gitee.com/chenguangli)     |


## Security

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ---- | ------------ |
| security | security/integrity/*  | [@xiujianfeng](https://gitee.com/xiujianfeng) [@zhujianwei](https://gitee.com/zhujianwei001) |
| cve | *  | [@xiujianfeng](https://gitee.com/xiujianfeng) [@gatieme](https://gitee.com/gatieme) [@zhengzengkai](https://gitee.com/zhengzengkai) |


## packaging

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| --------- | ------------------------------------------------------------ | ---------------------- |
| packaging | src-openeuler/kernel/*                                       | [@wuxu](https://gitee.com/wuxu_buque)            |
| configs   | arch/arm64/configs/openeuler_defconfig<br/>arch/arm64/configs/openeuler_defconfig | [@xiexiuqi](https://gitee.com/xiexiuqi)  [@wuxu](https://gitee.com/wuxu_buque) |

## drivers

| 模块<img width=40/>   | 文件<img width=300/>                       | Committer(s) <img width=200/>                     |
| ---- | ------------------------------- | ------------ |
| bma  | drivers/net/ethernet/huawei/bma | [@chenjiesong](https://gitee.com/gasonchen) |



## Notes
* Linux 内核很庞大，社区需要更多的 Committer 参与开发和维护。
* 非常期望有更多人参与细分子模块的开发和维护，成为各模块的 Committer。