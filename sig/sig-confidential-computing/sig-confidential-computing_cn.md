# 新建SIG申请
[English](./sig-confidential-computing.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

# SIG-Confidential_Computing
机密计算（Confidential Computing）是指通过基于硬件的可信执行环境，保护用户使用中的数据的隔离计算技术。传统上传输和存储中的数据是经过加密保护的，可信执行环境（TEE）提供了受保护的环境确保处理中的代码和数据不会被TEE外部读取和修改，进而保护处理中的数据的安全。


## SIG组工作目标和范围

sig-confidential_computing主要讨论在openEuler社区版本中已有或未来规划的机密计算技术：

- 在openEuler社区版本中支持硬件机密计算技术如Intel SGX和ARM Trustzone的基础软件栈和SDK

- 在openEuler社区版本中支持机密计算开发框架，支持机密计算应用开发一套源码支持多种硬件机密计算平台

- 机密计算中间件和服务支持，以及其他面向未来的机密计算讨论和规划



 ### 该SIG管理的repository及描述

- sig-confidential-computing：
  - 交付件形式：源码、tar包或兼而有之
  - openeuler/secGear
  - openeuler/itrustee_sdk
  - openeuler/itrustee_tzdriver
  - openeuler/itrustee_client
  - src-openeuler/linux-sgx
  - src-openeuler/linux-sgx-driver
  - src-openeuler/intel-sgx-ssl
  - src-openeuler/secGear
  - src-openeuler/itrustee_sdk
  - src-openeuler/intel-device-plugins-for-kubernetes
