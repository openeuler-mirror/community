# openEuler软件打包指南

目录

- [软件打包基础说明](#id1)
  - [打包规则](#id1-1)
  - [打包基础知识](id1-2)
- [openEuler打包规则](#id2)
  - [软件包拆分/合并规则](#id2-1)
- [SPEC编写规范](#id3)
  - SPEC文件说明
  - [openEuler custom amcros](#id4)
  - [软件打包验证](#id5)
  
- [范例说明](#id5)
  - [范例一](#id5-1)
  - [范例二](#id5-2)
  - [范例三](#id5-3)
  - [范例四](#id5-4)
  - [范例五](#id5-5)



<h2 id="id1">软件打包基础</h2>

**打包** 是指编译并捆绑软件与元数据，例如软件全名、描述、正常运行所需要的依赖列表等的动作。这是为了让软件使用者可以使用类似RPM等软件包管理器，方便舒服的对其所使用的软件进行安全、升级或者删除。



<h3 id="id1-1">打包规则</h3>
openEuler社区综合了多个开源项目的软件包，并把他们集成到一个系统中。所以规范化多种多样的开源项目到一个连贯的系统中是非常有必要的。此处简要描述openEuler社区的打包规则：

- 我们遵守一般的[Linux基础标准（LSB）]()。该标准致力于减少各个发现版之间的差异；

- 我们遵守[Linux文件系统层级标准（FHS）]()。该标准主要是关于如何管理Linux文件系统层级的参考；

- 除了遵守以上Linux发行版通常都会默认遵守的规则，本指南还规范化了为openEuler社区的软件包打包的的规则要求。

  

<h3 id="id1-2">打包基础知识</h3>
一个软件包（假设软件包名为*pgname*）通常会拆分成多个RPM包：

- **与软件包同名的主包**：包括命令、配置、动态库（简单的软件无需对外提供libs时会使用）等

- **libs包**：提供动态库，供二次开发和使用，通常命名为*pgname*-libs

- **开发用devel包**：提供动态库、编译使用的头文件，两者命名方式和拆分原则一致？？？？？，通常命名为*pgname*-devel？？

- **开发用static包** ：提供.a等静态编译需要的组件，通常命名为devel-static

- **文档doc包**：提供二次开发文档、接口函数说明手册、范例和man、info等手册

- **本地化支持lang包**：提供语言和时区等本地化支持，通常命名为*pgname*-local；

- **其他包**：如server、utils、tools、plugins等，和包的功能紧密相关的软件包，比如部分网络软件单独提供一个server或clinet包。

  大部分软件包遵循以上拆分原则，openEuler在次基础上定义了自己的打包规则，以指导软件包的拆分、依赖关系建立，从而形成自己的软件包体系。



<h2 id="id2">openEuler打包规则</h2>
<h3 id="id2-1">软件包拆分/合并规则</h3>
openEuler将软件包拆分成3个主要的二进制RPM包：主包、devel包和help包，其规则如下：

 - **主包**
     - 包名：*pgname*
     - 包含内容：命令、配置、本软件包包含的命令运行所需的so，以及本软件对外提供的动态库、license、copyright、Author、readme（如果包含版权信息）
     - 主要变化：主包中的man、info、readme等功能、版权、license无关的文档信息拆分到help包中
     - 关键点：通过Provides、Obsoletes声明实现与前项版本的兼容
        - 动态库.so，RPM构建会到处动态库的内容，无需单独提供Provides声明
        - libs包合并到主包后，Provides的内容RPM无法自动导出，需要在主包对原来libs包中的内容追加Provides声明
        - 原本libs包提供的功能已经又主包提供，可以添加Obsoletes来指明主包已经替换了libs包（请参见[范例一]()）
 - **devel包**
      -  包名：*pgname*-devel
      - 包含内容：静态库.a、头文件、example范例、test用例、其他开发使用的内容
      - 主要变化：
         - 合并devel包和static包
         - 所有开发使用的内容都收编到devel包中
      - 关键点：
         - 所有属于开发范围的内容，统一打包成devel包。如果devel的内容包含了原来static等包提供的功能，需要应用Provieds和Obsoletes来保持和前项版本的兼容
         - 动态库打包到主包后，devel包一般需要Requires主包，否则部分动态库会找不到
 - **help**包
       - 包名：*pgname*-help
       - 包含内容：二次开发文档、接口函数说明手册和man、info手册等相关文档和手册
       - 主要变化：主包中的man、info等手册和文档拆分到help包中
       - 关键点：
             - 通常help包只依赖man、info等手册查询工具，不需要任何其他编译依赖和安装依赖。
             - 外部大部分软件包以doc包命名，修改时需要将其改成help包（请参考[范例二]()）

如果是复杂软件包，在上面3个分类的基础上，特殊场景还需考虑：

- **for-language包**
  - 包名：如python2-*pgname*、python3-*pgname*、per-*pgname*
  - 包含内容：针对perl、python2、python3等语言的支持的分拆
  - 主要变化：NA
  - 关键点：NA

- **本地化支持包**
  - 包名：*pgname*-lang
  - 包含内容：本地化、语言支持、时区相关等国际化相关内容。这里是针对复杂的、国际化的相关软件，简单的包不需要单独拆分出lang
  - 主要变化：所有lang合并成一个，不针对国家、地区进行拆分
  - 关键点：NA
- **其他复杂和特殊包**
  - 包名：例如openssh-server、openssh-client等
  - 包含内容：NA
  - 主要变化：建议尽可能将原有内容按照上面分类拆分，减少此类包
  - 关键点：单独评审是否有此类包



<h2 id="id3">SPEC编写规范</h2>
<h3 id="id3-1">SPEC文件说明</h3>
**spec中的缩进统一格式，使用空格，保持对齐**

**文件头**

> *Name*：#软件包名字，**保持**
>
> *Version*：#软件版本号，**保持**
>
> *Release*：#软件包发行号，**变更**。例如：`RElease:4%{?dist}->5`
>
> *Summary*：#概要，**变更**。一句话概括该软件包信息，打开URL查看软件包主页信息
>
> *License*：#变更：软件授权方式，多个License之间用and隔开。错误格式：LGPLv2 BSD，正确格式：LGPLv2 and BSD
>
> *Group*：#组信息，**删除**
>
> *URL*：#一般**保持**，需尝试登陆能否登上，无效的要替换成有效的
>
> *Source*：#**保持**，源码包的名字/下载地址，按顺序表示
>
> *Patch*：#补丁，需标明补丁来源，以保证补丁可溯性，**保持**
>
> *Description*：软件包具体描述

说明：

1.基础字段全部使用空格保证对齐，且各项关键字顺序需与上述一致

2.openEuler会自动匹配当前芯片架构，`%{?_isa}`可去除，比如`%{name}%{?_isa}`可以替换成`%{name}`

3.spec中version、release比较复杂的场景，如果灭有特殊要求，尽量简化为单个数字，且保持递增，h和`%{?dist}`的后缀要去除



**软件包依赖**

> - *BuildRequires*：定义build时所依赖的软件包，在构建编译软件包时需要的辅助工具。**尽量写到一行，用空格隔开，gcc建议去掉，因为一般环境中已经存在，无需特意说明。且写包名即可**，例如`%{bindir}/man`替换成`man`
> - *Requires*：定义安全时的依赖包，指二进制软件包在其他机器上的安装时，所需要依赖的其他软件包，**尽量写成一行，用空格隔开**。RreReq、Requires（pre）、Requires（post）、Requires（preun）、Requires（postun）等都是针对不同阶段的依赖指定的，**策略相同**。

说明：
1.该部分的依赖关系定义了一个软件包正常工作需要依赖其他软件包，在RPM包升级、安装和删除的时候需要确保依赖关系得到满足
2.多个编译依赖或安装依赖可以汇总成1~3行，这样看起来简洁



**预处理阶段（%prep）**

该阶段描述了解压源码包的方法

`%setup -q# ` 解压源文件程序

`patch #`  应用对应补丁

推荐更改成`%autosetup`命令，自动解压源码包和打补丁（请参考[范例三]()）



**编译阶段**（%build）

`%configure`：#configer文件默认不编译静态库，参数`--disable-static`可以去掉。#配置参数尽量**合并**一行（请参考[范例四]()）

`make`：#替换成`%nake build`（请参考[范例五]()）

说明：configure、make等编译命令，选项如果没有宏控制，可以汇总到1行。



**安装阶段**（%install）

需替换的指令：

1.清空安装目录在安装时会自动清除，`rm -rf %{buildroot}`和`rm -rf $RPM_BUILD_ROOT`命令可以删除

2.删除*.la和.a文件命令：

`rm %{buildroot}%{_libdir}/*.la`

或者

```
find $RPM_BUILD_ROOT -type f -name "*.la" -delete \
find $RPM_BUILD_ROOT -type f -name "*.a" -delete \
```

可以用宏`%delete la and a`调换

3.删除*.la文件：

`find $RPM_BUILD_ROOT -type f -name "*.la" -delete `

可以用宏`%delete la`调换



**%file阶段%**

%file是对软件打包时，**打包的顺序要和前面定义package的顺序保持一致**



<h3 id="id3-2">openEuelr custom amcros</h3>

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
Requires:		man info \
\
%description help \
Man pages and other related documents for %{name}. 

%install_info() 
/sbin/install-info %1 %{_infodir}/dir || :

%install_info_rm() 
/sbin/install-info --remove %1 %{_infodir}/dir || :
```



<h3 id="id3-3">软件打包验证</h3>
建议从下面三个角度验证。

- 不同的软件列表，软件选型
- 独立的软件拆分规则
- 基于不同分拆规则的软件依赖关系树。
- 确认软件是否重新选型，重新选型后，是否有接口、功能、使用方式上的差异，软件升级后，是否导致依赖此软件的上层软件功能异常。
- 如果软件未做选型升级，确认拆分前后，所有二进制RPM包含的内容是否有变化、遗漏，可以通过`rpm –qpl`查询对比。
- 拆分前后生成二进制RPM的Provides、Requires是否有变化，可以通过命令`rpm --provides` 或`rpm --requires`查看。特别是主包收编libs包的场景，要查看主包是否包含原libs包Provides、Requires内容。
- 将软件拆分前编译的二进制全部安装到系统，查看软件选型打包后的二进制包是否可以使用`rpm –Uvh`进行正确升级。
- 安装升级后，验证：① 服务类的，验证`start/ stop /restart/reload`；② 命令类的，至少要验证基本功能可用。
- 软件选型升级后，对其他软件包的影响，很难独立判断，需要做集成测试。



<h2 id="id3">范例</h2>
