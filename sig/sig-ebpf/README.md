
# eBPF SIG

## 使命与愿景
eBPF sig致力于为广大用户、开发者、爱好者提供便捷、完备eBPF技术生态、工具，通过扩展内核可编程能力，为广大eBPF技术爱好者提供创新原动力。

## 工作目标和范围

- 编程内核基础框架方向：
  1）eBPF运行时（包括安全、性能等）创新方向；
  2）可编程内核机制（包括网络、存储、调度等）创新方向；
  3）可编程内核能力服务化标准方向（eBPF as Service）；
  可编程内核基础框架方向工作由行业场景+技术创新双驱动（建立与学术界互动的交流机制），通过openEuler创新版本孵化、催熟新技术/机制；另一方面负责将新技术/机制upstream Linux上游社区。
- 业务场景方向：
  1）云原生网络、安全、存储等方向；
  2）车载设备场景；
  3）CT通信场景（包括SRv6）；
  4）运维相关的内核可观测性；
  5）eBPF + AI结合方向；
  6）eBPF + Smart硬件offload方向；
  业务场景方向工作主要由行业场景驱动，提供主流场景的成熟软件解决方案；

# 组织会议

- 每双周周三下午2:30-4:30
- 会议纪要&议题申报：https://etherpad.openeuler.org/p/sig-ebpf-meetings
- 例会固定议题：
  - 遗留问题审视
  - 项目进展跟踪


# sig核心组

### 成员

天翼云：王麟，胡亚弟
华为：陆志浩，魏勇军
软件所：王亚峰
信通院：王小雨
中山大学：陈鹏飞
西邮：陈莉君
锐捷：周超勇
深信服：许庆伟

### 职责

- 负责sig组发展方向，讨论制定sig组重大决定，投票通过议题及项目提案。
- 部分核心成员默认作为maintainer负责社区日常维护 。
- 负责维护sig roadmap以及maintainer、committer成员。

# 成员

### Maintainer列表

- [wangling](https://gitee.com/wonleing) | email:wangl29@chinatelecom.cn
- [luzhihao](https://gitee.com/MrRlu)| email:luzhihao@huawei.com
- [weiyongjun](https://gitee.com/weiyj) | email:weiyongjun1@huawei.com
- [xuqingwei](https://gitee.com/DevinRTK) | email:devin.rtk@gmail.com

### Committer列表
- [zhengyushen](https://gitee.com/yunwei37)
- [shangguandongdong](https://gitee.com/sgdd123)
- [liuxin](https://gitee.com/bitcoffee)
- [wuchangye](https://gitee.com/nlgwcy)
- [luzhihao](https://gitee.com/MrRlu)
- [xiesongyang](https://gitee.com/supercharge)
- [huangliming](https://gitee.com/LemmyHuang)


## 联系方式

- 邮件列表: dev@openeuler.org


## 项目清单
repository地址：

- https://gitee.com/openeuler/Agith
- https://gitee.com/src-openeuler/eunomia-bpf
- https://gitee.com/src-openeuler/libbpf
- https://gitee.com/src-openeuler/bpftrace
- https://gitee.com/src-openeuler/bcc
- https://gitee.com/openeuler/Kmesh
- https://gitee.com/openeuler/gala-gopher

roadmap:
```
eBPF&内核基础：
    20.03 SP3（21.12）：内存I/O预测（内核发布）
    22.03 SP1（22.12）：轻量级eBPF开发框架（eunomia-bpf）、内核可编调度框架（kernel内部发布）
运维&调优&安全：  
    22.09创新版本（22.09）：基于eBPF推进Redis加速（bmctool）
    22.03 SP1（22.12）：基于eBPF的全栈和全链路观测平台（gala-gopher）
    22.03 SP3（23.12）：基于eBPF的配置改变更影响性分析工具（Agith ）
    22.03 SP3（23.12）：基于eBPF的内核泄漏检测分析工具（eArmor）
    23.03创新版本（23.03）：   基于eBPF的OVS流表运维工具（天翼云）
云原生&网络：
     23.03创新版本（23.03）：下一个ServiceMesh数据面（性能10倍提升）（kmesh）
     23.03创新版本（23.03）：基于eBPF的服务网格加速、观察能力（天翼云）
     23.09创新版本（23.09）：基于eBPF的云原生安全规范则正当能力，性能10倍于现在拥有安全能力。（天翼云）
```
