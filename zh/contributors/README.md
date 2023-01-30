该文档指导大家参与openEuler社区。

# 欢迎

欢迎来到openEuler！

+ [欢迎](#欢迎)
+ [开始之前](#开始之前)
  + [签署CLA](#签署cla)
  + [行为准则](#社区行为守则)
- [开始您的贡献](#开始您的贡献)
  - [找到您感兴趣的工作](#找到您感兴趣的工作)
    - [了解SIG](#了解sig)
    - [找到您感兴趣的SIG、项目和Repository](#找到您感兴趣的sig或项目)
  - [开始您的贡献](#开始您的贡献)
    - [给自己分配一个Issue](#给自己分配一个issue)
    - [提出问题或建议](#提出问题或建议)
    - [搭建开发环境](#搭建开发环境)
      - [开发环境准备](#开发环境准备)
      - [下载和编译软件包](#下载和编译软件包)
    - [参与编码贡献](#参与编码贡献)
      - [了解SIG和项目内的开发注意事项](#了解sig和项目内的开发注意事项)
      - [下载代码和拉分支](#下载代码和拉分支)
      - [修改、编译和本地验证](#修改编译和本地验证)
      - [提交一个Pull Request（PR）](#提交一个pull-request)
	- [如何新增软件包](#如何新增软件包)
    - [检视代码](#检视代码)
    - [测试](#测试)
    - [选择社区组件打包](#选择社区组件打包)
    - [参与非代码类贡献](#参与非代码类贡献)
  - [社区安全问题反馈](#社区安全问题反馈)
  - [参与社区活动](#参与社区活动)
	- [社区内沟通方式说明](#社区内沟通方式说明)
	- [社区新闻和大事件](#社区新闻和大事件)
	- [社区聚会](#社区聚会)
- [问题反馈](#问题反馈)



# 开始之前

欢迎来到openEuler！



## 签署CLA

您必须首先签署[“贡献者许可协议”（CLA）](./../CLA.md)，然后才能参与社区贡献。



## 社区行为守则

openEuler是一个开源社区。它完全依赖于社区提供友好的开发和协作环境，所以在参与社区贡献之前，请先阅读并遵守openEuler社区的[行为守则](https://gitee.com/openeuler/community/blob/master/code-of-conduct.md)。



# 开始您的贡献

**随时欢迎您的加入！**

在社区上总是有可以改进的文档（比如您正在阅读的），需要检视的代码，可以重构或注释的函数或变量，可以持续补充和优化的测试用例。我们将帮助您了解openEuler SIG的组织方式，并引导您顺利的开始您的第一个贡献。所以如果您感兴趣，现在就行动吧。



## 找到您感兴趣的工作

### 了解SIG

SIG就是Special Interest Group的缩写，openEuler社区按照不同的SIG来组织，以便于更好的管理和改善工作流程。

- SIG组是开放的，欢迎任何人加入并参与贡献。
- SIG都是针对特定的一个或多个技术主题而成立的。SIG内的成员推动交付成果输出，并争取让交付成果成为openEuler社区发行的一部分。
- SIG的核心成员主导SIG的治理。请查看[SIG的角色说明](./../../community-membership_cn.md)。您可以在贡献的同时积累经验和提升影响力。
- 每一个SIG在Gitee上都会拥有一个或多个项目，这些项目会拥有一个或多个Repository。SIG的交付成果会保存在这些Repository内。
- 可以在SIG对应的Repository内提交Issue、针对特定问题参与讨论，提交和解决问题，参与评审等。
- 您也可以通过邮件列表、IRC或视频会议和SIG内的成员进行交流。



### 找到您感兴趣的SIG或项目

找到您感兴趣的SIG组，可以帮助您在正确的地方提出问题，并得到更快的社区响应。

- **方式一**：如果您不了解有哪些SIG或项目，您可以查看[SIG列表](https://openeuler.org/zh/sig/sig-list/)，它包含当前openEuler社区成立的所有SIG团队的清单。您可以通过该列表快速的定位到您感兴趣的领域所对应SIG团队。同时还为您提供该SIG团队的如下信息：
  
  - SIG下的项目，以及项目的Repository地址
  - SIG内的交流方式，包括邮件列表、IRC会议频道等
  - Maintainer的联系方式
  
- **方式二**：如果您知道感兴趣的项目名称，可以在openEuler的Repository列表下进行模糊搜索，从而快速定位到对应项目的首页地址。通常情况下，在该项目首页地址的`README.md`文件中，可以找到该项目所属的SIG信息、交流方式、成员和联系方式等。

  

  如果上述两种方式都定位不到您感兴趣的SIG，您可以向community@openeuler.org发求助邮件。建议您在邮件列表内用“【开发过程疑问】”作为标题，在内容中写出你寻找的SIG或项目的特征，我们会为您提供帮助。



## 开始您的贡献

### 给自己分配一个Issue

- **找到Issue列表**：在您感兴趣的项目的首页内（Gitee上的项目的Repository）的工具栏，点击<img src="figure/Issue图标" alt="捕获" style="zoom:50%;" />，您可以找到该SIG的Issue列表（如Community团队的Issue列表地址为<https://gitee.com/openeuler/community/issues>）

- **找到愿意处理的Issue**：如果您愿意处理其中的一个issue，可以将它分配给自己。只需要在评论框内输入 `/assign`或 `/assign @yourself`，机器人就会将问题分配给您，您的名字将显示在负责人列表里。
- **参与Issue内的讨论**：每个Issue下面可能已经有参与者们的交流和讨论，如果您感兴趣，也可以在评论框中发表自己的意见。



### 提出问题或建议

- **提出问题**：如果您发现并想向社区上报问题或缺陷，问题提交的方式就是创建一个Issue。您只要将问题以Issue的方式提交到该项目Repository的Issue列表内，并查看[Issue提交指南](issue-submit.md)以获取更多的信息。提交问题时，**请尽量遵守**问题提交准则。
- **提出建议**：如果您想对SIG领域内贡献出自己的意见或建议，也可以通过提交Issue的方式分享给大家。大家可以在该Issue上充分的交流和讨论。为了吸引更广泛的注意，您也可以把Issue的链接附在邮件内，通过邮件列表发送给所有人。



### 搭建开发环境

#### 开发环境准备

如果您想参与编码贡献，需要准备openEuler的开发环境，请参考[开发环境准备](prepare-environment.md)



#### 下载和构建软件包

如果您想下载、修改、构建及验证openEuler提供的软件包，请参考[构建软件包](package-install.md)



### 参与编码贡献

#### 了解SIG和项目内的开发注意事项

每个SIG内的项目使用的编码语言、开发环境、编码约定等都可能存在差异。如果您想了解并参与到编码类贡献，可以先找到该项目给开发者提供的贡献者指南——这个指南一般是在该SIG的首页地址内，以`CONTRIBUTING.md`文件的形式提供，或者就直接在该项目的`README.md`内（如何找到项目的Repository，请参考[上一节](#找到您感兴趣的工作)的内容）。

除了这些文件外，SIG可能还会提供其他指南信息。这些信息位于SIG或其项目的特定社区目录中。如果您未找到相关信息，或者对相关信息有疑问，可以在该SIG内提交Issue，或者把问题或疑问发送到该项目所属SIG的邮件列表。如果您认为长时间没有得到回应，可以向community@openeuler.org求助。



#### 下载代码和拉分支

如果要参与代码贡献，您还需要了解如何在Gitee下载代码，通过PR合入代码等。openEuler使用的是Gitee代码托管平台，向了解具体的指导，请参考[Gitee Workflow Guide](Gitee-workflow.md)。该托管平台的使用方法类似GitHub，如果您以前使用GitHub，本章的内容您可以大致了解甚至跳过。



#### 修改构建和本地验证

在本地分支上完成修改后，进行构建和本地验证，请参考[构建软件包](package-install.md)。



#### 提交一个Pull-Request

当你提交一个PR的时候，就意味您已经开始给社区贡献代码了。请参考[openEuler社区PR提交指导](pull-requests.md)。

#### 如何新增软件包
openEuler支持在gitee新增软件包的同时自动在obs的openEuler:Fctory上创建同名仓库。这样在向已创建的gitee仓库提交代码时，会自动对代码编译进行检测。具体流程可参考[如何新增软件包](create-package.md)。

### 检视代码

openEuler是一个开放的社区，我们希望所有参与社区的人都能成为活跃的检视者。可以参考[社区成员](https://gitee.com/openeuler/community/blob/master/community-membership_cn.md)，该文档描述了不同贡献者的角色职责。

**对于贡献者**，为了使您的提交更容易被接受，您需要：

+ 遵循SIG组的编码约定，如果有的话
+ 准备完善的提交信息
+ 如果一次提交的代码量较大，建议将大型的内容分解成一系列逻辑上较小的内容，分别进行提交会更便于检视者理解您的想法
+ 使用适当的SIG组和监视者标签去标记PR：社区机器人会发送给您消息，以方便您更好的完成整个PR的过程



**对于检视者**，强烈建议本着[行为准则](https://gitee.com/openeuler/community/blob/master/code-of-conduct.md)，超越自我，相互尊重和促进协作。在检视其他人的PR的时候，[补丁审核的柔和艺术](https://sage.thesharps.us/2014/09/01/the-gentle-art-of-patch-review/)提出了一系列检视的重点，旨在说明检视的活动也希望能够促进新的贡献者积极参与，而不会使贡献者一开始就被细微的错误淹没，所以检视的时候，可以重点关注包括：

+ 贡献背后的想法是否合理
+ 贡献的架构是否正确
+ 贡献是否完善

注意：如果您的PR请求没有引起足够的关注，可以在SIG的邮件列表或dev@openeuler.org求助。



<h1 id="id5">测试</h1>
测试——是所有贡献者的责任，对于社区版本来说，[sig-qa组](https://gitee.com/openeuler/QA)是负责测试活动的社区官方组织。如果您希望在自己的基础架构上开展测试活动，可以参考：[社区测试体系介绍](https://gitee.com/openeuler/QA/blob/master/社区测试体系介绍.md)。

为了成功发行一个社区版本，需要完成多种测试活动。不同的测试活动，测试代码的位置也有所不同，成功运行测试所需的环境的细节也会有差异，有关的信息可以参考[测试指南](https://gitee.com/openeuler/QA/blob/master/社区开发者测试贡献指南.md)。



## 选择社区组件打包

您也可以参与社区组件打包，请参考：[如何打包](packaging.md)



## 参与非代码类贡献

如果您的兴趣不在编写代码方面，可以在[非代码贡献指南](non-code-contributions.md)中找到感兴趣的工作。





# 安装openEuler

请参考[下载安装openEuler](https://openeuler.org/zh/download/)



# 社区安全问题披露

+ [安全处理流程](https://gitee.com/openeuler/security-committee/blob/master/security-process.md)——简要描述了处理安全问题的过程
+ [安全披露信息](https://gitee.com/openeuler/security-committee/blob/master/security-disclosure.md)——如果您希望报告安全漏洞，请参考此页面



# 参与社区活动

## 社区内沟通方式说明

openEuler社区的交流方式有邮件列表、IRC会议和视频会议等，使用方式请参考[社区交流方式指导](https://gitee.com/openeuler/community/tree/master/zh/communication)



## 社区新闻和大事件

openEuler参加或举办的社区和技术交流会议，关于这些事件和其他社区事件信息均可以在[openEuler新闻](https://openeuler.org/zh/interaction/news-list/)页面上找到




## 社区聚会

社区每年会定期举办开发者大会，您可以通过[https://openeuler.org](https://openeuler.org)上的信息或通过电子邮件<dev@openeuler.org>与我们联系。来加入我们吧~



# 问题反馈

如果您在使用该贡献者指南或对开发过程有疑问，请随时告诉[我们](community@openeuler.org)，并在邮件标题内用“【开发过程疑问】”作为邮件标题写出你的疑问和困惑，openEuler社区运营团队会并尽力确保您的问题得到解答。