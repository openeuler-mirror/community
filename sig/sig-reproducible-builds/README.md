# SIG名称
可重复构建SIG (reproducible-builds)

# 概述
可重复构建也被称为确定性编译，是一个编译软件的过程，目标是确保在使用相同的输入时（源代码、工具链、环境变量等）生成的二进制代码可以比特及重现。

## Reproducible-Builds SIG组工作目标和范围

### 工作目标
- 在 openEuler 社区建设RPM体系可重复构建能力; 任意发布RPM包都可还原其源码、构建环境、依赖、构建工程配置等、且再次构建二进制比特位100%一致
- 回合工作成果、并推动上游社区的包达成可重复构建
- 基于核心包、外围包分阶段达成; 对齐Debian社区可重复构建能力

### 工作范围
- 基于 openEuler Release包Policy规范、对影响可重复构建因素进行约束
  
- 加入 https://reproducible-builds.org/ 组织、共享共建复用社区已有能力、并得到国际社区认可
  
- 基于 openEuler 社区建设可重复构建工具链
  
- 建立修复问题、回合上游社区的体系 

- 建立与其他sig 组协同运作机制


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
- 熊风波 [@linxi9527](https://gitee.com/linxi9527) Email: xiongfengbo@huawei.com

# 项目清单
- 项目名称：reproducible-builds
- 项目仓库地址：https://gitee.com/openeuler/reproducible-builds/
- 构建结果看板地址：https://reproducible-builds.openeuler.org/
- 可重复构建国际社区成员：https://reproducible-builds.org/citests/
- sig-reproducible-builds ODD 2022 SIG组规划会议 (2022-04-14)：https://www.bilibili.com/video/BV1qi4y1U79W/?spm_id_from=333.999.0.0&vd_source=d8f1319892ff245c27d83fa9c30b127b

