
# Application to create a new SIG
English | [简体中文](./sig-high-performance-network_cn.md)


Note: The Charter of this SIG follows the convention described in the openEuler charter [README](/en/governance/README.md), and follows [SIG-governance](/en/technical-committee/governance/SIG-governance.md).

## SIG Mission and Scope

Describe the Mission and objectives of the new SIG, including but not limited to:

- The necessity of Sig-high-performance-network

- 1. Network acceleration technology: DPDK/RDMA/XDP is independent of the kernel protocol stack and provides network protocol stack services that are superior to the kernel protocol stack for upper-layer applications. At present, these types of network acceleration technologies have been widely used in various application scenarios. 
  2.  In order to allow manufacturers and enthusiasts using openEuler to use network acceleration technology more conveniently and accurately, openEuler should maintain, develop, and optimize the basic software packages, drivers, language library packages, and tools related to these types of network acceleration technologies. Software packages, basic service software packages, application software packages, etc.
  3. Through the continuous development of this sig, the network acceleration technology system with openEuler characteristics is realized, reflecting several characteristics: ease of use, high performance, and a better software ecology.

- Business scope of Sig-high-performance-network

- 1. Maintain DPDK/RDMA/XDP related software packages, including：

  2. - Basic software package: RDMA-Core, DPDK, DPDK driver. 
     - Language libraries: dpdk-go, libbpf, goebf, etc.
     - Toolkit: dpdk-perf, xdp-tools, dpdk-benchmark, etc.
     - Basic services: libnet, libvma, libkefir, etc.
     - Application software packages: cilium, lvs-fnat-xdp, kantran, etc.

  3. Develop openEuler high-performance network services, including general user mode protocol stack, high-performance LVS, etc.

  4. Track the application development related to hotspot technology, including the following directions: XDP transformation kernel network infrastructure, XDP transformation container/virtualized network, DPDK performance optimization and other directions.




### Deliverables

- Project name: General user mode protocol stack
  - Delivery form: source code
  - repository name: openEuler/libnet

- Project name: High performance lvs
  - Delivery form: source code
  - repository name: openEuler/lvs


### Repositories and description managed by this SIG


### Cross-domain and external-oriented processes

Cross-domain and externally-oriented processes and actions defined and implemented by this SIG:

- Non-Internal Process Checklist

- The organization guidance plan for the entire openEulerSIG owned by this SIG, etc.

