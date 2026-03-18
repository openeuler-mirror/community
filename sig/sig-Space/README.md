# SIG-Space

## 背景

- 商业航天（低轨巨型星座、软件定义卫星）与低空经济（无人机、eVTOL）爆发性增长，驱动空间装备向"智能体"演进
- 卫星等空间节点正从独立的信息中继演变为"分布式边缘计算节点"，新一代应用要求实现空天地跨域资源的动态感知、算力协同与任务编排
- 当前空间星载/机载软件多为垂直封闭体系，硬件绑定深，中间件与API不统一，导致重复开发、验证周期漫长，严重阻碍商业航天所需的快速创新节奏
- 故成立此SIG组，面向航天、低空全域空间智能场景，以开放、合作的方式构建高可靠、强实时、智能化的空间计算基础软件生态

## 目标

- 定义空间级操作系统基线：针对星载计算机、地面站、无人机、eVTOL等异构硬件平台，提供统一内核抽象与南向适配层，重点攻关混合关键性部署、安全可信启动及深度功耗管理
- 构筑空间系统高可靠堡垒：将单粒子翻转防护、抗瞬时掉电、故障隔离自愈等空间刚性需求，内化为操作系统级的原生高可靠特性
- 打造机载/在轨智能原生平台能力：推动操作系统与嵌入式AI运行时深度融合，提供从星载/机载轻量化推理、星地/空地协同处理到空天地算力调度的智能基础平台架构
- 建立开放社区，提供空间计算领域的技术交流与信息分享平台

## 业务范围

- 内核实时性与可靠性：深度优化PREEMPT_RT补丁集，探索混合关键性架构（Linux + RTOS）和Rust驱动开发
- 硬件抽象层与BSP：定义标准化板级支持接口，支持ARM、x86、RISC-V、SPARC、鲲鹏、飞腾、瑞芯微、昇腾等多平台
- 可靠性基础服务：容错内存管理、故障管理框架（HM/FDIR）、抗瞬时掉电文件系统
- 协议中间件与协同服务：CCSDS协议栈适配、DDS通信中间件、在轨OTA更新
- 嵌入式AI使能层：轻量化推理引擎优化、星地/空地协同推理框架

## 未来规划

### 第1-3个月：SIG组建与需求明确
- 召开SIG成立暨版本规划会议，公开征集和讨论初始需求，明确技术范围
- 建立SIG沟通渠道（邮件列表、例会制度），完成核心团队组建
- 输出首个版本技术路线图初稿

### 第4-9个月：核心开发与版本迭代
- 完成对QEMU、天数、昇腾、瑞芯微和SPARC等平台的官方BSP支持
- 推动PREEMPT_RT补丁测试、优化与验证
- 启动空间通用基础库与关键协议中间件项目，构建最小系统镜像
- 联合社区推动1-2个星载或机载轻量化AI模型的示范应用落地

### 第10-12个月：版本交付与社区推广
- 发布Space SIG首个正式版本，提供配套文档、镜像及发布说明
- 在openEuler开发者大会或相关Meetup中进行公开成果展示
- 启动下一个开发周期的需求收集与规划

## 组织会议

- 公开的会议时间：TODO（待确定）

## 成员

### Mentor 列表

- 任慰[@vonhust](https://atomgit.com/vonhust): <191362693@qq.com>
- Kai Liu[@kailiu42](https://atomgit.com/kailiu42): <kraml.liu@gmail.com>

### Maintainer 列表

- 任慰[@vonhust](https://atomgit.com/vonhust): <191362693@qq.com>
- 蔡鑫奇[@openHongYu](https://atomgit.com/openHongYu): <caixinqi@yfzx.space>
- 郑国玲[@zhengguoling](https://atomgit.com/zhengguoling): <zhengguoling@cdjrlc.com>
- 李弘宇[@LHY1999](https://atomgit.com/LHY1999): <543306408@qq.com>

### Committer 列表

- 王大维[@david_insist](https://atomgit.com/david_insist): <wangdawei@cdjrlc.com>
- 常亮[@gravityconstant](https://atomgit.com/gravityconstant): <changliang@cdjrlc.com>
- 余孝银[@qq_37212755](https://atomgit.com/qq_37212755): <yuxiaoyin@yfzx.space>
- 张慧鹏[@weixin_40149933](https://atomgit.com/weixin_40149933): <zhanghuipeng@yfzx.space>
- 刘潞[@C6B8B4567](https://atomgit.com/C6B8B4567): <2279372519@qq.com>
- 杨叶轩[@m0_55742107](https://atomgit.com/m0_55742107): <yyxrust@bupt.edu.cn>
- 杨伟[@xiariduoqiu](https://atomgit.com/xiariduoqiu): <yangwei@cdjrlc.com>
- 郑学珍[@zhengxuezhen](https://atomgit.com/zhengxuezhen): <zhengxuezhen@cdjrlc.com>
- 李云峰[@juezhong](https://atomgit.com/juezhong): <liyunfeng@cdjrlc.com>
- 林三虎[@linsanhu](https://atomgit.com/linsanhu): <linsanhu@cdjrlc.com>
- 王帅兵[@shuaibingwi](https://atomgit.com/shuaibingwi): <shuaibingwi@hotmail.com>
- 岳露斌[@qq_43873448](https://atomgit.com/qq_43873448): <1101894816@qq.com>
- 张佳鹏[@jpzhang187](https://atomgit.com/jpzhang187): <jpzhang187@163.com>

## 联系方式

- 邮件列表: <sig-Space@openeuler.org>

## 项目清单

- TODO（待确定）
