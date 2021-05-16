# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

## Create a directory for this module and go there
```
mkdir ~/cloud_storage
cd ~/cloud_storage
```

## Installation of the words list
`sudo apt install -y wamerican`

## Installation of an NFS server on VM2

### Prepare the directory

On VM2, create the directory to host the files:

```
sudo mkdir /data
```

Get the image files, decompressing them into the /data directory:

```
wget https://tinyurl.com/at6tefkx -O - | sudo tar -zx -C /data
```

Change permissions to allows reading and writing from VM1:

```
sudo chown -R nobody:nogroup /data
sudo chmod -R 777 /data
```

### NFS server installation on VM2

```
sudo apt update && sudo apt -y upgrade
sudo apt install -y nfs-kernel-server
```

Put the following line at the end of the `/etc/exports` file to export the /data directory to VM1 only:

```
/data   <private VM1 address>(rw,sync,no_subtree_check)
```

### Export the shared directory

```
sudo exportfs -a
sudo systemctl restart nfs-kernel-server
```

## Modify the security group on VM2

In the "Inbound rules", click on "Edit inbound rules", "Add Rule" and then select NFS, putting as source the VM1 private IP address, followed by the string /32. For example, 172.31.22.67/32. 

Click on Save rules and verify that the VM2 security group now allows NFS inbound.

## Mount the NFS directory on VM1

```
sudo apt update && sudo apt -y upgrade
sudo apt -y install nfs-common
sudo mkdir /remote_data
sudo mount <private VM2 address>:/data /remote_data/
```