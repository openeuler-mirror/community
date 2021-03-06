# Vision for High performance networking SIG

## 网络发展背景1

操作系统协议栈的产生背景是网络IO属于低速IO，为了能够高效利用网卡带宽资源以及提高CPU利用率，Linux内核协议栈通过抽象层达成这一目的。而随着网卡硬件技术的发展，网络IO能力已远超CPU单核计算能力，现有Linux内核协议栈的抽象反而成为系统瓶颈。

<img src = "./Vision for High performance networking SIG-01.png">

## 网络发展趋势1

Linux内核协议栈自身在不停的演进中，比如tcp零拷贝、offload、GRO/GSO等，但是其始终满足不了更高的性能要求。
网络数据面加速技术主流技术类型是bypass内核、offload硬件两类技术。前者代表有：DPDK、XDP，后者代表有：RDMA、智能网卡。

<img src = "./Vision for High performance networking SIG-02.png">

## 网络发展背景2

IT系统逐步向云原生方向发展，底层系统从“远离应用” 逐步“走向应用”。
应用对底层系统的诉求，不再是简单提供xx功能，提供xx runtime等，而是希望提高面向应用的网络服务、面向应用的存储服务等。

<img src = "./Vision for High performance networking SIG-03.png">



面向应用的网络服务与传统网络最大的区别在于，需要从云应用视角定义网络服务能力 ，这种网络服务能力统称为云网络。

云网络是IT和CT融合的产物，云网络并不是要重建一张新的网络来取代现有的网络基础设施，而是在现有网络基础上通过网络虚拟化、云原生化等技术重构出一张面向企业租户、应用的虚拟网络。云网络最终演进方向应该是面向万物互联，作为云计算、云原生等基础场景中企业租户、应用之间的纽带。

云网络的发展趋势大致是：

<img src = "./Vision for High performance networking SIG-06.png">

## 网络发展趋势2

云网络有其自身特点，与传统网络相比技术特点可以归纳为：

- 资源共享：云部署环境以及租户模式决定云网络运行环境必须兼顾资源共享以及安全隔离。
- 弹性伸缩：云网络集群式部署要求随着负载的变化而快速应对，网络服务的部署要能够随着应用负载自动伸缩部署。
- 高性能：随着视频流、HPC、AI等应用场景的广泛部署，低时延/高带宽成为云网络追求的永恒主题。
- 可视化运维：网络服务的边界从传统交换机/路由器延伸至应用的系统调用开始，网络路径所涉及的基础设施复杂而多样，这要求能够提供应用视角的可视化运维能力。
- 领域垂直切分：应用负载多样化，行业场景多样化这些都带来对网络服务要求的不同，随着行业发展会迭代出多样化的行业级网络解决方案，比如：企业私有云网络解决方案，视频直播网络解决方案，工业自动化网络解决方案，政企网络解决方案等。



## 愿景

基于上述两个背景/趋势，高性能网络sig提出2个愿景：

愿景1：通用场景提供高速IO、低速时延的高性能网络解决方案。并且通过eBPF等加速技术对linux网络基础设施（包括iptables、tc、lvs等）进行加速，在兼容传统Linux网络基础设施的前提下，为客户提供更高性能的网络基础设施。

愿景2：立足云原生场景，提供云原生基础网络服务（包括CNI、Ingress、Service Mesh等）面向应用提供网络服务。通过引入行业级网络解决方案，为客户提供网络服务的多样性，同时解决不同网络解决方案易用性。openEuler会基于eBPF技术打造开放式高性能数据面底座，让ISV等下游厂商边缘业务创新。



<img src = "./Vision for High performance networking SIG-05.png">



