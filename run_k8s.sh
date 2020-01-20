#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
# dockerpath=<>
dockerpath=yukiego/rlapp

# Step 2
# Run the Docker Hub container with kubernetes
echo "step 2"
docker login
kubectl run --image=$dockerpath rlapp --port=5000

# Step 3:
# List kubernetes pods
echo "step 3"
kubectl get po

# Step 4:
# Forward the container port to a host
echo "step 4"
kubectl expose deployment rlapp --type=LoadBalancer --name=rlapp-service
# kubectl expose deployment rlapp --type=NodePort --name=rlapp-service
kubectl describe services rlapp-service
kubectl get services rlapp-service