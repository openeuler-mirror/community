# openEuler 仓库配置管理文件格式规范

版本记录：
| 版本 | 作者 | 启用时间 | 变更说明 |
| :-- | :-- | :-- | :-- |
| 1.0| 曹志 George.Cao，胡欣蔚 Shinwell_Hu|  2020-??-?? | 描述初始版本格式以及2.0格式建议 |

## 背景说明

https://gitee.com/openeuler/community 代码仓中 repository 目录下的 openeuler.yaml 和 src-openeuler.yaml 两个文件，管理了整个 openEuler 开源项目中所有代码仓的元数据信息，指导社区自动化工具对这些代码仓的管理。本格式规范是对上述两个配置文件格式的说明，便于各个工具开发团队以及社区贡献者了解如何提交符合要求的Pull Request。

以下各个版本格式规范按时间由近及远排列，便于检索。已停用的格式规范依然在此归档，便于将来回溯查询。

##  版本 2

### 主要改变
- 增加格式版本信息
- 增加代码仓内分支的继承关系信息

### 格式规范

配置文件整体以yaml格式承载，包含三个基本元素：

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
|format_version| 浮点数 |**本版本新增**该配置管理文件版本号，文件格式变更时变更|
|community| 枚举类型，可选 openeuler或者 src-openeuler|组织名称，当前组织名称openeuler和src-openeuler|
|repositories|清单|该组织下所有仓库信息|

repositories清单中每个元素代表一个代码仓，以关系数组的方式呈现，需要包含以下子元素：
| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| name|字符串|仓库名称|
| rename_from|字符串|仓库原名称。这个子元素为可选，只有该代码仓是从另一个代码仓改名而来时才需要|
| description| 字符串 | 仓库包含组件的描述 |
| type|枚举类型，可选 public 或者 private | 仓库类型。private代码仓不提供开放访问|
|upstream|字符串|本代码仓对应的上游社区信息。当 community 为 src-openeuler时，这个子元素必须提供；当 community 为 openeuler 且项目本身就是社区原创项目时，可以不设置|
| branches|清单|**本版本变更**本代码仓下所有分支信息|

branches 清单中每个元素代表一个受管理的分支，以关系数组的方式呈现，需要包含以下子元素:
| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| name| 字符串 | 分支名称 |
| type | 枚举类型，可选protected/readonly |  分支类型，对照码云分支属性设置，protected 表示该分支可以被发布版本集成，readonly 表示该分支停止维护 |
| create_from | 字符串 | 分支创建起点，当 branches.name 为 master 时，字符串为空；新创其他分支时设置已存在的分支名或tag名，缺省为master |

### 说明
当工具处理本文件时未能获取 format_version，可以认为 format_version 为 1.0

后续当format_version变更时，约定若format_version的整数部分不变，则工具可以不做任何修改；若format_version整数部分变动，则所有工具都需要重新适配。

### 样例
```
format_version: 2.0
community: src-openeuler
repositories:
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

## 版本 1

### 主要改变
- openEuler 社区最初版本

### 格式规范

配置文件整体以yaml格式承载，包含两个基本元素：

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| community| 枚举类型，可选 openeuler 或者 src-openeuler | 组织名称|
| repositories| 清单 | 该组织下所有仓库信息，包含子字段 |

repositories清单中每个元素代表一个代码仓，以关系数组的方式呈现，需要包含以下子元素：

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| name | 字符串 |  仓库名称 |
| rename_from|字符串|仓库原名称。这个子元素为可选，只有该代码仓是从另一个代码仓改名而来时才需要|
| description | 字符串 | 仓库信息描述|
| protected_branches| 清单 | 保护分支的分支名列表|
| type| 枚举类型，可选 public 或者 private | 仓库类型。private代码仓不提供开放访问|
|upstream|字符串|本代码仓对应的上游社区信息。当 community 为 src-openeuler时，这个子元素必须提供；否则为可选项 **该子元素为中期添加，当时本文件尚未形成格式版本管理**|

样例：

```
community: src-openeuler
repositories:
- name: A-Tune
  description: 'This is a repo for ……'
  protected_branches:
  - master
  - openEuler-20.03-LTS
  - openEuler-20.09
  type: public
- name: A-Tune-UI
  description: 'Web server for A-Tune'
  upstream: https://gitee.com/openeuler/A-Tune-UI
  protected_branches:
  - master
  type: public
```


