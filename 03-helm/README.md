# Helm Charts

Relying solely on configuration files can be cumbersome. Imagine you want to
remove all application components created previously. Which ones were customized
to your needs? Which things should you remove?

Helm as package manager for Kubernetes solves this problem as it allows for
encapsulation of all application Kubernetes manifests while allowing for
flexible customizaation to your needs.

## Install helm:

https://helm.sh/

## Deploy as Helm Package

```shell
kubectl create ns helm-ns
```

Helm chart for myapp is in `myapp/chart`

```shell
helm install -n helm-ns myapp-helm ./myapp/chart --dry-run
```

```shell
helm install --atomic -n helm-ns myapp-helm ./myapp/chart
```

```shell
helm list -n helm-ns
```

Use kubectl to review created resources.

```shell
helm uninstall -n helm-ns myapp-helm
```

## Exercises

1. Try providing custom value for `varFromPodDefinition` when installing package
   using helm
2. Make number of pod replicas configurable.
