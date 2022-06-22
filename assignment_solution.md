# Solution for Assignment

See `get_db()` in application `main.py` for necessary environment values. We
need to provide REDIS_HOST and REDIS_PASSWORD

For Redis helm chart
see: https://github.com/bitnami/charts/tree/master/bitnami/redis

```shell
kubectl create ns redis-ns

helm repo add bitnami https://charts.bitnami.com/bitnami
helm install -n redis-ns redis bitnami/redis
```

```shell
# check redis service name, if redis is in the same namespace as myapp we can use Kubernetes DNS to resolve this name as domain to IP
kubectl get service
```

```shell
# to obtain password for redis
kubectl get secret --namespace redis-ns redis -o jsonpath="{.data.redis-password}" | base64 --decode
```

```yaml
# add to values.yaml
db:
  useRedis: true
  redisHost: 'redis-master'
  redisPassword: '<PASSWORD>'
```

```
# add to secrets in config.yaml
redis_password: {{.Values.db.redisPassword | b64enc}}
```

```
# add to env in deployment.yaml
{{- if .Values.db.useRedis}}
- name: REDIS_HOST
  value: {{.Values.db.redisHost | quote}}
- name: REDIS_PASSWORD
  valueFrom:
    secretKeyRef:
      name: {{.Values.config.secretKeyRef}}
      key: redis_password
{{- end}}
```

```shell
helm install -n redis-ns myapp-helm ./myapp/chart
```

Use `kubectl get`, `kubectl describe` to see if service is running.

## Check your solution

Start **port forwarding** for your service. Then try:

```shell
curl 'http://localhost:8080/ready?connections_check=1'
```

should output:

```json
{
  "message": "I am ready and connected"
}
```

```shell
curl -X POST 'http://localhost:8080/guests?guest=Greg'
```

should output:

```json
{
  "status": "ok"
}
```

```shell
curl 'http://localhost:8080/guests'
```

should output:

```json
{
  "guest": "Greg"
}
```