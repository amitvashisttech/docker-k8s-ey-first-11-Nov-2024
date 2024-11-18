# Kubernetes Service Management Training & Development

This section covers the steps to create, manage, and expose Kubernetes Services, along with interacting with deployments and pods.

## Commands Overview

### 1. Navigate to the Service Directory

Change to the directory where the service configuration files are stored:

```bash
cd 07-Service/
```

### 2. Manage Service Configuration
#### a. View and Edit the Service YAML File

List the files in the directory and view the service configuration:

```bash
cat helloworld.yaml
```
Edit the helloworld.yaml file as needed:

```bash
vim helloworld.yaml
```
#### b. Apply the Service Configuration

Apply the configuration to create the service:

```bash
kubectl apply -f helloworld.yaml
```
### 3. Get Deployment and Service Status
#### a. Check Deployment Status

Retrieve the current status of the deployment:

```bash
kubectl get deploy
```
#### b. Check Service Status

List the services in the namespace:

```bash
kubectl get svc
```

### 4. Manage and Expose Services
#### a. Delete an Existing Service

Delete the helloworld-deployment service:

```bash
kubectl delete svc helloworld-deployment
```
#### b. Re-Expose the Deployment as a Service

Expose the helloworld-deployment as a service again:

```bash
kubectl expose deploy helloworld-deployment
```
#### c. Access the Service

Get the service details and access it via its ClusterIP:

```bash
kubectl get svc
curl <ClusterIP>
```
#### Example: curl 10.107.52.235

### 5. Edit and Describe Services
#### a. Edit the Service Configuration

Edit the service configuration using kubectl edit:

```bash
kubectl edit svc helloworld-deployment
```
#### b. Describe the Service

Get detailed information about the helloworld-deployment service:

```bash
kubectl describe svc helloworld-deployment
```
### 6. View Pods with Labels

List all pods with additional information and labels:

```bash
kubectl get pods -o wide --show-labels
kubectl get pods --show-labels
```

### 7. Reapply Service Configuration
#### a. Create a New Service Configuration

Edit and apply a new service configuration file:

```bash
vim helloworld-svc.yaml
kubectl apply -f helloworld-svc.yaml
```
#### b. Verify the Service

Check the service status:

```bash
kubectl get svc
kubectl describe svc helloworld-service
```
### 8. Work with Combined Deployments and Services
#### a. Apply a Combined Deployment and Service Configuration

View and apply a combined deployment and service configuration:

```bash
cat app-svc-deployment.yaml
kubectl apply -f app-svc-deployment.yaml
```
#### b. Verify the Combined Resources

Check the status of the deployment, service, and pods:

```bash
kubectl get deploy,svc,pods
kubectl get pods
```
#### c. Describe the Service

Get detailed information about the python-webapp-svc service:

```bash
kubectl describe svc python-webapp-svc
```
#### d. View Pod Details

List the pods with additional information:

```bash
kubectl get pods -o wide
```
### 9. Interact with Pods
#### a. Execute Commands Inside a Pod

Run commands inside a specific pod:

```bash
kubectl exec -it python-webapp-deployment-54b95bd8d-xgsdm -- sh
kubectl exec -it python-webapp-deployment-54b95bd8d-xgsdm -- cat app.py
```
#### b. View Pod Logs

Check the logs of a specific pod:

```bash
kubectl logs python-webapp-deployment-54b95bd8d-xgsdm
```

