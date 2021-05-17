# bdp2-2021
This repository contains files used in the course <b>Infrastructures for Big Data Processing</b> (BDP2) at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see <a href=https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/435337>here</a>.

## git commands

Add files to git:
```
git add Dockerfile index.html
```

Check the status with
```
git status
```

Commit:
```
git commit -m "First commit of my web server"
```

Edit your Dockerfile to support non-interactive tzdata (add the line `ENV DEBIAN_FRONTEND=noninteractive`) and then add and commit the changed file:
```
git commit -a -m "Fix for non interactive tzdata"
```

You can now succesfully build and run your web server with 
```
docker build -t web_server .
docker run -d -p 8080:80 web_server
```

Changes and reverting to previous versions:
```
# this gives you details about the differences introduced in each commit
git log -p 

# revert to a version of a file (e.g. index.html) specified by a commit hash
git checkout <hash> -- index.html

# revert all files to a given commit (careful!)
git reset --hard <hash>
```