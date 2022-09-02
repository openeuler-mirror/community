# sig-rfo

Rancher最初是创业公司 RancherLabs 发起的开源项目，旨在给用户提供开箱即用的容器管理平台。随着容器技术的不断发展，到 Rancher2.0 时代已经完全Kubernetes化，成为了一个较为成熟的 Kubernetes 多集群管理软件。

随着2020年底 SUSE 收购 RancherLabs，Rancher 已经逐渐成长为一个由多个软件组成的企业级容器管理平台，包括多集群管理平面，Kubernetes发行版，以及容器安全管理等，并兼容主流的公有云生态。

RFO 的含义为 Rancher For openEuler，旨在打造面向 openEuler 的 Rancher 基础平台系统。

# 工作目标和范围

面向 openEuler 打造一款 Kubernetes 发行版，期望成为 openEuler 系统之上最好用的发行版，持续的工程化，且达到安全合规标准。

它具备以下特性：

- 完整可溯源的工程化
  - 从源码构建
  - CI Build 历史记录
  - e2e 测试结果
- 产品化，开箱即用
  - 版本生命周期与支持矩阵
  - 较少依赖的安装体验
  - 除Kubernetes基础组件外，同样打包主流的生态组件（nginx-ingress、flannel、calico等）
- 充分利用openEuler内部生态
  - 基于openEuler base image的package
  - 从openEuler OS环境构建
  - 与openEuler一致的CPU架构支持体系
- 供应链安全
  - 构建物CVE扫描
  - 二进制与镜像签名防中间人篡改
  - 社区可信任的镜像仓库

借助此发行版连接 openEuler 和 Rancher 平台的生态，并逐渐展开后续项目孵化。

# 组织会议

每双周周四下午4:00-5:30

# 成员

### Maintainer列表

- [@niusmallnan](https://gitee.com/niusmallnan)
- [@orangedeng](https://gitee.com/orangedeng)

### Committer列表

- [@kingsd041](https://gitee.com/kingsd041)

