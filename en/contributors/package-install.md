# Software Package Building

## Building a Local Software Package Using rpm-build<a name="section15377141663015"></a>

Perform the following procedure to build a local software package using rpm-build:

1. Download the source code from the openEuler community.
2. Build a local software package using rpm-build.
3. Obtain and install the built software package.

To build a local software package using rpm-build, perform the following steps:

1. Configure the repo source. For details, see *Configuring a repo Source* in [Development Environment Preparations](https://gitee.com/openeuler/community/blob/master/en/contributors/prepare-environment.md).

2. Build a local software package using rpm-build.
   
   1. Search for the source code to be operated. This section uses OpenSSL as an example. Change it as required.
      
      ```
      $ dnf list | grep openssl
      ```
      
      Check whether the command output contains the src file that includes the OpenSSL software name. If it includes, go to the next step. If no, leave a message in the community.
   
   2. Download the source code file.
      
      ```
      $ yumdownloader --source openssl
      ```
   
   3. Install the OpenSSL software package.
      
      ```
      $ rpm -ivh openssl-1.1.1d-5.src.rpm 
      ```
      
      After the command is executed, the **rpmbuild** directory is generated in the **$HOME** directory. The **rpmbuild** directory contains the following subdirectories:
      
      - **SOURCES**: source code directory, which stores source code packages, such as the .tar packages, and all patches.
      - **SPECS**: Spec file directory, which stores RPM package configuration files (.spec).
   
   4. Switch to the **$HOME/rpmbuild/SPECS** directory and run the **rpmbuild** command to build the software package. As the **rpmbuild** command does not need to be executed by the root user, it is recommended that you run this command as a common user.
      
      ```
      $ cd ~/rpmbuild/SPECS
      $ rpmbuild -ba openssl.spec
      ```
      
      After the command is executed, some error messages may be displayed. The error messages vary with the software packages to be built. Perform troubleshooting based on the error message.
      
      - An error message is displayed, indicating that the dependency package is missing.
        
        After the command is executed, if an error message is displayed indicating that the required software package is missing, install the required software package as prompted. The error message is shown as follows:
        
        error: Failed build dependencies:
        
        lksctp-tools-devel is needed by openssl-1:1.1.1d-5.aarch64
        
        ```
        $ sudo dnf install lksctp-tools-devel -y
        ```
      
      - An error message is displayed, indicating that the self-check fails.
        
        For some software packages, such as Coreutils, Augeas, and Diffutils, after the **rpmbuild** command is executed, the following error message is displayed: **FAIL test-localeconv (exit status: 134).** This occurs because the definitions of the char type in the Aarch64 and x86\_64 architectures are inconsistent. To rectify this error, add the **--fsigned-char** compilation option to the **Makefile** file.
      
      After all errors are rectified, run the **rpmbuild -ba openssl.spec** command again to build the software package. After the compilation is completed, the following directories are added to the **rpmbuild** directory:
      
      - **BUILD**: build directory. The source code package is decompressed to this directory, and the software package is built in the subdirectory of this directory.
      - **RPMS**: directory of the standard RPM package. Binary RPM packages are generated and saved in this directory.
      - **SRPMS**: directory of the source code RPM package. The source code RPM package (SRPM) is generated and saved in this directory.
   
   5. View the result of software package building.
      
      ```
      $ tree ~/rpmbuild/*RPMS
      ```
      
      After the command is executed, the following information is displayed:
      
      /home/user-A/rpmbuild/RPMS
      
      ├── aarch64
      
      │   ├── openssl-1.1.1d-5.aarch64.rpm
      
      │   ├── openssl-debuginfo-1.1.1d-5.aarch64.rpm
      
      │   ├── openssl-debugsource-1.1.1d-5.aarch64.rpm
      
      │   └── openssl-devel-1.1.1d-5.aarch64.rpm
      
      └── noarch
      
      └── openssl-help-1.1.1d-5.noarch.rpm
      
      /home/user-A/rpmbuild/SRPMS
      
      └── openssl-1.1.1d-5.src.rpm
      
      >![](icon/icon-note.gif) NOTE:   
      >If **tree: command not found** is displayed, run the **dnf install tree** command to install the tree software package.

3. Install the built software package.
   
   1. Switch to the directory of the built software package. The installation of the **openssl-devel-1.1.1d-5.aarch64.rpm** software package is used as an example.
      
      ```
      $ cd ~/rpmbuild/RPMS/aarch64
      ```
   
   2. Run the **rpm -ivh** command as the root user to install the software package.
      
      ```
      $ sudo rpm -ivh openssl-devel-1.1.1d-5.aarch64.rpm
      ```
      
      After the command is executed, if an error message is displayed indicating that the required software package is missing, install the required software package as prompted. Refer to the following example for details:
      
      error: Failed dependencies:
      
      krb5-devel is needed by openssl-devel-1:1.1.1d-5.aarch64
      
      ```
      $ sudo dnf install krb5-devel -y
      ```
      
      After the dependency software package is installed, run the **rpm -ivh openssl-devel-1.1.1d-5.aarch64.rpm** command again to install the software package. The installation is completed successfully when the following message is displayed:
      
      Updating / installing...
      
      1:openssl-devel-1:1.1.1d-5         ################################# \[100%]