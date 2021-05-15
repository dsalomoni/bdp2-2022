# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see <a href=https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/435337>here</a>.

## Configuration of the 2 VMs on AWS

### Software update
`sudo apt update && sudo apt -y upgrade`

### Changing the Linux prompt

Put the following at the end of the `.bashrc` file:

`PS1="\[\033[01;32m\]\u@VM1\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "`

The above command was for the VM called `VM1`. Do the same for `VM2`, changing VM1 to VM2 in the `PS1` string above.
Once done, activate the new prompt either by logging out and then back in, or simply typing `source .bashrc`

### Installing additional packages on VM1

```
sudo apt update
sudo apt -y upgrade
sudo apt -y install python3-pip python3-matplotlib
sudo pip install --upgrade Pillow scikit-image
```