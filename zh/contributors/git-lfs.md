## openEuler 社区 LFS 服务

我们建议 5MB 以上的文件均使用 Git LFS 进行管理，而在 openEuler 社区，您可以使用社区自建 LFS 服务存储大文件。其相较于 AtomGit LFS 服务，可以支持最大 5GB 文件的上传，且拥有更大的存储空间与更快的传输速度，大多数情况下两者的使用方式完全相同。

- Git LFS 的基本使用，即如何推送大文件：详阅 [Git LFS 操作指南](https://github.com/opensourceways/BigFiles/blob/master/docs/BasicGuide.md)。

- 社区 LFS 服务的域名为 https://artlfs.openeuler.openatom.cn
  - 目前暂未提供 Web 访问，浏览器打开可能显示 `{"message":"Success","data":"healthCheck success"}`

> 初次使用 Git LFS? 请注意 Git LFS 工具安装完成后您还需要执行一次 `git lfs install` 才能使之全局生效

### 仓库配置

> 注意：仓库根路径下应当已经存在 `.lfsconfig` 文件且 URL 中包含 `src-openEuler` 或 `openEuler`，**贡献时请不要随意修改这个配置文件**

> 如果仓库根路径下尚不存在 `.lfsconfig` 文件，请跳到 `为尚未使用社区 LFS 服务的官方仓库初次配置启用` 部分

#### 向已启用社区 LFS 服务的官方仓库提交贡献

- 手动修改本地 fork 仓库 LFS URL 配置：贡献者将自己 fork 的仓库 clone 到本地后，应当在仓库对应文件夹内手动使用如下命令修改这一本地仓库的 LFS URL 配置，使本地 Git LFS 向 `https://artlfs.openeuler.openatom.cn` **贡献者 fork 仓库对应目录**提交和获取文件
 
  > `{atomgit_username}/{repo}` 需替换为实际 fork 后的仓库名称，此配置仅对本地这一仓库生效，优先级高于 `.lfsconfig`

  ```
  $ git config --local lfs.url https://artlfs.openeuler.openatom.cn/{atomgit_username}/{repo}
  ```

- 如上配置后即可照常修改提交，若修改涉及 LFS 管理的文件则 git push 时需要输入 artlfs 用户名与口令，具体请参考后文 `权限认证` 部分

#### 为尚未使用社区 LFS 服务的官方仓库初次配置启用

  - 添加初始 LFS 配置：在涉及的每个仓库根路径下添加 `.lfsconfig` 配置文件使 Git LFS 默认情况下向 `https://artlfs.openeuler.openatom.cn` **官方仓库对应目录**提交和获取文件

    > 此处 `{org}/{repo}` 为启用服务的仓库名称，`src-openEuler/` 下仓库需改为 `src-openEuler/{repo}`，`openEuler/` 下仓库需改为 `openEuler/{repo}`

    ```
    [lfs]
        url = https://artlfs.openeuler.openatom.cn/{org}/{repo}
    ```
  - 手动修改本地 fork 仓库 LFS URL 配置：添加初始 `.lfsconfig` 配置后，请参照 `向已启用社区 LFS 服务的官方仓库提交贡献` 部分修改本地 fork 仓库 LFS URL 配置，将本地 Git LFS 配置为向 `https://artlfs.openeuler.openatom.cn` **贡献者 fork 仓库对应目录**提交和获取文件

  - 如上配置后即可照常修改提交，若修改涉及 LFS 管理的文件则 git push 时需要输入 artlfs 用户名与口令，具体请参考后文 `权限认证` 部分

  - 添加 `.lfsconfig` 对应 PR 合入后，初次配置启用流程即告完成

### 权限认证

- 克隆或推送大文件时，可能会提示需要输入在 `https://artlfs.openeuler.openatom.cn` 的用户名与口令

  ```
  Username for 'https://artlfs.openeuler.openatom.cn': atomgit_username
  Password for 'https://atomgit_username@artlfs.openeuler.openatom.cn': atomgit_token
  ```

    - 用户名：输入您的 AtomGit 用户名 (如 @atomgit_username 中的 atomgit_username)
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

