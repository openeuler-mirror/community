这里记录了openEuler社区当前的运作方式。



# 原则
openEuler社区遵循以下原则：
+ **开放**：openEuler是开源的和开放的
+ **尊重**：社区里的每一个人都必须遵守社区的行为准则
+ **透明**：社区内的工作和沟通都是以公开的形式进行的
+ **领先**：欢迎在社区开展技术孵化创新



## 行为守则

openEuler社区遵循[社区行为准则](code-of-conduct.md)




## 社区成员

请查看[社区成员](community-membership_cn.md)




##  社区团体

请查看[社区团体](https://openeuler.org/zh/sig.html)



### SIG (Special Interest Group)

------

openEuler社区主要的组织构成是**SIG**。

每个SIG的共同目的都是针对特定的一个或多个主题，推动交付成果输出，并争取让交付成果成为openEuler社区发行的一部分或者openEuler扩展包的一部分。SIG的每个可识别的部分都属于该SIG，包括存储库、目录、API、测试、问题、PR等。

SIG在任何给定时间内必须至少有一个或多个Maintainer。Maintainer负责SIG的运作，通过SIG的治理实现特定的目标，并与团队成员一起与技术委员会、其他SIG组、用户进行交流协同。

每个SIG都必须有一个章程，其中规定了SIG的业务范围（主题、代码库、目录等）、职责、权限区域，如何选择/授予权限/领导权的成员和角色，如何制定决策和解决冲突，如何管理章程等信息。在一些跨SIG流程（如发布流程）和资产（如存储库）的广泛指导原则约束下，SIG可以相对自定义的更改其操作方式。

SIG组内的交流必须是公开的，以确保其他SIG组的社区成员可以找到讨论、会议、涉及和决策的记录，SIG也需要定期向社区传递项目的工作概要。

有关SIG的治理的更多详细信息，请参考[SIG治理](/zh/technical-committee/governance/SIG-governance.md)、[SIG治理要求](/zh/techniacl-committee/governance/SIG-governance-requirements.md)。

[SIG文件夹](sig/)内记录了openEuler社区当前的所有SIG。



#### SIG、项目和repository

>  **SIG**：顾名思义，是一个团队，代表一群**“人”**
>
> **项目**：是为了完成某一特定目标而相互关联的任务，代表一组**“事”**



SIG会针对一个或多个主题树立目标，从而成立项目去实现目标。目标的交付成果（包括代码和软件包）保存在repository内。所以项目和repository是息息相关的。综上SIG、项目和repository的关系是：

- 一个SIG至少有一个项目

- 一个项目对应一个或多个repository（交付成果为便于管理，会保存在多个相关的repository内）。

- 一个项目可以由SIG内的一部分人参与，也可以由SIG内的所有人参与。

  

**由于项目的相关任务和成果均在repository上管理，所以在openEuler社区，项目等同于repository(ies)，它可以代表一个repository，也可以代表一组相关的repository**。





### 委员会

SIG是在公开场合运作的自愿团体，任何人都可以加入。但因为某些领域需要谨慎处理（例如安全性），所以委员会不公开成员资格，而且并不总是公开运作。

 技术委员会可以根据需要，在有限的时间内成立某一特定委员会。委员会的成员资格由技术委员会决定，但所有委员会成员必须是[社区成员](community-membership_cn.md)。与项目一样，委员会也有章程，并定期向社区和技术委员会报告。

[Committee文件夹](committee/)内记录了openEuler社区当前的所有的委员会。



## 跨项目沟通和协调

一方面，跨SIG协调的成本是昂贵的，虽然社区的大部分工作不需要协调，但仍然避免不了有跨越边界的工作（依赖等）。在这种情况下，期望多个SIG之间互相协调并达成共识比较困难，组建联合工作组就显得很有意义了。

另一方面，一些SIG确实会对所有SIG产生影响，比如发布、测试、打包等。即使都不需要这些的软件，有时也可能需要进行变更或影响到其他SIG。在这种情况下，所有SIG都应遵守社区范围内的沟通流程。

例如：具有影响力的提案需要在社区范围内公告，以便于其他SIG的成员有机会提供反馈和指导。不过本领域的项目拥有本领域的决策权。如果跨项目争议时间较长，则可以上升到技术委员会。



## Repository指南

openEuler Gitee下的所有的Repository都应该遵循[openEule的Repository指南](/zh/Gitee-management/README.md)中描述的过程。



## CLA

所有贡献者都必须签署openEuler CLA，请具体看[这里](/zh/CLA.md)。

