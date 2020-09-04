# Development Environment Preparations

## Prerequisites<a name="section79608213487"></a>

Hardware: physical or virtual machines (VMs) that run on the 64-bit ARM or x86-64 architecture

## Logging in to the Development Environment<a name="section183361235162117"></a>

- Self-owned development environment
  
  1. Download the openEuler OS and install it. For details about how to install the OS, see the [openEuler 20.03 LTS Installation Guide](https://openeuler.org/en/docs/20.03_LTS/docs/Installation/Installation.html).
     
        >![](icon/icon-note.gif) **NOTE:**   
        >Perform this step only when the openEuler OS is not installed.
  
  2. Log in to the OS using the user name and password set during the OS installation.

- Peng Cheng Ecosystem development environment
  
  1. Create an issue for applying for a VM on [community-issue](https://gitee.com/openeuler/community-issue/issues).
  
  2. Log in to the [Peng Cheng Ecosystem Developer Cloud](https://dw.pcl.ac.cn/cloud/login) website and apply for a VM as instructed.
  
     
  

## Configuring a Repo Source<a name="section141211033102420"></a>

You can configure a repo source by obtaining the repo source file or by mounting an ISO file.

**Method 1: Configure a repo source by obtaining the repo source file.**

>![](icon/icon-note.gif) **NOTE:**   
>openEuler provides multiple repo source files. This section uses the OS, source code, and full repo source files on the AArch64 architecture as an example.

1. Configure the gpg public key required by Yum.
   
   ```
   # cd /etc/pki/rpm-gpg
   # wget https://repo.openeuler.org/openEuler-20.03-LTS/OS/aarch64/RPM-GPG-KEY-openEuler
   ```

2. Go to the Yum source directory.
   
   ```
   # cd /etc/yum.repos.d
   ```

3. Create and edit the **local.repo** file. Configure the repo source file as the Yum source.
   
   ```
   # vi local.repo
   ```
   
   Edit the **local.repo** file as follows:
   
   \[basiclocal]
   
   name=basiclocal
   
   baseurl=http://repo.openeuler.org/openEuler-20.03-LTS/OS/aarch64/
   
   enabled=1
   
   gpgcheck=1
   
   gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-openEuler
   
   \[srclocal]
   
   name=srclocal
   
   baseurl=http://repo.openeuler.org/openEuler-20.03-LTS/source/
   
   enabled=1
   
   gpgcheck=1
   
   gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-openEuler
   
   \[everythinglocal]
   
   name=everythinglocal
   
   baseurl=http://repo.openeuler.org/openEuler-20.03-LTS/everything/aarch64/
   
   enabled=1
   
   gpgcheck=1
   
   gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-openEuler

**Method 2: Configure a repo source by mounting an ISO file.**

>![](icon/icon-note.gif) **NOTE:**   
>openEuler provides multiple ISO files that can be downloaded to the development environment. This section uses the basic ISO, full ISO, and source code ISO on the AArch64 architecture as an example.

1. Download an ISO file.
   
   1. Create a directory for storing the ISO file.
      
      ```
      # mkdir /home/basiciso
      # mkdir /home/everythingiso
      # mkdir /home/srciso
      ```
   
   2. Log in to the openEuler community at [https://openeuler.org/](https://openeuler.org/en/).
   
   3. Click **DOWNLOAD**. The **Download ISO** page is displayed.
   
   4. Click **Link** next to **Download ISO**. The download list is displayed.
   
   5. Select the version to be downloaded, for example, openEuler 20.03 LTS, and click **openEuler-20.03-LTS**. The download list is displayed.
   
   6. Click **ISO**. The ISO download list is displayed.
      
      - aarch64: ISO on the AArch64 architecture
      - x86\_64: ISO on the x86\_64 architecture
      - source: openEuler source code ISO
   
   7. Click **aarch64**. The ISO download list of the AArch64 architecture is displayed.
   
   8. <a name="li45321952115717"></a>Right-click **openEuler-20.03-LTS-aarch64-dvd.iso** and choose **Copy URL** from the shortcut menu to copy the address of the openEuler basic ISO.
   
   9. <a name="li98171862002"></a>Right-click **openEuler-20.03-LTS-everything-aarch64-dvd.iso** and choose **Copy URL** from the shortcut menu to copy the address of the openEuler full ISO.
   
   10. Return to the **ISO** page and click **source**.
   
   11. <a name="li121355504292"></a>Right-click **openEuler-20.03-LTS-source-dvd.iso** and choose **Copy URL** from the shortcut menu to copy the address of the openEuler source code ISO.
   
   12. Run the **wget** command to remotely download the ISO file to the development environment. In the command, *ipaddriso\_ basiceverything*, *ipaddriso\_everything*, and *ipaddriso\_source* are the addresses recorded in [1.8](#li45321952115717), [1.9](#li98171862002), and [1.11](#li121355504292), respectively.
       
       ```
       # cd /home/basiciso
       # wget ipaddriso_basic
       # cd /home/everythingiso
       # wget ipaddriso_everything
       # cd /home/srciso
       # wget ipaddriso_source
       ```

2. Mount the ISO file.
   
   1. Create a mount point.
      
      ```
      # mkdir /mnt/basicdvd
      # mkdir /mnt/everythingdvd
      # mkdir /mnt/srcdvd
      ```
   
   2. Run the **mount** command to mount the ISO file to the mount point.
      
      ```
      # mount /home/basiciso /mnt/basicdvd
      # mount /home/everythingiso /mnt/everythingdvd
      # mount /home/srciso /mnt/srcdvd
      ```
   
   3. Run the **df -h** command to check whether the mounting is successful.
      
      If the command output contains **/mnt/basicdvd**, **/mnt/everythingdvd** and **/mnt/srcdvd**, the mounting is successful. If the mount point is not displayed in the command output, the ISO file fails to be mounted to the mount point. Run the **mount** command to refresh the mount point.
      
      ```
      # df -h
      ```

3. Configure the repo source as the Yum source.
   
   1. Go to the Yum source directory.
      
      ```
      # cd /etc/yum.repos.d
      ```
   
   2. Create and edit the **local.repo** file. Configure the three mounted ISO files as the Yum source.
      
      ```
      # vi local.repo
      ```
      
      Edit the **local.repo** file as follows:
      
      \[basicisolocal]
      
      name=basicisolocal
      
      baseurl=file:///mnt/basicdvd
      
      enabled=1
      
      gpgcheck=0
      
      \[everythingisolocal]
      
      name=everythingisolocal
      
      baseurl=file:///mnt/everythingdvd
      
      enabled=1
      
      gpgcheck=0
      
      \[srcisolocal]
      
      name=srcisolocal
      
      baseurl=file:///mnt/srcdvd
      
      enabled=1
      
      gpgcheck=0
	  

## Installing the Software Package<a name="section15263148132618"></a>

Install the software required for development. The software required varies with the development tools, but the installation methods are the same. This section uses the installation of the rpm-build software as an example.

1. Run the **dnf list installed | grep rpm-build** command to check whether the rpm-build software has been installed.
   
   ```
   # dnf list installed | grep rpm-build
   ```
   
   Check the command output. If the command output contains **rpm-build**, the software has been installed. If no information is displayed, the software is not installed.

2. Clear the cache.
   
   ```
   # dnf clean all
   ```

3. Create a cache.
   
   ```
   # dnf makecache
   ```

4. Install the rpm-build software package.
   
   ```
   # dnf install rpm-build
   ```

5. Query the rpm-build software version.
   
   ```
   # rpmbuild --version
   ```