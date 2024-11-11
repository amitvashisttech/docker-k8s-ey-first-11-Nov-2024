```
  622  docker version
  623  systemctl status docker
  624  docker images
  625  docker run hello-world
  626  docker container ls
  627  docker container ls -a
  628  docker run --name test-av-1 hello-world
  629  docker container ls
  630  docker container ls -a
  631  docker run --name test-av-1 hello-world
  632  docker run --name test-av-2 hello-world
  633  docker run -d  --name test-av-3 hello-world
  634  docker container ls -a
  635  docker run -it --name test-ubuntu-1 ubuntu bash
  636  cat /etc/os-release
  637  docker run -it --name test-ubuntu-1 ubuntu bash
  638  docker run -it --name test-ubuntu-2 ubuntu:18.04 bash
  639  docker run -it --name test-ubuntu-3 ubuntu:18.04 bash
  640  docker ps
  641  docker ps -a
  642  docker start test-ubuntu-1
  643  docker ps -a
  644  docker attach 6d65981b8444
       docker logs -f <container-id / name >
       docker exec -it <container-id / name > ps -ef 

## Clean Up

  664  docker ps -a
  665  docker kill  cbdf8ce17d77
  666  docker ps -a
  667  docker rm test-ubuntu-3
  668  docker ps -a
  669  docker ps -a
  670  docker ps -aq
  671  docker rm $(docker ps -aq)
  672  docker ps -a
  673  docker images
  674  docker rmi 9c7a54a9a43c
  675  docker run -d ubuntu
  676  docker ps
  677  docker ps -a
  678  docker rmi 1f6ddc1b2547
  679  docker rm $(docker ps -aq)
  680  docker rmi 1f6ddc1b2547
  681  docker images

## Format Command
45  docker inspect $(docker ps -l) 
   46  docker ps -l
   47  docker ps -l -q 
   48  docker inspect $(docker ps -lq) 
   49  docker ps 
   50  docker ps -q
   51  docker inspect $(docker ps -q)
   52  docker inspect $(docker ps -q) | wc -l 
   53  docker ps 
   54  docker run -itd ubuntu top 
   55  docker ps 
   56  docker inspect --format '{{.Name}} {{.State.Running}} {{.NetworkSettings.IPAddress}}' $(docker ps -q)
   57  docker inspect --format '{{.Name}} - {{.State.Running}} - {{.NetworkSettings.IPAddress}}' $(docker ps -q)
   58  docker inspect --format '{{.Name}} - {{.State.Running}} - {{.NetworkSettings.IPAddress}}' $(docker ps -qa)

```
