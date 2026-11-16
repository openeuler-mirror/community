# Repository Management

## Background

The `repository/` directory is no longer used and is kept only for compatibility. Repository configuration has moved to the `sig/` directory and is maintained by each SIG.

## Adding a Repository

- Community-maintained projects: create a YAML file at `sig/<SIG>/openeuler/<first-letter>/<repository>.yaml`.
- Introduced software packages: create a YAML file at `sig/<SIG>/src-openeuler/<first-letter>/<repository>.yaml`.

For the YAML format, see [sig/README.md](/sig/README.md). For the procedure, see [Adding a New Software Package](/en/contributors/create-package.md).

## Modifying Repository Configuration

1. Modify the repository YAML file in the corresponding SIG directory.
2. Submit a PR. The SIG maintainer and the Technical Committee review and merge it.
3. After the PR is merged, the bot creates the repository and configures members and protected branches based on the YAML file.

## Maintainers

Maintainer information is managed in the order `OWNERS` > `sig-info.yaml` > other configurations. For details, see [sig/README.md](/sig/README.md).
