
# openEuler RISC-V 兴趣组
[English](./sig-template.md) | 简体中文

RISC-V 是一个免费开源的指令集（ISA）。RISC-V SIG 组旨在提供 openEuler_RISC-V 版本，并且提供 openEuler_RISC-V 的软件包构建、系统构建等指导，使对 RISC-V 感兴趣的开发者能够参与到开源系统开发中活动中来。

说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

## RISC-V SIG组工作目标和范围

工作目标：

 - 构建 openEuler 支持 RISC-V 架构（包括模拟器和硬件平台）

 - 源代码在 gitee 上开源，保持 openEuler_RISC-V 源码与 openEuler 主线保持一致，定期推送/回合 RISC-V 补丁到openEuler主线；
 
 - 提供可直接获取的 openEuler_RISC-V 的 rpm repo 以及 系统镜像

 - 提供用于构建 openEuler_RISC-V 系统的工具

 - 提供友好的文档用于指导构建与定制 openEuler_RISC-V 

 - 维护 openEuler_RISC-V 每日构建工程以及测试验证系统，提供自动化构建服务

 - 相应用户反馈，解决相应问题

 - 根据 RISC-V 指令集特点引入软件包，推动 openEuler 软件包数量扩容

 工作范围：

 - 制定 RISC-V SIG 组的工作流程、软件包规划、路线图等
 
 - 利用 openEuler 开源代码构建 openEuler_RISC-V 版本、

 - 识别 RISC-V 相关的补丁和修改，保持源码与 openEuler 主线保持一致

 - 制作用于半自动构建的工具 

 - 维护 openEuler_RISC-V 相关的文档、会议、邮件列表、IRC管理

 - 维护托管 openEuler_RISC-V 的 repo


 交付件：

 - RPM repo 源，openEuler_RISC-V 系统镜像，构建手册，自动化构建服务


 ### News

 _9 Jun 2020_ 大部分src-openEuler 主线代码支持RISC-V；增加自动化制作openEuler-RISC-V rootfs image 工具；
 增加[最小系统包范围定义](https://gitee.com/whoisxxx/autobuild-openeuler4riscv/blob/master/assets/Core_openEuler-20.03-LTS.list)；
 使能rv64g 编码工具链进行第二轮bootstrap 构建

 _18 may 2020_ stage1 阶段第一轮构建完成，通过[这里](https://isrc.iscas.ac.cn/mirror/openeuler-sig-riscv/)访问；建立openEuler4riscv[自动化构建工具仓](https://gitee.com/openeuler/autobuild-openeuler4riscv/commits/master)

 _28 Apr 2020_ The [OpenEuler SIG](https://gitee.com/openeuler/community/tree/master/sig/sig-RISC-V) set up.

 ### 该SIG管理的repository及描述
此处列出来的包为已构建成功的 RISC-V 版本软件包
这里的软件包版本策略为：
```
 1. 优先使用 openEuler 主线代码
 2. 若需要修改，RISC-V 补丁 合入 openEuler 主线，完成合入之前在个人仓
 3. 若版本不同，代码在个人仓托管，在引入时需要和相应软件包的SIG 负责团队讨论，制定版本计划：
    a. 版本策略（回合/升级/不回合）
    b. 制定 回合/升级 的计划 
```

```
  - 构建工具和 RISC-V 文档
    - https://gitee.com/openeuler/autobuild-openeuler4riscv

```

- 当前项目 包含的软件包 总数：896

### 涉及到修改的软件包 总数：19


| 软件包名称    | 状态   | 详情  | 链接  |
| ------------ | ----- | --------- | ---- | 
| LinuxKernel   |  待新开分支<br>5.5?<br>| 1. 4.19支持不完善<br>2. kernel仓开一分支，未来收编<br>3. defconfig 暂时使用arch/riscv/config默认<br>4. 暂时只使用源码仓不使用构建仓 | https://gitee.com/openeuler/kernel/issues/I1JE44#note_2639660                                     |
| gcc           |  待新开分支            | 1.  默认使用 rv64g 编码 <br> 2.  应用工具链的二进制进行自举构建 <br> 3. 代码开源节奏仍在讨论中                                                                  | 已单点讨论，尚未在社区讨论                                                                        |
| glibc         | 2.28-> 2.31 ?                | 1. glibc 期望升级，现有2.28 需要大量回合工作                                                                                                           | 已单点讨论，尚未在社区讨论                                                                        |
| gdb           |                            | 同上                                                                                                                                                   | 同上                                                                                              |
| libseccomp    | 待升级 <br> 2.4.1->2.4.3 <br>       | 1. libseccomp 2.4.3 为2020.03发布，尚未包含RISC-V支持；<br> 2. master分支已包含支持；<br>3. 需要升级并回合补丁 | 已内部对齐，issue跟踪<br>https://gitee.com/src-openeuler/libseccomp/issues/I1JEGY?from=project-issue |
| systemd       | PR待合入                   | systemd-243中riscv不支持gnu-EFI启动，需要修改configure；<br> 并且spec文件中打包的过程要根据架构去掉相应的文件    | https://gitee.com/src-openeuler/systemd/pulls/31                                                  |
| grub2         | 待升级 <br> 2.02->2.04 <br> 暑期任务 | 1. grub2 从2.04 之后支持RISC-V <br> 2. 目前启动方式为 openSBI+ flatten Image ，未使用grub引导 <br>3. 已提交暑期任务 为openEuler - RISC-V 添加grub的引导启动方式 | https://gitee.com/openeuler/marketing/issues/I1I1TS                                               |
| golang        | 暑期任务                   | 1. golang 尚未支持RISC-V                                                                                                                               | https://gitee.com/openeuler/marketing/issues/I1IKOI                                               |
| docker/iSulad | 暑期任务                   | 1. RISC-V上尚没有可用的容器引擎                                                                                                                        | https://gitee.com/openeuler/marketing/issues/I1IKQO                                               |
| openssh       | PR待合入                   | disable seccomp_filter                                                                                                                              | https://gitee.com/src-openeuler/openssh/pulls/10                                                  |
| pcre          | PR待合入                   | disable jit                                                                                                                                            | https://gitee.com/src-openeuler/pcre/pulls/6                                                      |
| pcre2         | PR待合入                   | disable jit                                                                                                                                            | https://gitee.com/src-openeuler/pcre2/pulls/5                                                     |
| libsecret     | PR待合入                   | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/libsecret/pulls/1                                                 |
| star          | PR待合入                   | %prep阶段增加riscv配置                                                                                                                                 | https://gitee.com/src-openeuler/star/pulls/3                                                      |
| python2       | PR待合入                   | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/python2/pulls/16                                                  |
| diffutils     | PR待合入                   | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/diffutils/pulls/3                                                 |
| libffi        | PR待合入                   | disable-multi-os-directory                                                                                                                             | https://gitee.com/src-openeuler/libffi/pulls/12                                                   |
| libtasn1      | 已合入                     | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/libtasn1/pulls/3                                                  |
| libmodulemd   | 已合入                     | valgrind                                                                                                                                               | https://gitee.com/src-openeuler/libmodulemd/pulls/1                                               |

### 使用src-openEuler 主线的软件包
```
      /adcli-0.8.2-6.src.rpm
      /anaconda-user-help-26.1-9.src.rpm
      /adobe-mappings-cmap-20190730-2.src.rpm
      /adobe-mappings-pdf-20190401-1.src.rpm
      /alsa-firmware-1.0.29-10.src.rpm
      /alsa-lib-1.1.6-6.src.rpm
      /anthy-9100h-39.src.rpm
      /acl-2.2.53-7.src.rpm
      /apache2-mod_xforward-0.6-lp151.1.2.src.rpm
      /argon2-20161029-9.src.rpm
      /arptables-0.0.4-16.src.rpm
      /arpwatch-2.1a15-44.src.rpm
      /asciidoc-8.6.10-3.src.rpm
      /aspell-0.60.6.1-25.src.rpm
      /atf-0.20-13.src.rpm
      /atk-2.30.0-3.src.rpm
      /atkmm-2.24.2-8.src.rpm
      /atmel-firmware-1.3-20.src.rpm
      /at-spi2-atk-2.30.0-2.src.rpm
      /attr-2.4.48-8.src.rpm
      /audiofile-0.3.6-24.src.rpm
      /autoconf213-2.13-42.src.rpm
      /autoconf-archive-2018.03.13-3.src.rpm
      /autogen-5.18.14-4.src.rpm
      /automake-1.16.1-6.src.rpm
      /babl-0.1.56-3.src.rpm
      /basesystem-12-1.src.rpm
      /bash-5.0-12.src.rpm
      /bash-completion-2.8-9.src.rpm
      /bc-1.07.1-10.src.rpm
      /bison-3.5-2.src.rpm
      /bridge-utils-1.6-4.src.rpm
      /brotli-1.0.5-3.src.rpm
      /byacc-1.9.20170709-9.src.rpm
      /bzip2-1.0.8-3.src.rpm
      /ca-certificates-2020.2.40-1.src.rpm
      /cachefilesd-0.10.10-6.src.rpm
      /cdparanoia-10.2-30.src.rpm
      /chrpath-0.16-11.src.rpm
      /cim-schema-2.43.0-8.src.rpm
      /cldr-emoji-annotation-33.1.0_0-3.src.rpm
      /cloud-utils-0.31-1.src.rpm
      /cmocka-1.1.5-2.src.rpm
      /color-filesystem-1-14.src.rpm
      /convmv-2.05-5.src.rpm
      /copy-jdk-configs-3.7-3.src.rpm
      /cpio-2.12-14.src.rpm
      /cracklib-2.9.7-2.src.rpm
      /CreateImage-0.0.5-31oe1.src.rpm
      /cronie-1.5.4-5.src.rpm
      /crontabs-1.11-21.src.rpm
      /crypto-policies-20180925-3.git71ca85f.src.rpm
      /ctags-5.8-27.src.rpm
      /CUnit-2.1.3-21.src.rpm
      /custom_build_tool-1.0-17oe1.src.rpm
      /dbus-1.12.16-13.src.rpm
      /dbus-glib-0.110-5.src.rpm
      /debootstrap-1.0.109-3.src.rpm
      /dejagnu-1.6.1-5.src.rpm
      /dejavu-fonts-2.35-8.src.rpm
      /desktop-file-utils-0.24-1.src.rpm
      /dhcp-4.3.6-37.src.rpm
      /diffstat-1.62-3.src.rpm
      /dkms-2.6.1-5.src.rpm
      /docbook5-style-xsl-1.79.2-8.src.rpm
      /docbook-dtds-1.0-78.src.rpm
      /docbook-style-dsssl-1.79-27.src.rpm
      /docbook-style-xsl-1.79.2-9.src.rpm
      /docker-compose-1.22.0-2.src.rpm
      /dos2unix-7.4.0-11.src.rpm
      /dosfstools-4.1-7.src.rpm
      /dotconf-1.3-22.src.rpm
      /dvd+rw-tools-7.1-31.src.rpm
      /dwz-0.12-11.src.rpm
      /e2fsprogs-1.45.3-4.src.rpm
      /ebtables-2.0.10-32.src.rpm
      /ed-1.14.2-6.src.rpm
      /efi-rpm-macros-4-2.src.rpm
      /eglexternalplatform-1.1-0.2.src.rpm
      /elfutils-0.177-3.src.rpm
      /elinks-0.12-1.src.rpm
      /emacs-auctex-12.1-8.src.rpm
      /ethtool-5.3-2.src.rpm
      /expat-2.2.6-5.src.rpm
      /fakechroot-2.19-8.src.rpm
      /fdupes-1.6.1-6.src.rpm
      /file-roller-3.30.1-2.src.rpm
      /filesystem-3.9-3.src.rpm
      /findutils-4.7.0-4.src.rpm
      /fipscheck-1.5.0-7.src.rpm
      /flex-2.6.1-13.src.rpm
      /fonts-rpm-macros-2.0.2-2.src.rpm
      /fpaste-0.4.0.0-1.src.rpm
      /freetype-2.9.1-5.src.rpm
      /fribidi-1.0.5-4.src.rpm
      /fros-1.1-18.src.rpm
      /fuse-2.9.9-0.src.rpm
      /fuse-python-0.2.1-24.src.rpm
      /fxload-2008_10_13-14.src.rpm
      /gamin-0.1.10-37.src.rpm
      /gcab-1.1-4.src.rpm
      /gcc_secure-1.0-0.6.src.rpm
      /gcr-3.34.0-1.src.rpm
      /gd-2.2.5-6.src.rpm
      /gdb-8.3.50.20190321-4.0.riscv64oe1.src.rpm
      /gdbm-1.18-2.src.rpm
      /gdk-pixbuf2-2.38.0-9.src.rpm
      /gdm-3.30.1-7.src.rpm
      /openEuler-indexhtml-7-14.src.rpm
      /openEuler-release-20.03LT
      /openEuler-repos-1.0-2.5.src.rpm
      /openEuler-rpm-config-30-9.src.rpm
      /GeoIP-1.6.12-5.src.rpm
      /GeoIP-GeoLite-data-2018.06-3.src.rpm
      /geolite2-20181002-2.src.rpm
      /gflags-2.1.2-9.src.rpm
      /glib-1.2.10-55.src.rpm
      /glibc-2.29.9000-8oe1.src.rpm
      /gmp-6.1.2-10.src.rpm
      /gnome-common-3.18.0-7.src.rpm
      /gobject-introspection-1.58.0-6.src.rpm
      /gperf-3.1-7.src.rpm
      /gpm-1.20.7-21.src.rpm
      /grep-3.4-0.src.rpm
      /groff-1.22.4-4.src.rpm
      /gsm-1.0.18-4.src.rpm
      /gzip-1.9-18.src.rpm
      /hardlink-1.0-24.src.rpm
      /haveged-1.9.8-2.src.rpm
      /hdparm-9.56-4.src.rpm
      /help2man-1.47.11-0.src.rpm
      /hfsplus-tools-540.1.linux3-17.src.rpm
      /hicolor-icon-theme-0.17-4.src.rpm
      /hostname-3.20-7.src.rpm
      /hwdata-0.316-3.src.rpm
      /hyphen-2.8.8-13.src.rpm
      /i2c-tools-4.1-1.src.rpm
      /icfg-0.9-18.src.rpm
      /icoutils-0.32.3-4.src.rpm
      /initscripts-10.01-6.src.rpm
      /intltool-0.51.0-14.src.rpm
      /iotop-0.6-20.src.rpm
      /iperf3-3.6-4.src.rpm
      /iproute-5.4.0-2.src.rpm
      /iptables-1.8.1-4.src.rpm
      /iputils-20190709-2.src.rpm
      /ipxe-20190930-5.src.rpm
      /irqbalance-1.4.0-18.src.rpm
      /iso-codes-3.79-4.src.rpm
      /itstool-2.0.4-5.src.rpm
      /ivtv-firmware-20080701-36.src.rpm
      /jbig2dec-0.16-2.src.rpm
      /jbigkit-2.1-17.src.rpm
      /jemalloc-5.1.0-3.src.rpm
      /jfsutils-1.1.15-14.src.rpm
      /json-c-0.13.1-6.src.rpm
      /Judy-1.0.5-19.src.rpm
      /kde-filesystem-4-62.src.rpm
      /kde-settings-29.1-3.src.rpm
      /keyrings-filesystem-1-12.src.rpm
      /keyutils-1.5.10-11.src.rpm
      /kmod-25-6.src.rpm
      /lcms2-2.9-7.src.rpm
      /less-551-3.src.rpm
      /libaec-1.0.4-1.src.rpm
      /libaesgm-20090429-21.src.rpm
      /libaio-0.3.111-5.src.rpm
      /libarchive-3.4.1-2.src.rpm
      /libart_lgpl-2.3.21-23.src.rpm
      /libasyncns-0.8-17.src.rpm
      /libatomic_ops-7.6.10-2.src.rpm
      /libcap-2.27-1.src.rpm
      /libcap-ng-0.7.9-7.src.rpm
      /libcgroup-0.41-23.src.rpm
      /libdaemon-0.14-20.src.rpm
      /libdatrie-0.2.12-1.src.rpm
      /libdbi-0.9.0-15.src.rpm
      /libdbusmenu-16.04.0-10.src.rpm
      /libdvdread-6.0.0-3.src.rpm
      /libecap-1.0.1-4.src.rpm
      /libedit-3.1-26.src.rpm
      /libell-0.9-2.src.rpm
      /libesmtp-1.0.6-18.src.rpm
      /libestr-0.1.9-12.src.rpm
      /libev-4.24-11.src.rpm
      /libevdev-1.5.9-6.src.rpm
      /libevent-2.1.11-2.src.rpm
      /libevhtp-1.2.16-3.src.rpm
      /libfastjson-0.99.8-3.src.rpm
      /libgcrypt-1.8.3-5.src.rpm
      /libgpg-error-1.35-3.src.rpm
      /libhbaapi-2.2.9-1.src.rpm
      /libICE-1.0.10-2.src.rpm
      /libid3tag-0.15.1b-20.src.rpm
      /libidn2-2.0.5-8.src.rpm
      /libijs-0.35-9.src.rpm
      /libimagequant-2.12.5-2.src.rpm
      /liblognorm-2.0.3-7.src.rpm
      /libmad-0.15.1b-28.src.rpm
      /libmaxminddb-1.2.0-7.src.rpm
      /libmetalink-0.1.3-8.src.rpm
      /libmicrohttpd-0.9.59-4.src.rpm
      /libmnl-1.0.4-10.src.rpm
      /libmodman-2.0.1-19.src.rpm
      /libmpc-1.1.0-3.src.rpm
      /libmpcdec-1.2.6-23.src.rpm
      /libmspack-0.7-0.1.6.src.rpm
      /libndp-1.7-3.src.rpm
      /libnet-1.1.6-17.src.rpm
      /libnetfilter_conntrack-1.0.6-7.src.rpm
      /libnetfilter_cthelper-1.0.0-15.src.rpm
      /libnetfilter_cttimeout-1.0.0-13.src.rpm
      /libnetfilter_queue-1.0.2-13.src.rpm
      /libnfnetlink-1.0.1-15.src.rpm
      /libnfs-1.11.0-4.src.rpm
      /libnftnl-1.1.1-6.src.rpm
      /libnl3-3.5.0-1.src.rpm
      /libnsl2-1.2.0-4.src.rpm
      /libogg-1.3.3-3.src.rpm
      /libomxil-bellagio-0.9.3-21.src.rpm
      /libpaper-1.1.24-25.src.rpm
      /libpcap-1.9.1-4.src.rpm
      /libpng12-1.2.57-10.src.rpm
      /libpsl-0.20.2-9.src.rpm
      /librabbitmq-0.9.0-3.src.rpm
      /libraw1394-2.1.2-8.src.rpm
      /librdkafka-0.11.4-3.src.rpm
      /librelp-1.2.16-3.src.rpm
      /libsemanage-2.9-2.src.rpm
      /libsepol-2.9-1.src.rpm
      /libsigc++20-2.10.1-2.src.rpm
      /libsigsegv-2.11-10.src.rpm
      /libsmi-0.4.8-24.src.rpm
      /libspiro-20150131-10.src.rpm
      /libsrtp-1.5.4-10.src.rpm
      /libssh2-1.9.0-2.src.rpm
      /libstemmer-0-12.src.rpm
      /libtar-1.2.20-17.src.rpm
      /libtheora-1.1.1-24.src.rpm
      /libtirpc-1.1.4-1.src.rpm
      /libtool-2.4.6-32.src.rpm
      /libunistring-0.9.10-7.src.rpm
      /libusb-0.1.5-15.src.rpm
      /libusbmuxd-1.0.10-12.src.rpm
      /libusbx-1.0.22-2.src.rpm
      /libutempter-1.1.6-16.src.rpm
      /libuv-1.23.0-2.src.rpm
      /libverto-0.3.1-2.src.rpm
      /libvisual-0.4.0-27.src.rpm
      /libvoikko-4.1.1-3.src.rpm
      /libx86emu-1.11-4.src.rpm
      /libXau-1.0.9-2.src.rpm
      /libXaw-1.0.13-13.src.rpm
      /libxcrypt-4.4.8-4.src.rpm
      /libXdmcp-1.1.3-2.src.rpm
      /libXext-1.3.4-2.src.rpm
      /libxkbcommon-0.8.4-3.src.rpm
      /libxkbfile-1.1.0-2.src.rpm
      /libXmu-1.1.3-1.src.rpm
      /libXpm-3.5.12-11.src.rpm
      /libxslt-1.1.32-7.src.rpm
      /libXt-1.1.5-11.src.rpm
      /libXtst-1.2.3-10.src.rpm
      /libyaml-0.2.2-2.src.rpm
      /libzip-1.5.1-3.src.rpm
      /linux-firmware-20190815-4.src.rpm
      /linuxptp-2.0-3.src.rpm
      /lksctp-tools-1.0.16-11.src.rpm
      /lmdb-0.9.22-4.src.rpm
      /lockdev-1.0.4-0.31.src.rpm
      /logrotate-3.15.1-2.src.rpm
      /logwatch-7.5.2-2.src.rpm
      /lrzsz-0.12.20-46.src.rpm
      /lsscsi-0.30-2.src.rpm
      /lua-expat-1.3.0-16.src.rpm
      /lua-filesystem-1.6.3-10.src.rpm
      /lua-json-1.3.2-13.src.rpm
      /lua-lpeg-1.0.2-2.src.rpm
      /lua-lunit-0.5-15.src.rpm
      /lua-socket-3.0-0.19.src.rpm
      /lvm2-2.02.181-8.src.rpm
      /lz4-1.9.2-2.src.rpm
      /lzo-2.10-1.src.rpm
      /lzop-1.04-1.src.rpm
      /m4-1.4.18-13.src.rpm
      /mac-robber-1.02-18.src.rpm
      /mailcap-2.1.48-6.src.rpm
      /mailx-12.5-32.src.rpm
      /make-4.2.1-15.src.rpm
      /mallard-rng-1.0.3-4.src.rpm
      /man-db-2.8.7-5.src.rpm
      /man-pages-5.02-4.src.rpm
      /mariadb-connector-c-3.0.6-6.src.rpm
      /mcpp-2.7.2-25.src.rpm
      /meson-0.51.1-3.src.rpm
      /mlocate-0.26-24.src.rpm
      /mobile-broadband-provider-info-20190116-1.src.rpm
      /mozilla-filesystem-1.9-21.src.rpm
      /mpfr-3.1.6-3.src.rpm
      /mrtg-2.17.7-3.src.rpm
      /mtdev-1.1.5-15.src.rpm
      /mt-st-1.1-25.src.rpm
      /mtx-1.3.12-21.src.rpm
      /multilib-rpm-config-1-14.src.rpm
      /mypaint-brushes-1.3.0-3.src.rpm
      /ncompress-4.2.4.4-18.src.rpm
      /ndisc6-1.0.4-1.src.rpm
      /neon-0.30.2-9.src.rpm
      /nettle-3.4.1rc1-4.src.rpm
      /net-tools-2.0-0.54.src.rpm
      /npth-1.5-7.src.rpm
      /nss-altfiles-2.18.1-8.src.rpm
      /nss_wrapper-1.1.3-2.src.rpm
      /ntpstat-0.5-3.src.rpm
      /numactl-2.0.13-4.src.rpm
      /numad-0.5-31.src.rpm
      /nvme-cli-1.6-2.src.rpm
      /obs-env-1.0-5.src.rpm
      /obs-service-download_files-0.6.2-0.src.rpm
      /obs-service-extract_file-0.3-4.src.rpm
      /obs-service-rust2rpm-1-3.src.rpm
      /obs-service-set_version-0.5.10-5.src.rpm
      /oniguruma-6.9.0-2.src.rpm
      /opencc-1.0.5-4.src.rpm
      /openEuler-logos-1.0-6.src.rpm
      /openssl-pkcs11-0.4.10-1.src.rpm
      /opus-1.3.1-1.src.rpm
      /os-prober-1.74-12.src.rpm
      /p11-kit-0.23.14-6.src.rpm
      /parted-3.3-2.src.rpm
      /passwd-0.80-7.src.rpm
      /patch-2.7.6-12.src.rpm
      /patchutils-0.3.4-13.src.rpm
      /pax-3.4-34.src.rpm
      /pciutils-3.6.2-5.src.rpm
      /pigz-2.4-7.src.rpm
      /pkcs11-helper-1.25.1-1.src.rpm
      /pkgconf-1.6.3-6.src.rpm
      /pnm2ppa-1.04-42.src.rpm
      /policycoreutils-2.8-14.src.rpm
      /poppler-data-0.4.9-4.src.rpm
      /popt-1.16-17.src.rpm
      /pps-tools-1.0.2-3.src.rpm
      /pptp-1.10.0-6.src.rpm
      /prefetch_tuning-1.0-2.src.rpm
      /procmail-3.22-50.src.rpm
      /procps-ng-3.3.16-11.src.rpm
      /proj-4.9.3-8.src.rpm
      /psacct-6.6.4-4.src.rpm
      /psutils-1.23-16.src.rpm
      /python2-typing-3.6.2-4.src.rpm
      /python3-mallard-ducktype-0.3-5.src.rpm
      /python-alsa-1.1.6-1.src.rpm
      /python-aniso8601-7.0.0-1.src.rpm
      /python-apipkg-1.5-2.src.rpm
      /python-argcomplete-1.9.5-2.src.rpm
      /python-asn1crypto-0.24.0-8.src.rpm
      /python-atomicwrites-1.1.5-13.src.rpm
      /python-attrs-17.4.0-9.src.rpm
      /python-augeas-0.5.0-16.src.rpm
      /python-backports-1.0-17.src.rpm
      /python-backports_abc-0.5-9.src.rpm
      /python-backports-ssl_match_hostname-3.7.0.1-2.src.rpm
      /python-backports-unittest_mock-1.2.1-7.src.rpm
      /python-bcrypt-3.1.4-7.src.rpm
      /python-beautifulsoup4-4.6.3-2.src.rpm
      /python-blinker-1.4-4.src.rpm
      /python-bottle-0.12.13-7.src.rpm
      /python-cached_property-1.5.1-1.src.rpm
      /python-cffi-1.11.5-10.src.rpm
      /python-chardet-3.0.4-8.src.rpm
      /python-cheetah-3.1.0-7.src.rpm
      /python-cherrypy-3.5.0-12.src.rpm
      /python-click-7.0-1.src.rpm
      /python-configobj-5.0.6-15.src.rpm
      /python-configparser-3.5.0b2-11.src.rpm
      /python-configshell-1.1.27-1.src.rpm
      /python-constantly-15.1.0-4.src.rpm
      /python-construct-2.5.1-19.src.rpm
      /python-contextlib2-0.5.5-9.src.rpm
      /python-coverage-4.5.3-1.src.rpm
      /python-cryptography-vectors-2.6.1-1.src.rpm
      /python-cups-1.9.72-23.src.rpm
      /python-cycler-0.10.0-2.src.rpm
      /python-dateutil-2.7.0-7.src.rpm
      /python-decorator-4.3.0-3.src.rpm
      /python-dict2xml-1.6.1-1.src.rpm
      /python-distro-1.3.0-5.src.rpm
      /python-dmidecode-3.12.2-17.src.rpm
      /python-dns-1.15.0-10.src.rpm
      /python-docker-4.0.2-1.src.rpm
      /python-dockerpty-0.4.1-1.src.rpm
      /python-docker-pycreds-0.4.0-1.src.rpm
      /python-docopt-0.6.2-11.src.rpm
      /python-ecdsa-0.14.1-1.src.rpm
      /python-enchant-2.0.0-6.src.rpm
      /python-entrypoints-0.2.3-10.src.rpm
      /python-enum34-1.1.6-8.src.rpm
      /python-ethtool-0.14-2.src.rpm
      /python-evdev-1.1.2-5.src.rpm
      /python-execnet-1.5.0-5.src.rpm
      /python-extras-1.0.0-6.src.rpm
      /python-filelock-3.0.12-1.src.rpm
      /python-fixtures-3.0.0-12.src.rpm
      /python-flask-1.0.4-3.src.rpm
      /python-flask-restful-0.3.6-10.src.rpm
      /python-flit-1.0-5.src.rpm
      /python-freezegun-0.3.8-12.src.rpm
      /python-funcsigs-1.0.2-13.src.rpm
      /python-futures-3.1.1-5.src.rpm
      /python-genshi-0.7-23.src.rpm
      /python-gflags-2.0-16.src.rpm
      /python-google-apputils-0.4.2-15.src.rpm
      /python-hamcrest-1.9.0-8.src.rpm
      /python-html5lib-1.0.1-5.src.rpm
      /python-httplib2-0.13.1-4.src.rpm
      /python-humanize-0.5.1-16.src.rpm
      /python-hwdata-2.3.7-5.src.rpm
      /python-hyperlink-18.0.0-8.src.rpm
      /python-hypothesis-3.66.11-2.src.rpm
      /python-idna-2.8-3.src.rpm
      /python-imagesize-1.0.0-4.src.rpm
      /python-incremental-17.5.0-5.src.rpm
      /python-iniparse-0.4-36.src.rpm
      /python-inotify-0.9.6-16.src.rpm
      /python-ipaddress-1.0.18-9.src.rpm
      /python-IPy-0.81-26.src.rpm
      /python-iso8601-0.1.11-2.src.rpm
      /python-itsdangerous-1.1.0-1.src.rpm
      /python-jinja2-2.10-10.src.rpm
      /python-jsonpatch-1.21-5.src.rpm
      /python-jsonpointer-1.10-15.src.rpm
      /python-jsonschema-2.6.0-6.src.rpm
      /python-junitxml-0.7-17.src.rpm
      /python-jwt-1.7.1-2.src.rpm
      /python-keyczar-0.71c-13.src.rpm
      /python-kitchen-1.2.6-1.src.rpm
      /python-kiwisolver-1.1.0-3.src.rpm
      /python-kmod-0.9-21.src.rpm
      /python-ldap-3.1.0-1.src.rpm
      /python-linecache2-1.0.0-18.src.rpm
      /python-linux-procfs-0.5.1-8.src.rpm
      /python-lit-0.7.0-3.src.rpm
      /python-logutils-0.3.5-7.src.rpm
      /python-markdown-2.4.1-13.src.rpm
      /python-markupsafe-1.0-3.src.rpm
      /python-meh-0.47-4.src.rpm
      /python-memcached-1.58-1.src.rpm
      /python-mimeparse-1.6.0-8.src.rpm
      /python-mock-2.0.0-11.src.rpm
      /python-more-itertools-4.1.0-5.src.rpm
      /python-mox-0.5.3-18.src.rpm
      /python-mysqlclient-1.3.12-7.src.rpm
      /python-netaddr-0.7.19-14.src.rpm
      /python-nose-1.3.7-26.src.rpm
      /python-ntplib-0.3.3-13.src.rpm
      /python-oauthlib-3.0.2-1.src.rpm
      /python-olefile-0.46-2.src.rpm
      /python-ordered-set-2.0.2-1.src.rpm
      /python-packaging-17.1-2.src.rpm
      /python-paramiko-2.4.1-7.src.rpm
      /python-parse-1.8.4-2.src.rpm
      /python-paste-2.0.3-10.src.rpm
      /python-path-5.2-15.src.rpm
      /python-pbr-4.1.1-3.src.rpm
      /python-pecan-1.3.2-5.src.rpm
      /python-pip-18.0-12.src.rpm
      /python-pluggy-0.6.0-6.src.rpm
      /python-ply-3.9-9.src.rpm
      /python-pocketlint-0.17-2.src.rpm
      /python-polib-1.1.0-2.src.rpm
      /python-pretend-1.0.8-15.src.rpm
      /python-prettytable-0.7.2-18.src.rpm
      /python-productmd-1.22-2.src.rpm
      /python-psutil-5.4.3-7.src.rpm
      /python-pyasn1-0.3.7-8.src.rpm
      /python-pycparser-2.19-1.src.rpm
      /python-pycurl-7.43.0.2-6.src.rpm
      /python-pygments-2.2.0-15.src.rpm
      /python-pymongo-3.9.0-2.src.rpm
      RPM
      /python-pynacl-1.2.1-4.src.rpm
      /python-pysocks-1.7.0-2.src.rpm
      /python-pytest-cov-2.5.1-7.src.rpm
      /python-pytest-expect-1.1.0-3.src.rpm
      /python-pytest-fixture-config-1.2.11-6.src.rpm
      /python-pytest-mock-1.10.0-4.src.rpm
      /python-pytest-shutil-1.2.6-6.src.rpm
      /python-pytest-virtualenv-1.2.11-11.src.rpm
      /python-pytoml-0.1.18-2.src.rpm
      /python-pyudev-0.21.0-10.src.rpm
      /python-redis-2.10.6-6.src.rpm
      /python-reportlab-3.4.0-10.src.rpm
      /python-repoze-lru-0.7-2.src.rpm
      /python-requests-file-1.4.3-9.src.rpm
      /python-requests-ftp-0.3.1-15.src.rpm
      /python-rpm-generators-9-1.src.rpm
      /python-rsa-3.4.2-11.src.rpm
      /python-ruamel-yaml-clib-0.1.2-1.src.rpm
      /python-schedutils-0.6-5.src.rpm
      /python-scikit-optimize-0.5.2-1.src.rpm
      torage/
      /python-semantic_version-2.6.0-9.src.rpm
      /python-setuptools-40.4.3-4.src.rpm
      /python-setuptools_git-1.1-10.src.rpm
      /python-setuptools_scm-3.1.0-2.src.rpm
      /python-simplegeneric-0.8.1-11.src.rpm
      /python-simpleline-1.6-1.src.rpm
      /python-singledispatch-3.4.0.3-14.src.rpm
      /python-six-1.12.0-1.src.rpm
      /python-slip-0.6.5-4.src.rpm
      /python-snowballstemmer-1.2.1-8.src.rpm
      /python-sphinx-1.7.6-6.src.rpm
      /python-sphinxcontrib-spelling-4.2.0-2.src.rpm
      /python-sphinxcontrib-websupport-1.0.1-11.src.rpm
      /python-sphinx_rtd_theme-0.4.1-2.src.rpm
      /python-sphinx-theme-alabaster-0.7.11-6.src.rpm
      /python-sqlalchemy-1.2.11-2.src.rpm
      /python-subprocess32-3.2.7-1.src.rpm
      /python-suds-0.7-2.src.rpm
      /python-sure-1.4.11-4.src.rpm
      /python-systemd-234-10.src.rpm
      /python-tempita-0.5.1-21.src.rpm
      /python-testscenarios-0.5.0-14.src.rpm
      /python-testtools-2.3.0-11.src.rpm
      /python-texttable-1.4.0-2.src.rpm
      /python-threadpoolctl-1.1.0-2.src.rpm
      /python-toml-0.10.0-1.src.rpm
      /python-tornado-5.0.2-5.src.rpm
      /python-tqdm-4.28.1-1.src.rpm
      /python-traceback2-1.4.0-19.src.rpm
      /python-u-msgpack-python-2.5.0-2.src.rpm
      /python-unittest2-1.1.0-16.src.rpm
      /python-urwid-2.0.1-5.src.rpm
      /python-varlink-27.1.1-2.src.rpm
      /python-virtualenv-16.0.0-6.src.rpm
      /python-waitress-1.1.0-5.src.rpm
      /python-webencodings-0.5.1-7.src.rpm
      /python-webob-1.8.2-3.src.rpm
      /python-websocket-client-0.47.0-6.src.rpm
      /python-webtest-2.0.30-2.src.rpm
      /python-werkzeug-0.14.1-6.src.rpm
      /python-which-1.1.0-23.src.rpm
      /python-whoosh-2.7.4-13.src.rpm
      /python-zipp-0.5.1-1.src.rpm
      /python-zope-event-4.2.0-12.src.rpm
      /python-zope-interface-4.5.0-3.src.rpm
      /qt5-5.11.1-7.src.rpm
      /qt5-doc-5.11.1-4.src.rpm
      /quota-4.05-1.src.rpm
      /re2-20160401-8.src.rpm
      /readline-7.0-13.src.rpm
      /recode-3.6-50.src.rpm
      /rhash-1.3.5-5.src.rpm
      /rootfiles-8.1-25.src.rpm
      /rootsh-1.5.3-15.src.rpm
      /rpcbind-1.2.5-2.src.rpm
      /rpcsvc-proto-1.4-2.src.rpm
      /rpmdevtools-8.10-8.src.rpm
      /rpmrebuild-2.11-7.src.rpm
      /glibc-2.29.9000-8oe1.src.rpm
      /swig-3.0.12-22.src.rpm
      /ncurses-6.1-14.src.rpm
      /rsync-3.1.3-6.src.rpm
      /ruby-common-2.1-106.3.src.rpm
      /sanlock-3.6.0-7.src.rpm
      /sblim-cmpi-devel-2.0.3-19.src.rpm
      /scrub-2.5.2-14.src.rpm
      /security-tool-2.0-1.43.src.rpm
      /sed-4.7-0.src.rpm
      /setup-2.13.3-4.src.rpm
      /sg3_utils-1.42-10.src.rpm
      /sgml-common-0.6.3-51.src.rpm
      /sharutils-4.15.2-15.src.rpm
      /smp_utils-0.98-14.src.rpm
      /snappy-1.1.7-10.src.rpm
      /sos-3.6-5.src.rpm
      /soundtouch-2.1.0-2.src.rpm
      /speexdsp-1.2.0-1.src.rpm
      /spice-protocol-0.12.14-3.src.rpm
      /zstd-1.3.6-3.src.rpm
      /gettext-0.20.1-2.src.rpm
      /chrpath-0.16-11.src.rpm
      /git-2.23.0-12.src.rpm
      /krb5-1.17-9.src.rpm
      /openldap-2.4.46-15.src.rpm
      /python3-3.7.4-8.src.rpm
      /swig-3.0.12-22.src.rpm
      /ncurses-6.1-14.src.rpm
      /boost-1.66.0-18.src.rpm
      /perl-5.28.0-434.src.rpm
      /sqlite-3.24.0-9.src.rpm
      /coreutils-8.31-4.src.rpm
      /binutils-2.33.1-1.oe1.src.rpm
      /libselinux-2.9-1.src.rpm
      /chkconfig-1.10-4.oe1.src.rpm
      /chkconfig-1.10-1.oe1.src.rpm
      /gcc-8.2.1-7.1.riscv64.oe1.src.rpm
      /bind-9.11.4-13.src.rpm
      /file-5.38-1.src.rpm
      /pam-1.3.1-8.src.rpm
      /rpm-4.15.1-13.src.rpm
      /gawk-5.0.1-2.src.rpm
      /uuid-1.6.2-43.src.rpm
      /gc-8.0.4-2.src.rpm
      /perl-libwww-perl-6.35-2.src.rpm
      /shadow-4.7-10.src.rpm
      /util-linux-2.34-8.src.rpm
      /libffi-3.3-7.src.rpm
      /glib2-2.62.1-1.src.rpm
      /audit-3.0-5.src.rpm
      /gnutls-3.6.9-5.src.rpm
      /qrencode-4.0.2-2.src.rpm
      /vim-8.1.450-8.src.rpm
      /isl-0.16.1-7.oe1.src.rpm
      /kernel-headers-5.4.0-0.rc6.git0.1.1.riscv64.oe1.src.rpm
      /libpwquality-1.4.0-11.src.rpm
      /nss-pem-1.0.4-2.src.rpm
      /libpng-1.6.36-4.src.rpm
      /lua-5.3.5-4.src.rpm
      /passwd-0.80-7.src.rpm
      /net-tools-2.0-0.54.src.rpm
      /autoconf-2.69-30.src.rpm
      /elinks-0.12-1.src.rpm
      /libdb-5.3.28-35.src.rpm
      /nss-3.40.1-11.src.rpm
      /perl-WWW-Curl-4.17-19.oe1.src.rpm
      /perl-Digest-1.17-419.src.rpm
      /perl-libnet-3.11-420.src.rpm
      /unbound-1.7.3-14.src.rpm
      /libunistring-0.9.10-7.src.rpm
      /guile-2.0.14-15.src.rpm
      /perl-threads-shared-1.59-2.src.rpm
      /perl-threads-2.22-419.src.rpm
      /perl-podlators-4.11-5.src.rpm
      /perl-Archive-Tar-2.30-421.src.rpm
      /perl-B-Debug-1.26-4.src.rpm
      /perl-perlfaq-5.20180915-5.src.rpm
      /perl-Data-Dumper-2.172-3.src.rpm
      /perl-parent-0.237-4.src.rpm
      /perl-Carp-1.50-418.src.rpm
      /perl-CPAN-2.27-3.src.rpm
      /perl-Config-Perl-V-0.30-5.src.rpm
      /perl-DB_File-1.842-2.src.rpm
      /perl-Env-1.04-397.src.rpm
      /perl-experimental-0.020-2.src.rpm
      /grubby-8.40-24.src.rpm
      /systemtap-4.1-3.src.rpm
      /perl-constant-1.33-421.src.rpm
      /perl-Exporter-5.73-420.src.rpm
      /perl-Text-ParseWords-3.30-419.src.rpm
      /perl-Getopt-Long-2.50-419.src.rpm
      /perl-Unicode-Normalize-1.26-419.src.rpm
      /perl-Time-HiRes-1.9760-2.src.rpm
      /perl-Time-Local-1.280-6.src.rpm
      /perl-Digest-MD5-2.55-419.src.rpm
      /perl-HTML-Parser-3.72-16.src.rpm
      /perl-Pod-Parser-1.63-397.src.rpm
      /perl-Pod-Usage-1.69-418.src.rpm
      /perl-CPAN-Meta-2.150010-419.src.rpm
      /perl-Encode-2.98-9.src.rpm
      /perl-ExtUtils-MakeMaker-7.42-2.src.rpm
      /perl-autodie-2.29-398.src.rpm
      /perl-bignum-0.50-4.src.rpm
      /perl-Thread-Queue-3.13-3.src.rpm
      /perl-Unicode-Collate-1.25-4.src.rpm
      /perl-Text-Tabs+Wrap-2013.0523-419.src.rpm
      /perl-Test-Harness-3.43_01-3.src.rpm
      /perl-Term-ANSIColor-4.06.511.src.rpm
      /perl-Term-Cap-1.17-510.src.rpm
      /perl-CPAN-Meta-YAML-0.018-420.src.rpm
      /perl-CPAN-Meta-Requirements-2.140-419.src.rpm
      /perl-File-Fetch-0.56-4.src.rpm
      /perl-Compress-Bzip2-2.26-10.src.rpm
      /perl-Compress-Raw-Zlib-2.081-6.src.rpm
      /perl-File-Temp-0.230.800-4.src.rpm
      /perl-File-Path-2.16-4.src.rpm
      /perl-HTTP-Tiny-0.076-3.src.rpm
      /perl-Locale-Maketext-1.28-1.src.rpm
      /perl-Filter-1.59-2.src.rpm
      /perl-ExtUtils-Install-2.14-419.src.rpm
      /perl-ExtUtils-Manifest-1.71-4.src.rpm
      /perl-ExtUtils-ParseX
      /perl-MIME-Base64-3.15-418.src.rpm
      /perl-Locale-Codes-3.58-2.src.rpm
      /perl-Math-BigInt-1.9998.13-5.src.rpm
      /perl-Math-BigRat-0.2614-2.src.rpm
      /perl-Math-BigInt-FastCalc-0.500.700-4.src.rpm
      /perl-Module-CoreList-5.20180920-2.src.rpm
      /perl-IPC-Cmd-1.04-4.src.rpm
      /perl-IO-Compress-2.081-6.src.rpm
      /perl-Module-Load-0.32-418.src.rpm
      /perl-Compress-Raw-Bzip2-2.081-8.src.rpm
      /perl-Module-Load-Conditional-0.68-418.src.rpm
      /perl-Module-Metadata-1.000036-3.src.rpm
      /perl-Params-Check-0.38-418.src.rpm
      /perl-Pod-Checker-1.73-398.src.rpm
      /perl-Pod-Escapes-1.07-419.src.rpm
      /perl-Pod-Perldoc-3.28-3.src.rpm
      /perl-Text-Balanced-2.03-420.src.rpm
      /perl-Devel-PPPort-3.42-4.src.rpm
      /perl-version-0.99.24-3.src.rpm
      /perl-PerlIO-via-QuotedPrint-0.08-397.src.rpm
      /perl-PathTools-3.75-4.src.rpm
      /targetcli-2.1.fb48-9.src.rpm
      /perl-Text-Diff-1.45-7.src.rpm
      /libssh-0.8.3-7.src.rpm
      /nghttp2-1.39.2-2.src.rpm
      /curl-7.66.0-2.src.rpm
      /pyparsing-2.2.0-4.src.rpm
      /ima-evm-utils-1.2.1-8.src.rpm
      /gnupg2-2.2.17-5.src.rpm
      /python-rtslib-2.1.70-3.src.rpm
      /tar-1.30-11.src.rpm
      /ima-evm-utils-1.1-2.oe1.src.rpm
      /perl-Algorithm-Diff-1.1903-14.src.rpm
      /perl-File-HomeDir-1.004-4.src.rpm
      /pygobject3-3.30.1-2.src.rpm
      /libX11-1.6.9-2.src.rpm
      /publicsuffix-list-20180723-3.src.rpm
      /perl-File-Which-1.22-6.src.rpm
      /libxcb-1.13.1-2.src.rpm
      /libassuan-2.5.1-6.src.rpm
      /libksba-1.3.5-12.src.rpm
      /apr-util-1.6.1-11.src.rpm
      /apr-1.6.5-4.src.rpm
      /accountsservice-0.6.54-2.src.rpm
      /cryptsetup-2.0.4-2.src.rpm
      /cyrus-sasl-2.1.27-10.src.rpm
      /lua-posix-33.3.1-12.src.rpm
      /libuser-0.62-20.src.rpm
      /libxml2-2.9.8-9.src.rpm
      /pam_krb5-2.4.13-12.src.rpm
      /dnf-4.2.15-8.src.rpm
      /dnf-plugins-core-4.0.11-5.src.rpm
      /libdnf-0.37.2-2.src.rpm
      /fontconfig-2.13.1-3.src.rpm
      /cairo-1.15.14-3.src.rpm
      /pango-1.43.0-3.src.rpm
      /gtk2-2.24.32-7.src.rpm
      /libthai-0.1.28-3.src.rpm
      /libXrender-0.9.10-10.src.rpm
      /libXft-2.3.2-13.src.rpm
      /harfbuzz-1.8.7-2.src.rpm
      /libXcomposite-0.4.4-17.src.rpm
      /libXrandr-1.5.1-10.src.rpm
      /libXcursor-1.1.15-5.src.rpm
      /libXdamage-1.1.4-18.src.rpm
      /libXfixes-5.0.3-11.src.rpm
      /libXi-1.7.9-11.src.rpm
      /libXinerama-1.1.4-5.src.rpm
      /libtiff-4.1.0-1.src.rpm
      /cups-2.2.8-8.src.rpm
      /libreport-2.10.1-7.src.rpm
      /libcomps-0.1.8-20.src.rpm
      /gpgme-1.13.1-5.src.rpm
      /gtk3-3.24.1-3.src.rpm
      /shared-mime-info-1.10-4.src.rpm
      /libjpeg-turbo-2.0.0-4.src.rpm
      /pixman-0.38.0-1.src.rpm
      /giflib-5.1.4-6.src.rpm
      /freeglut-3.0.0-10.src.rpm
      /libwebp-1.0.0-5.src.rpm
      /javapackages-tools-5.3.0-2.src.rpm
      /libepoxy-1.5.3-2.src.rpm
      /wayland-1.17.0-2.src.rpm
      /rest-0.8.1-7.src.rpm
      /json-glib-1.4.4-2.src.rpm
      /colord-1.4.3-6.src.rpm
      /adwaita-icon-theme-3.32.0-1.src.rpm
      /satyr-0.27-5.src.rpm
      /avahi-0.7-21.src.rpm
      /newt-0.52.21-3.src.rpm
      /libproxy-0.4.15-13.src.rpm
      /libdnf-0.37.2-1.oe1.src.rpm
      /graphite2-1.3.13-2.src.rpm
      /icu-62.1-5.src.rpm
      /libsoup-2.66.1-1.src.rpm
      /xmlrpc-c-1.51.03-4.src.rpm
      /augeas-1.12.0-4.src.rpm
      /xkeyboard-config-2.24-6.src.rpm
      /subscription-manager-1.23.3-1.oe1.src.rpm
      /libgusb-0.3.0-5.src.rpm
      /pyatspi-2.33.92-1.src.rpm
      /perl-TermReadKey-2.38-2.src.rpm
      /at-spi2-core-2.34.0-1.src.rpm
      /perl-Error-0.17026-4.src.rpm
      /perl-Text-WrapI18N-0.06-33.src.rpm
      /glib-networking-2.58.0-7.src.rpm
      /gsettings-desktop-schemas-3.34.0-1.src.rpm
      /NetworkManager-1.16.0-7.src.rpm
      /annobin-8.23-2.src.rpm
      /libsolv-0.7.7-2.src.rpm
      /libappstream-glib-0.7.14-3.src.rpm
      /ipcalc-0.2.5-1.src.rpm
      /jansson-2.11-4.src.rpm
      /wpa_supplicant-2.6-26.src.rpm
      /ModemManager-1.8.0-7.src.rpm
      /libteam-1.27-14.src.rpm
      /polkit-0.116-4.src.rpm
      /slang-2.3.2-8.src.rpm
      /libical-3.0.4-2.src.rpm
      /strace-5.0-2.src.rpm
      /stunnel-5.48-3.src.rpm
      /sudo-1.8.27-4.src.rpm
      /symlinks-1.4-23.src.rpm
      /sysfsutils-2.1.0-28.src.rpm
      /sysstat-12.1.6-2.src.rpm
      /taglib-1.11.1-12.src.rpm
      /targetcli-2.1.fb48-9.src.rpm
      /tcl-8.6.8-8.src.rpm
      /tcllib-1.19-2.src.rpm
      /tcp_wrappers-7.6-96.src.rpm
      /telepathy-filesystem-0.0.2-7.src.rpm
      /TeXamator-1.7.5-11.src.rpm
      /texi2html-5.0-13.src.rpm
      /texinfo-6.6-2.src.rpm
      /texlive-2018-22.src.rpm
      /tidy-5.6.0-1.src.rpm
      /time-1.9-7.src.rpm
      /tinycdb-0.78-11.src.rpm
      /tinyxml2-6.0.0-5.src.rpm
      /tokyocabinet-1.4.48-13.src.rpm
      /traceroute-2.1.0-10.src.rpm
      /transfig-3.2.6a-6.src.rpm
      /tree-1.7.0-18.src.rpm
      /trousers-0.3.14-3.src.rpm
      /ttmkfdir-3.0.9-56.src.rpm
      /tuned-2.10.0-7.src.rpm
      /tzdata-2019b-10.src.rpm
      /uchardet-0.0.6-1.src.rpm
      /uname-build-checks-1.0-0.4.src.rpm
      /unicode-emoji-11.0-3.src.rpm
      /unicode-ucd-11.0.0-3.src.rpm
      /unzip-6.0-45.src.rpm
      /usb_modeswitch-data-20170806-4.src.rpm
      /ustr-1.0.4-28.src.rpm
      /utf8proc-2.1.1-6.src.rpm
      /vconfig-1.9-26.src.rpm
      /virt-what-1.18-8.src.rpm
      /vulkan-headers-1.1.92.0-2.src.rpm
      /wavpack-5.1.0-10.src.rpm
      /which-2.21-14.src.rpm
      /words-3.0-32.src.rpm
      /xcb-proto-1.13-6.src.rpm
      /xcb-util-0.4.0-13.src.rpm
      /xfsprogs-4.17.0-5.src.rpm
      /xhtml1-dtds-1.0-20020801.15.src.rpm
      /xmltoman-0.4-19.src.rpm
      /xorg-x11-drivers-7.7-28.src.rpm
      /xorg-x11-proto-devel-2018.4-3.src.rpm
      /xorg-x11-util-macros-1.19.2-4.src.rpm
      /xorg-x11-xbitmaps-1.1.1-16.src.rpm
      /xz-5.2.4-10.src.rpm
      /yajl-2.1.0-12.src.rpm
      /yaml-cpp-0.6.3-1.src.rpm
      /zd1211-firmware-1.5-5.src.rpm
      /zip-3.0-25.src.rpm
      /zlib-1.2.11-17.src.rpm
      /zopfli-1.0.1-8.src.rpm
      /zstd-1.3.6-3.src.rpm
```

 ### 跨领域和面向外部的流程

 由该SIG定义和执行的，且跨领域和面向外部的流程和行动：

 - 非内部流程清单
 - 该SIG拥有的面向整个openEulerSIG的组织指导计划等
