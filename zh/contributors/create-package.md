# 新增软件包

执行以下步骤，可以在gitee新增软件包的同时在EulerMaker建立对应工程。

- [操作步骤](#操作步骤)
- [社区LFS服务](#社区LFS服务)

## 操作步骤

通过修改gitee中的openeuler/community仓库实现新增软件包的具体操作步骤如下：

1. 点击进入[community仓库](https://gitee.com/openeuler/community.git)，将其fork到自己的仓库。

2. 将fork完成的community仓库clone到本地。

  ```
  git clone https://gitee.com/"$username"/community.git
  ```

3. 修改community仓库。以在gitee新增zip软件包，并且同步在openEuler:Factory工程项目下添加该包为例。

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

   * 提交PR（请参考[PR提交指南](https://gitee.com/openeuler/community/blob/master/zh/contributors/pull-request.md)，PR合入后将会在gitee建立同名仓库。查看地址：[src-openeuler](https://gitee.com/src-openeuler)。同时在EulerMaker上创建对应工程：https://build.openeuler.org/project/show/openEuler:Factory

## 社区LFS服务

我们建议5MB以上的文件均使用Git LFS进行管理，而在openEuler社区，您可以使用社区自建LFS服务存储大文件。其相较于Gitee LFS服务，可以支持最大5G文件的上传，且拥有更大的存储空间与更快的传输速度。大多数情况下两者的使用方式完全相同，您可能希望了解以下问题：

- 如何配置LFS服务：在仓库根路径下添加`.lfsconfig`文件即可完成配置，配置完成后可使用[Git LFS](https://git-lfs.com/)上传大文件。配置文件内容如下（{owner}/{repo}为启用服务的仓库名称）：

  ```
  [lfs]
      url = https://artlfs.openeuler.openatom.cn/{owner}/{repo}
  ```

- Git LFS的基本使用，即如何推送大文件：详阅[Git LFS 操作指南](https://help.gitee.com/enterprise/code-manage/code-hosting/large-file-manage/git-lfs)。

- 当您推送大文件到自己fork的已启用LFS服务的仓库时：需在本地仓库内手动使用如下命令修改LFS配置（{owner}/{repo}需替换为实际fork后的仓库名称）：

  ```
  $ git config --local lfs.url https://artlfs.openeuler.openatom.cn/{owner}/{repo}
  ```

- 权限认证：克隆或推送大文件时，可能会提示需要输入在`https://artlfs.openeuler.openatom.cn`的账号，使用Gitee账号即可进行认证。使用ssh方式克隆或推送时也需要此认证。

  ```
  Username for 'https://artlfs.openeuler.openatom.cn': gitee_username
  Password for 'https://gitee_username@artlfs.openeuler.openatom.cn':
  ```

- 当您的仓库已使用Gitee LFS，现希望切换到社区自建LFS服务：

  1. 克隆仓库。

      ```
      $ git clone <url>
      ```

  2. 获取存储在Gitee LFS服务中的所有LFS文件。

      ```
      $ git lfs fetch --all origin
      ```

  3. 添加`.lfsconfig`文件配置社区自建LFS服务。

      ```
      $ git add .
      $ git commit -m "add .lfsconfig"
      ```

  4. 推送大文件和提交。

      ```
      $ git lfs push --all origin
      $ git push
      ```
