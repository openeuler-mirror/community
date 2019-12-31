# SIG  管理指南

 所有openEuler社区的SIG都必须有一个章程（Charter）来明确SIG的范围和治理规则。

+ 范围必须明确定义SIG负责指导和维护的领域
+ 治理规则必须说明SIG中的职责，以及拥有这些职责的角色和工作开展方式



## 申请新SIG的流程

**1、使用SIG模板创建自己的新SIG**

将 gitee.com/openeuler/community Fork到你的Gitee下。


```
git clone https://gitee.com/YOURGITEE/community

cd ./community/sig

cp -r sig-template sig-YOURSIGNAME

cd sig-YOURSIGNAME

```


**2、完成新SIG章程的填写**

为便于更好的理解章程模板里的内容，建议先阅读[建议书和要求](./SIG-governance-requirements.md)，完成新SIG的申请填写。

```
mv sig-template_cn.md sig-YOURSIGNAME_cn.md

mv sig-template.md sig-YOURSIGNAME.md

vi sig-YOURSIGNAME_cn.md

vi sig-YOURSIGNAME.md

```

**3、完成新项目成员的配置**

请在OWNERS文件中完成对SIG成员的配置

```
vi OWNERS

```

**4、完成新SIG的Repository的配置**

请参考[openEuler的Repository说明](/zh/Gitee-Management/Gitee-management-guide.md)，完成SIG和项目所拥有的Repository的配置。

- 如果您的项目在openEuler社区只维护软件包，请点击[src-openeuler.yaml](/repository/src-openeuler.yaml)，在其中按照格式把你的项目添加进来。

```
vi ../../repository/src-openeuler.yaml

```

- 如果不是以上的情况，请单击[openeuler.yaml](/repository/openeuler.yaml)，并按照内部的格式在文件的最后把您的SIG添加进来

```
vi ../../repository/openeuler.yaml

```

**5、在sig文件夹的sig.yaml内添加新SIG的相关信息**

根据以上的信息，打开sig文件夹下[sigs.yaml](/sig/sigs.yaml)文件，在末尾添加新sig的相关信息并提交PR。

```
vi ../sigs.yaml

- name: sig-YOURSIGNAME
  repositories:
  - openeuler/aaa
  - src-openeuler/bbb
```

**6、提交PR**

将以上修改提交到Gitee上，并在Gitee上创建一个Pull Request。

**7、向TC发送邮件申请**

给技术委员会发邮件（邮箱<tc@openeuler.org>），并在正文中包含主题“[*新SIG提案]*”和PR的链接

**8、TC评审并反馈意见**

8.技术委员会通常会在发送申请后的一周内反馈。如果遇到假期或重要会议等因素，可能会需要更长时间。在此期间，您可以进行任何有需要的更改

**9.TC评审通过并合入**

技术委员会将通过合并Pull Request的方式来批准您的申请



##  SIG变更批准流程

如果您要修改SIG章程（charter.md）、团队成员(OWNERS)、增删Repository(Repository)。

**1、对于影响范围小的变更**，比如只影响本SIG范围内的问题或领域（比如变更团队成员），PR申请填写完成以后，SIG的Mainatiner可以自行审批协助完成变更

**2、对于以上的重大变更或可能影响其他SIG组的任何变更**（例如项目范围变更、增删Repository）

+ 从SIG组中确定推动变更的负责人，最常见的就是SIG的Mainatiner作为负责人
+ 变更所有者组织SIG组成员一起制定变更内容，并与技术委员会讨论（为便于信息同步，可以在与指导委员会的沟通中键入SIG组的邮件列表）
+ 获取到技术委员会的批准意见后，提交PR，并将该申请发送给[技术委员会邮件列表](tc@openeuler.org)，发送主题请标注成“【*SIG章程更新：*YOUR SIG/RPROJECT】”
+ 对于较大的变更，确认变更范围后请通知openEuler社区内受到影响的其他SIG组，并将邮件发送到tc@openeuler.org，或者在社区门户上宣布。

如果这一过程中有任何疑问，请联系技术委员会：<tc@openeuler.org>

