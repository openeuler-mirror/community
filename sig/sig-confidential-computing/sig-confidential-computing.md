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

- blue0613
- chenmaodong

### Committer

- whzhe
- liwei3013
- yanlu
- wolfkernel

### Deliverables

- Source code and tar
  - openeuler/secGear
  - openeuler/itrustee_sdk
  - src-openeuler/linux-sgx
  - src-openeuler/linux-sgx-driver
  - src-openeuler/intel-sgx-ssl
  - src-openeuler/ocaml-dune
  - src-openeuler/secGear
  - src-openeuler/itrustee_sdk
  - src-openeuler/intel-device-plugins-for-kubernetes
