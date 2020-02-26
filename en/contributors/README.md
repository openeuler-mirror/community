**The contenct in this folder is not finalized yet and please visit [How to contribute](https://openeuler.org/en/developer.html) to get help. And you are more than welcome to work with us together on updating tis folder. If you'd like to please visit <community@openeuler.org>.**

该文档指导大家如何为openEuler社区做出贡献。欢迎阅读[待解决的问题]()并提出新的问题。



# 欢迎

欢迎来到openEuler！

+ 欢迎
+ [开始之前](#id1)
  + [签署CLA](#id1-1)
  + [行为准则](#id1-2)
  + [社区期望](#id1-3)
- [您的第一个贡献](#id2)
  - [找到您感兴趣的工作](#id2-1)
    - [了解SIG](#id2-1-1)
    - [找到您感兴趣的SIG和respository](#id2-1-2)
  - [开始您的贡献](#id2-2)
    - [给你自己分配一个issue](#id2-2-1)
    - [提出问题](#id2-2-2)
    - [SIG贡献者指南](#id2-2-3)
    - [社区贡献指导](#id2-2-4)
  - [沟通](id2-3)
- [Gitee工作流程](#id3)
- [代码检视](#id4)
- [测试](#id5)
- [选择社区组件打包](#id6)
- [下载安装openEuler](#id7)
- [安全](#id8)
- [社区文档](#id9)
- [社区活动](#id10)
  - [社区交流](#id10-1)
  - [大事记](#id10-2)
  - [聚会](#id10-3)




<h1 id=“id1”>开始之前</h1>
<h2 id="id1-1">签署CLA</h2>

您必须首先签署[“贡献者许可协议”（CLA）](./../CLA.md)，然后才能参与社区贡献.



<h2 id="id1-2">行为守则</h2>

请确保阅读并遵守openEuler社区的[行为守则](./../../code-of-conduct.md)。



<h2 id="id1-3">社区期望</h2>

openEuler是一个开源社区。因此它完全依赖于社区提供开发，以及友好和协作的环境，请查看[社区成员角色](./../../community-membership.md)。社区鼓励您在积累经验的同时提高你的贡献级别。



<h1 id="id2">您的第一个贡献</h1>
随时欢迎您的加入！在社区上总是有可以改进的文档（比如您正在阅读的），可以澄清的代码，可以重构或注释的函数或变量，始终需要测试的代码。我们将帮助您了解openEuler SIG的组织方式，并引导您顺利的开始您的第一个贡献。您可以选择解决问题、编写代码，或者检视和合并等工作。所以如果您感兴趣，现在就行动吧~~

如果您对开发过程有疑问，请随时加入我们的[开发邮件列表](dev@openeuler.org)，并在邮件标题内用“【开发过程疑问】”作为标题 写出你的疑问和困惑，openEuler团队会定期扫描邮件列表上的内容，并尽力确保您的问题得到解答。


<h2 id="id2-1">找到您感兴趣的工作</h2>

<h3  id="id2-1-1">了解SIG</h3>

#### SIG和Repository

我们将社区按照不同的SIG来组织，以便于更好的管理和改善工作流程。

SIG组是开放的，欢迎任何人加入并参与贡献。SIG组内部会定期开会，每一个SIG都有一个公共频道。每一个SIG在Gitee上都会拥有一个或多个repository，单击SIG名称中的链接，可以获取每个SIG的`README.md`。在`README.md`里可以查找到SIG包含的子项目和子项目的额repository。

<h3 id="id2-1-2">找到您感兴趣的SIG和repository</h3>

找到适合您贡献的SIG组，可以帮助您在正确的地方提出问题，为您的贡献提供更高的知名度和更快的社区响应速度。您可以查看[SIG列表](https://openeuler.org/zh/sig.html)，以便您最快速的定位到自己感兴趣的领域。

在openEuler的Repository列表下搜索SIG名称，也可以找到对应子SIG的repository。如果搜索不到，您可以尝试在dev@openeuler.org中寻求帮助。同样，请在邮件列表内用“【开发过程疑问】”作为标题 写出你寻找的SIG或项目。



<h2 id="id2-2">开始您的贡献</h2>

如果您的兴趣不在编写代码方面，可以在[《非代码贡献指南》](non-code-contributions.md)中找到感兴趣的工作。



<h3 id="id2-2-1">给自己分配一个issue</h3>

如果您愿意处理一个issue，可以将它分配给自己。只需要在评论框内输入 `/assign`或 `/assign @yourself`，机器人就会将问题分配给您，您的名字将显示在负责人列表里。



<h3 id="id2-2-2">提出问题</h3>

尽管社区鼓励每个人贡献代码，但是当您报告问题或缺陷的时候，也是值得赞赏的。问题应提交到对应的repository下面。您可以查看[问题提交指南](issue-submit.md)以获取更多的信息。提交问题时，请确保遵守问题提交准则。


<h3 id="id2-2-3">SIG贡献指南</h3>
每个SIG或子项目的编码语言、开发环境、编码约定等都可能是由差异的。所以每一个SIG或其子项目都可能有自己的贡献者指南——一般是`CONTRIBUTING.md`文件。除了这些文件外，SIG可能还会提供其他指南信息。这些信息位于SIG或子项目的特定社区目录中。



<h3 id="id2-2-4">社区贡献指导</h3>

初学者也可以通过下面的[提交PR](pull-requests.md)和[代码检视](expectations.md)中找到相关指导。




<h2 id="id2-3">沟通</h2>

openEuler是开源的，我们希望围绕开发建立一些半正式的管理规则，这样可以使事情开展的更加顺利。如果您认为这些规则有问题，请提出来。作为潜在的贡献者，无论是在白天、黑夜、工作日、周末或节假日，不要犹豫，我们都欢迎您提出自己的想法到dev@openeuler.org。我们致力于改善您的贡献体验。如果您发现不良的参与体验，请告诉我们！



<h1 id="id3">Gitee工作流程</h1>

想获取要使用的代码，请参考[Gitee workflow Guide](Gitee-workflow.md)。

### 提交一个PR

openEuler遵循标准的[Gitee PR请求流程](https://gitee.com/help/articles/4122)，但openEuler社区还做了部分的定制，请参考[openEuler社区Gitee工作流程](pull-requests.md)。

这两个流程的主要区别是，openEuler的机器人会将结构化标签运用于PR中。该机器人可以为您的PR过程提供一些有用的建议。为了方便查看，可以在注释中输入XXXXXXX选项，以触发自动标记和通知功能。请参阅[社区命令参考文档](./../sig-infrastructure/command.md)。

对于新贡献者来说，常遇到的问题是：

+ 在您的第一个PR之前没有正确的签署CLA（请参阅[签署CLA](/../CLA.md)）
+ 为PR在SIG组内找到合适的检视者，并保证自己的贡献遵循SIG组内特定的贡献准则（请参阅[了解SIG](https://openeuler.org/zh/sig.html)，从其中查找感兴趣的SIG提供的贡献者指导）
+ 处理在PR上失败的测试用例，这些测试用例可能与您引入的更改无关（请参阅）
+ 不遵守一些[良好的编码实践]()
+ 在提交的信息中包含了可能关闭issue的关键字，比如XXXXXXXX等



<h1 id="id4">代码检视</h1>

对于贡献者，关于代码检视的重要性的简要说明，请参阅[代码检视](expectations.md)。为了使您的提交更容易被接受，您需要：

+ 遵循SIG组的[编码约定]()
+ 准备完善的提交信息
+ 如果一次提交的代码量较大，建议将大型的内容分解成一系列逻辑上较小的内容，分别进行提交会更便于检视者理解您的想法
+ 使用适当的SIG组和监视者标签去标记PR：机器人会发送给您消息，以方便您更好的完成整个PR的过程



对于检视者，强烈建议本着[行为准则](/../code-of-conduct.md)和[社区期望](/expectations.md)，超越自我，相互尊重和促进协作。在审查其他人的PR的时候，[补丁审核的柔和艺术](https://sage.thesharps.us/2014/09/01/the-gentle-art-of-patch-review/)提出了一系列检视的重点，旨在说明检视的活动也希望能够促进新的贡献者积极参与，而不会使贡献者一开始就被细微的错误淹没，所以检视的时候，可以重点关注包括：

+ 贡献背后的想法是否合理
+ 贡献的架构是否正确
+ 贡献是否完善

注意：如果您的PR请求没有引起足够的关注，可以在XXXXX的XXXXX频道来获取查找评论者们的帮助。



<h1 id="id5">测试</h1>

测试——是所有贡献者的责任，对于社区版本来说，sig-qa也会做很多的协调工作。有关的信息信息，可以参考[《测试指南》](./../sig-test/testing.md)

为了成功发行一个社区版本，需要完成多种测试活动。不同的测试活动，测试代码的位置也有有所不同，成功运行测试所需的环境的细节也会有差异：

todo：待qa团队补充具体的测试活动内容

+ 单元测试：这一测试活动确定特性功能的行为是否符合预期。XXXXXXXXXXXXXXXX，可以在给定包中与相应源代码的相邻位置找到单元测试的源代码。例如XXXXXXXX中定义的函数将在XXXXXXXXXX中进行单元测试。
+ XXXX测试
+ XXXX测试

持续集成会将这些测试活动在PR提交前完成，结果会出现在XXXX上

[sig-qa组](/../sig/sig-qa/)是负责测试活动的官方机构，他们的相关测试自动化工具在test-fra中。如果您你希望自己的基础架构上能运行XXX测试，可以考虑采用。



<h1 id="id6">选择社区组件打包</h1>

请参考[如何打包](packaging.md)



<h1 id="id7">安装openEuler</h1>

请参考[下载安装openEuler](https://openeuler.org/zh/docs/installation/installation.html)



<h1 id="id8">安全</h1>

+ [安全发布页面]()——简要描述了处理安全问题的过程
+ [安全披露信息]()——如果您希望报告安全漏洞，请参考此页面



<h1 id="id9">社区文档</h1>

+ [贡献文档]()



<h1 id="id10">社区活动</h1>

<h2 id="id10-1">交流</h2>

[社区常规交流方式](./communication)


<h2 id="id10-2">大事记</h2>

openEuler参加了XXXXXX，每年在XXXXXXX，关于这些事件和其他社区事件信息可以在[openEuler事件]()页面上找到



<h2 id="10-3">聚会</h2>

我们遵循针对开发者的聚会的XXXXX准则，您可以通过XXXXX上的直接消息或通过电子邮件<XXXX@huawei.com>与XXXX联系。来加入我们把~
