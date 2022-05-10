# Helm Charts

Install helm:
https://helm.sh/

```shell
kubectl create ns helm-ns
```

```shell
helm install -n helm-ns myapp-helm ./03-helm/myapp --dry-run
```

```shell
helm install --atomic -n helm-ns myapp-helm ./03-helm/myapp
```

```shell
helm list -n helm-ns
```

Use kubectl to review created resources.

```shell
helm uninstall -n helm-ns myapp-helm
```

