
# Application to create a new SIG
English | [简体中文](./sig-ai-bigdata_cn.md)


Note: The Charter of this SIG follows the convention described in the openEuler charter [README] (/en/governance/README.md), and follows [SIG-governance] (/en/technical-committee/governance/SIG-governance.md).

## SIG Mission and Scope

- Why we create sig-ai-bigdata in openEuler
  - Big data and artificial intelligence have penetrated into many areas of our society, and used to improve productivity in many industries. 
  There are lots of enthusiasts outside the industrial and academic circles. 
  It is necessary to provide big data and artificial intelligence-related capabilities in open euler for scientists in research institutes and enthusiasts to implement big data and artificial intelligence on open euler, 

- Why we keep artificial intelligence and big data together
  - On the one hand, when big data is used in production on a large scale, artificial intelligence is still in the experimental stage, on the other hand, the popularization of artificial intelligence is gradually being imported from one application to another, leading to a split situation of the big data and artificial intelligence in many companies.
    In fact, the processing results of big data can then be used for model training, and the samples required for model training also require big data technology for preprocessing.
    After gradually realizing this, many big data tools have model training and inference functions, such as sparkml for spark, flinkml for flink, and many artificial intelligence frameworks are gradually enhancing their data processing capabilities, which has also spawned a few fusion tools such as big data and tony.
    Therefore, big data and artificial intelligence are directly considered together in open euler.

- The scope of the SIG
  - Basic capabilities of big data and artificial intelligence in open euler, including but not limited to supporting and accelerating libraries for various chips, various data warehouses, analysis engines, training engines, algorithm libraries, data sets, etc.
  - A unified platform for big data and artificial intelligence in open euler, integrating various commonly used tools and software to provide a unified user interface to make big data and artificial intelligence easier and better to use on open euler.
  - Performance optimization of big data and artificial intelligence in open euler.
  - Integration of big data and artificial intelligence capabilities in open euler, supporting new chips and softwares in open euler

- Which SIGs in openEuler to coorperate with
  - Some tool may have some dependency packages, and in addition, they may have dependencies on kernel subsystems during new hardware support and performance optimization.

### Deliverables
- Source and tar
 
### Repositories and description managed by this SIG

- project name:
  - data store, cache, query
    - hdfs
    - kafka
    - hbase
    - hive
    - pular
    - druid
  - framework and library for data analysis
    - spark
    - flink
    - mapreduce
    - beam
    - pandas
    - numpy
  - model training and predicting
    - tensorflow
    - caffe
    - scikit-learn
    - pytorch
    - libsvm
    - mkl
    - neon
    - dlib
    - daal
  - develop environment
    - jupyter
    - zeppelin
  - resource management
    - kubernetes
    - mesos
    - yarn
  - to be continued

### Cross-domain and external-oriented processes

Cross-domain and externally-oriented processes and actions defined and implemented by this SIG:

- Non-Internal Process Checklist

- The organization guidance plan for the entire openEulerSIG owned by this SIG, etc.


## Basic Information

### Project Introduction
    https: /gitee.com/openeuler/community/sig/sig-xxxx/

***Tips***: After the SIG is successfully created, https: /gitee.com/openeuler/community/sig/sig-xxxx/ management will be managed by the Maintainer, and the project team can enrich their project introduction, including but not limited to the following content.
```
### Maintainers
  - sinever
  - ZZZHB
  - njlzk
  - myeuler
  - chxssg

### Committers
  - sinever

### Mailing list

### IRC Channel

### Conference Information

### External Contact
-Name (Gitee ID)
```

