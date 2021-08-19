
# Application to create a new SIG
English | [简体中文](./sig-industrial-control_cn.md)


Note: The Charter of this SIG follows the convention described in the openEuler charter [README](/en/governance/README.md), and follows [SIG-governance](/en/technical-committee/governance/SIG-governance.md).
The Industrial control  SIG group is mainly dedicated to developing OpenEuler as a real-time operating system for industrial control or embedded applications.

## SIG Mission and Scope

### Mission

Foreign real-time operating systems such as RTAI, RTLinux, Xenomai and other systems have been developed for many years, while the relevant real-time operating system community in China is relatively backward. In order to improve the community activity of the real-time operating system and to face the domestic industrial control and other related fields, we hope to participate in the OpenEuler community and conduct research on the real-time system based on the OpenEuler community, so as to apply it to the industrial control related fields or embedded fields.

Our SIG group will introduce the strong real-time XENOMAI solution and the weak real-time PREMMPT_RT solution to the OpenEuler community, and will migrate, adapt and optimize the common industrial control field bus, so as to build OpenEuler into an operating system that can be applied in the field of industrial control.

On the other hand, with the development of hardware technology, the Real-time hardware virtualization will also become the future development direction. 
this SIG group will focus on the research of hardware virtualization, and will make common RTOS, such as Zephyr, RTEMS, FreeRTOS and other systems run on the same platform as openEuler at the same time.Therefore, OpenEuler will be able to run on the same platform with common RTOS systems, such as Zephyr, RTAMS, FreeRTOS, etc., to meet the needs of new industrial control related fields where some cores run real-time tasks and other cores run general tasks.

### Scope

 - Develop the version life cycle of software packages related to the Xenomai real-time solution
 - Migration, adaptation and optimization of common open source industrial control fieldbuses, such as Modbus, CANopen, EtherCAT, etc
 - Migration of virtualization solutions that are real-time relevant or applicable to the industrial control domain
 - Porting RTOS systems, such as Zephyr,
 - Reuse the results of the Embedded SIG group to provide real-time solutions for embedded systems
 - Give back to the upstream community
 - Respond to user feedback in a timely manner and solve related problems
 - importing other features and new technologies related to industrial control

### Deliverables
 - Source and tar

### Repositories and description managed by this SIG

  - https://gitee.com/openeuler/xenomai
  - https://gitee.com/src-openeuler/xenomai
  - https://gitee.com/src-openeuler/ipipe
  - https://gitee.com/src-openeuler/libmodbus
  - https://gitee.com/src-openeuler/soem
  - https://gitee.com/src-openeuler/soes
  - https://gitee.com/src-openeuler/canopennode
  - https://gitee.com/src-openeuler/igh-ethercat-xenomai
  - https://gitee.com/src-openeuler/libmodbus-xenomai
  - https://gitee.com/src-openeuler/canfestival-xenomai

### Cross-domain and external-oriented processes

TBD. Stay tuned.

