# openEuler Packaging Guide



**Contributing to This Guide**

You can contribute to this guide by submitting an issue or PR on the Gitee repository. Both forms of contribution are highly appreciated and welcome.

RPM packages are important for Linux distributions. According to @myeuler, making yourself an expert in Linux is similar to preparing yourself for becoming a great chef. The first step is to get familiar with and identify various foodstuffs, be able to prepare food, and identify the taste of various dishes. The same thing goes for building RPM packages. Only when you are familiar with the structure and content of RPM packages and the dependencies between them, can you lay a solid foundation for becoming an OS expert.

This document describes how to make an RPM package. The detailed rules for building RPM packages are described in different specifications and will be updated and optimized continuously.

## Packaging Software

Creating an RPM package, also called packaging, refers to the task of compiling and binding software and metadata, such as the full name of the software, description, and dependency list required for normal running. This is to allow software users to install, remove, or upgrade the software comfortably using a package manager.

### Packaging Rules

openEuler tries to normalize a variety of open source projects into a coherent system. This packaging guide is drafted to standardize RPM building.

- openEuler complies with the [Linux Standard Base (LSB)](http://www.linuxbase.org/). This standard base aims to reduce the differences between distributions.
- openEuler also complies with the [Filesystem Hierarchy Standard (FHS)](http://www.pathname.com/fhs/). This standard is a reference on how to manage the Linux filesystem hierarchy.
- In addition to following these general rules for Linux distributions, this document standardizes the actual details of packaging for the openEuler community edition.

### Packaging Basics

Before using this document to create the RPM and SPEC files, you are advised to familiarize yourself with the following knowledge. The first two items are necessary for creating a high-quality software package, and the last two items are helpful for participating in openEuler contributions.

|      | Skill                                                        |      | Reference                                                        |
| :--: | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
|  1   | RPM software package management (including software installation, upgrade, uninstallation, compilation, and building)         | Mandatory| [RPM's official website](https://rpm.org)                                  |
|  2   | Official RPM packaging guide                                             | Mandatory| [RPM Packaging Guide](https://rpm-packaging-guide.github.io/)|
|  3   | Using the Open Build Service (OBS). openEuler uses OBS to build releases.| Optional| [RPM Packaging Guide](https://rpm-packaging-guide.github.io/)|
|  4   | Gitee routine operations (openEuler code is hosted at gitee.com/openEuler.)    | Optional| [Gitee Support Center](https://gitee.com/help#article-header0)|

### Related Document

If you want to introduce software into the openEuler official software repository, refer to the [Contribution Guide](https://www.openeuler.org/en/community/contribution/detail.html).

### Applicability

Generally, these guidelines apply to all versions of openEuler, including LTS versions, non-LTS versions, and development versions.

The guidelines also cover, to some extent, all types and delivery scenarios of software packages entering openEuler. openEuler is a community edition. Therefore, it cannot be ensured that all rules remain unchanged. Currently, the core and most important principles of openEuler will not change greatly in the foreseeable future.

### Document Conventions

We do not have mandatory requirements on the advice and recommendations for packaging.

However, if the word "must" or "rule" is used, the packaging can deviate from the specific rule only after being reviewed by the Technical Committee (TC).

## Packaging Rules

Each OS has its own system. Besides different technical roadmaps and milestones, the software packages in the OSs are organized in different ways.

The main differences are as follows:

1. Different package managers (Fedora and openSUSE use RPM, and Debian uses DEB).
2. Different software package lists, including different software versions, that are maintained.
3. Different rules for splitting independent software packages.
4. Software dependency diagram formed based on different splitting rules.

### Software Package Manager

openEuler uses RPM as the base, together with DNF and Yum, to manage software packages. In the near future, if tools such as RPM cannot meet requirements, openEuler will consider initiating new projects.

### Software List and Selection

openEuler has its own software list. Currently, more than 2,000 software packages have been integrated and more software packages will be added and improved.

The source code of openEuler software packages is obtained from the stable versions of the native software community. The SPEC file is compiled based on the packaging specifications in this guide to package and integrate the software.

openEuler complies with the Upstream First principle.

### Software Splitting Rules

Different from other OS distributions, in which the software is split into the main, libs, devel, static, langpack, and doc packages, the openEuler software package is split into five RPM packages: main, libs, devel, static, and help (optional). However, for many simple software, the libs, devel, and main packages are merged to keep the package simple and easy to understand. If the software is split into too many packages, subsequent update and maintenance will be difficult and the dependencies will be sophisticated. However, if there is special and sophisticated software, more fine-grained splitting can be considered.

Common software package splitting:

| Category    | Package Name            | Content                                                    | Key Point                                                      |
| -------- | ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Main package    | The name is the same as that of the software source code package.| 1. Commands, configurations, and .so files required for running commands contained in the software<br>2. License, copyrights (if copyright information is included), Author, and Readme<br>3. Legal affairs-related files such as copyrights, licenses, and rights holders in the **licenses** directory.<br>4. man/info manuals| Use **Provides** and **Obsoletes** to state compatibility with other OSs.<br>(For details about **Provides**, **Conflicts**, and **Obsoletes**, see the official RPM manual.)|
| libs package  | *Software-package-name***-libs**   | Dynamic libraries and commands provided for external systems                             | Separate its own functions from the capabilities provided for external systems to ensure that upper-layer applications depend only on libs, reducing complex dependencies between software packages and avoiding cyclic dependency.|
| devel package | *Software-package-name***-devel**  | 1. Header file<br>2. Example<br>3. tests<br>4. Other content used for development| 1. Package all content within the development scope into a devel package.<br>2. If the dynamic libraries are packaged into the main package, the devel package must depend on (**Requires**) the main package. Otherwise, some dynamic libraries cannot be found.|
| static package| *Software-package-name***-static** | 1. *Static-library***.a**<br>2. Static version of the provided commands                    | If the static version is provided, it is necessary to use macros to control whether to compile and package the static version.|
| help package  | *Software-package-name***-help**   | Documents that describe interface functions and are used for secondary development                            | **Generally, this package is not mandatory. It is necessary to split documentation only when there are a large amount of contents.**|

For sophisticated software packages, special scenarios need to be considered based on the preceding categories:

| Category                                                        | Package Name                                                    | Content                                            |
| ------------------------------------------------------------ | -------------------------------------------------------- | ---------------------------------------------------- |
| for-language packages: They provide interfaces for multiple languages.            | Example: **python2-***software-package-name*, **python3-***software-package-name*, **perl-***software-package-name*| Split language support packages for Perl, Python 2, Python 3, and more.|
| lang packages: They are required for software involving localization and internationalization. For simple packages, there is no need to split lang packages.| Example: *Software-package-name-lang*                                     | Content related to internationalization, such as localization, language support, and time zone.      |
| Other sophisticated and special packages (such as gcc, python2, and python3)                 | Example: **openssh-server**, **openssh-client**                    |                                                      |

### Software Dependency Graph Based on Different Splitting Rules

Generally, based on new software splitting rules, the OS dependency graph is formed naturally, and the dependencies between software change accordingly.

RPM keywords such as **Provides**, **Conflicts**, and **Obsoletes** can be used to solve compatibility issues. openEuler exports the functions (**Symbols**) provided by the software, and then uses methods such as **Provides** and **Obsoletes** to ensure that the software is compatible with other OSs to some extent.

## 2. Verifying Software Packaging

Perform the verification from the following aspects:

- Different software lists and software selection.

- Independent software splitting rules.

- Software dependency graph based on different splitting rules.

1. Use rpmlint to check whether the SPEC file is correct and whether the corresponding RPM package can be built.

2. Check whether the software package splitting is proper and meets the openEuler software package splitting rules.

3. Run the **rpm --provides** and **rpm --requires** commands to check whether **Provides** and **Requires** of the binary RPM are correct. Ensure that the software package capability is correctly provided.

4. Check whether the binary package can be correctly installed, uninstalled, upgraded, and rolled back by running the **rpm** command.

5. After the installation and upgrade, (1) For services, verify the start, stop, restart, and reload functions; (2) For commands, at least verify that the basic functions are available.

6. The software package source code contains tests, which cannot be commented out, removed, or disabled randomly. Ensure that the make check test of the quality gate is passed when the code is submitted.

7. Perform integration tests especially after a software selection is upgraded, because it is difficult to determine the impact on other software packages independently.

## 3. Packaging Specifications

Rules and regulations are gradually improved. Comply with the existing rules as follows.

### Credible Source

- Do not embed precompiled binary files or library files. All binary files or library files contained in a software package must be compiled from the source code package. Binary files for firmware can be exempted. If certain binary files need to be introduced, the TC shall discuss and determine whether to introduce the binary files.
- Avoid bundling multiple, separate, and upstream projects into one software package. Try to ensure that one software package comes from one community.
- The software **should be** open source software. Visit https://opensource.org/osd.html for the open source definition. If the software is not open source software, the TC shall discuss and determine whether to use the software.
- Integrate open source software without legal risks. See the [licenses](https://opensource.org/licenses/alphabetical) approved by the Open Source Initiative (OSI).
- Adapt the SPEC file to openEuler and make it correct, accurate, clear, and concise. If the content is referenced from other distributions or from the native community, state the fact at the very beginning.
- **Do not** introduce the **blocklisted** software.
- Take the introduction decision of each piece of software as a case and use such case as a reference for subsequent decision-making on similar software introduction. The Technical Committee (TC) is responsible for the consistency of software introduction principles.

### Architecture Support

- Try to compile the package on different architectures such as AArch64 and x86_64. With the support of openEuler for other architectures, more build requirements may be added.
- Use the `%ifarch` macro to control the content closely related to the architecture.
- Build a noarch package for architecture-independent content, such as manuals, perl, python, and other interpreted language programs.
- Use `ExcludeArch:` or `ExclusiveArch:` to exclude the unsupported architecture.

### Software Splitting

- Comply with the openEuler software splitting rules.
- Do not disable the generation of debuginfo, except in special cases.
- You are not advised to split the man and info manuals into independent help subpackages unless the subpackages contain more sophisticated or diversified contents.
- You are advised to split the addon, plugins, modules, extensions, and components packages into independent subpackages to ensure the simplicity of the main package.
- If a minimal version needs to be provided, you are advised to split it into a subpackage, for example, bash-minimal. You are advised to use a macro to control minimal build and enable it by default.

### Naming Rules

- In principle, integrate only one version of software to openEuler, and keep the main package name the same as the software name. If multiple versions need to be introduced, use a version number suffix (for example, **openssl1.0f**) or a descriptive suffix (**-stable**) in the package name upon TC's approval.

- Name a language-specific module with a language prefix. For example, python-systemd, python3-systemd, and perl-systemd.

- Generally, the software package name comes from the native community. It is a meaningful English character string and case sensitive. If there are multiple words, you are advised to use hyphens (`-`) to separate them instead of underscores (`_`), periods (`.`), and plus signs (`+`). Exceptions include the following: Some software packages have the same name as that of other software packages, such as nss_db and sg3_utils; or the name of the native software contains special characters.

- Use clear and complete names for patches. Generally, you are advised to refer to the following requirements to ensure unified traceability:

    a. All new patches end with .patch, and their sources and functions are marked with comments in the format of *PATCH-(BUGFIX|CVE|FEATURE)-content*.

    b. Other Bugzillas can be referenced using abbreviations such as **CVE-2009-0067**, **GCC#123456**, **kde#123456**, and **rh#123456**.

    c. The patch file name does not need to be prefixed with a specific string, for example, **backport-** or **upstream-**.

    d. The sequence numbers of patches in the SPEC file must start from 0 and be consecutive.


### Basic Information

- Enter basic information, such as name, group, summary, and description, in the SPEC file based on the information on the official website. Use standard written language to describe or write the information and avoid words such as like and good/best.
- In the RPM-based upgrade scenario, the rule for comparing software versions is **epoch:version-release**. The priority of **epoch** is higher than that of **version** and **release**. In normal cases, **epoch** in the SPEC file is specified by the version by default. You do not need to specify it. In the following scenarios, you need to use **epoch** to ensure that the software can be upgraded using Yum: a. If **version** and **release** of a piece of software are downgraded or rolled back due to special reasons, **epoch** needs to be increased based on the original one. b. Different branches have different development progresses. For example, the **version** and **release** of the maintenance branch are later than those of the development branch. To ensure that the maintenance branch can be upgraded to the development branch, the **epoch** of the development branch must be later than that of the maintenance branch.
- The **version** in the SPEC file must be the same as that in the upstream community. The **version** information in the SPEC file of an aggregated software package (a repository contains source code from multiple upstream communities) is determined by the maintainer based on the community conventions. For example, [xorg-x11-font-utils](https://gitee.com/src-openeuler/xorg-x11-font-utils). The **release** number identifies the number of releases of openEuler based on the upstream community. When the software package **version** is upgraded and released for the first time, the **release** number starts from 1 and increments subsequently.

### Formats

- All SPEC files must be legible and maintained in a way that the packager can understand and use them.
- Use spaces for both indentation and alignment.
- Summarize multiple compilation or installation dependencies into one to three lines to make it concise.
- You do not need to pay attention to the encoding of the SPEC file unless you need to use characters other than those in the ASCII table. If you do need to use non-ASCII characters, save your SPEC file in UTF-8 format.
- The changelog complies with a specific format. A typical format is as follows:

```SPEC
* Tue Apr 7 2020 openEuler Buildteam <buildteam@openeuler.org> - 10.33-3
- Type:CVES/Bugfix/Feature
- ID:CVE-2019-20454
- SUG:NA
- DESC:fix CVE-2019-20454
```

### Dependencies

- Ensure that the compilation and installation dependencies of the software package exist in the openEuler repository. If not, package and import them.
- Check that the compilation and installation dependencies are complete. After the dependencies are installed in the openEuler OS, ensure that rpmbuild can normally build packages.
- Avoid cyclic dependency.
- Try to get rid of dependencies on files and commands, which make things complicated.

- -Specify the dependency on the main package, including the version number and release number, for the devel package or other subpackages. Otherwise, the single package can be upgraded separately, causing compatibility problems.
- Use `Requires` to specify dependencies required by the software to work properly. If the software package still functions properly without certain dependencies, you are advised to use `Recommends` or `Suggests` to specify those dependencies. If the dependencies are used to supplement integrity and enhance features, such as plugins and addon, you are advised to use `Supplements` or `Enhances` to specify them. For details about the usage differences, see the RPM documentation.
- The dependencies in special formats, such as `pkgconfig(foo)`, `dist(foo)`, `perl(strict)`, must be unified.

### Application of Macros

- Use `with_python2` to control a Python module provided by the software package that supports both Python 2 and Python 3.
- Use macros instead of hardcoding to compile the SPEC file. You can run the **rpm --showrc** command to query the supported macros. If you want to add macros, you can notify the packaging owner. We will try our best to keep the SPEC file concise and elegant.
  - Including but not limited to `%{name}`, `%{buildroot}`, and `%{_bindir}` built in rpmbuild.
  - Preferentially try to abstract a common operation into a public macro and report it to the package management committee.

### Compilation and Build

- If not necessary, you can use `autosetup` in the template to apply a patch, instead of running the `patch` command.
- Consider using `%exclude` in the `%files` section to exclude unnecessary files instead of deleting them in the `%install` phase.
- Do not skip `make test` or `make check` to disable self-test cases during compilation.
- When specifying files to be packaged in the `%files` section, keep the packaging sequence the same as the sequence for defining the package.
- In the `%files` section, use wildcard characters to replace multiple lines. Note that a single directory cannot be packaged randomly because it may conflict with the actual owner of the directory.
- During the build process, openEuler appends security-related compilation options by default. Do not remove them unless otherwise required.
- To provide a background service, prepare a unit configuration file based on the systemd unit requirements.

### Conflict and Obsolescence

- You can always obtain the latest software packages from the openEuler release address. If possible, openEuler will try to resolve conflicts before release. If certain conflicts cannot be solved, openEuler will provide a release note to help users make choices.

- openEuler will not make a choice because multiple pieces of software provide the same functions. We hope to integrate as many software packages as possible to enrich the ecosystem.

- Package name conflicts must be resolved. You can communicate with the community. If the native community does not make concessions, consider using a prefix or suffix in the name

- If a conflict exists, explicitly use `Conflicts` in the SPEC file to specify the conflict. Generally, the following scenarios are involved:

  - When multiple pieces of software provide the same function and cannot be installed and used at the same time. For example, you are advised to specify `Conflicts: linaro-gcc` in the GCC SPEC file.

  - Whe multiple pieces of software provide the same files, tools, and standard commands, try to avoid duplicate names (for example, the manual name is the same or the busybox command name is the same as that of another tool). You can communicate with the community about duplicate names or request openEuler to rename the software. If the problem persists, you are advised to specify `Conflicts` in the SPEC file until no conflict occurs in the latest version.

  - Compat package conflicts, for example, conflicts between compat-gcc and gcc (the original purpose is to provide multiple versions of GCC in the same system, which is not allowed in principle in openEuler).

  - If a piece of software cannot run on a library of an earlier version, you are advised to use `Requires` instead of `Conflicts` to specify the library.

    ```SPEC
    **WRONG:** Conflicts: libbar < 1.2.3
    **RIGHT:** Requires: libbar >= 1.2.3
    ```

- Other conflicts that actually occur but are not listed need to be reported to the package management committee to obtain the final solution.

- When the name of a package is changed or the package is obsoleted, use `Obsolete` to specify the package name.`Provides: libfoo   Obsoletes: libfoo`

## Review Principles

This is a set of guidelines for code review. Please note that the guidelines are still being improved and may not cover all scenarios. Reviewers should make good judgment when reviewing software packages. The items listed fall into two categories: mandatory and recommended.

- **Mandatory**: Use the rpmlint tool to check whether the software is correctly packaged.
- **Mandatory**: The package name must comply with the openEuler naming rules.
- **Mandatory**: The name of the SPEC file must be the same as that of the main package, unless there is an exception in your package, but the package must be reviewed by the TC or package management committee.
- **Mandatory**: The software package must be licensed using a license approved by openEuler.
- **Mandatory**: The software package must comply with the packaging rules.
- **Mandatory**: The license field in the SPEC file of the software package must match the actual license.
- **Mandatory**: If the source package contains the license text in its own file, the file containing the license text must be contained in `%license`. If the source code does not contain the license, you need to supplement the license in the repository.
- **Mandatory**: The SPEC file of the package must be written in English and be clear and readable.
- **Mandatory**: The source code used to build the package must match the upstream source code provided in the URL in the SPEC file. Reviewers must run commands to verify the correctness of the source code package.
- **Mandatory**: If a package is not successfully compiled, built, or operating on a specific processor architecture, the architecture should be listed in `ExcludeArch` in the SPEC file.
- **Mandatory**: All build dependencies must be listed in `BuildRequires`.
- **Mandatory**: The SPEC file must correctly process the locale. This is done by using the `%find_lang` macro. `%{datadir}/locale/*` is forbidden.
- **Mandatory**: In principle, a single file cannot be packaged into multiple RPM packages (except the license files).
- **Mandatory**: The installation path must be a relative path to the`prefix` path (for example, `/usr`), instead of the default path `/`.
- **Mandatory**: The file permissions must be correctly set.
- **Mandatory**: Large documentation files must be placed in the help subpackage. (The definition of large depends on the best judgment of the packager, but is not limited to size. Large may refer to size or quantity.) If the help package is not installed, the functions of the software are not affected.
- **Mandatory**: The development file and static file must be in the devel package.
- **Mandatory**: In most cases, the devel package requires complete dependencies, including the version numbers. For example, **Requires: %{name}-%{version}-%{release}**.
- **Mandatory**: Temporary files and intermediate files generated during software building cannot be packaged into the final RPM package.
- **Mandatory**: The software package cannot contain the files or directories that are already packaged into other software packages.
- **Mandatory**: All file names in the RPM package must be in valid UTF-8 format.
- **Mandatory**: Packages added to an openEuler release cannot depend on any packages marked as obsoleted.
- **Mandatory**: If the native community provides the SPEC file, you can refer to or reference it. However, the copyright information and modification records of the community must be retained.
- **Recommended**: If the source package does not include the license text as an upstream-independent file, the packager should query the upstream to include it.
- **Recommended**: Use macros whenever possible.
- **Recommended**: Reviewers should test whether the package can be built using mock or rpmbuild.
- **Recommended**: Packages should be compiled and built into binary on all supported processor architectures.
- **Recommended**: Reviewers should test whether the functions of the package are as described.
- **Recommended**: If scriptlets are used, they must be robust. If they are not clear, jointly determine whether they are reasonable with reviewers.
- **Recommended**: Generally, if a subpackage other than the devel package depends on the main package, the dependency on the main package must be clearly described and the complete version information must be provided. Otherwise, problems may occur during the upgrade.
- **Recommended**: If the package depends on files outside of **/etc**, **/bin**, **/sbin**, **/usr/bin**, or **/usr/sbin**, consider requiring the packages that contain the files instead of the files.
- **Recommended**: If the software contains too many documentation files, you are advised to split the files into a help package.

## Your First RPM Package

### Prerequisites

According to this tutorial, you need to install the following software packages, some of which are installed in the system by default:

```
$ yum install gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools
```

### Example

The following table lists the sections used in the RPM SPEC file. The sections can be combined into simple SPEC files.

| SPEC Section | Definition                                                   |
| ------------------ | ------------------------------------------------------------ |
| `%description`     | A full description of the software in the RPM package. The description can span multiple lines or be divided into paragraphs.|
| `%prep`            | Command or series of commands to prepare the software to be built. This section can be seen as a shell script.|
| `%build`           | Command or script for actually building the software into machine code (for compiled languages) or byte code (for some interpreted languages).|
| `%install`         | Command or series of commands for copying the required build artifacts from `%builddir` (where the build happens) to the `%buildroot` directory (containing the directory structure with the files to be packaged). This usually means copying files from `~/rpmbuild/build` to `~/rpmbuild/buildroot` and creating the necessary directories in `~/rpmbuild/buildroot`. For details, see the SPEC file.|
| `%check`           | Command or series of commands to test the software. This usually includes things such as unit tests.            |
| `%files`           | The list of files that will be installed in the end user's system.                          |
| `%changelog`       | A record of changes that happened to the package between different versions.              |

Creating an RPM package can be complicated. Here is a complete working RPM SPEC file with several things skipped and simplified. It is only a template. You need to modify the content based on the actual situation. Save this file as **helloworld.spec**.

```SPEC
#This is a template. Unnecessary comments can be deleted or modified. %% is the escape character of %, and the line starting with # is a comment.
#Copyright, license or readme

#Global macro or variable

#Basic Information. The definition sequence must be unified. Fields are filled in in the following sequence:
Name:           helloworld
Version:        1.0
Release:        1
Summary:        Most simple RPM package
License:        MIT
URL:            https://github.com/Aditmadzs/HelloWorld
#Source0:         There is no actual native community or source code.

#Dependency
BuildRequires:  gcc make rpm-build
#The dependencies must be RPM package names instead of commands.
Requires:       glibc

%description
This is my first RPM package, which does nothing.

%package	libs
Summary:    Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description libs
This is my first RPM package, which does nothing.

%package	devel
Summary:    Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description devel
This is my first RPM package, which does nothing.

%package 	help
Summary:	Documents for autogen
Buildarch:	noarch
Requires:	man/info

%description    help
Man pages and other related documents.

#Secondary package
#Define other packages here.

#Build sections
%prep
#%%autosetup -n %{name}-%{version} -p1
#You are advised to use autosetup to automatically install patches.

%build
#%%configure         #Options requiring special attention
#%%make_build
cat > helloworld.sh <<EOF
#!/usr/bin/bash
echo Hello world
EOF

%install
#%%make_install
mkdir -p %{buildroot}/usr/bin/
install -m 755 helloworld.sh %{buildroot}/usr/bin/helloworld.sh

%check
#make test # or make check

#Install and uninstall scripts
%pre

%preun

%post

%postun

#File list of each package, following the sequence of %doc, %license, configuration, command, library, documentation, man page, and others
%files
%defattr(-,root,root)
%{_bindir}/helloworld.sh

#%%license license
#%%config


%files libs
%defattr(-,root,root)
#%%lib

%files devel
#%%include
#%%lib*.a

%files help
#%%man, info
#%%doc

#%%other

%changelog
* Wed Jul 18 2018 openEuler Buildteam <buildteam@openeuler.org> - version-release
- Package init
```

Now run the **rpmdev-setuptree** command to create working directories.

```
$ rpmdev-setuptree
$ rpmlint helloworld.spec                //Check the SPEC syntax.
$ rpmbuild -ba helloworld.spec
```

The following table lists the directory layout of the RPM packaging workspace.

| Directory | Purpose                                                      |
| --------- | ------------------------------------------------------------ |
| BUILD     | Working directory created during compilation and building. The source code is decompressed, the patch is installed, and the building operation is performed here.|
| RPMS      | Stores the encapsulated RPMs in subdirectories for different architectures, for example in subdirectories **x86_64** and **noarch**.|
| SOURCES   | Compressed source code archives, including source code packages, patches, and configuration files.          |
| SPECS     | Stores the SPEC files.                              |
| SRPMS     | Stores the generated source RPM (SRPM).|

After the **rpmbuild** command is executed successfully, four binary RPM packages are generated, including **helloworld**, **helloworld-libs**, **helloworld-devel**, and **helloworld-help**.

```
Processing files: helloworld-libs-1.0-1.x86_64
Processing files: helloworld-devel-1.0-1.x86_64
Processing files: helloworld-help-1.0-1.noarch
Checking for unpackaged file(s): /usr/lib/rpm/check-files /root/rpmbuild/BUILDROOT/helloworld-1.0-1.x86_64
Wrote: /root/rpmbuild/SRPMS/helloworld-1.0-1.src.rpm
Wrote: /root/rpmbuild/RPMS/x86_64/helloworld-1.0-1.x86_64.rpm
Wrote: /root/rpmbuild/RPMS/x86_64/helloworld-libs-1.0-1.x86_64.rpm
Wrote: /root/rpmbuild/RPMS/x86_64/helloworld-devel-1.0-1.x86_64.rpm
Wrote: /root/rpmbuild/RPMS/noarch/helloworld-help-1.0-1.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.UnMR3x
+ umask 022
+ cd /root/rpmbuild/BUILD
+ /usr/bin/rm -rf /root/rpmbuild/BUILDROOT/helloworld-1.0-1.x86_64
+ exit 0
```

### Building Software from Source Code

This section describes how to build software from the source code. We are not going to explain the basic concepts, such as what source code is, what a patch is, what a binary executable program is, and how to use automatic build scripts such as configure and make.

We focus on how to build a binary RPM from the source code through the SPEC file.

You need to understand several important concepts.

| Concept      | Description                                                         |
| --------- | ------------------------------------------------------------ |
| Source code package    | A file compressed in a certain format. For example, **helloworld-1.0.tar.gz** specifies that the software package name is **helloworld**, the version number is **1.0**, and the compression format is **tar.gz**.|
| Patch| Incremental source code that updates other source code. It is formatted as a diff to represent the difference between two versions of text. A diff is created using the `diff` utility, and applied to the original source code using the `patch` utility. This gives you a copy of the new code that fixes a certain issue. In the build using the SPEC file, the `patch` utility is generally a .patch text file.|
| Patching   | In the source code directory, run the `patch` or `git am` command to apply a patch to the source code. This process is usually performed in the `%pre` phase of the SPEC file.|
| Build dependencies | A comma-or space-separated list of packages that build the basic compilation environment required by the software. There can be multiple entries of `BuildRequires`, each on its own line in the SPEC file.|
| Installation dependencies | Runtime dependencies required for installing the software to the system. Generally, if this section is missing, the commands, libraries, or other files required for software running are missing. As a result, the function is abnormal.|
| Source RPM | An RPM with the source code and SPEC encapsulated. You can decompress the package using rpm2cpio to view the complete content.|
| Binary RPM| RPM with commands or files generated by the **make install** command encapsulated in a specified format based on certain rules.|
| RPM signature  | Signing packages is a way to protect packages for end users. Signing is to ensure that no third party can change the contents of the packages.|
| section   | Sections `%pre`, `%build`, `%install`, `%test`, and `%clean` correspond to specific actions. The **rpmbuild** command automatically converts each section into a script.|

The following describes `%pre`, `%build`, `%install`, `%test`, `%clean`, and the SPEC file as a build script. They fix the following steps programmatically:

1. `%pre`: In this section, the key work is to install patches for the original source code and prepare the compilation environment.
2. `%build`: It is equivalent to running **make build** on the source code, except that **make build** is embedded in rpmbuild.
3. `%install`: It is equivalent to **make install** during source code building and installation. The difference is that in the rpmbuild process, the installation location `%{buildroot}` needs to be specified to facilitate file encapsulation.
4. `%test`: **make test**. It contains test cases provided by the source code of the community.
5. `%clean`: (Optional) It is used to remove temporary directories and files generated during rpmbuild.

When you obtain a copy of source code from the native community of the software, manually complete the operations in the preceding sections locally, add the preceding operations to a standard SPEC template, and fill in the basic information of the software package, a software package is quickly packaged.


### openEuelr Custom Macros
Here are some RPM macros specially defined by openEuler.

```
%disable_rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool \
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%delete_la_and_a
find $RPM_BUILD_ROOT -type f -name "*.la" -delete \
find $RPM_BUILD_ROOT -type f -name "*.a" -delete

%delete_la
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%chrpath_delete
find $RPM_BUILD_ROOT/ -type f -exec file {} ';' | grep "\<ELF\>" | awk -F ':' '{print $1}' | xargs –i chrpath --delete {}

%package_help
%package        help \
Summary:        Documents for %{name} \
Buildarch:      noarch \
Requires:               man info \
\
%description help \
Man pages and other related documents for %{name}.

%install_info()
/sbin/install-info %1 %{_infodir}/dir || :

%install_info_rm()
/sbin/install-info --remove %1 %{_infodir}/dir || :
```
