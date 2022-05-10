# Deplyments and Services

```shell
kubectl apply -f 02-service/deployment/service.yaml
```

```shell
kubectl port-forward svc/myapp-service 8080:80
```

Try going to http://localhost:8080

```shell
kubectl logs <POD-NAME>
```

## Note on kubectl

```shell
kubectl get <resource type> [<resource name>]
kubectl get <resource type> <resource name> -o yaml
kubectl describe <resource type> <resource name>
kubectl edit <resource type> <resource name>
kubectl delete <resource type> <resource name>
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

```shell
kubectl apply -f 02-service/deployment/02-deployment-probes.yaml
```

## Scaling and Resources

```shell
kubectl apply -f 02-service/deployment/03-deployment-replicas-resources.yaml
```

```shell
kubectl get replicaset
```

## Configuration:

```shell
kubectl apply -f 
/deployment/04-deployment-env-vars.yaml
```

You can also use kubectl to directly create secrets
```shell
kubectl create secret generic myapp-secrets --from-literal=var_from_secret=do_not_tell
```
