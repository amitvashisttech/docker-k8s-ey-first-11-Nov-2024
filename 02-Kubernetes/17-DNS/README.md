## Deploy Custom BusyBox Pod for DNS Example.
```
kubectl apply -f 17-DNS/01-busybox-dns.yaml 
kubectl get po 
```




## APP Deployment with Svc
```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl apply -f 07-Service/03-app-svc-deploy.yaml
service/python-webapp-svc created
deployment.apps/python-webapp-deployment created
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes#
```

```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl get svc
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)           AGE
kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP           6d
python-webapp-svc    NodePort    10.96.238.206   <none>        31007:31007/TCP   10s
storage-deployment   NodePort    10.96.196.211   <none>        80:30276/TCP      22h
```
```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl get po
NAME                                        READY   STATUS    RESTARTS   AGE
busybox                                     1/1     Running   0          8m13s
python-webapp-deployment-868d6d9889-hfkpr   1/1     Running   0          12s
python-webapp-deployment-868d6d9889-kv7lq   1/1     Running   0          12s
python-webapp-deployment-868d6d9889-zhlmf   1/1     Running   0          12s
```


## DNS Lookup for the Services
```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl exec -it busybox -- nslookup kubernetes
Server:    10.96.0.10
Address 1: 10.96.0.10 kube-dns.kube-system.svc.cluster.local

Name:      kubernetes
Address 1: 10.96.0.1 kubernetes.default.svc.cluster.local
```

```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl exec -it busybox -- nslookup storage-deployment
Server:    10.96.0.10
Address 1: 10.96.0.10 kube-dns.kube-system.svc.cluster.local

Name:      storage-deployment
Address 1: 10.96.196.211 storage-deployment.default.svc.cluster.local
```

```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl exec -it busybox -- nslookup python-webapp-svc
Server:    10.96.0.10
Address 1: 10.96.0.10 kube-dns.kube-system.svc.cluster.local

Name:      python-webapp-svc
Address 1: 10.96.238.206 python-webapp-svc.default.svc.cluster.local
```


## Let Connect to the App via DNS Name Resolution
```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl exec -it busybox -- wget python-webapp-svc:31007
Connecting to python-webapp-svc:31007 (10.96.238.206:31007)
index.html           100% |*************************************************************************************************************|    31   0:00:00 ETA
```
```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl exec -it busybox -- cat index.html
<h1>Hello From Flask App.!</h1>root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl exec -it busybox -- rm index.html
```

```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl exec -it busybox -- wget python-webapp-svc:31007/info
Connecting to python-webapp-svc:31007 (10.96.238.206:31007)
info                 100% |*************************************************************************************************************|   132   0:00:00 ETA
```
```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl exec -it busybox -- cat info
<h2> Hey Python Web Server</h2><b> Hostname: </b> python-webapp-deployment-868d6d9889-hfkpr<br/><b> IP Address: </b> 10.244.2.4<br/>
```

## Check the POD Deatils 
```
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes# kubectl get po -o wide
NAME                                        READY   STATUS    RESTARTS   AGE     IP           NODE          NOMINATED NODE   READINESS GATES
busybox                                     1/1     Running   0          10m     10.244.2.2   k8s-worker2   <none>           <none>
python-webapp-deployment-868d6d9889-hfkpr   1/1     Running   0          2m46s   10.244.2.4   k8s-worker2   <none>           <none>
python-webapp-deployment-868d6d9889-kv7lq   1/1     Running   0          2m46s   10.244.2.3   k8s-worker    <none>           <none>
python-webapp-deployment-868d6d9889-zhlmf   1/1     Running   0          2m46s   10.244.2.4   k8s-worker    <none>           <none>
root@ubuntugui:~/docker-k8s-ey-first-11-Nov-2024/02-Kubernetes#
```
