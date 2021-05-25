# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see <a href=https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/435337>here</a>.

## Create a directory for this module and go there
```
mkdir ~/aai
cd ~/aai
```
## Self-register your application to IAM

Follow the slides for details on which IAM server to use and how to authenticate to it. A key point is that in the `Redirect URI(s)` field you should put 

```
http://<VM1_public_IP_address>:8080/redirect_uri
```

## Building and running the OIDC-enabled container

