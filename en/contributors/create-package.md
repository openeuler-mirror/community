# Adding a New Software Package

> Note: openEuler currently uses AtomGit as its code hosting platform. The UI, domain names, and commands in this document use AtomGit as an example.

Perform the following steps to add a software package to the code hosting platform and create the corresponding project in EulerMaker.

- [Procedure](#procedure)
  - [Method 1: Create a repository by submitting an issue (recommended)](#method-1-create-a-repository-by-submitting-an-issue-recommended)
  - [Method 2: Create a repository by forking the repository and submitting a PR](#method-2-create-a-repository-by-forking-the-repository-and-submitting-a-pr)

## Procedure

You can add a software package in either of the following ways. Method 1 is recommended. The community bot automatically generates a repository creation PR, which simplifies the procedure.

### Method 1: Create a repository by submitting an issue (recommended)

Submit a "repository creation" issue in the community repository. The community bot automatically parses the issue and generates a repository creation PR. Developers do not need to fork the repository or manually edit configuration files.

**Procedure:**

1. Go to the issue creation page of the community repository: [https://atomgit.com/openeuler/community/issues](https://atomgit.com/openeuler/community/issues). Click **New Issue** and select the repository creation template.

2. Fill in the following fields as prompted. The issue title automatically starts with a fixed prefix. Do not delete the prefix.

   | Field | Required | Description |
   |-------|----------|-------------|
   | Repository name | Yes | Only lowercase letters, digits, and hyphens are supported, for example, `my-package`. |
   | Repository organization | Yes | `openeuler` (community-maintained projects) or `src-openeuler` (introduced artifact repositories). |
   | Upstream repository URL | Conditionally required | Required when the organization is `src-openeuler`. Example: `https://atomgit.com/org/repo` or `https://github.com/org/repo`. |
   | Repository description | Yes | Brief description of the repository. |
   | Default branch name | Yes | Defaults to `master`. |
   | Repository type | Yes | `public` or `private`. |
   | Branch protection configuration | No | Other branches to be created and protected, one per line. Format: `branch:source branch:protection type`, for example, `openEuler-24.03-LTS-Next:master:protected`. |
   | SIG | Yes | Name of the SIG to which the software package belongs, for example, `Base-service`. |

3. After the issue is submitted, the bot automatically monitors and processes it:

   - **Parsing and validation**: The bot parses the issue content and validates the fields. If validation fails, the bot comments on the issue with the specific error.
   - **Automatic PR generation**: After validation is successful, the bot automatically creates a repository creation PR in the community repository. The PR contains the YAML configuration file of the new repository, and the PR description links to the source issue for traceability.
   - **Result feedback**: After the PR is created, the bot comments on the issue with the PR link. Developers can then follow the PR approval process.

4. If validation or PR creation fails, modify the issue content according to the bot's comment and comment `/retrigger` on the issue to trigger the bot to run the repository creation process again.

5. After the PR is reviewed and merged by the SIG maintainers and the Technical Committee, a repository with the same name is automatically created, and the corresponding project is created in EulerMaker: [https://build.openeuler.org/project/show/openEuler:Factory](https://build.openeuler.org/project/show/openEuler:Factory).

### Method 2: Create a repository by forking the repository and submitting a PR

To add a software package by modifying the openeuler/community repository on the code hosting platform, perform the following steps:

1. Go to the [community repository](https://atomgit.com/openeuler/community.git) and fork it to your own repository.

2. Clone the forked community repository to the local host.

  ```
  git clone https://atomgit.com/"$username"/community.git
  ```

3. Modify the community repository. The following describes how to add the **zip** software package to the code hosting platform and add the package to the **openEuler:Factory** project.

   * cd community/sig

   * Find the SIG to which the software package belongs. For example, the **zip** package belongs to the Base-service SIG. (See the *Contributor Guide* to find the SIG or project that you are interested in.)

   * Modify the contents in the corresponding subfolder of the **sig** folder, such as the project list.

   * Modify the **sig-info.yaml** file of the corresponding SIG in the **sig** folder and add the software package in the form of **- src-openeuler/zip**. The following uses the **zip** software package as an example to describe how to modify **sig/Base-service/sig-info.yaml**:

   ```yaml
        repositories:
        - repo:
          - openeuler/openEuler-rpm-config
          - src-openeuler/abseil-cpp
          - src-openeuler/acl
          - src-openeuler/acpica-tools
          - src-openeuler/adcli
          - src-openeuler/aide
          - src-openeuler/airline

         ...

          - src-openeuler/jansson
          - src-openeuler/apr
          - src-openeuler/python-lxml
          - src-openeuler/zip
   ```

   * Create the repository: Add the corresponding YAML file to **sig/***{sig_directory}***/src-openeuler/***initial_letter_of_the_software_name*. (For projects maintained by the openEuler community, use the **openeuler** directory. For packages introduced from other communities, use the **src-openeuler** directory. Example: **sig/Base-service/src-openeuler/z/zip.yaml**.)

      ```yaml
      name: pkgname
      description: about pkgname
      upstream: https://somepkg.org/
      branches:
      - name: master
        type: protected
      type: public
      ```

   * Submit a PR. For details, see the [Pull Request Submission Guide](pull-request.md). After the PR is merged, a repository with the same name is created in [src-openeuler](https://atomgit.com/src-openeuler) on the code hosting platform, and the corresponding project is created in EulerMaker: [https://build.openeuler.org/project/show/openEuler:Factory](https://build.openeuler.org/project/show/openEuler:Factory).
