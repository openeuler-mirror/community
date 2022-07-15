
# Application to create DyscheOS SIG

English | [简体中文](./sig-DyscheOS_cn.md)


Note: The Charter of this SIG follows the convention described in the openEuler charter [README] (/en/governance/README.md), and follows [SIG-governance] (/en/technical-committee/governance/SIG-governance.md).

## SIG Mission and Scope

Monolithic fails to scale, while micro's performace is poor, what is the future of Operating System.

Computing system in the future could be cluster of tiny computing units, or one big monster divided into many smaller pieces. Maybe heterogeneous computing in which CPUs do little things and devices take on more. How would OS evolve to match these trending?

Those academics are exploring. Some are really disruptive(Barrelfish from ETH Zurich), by designing a totally newly builded OS. Others just reuse and reconstruct current OSes(Popcorn linux).

### Mission

We are aiming at implementing a DYnamic SCalable HEterogeneous Operating System - DyscheOS on heterogeneous many-core system, based on existing OS.

### Scope

- Dividing hardware resource flexibly
- Deploy several OSes, OS can be deployed on user-defined hardware
- Isolation of OSes, OS can not be interrupted by other OS accidentally
- Communication among OSes, through shared memory and interrupts
- Limited sharing of specific devices, for some platform devices
- Collabration of OSes, to make some application running on multiple OSes efficiently

### Deliverables

What and in what form the SIG is responsible for delivering
 
- Source code
- Scripts
- Installation Guide

### Repositories and description managed by this SIG


## Basic Information

### Maintainers
- 黎亮 (liliang_euler)
- 邓广兴 (minknov)
- 高超 (TrueAI)
- 王创 (hw-chuang)

### Committers
- 黎亮 (liliang_euler)
- 邓广兴 (minknov)
- 高超 (TrueAI)
- 王创 (hw-chuang)

### Mailing list
- dev@openeuler.org

### IRC Channel
- #openeuler-dev

### Conference Information


### External Contact
- denggx_elros
