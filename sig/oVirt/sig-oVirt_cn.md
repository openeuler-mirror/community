# openEuler oVirt兴趣小组（SIG）
[English](./sig-oVirt.md) | 简体中文

oVirt SIG小组致力于将oVirt这款业界知名的开源企业级虚拟化解决方案引入至openEuler社区中，并进行相关适配、迁移和优化，帮助用户解决实际问题。


## oVirt SIG组工作目标和范围

### 工作目标

- 在openEuler社区中添加对oVirt的支持
- 实施oVirt在ARM64平台下的移植、适配和优化工作
- 负责oVirt相关软件包的规划、维护和升级
- 处理oVirt相关文档的多语言
- 将openEuler社区中oVirt的工作成果回馈给上游社区
- 及时响应用户反馈，解决相关问题


### 工作范围

- oVirt相关软件包的维护、升级等
- oVirt相关依赖软件包（如果在openEuler中不存在）的引入、维护、升级等
- oVirt相关依赖软件包（如果在openEuler中已存在）的协调、维护等
- oVirt SIG组所有相关的文档、会议、邮件列表、IRC的管理


### 交付物

- 源码和tar包


### 该SIG管理的repository

oVirt相关软件包的仓库如下，详见：https://resources.ovirt.org/pub/ovirt-4.3/rpm/el7Server/SRPMS/。

- https://gitee.com/src-openeuler/go-ovirt-engine-sdk4
- https://gitee.com/src-openeuler/ioprocess
- https://gitee.com/src-openeuler/ovirt-ansible-cluster-upgrade
- https://gitee.com/src-openeuler/ovirt-ansible-hosted-engine-setup
- https://gitee.com/src-openeuler/ovirt-ansible-infra
- https://gitee.com/src-openeuler/ovirt-provider-ovn
- https://gitee.com/src-openeuler/cockpit-ovirt
- https://gitee.com/src-openeuler/engine-db-query
- https://gitee.com/src-openeuler/go-ovirt-engine-sdk4
- https://gitee.com/src-openeuler/imgbased
- https://gitee.com/src-openeuler/java-ovirt-engine-sdk4
- https://gitee.com/src-openeuler/mingw-spice-vdagent
- https://gitee.com/src-openeuler/mom
- https://gitee.com/src-openeuler/nsis-simple-service-plugin
- https://gitee.com/src-openeuler/otopi
- https://gitee.com/src-openeuler/ovirt-ansible-cluster-upgrade
- https://gitee.com/src-openeuler/ovirt-ansible-disaster-recovery
- https://gitee.com/src-openeuler/ovirt-ansible-engine-setup
- https://gitee.com/src-openeuler/ovirt-ansible-hosted-engine-setup
- https://gitee.com/src-openeuler/ovirt-ansible-image-template
- https://gitee.com/src-openeuler/ovirt-ansible-infra
- https://gitee.com/src-openeuler/ovirt-ansible-manageiq
- https://gitee.com/src-openeuler/ovirt-ansible-repositories
- https://gitee.com/src-openeuler/ovirt-ansible-roles
- https://gitee.com/src-openeuler/ovirt-ansible-shutdown-env
- https://gitee.com/src-openeuler/ovirt-ansible-v2v-conversion-host
- https://gitee.com/src-openeuler/ovirt-ansible-vm-infra
- https://gitee.com/src-openeuler/ovirt-cockpit-sso
- https://gitee.com/src-openeuler/ovirt-engine
- https://gitee.com/src-openeuler/ovirt-engine-api-explorer
- https://gitee.com/src-openeuler/ovirt-engine-appliance
- https://gitee.com/src-openeuler/ovirt-engine-cli
- https://gitee.com/src-openeuler/ovirt-engine-dwh
- https://gitee.com/src-openeuler/ovirt-engine-extension-aaa-ldap
- https://gitee.com/src-openeuler/ovirt-engine-extension-aaa-misc
- https://gitee.com/src-openeuler/ovirt-engine-metrics
- https://gitee.com/src-openeuler/ovirt-engine-nodejs
- https://gitee.com/src-openeuler/ovirt-engine-nodejs-modules
- https://gitee.com/src-openeuler/ovirt-engine-ui-extensions
- https://gitee.com/src-openeuler/ovirt-engine-wildfly
- https://gitee.com/src-openeuler/ovirt-engine-wildfly-overlay
- https://gitee.com/src-openeuler/nodejs-yarn
- https://gitee.com/src-openeuler/ovirt-guest-agent
- https://gitee.com/src-openeuler/ovirt-guest-agent-windows
- https://gitee.com/src-openeuler/ovirt-guest-tools-iso
- https://gitee.com/src-openeuler/ovirt-host
- https://gitee.com/src-openeuler/ovirt-host-deploy
- https://gitee.com/src-openeuler/ovirt-hosted-engine-ha
- https://gitee.com/src-openeuler/ovirt-hosted-engine-setup
- https://gitee.com/src-openeuler/ovirt-imageio-common
- https://gitee.com/src-openeuler/ovirt-imageio-daemon
- https://gitee.com/src-openeuler/ovirt-imageio-proxy
- https://gitee.com/src-openeuler/ovirt-iso-uploader
- https://gitee.com/src-openeuler/ovirt-lldp-labeler
- https://gitee.com/src-openeuler/ovirt-log-collector
- https://gitee.com/src-openeuler/ovirt-node-ng
- https://gitee.com/src-openeuler/ovirt-node-ng-image-update
- https://gitee.com/src-openeuler/ovirt-provider-ovn
- https://gitee.com/src-openeuler/ovirt-release43
- https://gitee.com/src-openeuler/ovirt-scheduler-proxy
- https://gitee.com/src-openeuler/ovirt-setup-lib
- https://gitee.com/src-openeuler/ovirt-vmconsole
- https://gitee.com/src-openeuler/ovirt-web-ui
- https://gitee.com/src-openeuler/nmstate
- https://gitee.com/src-openeuler/unboundid-ldapsdk
- https://gitee.com/src-openeuler/python-ovirt-engine-sdk4
- https://gitee.com/src-openeuler/rubygem-ovirt-engine-sdk4
- https://gitee.com/src-openeuler/v2v-conversion-host
- https://gitee.com/src-openeuler/vdsm
- https://gitee.com/src-openeuler/vdsm-jsonrpc-java
- https://gitee.com/src-openeuler/java-client-kubevirt
- https://gitee.com/src-openeuler/ovirt-engine-extension-aaa-jdbc
- https://gitee.com/src-openeuler/ovirt-engine-extension-logger-log4j
- https://gitee.com/src-openeuler/ovirt-engine-extensions-api
- https://gitee.com/src-openeuler/ovirt-imageio
- https://gitee.com/src-openeuler/ovirt-jboss-modules-maven-plugin
- https://gitee.com/src-openeuler/safelease
- https://gitee.com/src-openeuler/ovirt-engine-api-model
- https://gitee.com/src-openeuler/virt-viewer
- https://gitee.com/src-openeuler/virt-manager


## SIG基本信息

### 项目简介
    https://gitee.com/openeuler/community/tree/master/sig/sig-oVirt/

### Maintainers
- hjimmy
- wm-wm-wm
- jxy_git
- crrs666

### Contributors
- beijing-yitong

### 邮件列表
- dev@openeuler.org

### IRC频道
- #openeuler-dev

### 对外联络人
- hjimmy
