
```
cd 01-PathBased-Routing/

kubectl apply -f 01-cafe.yaml
kubectl get deploy
kubectl get po
kubectl get svc


kubectl apply -f 02-PathBased-Ingress.yaml
kubectl get ingress
kubectl describe ingress
kubectl get svc
kubectl get po -o wide
```





```
root@ubuntugui:~/# curl 172.23.0.2:32594/tea 
Server address: 10.244.1.16:8080
Server name: tea-596697966f-f526z
Date: 22/Nov/2024:06:36:47 +0000
URI: /tea
Request ID: 35447f42bdd57fafd7b5c756e9120767
```
```
root@ubuntugui:~/# curl 172.23.0.2:32594/coffee
Server address: 10.244.2.21:8080
Server name: coffee-56b44d4c55-h7v2c
Date: 22/Nov/2024:06:36:54 +0000
URI: /coffee
Request ID: dd8d739321a195a5608298c90b699a80
```
