```
  151  cd docker-k8s-ey-first-11-Nov-2024/
  152  ls
  153  mkdir 04-Docker-Custom-Images
  154  ls
  155  cd 04-Docker-Custom-Images/
  156  ls
  157  mkdir apache
  158  ls
  159  cd apache/
  160  ls
  161  mkdir v1
  162  ls
  163  cd v1/
  164  ls
  165  vim Dockerfile
  166  ls
  167  docker build -t myapache:v1 .
  168  docker images
  169  docker run -d --name test-myapache-1 myapache:v1
  170  docker ps
  171  cat Dockerfile
  172  docker exec -it a669f9aba134 ps
  173  docker exec -it a669f9aba134 ps -a
  174  docker exec -it a669f9aba134 ps -ef
  175  docker exec -it a669f9aba134 bash
  176  docker ps
  177  l
  178  docker inspect test-myapache-1
  179  curl 172.17.0.2
```
