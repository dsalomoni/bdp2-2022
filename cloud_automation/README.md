# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see <a href=https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/435337>here</a>.

Note: all the commands below should be performed on VM1.

## Create a directory for this module and go there

```
mkdir -p ~/cloud_automation
cd ~/cloud_automation
```

## Install kubectl

`kubectl` is a command line tool used to control Kubernetes clusters. Install it with the following commands:

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/
```

## Install minikube

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x ./minikube-linux-amd64
sudo mv ./minikube-linux-amd64 /usr/local/bin/minikube
```

Before moving on, check that both kubectl and minikube work with the commands

```
kubectl version --client
minikube version
```

## Creation of a one-node Kubernetes cluster

```
minikube create cluster
```

Check what happened with the following commands:

```
docker ps
kubectl cluster-info
kubectl get nodes
kubectl get nodes -o wide
docker exec minikube ip address show eth0
kubectl get pods
```

Can you make out what type of output each command returns, and how they relate to each other?

## Destroy the Kubernetes cluster

```
minikube delete
```

Check that the cluster is gone with 

```
docker ps
kubectl cluster-info
```

## Creation of a Kubernetes with one control node and two workers

```
minikube start --nodes 3
```

Check again what happened with the following commands:

```
docker ps
kubectl cluster-info
kubectl get nodes -o wide
kubectl get pods
```

You should now have your Kubernetes cluster running. Notice that you still have no running pods in the cluster.

## Creation of the nginx pod(s)

### Create a single pod

```
kubectl apply -f nginx-pod.yaml
```

Check the status of the cluster before and after the command above with `kubectl get all -o wide`

You can delete the pod with `kubectl delete pod nginx`.

### Create a Deployment

Open a second terminal window on VM1 and issue the command `watch kubectl get all -o wide`. This will periodically check the status of our Kubernetes cluster. 

Create a "Kubernetes Deployment" now with

```
kubectl apply -f nginx-deployment.yaml
```

and observe what happens to the cluster. 

Now delete one of the pods with `kubectl delete pod nginx-deploy-xxxxx` (replace xxxxx with the appropriate string for one of your pods). What happens? Play with the number of replicas in the YAML file.

You can delete the Deployment with `kubectl delete deployment nginx-deploy`. 