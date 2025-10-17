## openEuler 开源社区标签

openEuler 开源社区所有的项目都有很多标签。
这些标签给予了 Issue 和 Pull Request 某些特定的含义。
这些标签包括：

### CLA

* openeuler-cla/yes: CLA检查通过，PR合入必要条件，表示此PR贡献者已经签署CLA协议
* openeuler-cla/no: CLA检查未通过，可以通过 `/check-cla` 命令再次检查是否满足CLA协议条件

### Kind

* kind/api-change: PR或者issue类型，可以通过 `/kind api-change` 添加 或 `/remove-kind api-change`移除该标签
* kind/bug: PR或者issue类型，可以通过 `/kind bug` 添加 或 `/remove-kind bug`移除该标签
* kind/cleanup: PR或者issue类型，可以通过 `/kind cleanup` 添加 或 `/remove-kind cleanup`移除该标签
* kind/design: PR或者issue类型，可以通过 `/kind design` 添加 或 `/remove-kind design`移除该标签
* kind/documentation: PR或者issue类型，可以通过 `/kind documentation` 添加 或 `/remove-kind documentation`移除该标签
* kind/failing-test: PR或者issue类型，可以通过 `/kind failing-test` 添加 或 `/remove-kind failing-test`移除该标签
* kind/feature: PR或者issue类型，可以通过 `/kind feature` 添加 或 `/remove-kind feature`移除该标签
* kind/enhancement: PR或者issue类型，可以通过 `/kind enhancement` 添加 或 `/remove-kind enhancement`移除该标签

### Priority

* priority/high： PR或者issue优先级，可以通过 `/priority high` 添加 或 `/remove-priority high`移除该标签
* priority/medium： PR或者issue优先级，可以通过 `/priority medium` 添加 或 `/remove-priority medium`移除该标签
* priority/low： PR或者issue优先级，可以通过 `/priority low` 添加 或 `/remove-priority low`移除该标签

### merge
* stats/needs-squash: 提示类型标签，提示SIG成员是否需要通过 squash 方式合入
* merge/squash: PR以squash方式合入，可以通过 `/squash` 添加 或 `/squash cancel`移除该标签
* merge/rebase: PR以rebase方式合入，可以通过 `/rebase` 添加 或 `/rebase cancel`移除该标签


### Sig

sig标签，表示该PR或者issue分属那个SIG组
* sig/kernel
* sig/driver
* sig/testing
* sig/release
* sig/doc
* sig/api
* ...

### CI

* lgtm："Look good to me", PR合入必要条件, 表示SIG组成员检视通过, SIG组成员可以通过 `/lgtm` 添加 或 `/lgtm cancel`移除该标签
* approved:  PR合入必要条件, 表示SIG组成员检视通过, SIG组成员可以通过 `/approve ` 添加 或 `/approve cancel`移除该标签
* ci_successful: 门禁运行成功，部分仓PR合入必要条件(仓库名单可配中)
* ci_processing: 门禁运行中
* ci_failed: 门禁运行失败
* wait_confirm: community仓特有，表示待SIG成员确认

### Others

* duplicate: 平台默认标签，表示PR或issue重复的
* help-wanted: 平台默认标签，表示寻求帮助
* invalid: 平台默认标签，表示无效的PR或者issue
* question: 平台默认标签，表示此issue为一个问题
* wontfix: 平台默认标签，表示不修复
* newcomer: 第一次在社区提pr 或 issue
