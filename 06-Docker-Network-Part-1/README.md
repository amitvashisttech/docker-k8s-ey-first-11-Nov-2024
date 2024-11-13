```
360  docker ps -a
  361  ip a
  362  docker network ls
  363  docker network inspect 1e772b6de7f2
  364  ls
  365  docker ps
  366  docker ps -a
  367  docker start test-1
  368  docker ps
  369  docker inspect test-1
  370  ls
  371  ip a
  372  docker ps
  373  docker stop test-1
  374  docker kill test-1
  375  docker ps
  376  ip a
  377  docker start test-1
  378  ip a
  379  docker start test-2
  380  ip a
  381  cd /var/run/docker/netns/
  382  ls
  383  docker kill test-2
  384  ls
  385  ip a
  386  s
  387  ls
  388  docker ps
  389  curl 172.17.0.2:5000
  390  curl 10.4.3.153:5000
  391  ld
  392  docker ps
  393  cd
  394  docker run -d --name test-nw-1 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v1
  395  docker ps
  396  docker kill test-1
  397  docker ps
  398  curl 10.4.3.153:5000
  399  docker run -d -p 8080:5000 --name test-nw-2 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v1
  400  docker ps
  401  apt-get install net-tools -y
  402  netstat -tulnp
  403  systemctl status docker
  404  curl 10.4.3.153:5000
  405  curl 10.4.3.153:8080
  406  docker ps
  407  docker run -d -p 8080:5000 --name test-nw-3 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v1
  408  netstat -tulnp
  409  docker run -d -P --name test-nw-4 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v1
  410  docker ps
  411  curl 10.4.3.153:32768
  412  docker run -d -P --name test-nw-5 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v1
  413  docker run -d -P --name test-nw-6 amitvashist7/docker-k8s-ey-first-11-nov-2024-python:v1
  414  docker ps
  415  docker run -itd -P --name test-nw-7 ubuntu
  416  docker ps
  417  docker images
  418  docker inspect 59ab366372d5 | grep -i expose
  419  docker inspect 0f36ed73f6ea | grep -i expose
  420  docker inspect 0f36ed73f6ea | grep -iA5 expose
  421  docker run -itd -p 8081:80 --name test-nw-8 ubuntu
  422  docker ps
  423  curl 10.4.3.153:8081
  424  docker kill test-nw-6
  425  docker ps
  426  docker start test-nw-6
```
