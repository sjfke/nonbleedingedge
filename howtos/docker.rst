:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/howtos/docker.rst

******
Docker
******

Introduction
============

This HOWTO explains how to use `docker` on `Fedora 28`, `MacOS`, and it is based on the tutorial links below.

Tutorial Links
==============

* `Docker for Beginners <https://docker-curriculum.com/>`_
* `Docker Getting Started <https://docs.docker.com/get-started/>`_

Useful Links
============

* `Docker Hub (Dev-test pipeline automation, 100,000+ free apps, public and private registries) <https://hub.docker.com/>`_
* `BusyBox: The Swiss Army Knife of Embedded Linux <https://busybox.net/about.html>`_
* `Homebrew: The missing package manager for macOS <https://brew.sh/>`_
* `Homebrew installation <https://www.howtogeek.com/211541/homebrew-for-os-x-easily-installs-desktop-apps-and-terminal-utilities/>`_


Installation
============

First create your `free` **DockerID** `DockerHub registration <https://docs.docker.com/docker-id/>`_

Fedora provides a Group Installation::

	$ sudo dnf group list --installed | grep -i container
	   Container Management
	   
	$ sudo dnf group info 'Container Management'
	Last metadata expiration check: 1:50:48 ago on Wed 17 Oct 2018 02:41:52 PM CEST.
	
	Group: Container Management
	 Description: Tools for managing Linux containers
	 Mandatory Packages:
	   atomic
	 Default Packages:
	   docker
	 Optional Packages:
	   buildah
	   podman
	 Conditional Packages:
	   cockpit-docker

	$ sudo dnf group install 'Container Management' # install
	$ sudo dnf group remove 'Container Management'  # deinstall

	$ sudo systemctl status docker  # docker running?
	$ sudo systemctl start docker   # start docker
	$ sudo systemctl enable docker  # start docker on system boot
	$ sudo docker ps -a
	Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
	
On MacOS use `brew cask`:
::

	$ brew cask install docker   # Installs the Docker application
	$ brew cask uninstall docker # Deinstalls the Docker application
	
Once installed, *double-click* the `Docker` icon to open it, enter your Docker ID details.

When this article was written, 2018.10.18, I encountered issues *removing* and *reinstalling* 
`docker`; the following was required to get it working. 
::

	$ brew cask --force uninstall docker
	$ brew cleanup
	$ brew update
	$ brew upgrade
	$ brew cleanup
	$ brew cask install docker # AND THEN reboot your Mac!


Checking Your installation
==========================
	
Run some simple tests::

	$ sudo docker run hello-world
	Hello from Docker!
	This message shows that your installation appears to be working correctly.
	
	To generate this message, Docker took the following steps:
	 1. The Docker client contacted the Docker daemon.
	 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
	    (amd64)
	 3. The Docker daemon created a new container from that image which runs the
	    executable that produces the output you are currently reading.
	 4. The Docker daemon streamed that output to the Docker client, which sent it
	    to your terminal.
	
	To try something more ambitious, you can run an Ubuntu container with:
	 $ docker run -it ubuntu bash
	
	Share images, automate workflows, and more with a free Docker ID:
	 https://hub.docker.com/
	
	For more examples and ideas, visit:
	 https://docs.docker.com/get-started/

	$ docker run -it ubuntu bash # interacive bash shell using latest Ubuntu release.
	root@9b5393a077b0:/# cat /etc/lsb-release 
	DISTRIB_ID=Ubuntu
	DISTRIB_RELEASE=18.04
	DISTRIB_CODENAME=bionic
	DISTRIB_DESCRIPTION="Ubuntu 18.04.1 LTS"
	root@9b5393a077b0:/# exit

	$ sudo docker pull busybox   # pull the latest busybox, 'run' will also do this.
	$ sudo docker run busybox    # produces no output, but actually creates the container and runs it.
	$ sudo docker run busybox echo "hello from busybox"
	hello from busybox

	$ sudo docker pull toybox    # BSD Licensed version of BusyBox not available.
	Using default tag: latest
	Trying to pull repository docker.io/library/toybox ... 
	Trying to pull repository registry.fedoraproject.org/toybox ... 
	Trying to pull repository quay.io/toybox ... 
	Trying to pull repository registry.access.redhat.com/toybox ... 
	Trying to pull repository registry.centos.org/toybox ... 
	Trying to pull repository docker.io/library/toybox ... 
	repository docker.io/toybox not found: does not exist or no pull access

	$ sudo docker run --help     # Help summary


Which docker containers have we run or are still running?::

	$ sudo docker ps    # no running docker images, so nothing listed.
	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

	$ sudo docker ps    # 1 ubuntu docker image running.
	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
	b076c01e8e87        ubuntu              "bash"              7 seconds ago       Up 6 seconds                            jolly_euclid

	$ sudo docker ps -a # all docker images that have been run and their status.
	CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                         PORTS               NAMES
	9b5393a077b0        ubuntu              "bash"                   52 seconds ago      Exited (0) 22 seconds ago                          naughty_leavitt
	65369ae65026        busybox             "echo 'hello from ..."   5 minutes ago       Exited (0) 5 minutes ago                           objective_ptolemy
	bff5545478e5        busybox             "echo 'hello from ..."   5 minutes ago       Exited (0) 5 minutes ago                           compassionate_hawking
	d8f0813dc896        hello-world         "/hello"                 39 minutes ago      Exited (0) 39 minutes ago                          nostalgic_borg
	af57a783956b        busybox             "sh"                     About an hour ago   Exited (0) About an hour ago                       quirky_aryabhata
	67c9e731a433        busybox             "echo 'hello from ..."   About an hour ago   Exited (0) About an hour ago                       trusting_feynman
	fe96abf8f8ff        busybox             "sh"                     About an hour ago   Exited (0) About an hour ago                       determined_saha
	e17558e53834        ubuntu              "bash"                   2 hours ago         Exited (0) 2 hours ago                             sharp_heisenberg


What docker images have been `pulled`?::

	$ sudo docker images
	REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
	docker.io/busybox       latest              59788edf1f3e        2 weeks ago         1.15 MB
	docker.io/hello-world   latest              4ab4c602aa5e        5 weeks ago         1.84 kB
	docker.io/ubuntu        latest              cd6d8154f1e1        5 weeks ago         84.1 MB

Removing a docker image::

	$ sudo docker ps -a
	CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                    PORTS               NAMES
	b076c01e8e87        ubuntu              "bash"                   22 hours ago        Exited (0) 22 hours ago                       jolly_euclid
	9b5393a077b0        ubuntu              "bash"                   22 hours ago        Exited (0) 22 hours ago                       naughty_leavitt
	65369ae65026        busybox             "echo 'hello from ..."   22 hours ago        Exited (0) 22 hours ago                       objective_ptolemy
	bff5545478e5        busybox             "echo 'hello from ..."   22 hours ago        Exited (0) 22 hours ago                       compassionate_hawking
	$ sudo docker rm 9b5393a077b0
	9b5393a077b0
	$ sudo docker ps -a
	CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                    PORTS               NAMES
	b076c01e8e87        ubuntu              "bash"                   22 hours ago        Exited (0) 22 hours ago                       jolly_euclid
	65369ae65026        busybox             "echo 'hello from ..."   22 hours ago        Exited (0) 22 hours ago                       objective_ptolemy
	bff5545478e5        busybox             "echo 'hello from ..."   22 hours ago        Exited (0) 22 hours ago                       compassionate_hawking

	$ docker rm $(docker ps -a -q -f status=exited) # remove all exited containers
	$ docker container prune                        # remove all exited containers

	
WebApps with Docker
===================
::

	$ sudo docker run -d -P --name static-site prakhar1989/static-site # detach '-d' 
	
	$ sudo docker port static-site
	443/tcp -> 0.0.0.0:32768
	80/tcp -> 0.0.0.0:32769
	
	$ sudo dnf install perl-libwww-perl.noarch # if not installed.
	$ HEAD http://localhost:32769/
	200 OK
	Connection: close
	Date: Thu, 18 Oct 2018 14:31:36 GMT
	Accept-Ranges: bytes
	ETag: "5688a450-7f9"
	Server: nginx/1.9.9
	Content-Length: 2041
	Content-Type: text/html
	Last-Modified: Sun, 03 Jan 2016 04:32:16 GMT
	Client-Date: Thu, 18 Oct 2018 14:31:36 GMT
	Client-Peer: ::1:32769
	Client-Response-Num: 1
	
	$ sudo docker run -p 8888:80 prakhar1989/static-site # redirect port 8888 (in one shell)
	Nginx is running...
	172.17.0.1 - - [18/Oct/2018:14:32:15 +0000] "HEAD / HTTP/1.1" 200 0 "-" "lwp-request/6.34 libwww-perl/6.34" "-"

	$ HEAD http://localhost:8888/  # check the access (in another shell)
	200 OK
	Connection: close
	Date: Thu, 18 Oct 2018 14:32:15 GMT
	Accept-Ranges: bytes
	ETag: "5688a450-7f9"
	Server: nginx/1.9.9
	Content-Length: 2041
	Content-Type: text/html
	Last-Modified: Sun, 03 Jan 2016 04:32:16 GMT
	Client-Date: Thu, 18 Oct 2018 14:32:15 GMT
	Client-Peer: ::1:8888
	Client-Response-Num: 1

	$ sudo docker stop static-site
	static-site
	$ HEAD http://localhost:32769/
	500 Can't connect to localhost:32769 (Connection refused)
	Content-Type: text/plain
	Client-Date: Thu, 18 Oct 2018 14:34:56 GMT
	Client-Warning: Internal response

Build Your Own
==============

By default `dockerd <https://docs.docker.com/engine/reference/commandline/dockerd/>`_ will 
attempt to do 5 `pushes` in parallel, which will not work on a *modest* ADSL connection. 
Try adjusting `"--max-concurrent-uploads"` officially this is in `"/etc/docker/daemon.json"` 
but this is not true on Fedora or MacOS.
::

	Fedora: 
	$ sudo vim /etc/sysconfig/docker
	# Modify these options if you want to change the way the docker daemon runs
	# OPTIONS='--selinux-enabled --log-driver=journald --live-restore'
	OPTIONS='--max-concurrent-uploads 1 --selinux-enabled --log-driver=journald --live-restore'
	$ sudo systemctl restart docker
	
	MacOS:
	Docker Icon > Preferences > Daemon > Advanced

So having stopped `"docker push"` from hanging your ADSL connection, you can continue.
::

	$ git clone https://github.com/prakhar1989/docker-curriculum
	$ cd docker-curriculum/flask-app
	
	cat > Dockerfile <<EOT
	# our base image
	FROM python:3-onbuild
	# specify the port number the container should expose
	EXPOSE 5000
	# run the application
	CMD ["python", "./app.py"]
	EOT
	
	$ sudo docker build -t sjfke/catnip .  # 'sjfke' my DockerHub account
	$ sudo docker login                    # login to DockerHub
	$ sudo docker push sjfke/catnip        # push my container to DockerHub
 
	$ docker run -p 8888:5000 sjfke/catnip # download and run on another system
	
AWS Elastic Beanstalk (EB)
==========================

* `AWS EB <https://aws.amazon.com/elasticbeanstalk/>`_

Much of this is interacting with Web graphical interfaces, so `follow the tutorial instructions <https://docker-curriculum.com/#docker-on-aws>`_. 


Multi-Container Environments
============================

::

	$ git clone https://github.com/prakhar1989/FoodTrucks
	$ cd FoodTrucks/
	$ sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.2
	$ sudo docker run -d --name es -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.2
	$ sudo docker container ls # inconviently the name is the last field!
	$ sudo docker container logs es
	
	$ curl 0.0.0.0:9200
	{
	  "name" : "MYk3rl7",
	  "cluster_name" : "docker-cluster",
	  "cluster_uuid" : "dCG3beIgQSq3mGhSVHku_g",
	  "version" : {
	    "number" : "6.3.2",
	    "build_flavor" : "default",
	    "build_type" : "tar",
	    "build_hash" : "053779d",
	    "build_date" : "2018-07-20T05:20:23.451332Z",
	    "build_snapshot" : false,
	    "lucene_version" : "7.3.1",
	    "minimum_wire_compatibility_version" : "5.6.0",
	    "minimum_index_compatibility_version" : "5.0.0"
	  },
	  "tagline" : "You Know, for Search"
	}

So cool we have `ElasticSearch` running in its own container `es`.

Now build the `flask` application, but because we need to customize it by running 
commands, we will use an ubuntu container as can be seen in the `Dockerfile`::

	# start from base
	FROM ubuntu:latest
	MAINTAINER Prakhar Srivastav <prakhar@prakhar.me>
	
	# install system-wide deps for python and node
	RUN apt-get -yqq update
	RUN apt-get -yqq install python-pip python-dev curl gnupg
	RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
	RUN apt-get install -yq nodejs
	
	# copy our application code
	ADD flask-app /opt/flask-app
	WORKDIR /opt/flask-app
	
	# fetch app specific deps
	RUN npm install
	RUN npm run build
	RUN pip install -r requirements.txt
	
	# expose port
	EXPOSE 5000
	
	# start app
	CMD [ "python", "./app.py" ]

	# check we are Foodtrucks directory
	$ sudo docker build -t prakhar1989/foodtrucks-web .

So now lets try to run it::

	$ sudo docker run -P --rm prakhar1989/foodtrucks-web
	Unable to connect to ES. Retrying in 5 secs...
	Unable to connect to ES. Retrying in 5 secs...
	Unable to connect to ES. Retrying in 5 secs...
	Out of retries. Bailing out...
 	
