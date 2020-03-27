# 构建软件包



## rpm-build本地构建<a name="section15377141663015"></a>

通过rpm-build本地构建软件包的基本过程如下：

1.  从openEuler社区下载源码。
2.  使用rpm-build进行本地构建。
3.  获取并安装已构建的软件包。

rpm-build本地构建软件包的具体操作步骤如下：

1.  配置repo源，具体请参考[开发环境准备](https://gitee.com/openeuler/community/blob/master/zh/contributors/prepare-environment.md)中的配置repo源内容。
2.  使用rpm-build进行本地构建。
    1.  查找需要操作的源码。以openssl为例，请根据实际修改。

        ```
        # dnf list | grep openssl
        ```

        查看打印信息中是否有包含zziplib软件名的.src的文件，若有则继续下面的操作，若无则在社区上留言。

    2.  下载源码文件。

        ```
        # yumdownloader --source openssl.src
        ```

    3.  安装zzliplib软件包。

        ```
        # rpm -ivh openssl-1.1.1d-5.src.rpm 
        ```

        命令执行完成后，会在/root目录下生成rpmbuild目录。rpmbuild目录下有如下目录：

        -   SOURCES：源代码目录，保存源码包（如 .tar 包）和所有 patch 补丁。
        -   SPECS：Spec 文件目录，保存 RPM 包配置（.spec）文件。

    4.  切换目录到/root/rpmbuild/SPECS，然后执行rpmbuild命令构建软件包。

        ```
        # cd ~/rpmbuild/SPECS
        # rpmbuild -ba openssl.spec
        ```

        命令执行后，可能会有一些报错信息，且构建不同的软件包报错信息不同。请根据具体的报错信息进行解决。

        -   缺少依赖包报错信息。

            命令执行后，若有缺少依赖的软件包报错信息，则根据提示安装依赖软件包。 如下所示：

            error: Failed build dependencies:

            lksctp-tools-devel is needed by openssl-1:1.1.1d-5.aarch64

            ```
            # dnf install lksctp-tools-devel -y
            ```

        -   自检失败报错信息。

            有些软件包，如coreutils，augeas，diffutils，在rpmbuild命令执行后，有提示“FAIL test-localeconv \(exit status: 134\)”报错信息。该报错信息是由于Aarch64和x86\_64在char类型上定义不一致导致的，请在Makefile文件中增加--fsigned-char编译选项以解决。

        解决了所有报错信息后再次执行**rpmbuild -ba openssl.spec**构建软件包。编译完成后，在rpmbuild目录会新增如下目录：

        -   BUILD：构建目录，源码包被解压至此，并在该目录的子目录完成构建。
        -   RPMS：标准 RPM 包目录，生成/保存二进制 RPM 包。
        -   SRPMS：源代码 RPM 包目录，生成/保存源码 RPM 包\(SRPM\)。

    5.  查看构建结果。

        ```
        # tree ~/rpmbuild/*RPMS
        ```

        命令执行后，打印信息如下：

        /root/rpmbuild/RPMS

        ├── aarch64

        │   ├── openssl-1.1.1d-5.aarch64.rpm

        │   ├── openssl-debuginfo-1.1.1d-5.aarch64.rpm

        │   ├── openssl-debugsource-1.1.1d-5.aarch64.rpm

        │   └── openssl-devel-1.1.1d-5.aarch64.rpm

        └── noarch

        └── openssl-help-1.1.1d-5.noarch.rpm

        /root/rpmbuild/SRPMS

        └── openssl-1.1.1d-5.src.rpm

        >![](icon/icon-note.gif) **说明：**   
        >若命令执行提示“tree: command not found”，请执行**dnf install tree**安装tree软件包。  


3.  安装构建后的软件包。
    1.  切换到已构建的软件包的目录，以openssl-devel-1.1.1d-5.aarch64.rpm软件包的安装为例。

        ```
        # cd ~/rpmbuild/RPMS/aarch64
        ```

    2.  执行rpm -ivh命令安装软件包。

        ```
        # rpm -ivh openssl-devel-1.1.1d-5.aarch64.rpm
        ```

        命令执行后，若有提示缺少依赖的软件包，则根据提示安装依赖软件包。 如下所示：

        error: Failed dependencies:

        krb5-devel is needed by openssl-devel-1:1.1.1d-5.aarch64

        ```
        # dnf install krb5-devel -y
        ```

        依赖软件包安装完成后再次执行**rpm -ivh openssl-devel-1.1.1d-5.aarch64.rpm**安装软件包。出现如下提示时表示安装成功。

        Updating / installing...

        1:openssl-devel-1:1.1.1d-5         \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# \[100%\]