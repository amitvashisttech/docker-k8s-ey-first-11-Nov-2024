# Kubernetes RBAC 

## Create a Pod Reader Role
```
kubectl create role pod-reader --verb=get,list,watch --resource=pods --dry-run -o yaml > 14-RBAC/pod-reader-role.yaml
cat 14-RBAC/pod-reader-role.yaml 
kubectl create -f 14-RBAC/pod-reader-role.yaml
```

## Create a POD Reader RoleBinding 
```
kubectl create rolebinding --help
kubectl create rolebinding read-pod-binding --role=pod-reader --user=amit --dry-run -o yaml > 14-RBAC/read-pod-binding.yaml
kubectl create -f 14-RBAC/read-pod-binding.yaml
kubectl auth can-i get pods --user=amit 
```

## Check the Roles & Context with role Permissions:
```
kubectl get role
kubectl get rolebinding 

kubectl config get-contexts
kubectl config use-context amit@kubernetes
kubectl config get-contexts

kubectl get pods 
kubectl get pods -n myspace
kubectl delete pods  helloworld-deployment-6dc57c75b4-8nlmw -n myspace
kubectl delete deploy  helloworld-deployment -n myspace
```


# Create a ClutserRole Binding with Cluster Admin role for normal user: amit


## View Cluster & Binding via kubernetes-admin context
```
kubectl config get-contexts
kubectl config use-context kubernetes-admin@kubernetes
kubectl config get-contexts
kubectl get pods -n kube-system

kubectl get clusterrole
kubectl describe clusterrole cluster-admin
kubectl get clusterrolebinding
kubectl describe clusterrolebinding cluster-admin
```

## Create a Clusterole binding with existing cluster admin role
```
kubectl create clusterrolebinding admin-user-amit --clusterrole=cluster-admin --user=amit  --dry-run 
kubectl create clusterrolebinding admin-user-amit --clusterrole=cluster-admin --user=amit  --dry-run -o yaml > amit-cluster-rolebinding.yaml
cat amit-cluster-rolebinding.yaml 

kubectl create -f amit-cluster-rolebinding.yaml
kubectl get clusterrolebinding
kubectl describe clusterrolebinding admin-user-amit
```

## Change the conetext & validate the role permissions
```
kubectl config get-contexts
kubectl config use-context amit@kubernetes
kubectl get pods 
kubectl get pods --all-namespaces
   
```



## Dry Auth - Check
```
kubectl auth can-i get pods
kubectl auth can-i get pods --user=amit

```
