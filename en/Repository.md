# Repository

## Maintenance

### Background

There are hundreds of repositories in openEuler community.
It is very difficult to maintain all of repositories and the members in every single repository.
An automatic tool is wanted to figure out these problems and save the team's workload.

### Solution

The infrastucture team have built a mechanism to simplify the repository maintenance.
All of the repositories and repository members are addressed in
[one yaml file](https://gitee.com/openeuler/infrastructure/blob/master/repository/projects.yaml) of the infrastructure repository.
If this yaml file is changed by a pull request, the ```openeuler-ci-bot``` will detect these changes
and automatically do some actions like ```create a repository```, ```add members for a repository```
and ```remove members from a repository``` based on the Gitee API.

### How to create a repository

``` yaml
repositories:
  - name: abattis-cantarell-fonts
    description: "fonts repo"
    type: private
```

If you want to add a new repository into openEuler community,
you can modify the [yaml file](https://gitee.com/openeuler/infrastructure/blob/master/repository/projects.yaml)
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
you can also modify the [yaml file](https://gitee.com/openeuler/infrastructure/blob/master/repository/projects.yaml)
with a pull request with the above example.

* `openeuler`: the name of the openEuler communtiy, actually it is no need to modify.
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
  the ```openeuler-ci-bot``` will use `managers`, `developers` and `viewers` under `community`
  to create members for this repository like `abattis-cantarell-fonts`.
* If a repository does specify some members(including `managers`, `developers` and `viewers`) like `accountsservice`,
  the ```openeuler-ci-bot``` will use `managers`, `developers` and `viewers` under the repository
  to create members like `accountsservice`.
* If a Gitee account is exsiting in `managers`, `developers` and `viewers`,
  this Gitee account will be as a manager, as the permisson in Gitee is like `managers` > `developers` > `viewers`.
