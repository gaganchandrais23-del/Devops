# Exercise 2 - Minikube Flask Application

## Objective
Deploy a Python Flask web application on Kubernetes using Minikube and kubectl.

## Technologies
- Python
- Flask
- Docker
- Kubernetes
- Minikube

## Files
- app.py - Flask web application
- Dockerfile - Builds the Flask Docker image
- flask-deployment.yaml - Kubernetes Deployment configuration
- README.md - Project documentation

## Steps to Run

### 1. Start Minikube
    minikube start

### 2. Configure Minikube Docker
    eval $(minikube docker-env)

### 3. Build the Docker Image
    docker build -t flask-app:latest .

### 4. Deploy the Application
    minikube kubectl -- apply -f flask-deployment.yaml

### 5. Verify the Deployment
    minikube kubectl -- get deployments
    minikube kubectl -- get pods -l app=flask-app

### 6. Access the Application
    minikube kubectl -- port-forward deployment/flask-app 8081:15000

Open http://localhost:8081 in a browser.

Expected response:

    Hello from Flask on Kubernetes!

### 7. View Logs
    minikube kubectl -- logs deployment/flask-app

## Cleanup
    minikube kubectl -- delete -f flask-deployment.yaml
