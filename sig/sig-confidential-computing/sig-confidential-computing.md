# Application to create a new SIG
English | [简体中文](./sig-confidential-computing_cn.md)


Note: The Charter of this SIG follows the convention described in the openEuler charter [README] (/en/governance/README.md), and follows [SIG-governance] (/en/technical-committee/governance/SIG-governance.md).

# SIG-Confidential_Computing
Confidential computing is an isolation computing technology that protects data in use through a hardware-based trusted execution environment. Traditionally, data in transmission and storage is encrypted. The Trusted Execution Environment (TEE) provides a protected environment to ensure that the code and data being processed are not read and modified outside TEE, thereby protecting the security of the data being processed. 

## SIG Mission and Scope

The sig-confidential_computing mainly discusses the existing or future confidential computing technologies in the openEuler community version. 

- Supports hardware confidential computing technologies, such as the basic software stack and SDK of Intel SGX and ARM Trustzone 

- Supports the confidential computing development framework to simplicify programming for multiple hardware confidential computing platforms

- Confidential computing middleware and service support, and other future-oriented confidential computing discussions and planning 


### Maintainer

- Guijin Gao[@blue0613](https://gitee.com/blue0613), gaoguijin@huawei.com
- Maodong Chen[@chenmaodong](https://gitee.com/chenmaodong), chenmaodong@xfusion.com
- Linhao Zhang[@wolfkernel](https://gitee.com/wolfkernel), zhanglinhao@huawei.com
- Dongdong Yao[@dongdo-yao](https://gitee.com/dongdo-yao), yaodongdong@huawei.com
- Mingyong Hou[@houmingyong](https://gitee.com/houmingyong), houmingyong@huawei.com

### Committer

- Yu Wang[@BornThisWay](https://gitee.com/BornThisWay), wangyu283@huawei.com
- Cheng Wang[@hzero1996](https://gitee.com/hzero1996), wangcheng156@huawei.com

### Deliverables

- Source code and tar
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
