# Reproducible-Builds SIG
[English](./sig-reproducible-builds.md) | 简体中文

## Reproducible-Builds SIG组工作目标和范围

### 工作目标
- 在 openEuler 社区建设RPM体系可重复构建能力； 任意发布RPM包都可还原其源码、构建环境、依赖、构建工程配置等、且再次构建二进制比特位100%一致
- 回合工作成果、并推动上游社区的包达成可重复构建；
- 基于核心包、外围包分阶段达成; 对齐Debian社区可重复构建能力；

### 工作范围
- 基于 openEuler Release包Policy规范、对影响可重复构建因素进行约束
  
- 加入 https://reproducible-builds.org/组织、共享共建复用社区已有能力、并得到Reproducible社区认可
  
- 基于 openEuler 社区建设可重复构建工具链
  1. 构建信息buildInfo自动采集含构建环境、源码清单、依赖、工程配置等
  2. 基于buildInfo还原时间、构建环境、工程、依赖等、并重复构建
  3. 二进制比较工具、二进制差异比较可视化、自动定位
  4. 通过自动化CI测试，及时发现问题，问题报告、邮件自动推送、issue自动提交
  5. 对总体情况的统计分析，图表呈现
  6. 常见问题分类、给与自动化修复指导
  7. 支持开发者、合作伙伴本地客户端一键还原构建环境、源码、工程配置等信息，并实现再次编译二进制一致
  
- 建立修复问题、回合上游社区的体系 

- 建立与其他sig 组协同运作机制

- Reproducible-Builds  SIG组所有相关的文档、会议、邮件列表、IRC的管理

### 该SIG管理的repository及描述

- 项目名称：Reproducible-Builds 
- 交付件形式：规则规范、运作章程、自动化工具链、问题修复指导
- Reproducible-Builds  版本的开发工程，包括构建脚本、工程配置等：openeuler/Reproducible-Builds


# 成员

### Maintainers列表
- 刘波 [@robellliu](https://gitee.com/robellliu/) Email: robell.liu@huawei.com
- 吴峰光 [@wu_fengguang](https://gitee.com/wu_fengguang/) Email: wufengguang@huawei.com
- 徐亮 [@wl1587](https://gitee.com/wl1587/) Email: aron.xu@huawei.com
- 曹志 [@georgecao](https://gitee.com/georgecao) Email: caozhi1214@qq.com
- 胡胜 [@TommyLike](https://gitee.com/TommyLike) Email: tommylikehu@gmail.com

### Committers列表
- 刘路 [@pubian](https://gitee.com/pubian/) Email: liulu99@huawei.com
- 赵栩锋 [@zxf_0731](https://gitee.com/zxf_0731/) Email: zhaoxufeng5@huawei.com
- 文豪 [@wenhao7](https://gitee.com/wenhao7/) Email: wenhao7@huawei.com

# 邮件列表

[邮件列表](dev@openeuler.org)

# IRC 频道
openeuler-Reproducible-Builds

