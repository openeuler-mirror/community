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
    1.  登录[鹏城生态开发者云](https://dw.pcl.ac.cn/cloud/login)网站，进入登录页面。
    2.  注册并激活鹏城生态会员。

        >![](icon/icon-note.gif) **说明：**   
        >仅在未注册和激活时才需要执行本步骤。  

        1.  单击“注册”，进入条款页面。
        2.  认真阅读条款，单击“同意上述条款”。
        3.  认真填写注册信息，带“\*”的必填。
            -   用户名：长度为6-16个字符，仅限字母、数字、下划线、减号。建议以“openEuler-”为前缀。
            -   密码：长度为6\~20个字符，至少包含字母和数字。
            -   邮箱：正常使用的邮箱，因为注册完成后需要登录邮箱以激活账号。

        4.  单击“注册”，并跳转到登录页面。
        5.  输入已注册的用户名和密码，单击“登录”，进入激活邮箱页面。
            -   若页面中包含“激活邮件发送成功！”则执行下一步。
            -   若页面中包含“激活邮件发送失败！”或没有收到激活邮件，则单击“重新发送验证邮件”。
            -   若邮箱已验证，则单击“跳转到登录页面”。

        6.  登录注册时填写的邮箱，单击邮箱中的链接并跳转到激活账号页面。
            -   若页面中包含“恭喜您：_xxx_激活成功”，表示激活成功。则单击“跳转到登录页面”。
            -   若页面中未包含“恭喜您：_xxx_激活成功”，则单击“重新发送验证邮件”。

                其中_xxx_为注册时的用户名。


    3.  输入已注册的用户名和密码，单击“登录”，进入需求列表页面。
    4.  单击“需求申请”以申请虚拟机环境。需求申请中带“\*”的必填。
        1.  根据实际情况填写项目信息，完成后单击“下一步”，其中项目名称要求为：openEuler development，如[图1](#fig11398175166)所示。
    
            **图 1**  项目信息中的项目名称填写<a name="fig11398175166"></a>  
            ![](figure/项目信息中的项目名称填写.png "项目信息中的项目名称填写")
    
        2.  根据实际情况填写产品信息，完成后单击“下一步”。
        3.  根据实际情况填写城市信息，完成后单击“下一步”。
        4.  根据实际情况填写基本信息，完成后单击“下一步”。
        5.  根据实际情况填写资源信息，完成后单击“提交”。
        6.  在需求列表中查看需求申请的状态。
            -   “完成”：表示申请的虚拟机环境已配置。
            -   “待处理”：表示需求申请需要等待处理。此时单击“详情”查看需求申请的详细信息；单击“删除”删除该需求申请；单击“编辑”重新修改该需求申请。
    
        7.  待需求列表中的“状态”为“完成”后，单击左侧的“云主机”进入云主机列表页面。
            -   “详情”：显示云主机的“ID”、“管理员密码”、“映射端口”和“映射协议”。
            -   “更多操作 \> 申请端口”：申请云主机的端口权限。
            -   “更多操作 \> Shutdown”：关闭云主机。
            -   “更多操作 \> Reboot”：重启云主机。
            -   “更多操作 \> Delete”：删除云主机。
    
        8.  在云主机列表页面，单击“详情”，获取云主机的“管理员密码”、“映射端口”。如[图2](#fig77338597358)所示，其中“映射端口”中格式为_xx_._xx_._xx_._xx_:_yy_的内容分别表示云主机的IP地址和端口号。
    
            **图 2**  云主机详情示例<a name="fig77338597358"></a>  
            ![](figure/云主机详情示例.png "云主机详情示例")
    
        9.  使用云主机的IP地址、端口号和管理员密码，通过SSH远程登录工具（如PuTTY）登录云主机。



## 配置repo源<a name="section141211033102420"></a>

可以通过直接获取repo源文件的方式配置repo源或通过挂载ISO的方式配置repo源。

**方式一：通过直接获取repo源文件的方式配置repo源。**

>![](icon/icon-note.gif) **说明：**   
>openEuler提供了多种repo源文件，本操作以AArch64架构的OS repo源文件、源码repo 源文件和全量repo源文件为例。  

1.  进入到yum源目录。

    ```
    # cd /etc/yum.repos.d
    ```

2.  新建local.repo文件并编辑local.repo，将repo源文件配置为yum源。

    ```
    # vi local.repo
    ```

    编辑local.repo文件的内容如下：

    \[basiclocal\]

    name=basiclocal

    baseurl=http://repo.openeuler.org/openEuler-20.03-LTS/OS/aarch64/

    enabled=1

    gpgcheck=0

    \[srclocal\]

    name=srclocal

    baseurl=http://repo.openeuler.org/openEuler-20.03-LTS/source/aarch64/

    enabled=1

    gpgcheck=0

    \[everythinglocal\]

    name=everythinglocal

    baseurl=http://repo.openeuler.org/openEuler-20.03-LTS/everything/aarch64/

    enabled=1

    gpgcheck=0

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
    12. 使用**wget**命令远程下载ISO文件到开发环境，命令中的  _ipaddriso\_ basiceverything_  、  _ipaddriso\_everything_  和  _ipaddriso\_source_  分别为[1.h](#li45321952115717)、[1.i](#li98171862002)和[1.k](#li121355504292)中记录的地址。

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