# Environment Setup for Kubernetes Training #

## Install Prerequisites

- docker https://docs.docker.com/get-docker/
- kubectl https://kubernetes.io/docs/tasks/tools/
- kind https://kind.sigs.k8s.io/docs/user/quick-start/#installation

**Note:** Docker requires buying commercial licence for commercial use. If you
don't have it you can find free alternatives. For example

- https://betterprogramming.pub/how-to-install-docker-without-docker-desktop-on-windows-a2bbb65638a1
- https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9

## Check if your environment is setup properly

Create cluster:

```shell
kind create cluster
```

Expected output:

```
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.24.0) 🖼 
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Not sure what to do next? 😅  Check out https://kind.sigs.k8s.io/docs/user/quick-start/
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
kind-control-plane   Ready    control-plane   2m    v1.24.0
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


