## openEuler Community Labels

The openEuler Community uses a variety of labels across its projects. These labels provide meaningful context for Issues and Pull Requests (PRs). 
Categories include:

### CLA

* openeuler-cla/yes: CLA check passed. Required for merging the PR. Indicates the contributor has signed the Contributor License Agreement (CLA). 
* openeuler-cla/no: CLA check failed. Use `/check-cla` to re-run verification and confirm CLA compliance.

### Kind

* kind/api-change: For a PR or Issue, you can add it using `/kind api-change` or remove it with `/remove-kind api-change`.
* kind/bug: For a PR or Issue, you can add it using `/kind bug` or remove it with `/remove-kind bug`.
* kind/cleanup: For a PR or Issue, you can add it using `/kind cleanup` or remove it with `/remove-kind cleanup`.
* kind/design: For a PR or Issue, you can add it using `/kind design` or remove it with `/remove-kind design`.
* kind/documentation: For a PR or Issue, you can add it using `/kind documentation` or remove it with `/remove-kind documentation`.
* kind/failing-test: For a PR or Issue, you can add it using `/kind failing-test` or remove it with `/remove-kind failing-test`.
* kind/feature: For a PR or Issue, you can add it using `/kind feature` or remove it with `/remove-kind feature`.
* kind/enhancement: For a PR or Issue, you can add it using `/kind enhancement` or remove it with `/remove-kind enhancement`.

### Priority

* priority/high: PR or Issue priority. You can add it using `/priority high` or remove it with `/remove-priority high`.
* priority/medium: PR or Issue priority. You can add it using `/priority medium` or remove it with `/remove-priority medium`.
* priority/low: PR or Issue priority. You can add it using `/priority low` or remove it with `/remove-priority low`.

### merge
* stats/needs-squash: Suggests SIG members evaluate if squash merging is needed.
* merge/squash: Enables squash merge. Use `/squash` to apply, `/squash cancel` to remove.
* merge/rebase: Enables rebase merge. Use `/rebase` to apply, `/rebase cancel` to remove.

### Sig

SIG label, indicating the SIG group associated with the PR or issue. 

* sig/kernel
* sig/driver
* sig/testing
* sig/release
* sig/doc
* sig/api

### CI

* lgtm: Required for merge (indicates SIG member approval). Use `/lgtm` to apply, `/lgtm cancel` to remove.
* approved: Required for merge (indicates SIG member approval). Use `/approve` to apply, `/approve` to remove.
* ci_successful: CI check passed. Required for merge.
* ci_processing: CI check in progress.
* ci_failed: CI check failed.
* wait_confirm: (Community repos only) Awaiting SIG member confirmation.

### Others

* duplicate: Indicates a duplicate PR or Issue (platform default label).
* help-wanted: Indicates a request for assistance (platform default label).
* invalid: Indicates an invalid PR or Issue (platform default label).
* question: Indicates an inquiry-type Issue (platform default label).
* wontfix: Indicates no fix will be applied (platform default label).
* newcomer: Indicates the contributor's first PR/Issue in the community.

