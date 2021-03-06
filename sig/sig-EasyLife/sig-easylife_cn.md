
# 新建EasyLife SIG
[English](./sig-automation.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## SIG组工作目标和范围

src-openeuler当前已经有超过2000个软件包，而openeuler中不超过30个开源项目。
从这个差异中可以看出openEuler作为一个发行版，绝大部分软件来自其他的上游开源软件社区。
为了openEuler本身的健康发展，我们需要对上游开源软件的发布情况，与openEuler自身的跟进发布情况有完整的洞察。

目前社区中并没有这样的信息。
Gitee虽然可以提供软件开发活动角度的统计，但并不能给出和开源软件版本相关的信息。

本SIG关注通过软件的方式逐步实现src-openeuler中软件维护的自动化。

SIG当前计划分3个阶段：

1. 对当前openEuler Main和LTS版本中的开源软件健康程度实现自动化的洞察。以便提供给技术委员会作为输入。
2. 对当前openEuler已打包的软件，实现自动化的更新提醒，帮助各个的维护人员及时更新。用自动化工具落实软件包的维护更新策略。
3. 对当前openEuler已打包的软件，实现半自动化的更新，使得openEuler社区的维护人员可以更多投入创新和新软件包的引入。

 ### 该SIG管理的repository及描述

- openEuler-Advisor：
  - http://gitee.com/openeuler/openEuler-Advisor