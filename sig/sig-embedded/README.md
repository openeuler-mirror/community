
# Embedded SIG
## 使命和愿景

Embedded SIG 小组致力于openEuler的嵌入式版本开发，使其能够广泛应用于嵌入式设备。

# 组织会议

- 公开的会议时间：北京时间，议题触发，每双周四下午，两点~四点

# 成员


### Maintainer列表
- 任  慰[@vonhust](https://gitee.com/vonhust)
- 谢焜勋[@beilingxie](https://gitee.com/beilingxie)
- 林子畅[@linzichang](https://gitee.com/linzichang)
- 朱家法[@wl1587](https://gitee.com/wl1587)

### Committer列表
- 任  慰[@vonhust](https://gitee.com/vonhust)
- 谢焜勋[@beilingxie](https://gitee.com/beilingxie)
- 林子畅[@linzichang](https://gitee.com/linzichang)
- 朱家法[@wl1587](https://gitee.com/wl1587)
- 方林旭[@fanglinxu](https://gitee.com/fanglinxu)
- 李小勇[@lxy1579](https://gitee.com/lxy1579)
- 李新宇[@alichinese](https://gitee.com/alichinese)
- 罗泳伦[@luojects](https://gitee.com/luojects)
- 刘铭锴[@hmilylmk](https://gitee.com/hmilylmk)
- 韩宗成[@hzc04](https://gitee.com/hzc04)
- 张伟刚[@harvey-rtos](https://gitee.com/harvey-rtos)


# 邮件列表

[邮件列表](dev@openeuler.org)

# IRC 频道
openeuler-embedded

# 项目清单

项目名称：Embedded

repository地址：
- 分布式软总线: openeuler/dsoftbus_standard, openeuler/embedded-ipc
- 实时能力: openeuler/lep, openeuler/UniProton
- 混合关键部署: src-openeuler/libmetal, src-openeuler/OpenAMP
- 编译器和构建工具: src-openeuler/ct-ng, src-openeuler/patchelf
- flash文件系统支持工具: src-openeuler/yaffs2, src-openeuler/mtd-utils
- 嵌入式工具: src-openeuler/libftdi, src-openeuler/urjtag
- 嵌入式OBS构建参考：openeuler/embedded, src-openeuler/embedded-kernel

- roadmap：
```
├── 2021.01：sig成立
    └── 2021.02：基础的用户态轻量级镜像（arm64架构，与sig-RaspberryPi合作，基于社区已支持硬件树莓派验证，包含img验证和容器OS验证）
        └── 2021.03：基于嵌入式场景和基础镜像对rpm包组织结构进行梳理和分层，完成嵌入式版本定制构建系统v1.0（与sig-OS-builder合作）
            └── 2021.04：增加对x86架构的支持（基于kvm virtual machine验证）
                └── 2021.06：增加对Odroid N2开源硬件的支持
                    ···
                        └──2022.03:随openEuler22.03 LTS发布嵌入式版本
```
