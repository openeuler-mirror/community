# Computing

- sig范围：操作系统泛计算领域相关的兴趣小组，负责系统中基础功能软件包，C/C++ lib库，设备管理以及其它一些底层lib库，如多媒体相关。
- 工作职责和目标：
    - 现有软件包升级维护。
    - 计算领域中新技术探索的试验田。
    - 提名优秀contributor为committer。

# 组织会议

- 邮件讨论。


# 成员

### Maintainer列表

- liqingqing_1229
- wangbin224
- SuperSix173
- juyin
- yang_yanchao

### Committer列表

- liqingqing_1229
- wangbin224
- SuperSix173
- juyin
- yang_yanchao
- dongjiang1989

committer | 细分领域
------ | ------
SuperSix173 | OSBase
liqingqing_1229 | OSBase
yang_yanchao | OSBase
SuperSix173 | dev-utils
wangbin224 | dev-utils
liqingqing_1229 | C-lib
juyin | C-lib
yang_yanchao | C-lib
SuperSix173 | C-lib
wangbin224 | C-lib
wangbin224 | device-manager
liqingqing_1229 | device-manager
wangbin224 | media
SuperSix173 | media
yang_yanchao | media
wangbin224 | Desktop
liqingqing_1229 | Desktop
dongjiang1989 | CodeC

# 联系方式

- 邮件列表：dev@openeuler.org

# 项目清单

## OSBase 操作系统基础功能   (committer: SuperSix173、yang_yanchao、liqingqing_1229)
  - https://gitee.com/src-openeuler/procps-ng
  - https://gitee.com/src-openeuler/irqbalance
  - https://gitee.com/src-openeuler/psmisc
  - https://gitee.com/src-openeuler/numad
  - https://gitee.com/src-openeuler/kmod
  - https://gitee.com/src-openeuler/tzdata
  - https://gitee.com/src-openeuler/numactl
  - https://gitee.com/src-openeuler/glibc
  - https://gitee.com/src-openeuler/libthai 
  - https://gitee.com/src-openeuler/libinput
  - https://gitee.com/src-openeuler/tuned
  - https://gitee.com/src-openeuler/newlib

## C-lib C/C++ lib库   （committer: yang_yanchao、liqingqing_1229、juyin、SuperSix173、wangbin224）
  - https://gitee.com/src-openeuler/libqb
  - https://gitee.com/src-openeuler/userspace-rcu
  - https://gitee.com/src-openeuler/libatomic_ops
  - https://gitee.com/src-openeuler/boost
  - https://gitee.com/src-openeuler/gperftools
  - https://gitee.com/src-openeuler/libhugetlbfs
  - https://gitee.com/src-openeuler/memkind
  - https://gitee.com/src-openeuler/libevdev
  - https://gitee.com/src-openeuler/mpfr
  - https://gitee.com/src-openeuler/nspr
  - https://gitee.com/src-openeuler/lockdev
  - https://gitee.com/src-openeuler/gmp
  - https://gitee.com/src-openeuler/npth
  - https://gitee.com/src-openeuler/jamm
  - https://gitee.com/src-openeuler/double-conversion
  - https://gitee.com/src-openeuler/ps_mem
  - https://gitee.com/src-openeuler/scipy
  - https://gitee.com/src-openeuler/protobuf-c
  - https://gitee.com/openeuler/libgmem
  - https://gitee.com/src-openeuler/libgmem
  - https://gitee.com/src-openeuler/ORBit2
  - https://gitee.com/src-openeuler/libumem
  - https://gitee.com/src-openeuler/shapelib

## dev-utils 计算领域开发工具  （committer: SuperSix173、 wangbin224）
  - https://gitee.com/src-openeuler/gdb
  - https://gitee.com/src-openeuler/libipt
  - https://gitee.com/src-openeuler/strace
  - https://gitee.com/src-openeuler/systemtap
  - https://gitee.com/src-openeuler/dyninst         
  - https://gitee.com/src-openeuler/lttng-ust  
     
## device-manager 设备管理相关软件   (committer: wangbin224、liqingqing_1229)
  - https://gitee.com/src-openeuler/lm_sensors
  - https://gitee.com/src-openeuler/hwdata
  - https://gitee.com/src-openeuler/hwinfo
  - https://gitee.com/src-openeuler/linux-firmware
  - https://gitee.com/src-openeuler/alsa-firmware
  - https://gitee.com/src-openeuler/alsa-lib
  - https://gitee.com/src-openeuler/alsa-tools
  - https://gitee.com/src-openeuler/dmidecode
  - https://gitee.com/src-openeuler/i2c-tools
  - https://gitee.com/src-openeuler/acpid
  - https://gitee.com/src-openeuler/upower
  - https://gitee.com/src-openeuler/beanstalkd

## media 多媒体相关lib   （committer: SuperSix173、 yang_yanchao、wangbin224）
  - https://gitee.com/src-openeuler/libsamplerate
  - https://gitee.com/src-openeuler/libogg
  - https://gitee.com/src-openeuler/pulseaudio
  - https://gitee.com/src-openeuler/libsndfile
  - https://gitee.com/src-openeuler/flac
  - https://gitee.com/src-openeuler/libijs
  - https://gitee.com/src-openeuler/libmpc
  - https://gitee.com/src-openeuler/libvisual
  - https://gitee.com/src-openeuler/opus

## Desktop 桌面相关lib  （committer: liqingqing_1229、wangbin224）
  - https://gitee.com/src-openeuler/libwacom

## CodeC 编解码lib  （committer: dongjiang1989、left0317）
  - https://gitee.com/openeuler/kspack-go
  - https://gitee.com/openeuler/kspack-c
  - https://gitee.com/openeuler/kspack-java
  - https://gitee.com/openeuler/kspack-rust
# 软件包升级策略
* 结合openEuler软件版本兼容性策略及软件包定级策略以及本SIG软件包特点，软件包整体升级策略如下：
  - level0.5 glibc：兼容性为主，兼顾性能与新特性，master版本与kernel(level0)版本配套升级（glibc版本升级时机在LTS版本的前一年的创新版本，如2603-LTS版本在2509创新版本选型时确认），LTS版本生命周期内原则上不升级版本。
  - 其余软件master版本可根据需要实时升级到最新，如下软件LTS版本生命周期原则上不升级版本，否则容易引起系统变更：
    - level1 alsa-lib
    - level2 boost gmp kmod
    - level3 系统最小集 procps-ng irqbalance kmod npth numactl protobuf-c psmisc gmp tzdata userspace-rcu tuned hwdata mpfr procps-ng dmidecode
  - LTS分支来源于master分支但不完全等同，根据兼容性原则、社区推荐讨论等可能会存在LTS从master分支拉取分支后重新选型的过程，详细参见“openEuler 2403-LTS版本最小集核心软件包选型与降级公式”。

# 参考：
* openEuler软件包管理策略原则：https://gitee.com/openeuler/community/blob/master/zh/technical-committee/governance/software-management.md
* openEuler软件包兼容性分级：https://gitee.com/openeuler/oec-application/blob/master/doc/compatibility_level.md
* openEuler 2403-LTS版本最小集核心软件包选型与降级公式：https://gitee.com/openeuler/release-management/blob/master/openEuler-24.03-LTS/%E6%9C%80%E5%B0%8F%E9%9B%86%E6%A0%B8%E5%BF%83%E5%8C%85%E9%80%89%E5%9E%8B%E5%9F%BA%E7%BA%BF.md
