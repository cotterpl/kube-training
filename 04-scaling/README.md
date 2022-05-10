# Auto Scaling #

Kubernetes, together with dedicated metrics gathering tool, can perform
auto-scaling of your application.

## Metrics Server

Auto-scaling needs to have access to metrics so that it can make decisions on
when to scale.

When using known cloud providers metrics should be available out of the box. In
our Kind cluster they are not available. We need to add metrics server.

https://github.com/kubernetes-sigs/metrics-server#readme

```shell
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
helm install \
  -n default \
  metrics-server metrics-server/metrics-server
```

## Service

We need a service with auto-scaling configured. Please notice custom values file
and compare it against helm chart.

```shell
kubectl create namespace hpatest

helm install \
  -n hpatest myapp-helm \
  ./03-helm/myapp \
  --values ./04-scaling/values-myapp.yaml \
  --dry-run
```

Now remove `--dry-run` and install it.

```shell
kubectl -n hpatest get hpa --watch
```

## Generate Load

```shell
kubectl run -n hpatest -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.03; do wget -q -O- http://myapp-service/hpatest; done"
```

## Appendix

Corrected command for Metrics Server installation:

```shell
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
helm install \
  -n default \
  metrics-server metrics-server/metrics-server \
  --values ./04-scaling/values-metrics-server.yaml
```