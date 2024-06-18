# openEuler K8sDistro SIG

&#160;&#160;&#160;&#160;sig-K8sDistro 致力于围绕以 Kubernetes 为核心的云原生生态，在openEuler社区中适配、维护、推广、创新基于Kubernetes的各类发行版，降低用户对 Kubernetes 和相关云原生工具的安装与使用门槛，让云原生赋能 openEuler 用户。

&#160;&#160;&#160;&#160;当前sig主要工作方向包括：
- [kubeSphere](https://github.com/kubesphere/kubesphere)，KubeSphere 是一个开源的基于 Kubernetes 的容器平台，能够帮助用户快速搭建与运维云原生技术栈，提供可视化的操作界面，并且通过了 CNCF K8s 一致性认证和 Taishan 200 兼容性测试。
- [OKD](https://github.com/openshift/okd)，OKD是红帽公司企业级容器云PaaS平台openshift的开源版本，用以管理混合云和多云应用部署。
- [NestOS](https://gitee.com/openeuler/NestOS)，NestOS是sig-K8sDistro与sig-CloudNative联合孵化的云底座操作系统，技术路线衍生自Fedora CoreOS，但基于openEuler生态深度重新打造，集成openEuler 云原生领域创新特性，便于作为不可变基础设施的一部分被Kubernetes发行版纳管。
- [NKD](https://gitee.com/openeuler/nestos-kubernetes-deployer)，NKD（NestOS Kubernetes Deployer）是NestOS团队面向容器云场景开发的部署运维工具，通过了 CNCF K8s 一致性认证。其旨在通过在集群外提供一系列服务，涵盖了基础设施和Kubernetes核心组件的部署、更新和配置管理等，从而简化了集群部署和升级的流程。NKD的设计目标在于提供更为便捷的集群操作体验，使得用户能够轻松完成复杂的管理任务，从而提高整体部署和维护的效率。
- [CCPS](https://gitee.com/openeuler/ccps)，容器云管理平台解决方案（CCPS）是以 Kubernetes、OKD、CRI-O为基础，以应用为中心的企业级容器云 PaaS 平台，通过全栈自动化操作的 DevOps 工作流，对接各种基础架构的方法，提供自动伸缩、配置管理、资源管理、自动运维等功能，实现对容器化应用的 全生命周期管理。

## SIG组职责

- 适配、维护openEuler社区KubeSphere、OKD等Kubernetes发行版
- 探索Kubernetes发行版在openEuler生态的创新及应用
- 及时响应用户反馈，解决相关问题


## 组织会议
- 本SIG当前安排公开会议为月度例会，由maintainer轮值。如有紧急议题，可联系Maintainer召开临时会议。
- 公开会议时间：北京时间，每月最后一个周五的上午，10点~12点
- 公开会议纪要：https://etherpad.openeuler.org/p/sig-K8sDistro-meetings

## 成员

### Maintainers列表

- 王悦良[@wangyueliang](https://gitee.com/wangyueliang)
- 杜奕威[@duyiwei7w](https://gitee.com/duyiwei7w)
- 王利民[@wanglmb](https://gitee.com/wanglmb)
- 季宗耀[@orangeji11](https://gitee.com/orangeji11)


### Committers列表
- 于爽[@calvinyu](https://gitee.com/calvinyu)
- 郭峰[@pixiake](https://gitee.com/pixiake)
- 孙玉轩[@sunyuxuan12](https://gitee.com/sunyuxuan12)
- 麦合木提·买买提[@mahmut](https://gitee.com/mahmut)
- 朱云成[@zhu-yuncheng](https://gitee.com/zhu-yuncheng)
- 刘阔[@lauk001](https://gitee.com/lauk001)
- 魏欢欢[@weihuanhuan_ky](https://gitee.com/weihuanhuan_ky)


### Honor Maintainer
感谢以下原maintainer对sig-K8sDistro及openEuler社区的贡献：

- 于爽[@calvinyu](https://gitee.com/calvinyu)
- 郭峰[@pixiake](https://gitee.com/pixiake)
- 杨昭[@yangzhao_kl](https://gitee.com/yangzhao_kl)


## 项目清单
  - https://gitee.com/src-openeuler/pulp
  - https://gitee.com/src-openeuler/moosefs
  - https://gitee.com/src-openeuler/quay
  - https://gitee.com/src-openeuler/origin
  - https://gitee.com/src-openeuler/openshift-ansible
  - https://gitee.com/src-openeuler/go-srpm-macros
  - https://gitee.com/src-openeuler/goversioninfo
  - https://gitee.com/src-openeuler/go-rpm-macros
  - https://gitee.com/src-openeuler/bootupd
  - https://gitee.com/src-openeuler/ignition
  - https://gitee.com/src-openeuler/rpm-ostree
  - https://gitee.com/src-openeuler/kubekey
  - https://gitee.com/openeuler/nestos-kubernetes-deployer
  - https://gitee.com/openeuler/ccps

## 联系方式

- [邮件列表](dev@openeuler.org)
- [IRC频道](#openeuler-dev)
- [IRC公开会议](#openeuler-meeting)

## 历史
  &#160;&#160;&#160;&#160;本SIG由原sig-OKD与原sig-KubeSphere合并而来，查看历史信息可访问：
  - [sig-OKD](../../archived_sigs/sig-OKD/)
  - [sig-KubeSphere](../../archived_sigs/sig-KubeSphere/)
