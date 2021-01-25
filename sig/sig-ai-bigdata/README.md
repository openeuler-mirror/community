# AI and Big Data SIG

## 概述
大数据和人工智能已经深入到社会的很多领域，各行各业都可以用来提高生产力。工业界、学术界之外也有众多爱好者，为了更好的支持科研院所、生产企业中的爱好者、开发者在 openEuler 上更快更好的进行大数据和人工智能的实践，openEuler 也需要具备大数据和人工智能的相关能力。

## 将 AI 和 Big Data 放在一起的原因
一方面当大数据大规模用于生产时，人工智能还在实验阶段；另一方面，人工智能的普及也是从一个应用，一个部分逐步展开的，导致很多公司的大数据和人工智能从上到下都是两套甚至多套，形成割裂局面。而实际上，大数据的处理结果还可以用于模型训练，而模型的训练需要的样本也需要大数据技术进行预处理。逐步意识到这个问题后，很多大数据工具有了模型训练和推理功能，如 SparkML、FlinkML；而众多人工智能框架也在逐渐增强数据处理能力，更是催生了 Submarine、Tony 这种大数据和人工智能的融合工具。因此 openEuler 里直接将大数据和人工智能放在一起考虑。

## 该SIG的业务范围
  - openEuler 中大数据和人工智能的基础运行能力，包括对各种芯片的支持和加速库，各种数据仓库、分析引擎、训练引擎、算法库、数据集等。
  - openEuler 中大数据和人工智能的统一平台，将各种常用的工具软件集成提供统一的用户界面解决各种维护环境的痛苦，让大数据和人工智能在 openEuler 上更易上手，更好用。
  - openEuler 中大数据和人工智能的性能优化，对通用软件在 openEuler 上的性能优化。
  - openEuler 中大数据和人工智能的能力集成，新芯片和软件进入 openEuler 时的支持。

![logo](./logo.png)

## 会议

- 每周一次，请订阅邮件列表获取具体时间和会议链接
- 线上

## 成员

### Maintainer列表
  - sinever
  - hubble_zhu
  - myeuler

### Committer列表

- sinever

## repository地址：

- https://gitee.com/src-openeuler/jupyter
- https://gitee.com/src-openeuler/tensorflow
- https://gitee.com/src-openeuler/hadoop
- https://gitee.com/src-openeuler/libsvm
- https://gitee.com/src-openeuler/libhdfs
- https://gitee.com/src-openeuler/ComputeLibrary
- https://gitee.com/src-openeuler/arm-ml-examples
- https://gitee.com/src-openeuler/armnn
- https://gitee.com/src-openeuler/libmetal
- https://gitee.com/src-openeuler/oneDNN
- https://gitee.com/src-openeuler/pytorch
- https://gitee.com/src-openeuler/SuperLUMT
- https://gitee.com/src-openeuler/gl2ps
- https://gitee.com/src-openeuler/glpk
- https://gitee.com/src-openeuler/lzip
- https://gitee.com/src-openeuler/octave
- https://gitee.com/src-openeuler/qrupdate
- https://gitee.com/src-openeuler/sundials
- https://gitee.com/src-openeuler/opencl-headers
- https://gitee.com/src-openeuler/eigen
- https://gitee.com/src-openeuler/opencl
- https://gitee.com/src-openeuler/libxsmm
- https://gitee.com/src-openeuler/dlib
- https://gitee.com/src-openeuler/opennn
- https://gitee.com/src-openeuler/mlpack
- https://gitee.com/src-openeuler/ensmallen
- https://gitee.com/src-openeuler/zookeeper
- https://gitee.com/src-openeuler/kafka
- https://gitee.com/src-openeuler/zeppelin
- https://gitee.com/src-openeuler/incubator-mxnet
- https://gitee.com/src-openeuler/opencv
- https://gitee.com/src-openeuler/ibis
- https://gitee.com/src-openeuler/presto
- https://gitee.com/src-openeuler/rain
- https://gitee.com/src-openeuler/ignite
- https://gitee.com/src-openeuler/bigtop

## 路线图
 ![roadmap](./sig-road-map.jpg)

## 联系方式
- [邮件列表](https://mailweb.openeuler.org/hyperkitty/list/sig-ai-bigdata@openeuler.org/)
- [slack](https://join.slack.com/t/openeulerworkspace/shared_invite/zt-fputhzcx-QR9KAqwNmUTN4U2A35BMGQ)
- 微信（欢迎大家添加小助手，小助手会帮忙拉进群交流）  
  <img src="./sig-wechat-qr.jpg" width = "60"/>
