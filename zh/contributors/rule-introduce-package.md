# openEuler 软件引入策略原则

 

## 版本

 

- 2020-01-11 Initial Draft by Xinwei Hu

- 2020-01-21 Integrate input from Liang Chengye, Wang Lingzhuo, Guodong Xu and Yang Li

 

 **目录**

- [关于本文档](#id1)
  - [目标](#id1-1)
  - [范围](#id1-2)

  - [本文的改进和修订说明](#id1-3)
- [软件选型及引入](#id2)
  - [什么是软件选型](#id2-1)
  - [软件选型规则的适用范围](#id2-2)
  - [软件包进入选型的两个基本前置条件](#id2-3)
  - [openEuler软件包引入原则](#id2-4)
  - [黑名单机制](#id2-5)
- [软件包的元数据](#id3)
  - [元数据的存储](#id3-1)
  - [元数据库中的 Identification](#id3-2)
  - [元数据库中的 主页地址 ](#id3-3)
  - [元数据库中的 REPO地址](#id3-4)
  - [元数据库中的 LANG](#id3-5)
  - [元数据库中的 TAG](#id3-6)
  - [元数据库中的 LISENCE](#id3-7)
  - [元数据库中的 项目关系](#id3-8)
  - [选型过程 request](#id3-9)
  - [附带软件的选型入库](#id3-10)
  - [软件是否存在于公开的语言库 **TODO**](#id3-11)
  - [项目关系列表](#id3-12)





<h2 id= "id1">关于本文档</h2>
<h3 id="id1-1">目标</h3>
 openEuler是一个致力于创建开放操作系统的合作组织。我们希望openEuler

 

- 尽可能集成多的软件组件

- 鼓励所有人使用openEuler，并可以在openEuler上开发软件

- 使能任何人，在不违反license，进出口管制或其他相关法律的前提下，可以容易的制作安装介质

 

openEuler遵从 [Open Source Definition](https://opensource.org/docs/osd) ，满足这一定义的软件，被openEuler社区认同为开源软件。

 

提供适度，高质量的开源软件是openEuler主要目标之一。openEuler努力为其所提供的开源软件在生命周期内提供高质量的支持服务。开源软件自由众多，质量不一。本着提供高质量开源软件的宗旨，特别拟定本规则指南。本规则的中**必须**，**必须不能**，**应该**，**应该不能**的含义参考rfc2119。

 

<h3 id="id1-2">范围</h3>
 本文档定义了openEuler软件包所需要遵从的策略要求。所以提交到openEuler的软件包需要满足本手册中定义的技术要求。

 

<h3 id="id1-3">本文的改进和修订说明</h3>

- 本文档由openEuler技术委员会 （Technical Committee）主导起草和维护。本文档的最新版本总可以在 XXXXXX [URL] 上找到。

- **所有对本文档的修改意见可以通过邮件列表 XXXXX 反馈和讨论。 任何对于本文中涉及的规则的增加，修改，删除都**必须**被追踪，[请进入该追踪系统](https://gitee.com/openeuler/community/issues) 。**
- 最终规则的经过充分的讨论后，由技术委员会定稿。





<h2 id= "id2">软件选型、选型规则及引入原则</h2>
<h3 id="id2-1">什么是软件选型</h3>

 一个软件的选型指的是一个软件(项目)从用户库被申请引入到官方库，依照本文件描述的规则讨论，进而满足规则要求，最终引入官方库的过程。

整个引入的过程都**必须**可被追踪。目前 [https://gitee.com/src-openeuler/openEuler-repos/issues](https://gitee.com/src-openeuler/openEuler-repos/issues) 是这个过程的追踪系统。



<h3 id="id2-2">软件选型规则的适用范围</h3>

 选型规则约束一个软件(项目)是否可以被引入到src-openeuler.yaml文件中，并在src-openeuler中作为一个目录维护。

**注意**：升级一个官方库中已存在的软件包不是软件选型，所以不在本规则的覆盖范围内。



<h3 id="id2-3">软件包进入选型的两个基本前置条件</h3>

凡是需要引入到openEuler的开源软件(项目)，**必须**有唯一的ID。这个ID是openEuler中管理开源项目的元数据库中的唯一标识。

- 第一步：在元数据库中创建一个item。

- 第二步：以元数据库的ID做为标识来讨论的软件(项目)。

 

<h3 id="id2-4">openEuler软件包引入原则</h3>

为实现对软件生命周期的维护和管理，基于证据的可信贯穿于选型的整个过程。在一个软件包被引入的每一步都需要有记录，这些记录被作为可信过程的存证。

* 一次**必须**只能引入一个软件。

* 软件**应该**有明确的引入理由。

* 软件**应该**是开源软件，开源软件的定义参考[https://opensource.org/osd.html](https://opensource.org/osd.html) 。如果非开源软件，经由technical committ讨论后决定。

* 软件**应该**是源码包，原则上二进制**不应该**被引入。如果需要引入二进制，经由Technical Committ讨论后决定。

* 原则上，该软件**应该**在openEuler上可以被正确构建。当软件有尚未被引入的依赖关系，或者软件的运行或者构建依赖一个绝不可能引入openEuler的组件，此等例外，经由Technical Committ讨论后决定。

* 原则上，openEuler不引入**rootkit**或者其他类似存在可信问题的软件。

* 存在于**黑名单**的软件**必须不能**引入。

* 每一个软件的引入决定，都作为案例，作为后续类似软件引入决策的参考。Technical Committ对软件引入原则的一致性负责。

 

<h3 id="id2-5">黑名单机制</h3>

Technical Committ讨论后，可以将被拒绝引入的软件被记录到一个软件黑名单，作为证据减少重复劳动。

https://gitee.com/src-openeuler/openEuler-repos/software-blacklist.md





<h2 id= "id3">元数据</h2>
<h3 id="id3-1">元数据的存储</h3>

鉴于目前openEuler采用RPM作为包管理系统，同时考虑到对元数据的需求，本规则定义的元数据需要考虑兼容RPM SPEC的前提下作为单独的一份文件存储于RPM SRC包中。所有的软件包都应提供其元数据信息，该信息需符合以下openEuler软件包元数据定义的模板要求。

**注意**：该独立的文件名字是meta.json，并采用json的数据格式。

 

<h3 id="id3-2">元数据库中的 Identification</h3>

#### 目的



  唯一识别该软件

 

#### 强制性

 

* **必须**

 

#### 作用

 

引入的软件**必须**有唯一的ID。ID可以用来描述不同软件包之间的关系，所以ID的唯一性很重要。

 

#### 格式

 

##### RPM SPEC

 

```SPEC

Name: openssl

```

 

RPM 包的名字，在整个REPO具有唯一性，可以作为ID。

 

##### Json ORG style

 

org id, 代表该软件包项目的组织ID，类似namespace的作用。

art id, 代表该项目的ID

 

json的表达格式实例

```json

"id": {

  "org": "org.openssl",

  "art": "openssl"

}

```

 

推荐，如果同时提供RPM SPEC的方式和Json ORG style两种，**应该**考虑名字的一致性。

 

<h3 id="id3-3">元数据库中的 主页地址</h3>

#### 目的

 

一个开源项目的真正的实质。它和ID在一起作为元数据库中跟实际项目的binding。

不同的ID的项目**应该不能**一样。一个项目只能由一个官方主页。

 

#### 强制性

 

* **必须**

 

#### 格式

 

##### RPM SPEC

 

```SPEC

URL: https://www.openssl.org/

```

 

#####  JSON style

 

  软件包的 主页地址，任何一个开源软件都需要有一个主页，如果没有正式的官方主页，那可以认为软件的发布页为主页，比如github的项目主页。

 

json的表达格式的实例

```json

"official": "https://www.openssl.org/"

```

 

<h3 id="id3-4">元数据库中的 REPO地址</h3>

#### 目的

 

保存该开源项目的repo地址。可以有多个。

 

#### 强制性

 

* **可选**

 

#### 格式

 

##### JSON style

 

```JSON style

"repo": [

​    "git://git.openssl.org/openssl.git",

​    "https://github.com/openssl/openssl.git"

]

```

 

<h3 id="id3-5">元数据库中的 LANG</h3>

#### 目的

 

说明该项目使用的主要编程语言。

 

#### 强制性

 

* **可选**

 

#### 格式

 

##### JSON style

 

```JSON style

"lang": [

  "c"

]

```

 

<h3 id="id3-6">元数据库中的 TAG</h3>

#### 目的

 

说明该项目主要的应用领域的其它属性。

 

#### 强制性

 

* **可选**

 

#### 格式

 

##### JSON style


```JSON style

"tag": [

  "protocol",

  "tls"

]

```

 

<h3 id="id3-7">元数据库中的 LISENCE</h3>

#### 目的

 

说明该项目用来描述该项目使用的LISENCE，LISENCE需要使用SPDX定义的ID。

 

#### 强制性

 

* **必须**

 

#### 格式

 

##### JSON style

 

为兼容SPDX，使用来自SPDX标准的命名。

```JSON style

"lisence": [

  "SPDX-License-Identifier: OpenSSL"

]

```

 

<h3 id="id3-8">元数据库中的 项目关系</h3>

#### 目的

 

说明该项目用来描述该项目之间关系。这个关系可用分析项目直接的关系，其中requires的关系可以直接推导出运行时的依赖关系。

 

#### 强制性

 

* **可选**

 

#### 格式

 

##### RPM SPEC

 

```SPEC

Requires: coreutils perl ca-certificates crypto-policies

```

 

##### JSON style

 

为兼容SPDX，使用来自SPDX标准的命名。

```JSON style

"related": {

  "HAS_PREREQUISITE": ["org.gnu.coreutils", "org.perl.perl", "ca-certificates", "crypto-policies"]

}

```

 

##### 软件(项目)关系的定义列表见附件

 

<h3 id="id3-9">选型过程 request</h3>

每次选型如果的请求都应该被记录，都应该可追溯。

 

```text

https://gitee.com/organizations/src-openeuler/issues

```

 

#### requester

 

提出该次选型入库申请的申请人。该申请人**应该**是被申请包的作者。

 

#### reason

 

申请的理由，描述这个软件(项目)为什么应该存在于官方的repo中。

 

#### result

 

描述这次选型入库的申请是否通过。

 

##### 取值

 

* accepted  **应该**有reason。

* rejected  **应该**有reason。

 

<h3 id="id3-10">附带软件的选型入库</h3>

引入一个软件有可能附带引入其它软件(项目)，根据一次引入一个软件的原则，分别为每个软件提交请求，并且附带软件的引入原因需要体现被附带引入这个情况。

 

<h3 id="id3-11">软件是否存在于公开的语言库 TODO</h3>

 比如 Marven，PIP，Python，NPM，Ruby等等，

 如果有**应该**提供在所在语言库的链接。

 

<h3 id="id3-12">项目关系列表</h3>

为兼容SPDX，使用来自SPDX标准的命名。

 

| relation | description |

| -------- | ------------|

| HAS_PREREQUISITE | 该软件需要其它的软件支持其运行，所有的被依赖软件都**应该**被列举。 相当于 RPM SPEC中 Requires |

| PREREQUISITE_FOR | 该软件支撑了其它软件的运行，不能被完全列举。 |

| HEEDS_BUILD_TOOL | 该软件构建时需要那些软件的支持。相当于 RPM SPEC 中 BuildRequires |