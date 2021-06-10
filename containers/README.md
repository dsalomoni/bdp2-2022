# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see <a href=https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/435337>here</a>.

## Create a directory for this module and go there
```
mkdir -p ~/containers
cd ~/containers
```

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

Remember to log out and then log back in to apply this change. Once done, you should be able to issue a docker command such as `docker info` without prefixing it with `sudo`.

## Inspecting bridges

Create a bridge and connect a container to that bridge:

```
docker network create my-bridge
docker run --rm -it --network=my-bridge --name=test1 alpine sh
```
Show the configuration of a bridge:

```
docker network inspect <bridge>
```

Parse the output of this command to print the containers connected to a certain bridge:

```
docker network inspect my-bridge | python3 -c "import sys, json; print([v['Name'] for k,v in json.load(sys.stdin)[0]['Containers'].items()])"
```

## What is my IP address?

Check the real IP address of `test1`, connected to the `my-bridge` bridge:
```
# this is to be done on test1
apk update && apk add bind-tools
dig +short myip.opendns.com @resolver1.opendns.com
```

## Install portainer

```
docker volume create portainer_data
docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

Remember to change the VM1 security group appropriately or you won't be able to connect to portainer.

__Note that the unibo wireless network may block outgoing traffic to port 9000__. In this case, you would not be able to open the Portainer web page. Possible workarounds: change the port exposed by VM1 to port 80 with the `-p` flag above, or connect to the Internet through another network.

## Run mypi.py in a container

Create an alpine container, connect to it and run `mypi.py`:

```
docker run --rm -it --name=test1 alpine sh
# install python3 in the container
apk update && apk add python3 

# write mypi.py in the container
# copy it from this repo

# run mypi.py in the container
python3 mypi.py #
```

Check what's going on in another terminal window on VM1 with `docker top test1`, with `docker stats test1`, as well as with portainer.

## Install `git` on VM1

```
sudo apt update && sudo apt install -y git
```


## Create a local repo

```
mkdir -p ~/containers/myweb
cd ~/containers/myweb
git init
```

## Pushing a new repo to GitHub

Tell git the location of the remote repository (it must be already created on GitHub) and push your changes to GitHub. You will be asked your GitHub username and password.
```
git remote add origin https://github.com/dsalomoni/bdp2-test.git
git push -u origin master
```

If you then want to retrieve the latest published version of the files on the repo, use the `pull` command:
```
git pull origin master
```

## Cloning a repo
The command is `git clone`. Try it on VM2.
```
git clone https://github.com/dsalomoni/bdp2-test.git
```