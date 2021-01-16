# The Configuration Guide of openEuler Repository

Versions：
| version| author | begin | explanation |
| :-- | :-- | :-- | :-- |
| 1.0|  George.Cao，Shinwell_Hu|  2020-11-24 | Describe the format of the initial version and the recommended format of version 2.0. |

## Background

The **openeuler.yaml** and **src-openeuler.yaml** files in the directory of the https://gitee.com/openeuler/community/tree/master/repository manage metadata information of all repositories in openEuler community and guide all automation tools. This document describes the formats of the preceding two configuration files, helping tool-development teams and community contributors understand how to submit pull requests that meet requirements.

The format specifications of the following versions are sorted in descending order of time to facilitate search. Obsoleted format specifications are still archived here for backtracking.

##  Version 2

### Major changes
- Add format version information.
- Add the inheritance relationship information of branches in the repositories.

### Format Guide

The configuration file is in YAML format and contains the following basic elements:

| Name| Type | Remarks|
| :-- | :-- | :-- |
|format_version| float |**New in this version**, Version id of this configuration file. The value is changed when the file format changes.|
|community| enumeration，optional， openeuler or src-openeuler|organization name，current names：openeuler or src-openeuler|
|repositories|list| All repositories under the organization|

Each element in the **repositories** list represents a repository and is presented as a relational array. The following subelements are required:
| Name| Type | Remarks |
| :-- | :-- | :-- |
| name|string|repository name|
| rename_from|string|Original repository name. This sub-element is optional and is required only when the repository is renamed from another repository.|
| description| string | Description of the component contained in the repository |
| type|enumeration，optional，public or private | repository type. The private repository does not provide open access.|
|upstream|string|Indicates the upstream community information of the repository. When organization is src-openeuler, this sub-element must be provided. This parameter is optional when organization is openEuler and the project is an original project of the community.|
| branches|list|**Changed in this version**，Information about all branches in this repository|

Each element in the branches list represents a managed branch and is presented as a relational array. The following sub-elements are required:
| Name| Type | Remarks |
| :-- | :-- | :-- |
| name| string | Branch name |
| type | enumeration，optional，protected/readonly | Branch type. Set this parameter based on Gitee branch attribute. **protected** indicates that the branch can be integrated in the released version. **readonly** indicates that the branch is not maintained.|
| create_from | string |Start point for creating a branch. When **branches.name** is master, this string is empty. Set it the name of an existing branch or tag when creating another branch. The default value is master. |

### Remarks
If the tool fails to obtain **format_version** when processing this, the value of **format_version** is 1.0.

When **format_version** changes later, if the integer part of **format_version** remains unchanged, the tool does not need to be modified. If the integer part of **format_version** changes, all tools need to be adapted again.

### Example
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

## Version 1

### Major changes
- Initial version of the openEuler community

### Format Guide

The configuration file is in YAML format and contains the following basic elements:

|Name | Type | Remarks |
| :-- | :-- | :-- |
|community| enumeration，optional， openeuler or src-openeuler|organization name，current names：openeuler or src-openeuler|
|repositories|list| All repositories under the organization|

Each element in the **repositories** list represents a repository and is presented as a relational array. The following subelements are required:
| Name| Type | Remarks |
| :-- | :-- | :-- |
| name|string|repository name|
| rename_from|string|Original repository name. This sub-element is optional and is required only when the repository is renamed from another repository.|
| description| string | Description of the component contained in the repository |
| protected_branches| list| Name list of the protected branches|
| type|enumeration，optional，public or private | repository type. The private repository does not provide open access.|
|upstream|string|Indicates the upstream community information of the repository. When organization is src-openeuler, this sub-element must be provided. This parameter is optional when organization is openEuler and the project is an original project of the community.|

### example：

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
