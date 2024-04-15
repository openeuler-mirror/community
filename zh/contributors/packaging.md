# openEuler packaging guidelines



**为本指南作出贡献**

您可以通过在 Gitee 仓库上提交一个问题或者一个PR来对本指南做出贡献。这两种形式的贡献都深受赞赏和欢迎。

@myeuler 曾经这样比喻制作rpm包对于操作系统发行版的意义。如果说一个人想要成为一个优秀的Linux系统工程师，就好像要成为一个顶级大厨，任何大厨成长的第一步一定不是上手学做菜，一定是要熟悉，识别各种食材，能够熟练的洗菜，切菜，识别各种菜式的品性。这是一个大厨成长的起点。而为操作系统发行版做各种各样的rpm包就是在熟悉食材，了解食材的品性。只有对rpm包的结构，内容，以及rpm之间的依赖关系有一个熟练的掌握，才能为后续成为一个真正的操作系统高手打下基础。

本文档就是一个介绍rpm制作的指导性文档，重点指导你完成第一个rpm包的制作，具体rpm包的制作细则则会分散在各个具体规范中，我们将不断更新和完善。

## 0 软件打包

制作RPM包，俗称**打包**，是指编译并捆绑软件与元数据例如软件全名、描述、正常运行所需的依赖列表等等的任务。这是为了让软件使用者可以使用软件包管理器舒服的安装、删除或者升级他们所使用的软件。

### 打包规则

openEuler试图规范化多种多样的开源项目到一个连贯的系统。因此openEuler制定此打包指导来规范制作RPM的动作。

- openEuler遵守一般的[Linux基础标准(LSB)](http://www.linuxbase.org/)。该标准致力于减少各个发行版间的不同。
- openEuler也遵守[Linux文件系统层级标准(FHS)](http://www.pathname.com/fhs/)。该标准是关于如何管理 Linux 文件系统层级的参考。
- 除了遵守这些一般Linux发行版都会遵守的一般规则，本文档规范化了为openEuler社区版打包的实际细节问题。

### 打包基础知识

运用此文档创建RPM和.spec之前，建议你先熟悉下面知识点，前两项是如何创建一个高质量的软件包所必须的，后两项对参与openEuler很有帮助。

|      | skill                                                        |      | links                                                        |
| :--: | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
|  1   | rpm软件包管理（包括软件安装、升级、卸载、编译构建）          | 必选 | [RPM官网](https://rpm.org)                                   |
|  2   | rpm官方打包指导                                              | 必选 | see the [RPM Packaging Guide](https://rpm-packaging-guide.github.io/). |
|  3   | open build service 使用(openEuler 使用 OBS构建系统来构建版本) | 可选 | see [obs user guide](https://openbuildservice.org/help/manuals/obs-user-guide/) |
|  4   | Gitee 日常操作（openEuler代码托管在gitee.com/openEuler）     | 可选 | see [Gitee Support Center](https://gitee.com/help#article-header0) |

### 关联文档

如果你计划将软件引入到openEuler official software repository，请参考 [社区贡献者指南](https://www.openeuler.org/zh/community/contribution/detail.html)。

### 适用性

一般来说，这些准则适用于openEuler的所有版本，包括非生命周期版本、生命周期版本以及开发版本。

指导方针也在一定程度上涵盖了进入openEuler的所有类型和交付场景的软件包。openEuler是一个社区版本，因此不能保证所有的规则是一成不变，当前其最核心最重要的基本原则，在可预期的未来是不会有大的变动。

### 文档中约定

如果在文档中使用了“应该”或“建议”的语言，打包时我们对条款不做强制要求，当然我们强烈建议和规则的要求保持一致。

如果使用了“必须”或“规则”的措词，打包时只有TC决策后，才可以偏离准则。

## 1 打包规则

每个操作系统都自成体系，彼此之间除了技术路线、里程碑不同之外，软件包的组织方式也有所不同。

其主要的区别集中在下面几个方面：

1. 不同的包管理器（fedora、openSUSE使用rpm、debian使用deb等）。
2. 维护不同的软件包列表，包括不同的软件版本。
3. 互相独立的软件包拆分规则。
4. 基于不同拆分规则，而自然形成的软件依赖关系图。

### 软件包管理器

openEuler不打算重复造轮子，使用rpm作为底座，附以dnf、yum来管理软件包。也许在不久的将来，如果rpm等工具不能满足需求，openEuler会考虑发起新的项目。

### 软件列表、软件选型

openEuler有自己的软件列表集合，当前已经集成2000+软件包，还在继续丰富和完善。

openEuler的软件代码来源，是直接取自软件原生社区的稳定版本，同时按照此打包规范编写spec打包并集成。

openEuler遵循Upstream First原则。

### 软件拆分规则

区别于其他OS发行商等将软件拆分成主包、libs、devel、static、langpack、doc等包。
openEuler软件包拆分的原则是不做复杂的拆分，将软件拆分为基本固定的5个rpm包，分别为：主包、libs包、devel包、static包和help包（可选）。但是对于很多简单的软件来说，可以将libs包，devel包和主包合并，不单独拆分。目的是保持包的简洁，易于理解，不会将包的粒度做的过细而导致后续更新，维护困难，并且增加依赖关系的复杂性。但是如果出现特殊的，复杂的软件可以考虑更细粒度的拆分。

一般软件包分拆：

| 分类     | 包名             | 包含内容                                                     | 关键点                                                       |
| -------- | ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 主包     | 与软件源码包同名 | 1、命令、配置、本软件包含的命令运行所需的so<br />2、license、copyright、Author、readme（如果包含版权信息）  <br />3、版权、许可、权利人等法务相关的文件都放licenses目录下<br />4、man、info手册 | 可以通过Provides、Obsoletes声明实现与其他OS的兼容。<br />（Provides、Conflicts、Obsoletes等功能介绍参考附件中的rpm官方手册。） |
| libs包   | 软件包名-libs    | 1、只包含对外提供的动态库、命令                              | 将自身的功能与对外提供的能力分离，确保上层应用只依赖于libs本身，减少软件包之间的复杂性，避免循环依赖。 |
| devel包  | 软件包名-devel   | 1、头文件<br />2、Example<br />3、tests用例<br />4、其他开发使用的内容 | 1、所有属于开发范围的内容，统一打包成devel包。<br />2、动态库打包到主包中后，devel包一般要Requires主包，否则部分动态库找不到 |
| static包 | 软件包名-static  | 1、静态库.a<br />2、提供的命令的静态版本                     | 如果提供static版本，有必要使用宏来控制static是否编译和打包。 |
| help包   | 软件包名-help    | 二次开发文档  接口函数说明的手册                             | **通常这个拆分是非必须的，当且仅当包含的文档内容非常大时，有必要单独拆分。** |

复杂软件包，在上面分类的基础上，需要考虑特殊场景：

| 分类                                                         | 包名                                                     | 包含内容                                             |
| ------------------------------------------------------------ | -------------------------------------------------------- | ---------------------------------------------------- |
| for-language包——软件包提供多个不同语言的支持接口             | 例如：python2-软件包名  python3-软件 包名  perl-软件包名 | 软件包针对perl、python2、python3等语言的支持可以分拆 |
| 本地化支持——这要针对复杂的、国际化相关的软件，简单的包，不需要单独拆分lang | 例如：软件包名-lang                                      | 本地化、语言支持、时区相关等与国际化相关的内容       |
| 其他复杂和特殊包（gcc、python2、python3等）                  | 例如：openssh-server、openssh-client                     |                                                      |

### 基于不同分拆规则的软件依赖关系树

通常基于新的软件拆分规则，OS依赖体系自然形成，其软件间的依赖关系随之变化。

Provides、Conflicts、Obsoletes等RPM关键字提供的功能可以解决兼容的问题。openEuler导出软件提供的功能（Symbols），再利用Provides、Obsoletes等手段可以确保与其他OS的部分兼容。

## 2 软件打包验证

从下面三个角度验证。

- 不同的软件列表，软件选型；

- 独立的软件拆分规则；

- 基于不同分拆规则的软件依赖关系树。

1、 使用rpmlint测试spec是否有问题，确认是否能正常地构建出对应的rpm。

2、 确认软件包拆分是否合理，是否满足openEuler软件包拆分规则。

3、 查看生成二进制RPM的Provides、Requires是否正常，可以通过命令rpm --provides 或rpm --requires查看，确保软件包具备的能力被正确的提供出来。

4、 查看软件选型打包后的二进制包是否可以正常使用rpm命令进行正确安装、卸载、升级和回滚。

5、 安装升级后，验证：1）服务类的，验证start/stop/restart/reload；2）命令类的，至少要验证基本功能可用。

6、 软件包源码中自带tests，不能随意注释、删除、禁用，需要确保代码提交时，门禁中make check自测用例通过。

7、 特别是软件选型升级后，对其他软件包的影响，很难独立判断，需要做集成测试。

## 3 打包规范

规则和规范是一个逐步完善的过程，确保已有的规则得到遵循。

### 来源可靠

- 不要内嵌预编译好的二进制文件或库文件，软件包中包含的所有二进制文件或库文件都必须是从源代码包中被编译的。二进制固件类的文件可豁免。如果需要引入二进制，经由TC讨论后决定。
- 软件包应该尽量避免多个、分离的、上游的项目被捆绑到一个软件包中，力争做到一个软件包来源一个社区。
- 软件**应该**是开源软件，开源软件的定义参考https://opensource.org/osd.html 。如果非开源软件，经由TC讨论后决定。
- 集成没有法律风险的开源软件，[开源许可名录](https://opensource.org/licenses/alphabetical)。
- spec文件要适配openEuler，做到正确、准确、清晰、简洁。如果引用了其他发行版内容，或来自原生社区，必须顶部说明。
- 存在于**黑名单**的软件**必须不能**引入。
- 每一个软件的引入决定，都作为案例，作为后续类似软件引入决策的参考。Technical Committ对软件引入原则的一致性负责。

### 架构支持

- 打包者应尽量提供支持在aarch64和x86_64等几种架构上编译成功，后续随openEuler对其它体系架构的支持，可能会增加构建的要求。
- 对于架构强相关的内容，通过`%ifarch`宏来控制。
- 独立于架构的内容，如文档手册，perl、python等解释性语言程序，构建成一个noarch包。
- 如果软件当前支持的架构尚不全面，可以使用`ExcludeArch:` or `ExclusiveArch:` 来控制。

### 软件拆分

- 软件的拆分需要按照openEuler软件拆分规则实施。
- 不允许直接禁用debuginfo的生成。特殊情况除外。
- man、info手册，原则上我们不建议单独拆分出一个help子包，除非里面包含更复杂或多样的内容。
- 对于addon、plugins、modules、extensions、components类型的包，我们建议单独拆分一个对应的子包，以此来保证主包的简洁。
- 如果提供了一个minimal的版本，建议拆分出一个子包，如bash-minimal，对于minimal的构建，建议用宏控制，并默认开启。

### 命名规则

- 原则上，openEuler只集成软件的某一个版本，主包名称与软件名称同名，如果坚持引入多个版本，经过TC同意后，可以采用后缀版本号（openssl1.0f、注意这里是原名称里不是以数字结尾，否则使用`-`隔开）或描述性后缀（-stable）。

- 针对语言的模块，可以前缀语言来命名。如python-systemd、python3-systemd、perl-systemd等。

- 软件包名一般情况，来自原生社区，英文，有意义词组，大小写敏感。如果有多个词，我们建议直接用`-`分割，而不是`_`、`.`和`+`下划线，例外情况包括nss_db、sg3_utils等软件包重名或原生社区本身就自带特殊符号。

- 补丁命名内容清晰完整即可，通常我们建议你参考下面的要求来做，确保统一可追溯：

    a、所有新补丁以.patch结尾，并通过注释方式标注其来源及其作用，注释的格式“PATCH-(BUGFIX|CVE|FEATURE)-内容”。

    b、允许引用其他bugzilla，可用缩写代替，如CVE-2009-0067、GCC#123456、kde#123456、rh#123456等。

    c、不要求补丁文件名称添加特定前缀，如backport-、upstream-等。

    d、要求spec补丁序号从0开始，且保持连续。


### 基本信息

- spec中的基本信息，如name、group、summary、description等信息，根据官网查询填写，请使用规范的书面语言描述或书写，避免`like`、`good/best`等字眼。
- 在rpm升级的场景中，比较软件版本高低的规则是epoch:version-release，epoch优先级比version、release高。spec中epoch的正常情况下默认由版本统一指定，不需要特别指定。以下两种情况需要使用epoch能保证该软件可yum升级: a. 某软件因特殊原因，version与release产生了降级、回退，epoch需要在原来的基础上递增；b. 不同分支因开发进度不一致，比如维护分支的version和release比开发分支高，为了保证维护分支可以向开发分支升级，需保证开发版本的epoch比维护版本的epoch高。
- spec中version需要和上游社区的版本号保持一致，聚合性软件包（一个repo中有多个上游社区的源码：[xorg-x11-font-utils](https://gitee.com/src-openeuler/xorg-x11-font-utils)）spec 中version信息由maintainer 按照社区惯例确定。release号用于标识openEuler基于上游社区的发布次数，软件包version升级后首次发布时release 从1 开始，后续保持递增。

### 格式规范

- 所有spec文件必须清晰易读，并以打包者能够理解和使用它们的方式进行维护。
- spec中的缩进统一格式，使用空格，保持对齐。
- 多个编译依赖或安装依赖可以汇总成1~3行，这样看起来更简洁。
- 除非您需要使用ASCII配置表以外的字符，否则不需要关心spec文件的编码。如果您确实需要非ascii字符，请将您的spec文件保存为UTF-8。
- changelog遵循特定的格式，一个典型的格式如下。

```SPEC
* Tue Apr 7 2020 openEuler Buildteam <buildteam@openeuler.org> - 10.33-3
- Type:CVES/Bugfix/Feature
- ID:CVE-2019-20454
- SUG:NA
- DESC:fix CVE-2019-20454
```

### 依赖关系

- 要保证软件包的编译依赖和安装依赖已经存在于openEuler仓库中。如果没有，需要一并打包引入。
- 编译依赖和安装依赖需要自行确认，确保完整。在openEuler系统上，安装依赖后，确保rpmbuild能够正常构建。
- 尽量避免循环依赖。
- 尽量去掉对文件和命令的依赖，这会使事情变的复杂。

- -devel包或其他子包，都要写明对主包的依赖，包括版本号和release号，否则出现单包能升级成功，从而导致兼容问题。
- `Requires` 要求必须使用，如果依赖是软件正常工作所需的。如果在失去某些依赖后软件包的功能仍然正常，我们推荐使用`Recommends` 或 `Suggests`。如果是用于补充完整性和增强特性时，如plugins、addon，我们建议使用`Supplements` 或 `Enhances`。请参考rpm手册准确了解相关用法的区别。
- 一些特殊格式的依赖，要保持统一，如`pkgconfig(foo)`、`dist(foo)`、`perl(strict)`等。

### 宏的应用

- 对于软件包提供的python模块，同时支持python2、python3，并用`with_python2`宏控制。
- 使用宏而不是硬编码的方式来编写spec，当前支持的宏可以使用rpm --showrc查询得出。如果有新增宏的诉求，可以告知打包负责人，我们力求spec简洁优美。
  - 包括但不限于rpmbuild内置的%{name}、%{buildroot}、%{_bindir}等。
  - 优先尝试将通用的操作抽象成一个公共的宏，并报告给包管理委员会。

### 编译构建

- 如无必要，可以直接使用模板中的`autosetup`来应用打补丁，而不使用`patch`命令打补丁。
- `%install`阶段删除的多余文件，可以考虑files的时候使用`%exclude`替代。
- 不允许直接跳过`make test`或`make check`来禁用编译过程的自测用例。
- `%files`对软件的打包时，打包的顺序要和前面定义package的顺序保持一致。
- `%files`中列表，多行可以考虑通配符替代。但注意单个目录不能随便打包，可能和目录的真实属主产生冲突。
- build过程中，openEuler默认会追加安全相关的编译选项，不要轻易的去除。
- 如果提供的是一个后台服务，请按照systemd unit的要求提供一个unit配置文件。

### 冲突与弃用

- 用户总是能从openEuler发布地址中获取最新的软件包。只要有可能，openEuler会在发布前尽量解决冲突。无法解决的，openEuler会在发布时给出说明，帮助用户做出选择。

- openEuler不会因为多个软件提供相同的功能，而做出非此即彼的选择，我们希望尽可能地集成更多的软件包，以此来丰富生态。

- 包命名冲突必须要被解决，可与社区沟通，如果原生社区不做让步，考虑前缀、后缀处理。

- 如果存在冲突，请在spec中显示地使用`Conflicts:`指出来，通常会有以下场景。

  - 当多个软件提供相同的功能，且不能同时安装使用时。我们建议gcc的spec中写明`Conflicts: linaro-gcc`。

  - 当多个软件提供相同的文件、工具、标准命令等。首先会尝试避免相同的命名（例如手册名相同或busybox命令与其他工具名称相同），可与社区沟通重名、或openEuler重命名来处理。如果还是不能避免，我们建议在spec中写明`Conflicts: `，直到最新的版本不再有冲突。

  - compat包的冲突，例如compat-gcc与gcc，这样做的原始目的可能是希望同一个系统中提供多个版本的gcc，原则上我们不允许这种情况的存在。

  - 某个软件不能在某个低版本的库上运行，这种冲突，我们建议使用`Requires:`而不是`Conflicts: `。

    ```SPEC
    **WRONG:** Conflicts: libbar < 1.2.3
    **RIGHT:** Requires: libbar >= 1.2.3
    ```

- 其他实际产生但未列出的冲突，需要报告包管理委员会，获取最终的解决方案。

- 当包的名称发生了变更，或是此包被弃用，需要使用`obsolete:`来显示说明。`Provides: libfoo   Obsoletes: libfoo`

## 4 检视原则

这是一套代码检视的指导方针。请注意，本方针还在完善过程中，不能确保能覆盖到所有的场景。检视人员或评审人员在评审软件包时应使用他们自己的良好判断力。列出的项目分为两类: 必须和建议。

- **必须**：使用rpmlint工具来检查打包的正确性。
- **必须**：包命名符合openEuler命名规则。
- **必须**：spec的名称与主包的名称保持一致，除非你的包存在例外，但需进过TC或包管理委员会评审。
- **必须**：软件包必须使用openEuler认可的许可证进行许可。
- **必须**：必须符合打包规则。
- **必须**：软件包规范文件中的License字段必须与实际的许可证相匹配。
- **必须**：如果(且仅当)源包在自己的文件中包含许可证文本，那么包含许可证文本的文件必须包含在%license许可证中，源码中没有许可证书的，需要在仓库中补充许可证书。
- **必须**：包的spec文件必须用英语撰写且清晰可读。
- **必须**：用于构建包的源代码必须与spec中URL中提供的上游源代码匹配。检视人员应该使用命令校验源码包的正确性。
- **必须**：如果包没有成功地在某个架构上编译、构建或工作，那么这些架构应该在ExcludeArch的规范中列出。
- **必须**：所有的构建依赖项必须在BuildRequires中列出。
- **必须**：规范文件必须正确处理区域设置。这是通过使用%find_lang宏来完成的。严格禁止使用%{datadir}/locale/* 。
- **必须**：软件包原则上不能将生成的单一文件%files打包到多个rpm包中，(显著的例外: License、许可文件可以打包到多个二进制RPM中)。
- **必须**：在install时，要安装到prefix(/usr)相对路径下，而不是默认的/下。
- **必须**：必须正确设置文件的权限。
- **必须**：大型文档文件必须放在-help子包中。 (大的定义取决于打包者的最佳判断，但不限于大小。 大可以指大小或数量)。单独的-help不安装的话，不能影响软件本身的功能。
- **必须**：开发文件、static文件必须在-devel包中。
- **必须**：在绝大多数情况下，devel包必须使用完整的依赖，包版本号: Requires: %{name}-%{version}-%{release}。
- **必须**：软件构建过程中的临时文件、中间文件，不能打包到最终的rpm中。
- **必须**：软件包不能拥有其他软件包已经拥有的文件或目录。
- **必须**：rpm包中的所有文件名都必须是有效的UTF-8。
- **必须**：添加到发行版中的包不能依赖于任何标记为已弃用的包。
- **必须**：如果原生社区提供了spec，可以借鉴或引用，但要保留社区的版权信息和修改记录。
- **建议**：如果源包没有将许可证文本作为独立于上游的文件包括在内，那么打包者应该查询上游以包括它。
- **建议**：尽可能地使用宏。
- **建议**：评审人员应该测试包是否能在mock中构建或rpmbuild构建。
- **建议**：包应该在所有支持的体系结构上编译并构建成二进制。
- **建议**：检视人员应该测试包的功能是否如描述的那样。
- **建议**：如果使用scriptlets，那么这些scriptlets必须是健全的。如果不明确，联合审查人员来判断是否合理。
- **建议**：通常，devel以外的子包依赖主包的话，要明确写清楚对主包的依赖，并且写上完整的版本信息。否则升级会导致问题。
- **建议**：如果包在/etc、/bin、/sbin、/usr/bin或/usr/sbin 之外有文件依赖项，那么考虑要求提供文件的包而不是文件本身。
- **建议**：如果软件包含的文档内容过多，建议单独拆分一个-help包。

## 5 创建第一个软件包

### 先决条件

按照这个教程，你需要安装这些软件包，部分软件系统已经默认安装:

```
$ yum install gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools
```

### 示例

此表部分列出了RPM spec文件使用的section，各个section可自由组合成一个简单的spec:

| SPEC section | Definition                                                   |
| ------------------ | ------------------------------------------------------------ |
| `%description`     | package在RPM中的软件的完整描述。 这种描述可以跨多行，也可以分为多个段落。 |
| `%prep`            | 命令或一系列命令来准备要构建的软件，此section展开相当于一个shell脚本。 |
| `%build`           | 用于将软件实际构建为机器代码(用于编译语言)或字节代码(用于某些解释语言)的命令或脚本。 |
| `%install`         | 命令或一系列命令，用于将所需的构建构件从%builddir(构建发生的地方)复制到%buildroot目录(包含要打包的文件的目录结构)。 这通常意味着将文件从~/rpmbuild/build复制到~/rpmbuild/buildroot，并在~/rpmbuild/buildroot中创建必要的目录。详细信息请参阅spec文件。 |
| `%check`           | 一系列命令用来测试软件。这通常包括单元测试。             |
| `%files`           | 安装在最终用户系统中的文件列表。                           |
| `%changelog`       | 不同版本之间发生的变更记录。               |

创建RPM包可能比较复杂。下面是一个完整的工作RPM Spec文件，跳过并简化了一些内容。这只是一个模板，很多东西，你需要根据多种情况，酌情修改里面的内容。并将最终的内容保存为helloworld.spec。

```SPEC
#这里提供的是一个模板，不需要的注释可以删除或修改，%%是对%的转义，#开始的行是注释。
#Copyright, license or readme

#Global macro or variable

#Basic Information，定义的顺序要统一，字段按照如下顺序填充
Name:           helloworld
Version:        1.0
Release:        1
Summary:        Most simple RPM package
License:        MIT
URL:            https://github.com/Aditmadzs/HelloWorld
#Source0:        这里没有实际的原生社区，没有源码

#Dependency
BuildRequires:  gcc make rpm-build
#不能出现对命令的依赖，要转化成rpm name
Requires:       glibc

%description
This is my first RPM package, which does nothing.

%package	libs
Summary:    Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description libs
This is my first RPM package, which does nothing.

%package	devel
Summary:    Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description devel
This is my first RPM package, which does nothing.

%package 	help
Summary:	Documents for autogen
Buildarch:	noarch
Requires:	man/info

%description    help
Man pages and other related documents.

#Secondary package
#这里定义其他package

#Build sections
%prep
#%%autosetup -n %{name}-%{version} -p1
#推荐用autosetup自动打补丁

%build
#%%configure         #特别注意选项
#%%make_build
cat > helloworld.sh <<EOF
#!/usr/bin/bash
echo Hello world
EOF

%install
#%%make_install
mkdir -p %{buildroot}/usr/bin/
install -m 755 helloworld.sh %{buildroot}/usr/bin/helloworld.sh

%check
#make test #或make check

#Install and uninstall scripts
%pre

%preun

%post

%postun

#Files list, 每个package的文件列表，遵循，%doc、%license、配置、命令、库、文档和man手册、其他等这样的顺序。
%files
%defattr(-,root,root)
%{_bindir}/helloworld.sh

#%%license license
#%%config


%files libs
%defattr(-,root,root)
#%%lib

%files devel
#%%include
#%%lib*.a

%files help
#%%man、info
#%%doc

#%%other

%changelog
* Wed Jul 18 2018 openEuler Buildteam <buildteam@openeuler.org> - version-release
- Package init
```

现在你可以使用命令rpmdev-setuptree创建工作目录。

```
$ rpmdev-setuptree
$ rpmlint helloworld.spec                //检查spec语法问题
$ rpmbuild -ba helloworld.spec
```

下面是RPM打包工作区的目录布局:

| Directory | Purpose                                                      |
| --------- | ------------------------------------------------------------ |
| BUILD     | 编译构建时的工作目录，在这里解压源代码、打上补丁，执行构建动作。 |
| RPMS      | 构建好的结果，封装在RPM中，存放在这里，按体系结构区分，例如子目录x86_64和noarch。 |
| SOURCES   | 这里实际上就是归档源码仓库的文件，包含源码压缩包、补丁及配置文件等           |
| SPECS     | spec文件存放在这里。                               |
| SRPMS     | 构建生成的SRPM存放在这里。 |

执行rpmbuild命令构建成功后，从结果来看，会生成helloworld、helloworld-libs、helloworld-devel、helloworld-help等4个二进制rpm包:

```
Processing files: helloworld-libs-1.0-1.x86_64
Processing files: helloworld-devel-1.0-1.x86_64
Processing files: helloworld-help-1.0-1.noarch
Checking for unpackaged file(s): /usr/lib/rpm/check-files /root/rpmbuild/BUILDROOT/helloworld-1.0-1.x86_64
Wrote: /root/rpmbuild/SRPMS/helloworld-1.0-1.src.rpm
Wrote: /root/rpmbuild/RPMS/x86_64/helloworld-1.0-1.x86_64.rpm
Wrote: /root/rpmbuild/RPMS/x86_64/helloworld-libs-1.0-1.x86_64.rpm
Wrote: /root/rpmbuild/RPMS/x86_64/helloworld-devel-1.0-1.x86_64.rpm
Wrote: /root/rpmbuild/RPMS/noarch/helloworld-help-1.0-1.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.UnMR3x
+ umask 022
+ cd /root/rpmbuild/BUILD
+ /usr/bin/rm -rf /root/rpmbuild/BUILDROOT/helloworld-1.0-1.x86_64
+ exit 0
```

### 从源代码构建软件

本节从源代码解释构建软件。我们不打算从头阐述什么是源代码，什么是补丁，什么是二进制可执行程序，如何使用configure、make等自动化构建脚本。

我们把关注的焦点放在，从你获取一份包含源代码的压缩包开始，如何从源代码通过spec一步一步的构建出二进制rpm。

首先，需要了解几个重要的概念。

| 概念      | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| 源码包    | 通常是一个以某种格式压缩。如helloworld-1.0.tar.gz，明确的说明了，软件包名称helloworld、版本号1.0、压缩格式tar.gz。 |
| patch补丁 | 补丁是更新源代码的增量源代码。它被格式化为 diff，用来表示两个文本版本之间的不同之处。 使用 diff 创建 diff格式补丁，然后使用patch命令应用补丁于初始源代码。这样你便得到一份修补了某个问题的新代码。在spec的方式中，一般将补丁命令为.patch后缀的文本文件。 |
| 打补丁    | 在源代码目录，使用patch命令或git am来应用补丁到原始代码的过程。这个过程通常放在spec中的`%prep`阶段。 |
| 构建依赖  | 以逗号或空格分隔的包列表，这些包构建软件所需的基础编译环境。可以有 buildrequire 的多个条目，每个条目在spec文件中各自的行上。 |
| 安装依赖  | 是软件安装到系统所必须的运行依赖。通常缺少此部分，软件运行所需的命令、库或其他文件会缺少，导致功能异常。 |
| 源码 RPM  | 是将源码及spec封装一个rpm，通过rpm2cpio解压开，可以看到完整的内容。 |
| 二进制RPM | 将make install所生成的命令或文件，按照一定规则封装到特定格式的rpm中，作为一个集合。 |
| RPM签名   | 对包进行签名是为最终用户保护包的一种方法。签名是为了确保没有第三方可以更改包的内容。 |
| section   | `%prep`、`%build`、`%install`、`%test`、`%clean`，每一个section对应一个动作，rpmbuild命令会将其自动的转化成一个脚本。 |

先来说说基本步骤，重点阐述`%prep`、`%build`、`%install`、`%test`、`%clean`、spec犹如一个构建脚本，将下面的步骤程序化地固定下来:

1. `%prep`    		在这个section，重点完成的工作是如果将原始的源码包，打上补丁，准备编译前的环境。
2. `%build`       相当于源码的make build，只不过这个make build是内嵌在rpmbuild中。
3. `%install`   相当于直接从源码构建安装时的make install，不同的地方是，在rpmbuild过程中，要指定安装的位置%{buildroot}，方便后面files的封装。
4. `%test`	      make test 社区源码的自带测试用例。
5. `%clean`        清理rpmbuild构建生成的临时目录和文件，非必须。

当你从软件包的原生社区拿到一份源码，手动地在本地完成上面各个section的动作，再将上面的动作补充到一个spec标准模板中，同时填写基本的软件包信息，便很快的完成一个软件的打包。


### openEuelr custom amcros
这里有一些openEuler特殊定义的rpm宏，你可能需要了解一下。

```
%disable_rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool \
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%delete_la_and_a
find $RPM_BUILD_ROOT -type f -name "*.la" -delete \
find $RPM_BUILD_ROOT -type f -name "*.a" -delete

%delete_la
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%chrpath_delete
find $RPM_BUILD_ROOT/ -type f -exec file {} ';' | grep "\<ELF\>" | awk -F ':' '{print $1}' | xargs –i chrpath --delete {}

%package_help
%package        help \
Summary:        Documents for %{name} \
Buildarch:      noarch \
Requires:               man info \
\
%description help \
Man pages and other related documents for %{name}.

%install_info()
/sbin/install-info %1 %{_infodir}/dir || :

%install_info_rm()
/sbin/install-info --remove %1 %{_infodir}/dir || :
```

