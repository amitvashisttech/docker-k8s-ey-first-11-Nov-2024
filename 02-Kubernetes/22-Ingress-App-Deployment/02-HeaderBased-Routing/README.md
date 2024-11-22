
```
cd 02-HeaderBased-Routing/
cat 02-HeaderBased-ingress.yaml
kubectl apply -f 02-HeaderBased-ingress.yaml
kubectl get ingress
kubectl describe ingress
```





```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes/22-Ingress-App-Deployment/02-HeaderBased-Routing# curl 172.23.0.2:32594/tea -H 'Host: cafe.example.com'
Server address: 10.244.1.16:8080
Server name: tea-596697966f-f526z
Date: 22/Nov/2024:06:36:47 +0000
URI: /tea
Request ID: 35447f42bdd57fafd7b5c756e9120767
```
```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes/22-Ingress-App-Deployment/02-HeaderBased-Routing# curl 172.23.0.2:32594/coffee -H 'Host: cafe.example.com'
Server address: 10.244.2.21:8080
Server name: coffee-56b44d4c55-h7v2c
Date: 22/Nov/2024:06:36:54 +0000
URI: /coffee
Request ID: dd8d739321a195a5608298c90b699a80
```
