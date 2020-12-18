# Adding a New Software Package

When adding a software package to Gitee, you can use this procedure to create a repository with the same name as that of the added software package in OBS.

- [Procedure]
- [Modifying the Method of Pulling Code to OBS]

## Procedure

Use this procedure to add a software package by modifying the openEuler/community repository in the Gitee:

1. Go to the [community repository](https://gitee.com/openeuler/community.git) and fork it to your own repository.
2. Clone the community repository that has been forked to the local host.

```
git clone https://gitee.com/"$username"/community.git
```

3. Modify the community repository. The following describes how to add a ZIP software package to Gitee and add the software package to the **openEuler:Factory** project.
   
   * cd community/sig
   
   * Specify the SIG to which the software package belongs. For example, the ZIP software package belongs to the Base-service SIG. (See the *Contributor Guide* to find the SIG or project that you are interested in.)
   
   * Modify the content in the corresponding SIG folder, such as the project list.
   
   * Modify **sig/sigs.yaml** and add the new software package in the form of **- src-openeuler/zip** to the corresponding SIG group list. The following uses the ZIP software package as an example:
   
   ```c
   - name: Base-service
     repositories:
     - src-openeuler/python-cheetah
     - src-openeuler/sombok
     - src-openeuler/yasm
     - src-openeuler/python-redis
     - src-openeuler/python-google-apputils
     - src-openeuler/zopfli
   
     ...
   
     - src-openeuler/jansson
     - src-openeuler/apr
     - src-openeuler/python-lxml
     - src-openeuler/zip
   
   ```
   
   * Submit a Pull Request (PR). (For details, see the [openEuler Community PR Submission Guide](https://gitee.com/openeuler/community/blob/master/zh/contributors/pull-request.md). After the PR is integrated, a repository with the same name will be created in Gitee.) Address: [src-openeuler](https://gitee.com/src-openeuler). In addition, create a repository with the same name on OBS. You can view the repository on the OBS website: https://build.openeuler.org/project/show/openEuler:Factory

## Modifying the Method of Pulling Code to OBS

OBS uses the source service to obtain the source code. To use the source service, the **service** file is required. When a software package is added, the openEuler automatically uses the **tar\_scm\_kernel\_repo** plug-in to pull the code. **service** will be created automatically by ci-bot when package is added to file openeuler.yaml or src-openeuler.yaml. If you want to modify it, use this procedure to modify the **service** file of the corresponding software package in the **src-openeuler/obs\_meta** repository:

1. Go to the [**obs\_meta** repository](https://gitee.com/src-openeuler/obs_meta.git) and fork it to your own repository.
2. Clone the **obs\_meta** repository that has been forked to the local host.

```
git clone https://gitee.com/"$username"/obs_meta.git
```

3. Modify the **obs\_meta** repository.
   * cd obs\_meta/master/openEuler:Factory/
   
   * Run the **vim "package\_name"/service** command to modify the **service** file as required. (In the preceding command, **package\_name** indicates the name of the software package whose **service** file needs to be customized.)
   
   * Submit a PR. After the PR is integrated, the modified **service** file is synchronized to the repository.
