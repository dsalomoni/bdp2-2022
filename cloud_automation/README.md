# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see <a href=https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/435337>here</a>.

Note: all commands below should be performed on VM1.

## Create a directory for this module and go there

```
mkdir -p ~/cloud_automation
cd ~/cloud_automation
```

## Install Kind

```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin
```

## Install kubectl

`kubectl` is a command line tool used to control Kubernetes clusters. Install it with the following commands:

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/
```

## Creation of a one-node Kubernetes cluster

```
kind create cluster
```

Check what happened with the following commands:

```
docker ps
kind get clusters
kubectl cluster-info
kubectl get nodes
kubectl get nodes -o wide
docker exec kind-control-plane ip address show eth0
docker network ls
docker inspect kind
kubectl get pods
```

Can you make out what type of output each command returns, and how they relate to each other?

## Destroy the Kubernetes cluster

```
kind delete cluster
```

Check that the cluster is gone with 

```
docker ps
kind get clusters
kubectl cluster-info
```

## Creation of a Kubernetes with one control node and two workers

Copy the `kind-config.yaml` file taken from this repository and create the cluster with

```
kind create cluster --config kind-config.yaml
```

Check again what happened with the following commands:

```
docker ps
kind get clusters
kubectl cluster-info
kubectl get nodes
kubectl get nodes -o wide
docker inspect kind
kubectl get pods
```

You should now have your Kubernetes cluster running. Notice that you still have no running pods in the cluster.

## Creation of the nginx pod(s)

### Single pod

```
kubectl create -f nginx-pod.yaml
```

Check the status of the cluster before and after the command above with `kubectl get all -o wide`

You can delete the pod with `kubectl delete pod nginx`

### Create a replica set

Now open a separate terminal window on VM1 and issue the command `watch kubectl get all -o wide`. This will periodically check the status of our Kubernetes cluster. 

Create a "replica set" now with

```
kubectl create -f nginx-replicas.yaml
```

and observe what happens to the cluster. 

Now delete one of the pods with `kubectl delete pod nginx-replicaset-xxxxx` (replace xxxxx with the appropriate string for one of your pods). What happens?

Delete the replica set with `kubectl delete replicaset nginx-replicaset`. Observe the status of the cluster.