

### 1.从云上folk

1. 访问 https://gitee.com/openEuler/openEuler
2. 点击右上角的 `Fork` 按钮建立一个属于自己的云上folk分支

### 2.把folk分支复制到本地

请按照以下的复制过程将openEuler的代码下载到您的在计算机上。

定义本地工作目录：

```
# If your PATH has multiple paths, pick
# just one and use it instead of $PATH here.
# You must follow exactly this pattern,
# neither `$PATH/src/gitee.com/${your gitee profile name/`
# nor any other pattern will work.
export working_dir=$PATH/src/XXXXXX
```

> 如果你已经在openEuler上做过开发， `XXX`会成为您现有的`gitee.com` 目录的子目录.

把git上的 `user` 设置成您gitee的个人名称：

```
export user={your gitee profile name}
```

`$working_dir` and `$user` 都需要按照上面的要求完成配置



创建您的分支:

```
mkdir -p $working_dir
cd $working_dir
git clone https://gitee.com/$user/openEuler.git
# or: git clone git@gitee.com:$user/openEuler.git

cd $working_dir/openEuler
git remote add upstream https://gitee.com/kubernetes/openEuler.git
# or: git remote add upstream git@gitee.com:openEuler/openEuler.git

# Never push to upstream master
git remote set-url --push upstream no_push

# Confirm that your remotes make sense:
git remote -v
```

### 3.拉分支

更新您的本地分支

```
cd $working_dir/openEuler
git fetch upstream
git checkout master
git rebase upstream/master
```

从这里拉分支:

```
git checkout -b myfeature
```

然后在 `myfeature` 分支上编辑和修改代码。

#### 构建

具体的构建请参考：[《开发指南》]()



### 4.保持您的分支和master的同步

```
# While on your myfeature branch
git fetch upstream
git rebase upstream/master
```

执行merge的时候，请不要使用 `git pull` 替代上面的 `fetch` / `rebase`. `git pull` 。因为这种方式会使提交历史变得混乱，并使代码更难被理解。您也可以通过更改文件来达到目的， `.git/config` 文件通过 `git config branch.autoSetupRebase always` 去改变 `git pull`的行为。

### 5 提交

提交您的更改。

```
git commit
```

您可能会回来继续编辑构建并测试更多内容，可以使用 `commit --amend` 继续添加提交。



### 6 推送

准备进行审查（或只是建立工作的异地备份）时，将分支推到你在`gitee.com`的folk:

```
git push -f ${your_remote_name} myfeature
```



### 7 创建一个 pull request

1. 访问你在 `https://gitee.com/$user/openEuler`
2. 在您的 `myfeature` 分支上点击`Compare & Pull Request` .
3. 可以查看[pull-request](pull-request)获得更多的建议.

*如果您具有上游写访问权*，请不要使用Gitee UI创建PR，因为Gitee会在主存储库而不是您的fork中创建PR分支。

#### 获取代码审查

#### 查看代码检视

你提交PR申请后，PR被分配给一个或多个检视者。这些检视者将进行彻底的代码检视。

小的PR很容易检视。量级较大的PR很难被正确的检视。

#### Squash and Merge

Upon merge (by either you or your reviewer), all commits left on the review branch should represent meaningful milestones or units of work. Use commits to add clarity to the development and review process.

Before merging a PR, squash any *fix review feedback*, *typo*, *merged*, and *rebased* sorts of commits.

It is not imperative that every commit in a PR compile and pass tests independently, but it is worth striving for.

In particular, if you happened to have used `git merge` and have merge commits, please squash those away: they do not meet the above test.

A nifty way to manage the commits in your PR is to do an [interactive rebase](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History), which will let you tell git what to do with every commit:

```
git fetch upstream
git rebase -i upstream/master
```

For mass automated fixups (e.g. automated doc formatting), use one or more commits for the changes to tooling and a final commit to apply the fixup en masse. This makes reviews easier.

### 回退一个提交

如果你想回退提交，请采用下面的方式

*如果您具有上游写访问权限*，请不要使用`Revert`Gitee UI中的 按钮创建PR，因为Gitee会在主存储库而不是您的fork中创建PR分支。

- 创建一个分支并用upstream进行同步

  ```
  # create a branch
  git checkout -b myrevert
  
  # sync the branch with upstream
  git fetch upstream
  git rebase upstream/master
  ```

- 如果您希望还原的提交是:

  - **merge commit:**

    ```
    # SHA is the hash of the merge commit you wish to revert
    git revert -m 1 SHA
    ```

  - **single commit:**

    ```
    # SHA is the hash of the single commit you wish to revert
    git revert SHA
    ```

- 这将创建一个新的提交以回退到更新前。 push这次提交到远程工作目录

```
git push ${your_remote_name} myrevert
```

- 用这个分支创建一个PR.