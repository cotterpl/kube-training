# Kubernetes Basics

Contains materials for Kubernetes basics training

Training contents:

- [Introduction](01-intro/README.md)
- [Service](02-service/README.md)
- [Helm Charts](03-helm/README.md)
- [Auto Scaling](04-scaling/README.md)

# Assignment

Setup and configure Kubernetes cluster so that `myapp` endpoints:

- `POST /guests` - saves last guest
- `GET /guests` - returns last guest saved with `POST /guests`

There is no need to modify application code or it's docker image. However you
need to install Redis wihin cluster and configure myapp to connect to it.

Hints:

- What configuration does `myapp` need?
- Is there a helm chart for Redis?
- What is Redis host address?
- How to get or set Redis password?
- Should we check Redis connection in readiness probe?

See only if you feel lost: [Solution description](assignment_solution.md)