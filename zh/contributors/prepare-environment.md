# 开发环境准备



## 前提条件<a name="section79608213487"></a>

硬件：Arm64位或x86\_64位架构的物理机或虚拟机。

## 登录开发环境<a name="section183361235162117"></a>

-   自有环境
    1.  下载openEuler操作系统并进行安装。具体安装操作系统方法请参考[openEuler 20.03 LTS 安装指南](https://openeuler.org/zh/docs/20.03_LTS/docs/Installation/installation.html)。

        >![](icon/icon-note.gif) **说明：**   
        >仅在未安装openEuler操作系统时才需要执行本步骤。  

    2.  使用安装时设置的用户名和密码登录操作系统。

-   鹏城生态开发环境
    1.  在[community-issue](https://gitee.com/openeuler/community-issue/issues)创建申请VM的issue。
    2.  登录[鹏城生态开发者云](https://dw.pcl.ac.cn/cloud/login)网站，按照提示正式申请VM。
    
    详细信息请参考博客文章[Apply for VMs from Peng Cheng Laboratory](https://www.openeuler.org/zh/blog/fred_li/2020-03-25-apply-for-vm-from-pcl.html)。




## 配置repo源<a name="section141211033102420"></a>

可以通过直接获取repo源文件的方式配置repo源或通过挂载ISO的方式配置repo源。

**方式一：通过直接获取repo源文件的方式配置repo源。**

>![](icon/icon-note.gif) **说明：**   
>openEuler提供了多种repo源文件，本操作以AArch64架构的OS repo源文件、源码repo 源文件和全量repo源文件为例。  

1.  配置yum所需的gpg公钥

    ```
    # cd /etc/pki/rpm-gpg
    # wget https://repo.openeuler.org/openEuler-20.03-LTS/OS/aarch64/RPM-GPG-KEY-openEuler
    ```

2.  进入到yum源目录。

    ```
    # cd /etc/yum.repos.d
    ```

3.  新建local.repo文件并编辑local.repo，将repo源文件配置为yum源。

    ```
    # vi local.repo
    ```

    编辑local.repo文件的内容如下：

    \[basiclocal\]

    name=basiclocal

    baseurl=http://repo.openeuler.org/openEuler-20.03-LTS/OS/aarch64/

    enabled=1

    gpgcheck=1

    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-openEuler

    \[srclocal\]

    name=srclocal

    baseurl=http://repo.openeuler.org/openEuler-20.03-LTS/source/

    enabled=1

    gpgcheck=1

    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-openEuler

    \[everythinglocal\]

    name=everythinglocal

    baseurl=http://repo.openeuler.org/openEuler-20.03-LTS/everything/aarch64/

    enabled=1

    gpgcheck=1

    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-openEuler

**方式二：通过挂载ISO的方式配置repo源。**

>![](icon/icon-note.gif) **说明：**   
>openEuler提供了多种ISO，可分别下载到开发环境。本操作以下载AArch64架构的基础ISO、全量ISO和源码ISO为例。  

1.  下载ISO。
    1.  创建存放ISO的目录。

        ```
        # mkdir /home/basiciso
        # mkdir /home/everythingiso
        # mkdir /home/srciso
        ```

    2.  登录openEuler社区，网址为：[https://openeuler.org](https://openeuler.org)。
    3.  单击“下载”，进入下载页面。
    4.  单击“获取ISO：”后面的“Link”，显示版本列表。
    5.  选择需要下载的版本，如openEuler 20.03 LTS，则单击“openEuler-20.03-LTS”，进入下载列表。
    6.  单击“ISO”，进入ISO下载列表。
        -   aarch64：AArch64架构的ISO。
        -   x86\_64：x86\_64架构的ISO。
        -   source：openEuler源码ISO。

    7.  单击“aarch64”，进入AArch64架构的ISO下载列表。
    8.  <a name="li45321952115717"></a>右键单击“openEuler-20.03-LTS-aarch64-dvd.iso”，单击“复制链接地址”，将openEuler基础ISO地址记录好。
    9.  <a name="li98171862002"></a>右键单击“openEuler-20.03-LTS-everything-aarch64-dvd.iso”，单击“复制链接地址”，将openEuler全量ISO地址记录好。
    10. 返回到“ISO”，单击“source”。
    11. <a name="li121355504292"></a>右键单击“openEuler-20.03-LTS-source-dvd.iso”，单击“复制链接地址”，将openEuler源码ISO地址记录好。
    12. 使用**wget**命令远程下载ISO文件到开发环境，命令中的  _ipaddriso\_ basiceverything_  、  _ipaddriso\_everything_  和  _ipaddriso\_source_  分别为[1.8](#li45321952115717)、[1.9](#li98171862002)和[1.11](#li121355504292)中记录的地址。

        ```
        # cd /home/basiciso
        # wget ipaddriso_basic
        # cd /home/everythingiso
        # wget ipaddriso_everything
        # cd /home/srciso
        # wget ipaddriso_source
        ```

2.  挂载ISO。
    1.  创建挂载点。

        ```
        # mkdir /mnt/basicdvd
        # mkdir /mnt/everythingdvd
        # mkdir /mnt/srcdvd
        ```

    2.  执行**mount**命令，将iso分别挂载到挂载点。

        ```
        # mount /home/basiciso /mnt/basicdvd
        # mount /home/everythingiso /mnt/everythingdvd
        # mount /home/srciso /mnt/srcdvd
        ```

    3.  执行**df -h**命令，查看挂载是否成功。

        若打印信息中包含/mnt/basicdvd，/mnt/everythingdvd，/mnt/srcdvd，则表示已挂载成功。若挂载点未出现在打印信息中，则表示该挂载点挂载失败，需要执行**mount**命令，重新刷新该挂载点。

        ```
        # df -h
        ```

3.  repo源配置为yum源
    1.  进入到yum源目录。

        ```
        # cd /etc/yum.repos.d
        ```

    2.  新建local.repo文件并编辑local.repo，将挂载的3个ISO配置为yum源。

        ```
        # vi local.repo
        ```

        编辑local.repo文件的内容如下：
        
        \[basicisolocal\]

        name=basicisolocal

        baseurl=file:///mnt/basicdvd

        enabled=1

        gpgcheck=0

        \[everythingisolocal\]

        name=everythingisolocal

        baseurl=file:///mnt/everythingdvd

        enabled=1

        gpgcheck=0

        \[srcisolocal\]

        name=srcisolocal

        baseurl=file:///mnt/srcdvd

        enabled=1

        gpgcheck=0

## 安装软件包<a name="section15263148132618"></a>

安装开发过程中需要用到的软件。不同的开发需要的软件不一样，但安装方法相同，本章以安装rpm-build软件为例。

1.  执行**dnf list installed  | grep **_rpm-build_  查询rpm-build软件是否已安装。

    ```
    # dnf list installed | grep rpm-build
    ```

    查看命令打印信息，若打印信息中包含“rpm-build”，表示该软件已经安装了，则不需要再安装。若无任何打印信息，则表示该软件未安装。

2.  清除缓存。

    ```
    # dnf clean all
    ```

3.  创建缓存。

    ```
    # dnf makecache
    ```

4.  安装rpm-build软件包。

    ```
    # dnf install rpm-build
    ```

5.  查询rpm-build软件版本。

    ```
    # rpmbuild --version
    ```