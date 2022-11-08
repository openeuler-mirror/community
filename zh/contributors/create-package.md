# 新增软件包

执行以下步骤，可以在gitee新增软件包的同时在obs建立同名仓库！

- [操作步骤](#操作步骤)
- [修改obs拉取代码方式](#修改obs拉取代码方式)

## 操作步骤

通过修改gitee中的openeuler/community仓库实现新增软件包的具体操作步骤如下：

1. 点击进入[community仓库](https://gitee.com/openeuler/community.git)，将其fork到自己的仓库。
2. 将fork完成的community仓库clone到本地。

```
git clone https://gitee.com/"$username"/community.git
```

3. 修改community仓库。以在gitee新增zip软件包，并且同步在openEuler:Factory工程项目下添加该包为例。
   * cd community/sig

   * 明确软件包所属的sig组，如zip属于Base-service组（请参考贡献者指南中的找到您感兴趣的SIG或项目）；
   
   * 修改所属sig文件夹下的内容，如项目清单等；
   
   * 修改所属sig文件夹下的sig-info.yaml，将要新增的软件包以"- src-openeuler/zip"的形式添加到对应的sig组列表下；以zip为例，修改sig/Base-service/sig-info.yaml：
   
   ```yaml
        repositories:
        - repo: 
          - openeuler/openEuler-rpm-config
          - src-openeuler/abseil-cpp
          - src-openeuler/acl
          - src-openeuler/acpica-tools
          - src-openeuler/adcli
          - src-openeuler/aide
          - src-openeuler/airline
     
         ...
     
          - src-openeuler/jansson
          - src-openeuler/apr
          - src-openeuler/python-lxml
          - src-openeuler/zip
 
   ```

   * 建仓：在 sig/{sig目录}/src-openeuler/软件名首字母 新增下对应的yaml文件(openeuler社区维护项目: openeuler目录；其他社区引入包: src-openeuler目录。示例参考：sig/Base-service/src-openeuler/z/zip.yaml)

   ```yaml
   name: pkgname
   description: about pkgname
   upstream: https://somepkg.org/
   branches:
   - name: master
     type: protected
   type: public
   ```

   * 提交PR（请参考[PR提交指南](https://gitee.com/openeuler/community/blob/master/zh/contributors/pull-request.md)，PR合入后将会在gitee建立同名仓库。查看地址：[src-openeuler](https://gitee.com/src-openeuler)。同时在obs上建立同名仓库，可在obs网站查看：https://build.openeuler.org/project/show/openEuler:Factory
   
## 修改obs拉取代码方式

obs使用源服务获取源码([源服务](https://openbuildservice.org/help/manuals/obs-user-guide/cha.obs.source_service.html))，要使用源服务，需要_service文件。新增软件包时，openEuler自动使用了tar_scm_kernel_repo插件拉取代码。可通过修改src-openeuler/obs_meta仓库下对应软件包的_service文件实现自定义更改，具体步骤如下：
   
1. 点击进入[obs_meta仓库](https://gitee.com/src-openeuler/obs_meta.git)，将其fork到自己的仓库。
2. 将fork完成的obs_meta仓库clone到本地。

```
git clone https://gitee.com/"$username"/obs_meta.git
```
3. 修改obs_meta仓库。
   * cd obs_meta/master/openEuler:Factory/

   * vim "package_name"/_service 根据自己的需求修改 _service 文件。(package_name是需要自定义_service文件的软件包名称)
	    
   * 提交PR，PR合入后将会把修改后的_service文件同步到该仓库。
