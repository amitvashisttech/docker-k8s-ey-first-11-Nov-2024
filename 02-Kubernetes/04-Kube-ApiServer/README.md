## KubeAPI Server Intro

```
kubectl cluster-info
kubectl api-versions
kubectl api-resources
```

```
kubectl proxy --address='<YourNodeIPAddress>' --port=8001 --accept-hosts='.' --accept-paths='.' &
```


```
curl http://<YourNodeIPAddress>:8001
curl http://<YourNodeIPAddress>:8001/apis
curl http://<YourNodeIPAddress>:8001/api/v1
curl http://<YourNodeIPAddress>:8001/api/v1/pods
```
