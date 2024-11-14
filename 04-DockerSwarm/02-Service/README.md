# Create Docker Swarm Service.

### List the Services & Node
```
docker service ls 
docker node ls 
```

### Let's create Nginx Based Service
```
docker service create --replicas 1 --name hello-swarm nginx
```

```
docker service ls 
docker service inspect <<servicename>> 
```

```
root@docker~# docker service ls
ID            NAME         MODE        REPLICAS  IMAGE
543hms09kdwb  hello-swarm  replicated  1/1       nginx:latest
root@docker~#
```

### Service Wide Output
```
root@docker~# docker service ps hello-swarm
ID            NAME           IMAGE         NODE             DESIRED STATE  CURRENT STATE          ERROR  PORTS
85flckugvpaa  hello-swarm.1  nginx:latest  ip-172-31-30-28  Running        Running 2 minutes ago
root@docker~#
```


### Scale Out Opp.
```
docker service scale hello-swarm=5
```
```
root@docker~# docker service ls
ID            NAME         MODE        REPLICAS  IMAGE
543hms09kdwb  hello-swarm  replicated  5/5       nginx:latest
```
```
root@docker~# docker service ps hello-swarm
ID            NAME           IMAGE         NODE              DESIRED STATE  CURRENT STATE           ERROR  PORTS
85flckugvpaa  hello-swarm.1  nginx:latest  ip-172-31-30-28   Running        Running 4 minutes ago
kxjoiy8wy1ol  hello-swarm.2  nginx:latest  ip-172-31-27-32   Running        Running 18 seconds ago
whtbz9auu75k  hello-swarm.3  nginx:latest  ip-172-31-27-32   Running        Running 18 seconds ago
u2ybhfh8ckou  hello-swarm.4  nginx:latest  ip-172-31-30-28   Running        Running 18 seconds ago
3efcxxmjtf7d  hello-swarm.5  nginx:latest  ip-172-31-18-246  Running        Running 18 seconds ago
root@docker~#
```


### Scale In Opps.
```
docker service scale hello-swarm=3
```
```
root@docker~# docker service scale hello-swarm=3
hello-swarm scaled to 3


root@docker~# docker service ps hello-swarm
ID            NAME           IMAGE         NODE              DESIRED STATE  CURRENT STATE               ERROR  PORTS
kxjoiy8wy1ol  hello-swarm.2  nginx:latest  ip-172-31-27-32   Running        Running about a minute ago
u2ybhfh8ckou  hello-swarm.4  nginx:latest  ip-172-31-30-28   Running        Running about a minute ago
3efcxxmjtf7d  hello-swarm.5  nginx:latest  ip-172-31-18-246  Running        Running about a minute ago
root@docker~#
```


### Remove the Service
```
docker service rm hello-swarm
```
