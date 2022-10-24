
# 新建SIG申请

[English](./bigdata.md) | 简体中文

说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

# SIG组工作目标和范围

 - sig的必要性 
   数据已经成为土地、劳动力、资本、技术之后的第五生产要素。在这种情况下，openEuler社区需要从技术角度考虑如何更充分的发挥数据在生产、生活中的作用，要构建大数据处理相关能力，由本SIG负责。
 - 该SIG的业务范围
   - openEuler上的大数据基础运行能力，包括数据采集、数据传输、数据存储、数据分析、数据可视等。
   - openEuler上大数据平台，将各种常用的工具软件集成提供统一的用户界面解决让大数据在openEuler上更易用。
   - openEuler上的大数据组件和平台的性能优化，让大数据在openEuler上更好用。
   - openEuler上的大数据相关能力集成，新芯片和软件进入openEuler时的支持。

# 该SIG管理的repository及描述

- [jupyter](https://gitee.com/src-openeuler/jupyter)
  An environment for interactive computing in multiple languages
- [hadoop](https://gitee.com/src-openeuler/hadoop) 
  A software platform for processing vast amounts of data
- [libhdfs](https://gitee.com/src-openeuler/libhdfs) 
  The Apache Hadoop Filesystem Library
- [lzip](https://gitee.com/src-openeuler/lzip) 
  Lossless file compressor based on the LZMA algorithm
- [qrupdate](https://gitee.com/src-openeuler/qrupdate) 
  A Fortran library for fast updates of QR and Cholesky decompositions
- [zookeeper](https://gitee.com/src-openeuler/zookeeper) 
  A high-performance service for building distributed applications
- [kafka](https://gitee.com/src-openeuler/kafka) 
  A Distributed Streaming Platform
- [ibis](https://gitee.com/src-openeuler/ibis) 
  A toolbox to bridge the gap between local Python environments, remote storage, execution systems like Hadoop components (HDFS, Impala, Hive, Spark) and SQL databases. Its goal is to simplify analytical workflows and make you more productive.
- [presto](https://gitee.com/src-openeuler/presto) 
  A distributed SQL query engine for big data.
- [rain](https://gitee.com/src-openeuler/rain) 
  An open-source distributed computational framework for processing of large-scale task-based pipelines.
- [alluxio](https://gitee.com/src-openeuler/alluxio)
  Alluxio (formerly known as Tachyon) is a virtual distributed storage system.
- [ambari](https://gitee.com/src-openeuler/ambari)
  Apache Ambari is a tool for provisioning, managing, and monitoring Apache Hadoop clusters.

# 基本信息

## Maintainers
  - [sinever](https://gitee.com/sinever)
  - [njlzk](https://gitee.com/njlzk)
  - [yangzhao_kl](https://gitee.com/yangzhao_kl)
  - [wuzeyi1](https://gitee.com/wuzeyi1)

## Committers

## 邮件列表
  - bigdata@openeuler.org  
  [点击订阅](https://openeuler.org/zh/community/mailing-list/)  
  [历史信息](https://mailweb.openeuler.org/hyperkitty/list/bigdata@openeuler.org/)  

## 路标

### 大数据平台：
- 0630 同Linaro联合通过bigtop直接在openEuler社区中构建发布版本或Bigtop发布适配openEuler系统版本后以发布包方式在社区呈现
- 0630 联合国内大数据厂商，在openEuler社区发布其对应的大数据平台版本
- 0930 使用jupyter构建openEuler上的数据解决方案

### 优化项目：
- 0930 Vector API：在java中支持Vector API方式直接使用向量指令，以Spark MLlib优化为样例呈现应用中如何使用
- 1230 动态调度(hadoop/hive)：优化各个组件在磁盘上任务调度策略，实现均衡调度以提升磁盘的吞吐量达到性能提升