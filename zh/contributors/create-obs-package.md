# 通过gitee在obs上建仓



## 基本流程

通过修改gitee中的src-openeuler/obs_meta仓库可以实现在obs建仓，基本流程如下：

1. 从src-openeuler/obs_meta  fork 到自己的仓库。
2. 修改fork后的obs_meta仓库。
3. 提交修改。

## 操作步骤

通过修改gitee中的src-openeuler/obs_meta仓库实现在obs建仓的具体操作步骤如下：

1. 点击进入[obs_meta仓库](https://gitee.com/src-openeuler/obs_meta.git)，将其fork到自己的仓库。
2. 将fork完成的obs_meta仓库clone到本地。

```
git clone https://gitee.com/"$username"/obs_meta.git
```

3. 修改obs_meta仓库。以在openEuler:Factory工程项目下添加zip仓库为例。
   * cd obs_meta/projects/openEuler:Factory

   * mkdir zip
   
   * obs使用源服务获取源码([源服务](https://openbuildservice.org/help/manuals/obs-user-guide/cha.obs.source_service.html))，要使用源服务，需要_service文件。openEuler目前统一使用了tar_scm_kernel_repo插件。

   * vim zip/_service 根据自己的需求添加 _service 文件。模板如下：

   ```c
   <services>
     <service name="tar_scm_kernel_repo">
       <param name="scm">repo</param>
       <param name="url">next/openEuler/zip</param>
     </service>
   </services>
   
   /***********************************************************************************************************************************************************************
   * 其中最外层为<services>标记，在<services>内则为一个个<service>函数，而<param>则为<service>函数的参数。
   * 在模板中，tar_scm_kernel_repo将从指定目录(next/openEuler/zip)拉取代码,在gitee src-openeuler/zip仓库的代码提交合入后，后台会将相应代码自动更新到next/openEuler/zip同名目录下。
   ***********************************************************************************************************************************************************************/
   
   ```
	    
   * 将改动提交至gitee，在pr review成功之后将会在obs建立同名仓库。可在obs网站查看：https://117.78.1.88/project

* 注1：obs_meta仓库修改、建仓的pr review提交后，可以在[community](https://gitee.com/openeuler/community.git)提issue，以便我们更及时的回复。
* 注2：gitee-obs一体建仓功能正在开发、测试中，预计5月上线。