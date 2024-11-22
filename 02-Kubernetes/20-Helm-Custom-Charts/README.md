```
2149  mkdir 20-Helm-Custom-Charts
 2150  ls
 2151  cd 20-Helm-Custom-Charts/
 2152  ls
 2153  helm create my-tiny-webapp
 2154  ls
 2155  tree my-tiny-webapp/
 2156  apt install tree -y
 2157  tree my-tiny-webapp/
 2158  ls
 2159  cd my-tiny-webapp/
 2160  ls
 2161  cat templates/deployment.yaml
 2162  ls
 2163  vim values.yaml
 2164  ls
 2165  cd ..
 2166  ls
 2167  helm install my-web my-tiny-webapp --dry-run
 2168  helm install my-web my-tiny-webapp
 2169  helm list
 2170  kubectl get deploy
 2171  kubectl get po
 2172  kubectl get svc
 2173  ls
 2174  kubectl get deploy
 2175  kubectl describe deploy
 2176  ls
 2177  kubectl get po
 2178  kubectl get po -o yaml
 2179  ls
 2180  mkdir v1
 2181  mv my-tiny-webapp v1/
 2182  ls
 2183  cp -rf v1 v2
 2184  ls
 2185  cd v2/
 2186  ls
 2187  cd my-tiny-webapp/
 2188  ls
 2189  vim Chart.yaml
 2190  ls
 2191  vim values.yaml
 2192  ls
 2193  cd ..
 2194  ls
 2195  helm install my-web my-tiny-webapp --dry-run
 2196  helm list
 2197  helm upgrade my-web my-tiny-webapp/
 2198  helm list
 2199  kubectl get deploy
 2200  kubectl get po
 2201  kubectl get svc
 2202  curl 172.23.0.2:30118
 2203  kubectl get po
 2204  kubectl describe po my-web-my-tiny-webapp-76669d4fc4-9p8nd
 2205  ls
 2206  kubectl get svc
 2207  curl 172.23.0.2:30118
 2208  kubectl get po
 2209  kubectl describe po my-web-my-tiny-webapp-76669d4fc4-9p8nd
 2210  ls
 2211  cd ..
 2212  ls
 2213  cp -rf v2 v3
 2214  ls
 2215  cd v3/
 2216  ls
 2217  cd my-tiny-webapp/
 2218  ls
 2219  vim values.yaml
 2220  ls
 2221  vim Chart.yaml
 2222  ls
 2223  cd ..
 2224  ls
 2225  helm upgrade my-web my-tiny-webapp
 2226  helm list
 2227  helm history my-web
 2228  kubectl get po
 2229  kubectl get svc
 2230  curl 172.23.0.2:30118
 2231  kubectl delete svc coffee-svc helloworld-db-service database-service tea-svc
 2232  kubectl get svc
 2233  ls
 2234  helm list
 2235  helm history my-web
 2236  helm rollback my-web
 2237  helm history my-web
 2238  kubectl get po
 2239  helm rollback my-web
 2240  helm history my-web
 2241  kubectl get po
 2242  helm rollback my-web 1
 2243  helm history my-web
```
