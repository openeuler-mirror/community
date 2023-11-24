# DB
[English](./README.md) | 简体中文

*DB SIG作为工作组，将整个数据库生态系统引入openEuler社区。*<br>
*\*注意\*:由于DB SIG意与全球贡献者一起工作，所以我们建议所有的PR开发流程或issue描述应该是英文版本。*<br>


## DB SIG 工作目标和范围
- 负责openEuler数据库开源软件包的维护，包括Mysql、MariaDB、PostgreSQL。
- 引入更多的OLTP数据库到openEuler，如openGauss或任何其他流行的开源数据库到openEuler社区。
- 围绕数据库引入生态系统工具，构建完整、丰富的数据库生产线软件生态系统。

## Etherpad of DB SIG
- DB SIG介绍及愿景，以及所有链接MAP

  https://etherpad.openeuler.org/p/DB-SIG
- DB SIG内部事务管理，投票及人员信息

  https://etherpad.openeuler.org/p/DB-SIG-inside
- DB SIG相关Working List,不限于SIG内部，对外公开。任何人都可以认领以及求助DB相关的工作。

  https://etherpad.openeuler.org/p/DB-SIG-worklist
- openEuler DB SIG主办或者涉及的线下events活动

  https://etherpad.openeuler.org/p/DB-SIG-events
- DB SIG meeting存档

  https://etherpad.openeuler.org/p/DB-meetings-archive

## DB SIG中软件包的引入范围和引入规则

### DB SIG包引入范围
DB SIG当前处于发展的初始阶段，团队维护能力有限，目前为了切合DB SIG主要目标，优先考虑支持主流开源数据库，包括优先补齐业界主流开源
数据库软件的主流版本。
**在DB SIG成立初期，我们优先接受匹配当前目标的新包或现有包的来进入DB SIG维护**

对于新包的贡献过程应如下所示:
1. 贡献者需要在[openEuler/community](https://gitee.com/openeuler/community)中发布新包提案的PR。
2. 并且@at DB SIG的[Maintainers](https://gitee.com/openeuler/community/tree/master/sig/DB#maintainers)来审查新包提案PR，
然后决定是否接受。也贡献者可以以任何其他方式联系DB SIG维护者，如微信，slack或电子邮件。
3.一旦上述PR从DB SIG的任何[Maintainers](https://gitee.com/openeuler/community/tree/master/sig/DB#maintainers)那里得到一个`/lgtm`，openEuler TC成员只需要合并该PR即可。

### 规则和权限澄清
- 只有DB SIG的[Maintainers](https://gitee.com/openeuler/community/tree/master/sig/DB#maintainers)可以决定是否接受新的包或openEuler中已经存在的DB相关包引入SIG。
- Committers 承担对DB SIG覆盖的项目的正常维护责任。

## 成员

### Maintainer列表
- Zhenyu Zheng[@ZhengZhenyu](https://gitee.com/ZhengZhenyu), *zheng.zhenyu@outlook.com*

### Committer列表
- Qide Chen[@dillon_chen](https://gitee.com/dillon_chen), *dillon.chen@turbolinux.com.cn*
- Zhenyu Zheng[@ZhengZhenyu](https://gitee.com/ZhengZhenyu), *zheng.zhenyu@outlook.com*

### 成员列表
- Junyan Zhang[@zjyabsa](https://gitee.com/zjyabsa/), *jyzhangcf@isoftstone.com*
- Dongxing Wang[@desert-sailor](https://gitee.com/desert-sailor/), *dongxing.wang_a@thundersoft.com*
- GreatSQL[@greatsql_admin](https://gitee.com/GreatSQL/), *jinrong.ye@greatdb.com*

### 已退休
- Bo Zhao[@bzhaoop](https://gitee.com/bzhaoop), *bzhaojyathousandy@gmail.com*

## 组织会议
- 每双周二下午 5:00pm -- 6:00pm

### 联系方式
- [MailList](mailto:dev@openeuler.org) *dev@openeuler.org*
- [slack](https://join.slack.com)
- **微信** *如果您对本SIG组感兴趣，请将您的个人微信账号发给Bo Zhao, 他会将您拉入DB SIG微信群组。*

# 项目清单

*<项目名称和申请表格一致，具体地址可以在申请下来以后在刷新>*

项目名称 && repository地址：
- https://gitee.com/src-openeuler/bucardo
- https://gitee.com/src-openeuler/derby
- https://gitee.com/src-openeuler/firebird
- https://gitee.com/src-openeuler/foomatic
- https://gitee.com/src-openeuler/foomatic-db
- https://gitee.com/src-openeuler/geolatte-geom
- https://gitee.com/src-openeuler/glassfish-legal
- https://gitee.com/src-openeuler/h2
- https://gitee.com/src-openeuler/phoenix
- https://gitee.com/src-openeuler/mariadb-connector-odbc
- https://gitee.com/src-openeuler/mysql5
- https://gitee.com/src-openeuler/percona-server
- https://gitee.com/src-openeuler/percona-toolkit
- https://gitee.com/src-openeuler/percona-xtrabackup
- https://gitee.com/src-openeuler/perl-DBIx-Safe
- https://gitee.com/src-openeuler/pig
- https://gitee.com/src-openeuler/pgadmin4-server
- https://gitee.com/src-openeuler/fastdb
- https://gitee.com/src-openeuler/pgpool2
- https://gitee.com/src-openeuler/postgresql
- https://gitee.com/src-openeuler/postgresql-odbc
- https://gitee.com/src-openeuler/gpdb
- https://gitee.com/src-openeuler/greatsql
- https://gitee.com/src-openeuler/unixODBC
- https://gitee.com/src-openeuler/mariadb
- https://gitee.com/src-openeuler/sqlite
- https://gitee.com/src-openeuler/perl-DBD-SQLite
- https://gitee.com/src-openeuler/perl-DBD-MariaDB
- https://gitee.com/src-openeuler/perl-DBD-MySQL
- https://gitee.com/src-openeuler/mongo-tools
- https://gitee.com/src-openeuler/opengauss-server
- https://gitee.com/src-openeuler/opengauss-dcf
- https://gitee.com/src-openeuler/nanomsg
- https://gitee.com/src-openeuler/apache-orc
- https://gitee.com/src-openeuler/cjson
- https://gitee.com/src-openeuler/tez
- https://gitee.com/src-openeuler/openGemini
- https://gitee.com/openeuler/cantian
- https://gitee.com/openeuler/cantian-connector-mysql
