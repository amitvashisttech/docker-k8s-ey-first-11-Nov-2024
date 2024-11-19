# Kubernetes Node Selectors and Label Management

This section provides guidance on managing Kubernetes pods with node selectors and labeling nodes to influence pod scheduling.

## Commands Overview

### 1. Node Information and Labeling

#### a. Get Node Information

To retrieve information about the nodes in the cluster:

```bash
kubectl get nodes
kubectl get nodes --show-labels
```

### 2. Create and Manage Deployments with Node Selectors
#### a. Create a Deployment with Node Selectors

Start by creating a deployment that specifies node selectors. This deployment configuration is defined in the helloworld-nodeselector.yaml file:

```bash
kubectl create -f helloworld-nodeselector.yaml
```

Verify the deployment and the pods:

```bash
kubectl get pods
kubectl describe pod helloworld-deployment-57986b947d-7p2nx
```

#### b. Label Nodes to Match Node Selector Requirements

Label specific nodes to match the node selector criteria in the deployment:

```bash
kubectl label nodes worker2 hardware=virtual
kubectl get nodes --show-labels
```
Check the wide output of pods to verify where they are running:

```bash
kubectl get pods -o wide
```
#### c. Additional Node Labeling

Further label nodes as required:

```bash
kubectl label nodes worker1 hardware=virtual
kubectl get nodes --show-labels
kubectl get pods -o wide
```
### 3. Scaling Deployments

Scale the deployment to adjust the number of pod replicas:

```bash
kubectl scale --replicas=6 deploy helloworld-deployment
kubectl get pods
```
Later, reduce the number of replicas:

```bash
kubectl scale --replicas=3 deploy helloworld-deployment
```
### 4. Create and Manage Multi-Node Selector Deployments
#### a. Create a Deployment with Multiple Node Selectors

Create a deployment that uses multiple node selectors as defined in helloworld-nodeselector-multi.yaml:

```bash
kubectl create -f helloworld-nodeselector-multi.yaml
```
Check the status of the new deployment and its pods:

```bash
kubectl get pods
kubectl describe pod helloworld-deployment-2-7fd7bbcd7-86jfs
```
#### b. Modify Node Labels

Label nodes with specific environment tags:

```bash
kubectl label nodes worker1 env=prod
kubectl get pods -o wide
kubectl get nodes --show-labels
```
Remove specific labels:

```bash
kubectl label nodes worker1 env-
kubectl label nodes worker1 hardware-
kubectl label nodes worker2 hardware-
kubectl get nodes --show-labels
```
### 5. Cleanup and Final Verification

After adjusting labels and deployments, ensure that nodes and pods are properly configured:

```bash
kubectl label nodes worker1 hardware=virtual
kubectl get nodes --show-labels
kubectl get pods -o wide
```
Finally, scale the deployment to a different number of replicas:

```bash
kubectl scale --replicas=5 deploy helloworld-deployment
kubectl get pods -o wide
```
### 6. Remove Labels

To clean up, remove labels from nodes:

```bash
kubectl label nodes worker1 hardware-
kubectl label nodes worker1 env-
kubectl label nodes worker2 env-
kubectl get pods
```
