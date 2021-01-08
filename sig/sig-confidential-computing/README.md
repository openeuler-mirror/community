# SIG-Confidential_Computing
机密计算（Confidential Computing）是指通过基于硬件的可信执行环境，保护用户使用中的数据的隔离计算技术。传统上传输和存储中的数据是经过加密保护的，可信执行环境（TEE）提供了受保护的环境确保处理中的代码和数据不会被TEE外部读取和修改，进而保护处理中的数据的安全。

## SIG组工作目标和范围

sig-confidential_computing主要讨论在openEuler社区版本中已有或未来规划的机密计算技术：

- 在openEuler社区版本中支持硬件机密计算技术如Intel SGX和ARM Trustzone的基础软件栈和SDK

- 在openEuler社区版本中支持机密计算开发框架，支持机密计算应用开发一套源码支持多种硬件机密计算平台

- 机密计算中间件和服务支持，以及其他面向未来的机密计算讨论和规划

### 交付物
   - 交付件形式：源码、tar包或兼而有之

### 该 SIG 管理的 repository 及描述
- sig-confidential-computing repository地址：
  - https://gitee.com/openeuler/secGear
  - https://gitee.com/openeuler/itrustee_sdk
  - https://gitee.com/src-openeuler/linux-sgx
  - https://gitee.com/src-openeuler/linux-sgx-driver
  - https://gitee.com/src-openeuler/intel-sgx-ssl
  - https://gitee.com/src-openeuler/ocaml-dune

### repository路标

- secGear
<img src="secGear_milestone.png" alt="secGear" style="zoom:80%;" />

# 组织会议

- 公开的会议时间：北京时间，每个月第一、第三周的周二下午，16点~17点

# 成员

### Maintainer列表

- blue0613
- chenmaodong

### Committer列表

- whzhe
- liwei3013
- yanlu
- wolfkernel

# 联系方式
- 邮件列表: dev@openeuler.org
