## openEuler Community Label

There are lots of labels for all of the projects in openEuler Community.
These labels represent meaningful description in the Issue or Pull Request.
The labels incluing as follows:

### CLA

* openeuler-cla/yes: The CLA check has passed, which is a requirement for merging this PR. This indicates that the contributor has signed the CLA (Contributor License Agreement).
* openeuler-cla/no: CLA check failed. You can use the `/check-cla` command to re-run the verification and confirm whether the contributor meets the CLA (Contributor License Agreement) requirements.

### Kind

* kind/api-change：For PR or issue, you can add it using `/kind api-change` or remove it with `/remove-kind api-change`.
* kind/bug：For PR or issue, you can add it using `/kind bug` or remove it with `/remove-kind bug`.
* kind/cleanup：For PR or issue, you can add it using `/kind cleanup` or remove it with `/remove-kind cleanup`.
* kind/design：For PR or issue, you can add it using `/kind design` or remove it with `/remove-kind design`.
* kind/documentation：For PR or issue, you can add it using `/kind documentation` or remove it with `/remove-kind documentation`.
* kind/failing-test：For PR or issue, you can add it using `/kind failing-test` or remove it with `/remove-kind failing-test`.
* kind/feature：For PR or issue, you can add it using `/kind feature` or remove it with `/remove-kind feature`.
* kind/enhancement：For PR or issue, you can add it using `/kind enhancement` or remove it with `/remove-kind enhancement`.

### Priority

* priority/high: For PR or issue priority levels, you can add it using `/priority high` or remove it with `/remove-priority high`.
* priority/medium: For PR or issue priority levels, you can add it using `/priority medium` or remove it with `/remove-priority medium`.
* priority/low: For PR or issue priority levels, you can add it using `/priority low` or remove it with `/remove-priority low`.

### merge
* stats/needs-squash: Prompt-type label indicating SIG members should evaluate whether the PR requires squash merging.
* merge/squash: Activates squash merge method. Apply via `/squash`, remove via `/squash cancel`.
* merge/rebase: Activates rebase merge method. Apply via `/rebase`, remove via `/rebase cancel`.

### Sig

SIG labels, Indicate which SIG group the PR or issue belongs to. 

* sig/kernel
* sig/driver
* sig/testing
* sig/release
* sig/doc
* sig/api

### CI

* lgtm: Required for merge (indicates SIG member approval). Apply via `/lgtm`, remove via `/lgtm cancel`.
* approved: Required for merge (indicates SIG member approval). Apply via `/approve`, remove via `/approve` cancel.
* ci_successful: CI validation passed. Merge prerequisite for configured repositories.
* ci_processing: CI validation in progress.
* ci_failed: CI validation failed.
* wait_confirm: (Community repos only) Awaiting SIG member confirmation.

### Others

* duplicate: Indicates the PR or issue is a duplicate (platform default label).
* help-wanted: Indicates assistance is requested (platform default label).
* invalid: Indicates an invalid PR or issue (platform default label).
* question: Indicates the issue is a question (platform default label).
* wontfix: Indicates no fix will be applied (platform default label).
* newcomer: Indicates the contributor's first PR/issue in the community.

