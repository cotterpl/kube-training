# Jobs and CronJobs

Kubernetes allows you to run ad-hoc one time tasks and reoccuring tasks.

## Job

Start container, run it's code, shut it down.

```shell
kubectl create -f 05-jobs/job.yaml
```

### Exercise

1. Try creating the job once more

## Generating unique names

Job names must be unique. We can ask kubernetes to generate unique names for us.

```shell
kubectl create -f 05-jobs/job-generate-name.yaml
```

## Job cleaning

By default jobs stay in system forever. Large amount of old jobs may degrade
system performance.

```shell
kubectl create -f 05-jobs/job-ttl.yaml
```

## CronJob

You can run jobs on a fixed schedule

```shell
kubectl create -f 05-jobs/cronjob.yaml
```

### Exercise

1. What kinds of objects are created by CronJob?
2. Check yaml definition of created CronJob. Do you see any parameters related
   to old jobs cleaning?
3. Change cronjob so that it is run once a day.
4. Add database migrations to myapp helm chart. Does helm work with
   `generateName`?

## Further reading

- https://kubernetes.io/docs/concepts/workloads/controllers/job/
- https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/

.

.

.

.

.

.

.

.

.

.

.

## Appendix

By default CronJob keeps last 3 runs. You can change this behaviour with
parameters:

- successfulJobsHistoryLimit
- failedJobsHistoryLimit

You can use version or revision number instead of `generateName` in helm:

```yaml
name: my-job-{{Release.Revision}}
```
