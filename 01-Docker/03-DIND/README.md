```

docker run --privileged --name test-dind -d docker:dind
docker ps
docker exec -it test-dind sh
```

```
docker run -d -P --name nginx-dind nginx 
docker inspect nginx-dind
wget <containerIP>
```
