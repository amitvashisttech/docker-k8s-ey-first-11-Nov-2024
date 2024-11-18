# Kubernetes Deployment and Rollout Management Training & Development

This section provides a set of commands for managing a Kubernetes Deployment, including updating images, exposing services, and handling rollouts.

## Commands Overview

### 1. Apply Deployment Configuration

Deploy the application using the provided YAML file:

```bash
kubectl apply -f 01-helloworld.yaml
```

### 2. Manage Deployments and Resources
#### a. Get Deployment Status

List all deployments in the current namespace:

```bash
kubectl get deploy
```

#### b. Get Deployments, ReplicaSets, and Pods

List all deployments, replicasets, and pods:

```bash
kubectl get deploy,rs,pod
```
#### c. Expose the Deployment as a Service

Expose the deployment helloworld-deployment as a NodePort service:

```bash
kubectl expose deploy helloworld-deployment --type=NodePort
```

#### d. Get Service Information

Check the status of services to find the NodePort:

```bash
kubectl get svc
```
#### e. Get Node Information

List nodes with detailed information, including IP addresses:

```bash
kubectl get nodes -o wide
```
#### f. Access the Application

Access the application via the NodePort by replacing <nodeip> and <nodeport> with actual values:

```bash
curl <nodeip>:<nodeport>
```
#### Example: curl 172.18.0.4:32742


### g. In case nodeport is not reachable then please provision busybox pod & try to access the application via CluserIP:ClusterPort: 
```
kubectl run -it busybox --image=busybox:1.28 -- sh

# wget <clusterip>:<clutserport>
```

### 3. Update Deployment Image
#### a. Update the Image Version

Update the deployment helloworld-deployment with a new image version:

```bash
kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2
kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:3
kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:4
```

### 4. Rollout Management
#### a. View Deployment Rollout History

Check the history of rollouts for the deployment:

```bash
kubectl rollout history deploy helloworld-deployment
```
#### b. View Specific Rollout Revisions

Check details of specific rollout revisions:

```bash
kubectl rollout history deploy helloworld-deployment --revision=1
kubectl rollout history deploy helloworld-deployment --revision=2
```
#### c. Rollback to a Previous Revision

Undo the last deployment, rolling back to a previous revision:

```bash
kubectl rollout undo deploy helloworld-deployment
kubectl rollout undo deploy helloworld-deployment --to-revision=2
kubectl rollout undo deploy helloworld-deployment --to-revision=1
```

### 5. Update Deployment with Rollout Record

Update the deployment image and record the rollout history:

```bash
kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:4 --record
kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:3 --record
kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record
kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web --record
```
#### a. Review the Rollout History After Updates

Review the rollout history after recording the changes:

```bash
kubectl rollout history deploy helloworld-deployment
```
