# 开发环境准备



## 前提条件

硬件：Arm64位架构的物理机或虚拟机。



## 登录开发环境

- 自有环境

  1. 下载openEuler操作系统并进行安装。具体安装操作系统方法请参考[openEuler 1.0 安装指南](https://openeuler.org/zh/docs/Installation/installation.html)。

     >![](icon\icon-notice.gif)**说明：**   
     >
     >仅在未安装openEuler操作系统时才需要执行本步骤。  

  2. 使用安装时设置的用户名和密码登录操作系统。

- 鹏城生态开发环境

  1. 登录[鹏城生态开发者云](https://dw.pcl.ac.cn/cloud/login)网站，进入登录页面。

  2. 注册并激活鹏城生态会员。

     >![](icon\icon-note.gif) **说明：**   
     >仅在未注册和激活时才需要执行本步骤。  

     1. 单击“注册”，进入条款页面。

     2. 认真阅读条款，单击“同意上述条款”。

     3. 认真填写注册信息，带“\*”的必填。

        -   用户名：长度为6-16个字符，仅限字母、数字、下划线、减号。建议以“openEuler-”为前缀。
        -   密码：长度为6\~20个字符，至少包含字母和数字。
        -   邮箱：正常使用的邮箱，因为注册完成后需要登录邮箱以激活账号。

     4. 单击“注册”，并跳转到登录页面。

     5. 输入已注册的用户名和密码，单击“登录”，进入激活邮箱页面。

        -   若页面中包含“激活邮件发送成功！”则执行下一步。
        -   若页面中包含“激活邮件发送失败！”或没有收到激活邮件，则单击“重新发送验证邮件”。
        -   若邮箱已验证，则单击“跳转到登录页面”。

     6. 登录注册时填写的邮箱，单击邮箱中的链接并跳转到激活账号页面。

        - 若页面中包含“恭喜您：_xxx_激活成功”，表示激活成功。则单击“跳转到登录页面”。

        - 若页面中未包含“恭喜您：_xxx_激活成功”，则单击“重新发送验证邮件”。

          其中_xxx_为注册时的用户名。
    3.  输入已注册的用户名和密码，单击“登录”，进入需求列表页面。
    4.  单击“需求申请”以申请虚拟机环境。
        1.  填写项目信息，完成后单击“下一步”。项目信息填写如图一所示。
      
            -   项目名称：建议以“openEuler-”为前缀。
            -   项目信息：选择“其他”，输入以“2020 openEuler 参赛项目”为前缀的项目信息。
            -   领域信息：选择“其他”，输入“国产操作系统”。
      
            **图 1**  项目信息示例 
            ![](figure\项目信息示例.png "项目信息示例")
      
        2.  填写产品信息，完成后单击“下一步”，产品信息填写示例如图二所示。
      
            -   产品名称：建议以“openEuler-iSula-”为前缀。
            -   产品信息：选择“互联网类产品”。
            -   云服务器用途：选择“开发”。
      
            **图 2**  产品信息示例  
            ![](figure\产品信息示例.png "产品信息示例")
      
        3. 根据实际填写城市信息，完成后单击“下一步”。
        
        4.  填写基本信息，完成后单击“下一步”。
            -   名称：建议以“openEuler-iSula-”为前缀。
            -   类型：选择“虚拟机”。
            -   使用时长：选择“90天”。
            -   数量：1。
            -   CPU架构要求：选择“鲲鹏920”。
        -   OS 版本要求：选择“openEuler操作系统”。
          
    5.  填写资源信息，完成后单击“提交”。资源信息示例如图三所示。
          
            -   CPU：选择“2”。
            -   虚拟机内存：选择“4G”。
            -   网卡数量：选择“1”。
        -   是否申请云硬盘：不勾选。
          
            **图 3**  资源示例  
        ![](figure\资源示例.png "资源示例")
          
        6.  在需求列表中查看需求申请的状态。
            -   “完成”：表示申请的虚拟机环境已配置。
        -   “待处理”：表示需求申请需要等待处理。此时单击“详情”查看需求申请的详细信息；单击“删除”删除该需求申请；单击“编辑”重新修改该需求申请。
          
        7.  待需求列表中的“状态”为“完成”后，单击左侧的“云主机”进入云主机列表页面。
            -   “详情”：显示云主机的“ID”、“管理员密码”、“映射端口”和“映射协议”。
            -   “更多操作 \> 申请端口”：申请云主机的端口权限。
            -   “更多操作 \> Shutdown”：关闭云主机。
            -   “更多操作 \> Reboot”：重启云主机。
        -   “更多操作 \> Delete”：删除云主机。
          
    8.  在云主机列表页面，单击“详情”，获取云主机的“管理员密码”、“映射端口”。如图4所示，其中“映射端口”中格式为_xx_._xx_._xx_._xx_:_yy_的内容分别表示云主机的IP地址和端口号。
          
            **图 4**  云主机详情示例
        
          ![](figure\云主机详情示例.png "云主机详情示例")
          
        9.  使用云主机的IP地址、端口号和管理员密码，通过SSH远程登录工具（如PuTTY）登录云主机。



## 配置repo源

1. 下载iso。

   1. 创建存放iso的目录。

      >![](icon\icon-note.gif) **说明：**   
      >openEuler提供了3个iso，可分别下载到开发环境。  

      ```
      mkdir /home/insiso
      mkdir /home/srciso
      mkdir /home/everythingiso
      ```

   2. 使用wget命令下载iso文件到开发环境。

      ```
      cd /home/everythingiso
      wget https://121.36.97.194/openeuler1.0/base/iso/openEuler-1.0-Base-Everything-dvd.iso
      cd /home/srciso
      wget https://121.36.97.194/openeuler1.0/base/iso/openEuler-1.0-Base-Source-dvd.iso
      cd /home/insiso
      wget https://121.36.97.194/openeuler1.0/base/iso/openEuler-1.0-Base-aarch64-dvd.iso
      ```

      >![](icon\icon-note.gif) **说明：**   
      >此处以openEuler 1.0 Base版本的下载地址为例。实际下载地址可以通过如下方式获取：  
      >
      >1.  登录[openEuler社区](https://openeuler.org)网站。  
      >2.  单击“下载”，进入下载页面。  
      >3.  单击“获取ISO：”后面的“Link”，显示下载列表。  
      >    ![](icon\icon-note.gif) **说明：**   
      >    若需要获取所有版本的下载地址，请在下载页面单击“获取全部版本\>\>”，并单击对应版本的“ISO”列的“Link”。  

      4.  右键单击需要下载的iso，单击“复制链接地址”。



2. 挂载iso。

   1. 创建挂载点。

      ```
      mkdir /mnt/insdvd
      mkdir /mnt/srcdvd
      mkdir /mnt/everythingdvd
      ```

   2. 执行**mount**命令，将iso分别挂载到挂载点。

      ```
      mount /home/insiso /mnt/insdvd
      mount /home/srciso /mnt/srcdvd
      mount /home/everythingiso /mnt/everythingdvd
      ```

   3. 执行**df -h**命令，查看挂载是否成功。

      若打印信息中包含`/mnt/insdvd`，`/mnt/srcdvd`，`/mnt/everythingdvd`，则表示已挂载成功。若挂载点未出现在打印信息中，则表示该挂载点挂载失败，需要执行**`mount`**命令，重新刷新该挂载点。

      ```
      df -h
      ```

3. repo源配置为yum源

   1. 进入到yum源目录。

      ```
      cd /etc/yum.repos.d
      ```

   2. 新建local.repo文件并编辑local.repo，将挂载的3个iso配置为yum源。

      ```
      vi local.repo
      ```

      编辑local.repo文件的内容如下：

      ```
\[insisolocal\]
      
name=insisolocal
      
baseurl=file:///mnt/insdvd
      
enabled=1
      
gpgcheck=0
      
\[srcisolocal\]
      
name=srcisolocal
      
baseurl=file:///mnt/srcdvd
      
enabled=1
      
gpgcheck=0
      
\[everythingisolocal\]
      
name=everythingisolocal
      
baseurl=file:///mnt/everythingdvd
      
enabled=1
      
      gpgcheck=0
      ```
      
      

## 安装软件包

安装开发过程中需要用到的软件。不同的开发需要的软件不一样，但安装方法相同，本章以安装rpm-build软件为例。

1. 执行`dnf list installed  | grep _rpm-build` 查询rpm-build软件是否已安装。

   ```
   dnf list installed | grep rpm-build
   ```

   查看命令打印信息，若打印信息中包含`rpm-build`，表示该软件已经安装了，则不需要再安装。若无任何打印信息，则表示该软件未安装。

2. 清除缓存。

   ```
   dnf clean all
   ```

3. 创建缓存。

   ```
   dnf makecache
   ```

4. 安装rpm-build软件包。

   ```
   dnf install rpm-build
   ```

5. 查询rpm-build软件版本。

   ```
   rpmbuild --version
   ```

