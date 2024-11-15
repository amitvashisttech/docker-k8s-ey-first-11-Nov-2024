```
 894  cd 05-Replicas-Cantroller/
  895  ls
  896  kubectl apply -f helloworld-rc.yaml
  897  kubectl get rc
  898  kubectl get pods
  899  kubectl get pods -o wide
  900  kubectl scale --replicas=1 rc helloworld-controller
  901  kubectl get pods -o wide
  902  kubectl scale --replicas=5 rc helloworld-controller
  903  kubectl get pods -o wide
  904  kubectl scale --replicas=1 rc helloworld-controller
  905  kubectl get pods -o wide
  906  kubectl get rc
  907  kubectl delete pod --all
  908  kubectl get pods -o wide
  909  ls
  910  kubectl delete pod --all
  911  kubectl get pods -o wide
  912  kubectl scale --replicas=3 rc helloworld-controller
  913  kubectl get pods -o wide
  914  kubectl delete pod helloworld-controller-cv65t
  915  kubectl get pods -o wide
  916  kubectl get rc
  917  ls
  918  kubectl delete -f helloworld-rc.yaml
  919  kubectl get rc
```
