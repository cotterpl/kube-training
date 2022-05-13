# Introduction #

## Install Prerequisites

- docker https://docs.docker.com/get-docker/
- kubectl https://kubernetes.io/docs/tasks/tools/
- kind https://kind.sigs.k8s.io/docs/user/quick-start/#installation

## Kubernetes Introduction

See: https://www.javatpoint.com/kubernetes

Why kubernetes:

- Standardized declarative deployment of software
- Everything runs in a container that you fully control
- High availability and scaling out of the box
- No need for dedicated/virtual machines - big savings
- Rich flexibility, less DevOps work
- Forget about logs rotations.
- Ad-hoc jobs https://kubernetes.io/docs/concepts/workloads/controllers/job/
- Authentication and authorization mechanisms both for humans and your
  applications
  https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
- Many environments in one
  cluster: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/

Against kubernetes:

- It is complex.
- Steep learning curve.

Before learning Kubernetes you should be familiar with:

- Containers: Docker and Docker compose
- Networking

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

To ask cluster to create pod:

```shell
kubectl apply -f 01-intro/ubuntu_pod.yaml
```

See if it has been created:

```shell
kubectl get pods
```

Enter pod shell:

```shell
kubectl exec -it ubuntu -- /bin/bash
```

See what is in `/var/run/secrets/kubernetes.io`.

## Namespaces

Namespace offers for logical separation of environments.

Many 'things' must have unique names but those names can be the same if they are
in separate namespaces.

To create a namespace called `example` run:

```shell
kubectl create namespace example
```

To work with namespace you need to provide it in the command:

```shell
kubectl get pod -n example
kubectl get pod --namespace example
```

Tip: https://github.com/blendle/kns.

Namespaces are useful for:

- separation of environments, you can have: dev/staging/ad-hoc environment in
  one cluster
- separation of infrastructure related software (for example keeping things like
  metric server, ArgoCD in separate namespace)

Note: You can apply limit resources available to
namespace https://kubernetes.io/docs/concepts/policy/resource-quotas/

### Exercise

1. Create ubuntu pod in the `example` namespace

## Useful Tooling

Install https://k9scli.io/

## Note on kubectl

The usual syntax is:

```shell
kubectl <action> <resource type> <resource name> ...
```

Actions: get, describe, apply, create, edit, delete, ...

Resource types: node, pod, namespace, service, ...

```shell
kubectl get <resource type> [<resource name>]
kubectl get <resource type> <resource name> -o yaml
kubectl describe <resource type> <resource name>
kubectl edit <resource type> <resource name>
kubectl delete <resource type> <resource name>
```

### Exercises

1. Figure out how to remove pod.
2. Download yaml definition of created namespace and pod (hint: `-o yaml`). Do
   you see any fields added by Kubernetes?
3. Check which pods are running in each node.
4. Try finding logs for Kubernetes control plane components.
5. See what is in `~/.kube`. What is `kubectl --context` for? How to switch it?

