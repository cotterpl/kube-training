# Deplyments and Services

In order to provide our application as externally reachable we need at least 2
components: a Deployment (can also be simple pod) and a Service.

Deployment defines a group of pods as one logical instance.

```shell
kubectl apply -f 02-service/deployment/01-deployment.yaml
```

Service provides entrypoint to a group of pods. As long as service does not
change its IP address does not change.

```shell
kubectl apply -f 02-service/deployment/service.yaml
```

There are various service types:

- NodePort - good for local development
- NodeBalancer - when you are using common cloud providers
- Ingress - dedicated entrypoint with routing rules between external clients and
  Services

More on service types:

- https://platform9.com/blog/understanding-kubernetes-loadbalancer-vs-nodeport-vs-ingress/
- https://kubernetes.io/docs/concepts/services-networking/service/

Even though we have a NodePort service it is still not accessible from outside.
We need to forward port outside:

```shell
kubectl port-forward svc/myapp-service 8080:80
```

Now try going to http://localhost:8080

## Logs

```shell
kubectl logs <POD-NAME>
```

## Networking

In ubuntu pod:

```shell
cat /etc/resolv.conf
```

Try:

```shell
curl <POD-IP>
curl <POD-IP-DASHED>.<NAMESPACE>.pod
```

```shell
curl myapp-service
curl myapp-service.<NAMESPACE>
curl myapp-service.<MAMESPACE>.svc.cluster.local
```

## Is My Application Alive?

Kubernetes can check if our application is ready to serve traffic.

```shell
kubectl apply -f 02-service/deployment/02-deployment-probes.yaml
```

**Liveness probe:** Application is working, kubernetes should NOT attempt to
restart it.

**Readiness probe:** Application is ready to serve traffic.

Application may be alive but not ready for example when the database it relies
on is not reachable.

## Scaling and Resources

```shell
kubectl apply -f 02-service/deployment/03-deployment-replicas-resources.yaml
```

Notice that Deployment also creates ReplicaSet:

```shell
kubectl get replicaset
```

## Configuration:

```shell
kubectl apply -f 02-service/deployment/04-deployment-env-vars.yaml
```

## Appendix

Missing command for configuration:

```shell
kubectl create -f 02-service/deployment/config.yaml
```

You can also use kubectl to directly create secrets

```shell
kubectl create secret generic myapp-secrets \
  --from-literal=var_from_secret=do_not_tell
```
