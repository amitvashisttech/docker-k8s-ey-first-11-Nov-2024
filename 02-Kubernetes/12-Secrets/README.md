```
1454  mkdir 12-Secrets
 1455  ls
 1456  cd 12-Secrets/
 1457  ls
 1458  kubectl get secrets
 1459  kubectl create secrets test-secrets --help
 1460  ls
 1461  kubectl create secret test-secrets --help
 1462  kubectl create secret generic test-secrets --help
 1463  kubectl create secret generic test-secrets --from-literal=Demo=EY  --from-literal=Location=Noida --dry-run
 1464  kubectl create secret generic test-secrets --from-literal=Demo=EY  --from-literal=Location=Noida --dry-run -o yaml
 1465  kubectl create secret generic test-secrets --from-literal=Demo=EY  --from-literal=Location=Noida
 1466  kubectl get secrets
 1467  s
 1468  ls
 1469  vim 1-hello-secrets.yaml
 1470  ls
 1471  oc apply -f 1-hello-secrets.yaml
 1472  kubectl apply -f 1-hello-secrets.yaml
 1473  kubectl get secrets
 1474  kubectl describe secrets my-db-secrets
 1475  kubectl edit secrets my-db-secrets
 1476  ls
 1477  vim 2-helloworld-secret-vol.yaml
 1478  kubectl get secrets
 1479  cat 2-helloworld-secret-vol.yaml
 1480  kubectl apply -f 2-helloworld-secret-vol.yaml
 1481  kubectl get po
 1482  kubectl exec -it helloworld-deployment-6bd478db8b-4blxj
 1483  kubectl exec -it helloworld-deployment-6bd478db8b-4blxj  -- bash
 1484  kubectl exec -it helloworld-deployment-6bd478db8b-4blxj  -- sh
```
