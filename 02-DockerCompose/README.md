```
 587  mkdir 02-DockerCompose/01-Setup -p
  588  s
  589  ls
  590  cd 02-DockerCompose/
  591  ls
  592  cd 01-Setup/
  593  ls
  594  vim install-compose.sh
  595  chmod +x install-compose.sh
  596  sh install-compose.sh
  597  docker-compose version
  598  cat install-compose.sh
  599  ls
  600  cd ..
  601  ls
  602  mkdir 02-Nginx
  603  cd 02-Nginx/
  604  ls
  605  vim docker-compose.yaml
  606  ls
  607  docker-compose up -d
  608  docker-compose ps
  609  docker ps
  610  curl localhost:8080
  611  docker-compose ps
  612  docker-compose stop
  613  docker-compose ps
  614  docker-compose rm
  615  docker-compose ps
  616  docker ps
  617  ls
  618  cd ..
  619  ls
  620  cp -rf 02-Nginx 03-MyApp
  621  ls
  622  cd 03-MyApp/
  623  ls
  624  docker images
  625  vim docker-compose.yaml
  626  docker-compose up -d
  627  vim docker-compose.yaml
  628  docker-compose up -d
  629  docker ps
  630  docker-compose ps
  631  docker network ls
  632  docker network inspect 4e065c2735bf
  633  ls
  634  docker ps
  635  curl localhost:8080
  636  curl localhost:8081
  637  ls
  638  cd ..
  639  ls
  640  cp -rf 04-Build
  641  cp -rf 02-Nginx  04-Build
  642  ls
  643  cd 04-Build/
  644  ls
  645  cp -rf ../../01-Docker/04-Docker-Custom-Images/apache/v3/*
  646  ls
  647  cp -rf ../../01-Docker/04-Docker-Custom-Images/apache/v3/* .
  648  ls
  649  mv MyDockerfile Dockerfile
  650  ls
  651  cat Dockerfile
  652  ls
  653  vim Dockerfile
  654  ls
  655  vim info.html
  656  ls
  657  cp -rf ../../01-Docker/04-Docker-Custom-Images/apache/v2/info.html .
  658  cat info.html
  659  vim info.html
  660  ls
  661  vim docker-compose.yaml
  662  ls
  663  docker-compose up -d
  664  docker ps
  665  curl localhost:8092
  666  curl localhost:8092/info.html
  667  ls
  668  vim info.html
  669  docker-compose up -d
  670  docker-compose up -d --build
  671  curl localhost:8092/info.html
  672  docker ps
  673  docker-compose up -d --build --help
  674  docker-compose up -d --build --force-recreate
  675  curl localhost:8092/info.html
  676  vim info.html
  677  docker-compose up -d --build --force-recreate
  678  curl localhost:8092/info.html
  679  docker-compose ps
  680  cat docker-compose.yaml
  681  docker ps
  682  ls
  683  cd ..
  684  ls
  685  cp -rf 03-MyApp 05-WebApp
  686  s
  687  ls
  688  cd 05-WebApp/
  689  s
  690  ls
  691  vim docker-compose.yaml
  692  docker-compose up -d
  693  docker-compose ps
  694  dockerls
  695  docker ps
  696  docker network ls
  697  docker inspect 05-webapp_mynet
  698  docker volume ls
  699  docker-compose ps
  700  docker exec -it 05-webapp-python-1 bash
```
