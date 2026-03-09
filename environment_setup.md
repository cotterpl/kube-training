# Environment Setup for Kubernetes Training #

## Install Prerequisites

- docker or free alternative such as https://podman.io/
- kubectl https://kubernetes.io/docs/tasks/tools/
- kind https://kind.sigs.k8s.io/docs/user/quick-start/#installation

## Check if your environment is setup properly

Create cluster:

```shell
kind create cluster
```

Expected output:

```text
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.35.0) 🖼 
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Have a question, bug, or feature request? Let us know! https://kind.sigs.k8s.io/#community 🙂
```

Check if cluster is there:

```shell
kind get clusters
```

Expected output:

```
kind
```

Check if you can talk to your cluster:

```shell
kubectl get nodes
```

Expected output (age and version may differ):

```
NAME                 STATUS   ROLES           AGE   VERSION
kind-control-plane   Ready    control-plane   59s   v1.35.0
```

You can delete the cluster for now:

```shell
kind delete cluster
```

Expected output:

```
Deleting cluster "kind" ...
```

**You are now ready for the training :)**


