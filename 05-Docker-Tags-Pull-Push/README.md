```
  315  docker images
  316  docker push mypython:v1
  317  docker login
  318  docker push mypython:v1
  319  docker tag mypython:v1 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v1
  320  docker images
  321  docker tag mypython:v2 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v2
  322  docker images
  323  docker push amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v1
  324  docker push amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v2
  325  docker kill $(docker ps -q)
  326  docker rm  $(docker ps -aq)
  327  docker ps -a
  328  docker images
  329  docker rmi $(docker images -q) --force
  330  docker images
  331  docker logout
  332  docker run -d --name test-1 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v1
  333  docker run -d --name test-1 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v2
  334  docker run -d --name test-2 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v2
  335  docker ps
  336  curl 172.17.0.2
  337  curl 172.17.0.2:5000
  338  curl 172.17.0.3:5000/info
```
