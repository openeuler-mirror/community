
# 新建SIG申请
[English](./sig-ai-bigdata.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

 ![logo](./logo.png)

# SIG组工作目标和范围

 - sig-ai-bigdata的必要性
   - 大数据和人工智能已经深入到社会的很多领域，各行各业都可以用来提高生产力。工业界、
   学术界之外也有众多爱好者，为了更好的支持科研院所、生产企业中爱好者、开发者在openEuler上更快更好的进行大数据和
   人工智能的实践，openEuler也需要具备大数据和人工智能的相关能力。
 - 将artificial intelligence和big data放在一起的原因
   - 一方面当大数据大规模用于生产时，人工智能还在实验阶段，另一方面，人工智能的普及也是从一个应用，一个部分逐步展开的，
   导致很多公司的大数据和人工智能从上到下都是两套甚至多套，形成割裂局面，而实际上，大数据的处理结果还可以用于模型训练，而模型的训练需要的样本也需要大数据技术进行预处理。
   逐步意识到这个问题后，很多大数据工具有了模型训练和推理功能，如sparkml, flinkml，而众多人工智能框架也在逐渐增强数据处理能力，更是催生了submarine、tony这种大数据和人工智能的融合工具。
   因此openEuler里直接将大数据和人工智能放在一起考虑。
 - 该SIG的业务范围
   - openEuler中大数据和人工智能的基础运行能力，包括对各种芯片的支持和加速库，各种数据仓库，分析引擎，训练引擎，算法库，数据集等。
   - openEuler中大数据和人工智能的统一平台，将各种常用的工具软件集成提供统一的用户界面解决各种维护环境的痛苦，让大数据和人工智能在openEuler上更易上手，更好用。
   - openEuler中大数据和人工智能的性能优化，对通用软件在open euler上的性能优化
   - openEuler中大数据和人工智能的能力集成，新芯片和软件进入open euler时的支持

 - 该SIG需要得到openEuler内哪些SIG的支持
   - 有些工具安装会有一些依赖，另外在新硬件支持和性能优化过程中对内核各子系统也可能有依赖。

# 该SIG管理的repository及描述

- [jupyter](https://gitee.com/src-openeuler/jupyter): 
  An environment for interactive computing in multiple languages
- [tensorflow](https://gitee.com/src-openeuler/tensorflow): 
  A framework for deep learning
- [hadoop](https://gitee.com/src-openeuler/hadoop): 
  A software platform for processing vast amounts of data
- [libsvm](https://gitee.com/src-openeuler/libsvm): 
  A Library for Support Vector Machines
- [libhdfs](https://gitee.com/src-openeuler/libhdfs): 
  The Apache Hadoop Filesystem Library
- [ComputeLibrary](https://gitee.com/src-openeuler/ComputeLibrary): 
  ARM Compute Library
- [arm-ml-examples](https://gitee.com/src-openeuler/arm-ml-examples): 
  Machine learning examples used in Arm's ML developer space
- [armnn](https://gitee.com/src-openeuler/armnn): 
  Arm NN SDK enables machine learning workloads on power-efficient devices
- [oneDNN](https://gitee.com/src-openeuler/oneDNN): 
  Intel(R) Math Kernel Library for Deep Neural Networks
- [pytorch](https://gitee.com/src-openeuler/pytorch): 
  python deep learning framework
- [SuperLUMT](https://gitee.com/src-openeuler/SuperLUMT): 
  Single precision real SuperLU routines for shared memory parallel machines
- [gl2ps](https://gitee.com/src-openeuler/gl2ps): 
  An OpenGL to PostScript printing library
- [glpk](https://gitee.com/src-openeuler/glpk): 
  GNU Linear Programming Kit
- [lzip](https://gitee.com/src-openeuler/lzip): 
  Lossless file compressor based on the LZMA algorithm
- [octave](https://gitee.com/src-openeuler/octave): 
  A high-level language for numerical computations
- [qrupdate](https://gitee.com/src-openeuler/qrupdate): 
  A Fortran library for fast updates of QR and Cholesky decompositions
- [sundials](https://gitee.com/src-openeuler/sundials): 
  Suite of nonlinear solvers
- [opencl-headers](https://gitee.com/src-openeuler/opencl-headers):  
  OpenCL (Open Computing Language) header files
- [eigen](https://gitee.com/src-openeuler/eigen): 
  a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.
- [opencl](https://gitee.com/src-openeuler/opencl): 
  OpenCL ICD Bindings
- [libxsmm](https://gitee.com/src-openeuler/libxsmm): 
  Library targeting Intel Architecture for specialized dense and sparse matrix operations, and deep learning primitives.
- [dlib](https://gitee.com/src-openeuler/dlib): 
  A modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real world problems.
- [opennn](https://gitee.com/src-openeuler/opennn): 
  An open source neural networks library for machine learning.
- [mlpack](https://gitee.com/src-openeuler/mlpack): 
  A fast, flexible machine learning library, written in C++
- [ensmallen](https://gitee.com/src-openeuler/ensmallen): 
  A flexible C++ library for efficient numerical optimization
- [zookeeper](https://gitee.com/src-openeuler/zookeeper): 
  A high-performance service for building distributed applications
- [kafka](https://gitee.com/src-openeuler/kafka): 
  A Distributed Streaming Platform
- [incubator-mxnet](https://gitee.com/src-openeuler/incubator-mxnet): 
  Apache MXNet (incubating) is a deep learning framework designed for both efficiency and flexibility.
- [opencv](https://gitee.com/src-openeuler/opencv): 
  OpenCV means Intel® Open Source Computer Vision Library.
- [ibis](https://gitee.com/src-openeuler/ibis): 
  A toolbox to bridge the gap between local Python environments, remote storage, execution systems like Hadoop components (HDFS, Impala, Hive, Spark) and SQL databases. Its goal is to simplify analytical workflows and make you more productive.
- [presto](https://gitee.com/src-openeuler/presto): 
  A distributed SQL query engine for big data.
- [rain](https://gitee.com/src-openeuler/rain): 
  An open-source distributed computational framework for processing of large-scale task-based pipelines.
- [alluxio](https://gitee.com/src-openeuler/alluxio):
  Alluxio (formerly known as Tachyon) is a virtual distributed storage system.
- [ambari](https://gitee.com/src-openeuler/ambari):
  Apache Ambari is a tool for provisioning, managing, and monitoring Apache Hadoop clusters.

# 基本信息

## 项目介绍
    [详情](https://gitee.com/openeuler/community/sig/sig-ai-bigdata/)

## Maintainers
  - [sinever](https://gitee.com/sinever)
  - [njlzk](https://gitee.com/njlzk)
  - [yangzhao_kl](https://gitee.com/yangzhao_kl)
  - [unioah](https://gitee.com/unioah)

## Committers

## 邮件列表
  - sig-ai-bigdata@openeuler.org  
  [点击订阅](https://openeuler.org/zh/community/mailing-list/)  
  [历史信息](https://mailweb.openeuler.org/hyperkitty/list/sig-ai-bigdata@openeuler.org/)  

## 路线图
 ![roadmap](./sig-road-map.jpg)
