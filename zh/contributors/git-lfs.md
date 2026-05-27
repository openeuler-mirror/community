## openEuler 社区 LFS 服务

我们建议 5MB 以上的文件均使用 Git LFS 进行管理，而在 openEuler 社区，您可以使用社区自建 LFS 服务存储大文件。其相较于 AtomGit LFS 服务，可以支持最大 5GB 文件的上传，且拥有更大的存储空间与更快的传输速度，大多数情况下两者的使用方式完全相同。

- Git LFS 的基本使用，即如何推送大文件：详阅 [Git LFS 操作指南](https://github.com/opensourceways/BigFiles/blob/master/docs/BasicGuide.md)。

- 社区 LFS 服务的域名为 https://artlfs.openeuler.openatom.cn
  - 目前暂未提供 Web 访问，浏览器打开可能显示 `{"message":"Success","data":"healthCheck success"}`

### 仓库配置

- 为 src-openEuler/ 及 openEuler/ 的仓库（下称 openEuler 社区仓库）配置使用 openEuler 社区 LFS 服务

  - 在涉及的每个仓库根路径下添加 `.lfsconfig` 配置文件使 Git LFS 向 `https://artlfs.openeuler.openatom.cn` 提交和获取文件

    > 此处 {owner}/{repo}为启用服务的仓库名称

    ```
    [lfs]
        url = https://artlfs.openeuler.openatom.cn/{owner}/{repo}
    ```

  - 个人 fork 已启用社区 LFS 服务的 openEuler 社区仓库（或为 openEuler 社区仓库添加社区 LFS 配置时）

    - 需在本地仓库内手动使用如下命令修改 LFS 配置
    
    > {owner}/{repo}需替换为实际fork后的仓库名称

  ```
  $ git config --local lfs.url https://artlfs.openeuler.openatom.cn/{owner}/{repo}
  ```

### 权限认证

- 克隆或推送大文件时，可能会提示需要输入在 `https://artlfs.openeuler.openatom.cn` 的用户名与口令

  ```
  Username for 'https://artlfs.openeuler.openatom.cn': atomgit_username
  Password for 'https://atomgit_username@artlfs.openeuler.openatom.cn': atomgit_token
  ```

    - 用户名：输入您的 AtomGit 用户名 (如 @atomgit_username 中的 atomgit_username )
    - 口令：输入您的 AtomGit 访问令牌（常称为 PAT）
    > 未创建过访问令牌的用户可移步 AtomGit 网站“个人设置”页面左侧“安全设置”栏点击“访问令牌”，并在右上角点击“新建访问令牌”进行创建。

### 迁移

#### 从 AtomGit 网站 LFS 服务切换到 openEuler 社区 LFS 服务

- 当您的仓库已使用AtomGit LFS，现希望切换到社区自建LFS服务：

  1. 克隆仓库。

      ```
      $ git clone <url>
      ```

  2. 获取存储在AtomGit LFS服务中的所有LFS文件。

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

### 常见问题

- 尝试通过 LFS 推送文件，输入完成用户名与口令后又反复提示输入用户名及口令
  - 检查您的 AtomGit 用户名与口令（AtomGit 访问令牌）是否输入正确
    - 若您在社区托管平台由 Gitee 迁移至 AtomGit 前就有使用社区 LFS 服务并按先前习惯输入了 Gitee 用户名及 Gitee 密码，请切换为 AtomGit 用户名与 AtomGit 访问令牌进行操作

- 推送到个人 fork 仓库时出现如下提示 `remote: GitCode: LFS objects are missing. Ensure LFS is properly setup or try a manual: git lfs push --all
  - 尝试如下操作进行确认
    - 确认本地 `git config --local lfs.url` 有正确设置
    - 确认对应社区仓库根目录下 `.lfsconfig` 有正确配套/添加
    - 确认手动 `git lfs push --all` 输入用户名及口令能够进行推送且无报错
  - 确认 fork 仓库设置中“自定义 LFS 存储源”选项是否已启用（此处一般为未启用）
    - 移步 AtomGit 对应仓库页面 - 项目设置 - 仓库管理 - LFS 设置并勾选“启用自定义 LFS 存储源”

