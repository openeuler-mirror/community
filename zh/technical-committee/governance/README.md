# 项目  Charter指南

 所有openEuler社区的项目都必须有一个章程（Charter）来明确项目的范围和治理规则。

+ 范围必须明确定义项目负责指导和维护的领域
+ 治理规则必须说明项目中的职责，以及拥有这些职责的角色和工作开展方式



## 申请新项目章程的步骤

1.将[模板](/template-proj-governance.md)复制到community/proj*YOURPROJECT*/charter.md下的新文件中（[范例]()）

2.为便于更好的理解模板里的内容，建议先阅读[建议书和要求](/proj-governance-requirement.md)

3.填写您的项目申请模板

4.请根据您申请模板中定义的项目，以及项目中的角色和项目的Repository更新[openeuler.yaml]()。项目的Repository请参考[openEuler的Repository说明](/Gitee-management/Gitee-management-guide.md)

5.在openeuler.yaml中添加您的项目，以及这个项目拥有的子项目

6.用修改好的charter.md和openeuler.yaml ，创建一个Pull Request，并在您的团队内对申请书内的项目范围和治理章程达成一致的意见

7.请将项目章程（charter.md）发送给技术委员会审查（网址为tc@openEuler.org），并在正文中包含主题“新项目/项目提案”和PR的链接

8.技术委员会通常会在发送申请后的一周内反馈。如果遇到假期或重要会议等因素，可能会需要更长时间。在此期间，您可以进行任何有需要的更改

9.技术委员会将通过合并Pull Request的方式来批准您的申请



## 更新现有项目章程的步骤

+ 对于重大变更或可能影响其他项目组的任何变更（例如范围变更），请填写PR申请，并将该申请发送给技术委员会，发送主题请标注成“项目章程更新：*YOURPROJECT*”
+ 对于影响范围小的变更，比如只影响本项目范围内的问题或领域，项目的Mainatiner可以自行协助进行变更



##  项目章程批准流程

引入新项目或对老项目的章程进行修改时，过程如下：

+ 从项目组中确定推动变更的负责人，最常见的就是项目的Mainatiner作为负责人
+ 变更所有者组织项目组成员一起制定变更内容，并与技术委员会讨论（为便于信息同步，可以在与指导委员会的沟通中键入项目组的邮件列表）。
+ 获取到技术委员会的批准意见后，提交PR并将邮件发送到tc@openeuler.org。对更改细节的讨论交流建议在申请PR之前在社区上进行。
+ 对于较大的变更，确认变更范围后请通知openEuler社区内受到影响的其他项目组，并将邮件发送到tc@openeuler.org，或者在社区门户上宣布。

如果这一过程中有任何疑问，请联系技术委员会：tc@openEuler.org





## 项目申请社区发行提案步骤

如果项目希望自己的交付件可以进入**社区发行范围**，请向技术委员会提出申请

1.将[模板](template-release.md)复制到community/proj*YOURPROJECT*/release.md

2.按照模板要求填写项目毕业申请

.用修改好的release.md和openeuler.yaml ，创建一个Pull Request

.请将社区发行申请（release.md）发送给技术委员会审查（网址为tc@openeuler.org），并在正文中包含主题“项目社区发行提案”和PR的链接

.技术委员会通常会在发送申请后的一周内反馈。如果遇到假期或重要会议等因素，可能会需要更长时间。在此期间，您可以进行任何有需要的更改

.技术委员会将通过合并Pull Request的方式来批准您的项目的社区发行申请

**请注意，申请社区发行有三种类型**：

- 第一种：进入发行光盘范围，
- 第二种：进入`/extra`（不在光盘内的额外的软件包）目录
- 第三种：进入`/experimental`（探索、实验性质的软件包）目录



## 常见问题

NULL


