
# Exercise 3 - Minikube Scaling Flask App with ReplicaSets

## Objective
Deploy a Flask flash-sale application using Kubernetes ReplicaSets and scale it across multiple Pods.

## Technologies
- Python
- Flask
- Docker
- Kubernetes
- Minikube

## Files
- app.py - Flask application
- Dockerfile - Builds the application image
- replicaset.yaml - Defines the ReplicaSet and desired replicas
- service.yaml - Exposes the application

## Steps to Run

### 1. Start Minikube
    minikube start

### 2. Build the image
    minikube image build -t flashsale:v1 .

### 3. Deploy the ReplicaSet
    minikube kubectl -- apply -f replicaset.yaml

### 4. Create the Service
    minikube kubectl -- apply -f service.yaml

### 5. Verify the ReplicaSet and Pods
    minikube kubectl -- get rs
    minikube kubectl -- get pods -l app=flashsale

### 6. Scale the application
    minikube kubectl -- scale rs flashsale-replicaset --replicas=5

### 7. Verify scaling
    minikube kubectl -- get rs flashsale-replicaset
    minikube kubectl -- get pods -l app=flashsale

## Cleanup
    minikube kubectl -- delete -f service.yaml
    minikube kubectl -- delete -f replicaset.yaml

