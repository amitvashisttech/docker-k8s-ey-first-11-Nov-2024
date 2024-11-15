### Install KIND K8s 3 Node Cluster 


## Install Kind Utils 
```
sh k8s-install.sh
```

## Create KinD Clutser
```
kind create cluster --config=ingress-cluster.yaml
```

## Check the Cluster Status
```
kubectl cluster-info --context kind-k8s
```


### Check the Node Status
```
kubectl get nodes
```
```
NAME                STATUS   ROLES           AGE     VERSION
k8s-control-plane   Ready    control-plane   2m33s   v1.30.0
k8s-worker          Ready    <none>          2m11s   v1.30.0
k8s-worker2         Ready    <none>          2m12s   v1.30.0
```
