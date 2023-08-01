# Porting Platform WinApp SIG

English | [简体中文](./sig-porting-platform-winapp_cn.md)

Note: The Charter of this SIG follows the convention described in the openEuler charter [README](/en/governance/README.md), and follows [SIG-governance](/en/technical-committee/governance/SIG-governance.md).

The Porting Platform WinApp SIG group focuses on technology and software development related to the migration of Windows applications to openEuler.

## SIG Mission and Scope

### Mission

For the software tools urgently needed for migration (such as Windows code analysis tools, integrated development environment engineering conversion tools, etc.), share the relevant source code framework, discuss with the software function and development direction, and realize the collaborative development and version iteration of software tools.

This SIG group is committed to building an open source community for Windows application migration, responsible for software development and information exchange related to Windows application migration in openEuler, and providing support for the expansion of openEuler and application ecology.

### Scope

- The VS Project Conversion Assistant will provide a sleek and convenient method to convert original Visual Studio (VS) projects into cross-platform Qt projects. It is designed to meet the needs of cross-platform software development and assist you in quickly and seamlessly migrating VS projects to the Qt framework.
- Provide windows app library dependency analysis tools to support the dependency of windows app in openEuler dependency
- Package production, windows original app in openEuler package release, support command line, graphical installation
- The windows app developed for the development framework such as winform / WPF / nodejs
  - Provide an evaluation tool to identify some features and capabilities that the current linux does not have
  - For the ability to support the above missing framework under the current linux
- Maintenance of Mono and other .NET Framework related packages.

### Repositories and description managed by this SIG

- Project Name：vs2qt
- Deliverables：Source and tar
- Repository：<https://gitee.com/openeuler/vs2qt>
