# Exercise 10 - Minikube Multi-Node Multi-App Deployment

## Overview
This project demonstrates deploying two Python Flask applications on a multi-node Kubernetes cluster using Minikube.

## Objective
To deploy multiple applications using Kubernetes Deployments and NodePort Services, and verify that application replicas run across multiple cluster nodes.

## Technologies Used
- Python
- Flask
- Docker
- Minikube
- Kubernetes
- YAML

## Applications

### 1. Product Catalog
- Returns a list of sample products in JSON format.
- Endpoint: `/products`
- Container port: `5000`
- NodePort: `30081`
- Replicas: 2

### 2. Shopping Cart
- Provides an endpoint to view cart contents.
- Supports adding an item using a POST request.
- Container port: `5001`
- NodePort: `30082`
- Replicas: 3

## Project Files
- `app.py` - Product Catalog application.
- `cart.py` - Shopping Cart application.
- `requirements.txt` - Python dependency.
- `Dockerfile` - Builds the application image.
- `product-catalog.yaml` - Product Catalog Deployment.
- `shopping-cart.yaml` - Shopping Cart Deployment.
- `product-catalog-service.yaml` - Product Catalog NodePort Service.
- `shopping-cart-service.yaml` - Shopping Cart NodePort Service.
- `README.md` - Project documentation.

## Cluster Configuration
- Minikube profile: `devops-multinode`
- Total nodes: 3 (1 control plane and 2 workers)
- Product Catalog replicas: 2
- Shopping Cart replicas: 3

## Deployment Commands
Build the Docker image:

```bash
docker build -t multi-app:v1 .
```

Load the image into Minikube:

```bash
minikube image load multi-app:v1 -p devops-multinode
```

Apply the Kubernetes configurations:

```bash
minikube kubectl -p devops-multinode -- apply -f product-catalog.yaml
minikube kubectl -p devops-multinode -- apply -f shopping-cart.yaml
minikube kubectl -p devops-multinode -- apply -f product-catalog-service.yaml
minikube kubectl -p devops-multinode -- apply -f shopping-cart-service.yaml
```

## Verification Commands

```bash
minikube kubectl -p devops-multinode -- get nodes
minikube kubectl -p devops-multinode -- get deployments
minikube kubectl -p devops-multinode -- get pods -o wide
minikube kubectl -p devops-multinode -- get services
```

## Expected Results
- Three Kubernetes nodes show `Ready`.
- Product Catalog deployment has 2 available replicas.
- Shopping Cart deployment has 3 available replicas.
- Both NodePort services are created successfully.
- Both applications respond to requests from inside the cluster.

## Learning Outcomes
- Creating and managing a multi-node Minikube cluster.
- Building and loading a Docker image.
- Deploying multiple applications with Kubernetes.
- Configuring Deployments, replicas, and NodePort Services.
- Verifying pod distribution and application availability.
