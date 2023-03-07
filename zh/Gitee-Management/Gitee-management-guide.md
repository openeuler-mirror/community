# openEuler Gitee组织管理指南

openEuler项目使用Gitee来管理团队和代码。本指南包含如何在openEuler社区准则的基础上运作这些组织。



## 服务承诺

Gitee管理团队将竭尽所能提供以下的服务水平：

- 新组织创建在所有成员资格满足以后的72小时内处理
- Repository的新建或迁移请求在PR提交后的72小时内回复。这个过程可能需要申请人提供一些信息，所以可能会花费一些时间。但所有条件一旦满足，Gitee管理团队会在72小时内完成响应repository的处理
- PR提交后的72小时内，会有所答复。问题解决的时间会按照问题的具体情况有所不同。

如果您需要上报紧急请求，请直接联系[openEuler基础设施团队](<mailto:infra@openeuler.org>)快速寻求帮助



##  openEuler的组织说明

- [openEuler](https://gitee.com/openeuler)：主要用于存放源码类项目
- [src-openEuler](https://gitee.com/src-openeuler)：主要用于存放制作发布件所需的软件包


## 将外部代码转移到openEuler组织中

由于开源许可和CLA等问题，在将软件包或/和代码转移到openEuler管理之前，需要进行一些调查，请先向[技术委员会](/zh/technical-committee/README.md)提交申请。



## 团队指导

### 团队角色和权限说明及配置方法





### 处理过程

- 创建新团队或项目请向技术委员会提交申请，请参考[如何申请一个SIG](/zh/technical-committee/governance/README.md)

- 向团队添加新成员， 提交PR申请修改[SIG](/sig)下自己项目的OWNERS文件，该PR可以由团队的`maintainer`批准

  

## repository使用指导

repository还有license、CLA等要求，请参见[openEuler项目模板]()





### 创建一个Repository

``` yaml
- name: A-Tune
  description: ""
  protected_branches:
  - master
  type: private
```

如果你想要在openEuler社区里面新增一个仓库，你可以基于上面的示例提交一个pull request修改
[openeuler.yaml](/repository/openeuler.yaml)或者[src-openeuler.yaml](/repository/src-openeuler.yaml)。

* `name`: 你想创建的新仓库名字。

* `description`: 新仓库描述。

* `type`: 表示仓库的类型。

  * `private`意味着新仓库只对某些特定的人群可见。

  * `public`意味着新仓库对所有人可见。

一旦你的pull request被合入，```openeuler-ci-bot```将会立即创建一个新仓库。


### 删除repository

待补充



