# Docker Networking and Custom Images: A Comprehensive Guide

This guide provides a detailed walkthrough on managing Docker networks, creating custom images with network utilities, and working with containers using different network configurations.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Commands Overview](#commands-overview)
4. [Step-by-Step Guide](#step-by-step-guide)
   - [Managing Docker Networks](#managing-docker-networks)
   - [Running Containers with Published Ports](#running-containers-with-published-ports)
   - [Creating a Custom Image with Network Utilities](#creating-a-custom-image-with-network-utilities)
   - [Running Containers with Different Network Configurations](#running-containers-with-different-network-configurations)
   - [Creating and Using Custom Networks](#creating-and-using-custom-networks)
5. [Cleaning Up](#cleaning-up)
6. [Conclusion](#conclusion)

## Introduction

Docker networking is essential for container communication both within the host and across different hosts. This guide covers the essential commands and concepts for managing Docker networks and creating custom images with network utilities.

## Prerequisites

- Docker installed on your system
- Basic knowledge of Docker commands

## Commands Overview

Here's a quick look at some Docker commands related to networking and custom images:

- `docker network ls`: Lists all Docker networks.
- `docker network inspect <network_name>`: Provides detailed information about a specific network.
- `docker run -p <host_port>:<container_port>`: Publishes a container's port to the host.
- `docker commit <container_id> <image_name>`: Creates a new image from a container's changes.
- `docker exec -it <container_name> <command>`: Executes a command in a running container.

## Step-by-Step Guide

### Managing Docker Networks

#### 1. List all Docker networks:
```
   docker network ls
  ```

#### 2. Inspect a specific network:
```
    docker network inspect 7daccc782664
```
### Running Containers with Published Ports
#### 1. Run a container with a specific port published:
  
```
docker run -d --name job2 -p 8080:80 myapache:v5
```
#### 2. Install network tools in a container:

```
apt-get install net-tools -y
```
#### 3. Check open ports on the host:
```
netstat -tulnp
```
#### 4. Test connectivity to a container:
```
    curl 10.4.0.178:8080
```
### Creating a Custom Image with Network Utilities

#### 1. Run an Ubuntu container and install network tools:
```
docker run -it ubuntu
apt-get update
apt-get install net-tools -y
```

#### 2. Exit the container (detach without stopping):

#### Press Ctrl + P, followed by Ctrl + Q

#### 3. Commit the container as a new image:
```
docker commit -m "My Second Image" -p 0563f19dbaf0 mynetwork-ubuntu:v1
```

#### 4. Verify the new image:
```
 docker images
```

### Running Containers with Different Network Configurations

### 1. Run a container with the default network:
```
docker run -itd --name default-nw-1 mynetwork-ubuntu:v1
```
#### 2. Run a container with the host network:

```
docker run -itd --name host-nw-2 --network host mynetwork-ubuntu:v1
```

#### 3. Run a container with no network:
```
docker run -itd --name none-nw-3 --network none mynetwork-ubuntu:v1
```

#### 5. Check network configurations inside containers:
```
    docker exec -it default-nw-1 ifconfig
    docker exec -it host-nw-2 ifconfig
    docker exec -it none-nw-3 ifconfig
```

### Creating and Using Custom Networks
#### 1. Create a custom bridge network:
    ```
    docker network create --driver bridge --subnet 172.28.5.0/24 --gateway 172.28.5.1 mybr0
    ```
#### 2. Verify the custom network:

```
docker network ls
docker network inspect mybr0
```
#### 3. Run containers on the custom network:
```
docker run -itd --name mybr-nw-1 --network mybr0 mynetwork-ubuntu:v1
docker run -itd --name mybr-nw-2 --network mybr0 mynetwork-ubuntu:v1
```
#### 4. Check network configurations inside containers:

```
docker exec -it mybr-nw-1 ifconfig
docker exec -it mybr-nw-2 ifconfig
```

#### 5. Test connectivity between containers:
```
    ping -c2 172.28.5.2
    ping -c2 172.28.5.3
```
### Cleaning Up

#### 1. Stop and remove all running containers:

```
docker kill $(docker ps -q)
docker rm $(docker ps -qa)
```

