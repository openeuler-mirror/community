# sig-kubesphere Roadmap

sig-kubesphere is going to provide the native Kubernetes installer for the openEuler community, tailored to openEuler OS. Then we are going to provide an open source container platform KubeSphere built on Kubernetes, which has been widely adopted in thousands of enterprises all over the world.

To better fit into openEuler's ecosystem, sig-kubesphere plans to support [iSulad](https://gitee.com/openeuler/iSulad) and Kata container distribution with Kubernetes and KubeSphere.

We briefly list the roadmap and milestone for the next few months, this is the first phase in our plan:

| Plan | Period |
| ---- | --- |
| Provide the Kubernetes installer that is compatible with openEuler OS, with its image packages | May |
| Provide KubeSphere installation scripts and source code, and the image packages | May |
| Work with SIG-Container to support [iSulad](https://gitee.com/openeuler/iSulad) and Kata container distribution | June ~ July |
| Provide documents for the above projects | May ~ July |


KubeSphere brings the cloud native stack on top of openEuler, means there are multiple image packages need to be submitted into the openEuler registry.

**kubernetes.tar**

```
  - coredns/coredns:1.6.0
  - calico/node:v3.7.3
  - calico/cni:v3.7.3
  - calico/kube-controllers:v3.7.3
  - kubernetes-helm/tiller:v2.14.3
  - mirrorgooglecontainers/cluster-proportional-autoscaler-amd64:1.6.0
  - mirrorgooglecontainers/pause-amd64:3.1
  - openeuler/pause:3.1
  - openeuler/k8s-dns-node-cache:1.15.5
  - openeuler/hyperkube:v1.17.3
```

**kubesphere.tar**

```
  - kubesphere/ks-console:v2.1.1
  - kubesphere/kubectl:v1.0.0
  - kubesphere/ks-account:v2.1.1
  - kubesphere/ks-devops:flyway-v2.1.0
  - kubesphere/ks-apigateway:v2.1.1
  - kubesphere/ks-apiserver:v2.1.1
  - kubesphere/ks-controller-manager:v2.1.1
  - kubesphere/cloud-controller-manager:v1.4.0
  - kubesphere/ks-installer:v2.1.1
  - quay.azk8s.cn/kubernetes-ingress-controller/nginx-ingress-controller:0.24.1
  - mirrorgooglecontainers/defaultbackend-amd64:1.4
  - gcr.azk8s.cn/google_containers/metrics-server-amd64:v0.3.1
  - kubesphere/configmap-reload:v0.3.0
  - kubesphere/prometheus:v2.5.0
  - kubesphere/prometheus-config-reloader:v0.34.0
  - kubesphere/prometheus-operator:v0.34.0
  - kubesphere/kube-rbac-proxy:v0.4.1
  - kubesphere/kube-state-metrics:v1.7.2
  - kubesphere/node-exporter:ks-v0.16.0
  - kubesphere/addon-resizer:1.8.4
  - kubesphere/k8s-prometheus-adapter-amd64:v0.4.1
  - grafana/grafana:5.2.4
  - redis:5.0.5-alpine
  - haproxy:2.0.4
  - alpine:3.10.4
  - quay.azk8s.cn/coreos/etcd:v3.2.18
  - mysql:8.0.11
  - nginx:1.14-alpine
  - postgres:9.6.8
  - osixia/openldap:1.3.0
  - minio/minio:RELEASE.2019-08-07T01-59-21Z
  - minio/mc:RELEASE.2019-08-07T23-14-43Z
```
