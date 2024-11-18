```
 1178  cd 08-HealthCheck/
 1179  ls
 1180  vim 01-helloworld-deploy-hc.yaml
 1181  kubectl apply -f 01-helloworld-deploy-hc.yaml
 1182  kubectl get deploy
 1183  kubectl get po
 1184  kubectl describe pod helloworld-deployment-548d9bfcd5-7sh4j
 1185  kubectl get po
 1186  watch -n .5 kubectl get po
 1187  kubectl edit deploy
 1188  kubectl get po
 1189  kubectl describe pod helloworld-deployment-75ffdbdb4b-pm9mp
 1190  watch -n .5 kubectl get po
 1191  kubectl describe pod helloworld-deployment-75ffdbdb4b-pm9mp
 1192  watch -n .5 kubectl get po
 1193  ls
 1194  vim 02-helloworld-deploy-custom-values.yaml
 1195  ls
 1196  kubectl apply -f 02-helloworld-deploy-custom-values.yaml
 1197  kubectl get po
 1198  kubectl describe po helloworld-2-deployment-b8dcfb87b-8vzk2
 1199  ls
 1200  kubectl get po
 1201  kubectl delete -f 01-helloworld-deploy-hc.yaml
 1202  kubectl delete -f 02-helloworld-deploy-custom-values.yaml
 1203  ls
 1204  cat 02-helloworld-deploy-custom-values.yaml
 1205  vim 03-Pod-prob-exec.yaml
 1206  ls
 1207  kubectl apply -f 03-Pod-prob-exec.yaml
 1208  kubectl get po
 1209  kubectl exec -it liveness-exec -- ls /tmp/
 1210  kubectl get po
 1211  watch -n .5 kubectl get po
 1212  kubectl get po
 1213  kubectl exec -it liveness-exec -- ls /tmp/
 1214  ls
 1215  cat 02-helloworld-deploy-custom-values.yaml
 1216  cat 03-Pod-prob-exec.yaml
 1217  ls
 1218  kubectl get po
 1219  vim 04-Readiness-live-hc.yaml
 1220  kubectl apply -f 04-Readiness-live-hc.yaml
 1221  kubectl get po
 1222  kubectl describe pod helloworld-deployment-6564c6c678-2z9dg
 1223  ls
 1224  cd ..
 1225  ls
 1226  kubectl delete -f 08-HealthCheck/
```
