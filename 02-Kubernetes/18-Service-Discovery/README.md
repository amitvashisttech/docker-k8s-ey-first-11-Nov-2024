```
 81  cd 09-Service-Discovery/
   82  ls
   83  cat 00-BusyBox.yaml
   84  kubectl  delete ../08-DNS/
   85  kubectl  delete -f ../08-DNS/
   86  cat 00-BusyBox.yaml
   87  ls
   88  cat 01-Secrets.yaml
   89  s
   90  ls
   91  cat 02-Database.yaml
   92  kubectl apply -f 00-BusyBox.yaml
   93  kubectl apply -f 01-Secrets.yaml
   94  kubectl apply -f 02-Database.yaml
   95  kubectl  get pods
   96  kubectl  delete -f ../07-Service/03-app-svc-deployment.yaml
   97  kubectl  get pods
   98  ls
   99  cat 03-Database-service.yml
  100  kubectl apply -f 04-Helloworld-app-deployment.yml
  101  kubectl  get pod
  102  kubectl delete -f 04-Helloworld-app-deployment.yml
  103  ls
  104  kubectl  apply -f 03-Database-service.yml
  105  kubectl  get pods
  106  kubectl  get svc
  107  vim 04-Helloworld-app-deployment.yml
  108  kubectl  apply -f 04-Helloworld-app-deployment.yml
  109  kubectl  get pods
  110  ls
  111  cat 05-Helloworld-app-svc.yml
  112  kubectl  apply -f 05-Helloworld-app-svc.yml
  113  kubectl  get pods
  114  kubectl  get svc
  115  kubectl  get pods
  116  kubectl  get svc



  198  kubectl  exec -it database -- mysql -u root -p
       > show databases;
       > use helloworld
       > show tables; 
       > select * from visits; 
       > exit
  199  kubectl  get pods
  200  kubectl  get svc
  201  kubectl  exec -it busybox -- nslookup database-service
  202  kubectl  exec -it busybox -- nslookup helloworld-db-service
  203  kubectl  exec -it busybox -- wget helloworld-db-service:3000
  204  kubectl  exec -it busybox -- cat index.html

```
