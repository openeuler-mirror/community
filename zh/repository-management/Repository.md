# 仓库管理

## 背景

`repository/` 目录已不再使用，仅用于兼容性保留。openEuler 的仓库配置已迁移到 `sig/` 目录，由各 SIG 在对应目录下维护。

## 新增仓库

- 社区维护项目：在 `sig/<SIG>/openeuler/<首字母>/<仓库名>.yaml` 新建 YAML 文件。
- 引入的软件包：在 `sig/<SIG>/src-openeuler/<首字母>/<仓库名>.yaml` 新建 YAML 文件。

YAML 格式参考 [sig/README.md](/sig/README.md)，操作步骤参考 [新增软件包指南](/zh/contributors/create-package.md)。

## 修改仓库配置

1. 修改对应 SIG 目录下的仓库 YAML 文件。
2. 提交 PR，由 SIG maintainer 和技术委员会审视后合入。
3. PR 合入后，机器人根据 YAML 配置执行仓库创建、成员配置、保护分支等操作。

## 维护人员

维护人员信息按 `OWNERS` > `sig-info.yaml` > 其他配置的优先级管理。具体格式参考 [sig/README.md](/sig/README.md)。
