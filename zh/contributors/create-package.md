# 新增软件包

执行以下步骤，可以在atomgit新增软件包的同时在EulerMaker建立对应工程。

- [操作步骤](#操作步骤)
  - [方式一：通过提交 Issue 申请建仓（推荐）](#方式一通过提交-issue-申请建仓推荐)
  - [方式二：通过 Fork 仓库提交 PR 申请建仓](#方式二通过-fork-仓库提交-pr-申请建仓)
- [社区LFS服务](#社区LFS服务)

## 操作步骤

新增软件包支持以下两种方式，推荐使用**方式一**，由机器人自动生成建仓 PR，简化操作流程：

### 方式一：通过提交 Issue 申请建仓（推荐）

通过在 community 仓库提交"创建仓库申请" issue，由社区机器人自动解析 issue 内容并生成建仓 PR，开发者无需 fork 仓库或手动编辑配置文件。

**操作步骤：**

1. 进入 community 仓库的 issue 创建页面：[https://atomgit.com/openeuler/community/issues](https://atomgit.com/openeuler/community/issues)，点击"新建 Issue"，选择**创建仓库申请**模板。

2. 按照模板提示填写以下字段（issue 标题会自动以 `[建仓申请]` 前缀开头，请勿删除该前缀）：

   | 字段 | 是否必填 | 说明 |
   |------|---------|------|
   | 仓库名称 | 是 | 仅支持小写字母、数字和连字符，例如 `my-package` |
   | 仓库所属组织 | 是 | `openeuler`（社区维护项目）或 `src-openeuler`（引入的制品仓） |
   | 上游仓库地址 | 条件必填 | 当组织为 `src-openeuler` 时必填，格式如 `https://gitcode.com/org/repo` 或 `https://github.com/org/repo` |
   | 仓库描述 | 是 | 仓库的简要说明 |
   | 默认分支名称 | 是 | 默认 `master` |
   | 仓库类型 | 是 | `public` 或 `private` |
   | 分支保护配置 | 否 | 配置其他需要创建并保护的分支，每行一条，格式：`分支名:来源分支:保护类型`，例如 `openEuler-24.03-LTS-Next:master:protected` |
   | 所属 SIG 组 | 是 | 软件包所属 SIG 组名称，例如 `Base-service` |

3. 提交 issue 后，机器人会自动监听并处理：

   - **解析与校验**：机器人解析 issue 内容并校验字段合法性，校验失败会在 issue 下评论提示具体错误原因。
   - **自动生成 PR**：校验通过后，机器人会在 community 仓库自动创建建仓 PR，PR 中包含对应新仓库的 yaml 配置文件，PR 描述会关联源 issue 链接以便溯源。
   - **结果反馈**：PR 创建成功后机器人会在 issue 下评论 PR 链接，开发者可继续跟进 PR 审批流程。

4. 若校验失败或 PR 创建失败，根据机器人评论的提示修改 issue 内容后，在 issue 下评论 `/retrigger` 命令触发机器人重新执行建仓流程。

5. PR 由所属 SIG 组维护者审核合入后，将自动建立同名仓库，并同步在 EulerMaker 上创建对应工程：[https://build.openeuler.org/project/show/openEuler:Factory](https://build.openeuler.org/project/show/openEuler:Factory)

### 方式二：通过 Fork 仓库提交 PR 申请建仓

通过修改atomgit中的openeuler/community仓库实现新增软件包的具体操作步骤如下：

1. 点击进入[community仓库](https://atomgit.com/openeuler/community.git)，将其fork到自己的仓库。

2. 将fork完成的community仓库clone到本地。

  ```
  git clone https://atomgit.com/"$username"/community.git
  ```

3. 修改community仓库。以在atomgit新增zip软件包，并且同步在openEuler:Factory工程项目下添加该包为例。

   * cd community/sig

   * 明确软件包所属的sig组，如zip属于Base-service组（请参考贡献者指南中的找到您感兴趣的SIG或项目）；

   * 修改所属sig文件夹下的内容，如项目清单等；

   * 修改所属sig文件夹下的sig-info.yaml，将要新增的软件包以"- src-openeuler/zip"的形式添加到对应的sig组列表下；以zip为例，修改sig/Base-service/sig-info.yaml：

   ```yaml
        repositories:
        - repo: 
          - openeuler/openEuler-rpm-config
          - src-openeuler/abseil-cpp
          - src-openeuler/acl
          - src-openeuler/acpica-tools
          - src-openeuler/adcli
          - src-openeuler/aide
          - src-openeuler/airline

         ...

          - src-openeuler/jansson
          - src-openeuler/apr
          - src-openeuler/python-lxml
          - src-openeuler/zip
   ```

   * 建仓：在 sig/{sig目录}/src-openeuler/软件名首字母 新增下对应的yaml文件(openEuler社区维护项目: openeuler目录；其他社区引入包: src-openeuler目录。示例参考：sig/Base-service/src-openeuler/z/zip.yaml)

      ```yaml
      name: pkgname
      description: about pkgname
      upstream: https://somepkg.org/
      branches:
      - name: master
        type: protected
      type: public
      ```

   * 提交PR（请参考[PR提交指南](https://atomgit.com/openeuler/community/blob/master/zh/contributors/pull-request.md)，PR合入后将会在atomgit建立同名仓库。查看地址：[src-openeuler](https://atomgit.com/src-openeuler)。同时在EulerMaker上创建对应工程：https://build.openeuler.org/project/show/openEuler:Factory

> 关于社区 Git LFS 服务的相关内容请移步 [对应文档](./git-lfs.md) 查看
