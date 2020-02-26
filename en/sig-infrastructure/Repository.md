# Repository

## Maintenance

### Background

There are hundreds of repositories in openEuler community.
It is very difficult to maintain all of repositories and the members in every single repository.
An automatic tool is wanted to figure out these problems and save the team's workload.

### Solution

The infrastucture team have built a mechanism to simplify the repository maintenance.
The repositories and repository members about openEuler are addressed in
[openeuler.yaml](https://gitee.com/openeuler/infrastructure/blob/master/repository/openeuler.yaml),
meanwhile the repositories and repository members about src-openEuler are addressed
in [src-openeuler.yaml](https://gitee.com/openeuler/infrastructure/blob/master/repository/src-openeuler.yaml).
If the yaml files are changed by a pull request, the `openeuler-ci-bot` will detect these changes
and automatically do some actions like `create a repository`, `add members for a repository`,
`remove members from a repository`, `add protecting a branch`  and `remove protecting a branch`
based on the Gitee API.

### How to create a repository

``` yaml
repositories:
  - name: abattis-cantarell-fonts
    description: "fonts repo"
    type: private
```

If you want to add a new repository into openEuler community,
you can modify the [openeuler.yaml](https://gitee.com/openeuler/infrastructure/blob/master/repository/openeuler.yaml)
or [src-openeuler.yaml](https://gitee.com/openeuler/infrastructure/blob/master/repository/src-openeuler.yaml)
with a pull request with the above example.

* `abattis-cantarell-fonts`: the name of the new repository you want to create.
* `fonts repo`: the description of the new repository.
* `private`: this represents the repository type.

  `private` means the new repository is only visible for some specified people.

  `public` means the new repository is public for all of the pepple.

When your pull request is merged, the ```openeuler-ci-bot``` will create the new repository immediately.

### How to create or remove a member

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

If you want to add or remove a member in a repository,
you can modify the [openeuler.yaml](https://gitee.com/openeuler/infrastructure/blob/master/repository/openeuler.yaml)
or [src-openeuler.yaml](https://gitee.com/openeuler/infrastructure/blob/master/repository/src-openeuler.yaml)
with a pull request with the above example.

* `openeuler`: the name of the openEuler communtiy which has another name `src-openeuler`, actually it is no need to modify.
* `managers`:  the managers you want to specify under `community` or the `repositories`.
  The Gitee accounts are needed here, like `zhuchunyi`.
* `developers`:  the developers you want to specify under `community` or the `repositories`.
  The Gitee accounts are needed here, like `igorkorkin`.
* `viewers`:  the viewers you want to specify under `community` or the `repositories`.
  The Gitee accounts are needed here, like `jianminw`.

***NOTE***: you may find `managers`, `developers` and `viewers` are existing
under `community` or the `repositories` in the same time. Let's see the difference between them:

* Usually if you want to add or remove a manager, developer or viewer of all the repositories,
  you can modify the `managers`, `developers` and `viewers` under `community`.
* Specially if you want to add or remove a manager, developer or viewer of a specified repository,
  you can modify the `managers`, `developers` and `viewers` under the specified repository like `accountsservice`.
* If a repository does not specify any member(including `managers`, `developers` and `viewers`) like `abattis-cantarell-fonts`,
  the `openeuler-ci-bot` will use `managers`, `developers` and `viewers` under `community`
  to create members for this repository like `abattis-cantarell-fonts`.
* If a repository does specify some members(including `managers`, `developers` and `viewers`) like `accountsservice`,
  the `openeuler-ci-bot` will use `managers`, `developers` and `viewers` under the repository
  to create members like `accountsservice`.
* If a Gitee account is exsiting in `managers`, `developers` and `viewers`,
  this Gitee account will be as a manager, as the permisson in Gitee is like `managers` > `developers` > `viewers`.


### How to add or remove protecting a branch

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

If you want to add or remove protecting a branch in a repository,
you can modify the [openeuler.yaml](https://gitee.com/openeuler/infrastructure/blob/master/repository/openeuler.yaml)
or [src-openeuler.yaml](https://gitee.com/openeuler/infrastructure/blob/master/repository/src-openeuler.yaml)
with a pull request with the above example.

* `openeuler`: the name of the openEuler communtiy which has another name `src-openeuler`, actually it is no need to modify.
* `protected_branches`:  the branches to be protected you want to specify under `community` or the `repositories`.

***NOTE***: you may find `protected_branches` is existing under `community` or the `repositories` in the
same time. Let's see the difference between them:

* Usually if you want to add or remove protecting a branch of all the repositories,
  you can modify the `protected_branches` under `community`.
* Specially if you want to add or remove protecting a branch of a specified repository,
  you can modify the `protected_branches` under the specified repository like `accountsservice`.
* If a repository does not specify any protected branches like `abattis-cantarell-fonts`,
  the `openeuler-ci-bot` will use `protected_branches` under `community`
  to add protecting branches for this repository like `abattis-cantarell-fonts`.
* If a repository does specify some protected branches like `accountsservice`,
  the `openeuler-ci-bot` will use `protected_branches` under the repository
  to add protecting branches like `accountsservice`.
* If the branch specified in `protected_branches` dose not exist, `openeuler-ci-bot` will do
  nothing relevant.

### How to create or remove a maintainer beyond Gitee

Gitee provides manager, developer and viewer and so forth for the repository permission management.
`openeuler-ci-bot` supports another way to add maintainers for every repository.
`openeuler-ci-bot` will scan the `OWNERS` file under every repository to discovery the extra maintainers.

Take <https://gitee.com/openeuler/ci-bot/blob/master/OWNERS> under `ci-bot` as an example.
The file content is like below:

``` yaml
maintainers:
  - edisontest
  - freesky-edward
  - TommyLike
  - xiangxinyong
  - zerodefect
```

It means all of these five users have the permission to merge the pull request in the `ci-bot` repository.
These users can use `/lgtm` and `/approve` commands to trigger `openeuler-ci-bot` to merge the pull request.
You can find more bot commands from <https://gitee.com/openeuler/community/blob/master/en/command.md>
By the way, all of the managers and developers in Gitee can also use `/lgtm` and `/approve`.

If you want to keep maintainers beyond Gitee, please add the `OWNERS` file under your repository,
and add the maintainer into the `OWNERS` file, `openeuler-ci-bot` will grant the `merge` permission to these maintainers.
