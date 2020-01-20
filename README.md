# devops_capstone

In this project, we are going to train a reinforcement learning model using airflow.  
And then we ar egoing to ship the trained model in an flask app.  
The app is then wrapped into a Docker container.  
We then launch a Kubernetes cluster using AWS CloudFormation where we eventually deploy our reinforcement learning app.  


## Setup
This will set project paths nicely for you.  

```
source setup.sh
```

## Train a ML model

We like to train a reinforcement learning model using Airflow pipeline.  

On a terminal
```
cd ml
make server
```

On another
```
cd ml
make scheduler
```

Then on an airflow UI (localhost:8080), start the `pipeline` task.  
Upon a successful completion, it will create a `model.pkl` in `app` folder.

## Build infrastructure
The following code will spin up a k8s cluster using cloudformation in AWS.  
Make sure you have configured awscli on your terminal first.  

```
cd cloudformation

aws cloudformation create-stack --stack-name devopsCapstoneK8S --template-body file://body-k8s.yml --parameters file://param-k8s.json --profile user1 --capabilities CAPABILITY_IAM

```

