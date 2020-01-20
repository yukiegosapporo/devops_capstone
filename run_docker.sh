#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
docker build --tag=rlapp .

# Step 2: 
# List docker images
docker image list

# Step 3: 
# Run flask app
docker run -it -p 80:80 rlapp 