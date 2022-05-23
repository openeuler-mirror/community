# Adding a New Software Package

Perform the following procedure to add a software package to Gitee and create a repository with the same name as the added software package in OBS.

- [Procedure](#procedure)
- [Modifying the Method of Pulling Code to OBS](#modifying-the-method-of-pulling-code-to-obs)

## Procedure

Add a new software package by modifying the openeuler/community repository on Gitee.

1. Go to the [community repository](https://gitee.com/openeuler/community.git) and fork it to your own repository.
2. Clone the forked community repository to the local host.

```
git clone https://gitee.com/"$username"/community.git
```

3. Modify the community repository. The following describes how to add the **zip** software package to Gitee and add the package to the **openEuler:Factory** project.
   * cd community/sig

   * Find the SIG to which the software package belongs. For example, the **zip** package belongs to the Base-service SIG. (See the *Contributor Guide* to find the SIG or project that you are interested in.)
   
   * Modify the contents in the corresponding subfolder of the **sig** folder, such as the project list.
   
   * Modify the **sig-info.yaml** file of the corresponding SIG in the **sig** folder and add the software package in the form of **- src-openeuler/zip**. The following uses the **zip** software package as an example to describe how to modify **sig/Base-service/sig-info.yaml**:
   
   ```yaml
        repositories:
        - repo: openeuler/openEuler-rpm-config
        - repo: src-openeuler/abseil-cpp
        - repo: src-openeuler/acl
        - repo: src-openeuler/acpica-tools
        - repo: src-openeuler/adcli
        - repo: src-openeuler/aide
        - repo: src-openeuler/airline
     
         ...
     
        - repo: src-openeuler/jansson
        - repo: src-openeuler/apr
        - repo: src-openeuler/python-lxml
        - repo: src-openeuler/zip
 
   ```

   * Add the corresponding YAML file to **sig/***{sig_directory}***/src-openeuler/***initial_letter_of the_software_name* to create a repository. (For projects maintained by the openEuler community, use the **openeuler** directory. For packages introduced from other communities, use the **src-openeuler** directory. Example: **sig/Base-service/src-openeuler/z/zip.yaml**)

   ```yaml
   name: pkgname
   description: about pkgname
   upstream: https://somepkg.org/
   branches:
   - name: master
     type: protected
   type: public
   ```

   * Submit a pull request (PR). For details, see the [Pull Request Submission Guide](pull-request.md). After the PR is merged, a repository with the same name as the added software package will be created in [src-openeuler](https://gitee.com/src-openeuler) on Gitee. A repository with the same name will be created on OBS. You can view the repository at <https://build.openeuler.org/project/show/openEuler:Factory>.
   
## Modifying the Method of Pulling Code to OBS

OBS uses the [source service](https://openbuildservice.org/help/manuals/obs-user-guide/cha.obs.source_service.html) to obtain the source code. The **_service** file is required for using the source service. When a software package is added, openEuler automatically uses the **tar_scm_kernel_repo** plug-in to pull code. You can modify the **_service** file of the corresponding software package in the **src-openeuler/obs_meta** repository. The procedure is as follows:
   
1. Go to the [obs_meta repository](https://gitee.com/src-openeuler/obs_meta.git) and fork it to your own repository.
2. Clone the forked obs_meta repository to the local host.

```
git clone https://gitee.com/"$username"/obs_meta.git
```
3. Modify the obs_meta repository.
   * cd obs_meta/master/openEuler:Factory/

   * **vim "***package_name***"/service** Modify the **_service** file as required. (*package_name* indicates the name of the software package whose **_service** file needs to be customized.)
	    
   * Submit a PR. After the PR is merged, the modified **_service** file is synchronized to the repository.
