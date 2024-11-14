```
506  docker images
  507  docker run -it --name stg-1 mynetwork-ubuntu:v1
  508  ls
  509  docker ps
  510  docker ps -a
  511  docker start stg-1
  512  docker ps -a
  513  docker ps
  514  docker attach stg-1
  515  docker ps
  516  docker ps -a
  517  docker kill $(docker ps -q)
  518  docker rm $(docker ps -q)
  519  docker rm $(docker ps -qa)
  520  ls
  521  docker ps
  522  docker ps -a
  523  docker volume ls
  524  docker volume create myvol1
  525  docker volume ls
  526  docker volume inspect myvol1
  527  ls -ltr /var/lib/docker
  528  ls -ltr /var/lib/docker/volumes/
  529  ls -ltr /var/lib/docker/volumes/myvol1/
  530  ls -ltr /var/lib/docker/volumes/myvol1/_data/
  531  ls
  532  docker run -it --name stg-2 -v myvol1:/myapp mynetwork-ubuntu:v1
  533  ls
  534  docker rm $(docker ps -qa)
  535  docker ps -a
  536  docker volume ls
  537  ls -ltr /var/lib/docker/volumes/myvol1/_data/
  538  ls -ltr /var/lib/docker/volumes/myvol1/_data/EY-DOCKER/
  539  cat /var/lib/docker/volumes/myvol1/_data/EY-DOCKER/info
  540  docker run -it --name stg-3 -v myvol1:/myapp mynetwork-ubuntu:v1
  541  docker ps
  542  docker run -it --name stg-4 -v myvol1:/var/www/html/myapp mynetwork-ubuntu:v1
  543  docker ps
  544  docker run -it --name stg-5 -v myvol1:/var/www/html/myapp:ro mynetwork-ubuntu:v1
  545  ls
  546  docker volume ls
  547  docker kill $(docker ps -q)
  548  docker rm $(docker ps -qa)
  549  docker volume ls
  550  docker run -itd --name stg-6 -v /mywebapp mynetwork-ubuntu:v1
  551  docker ps
  552  docker inspect stg-6
  553  docker volume ls
  554  docker ps
  555  docker attach stg-6
  556  docker kill $(docker ps -q)
  557  docker rm $(docker ps -qa)
  558  docker volume ls
  559  cat /var/lib/docker/volumes/afbabeb52a3c153c34d271f68674b23d5c7460a2a6d32d35c4afdd74f2a35614/_data/info
```
