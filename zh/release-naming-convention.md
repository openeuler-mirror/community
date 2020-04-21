本文档明确openEuler的各个release的包命名规则

# 版本发布规则
openEuler的release遵循以下原则。
+ **版本分类**：openEuler发布两种版本，社区创新版本（community release），长周期维护版本（LTS release)
+ **版本发布频率**：社区创新版本一年两次，长周期维护版本两年一次

# 版本命名规则
openEuler的版本命名以 年 + 月 的形式进行命名，例如20.03代表2020年3月份发布的版本，如果是LTS版本，则加入LTS字样，例如20.03LTS表明2020年3月份发布的LTS版本。

## **iso文件命名规则**：
+ iso文件命名分为5个部分，分别为：
    - **openEuler** : 名称
    - **年.月** : 发布日期
    - **LTS** : 可选项，如果是LTS版本，则增加这个字段，否则无此字段
    - **指令集架构** ：体系架构标识，如aarch64代表arm64架构，x86_64代表amd64架构等
    - **介质类型** ： 通常为dvd

  **社区创新版本** ：例如openEuler-20.09-aarch64-dvd.iso代表2020年9月份发布的arm64体系架构的openEuler社区创新版本。
  **LTS版本** ：例如openEuler-20.03-LTS-aarch64-dvd.iso代表2020年3月份发布的arm64体系架构的长维护周期版本。 

+ **软件包命名规则**：
  软件包命名除去依照[packaging guidelines](https://gitee.com/myeuler/community/tree/master/zh/packaging-guidelines)中原则进行命名之外，软件包在构建过程中需要依照相关release添加release的tag信息。具体规则如下：
    - **社区创新版本**：
