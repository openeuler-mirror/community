## 概述

openEuler Java SIG 致力于将 Java 生态中大量高质量开源应用、组件和基础库引入 openEuler 社区和系统，通过提供完善的构建解决方案、环境和指引文档，让更多对此感兴趣的人加入其中。


## 目标

- 首先在社区引入 maven,ant,gradle,sbt 这样的构建工具，为其他 Java 软件包的引入做好准备。当然这里主要是 maven。
- 定义编写 maven 构建相关的宏和脚本，屏蔽繁杂的实现细节，方便需要使用 maven 构建的 spec 的编写。
- 按需引入 Java 生态中的重要软件包，例如 tomcat、jetty、eclipse 等。
- 编写针对 Java 软件包的 spec 的指引文档，让更多人可以参与进来。
- 开发 javaporter 这样的自动化解析和打包工具，来减轻人力的投入。
- 创建一些针对不同 JDK 版本的 docker 镜像，这些镜像集成了完整的构建工具链（包括 maven 内部仓储）和环境，方便不同用途的构建和验证工作，例如开发者实验环境、CI 系统等。

## 任务

- 引入 maven：通过 rpm 的方式引入 maven 到社区。
- 定义 maven spec 宏：定义一系列用于简化针对 maven 构建的宏定义。
- Java 软件包打包自动化工具和指引文档。
- 引入更多重要 Java 生态中的应用、组件和基础库：例如 tomcat, jetty 等。
- 开放引入清单：鼓励更多人参与到 Java 生态引入的行列来。

![missions](missions.png)

## 组织会议

- 公开的会议时间：每周五 下午 6:00 - 6:30
- Zoom MeetID: 754 813 6418

## 成员

### Maintainer 列表

- luo-haibo
- sinever
- it_bricklayer
- rita_dong

### Committer 列表

欢迎提交 issue 或者 PR。

## 联系方式

- 邮件列表: java-sig@openeuler.org
- Slack: openeulerworkspace.slack.com channel -> #sig-java
- Zoom 公开会议 MeetID: 754 813 6418

## 项目清单

### JavaPackages

项目描述：  
用于存放 Java SIG 打包相关文档、代码和开发过程中产生的各类 issue。

repository 地址：  
- https://gitee.com/openeuler/Java-Packages

## 软件包清单
- https://gitee.com/src-openeuler/maven-local