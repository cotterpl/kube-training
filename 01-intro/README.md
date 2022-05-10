# Introduction #

## Install Prerequisites

- docker https://docs.docker.com/get-docker/
- kubectl https://kubernetes.io/docs/tasks/tools/
- kind https://kind.sigs.k8s.io/docs/user/quick-start/#installation

## Kind - Create Cluster

```shell
kind create cluster --config 01-intro/kind_cluster_config.yaml
```

```shell
kind get clusters
```

```shell
kind delete cluster
```

## Kubectl - Talk to Your Cluster

```shell
kubectl get nodes
```

```shell
kubectl describe node <NAME>
```

Kubectl is a CLI wrapper that talks to Kubernetes API:

Try going to: https://localhost:6443/

## Create your first pod

```shell
kubectl apply -f 01-intro/ubuntu_pod.yaml
```

```shell
kubectl get pods
```

Enter pod shell

```shell
kubectl exec -it ubuntu -- /bin/bash
```

See what is in `/var/run/secrets/kubernetes.io`.

## Namespaces

```shell
kubectl create namespace example
```

To work with namespace you need to provide it in the command:

```shell
kubectl get pod -n example
kubectl get pod --namespace example
```

See https://github.com/blendle/kns.

### Exercise

1. Create ubuntu pod in the namespace

## Tooling

Install https://k9scli.io/

### Exercises

1. Figure out how to remove pod.
2. Download yaml definition of created namespace and pod (hint: `-o yaml`). Do you see any fields added by Kubernetes?
3. Check what pods are running in each node.
4. Try finding logs for Kubernetes control plane components.
5. See what is in `~/.kube`. What is `kubectl --context` for? How to switch it?

