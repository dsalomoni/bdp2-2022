# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see <a href=https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/435337>here</a>.

## Create a directory for this module and go there

Do all of this of VM1.

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

## Create kind clusters

### Basic creation of a Kubernetes cluster

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

### Destroy the Kubernetes cluster

```
kind delete cluster
```

Check that the cluster is gone with 

```
docker ps
kind get clusters
kubectl cluster-info
```

### Create a Kubernetes with one control node and two workers

Copy the `kind-config.yaml` file taken from this repositrory and create the cluster with

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