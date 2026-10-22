# Exercise 1 - Hello Pod

## Objective
Deploy a simple NGINX Pod using Kubernetes and Minikube.

## Requirements
- Ubuntu
- Docker
- Minikube
- Kubernetes

## Steps
1. Start Minikube.
2. Apply the Kubernetes Pod configuration.
3. Check the Pod status.
4. Access the NGINX web server.
5. Delete the Pod after testing.

## Commands

Start Minikube:

    minikube start

Create the Pod:

    minikube kubectl -- apply -f pod.yaml

Check Pod status:

    minikube kubectl -- get pods

Access NGINX:

    minikube kubectl -- port-forward pod/hello-k8s 8080:80

Open http://localhost:8080 in a browser.

## Cleanup

    minikube kubectl -- delete -f pod.yaml
