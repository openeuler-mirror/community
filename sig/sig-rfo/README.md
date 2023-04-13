# sig-rfo

Rancher 最初是创业公司 RancherLabs 发起的开源项目，旨在给用户提供开箱即用的容器管理平台。随着容器技术的不断发展，到 Rancher2.0 时代已经完全 Kubernetes 化，成为了一个较为成熟的 Kubernetes 多集群管理软件。

随着 2020 年底 SUSE 收购 RancherLabs，Rancher 已经逐渐成长为一个由多个软件组成的企业级容器管理平台，包括多集群管理平面，Kubernetes 发行版，以及容器安全管理等，并兼容主流的公有云生态。

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
  - 除 Kubernetes 基础组件外，同样打包主流的生态组件（nginx-ingress、flannel、calico 等）
- 充分利用 openEuler 内部生态
  - 基于 openEuler base image 的 package
  - 从 openEuler OS 环境构建
  - 与 openEuler 一致的 CPU 架构支持体系
- 供应链安全
  - 构建物 CVE 扫描
  - 二进制与镜像签名防中间人篡改
  - 社区可信任的镜像仓库

借助此发行版连接 openEuler 和 Rancher 平台的生态，并逐渐展开后续项目孵化。

# RFO quick start

## 前置条件

RFO 仅在 openEuler 上进行功能性验证，并不保证其他系统上运行的可行性，经过验证的系统版本包括：

- openEuler 22.03-LTS
- openEuler 22.03-LTS-SP1

RFO 最低需要以下硬件支持：

- RAM：最低 4 GB（建议至少 8 GB）
- CPU：最少 2（建议至少 4 CPU）

RFO 的性能取决于数据库的性能。由于 RFO 嵌入式运行 etcd 并将数据目录存储在磁盘上，我们建议尽可能使用 SSD 以确保最佳性能。

### 安装准备

查看 OS 版本：

```console
[root@localhost ~]# cat /etc/os-release
NAME="openEuler"
VERSION="22.03 (LTS-SP1)"
ID="openEuler"
VERSION_ID="22.03"
PRETTY_NAME="openEuler 22.03 (LTS-SP1)"
ANSI_COLOR="0;31"
```

配置 NetworkManager 进行忽略 Canal CNI 的 veth 接口

```console
touch /etc/NetworkManager/conf.d/rfo-canal.conf
cat >> /etc/NetworkManager/conf.d/rfo-canal.conf << EOF
[keyfile]
unmanaged-devices=interface-name:cali*;interface-name:flannel*
EOF
systemctl disable nm-cloud-setup.service nm-cloud-setup.timer
systemctl reload NetworkManager
```

停止 openEuler 防火墙服务，RFO 中默认的 Canal CNI 与 Firewalld 网络栈有冲突：

```console
systemctl stop firewalld
systemctl disable firewalld
```

安装依赖组件：

```console
dnf install -y tar vim
```

安装前，需要确保所有节点中，hostname 设置互不相同，具有唯一性

## Server 节点安装

- 使用 install 脚本安装 RFO  
  `curl -sfL https://gitee.com/rfolabs/rfo/raw/rfo-master/install-rfo.sh | INSTALL_RFO_VERSION="v1.26.3+rfor1" sh -`
- 启用 rfo-server 服务  
  `systemctl enable rfo-server.service`
- 启动 rfo-server 服务  
  `systemctl start rfo-server.service`
- （可选）查看 rfo-server 服务日志  
  `journalctl -u rfo-server -f`

运行此安装程序后：

1. rfo-server 服务将被安装。rfo-server 服务将被配置为在节点重启后或进程崩溃或被杀时自动重启。
1. 其他的实用程序将被安装在/var/lib/rancher/rfo/bin/。它们包括 kubectl, crictl, 和 ctr. 注意，这些东西默认不在你的路径上。
1. 还有两个清理脚本会安装到 /usr/local/bin/rfo 的路径上。它们是 rfo-killall.sh 和 rfo-uninstall.sh。
1. 一个 kubeconfig 文件将被写入/etc/rancher/rfo/rfo.yaml。
1. 一个可用于注册其他 server 或 agent 节点的令牌将在 /var/lib/rancher/rfo/server/node-token 文件中创建。

> warning 注意： 如果你要添加额外的 server 节点，则总数必须为奇数。需要奇数来维持选举数。

## Agent 节点安装

- 运行安装程序  
  `curl -sfL https://gitee.com/rfolabs/rfo/raw/rfo-master/install-rfo.sh | INSTALL_RFO_VERSION="v1.26.3+rfor1" INSTALL_RFO_TYPE="agent" sh -`
- 启用 rfo-agent 服务  
  `systemctl enable rfo-agent.service`
- 配置 rfo-agent 服务

  ```console
  mkdir -p /etc/rancher/rfo/
  vim /etc/rancher/rfo/config.yaml
  ```

  config.yaml 的内容。

  ```yaml
  server: https://<server>:9345
  token: <token from server node>
  ```

  其中 token 可以在 server 节点中运行 cat /var/lib/rancher/rfo/server/node-token 命令获取。  
  rfo server 进程通过端口 9345 监听新节点的注册。正常情况下，Kubernetes API 仍可在端口 6443 上使用。

- 启动服务
  `systemctl start rfo-agent.service`
- （可选）查看 rfo-agent 服务日志
  `journalctl -u rfo-agent -f`

## 访问集群

在安装完成 rfo-server 节点后，即可以在 server 节点中使用内置的 kubectl 以及 kubeconfig 配置访问集群：

```console
export KUBECONFIG=/etc/rancher/rfo/rfo.yml
export PATH=/var/lib/rancher/rfo/bin:$PATH
kubectl get pods --all-namespaces
helm ls --all-namespaces
```

或在指令中指定 kubeconfig 文件位置：

```console
kubectl --kubeconfig /etc/rancher/rfo/rfo.yml get pods --all-namespaces
helm --kubeconfig /etc/rancher/rfo/rfo.yml ls --all-namespaces
```

若希望在集群外部访问集群，则可以复制 /etc/rancher/rfo/rfo.yml 配置文件到你位于集群外部的机器上，作为 ~/.kube/config。然后将文件中 127.0.0.1 替换为你的 RFO 服务器的 IP 或主机名。kubectl 现在可以管理你的 RFO 集群了。

# 版本清单

目前 RFO 已发布的版本如下：

- 1.23 Kubernetes Releases(EoL)
  - v1.23.14+rfor1
  - v1.23.15+rfor1
  - v1.23.16+rfor1
  - v1.23.17+rfor1
- 1.24 Kubernetes Releases
  - v1.24.8+rfor1
  - v1.24.9+rfor1
  - v1.24.10+rfor1
  - v1.24.11+rfor1
  - v1.24.12+rfor1
- 1.25 Kubernetes Releases
  - v1.25.4+rfor1
  - v1.25.5+rfor1
  - v1.25.6+rfor1
  - v1.25.7+rfor1
  - v1.25.8+rfor1
- 1.26 Kuberentes Releases
  - v1.26.0+rfor1
  - v1.26.1+rfor1
  - v1.26.2+rfor1
  - v1.26.3+rfor1

RFO 版本发布遵循 Kubernetes Release Plan 以及 RKE2 的发布计划，按月发布对应的版本，计划将在上游 RKE2 发布 2 周内完成对应版本发布。

# 组织会议

每双周周四下午 4:00-5:30

# 成员

### Maintainer 列表

- [@niusmallnan](https://gitee.com/niusmallnan)
- [@orangedeng](https://gitee.com/orangedeng)

### Committer 列表

- [@kingsd041](https://gitee.com/kingsd041)
