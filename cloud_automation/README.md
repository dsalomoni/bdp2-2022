# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see <a href=https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/435337>here</a>.

## Create a directory for this module and go there

```
mkdir -p ~/cloud_automation
cd ~/cloud_automation
```

## Install go and Kind

Kind requires the Go language to work, so we will first install Go:

```
sudo apt update && sudo apt -y upgrade
sudo apt -y install golang-go
```

Install Kind:

```
go get sigs.k8s.io/kind
sudo ln -s $(go env GOPATH)/bin/kind /usr/local/bin/kind
```