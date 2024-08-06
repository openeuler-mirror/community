# 仓库

## 维护

### 背景

在openEuler社区有成百上千个仓库。
这是非常困难的去维护在每一个仓库中的所有成员。
我们需要一个自动化的工具去解决这些问题从而节约团队的工作量。

### 解决方案

基础设施团队构建了一种机制去简化仓库的维护工作。
所有openEuler的仓库和仓库成员都放在
[openeuler.yaml](https://gitee.com/openeuler/community/blob/master/repository/openeuler.yaml)文件中,
而所有src-openEuler的仓库和仓库成员都放在
[src-openeuler.yaml](https://gitee.com/openeuler/community/blob/master/repository/src-openeuler.yaml)文件中。
如果这些yaml文件被一个pull request所修改，`openeuler-ci-bot`将会检测到这些改变
然后自动化地完成一些操作，例如`创建一个仓库`，`为一个仓库添加成员`，
`从一个仓库移除成员`，`保护一个分支`，`移除一个保护分支`等基于Gitee API的操作。

### 如何创建一个仓库

``` yaml
repositories:
  - name: abattis-cantarell-fonts
    description: "fonts repo"
    type: private
```

如果你想要在openEuler社区里面新增一个仓库，
你可以基于上面的示例提交一个pull request修改
[openeuler.yaml](https://gitee.com/openeuler/community/blob/master/repository/openeuler.yaml)
或者[src-openeuler.yaml](https://gitee.com/openeuler/community/blob/master/repository/src-openeuler.yaml)。

* `abattis-cantarell-fonts`: 你想创建的新仓库名字。
* `fonts repo`: 新仓库描述。
* `private`: 表示仓库的类型。

  `private`意味着新仓库只对某些特定的人群可见。

  `public`意味着新仓库对所有人可见。

一旦你的pull request被合入，```openeuler-ci-bot```将会立即创建一个新仓库。

### 如何创建或者删除一个成员

``` yaml
community:
  name: openeuler
  managers:
    - zhuchunyi
    - overweight
  developers:
    - igorkorkin
  viewers:
    - jianminw
repositories:
  - name: abattis-cantarell-fonts
    description: "fonts repo"
    type: private
  - name: accountsservice
    description: "account repo"
    type: private
    managers:
      - dogsheng
    developers:
      - igorkorkin
    viewers:
      - jianminw
```

如果你想要添加或者删除一个仓库的成员，
你可以基于上面的示例提交一个pull request
修改[openeuler.yaml](https://gitee.com/openeuler/community/blob/master/repository/openeuler.yaml)
或者[src-openeuler.yaml](https://gitee.com/openeuler/community/blob/master/repository/src-openeuler.yaml)。

* `openeuler`： openEuler组织名称， 另外还有一个组织`src-openeuler`，实际上不需要做修改。
* `managers`：  你想在`community`或者`repositories`下指定的管理员。
  这里需要Gitee账号，例如 `zhuchunyi`。
* `developers`：你想在`community`或者`repositories`下指定的开发者。
  这里需要Gitee账号，例如`igorkorkin`。
* `viewers`: 你想在`community`或者`repositories`下指定的观察者。
  这里需要Gitee账号，例如`jianminw`。

***注意***：你可能已经发现`managers`，`developers`和`viewers`是同时存在于`community`和`repositories`。
让我们来看看它们的不同之处：

* 通常情况下你想要为所有仓库添加或删除一个管理员，开发者或者观察者，
  你可以修改`community`下的`managers`，`developers`或者`viewers`。
* 特定的情况下你想要为一个指定的仓库添加或删除一个管理员，开发者或者观察者，
  你可以修改指定的仓库例如`accountsservice`下的`community`下的`managers`，`developers`或者`viewers`。
* 如果一个仓库没有指定任何成员（包括`managers`，`developers`和`viewers`），例如`abattis-cantarell-fonts`仓库，
  `openeuler-ci-bot`将会使用`community`下的`managers`，`developers`和`viewers`
  来为这个仓库例如`abattis-cantarell-fonts`仓库创建成员。
* 如果一个仓库指定了一些成员（包括`managers`，`developers`和`viewers`），例如`accountsservice`仓库，
  `openeuler-ci-bot`将会使用这个仓库下的`managers`，`developers`和`viewers`
  来为这个仓库例如`accountsservice`仓库创建成员。
* 如果一个Gitee账号是存在于`managers`，`developers`和`viewers`之中，
  这个Gitee账号将会是一个管理员，因为从Gitee的权限来讲，`managers` > `developers` > `viewers`。

### 如何创建或者删除一个保护分支

```yaml
community:
  name: openeuler
  protected_branches:
  - master
repositories:
  - name: abattis-cantarell-fonts
    description: "fonts repo"
    type: private
  - name: accountsservice
    description: "account repo"
    protected_branches:
    - master
    - dev
    type: private
```

如果你想要在一个仓库上创建或者删除一个保护分支，
你可以基于上面的示例提交一个pull request
修改[openeuler.yaml](https://gitee.com/openeuler/community/blob/master/repository/openeuler.yaml)
或者[src-openeuler.yaml](https://gitee.com/openeuler/community/blob/master/repository/src-openeuler.yaml)。

* `openeuler`：openEuler组织名称， 另外还有一个组织`src-openeuler`，实际上不需要做修改。
* `protected_branches`：你想要在`community`或`repositories`创建的保护分支。

***注意***：你可能已经发现`protected_branches`是同时存在于`community`和`repositories`。
让我们来看看它们的不同之处：

* 通常情况下你想要为所有仓库创建或删除一个保护分支，
  你可以修改`community`下的`protected_branches`。
* 特定的情况下你想要为一个指定的仓库添加或删除一个保护分支，
  你可以修改指定的仓库例如`accountsservice`下的`community`下的`protected_branches`。
* 如果一个仓库没有指定任何保护分支，例如`abattis-cantarell-fonts`仓库，
  `openeuler-ci-bot`将会使用`community`下的`protected_branches`
  来为这个仓库例如`abattis-cantarell-fonts`仓库创建保护分支。
* 如果一个仓库指定了一些保护分支，例如`accountsservice`仓库，
  `openeuler-ci-bot`将会使用这个仓库下的`protected_branches`
  来为这个仓库例如`accountsservice`仓库创建保护分支。
* 如果指定的`protected_branches`不存在，`openeuler-ci-bot`将会做任何动作。

### 如何创建或者删除一个在Gitee之外的维护人员

Gitee提供管理员、开发者和观察者等权限管理。
`openeuler-ci-bot`支持另一种为每一个仓库添加维护人员的方式。
`openeuler-ci-bot`将会扫描 `OWNERS`文件在每一个仓库下去发现额外的仓库维护人员。

以`ci-bot`仓库下的 <https://gitee.com/openeuler/ci-bot/blob/master/OWNERS> 为例。
文件内容如下：

``` yaml
maintainers:
  - edisontest
  - freesky-edward
  - TommyLike
  - xiangxinyong
  - zerodefect
```

这意味着所有这5个用户具备在`ci-bot`仓库下合入pull request的权限。
这些用户能使用`/lgtm`和`/approve`命令去触发`openeuler-ci-bot`何如pull request。
你可以发现更多的命令说明 <https://gitee.com/openeuler/community/blob/master/zh/sig-infrastructure/command.md>。
顺便说下，所有的Gitee管理员和开发者也能使用`/lgtm`和`/approve`命令。

如果你想要维护Gitee之外的仓库维护人员，请在你的仓库下添加`OWNERS`文件，
然后添加仓库维护人员到`OWNERS`文件，`openeuler-ci-bot`将会给予这些仓库维护人员`合入`权限。