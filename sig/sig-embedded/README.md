
# Embedded SIG
## 使命和愿景

Embedded SIG 小组致力于openEuler的嵌入式版本开发，使其能够广泛应用于嵌入式设备。

# 组织会议

- 公开的会议时间：北京时间，议题触发，每双周三下午，三点~五点





# 成员


### Maintainer列表
- 朱家法[@wl1587](https://gitee.com/wl1587/) Email:zhujiafa@huawei.com
- 吕修任[@lllxxxrrr](https://gitee.com/lllxxxrrr/) Email: lvxiuren@163.com

### Committer列表
- 吕修任[@lllxxxrrr](https://gitee.com/lllxxxrrr/) Email: lvxiuren@163.com
- 朱家法[@wl1587](https://gitee.com/wl1587/) Email:zhujiafa@huawei.com
- 姚伟利[@yyywwwlll](https://gitee.com/yyywwwlll/)
- 吴高翔[@gxwuOpen](https://gitee.com/gxwuOpen/) Email: wugaoxiang1@huawei.com



# 邮件列表

[邮件列表](dev@openeuler.org)

# IRC 频道
openeuler-embedded

# 项目清单

项目名称：Embedded

repository地址：
- embedded 版本的开发工程，包括构建脚本、工程配置等：openeuler/embedded
- embedded 版本的内核源码仓库：src-openeuler/embedded-kernel

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