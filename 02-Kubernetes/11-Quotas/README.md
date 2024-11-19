# Kubernetes Resource Quotas Management Training & Development

This section covers the steps to manage Resource Quotas in Kubernetes, including creating namespaces, applying resource quotas, and managing deployments within those quotas.

## Commands Overview

### 1. Navigate to the Resource Quotas Directory

Change to the directory where the resource quotas and related YAML files are stored:

```bash
cd 11-Quotas/
```

### 2. Manage Resource Quota Configurations
#### a. List and View Files

List the files in the directory and view the contents of the defaults.yml file:

```bash

ls
cat defaults.yml
```

#### b. Create a New Namespace

Create a new namespace called myspace:

```bash
kubectl create ns myspace
```

### 3. Apply and Manage Deployments Without Quotas
#### a. Apply a Deployment Without Quotas

Apply a deployment in the myspace namespace without any resource quotas:

```bash
kubectl apply -f helloworld-no-quotas.yml
```

#### b. Copy and Modify YAML Files

Copy and rename deployment files:

```bash
cp -rf ../05-Deployment/01-Helloworld.yaml .
mv 01-Helloworld.yaml 01-Helloworld-with-no-quota.yaml
```
Apply the modified deployment file in the myspace namespace:

```bash
kubectl apply -f 01-Helloworld-with-no-quota.yaml -n myspace
```
#### c. Verify Deployment

Check the pods in the myspace namespace:

```bash
kubectl get pods -n myspace
```
Delete the deployment without quotas:

```bash
kubectl delete -f 01-Helloworld-with-no-quota.yaml -n myspace
```
### 4. Apply and Manage Resource Quotas
#### a. Apply Default Resource Quotas

Apply the defaults.yml file to set resource quotas in the myspace namespace:

```bash
kubectl apply -f defaults.yml
kubectl get limitrange -n myspace
```
#### b. Apply a Deployment with Resource Quotas

Copy, modify, and apply a deployment file with resource quotas:

```bash
cp -rf 01-Helloworld-with-no-quota.yaml 03-Helloworld-with-quota.yaml
vim 03-Helloworld-with-quota.yaml
kubectl apply -f 03-Helloworld-with-quota.yaml -n myspace
```
#### c. Verify the Deployment with Quotas

Check the status of the deployment and its associated pods:

```bash
kubectl get pods -n myspace
kubectl describe pods helloworld-deploymenti-with-quota-7478bb4645-7bjvx -n myspace
```
Delete the deployment with resource quotas:

```bash
kubectl delete -f 03-Helloworld-with-quota.yaml -n myspace
```
### 5. Apply and Manage Specific Resource Quotas
#### a. Modify and Apply Resource Quotas

Modify the 04-Resourcequota.yml file as needed and apply it:

```bash
vim 04-Resourcequota.yml
kubectl apply -f 04-Resourcequota.yml
```
#### b. Verify Resource Quotas

Check the applied resource quotas in the myspace namespace:

```bash
kubectl get resourcequota -n myspace
```
### 6. Scale and Manage Deployments with Resource Quotas
#### a. Scale the Deployment

Scale the helloworld-deploymenti-with-quota deployment to 5 replicas:

```bash
kubectl scale --replicas=5 deploy helloworld-deploymenti-with-quota -n myspace
```
#### b. Verify Scaling

Check the status of the pods and the deployment:

```bash
kubectl get pods -n myspace
kubectl get deploy -n myspace
kubectl describe deploy helloworld-deploymenti-with-quota -n myspace
```

7. Cleanup and Resource Management
#### a. Delete Pods and Deployments

Delete specific pods and all pods in the myspace namespace:

```bash
kubectl delete pod helloworld-deploymenti-with-quota-569dc6fc8-ll6lf helloworld-deploymenti-with-quota-569dc6fc8-xzvv4 -n myspace
kubectl delete pod --all -n myspace --grace-period=0 --force
```

#### b. Final Verification

Check the final state of the pods and resource quotas:

```bash
kubectl get pods -n myspace
kubectl get resourcequota -n myspace
```
