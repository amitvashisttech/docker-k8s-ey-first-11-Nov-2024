Step 1: Start the Docker-in-Docker Containers

To run Docker in Docker, you can use the docker:dind image. Here, we’ll set up multiple containers and use one as the Swarm manager, and others as worker nodes.

### 1. Start the Docker Daemon in a Container , Each container will need to run its own Docker daemon. Use the following command to start a container with Docker-in-Docker:
```
docker run --privileged --name manager -d docker:dind
```

### 2. Start additional containers for Swarm worker nodes:
```
docker run --privileged --name worker1 -d docker:dind
docker run --privileged --name worker2 -d docker:dind
```

### 3. Initialize the Docker Swarm Manager
```
docker exec -it manager sh
ip a
```

```
docker swarm init --advertise-addr <MANAGER_CONTAINER_IP>
```

### 4. Get the Join Token for Workers : "Make a Node of IT" 


### 5. Connect to Each Worker Container
```
docker exec -it worker1 sh
```

### 6. Apply the token
```
docker swarm join --token SWMTKN-1-xyz <MANAGER_CONTAINER_IP>:2377
```

### 7. Now Login to Manager & check the status
```
docker node ls
```

### 8. Deploy Service to Swarm 
```
docker service create --name my-service --replicas 3 nginx
```


