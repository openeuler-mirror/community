# openEuler Repository Management Guide

The openEuler project uses AtomGit to manage teams and code. This guide describes how to operate these organizations based on openEuler community guidelines.

## Service Commitment

The platform management team will make every effort to provide the following service levels:

- New organization creation requests are processed within 72 hours after all membership requirements are met.
- Repository creation or migration requests receive a response within 72 hours after the PR is submitted. The requester may need to provide additional information. Once all conditions are met, the platform management team will complete the repository processing within 72 hours.
- PRs receive a response within 72 hours. The time required to resolve an issue depends on the specific situation.

For urgent requests, contact the [openEuler Infrastructure Team](<mailto:infra@openeuler.org>) for help.

## openEuler Organizations

- [openEuler][atomgit-openeuler]: stores source code projects.
- [src-openEuler][atomgit-src-openeuler]: stores software packages required for building releases.

## Moving External Code to openEuler Organizations

Due to open source license and CLA requirements, some investigation is required before software packages or code are moved to openEuler management. Submit an application to the [Technical Committee](/en/technical-committee/README.md) first.

## Team Guidance

### Team Roles, Permissions, and Configuration

### Process

- To create a team or project, submit an application to the Technical Committee. For details, see [How to Apply for a SIG](/en/technical-committee/governance/README.md).
- To add a new member to a team, submit a PR to modify the `OWNERS` file of the project under [SIG](/sig). The PR can be approved by the team maintainer.

## Repository Usage Guide

Repositories also have License and CLA requirements. For details, see the openEuler project template.

### Creating a Repository

The `repository/` directory is deprecated. Create a YAML file under the corresponding SIG directory:

- Community-maintained projects: `sig/<SIG>/openeuler/<first-letter>/<repository>.yaml`
- Introduced software packages: `sig/<SIG>/src-openeuler/<first-letter>/<repository>.yaml`

For the format and procedure, see [Repository Management](./Repository.md), [sig/README.md](/sig/README.md), and [Adding a New Software Package](/en/contributors/create-package.md).

### Deleting a Repository

To be supplemented.

[atomgit-openeuler]: https://atomgit.com/openeuler
[atomgit-src-openeuler]: https://atomgit.com/src-openeuler
