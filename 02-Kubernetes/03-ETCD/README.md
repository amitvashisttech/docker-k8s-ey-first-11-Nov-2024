# K8s Datastore - ETCD

## Check the status of ETCD
```
kubectl get pods -n kube-system | grep -i  etcd
```

## Let explore ETCD POD
```
kubectl exec -it <etcd-pod-name> -n kube-system   -- /bin/sh
```

## Export the below Env for Smooth ETCD Interations:
```
export ETCDCTL_API=3
export ETCDCTL_CACERT=/etc/kubernetes/pki/etcd/ca.crt
export ETCDCTL_CERT=/etc/kubernetes/pki/etcd/server.crt
export ETCDCTL_KEY=/etc/kubernetes/pki/etcd/server.key
```



## Check the ETCD Status
```  
etcdctl endpoint status  --write-out=table
```

```
+----------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|    ENDPOINT    |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+----------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
| 127.0.0.1:2379 | c22785f83a00f446 |   3.4.3 |  5.0 MB |      true |      false |         2 |      37052 |              37052 |        |
+----------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+

```

## Checking the ETCD Prefix
```
etcdctl  get / --prefix --keys-only
```
