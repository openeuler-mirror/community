# Vision for High performance networking SIG

## Network development background Ⅰ

The background of operating system protocol stack is that network IO belongs to low-speed IO. In order to make efficient use of network card bandwidth resources and improve CPU utilization, Linux kernel protocol stack achieves this goal through abstraction layer. With the development of network card hardware technology, the network IO capacity has far exceeded the CPU single core computing capacity, and the abstraction of the existing Linux kernel protocol stack has become the bottleneck of the system.

<img src = "./Vision for High performance networking SIG-01.png">

## Network development trend Ⅰ

Linux kernel protocol stack itself is constantly evolving, such as TCP zero copy, offload, gro / GSO, but it can not meet the higher performance requirements.

The main types of network data plane acceleration technology are bypass kernel and offload hardware. The former represents dpdk and XDP, while the latter represents RDMA and smart network card.

<img src = "./Vision for High performance networking SIG-02.png">

## Network development background Ⅱ

It system is gradually developing towards cloud origin, and the underlying system is gradually moving from "far away from application" to "application".

The application's demand for the underlying system is no longer to simply provide XX function and XX runtime, but to improve the application-oriented network service and application-oriented storage service.

<img src = "./Vision for High performance networking SIG-03.png">



The biggest difference between application-oriented network service and traditional network is that network service capability needs to be defined from the perspective of cloud application, which is collectively referred to as cloud network.

Cloud network is the product of the integration of it and CT. Cloud network is not to rebuild a new network to replace the existing network infrastructure, but to reconstruct a virtual network for enterprise tenants and applications based on the existing network through network virtualization, cloud biochemistry and other technologies. The ultimate evolution direction of cloud network should be the interconnection of all things, as the link between enterprise tenants and applications in basic scenarios such as cloud computing and cloud nativity.

The development trend of cloud network is as follows:

<img src = "./Vision for High performance networking SIG-06.png">

## Network development trend Ⅱ

- Compared with traditional network, cloud network has its own characteristics

  

  -Resource sharing: the cloud deployment environment and tenant mode determine that the cloud network operating environment must take resource sharing and security isolation into account.

  -Elastic scaling: cluster deployment of cloud network requires rapid response with the change of load, and the deployment of network services should be able to scale automatically with the application load.

  -High performance: with the wide deployment of video streaming, HPC, AI and other application scenarios, low latency / high bandwidth has become the eternal theme of cloud network.

  -Visual operation and maintenance: the boundary of network service extends from the traditional switch / router to the system call of application. The infrastructure involved in network path is complex and diverse, which requires the ability of visual operation and maintenance from the perspective of application.

  -Vertical domain segmentation: diversified application loads and industry scenarios all bring different requirements for network services. With the development of the industry, diversified industry level network solutions will be iterated out, such as enterprise private cloud network solutions, video live network solutions, industrial automation network solutions, government enterprise network solutions, etc.



## Vision

Based on the above two backgrounds / trends, SIG puts forward two visions

Vision 1: common scenarios provide high-performance network solutions with high-speed IO and low latency. And accelerate the Linux network infrastructure (including iptables, TC, LVS, etc.) through the acceleration technology such as ebpf, to provide higher performance network infrastructure for customers on the premise of compatible with traditional Linux network infrastructure.

Vision 2: Based on the cloud native scene, provide cloud native basic network services (including CNI, advance, service mesh, etc.) and provide network services for applications. Through the introduction of industry level network solutions, we can provide customers with the diversity of network services and solve the ease of use of different network solutions. Openeuler will build an open high-performance data base based on ebpf technology, allowing ISV and other downstream manufacturers to innovate their edge business.



<img src = "./Vision for High performance networking SIG-05.png">



