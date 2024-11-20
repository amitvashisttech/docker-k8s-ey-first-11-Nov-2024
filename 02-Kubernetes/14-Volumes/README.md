``` 
 1548  cd 14-Volumes/
 1549  ls
 1550  kubectl get sc
 1551  vim 01-PVC-Claim.yaml
 1552  ls
 1553  kubectl get pv
 1554  kubectl get pvc
 1555  kubectl get sc
 1556  kubectl apply -f 01-PVC-Claim.yaml
 1557  kubectl get pvc
 1558  kubectl describe pvc test-claim
 1559  kubectl get pvc
 1560  ls
 1561  vim 02-App-Deployment.yaml
 1562  ls
 1563  kubectl apply -f 02-App-Deployment.yaml
 1564  ls
 1565  kubectl get pvc
 1566  kubectl get po
 1567  kubectl delete deploy helloworld-deployment
 1568  kubectl get po
 1569  kubectl describe po storage-deployment-645fc5fcb9-g29jg
 1570  ls
 1571  kubectl get pv
 1572  kubectl get pvc
 1573  kubectl describe pvc test-claim
 1574  ls
 1575  kubectl delete -f 01-PVC-Claim.yaml
 1576  ls
 1577  vim 01-PVC-Claim.yaml
 1578  ls
 1579  kubectl apply -f 01-PVC-Claim.yaml
 1580  kubectl get pvc
 1581  kubectl delete -f 02-App-Deployment.yaml
 1582  kubectl get pvc
 1583  kubectl get pv
 1584  ls
 1585  kubectl apply -f 02-App-Deployment.yaml
 1586  kubectl get po
 1587  kubectl exec -it storage-deployment-645fc5fcb9-vmfxv -- sh
 1588  kubectl exec -it storage-deployment-645fc5fcb9-vmfxv -- bash
 1589  ls
 1590  kubectl get deploy
 1591  kubectl expose deploy storage-deployment --type=NodePort --dry-run -o yaml
 1592  kubectl expose deploy storage-deployment --type=NodePort --dry-run -o yaml > 03-App-Service.yaml
 1593  ls
 1594  kubectl apply -f 03-App-Service.yaml
 1595  kubectl get svc
 1596  curl 172.23.0.2:30276
 1597  curl 172.23.0.2:30276/amit/
 1598  ls
 1599  kubectl get po
 1600  kubectl get po  -o wide
 1601  kubectl delete pod --all
 1602  kubectl get po  -o wide
 1603  curl 172.23.0.2:30276/amit/
 1604  kubectl delete pod --all
 1605  curl 172.23.0.2:30276/amit/
 1606  kubectl get po  -o wide
```
