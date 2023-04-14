
# 新建SIG申请
[English](ai.md) | 简体中文


说明：本SIG的Charter内容遵循openEuler章程 [README](/zh/governance/README.md)中描述的约定，使用[SIG-governance](/zh/technical-committee/governance/SIG-governance.md)中概述的角色和组织管理。

# SIG组工作目标和范围

 ## sig的必要性
人工智能已经深入到社会的很多领域，各行各业都可以用来提高生产力。工业界、 学术界之外也有众多爱好者，为了更好的支持科研院所、生产企业中爱好者、开发者在openEuler上更快更好的进行人工智能的实践，openEuler需要构建人工智能的相关能力。

## 该SIG的业务范围

- 打造数字基础设施AI生态链，协同芯片厂商、第三方AI框架等一起发展AI产业，包括AI+大数据/HPC/搜索等融合。 
- 提供内置的AI框架训练/推理软件，让生态伙伴能够快速基于内置的AI能力开展AI相关技术探索。
- 构建AI相关软件维护能力，保障上游开源软件的供应安全以及未来的演进。
- 协同MindSpore等社区+openEuler社区，共同致力于开发者生态的繁荣。

# 该SIG管理的repository及描述
- [tensorflow](https://gitee.com/src-openeuler/tensorflow): 
  A framework for deep learning
- [libsvm](https://gitee.com/src-openeuler/libsvm): 
  A Library for Support Vector Machines
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
- [glpk](https://gitee.com/src-openeuler/glpk): 
  GNU Linear Programming Kit
- [octave](https://gitee.com/src-openeuler/octave): 
  A high-level language for numerical computations
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
- [incubator-mxnet](https://gitee.com/src-openeuler/incubator-mxnet): 
  Apache MXNet (incubating) is a deep learning framework designed for both efficiency and flexibility.
- [opencv](https://gitee.com/src-openeuler/opencv): 
  OpenCV means Intel® Open Source Computer Vision Library.
- [alluxio](https://gitee.com/src-openeuler/alluxio):
  Alluxio (formerly known as Tachyon) is a virtual distributed storage system.
- [MindSpore](https://gitee.com/src-openeuler/mindspore):
  MindSpore is a new open source deep learning training/inference framework that could be used for mobile, edge and cloud scenarios.
- [python-asttokens](https://github.com/gristlabs/asttokens):
  Module to annotate Python abstract syntax trees with source code positions

# 基本信息

## Maintainers
- bb-king
- sinever
- zhunaipan
- nicholas_yhr
- liuyang_655
- guoqi1024
- kingxian

## Committers

## 邮件列表
  - ai@openeuler.org

## 路标
- 2022-8-30：MindSpore训练推理打包相关流水线构建搭建完成；
- 2022-9-30：上线MindSpore训练推理 ARCH64版本及配套依赖软件；
- 2023-3-30：上线MindSpore训练推理 X86版本及配套依赖软件；


