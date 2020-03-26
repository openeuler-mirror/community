# 源码下载、编译、安装软件包



## 从openEuler社区下载源码下载

此处以openEuler 1.0 Base版本的下载地址为例。实际下载地址可以通过如下方式获取：

1. 登录[openEuler社区](https://openeuler.org)网站。

2. 单击“下载”，进入下载页面。

3. 单击“获取ISO：”后面的“Link”，显示下载列表。

   >![](icon\icon-note.gif) **说明：**   
   >若需要获取所有版本的下载地址，请在下载页面单击“获取全部版本\>\>”，并单击对应版本的“ISO”列的“Link”。  

4. 右键单击“openEuler-1.0-xxxx-Source-dvd.iso”，单击“复制链接地址”。其中“xxxxx”表示版本号。



## 编译

1. 查找需要操作的源码。以openssl为例，请根据实际修改。

   ```
   dnf list | grep openssl
   ```

   查看打印信息中是否有包含zziplib软件名的.src的文件，若有则继续下面的操作，若无则在社区上留言。

2. 下载源码文件。

   ```
   yumdownloader --source openssl.src
   ```

3. 安装zzliplib软件包。

   ```
   rpm -ivh openssl-1.1.1d-5.src.rpm 
   ```

   命令执行完成后，会在/root目录下生成rpmbuild目录。rpmbuild目录下有如下目录：

   -   SOURCES：源代码目录，保存源码包（如 .tar 包）和所有 patch 补丁。
   -   SPECS：Spec 文件目录，保存 RPM 包配置（.spec）文件。

4. 切换目录到/root/rpmbuild/SPECS，然后执行rpmbuild命令编译软件包。

   ```
   cd ~/rpmbuild/SPECS
   rpmbuild -ba openssl.spec
   ```

   命令执行后，若有提示缺少依赖的软件包，则根据提示安装依赖软件包。 如下所示：

   error: Failed build dependencies:

   lksctp-tools-devel is needed by openssl-1:1.1.1d-5.aarch64

   ```
   dnf install lksctp-tools-devel -y
   ```

   依赖软件包安装完成后再次执行**rpmbuild -ba openssl.spec**编译软件包。编译完成后，在rpmbuild目录会新增如下目录：

   -   BUILD：构建目录，源码包被解压至此，并在该目录的子目录完成编译。
   -   RPMS：标准 RPM 包目录，生成/保存二进制 RPM 包。
   -   SRPMS：源代码 RPM 包目录，生成/保存源码 RPM 包\(SRPM\)。

5. 查看编译结果。

   ```
   tree ~/rpmbuild/*RPMS
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

   >![](icon\icon-note.gif) **说明：**   
   >若命令执行提示“tree: command not found”，请执行**dnf install tree**安装tree软件包。  



## 安装

1. 切换到待安装软件包的目录，以openssl-devel-1.1.1d-5.aarch64.rpm软件包的安装为例。

   ```
   cd ~/rpmbuild/RPMS/aarch64
   ```

2. 执行rpm -ivh命令安装软件包。

   ```
   rpm -ivh openssl-devel-1.1.1d-5.aarch64.rpm
   ```

   命令执行后，若有提示缺少依赖的软件包，则根据提示安装依赖软件包。 如下所示：

   error: Failed dependencies:

   krb5-devel is needed by openssl-devel-1:1.1.1d-5.aarch64

   ```
   dnf install krb5-devel -y
   ```

   依赖软件包安装完成后再次执行**rpm -ivh openssl-devel-1.1.1d-5.aarch64.rpm**安装软件包。出现如下提示时表示安装成功。

   Updating / installing...

   1:openssl-devel-1:1.1.1d-5         \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# \[100%\]

