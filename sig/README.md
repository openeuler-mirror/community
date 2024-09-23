# SIG相关信息的格式化存储

## 背景

本目录下存放的是 openEuler 社区中，所有代码仓与特别兴趣小组 （Special Interest Group，以下简称 SIG）的运作信息。

本目录下每一个子目录，代表一个 SIG。每个 SIG 的目录中，当 OWNERS 文件存在时，SIG 的 maintainer 信息位于 OWNERS 文件中；当 OWNERS 文件不存在时，SIG 的 maintainer 信息位于 sig-info.yaml 文件中。每个 SIG 目录中，按实际管理情况，存在 openeuler 及 src-openeuler 子目录；所有被该 SIG 管理的代码仓，都以相应的独立 YAML 文件描述，存放于这两个子目录中（按首字母细分）。


## 数据存放和管理方式

1. 每个 SIG 在 openeuler/community 仓的 sig 目录中各有一个独立的目录，目录下必须至少存在 OWNERS 文件与 sig-info.yaml 文件其中之一。
2. 原则上由 技术委员会 修改和维护。各个 SIG 所对应的 sig-info.yaml 的修改，由各 SIG 的 maintainer 提交PR，经过技术委员会审视后合入。
3. 信息的权威性，OWNERS > sig-info.yaml > 其他。如果出现信息不一致，以排序最先的 YAML 文件中信息为准。
4. 各 SIG 独立目录下的 README.md 为 SIG 的信息展示区。其中 SIG 基本信息需按模板留空，由工具自动填充。

## 格式规范

### OWNERS 文件格式规范
OWNERS 当前仅仅支持 maintainer 列表，committer列表等没有实际权限配置效用。

### OWNERS 文件样例
```
maintainers:
- %gitee_id%
- %gitee_id2%
```

###  sig-info.yaml 文件格式

sig-info.yaml 文件为yaml格式承载，包含如下基本元素：
| 字段 | 类型 | 说明 |
|--|--|--|
| name | 字符串 | SIG组名称 |
| description | 字符串 | SIG组描述信息 |
| mailing_list | 字符串 | SIG组讨论邮件列表地址 |
| meeting_url | 字符串 | SIG例会纪要URL |
| mentors | 列表 | SIG组当前导师名单 |
| maintainers | 列表 | SIG组所有maintainer名单 |
| security_contacts | 列表 | SIG组安全接口人名单 |
| committers | 列表 | SIG组所有committer名单 |
| contributors | 列表 | SIG组管理仓库的责任人名单 |
| repositories| 列表 | SIG组所管辖的码云仓库信息 |

其中 mentors 列表中每一条记录代表一位 mentor 的个人信息，maintainers 列表中每一条记录代表一位 maintainer 的个人信息， security_contacts 列表中每一条记录代表一位 security_contact 的个人信息。每一条个人信息记录包含如下元素：

| 字段 | 类型 | 说明 |
|--|--|--|
| gitee_id | 字符串 | gitee ID, 必填 |
| name | 字符串 | 姓名(或者网名), 必填 |
| organization| 字符串 | 所在组织或单位, 选填 |
| email| 字符串 | 个人邮箱地址, 必填 |

其中 repositories 列表中每一条记录为SIG所管理的一组仓库信息：

| 字段 | 类型 |  说明 |
|--|--|--|
| repo | 字符串 | 一组SIG仓库 |


repositories的每个repo均由一组具体的仓库名以及committers和contributors组成：
| 字段 | 类型 |  说明 |
|--|--|--|
|  | 字符串 | 仓库全名 |
| committers | 列表 | 参与代码审核的人员 |
| contributors | 列表 | 参与代码仓贡献的其他开发人员 |

其中committers拥有该repo下所有仓库的代码审核权限，contributors是该repo下所有仓库的责任人。committers 列表中每一条记录代表一位 committer 的个人信息， contributors 列表中每一条记录为 仅参与该代码仓的贡献人员个人信息：

### sig-info.yaml 样例：
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
repositories:
- repo: 
  - openeuler/cve-manager
  - openeuler/tool-collections
  - openeuler/go-gitee
  - openeuler/gitbook-theme-hugo
  - cve-manager
- repo: 
  - openeuler/infrastructure
  - openeuler/website
  - openeuler/website-v2
  committers:
  - gitee_id: Bob
    name: BobMa
    email: zzzzzzz@yahoo.com
  contributors:
  - gitee_id: infra_superman
    name: Clark_Ken
    organization: Justice_L
    email: zzzzzzz@openeuler.org
```

### 代码仓描述文件格式

配置文件整体以yaml格式承载，包含如下基本元素：

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| name|字符串|仓库名称|
| rename_from|字符串|仓库原名称。这个子元素为可选，只有该代码仓是从另一个代码仓改名而来时才需要|
| description| 字符串 | 仓库包含组件的描述 |
| type|枚举类型，可选 public 或者 private | 仓库类型。private代码仓不提供开放访问|
|upstream|字符串|本代码仓对应的上游社区信息。当 community 为 src-openeuler时，这个子元素必须提供；当 community 为 openeuler 且项目本身就是社区原创项目时，可以不设置|
| branches|清单|本代码仓下所有分支信息|

branches 清单中每个元素代表一个受管理的分支，以关系数组的方式呈现，需要包含以下子元素:
| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| name| 字符串 | 分支名称 |
| type | 枚举类型，可选protected/readonly |  分支类型，对照码云分支属性设置，protected 表示该分支可以被发布版本集成，readonly 表示该分支停止维护 |
| create_from | 字符串 | 分支创建起点，当 branches.name 为 master 时，字符串为空；新创其他分支时设置已存在的分支名或tag名，缺省为master |

### 代码仓描述文件样例
```
- name: A-Tune
  description: 'This is a repo for ……'
  branches:
  - name: master
    type: protected
  - openEuler-20.03-LTS
    type: protected
    create_from: master
  - openEuler-20.09
    type: protected
    create_from: master
  type: public
- name: A-Tune-UI
  description: 'Web server for A-Tune'
  upstream: https://gitee.com/openeuler/A-Tune-UI
  branches:
  - name: master
    type: protected
  type: public
```
