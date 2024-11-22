# Install Helm

## Download the latest version of helm : as of today: 3.16.3
```
wget https://get.helm.sh/helm-v3.16.3-linux-amd64.tar.gz

tar -zxvf helm-v3.16.3-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin/helm
```

## Initialize Helm
```
kubectl create -f helm-rbac.yaml
```

## Install Nginx Web App.
```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add stable https://charts.helm.sh/stable
helm search repo nginx
```
```
NAME                                    CHART VERSION   APP VERSION     DESCRIPTION
bitnami/nginx                           18.2.5          1.27.2          NGINX Open Source is a web server that can be a...
bitnami/nginx-ingress-controller        11.5.4          1.11.3          NGINX Ingress Controller is an Ingress controll...
bitnami/nginx-intel                     2.1.15          0.4.9           DEPRECATED NGINX Open Source for Intel is a lig...
stable/nginx-ingress                    1.41.3          v0.34.1         DEPRECATED! An nginx Ingress controller that us...
stable/nginx-ldapauth-proxy             0.1.6           1.13.5          DEPRECATED - nginx proxy with ldapauth
stable/nginx-lego                       0.3.1                           Chart for nginx-ingress-controller and kube-lego
stable/gcloud-endpoints                 0.1.2           1               DEPRECATED Develop, deploy, protect and monitor...
```

```
helm install first-helm-deploy-nginx bitnami/nginx
```
```
NAME: first-helm-deploy-nginx
LAST DEPLOYED: Fri Nov 22 03:38:22 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: nginx
CHART VERSION: 18.2.5
APP VERSION: 1.27.2

** Please be patient while the chart is being deployed **
NGINX can be accessed through the following DNS name from within your cluster:

    first-helm-deploy-nginx.default.svc.cluster.local (port 80)

To access NGINX from outside the cluster, follow the steps below:

1. Get the NGINX URL by running these commands:

  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        Watch the status with: 'kubectl get svc --namespace default -w first-helm-deploy-nginx'

    export SERVICE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].port}" services first-helm-deploy-nginx)
    export SERVICE_IP=$(kubectl get svc --namespace default first-helm-deploy-nginx -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
    echo "http://${SERVICE_IP}:${SERVICE_PORT}"

```

```
helm list
helm history first-nginx
helm delete first-nginx
```

Have Fun.!!

