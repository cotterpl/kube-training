# Kubernetes Basics

Contains materials for Kubernetes basics training

Training contents:

- [Introduction](01-intro/README.md)
- [Service](01-intro/README.md)
- [Helm Charts](01-intro/README.md)
- [Auto Scaling](01-intro/README.md)

# Assignment

Setup and configure Kubernetes cluster so that `myapp` endpoints:

- `POST /guests` - saves last guest
- `GET /guests` - returns last guest saved with `POST /guests`

There is no need to modify application code or it's docker image. However you
need to install Redis wihin cluster and configure myapp to connect to it.

Tips:

- Is there a helm chart for redis?
- What configuration does `myapp` need?
- What is redis host address?
- How to get or set redis password?
- Should we check redis connection in readiness probe?