# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see <a href=https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/435337>here</a>.

## Install docker

On both VM1 and VM2:

```
sudo apt update && sudo apt -y upgrade
sudo apt install -y docker.io
```

To issue docker commands without `sudo`:

```
sudo usermod -aG docker ${USER}
```

Remember to log out and then log back in to apply this change. Once done, you should now be able to issue a docker command such as `docker info` without prefixing it with `sudo`.