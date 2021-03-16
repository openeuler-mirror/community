# SIG相关信息的格式化存储

## 背景

本目录下存放的是 openEuler 社区中，所有 特别兴趣小组 （Special Interest Group，以下简称 SIG）的运作信息。

在openEuler最初的设计中，SIG信息记录在 openeuler/community仓库的sig目录内。其中 SIG 的 maintainer 信息位于相应目录的 OWNER 文件内，而每个SIG所维护的仓库名称列表位于sig.yaml文件内。除此外的信息，包括SIG的邮件列表地址，maintainer的邮件和名字，SIG的描述信息等，都依托SIG的README文件。

为了能够加快 openEuler 社区的自动化工具和流程完善，我们需要提取准确的SIG信息，以支持会议预定、网站展示、代码仓权限管理等。我们重新定义 sigs.yaml 与 sig-info.yaml 文件，统一承载 openEuler 各个 SIG 的格式化信息。

## 数据存放和管理方式

1. openeuler/community 仓的 sig 目录下存在一个 sigs.yaml 文件，这个文件中管理从技术委员会角度看到的所有 SIG 的信息。
2. 每个 SIG 在 openeuler/community 仓的 sig 目录中各有一个独立的目录，其中必须存在一个 sig-info.yaml 文件。
3. sigs.yaml 原则上由 技术委员会 修改和维护。各个 SIG 所对应的 sig-info.yaml 的修改，由各 SIG 的 maintainer 提交PR，经过技术委员会审视后合入。
4. 信息的权威性，sigs.yaml > sig-info.yaml > 其他。如果出现信息不一致，以排序最先的 YAML 文件中信息为准。
5. 各 SIG 独立目录下的 README.md 为 SIG 的信息展示区。其中 SIG 基本信息需按模板留空，由工具自动填充。

##  sigs.yaml 文件格式
sigs.yaml 文件为yaml格式承载，包含如下基本元素：
| 字段 | 类型 | 说明 |
|--|--|--|
| sigs | 列表 | 当前所有 SIG 清单 |

其中 sigs 列表中每一条记录为SIG所管理的一个仓库信息：

| 字段 | 类型 |  说明 |
|--|--|--|
| name | 字符串 | SIG 的正式名称 |
| maturity | 枚举 | 可选为 startup, gratuated, standalone |
| mentors | 列表 | SIG 组当前导师名单 |
| repositories | 列表 | SIGS 组当前负责管理维护的所有代码仓清单 |

其中 mentors 列表中每一条记录代表一位 mentor 的个人信息。每一条个人信息记录包含如下元素：

| 字段 | 类型 | 说明 |
|--|--|--|
| gitee_id | 字符串 | gitee ID, 必填 |
| name | 字符串 | 姓名(或者网名), 必填 |
| organization| 字符串 | 所在组织, 选填 |
| email| 字符串 | 个人邮箱地址, 必填 |

##  sig-info.yaml 文件格式

sig-info.yaml 文件为yaml格式承载，包含如下基本元素：
| 字段 | 类型 | 说明 |
|--|--|--|
| name | 字符串 | SIG组名称 |
| description | 字符串 | SIG组描述信息 |
| mailing_list | 字符串 | SIG组讨论邮件列表地址 |
| meeting_url | 字符串 | SIG例会纪要URL |
| mentors | 列表 | SIG 组当前导师名单 |
| maintainers | 列表 | SIG组所有maintainer名单 |
| security_contacts | 列表 | SIG组安全接口人名单 |
| committers | 列表 | SIG组所有committer名单 |
| repositories| 列表 | SIG组所管辖的码云仓库信息 |

其中 mentors 列表中每一条记录代表一位 mentor 的个人信息，maintainers 列表中每一条记录代表一位 maintainer 的个人信息， security_contacts 列表中每一条记录代表一位 security_contact 的个人信息， committers 列表中每一条记录代表一位 committer 的个人信息。每一条个人信息记录包含如下元素：

| 字段 | 类型 | 说明 |
|--|--|--|
| gitee_id | 字符串 | gitee ID, 必填 |
| name | 字符串 | 姓名(或者网名), 必填 |
| organization| 字符串 | 所在组织, 选填 |
| email| 字符串 | 个人邮箱地址, 必填 |

其中 repositories 列表中每一条记录为SIG所管理的一个仓库信息：

| 字段 | 类型 |  说明 |
|--|--|--|
| repo | 字符串 | 仓库名称 |
| additional_contributors | 列表 | 参与代码仓贡献的其他开发人员 |

其中 additional_contributors 列表中每一条记录为 仅参与该代码仓的贡献人员个人信息：

## sig-info.yaml 样例：
```
name: Infrastructure
description: This is a sample sig. Please copy it over and modify it accordingly.
mailing_list: infra@openeuler.org
meeting_url: NA
mature_level: startup
mentors:
- gitee_id: batMan
  name: Wayne
  email: aaaaaaa@openeuler.org
maintainers:
- gitee_id: Joe
  name: JoeDou
  organization: RealT
  email: yyyyyyy@qq.com
- gitee_id: Jane
  name: JaneDou
  email: xxxxxxx@gmail.com
committers:
- gitee_id: Bob
  name: BobMa
  email: zzzzzzz@yahoo.com
repositories:
- repo: openeuler/infrastructure
  additional_contributors:
  - gitee_id: infra_superman
    name: Clark_Ken
  	orgnization: Justice_L
  	email: zzzzzzz@openeuler.org
- repo: openeuler/blog
- repo: openeuler/go-gitee
```
