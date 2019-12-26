#  OpenEuler社区命令参考文档

openEuler社区的所有项目都由Bot维护。 这意味着开发人员可以在每个Pull Request或Issue下面进行回复来触发Bot命令。 这些命令包括：

| 命令               | 示例                                  | 描述                                                         | 谁能使用                                                     |
| ------------------ | ------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| /check-cla         | /check-cla                            | 强制重新检查一个Pull Request的CLA状态。 如果Pull Request的作者已经签署CLA， 这个Pull Request将会新增一个名为`openeuler-cla/yes`的标签， 反之将会新增一个名为`openeuler-cla/no`的标签。 | 任何人                                                       |
| /lgtm [cancel]     | /lgtm /lgtm cancel                    | 为一个Pull Request添加或者删除`lgtm`标签，这个标签将用于Pull Request合入判断。 | 这个仓库的协作者。Pull Request能使用`/lgtm cancel`命令，但是不能使用`/lgtm`命令。 |
| /approve [cancel]  | /approve /approve cancel              | 为一个Pull Request添加或者删除`approved`标签，这个标签将用于Pull Request合入判断。 | 这个仓库的协作者。                                           |
| /[remove-]kind     | /kind bug /remove-kind bug            | 添加或者删除这种kind类型的标签。 例如：`kind/bug`标签。      | 任何人都能在一个Pull Request或者Issue上触发这种命令。        |
| /[remove-]priority | /priority high /remove-priority high  | 添加或者删除这种priority类型的标签。 例如：`priority/high`标签。 | 任何人都能在一个Pull Request或者Issue上触发这种命令。        |
| /[remove-]sig      | /sig kernel /remove-sig kernel        | 添加或者删除这种sig类型的标签。 例如：`sig/kernel`标签。     | 任何人都能在一个Pull Request或者Issue上触发这种命令。        |
| /close             | /close                                | 关闭一个Pull Request或者Issue。                              | 作者和仓库的协作者能触发这种命令。                           |
| /reopen            | /reopen                               | 重新打开一个Issue。                                          | 作者和仓库的协作者能触发这种命令。                           |
| /retest            | /retest                               | 重跑测试用例任务。                                           | 任何人都能在一个Pull Request上触发这种命令。                 |
| /assign [[@]...]   | /assign /assign @openeuler-ci-bot     | 分配一个Issue给负责人。                                      | 任何人都能在一个Issue上触发这种命令， 但是目标负责人必须是这个组织的一个成员。 如果没有指定目标负责人，这表明这个Issue会分配给自己。 |
| /unassign [[@]...] | /unassign /unassign @openeuler-ci-bot | 取消分配一个Issue给负责人。                                  | 任何人都能在一个Issue上触发这种命令， 但是目标负责人必须是这个组织的一个成员。 如果没有指定目标负责人，这表明这个Issue会取消分配给自己。 |