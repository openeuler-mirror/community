# epkg SIG

## 使命与愿景
epkg sig 致力于打造新型包管理体系，为开发者和用户提供便利的软件发行与安装管理能力:
- 多版本，多环境
- 普通用户安装、定制
- 原子升级，安全回退
- 一次适配，处处运行
- 环境复现，项目协作
- 统一构建，分层定制

## 工作目标和范围

1. epkg包管理器
- 软件管理：安装、卸载、升级
- 环境管理: 创建销毁、注册激活、升级回退、导入导出
- 场景兼容适配: rpm/deb/archlinux, 桌面/服务/AI
- 构建、定制
- 依赖解析
- 信息查询

2. 二进制转换epkg
- x2epkg格式转换工具：rpm/deb/archlinux/alpine/conda
- createrepo工具
- 加包工程

3. openEuler迁移epkg
- spec2yaml转换工具
- hash prefix适配
- yaml字段扩展/适配/维护
- EulerMaker/CompassCI/Mugen支持
- 社区基础设施支持

4. epkg iso
- OS installer
- OS 启动
- OS 升级/回退

5. 原生epkg
- autopkg
- 上游软件CI
- 滚动软件仓

6. 嵌入式场景
- 分层定制
- 交叉编译
- 多架构支持
- muslc库支持
- 软件特性、依赖、分包裁剪
- 编译器、构建选项定制

7. 云原生场景
- KubeOS集成
- epkg image输出轻量容器镜像
- 虚机镜像

8. epkg包管理标准
- yaml格式
- epkg格式
- repo格式
- epkg本地数据库格式
- epkg策略规则
- 分层定制规则

# 组织会议

- 每双周周三下午2:30-4:30
- 会议纪要&议题申报：https://etherpad.openeuler.org/p/sig-epkg-meetings
- 例会固定议题：
  - 遗留问题审视
  - 项目进展跟踪

# 成员

### 维护者

- 吴峰光[@wu_fengguang](https://gitee.com/wu_fengguang)
- 段鹏杰[@duan_pj](https://gitee.com/duan_pj)
- 刘恺[@kailiu42](https://gitee.com/kailiu42)
- 任慰[@vonhust](https://gitee.com/vonhust)
- 陈亚强[@yaqiangchen](https://gitee.com/yaqiangchen)
- FundaWang [@fundawang](https://gitee.com/fundawang)

### 开发者

- 刘星湘[@liuxingxiang](https://gitee.com/liuxingxiang)
- 孙志刚[@zhgsun](https://gitee.com/zhgsun)
- 贾超[@jiachao2130](https://gitee.com/jiachao2130)
- 蒋龙[@jl-brother1](https://gitee.com/jl-brother1)
- 熊开旗[@raccoon-king](https://gitee.com/raccoon-king)
- 陈曾[@zengchen1024](https://gitee.com/zengchen1024)
- 应嘉辉[@rkingkoyo](https://gitee.com/rkingkoyo)
- 邱堂珂[@qiu-tangke](https://gitee.com/qiu-tangke)
- 王章龙[@_coderlong](https://gitee.com/_coderlong)

## 联系方式

- 邮件列表: epkg@openeuler.org


## 项目清单

repository地址：

- https://gitee.com/openeuler/epkg
- https://gitee.com/src-openeuler/epkg
- https://gitee.com/openeuler/meta-openeuler
- https://gitee.com/openeuler/epkg-factory
- https://gitee.com/openeuler/epkg-spec2yaml
- https://gitee.com/openeuler/epkg-autopkg
- https://gitee.com/openeuler/epkg-merge
- https://gitee.com/openeuler/elf-loader
