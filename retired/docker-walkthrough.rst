:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/retired/docker-walkthrough.rst

***************************
Docker Tutorial Walkthrough
***************************

.. important:: Very old draft, anticipate inaccuracies and outdated information.

Introduction
============

This is a `walkthrough` of `Docker for Beginners` tutorial using a `Fedora 28` system.

Generally everything works as anticipated, but the `docker` commands need to be run as root on `Fedora 28`.

Tutorial Links
==============

* `Docker for Beginners by Prakhar Srivastav <https://docker-curriculum.com/>`_
* `Docker Getting Started <https://docs.docker.com/get-started/>`_

Useful Links
============

* `Docker Hub (Dev-test pipeline automation, 100,000+ free apps, public and private registries) <https://hub.docker.com/>`_
* `BusyBox: The Swiss Army Knife of Embedded Linux <https://busybox.net/about.html>`_
* `Homebrew: The missing package manager for macOS <https://brew.sh/>`_
* `Homebrew installation <https://www.howtogeek.com/211541/homebrew-for-os-x-easily-installs-desktop-apps-and-terminal-utilities/>`_
* `AWS CloudFormation <https://aws.amazon.com/cloudformation/>`_

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
	
	$ grep -n Elasticsearch flask-app/app.py # shows the failing connection, on line 8
	1:from elasticsearch import Elasticsearch, exceptions
	8:es = Elasticsearch(host='es')

	
This fails be the `foodtrucks-web` container cannot connect to `es` container on 0.0.0.0:9200
To understand why need to understand docker networks.

Docker networks
===============

Our Elasticsearch is running, but on 0.0.0.0:9200
::

	$ sudo docker container ls
	CONTAINER ID        IMAGE                                                 COMMAND                  CREATED             STATUS              PORTS                                            NAMES
	712659c6d89c        docker.elastic.co/elasticsearch/elasticsearch:6.3.2   "/usr/local/bin/do..."   31 minutes ago      Up 31 minutes       0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp   es

	$ sudo docker network ls # bridge is the default network for containers
	NETWORK ID          NAME                DRIVER              SCOPE
	544ab266e4de        bridge              bridge              local
	09a4096c7d69        host                host                local
	baf3cfdf732b        none                null                local

	$ sudo docker inspect bridge
	[
	    {
	        "Name": "bridge",
	        "Id": "544ab266e4de0d21850a4994cad1bc8faa916786ac637f0d32e9f192933c46c1",
	        "Created": "2018-12-13T18:41:45.124184344+01:00",
	        "Scope": "local",
	        "Driver": "bridge",
	        "EnableIPv6": false,
	        "IPAM": {
	            "Driver": "default",
	            "Options": null,
	            "Config": [
	                {
	                    "Subnet": "172.17.0.0/16",
	                    "Gateway": "172.17.0.1"
	                }
	            ]
	        },
	        "Internal": false,
	        "Attachable": false,
	        "Containers": {
	            "712659c6d89c205d9e24b5a1060c6f47c3a69dc5abb8f66279dfcac398cbf731": {
	                "Name": "es",
	                "EndpointID": "cde9ba10ebe16df0fd7f919b46814e5251ab4af0d2a56b668ef2fc5c256fd76e",
	                "MacAddress": "02:42:ac:11:00:02",
	                "IPv4Address": "172.17.0.2/16",
	                "IPv6Address": ""
	            }
	        },
	        "Options": {
	            "com.docker.network.bridge.default_bridge": "true",
	            "com.docker.network.bridge.enable_icc": "true",
	            "com.docker.network.bridge.enable_ip_masquerade": "true",
	            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
	            "com.docker.network.bridge.name": "docker0",
	            "com.docker.network.driver.mtu": "1500"
	        },
	        "Labels": {}
	    }
	]

So the `es` container is bond to 172.17.0.2:9200 but this is the default docker network, 
let's isolate our app to anothe rbridged network.::

	$ sudo docker network create foodtrucks-net
	f9005012280de00eda23d3ff18a5924ff1e410cb7a11a077db62da2b408767c0
	
	$ sudo docker network ls
	NETWORK ID          NAME                DRIVER              SCOPE
	544ab266e4de        bridge              bridge              local
	f9005012280d        foodtrucks-net      bridge              local
	09a4096c7d69        host                host                local
	baf3cfdf732b        none                null                local
	
	$ sudo docker stop es
	$ sudo docker rm es
	es
	$ sudo docker run -d --name es --net foodtrucks-net -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.2
	3ba626d4716ae921ec42b22a5fe5e65accba477ec4b66a319e214ae7bbdeed2f

	$ sudo docker network inspect foodtrucks-net
	[
	    {
	        "Name": "foodtrucks-net",
	        "Id": "f9005012280de00eda23d3ff18a5924ff1e410cb7a11a077db62da2b408767c0",
	        "Created": "2018-12-13T19:40:47.281917543+01:00",
	        "Scope": "local",
	        "Driver": "bridge",
	        "EnableIPv6": false,
	        "IPAM": {
	            "Driver": "default",
	            "Options": {},
	            "Config": [
	                {
	                    "Subnet": "172.18.0.0/16",
	                    "Gateway": "172.18.0.1"
	                }
	            ]
	        },
	        "Internal": false,
	        "Attachable": false,
	        "Containers": {
	            "3ba626d4716ae921ec42b22a5fe5e65accba477ec4b66a319e214ae7bbdeed2f": {
	                "Name": "es",
	                "EndpointID": "129c8ffdddaa13c9ac3d2c394e8abc9cf96ca14685875408b7f38cbe6b32b481",
	                "MacAddress": "02:42:ac:12:00:02",
	                "IPv4Address": "172.18.0.2/16",
	                "IPv6Address": ""
	            }
	        },
	        "Options": {},
	        "Labels": {}
	    }
	]

	$ sudo docker run -it --rm --net foodtrucks-net prakhar1989/foodtrucks-web bash
	root@9e892d64b9d9:/opt/flask-app# curl es:9200
	{
	  "name" : "5pAqhsu",
	  "cluster_name" : "docker-cluster",
	  "cluster_uuid" : "4etLMfQmTmamKqaayrLAyw",
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
	root@9e892d64b9d9:/opt/flask-app# ls
	app.py  node_modules  package-lock.json  package.json  requirements.txt  static  templates  webpack.config.js
	root@9e892d64b9d9:/opt/flask-app# python app.py
	Index not found...
	Loading data in elasticsearch ...
	Total trucks loaded:  623
	 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
	^C
	root@9e892d64b9d9:/opt/flask-app# exit
	exit

Thanks to *automatic service discovery* the communication works and it resolves the container names!::

	$ sudo docker run -d --net foodtrucks-net -p 5000:5000 --name foodtrucks-web prakhar1989/foodtrucks-web
	019f0602b51eb71324909b351f4bb217e08efd1309bb625c243acfd08bc5a21a
	$ curl -I 0.0.0.0:5000
	HTTP/1.0 200 OK
	Content-Type: text/html; charset=utf-8
	Content-Length: 3697
	Server: Werkzeug/0.11.2 Python/2.7.15rc1
	Date: Thu, 13 Dec 2018 18:52:28 GMT
 
The application is git repo is distributed with `setup-docker.sh` bash script::

	#!/bin/bash
	
	# build the flask container
	docker build -t prakhar1989/foodtrucks-web .
	
	# create the network
	docker network create foodtrucks-net
	
	# start the ES container
	docker run -d --name es --net foodtrucks-net -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.2
	
	# start the flask app container
	docker run -d --net foodtrucks-net -p 5000:5000 --name foodtrucks-web prakhar1989/foodtrucks-web

So to download and run the application all that is needed::

	$ git clone https://github.com/prakhar1989/FoodTrucks
	$ cd FoodTrucks
	$ ./setup-docker.sh
	
	# if following the toturial you need to clean up
	$ sudo docker stop foodtrucks-web es
	$ sudo docker rm foodtrucks-web es
	$ sudo docker network rm foodtrucks-net
	$ sudo docker network ls
	NETWORK ID          NAME                DRIVER              SCOPE
	544ab266e4de        bridge              bridge              local
	09a4096c7d69        host                host                local
	baf3cfdf732b        none                null                local
	#
	$ sudo ./setup-docker.sh

Docker Compose
==============

Various tools exists for running multiple docker containers:

* `Docker Machine <https://docs.docker.com/machine/overview/>`_ Create Docker hosts on your computer, on cloud providers, or own data center
* `Docker Compose <https://docs.docker.com/compose/overview/>`_ A tool for defining and running multi-container Docker applications.
* `Docker Swarm <https://docs.docker.com/swarm/overview/>`_ A native clustering solution for Docker.
* `Kubernetes <https://kubernetes.io/>`_ Production-Grade Container Orchestration.

Will focus on `Docker Compose`.

Docker Compose
--------------

::

	$ sudo dnf install docker-compose # F28 need to install
	$ docker-compose --version
	docker-compose version 1.20.1, build 5d8c71b

	$ cat docker-compose.yml 
	version: "3"
	services:
	  es:
	    image: docker.elastic.co/elasticsearch/elasticsearch:6.3.2
	    container_name: es
	    environment:
	      - discovery.type=single-node
	    ports:
	      - 9200:9200
	    volumes:
	      - esdata1:/usr/share/elasticsearch/data
	  web:
	    image: prakhar1989/foodtrucks-web
	    command: python app.py
	    depends_on:
	      - es
	    ports:
	      - 5000:5000
	    volumes:
	      - ./flask-app:/opt/flask-app
	volumes:
	    esdata1:
	      driver: local

	$ sudo docker stop es web # stop 'es' and 'web' containers
	$ sudo docker ps -a       # check that everything has exited
	
	
Online manuals:

* `Docker Compose V3 <https://docs.docker.com/compose/compose-file/compose-file-v3/>`_
* `Docker Compose V2 <https://docs.docker.com/compose/compose-file/compose-file-v2/>`_
* `Docker Compose V1 <https://docs.docker.com/compose/compose-file/compose-file-v1/>`_

::

	$ sudo docker-compose up
	Creating network "foodtrucks_default" with the default driver
	Creating volume "foodtrucks_esdata1" with local driver
	Creating es ... done
	Creating foodtrucks_web_1 ... done
	Attaching to es, foodtrucks_web_1
	es     | OpenJDK 64-Bit Server VM warning: Option UseConcMarkSweepGC was deprecated in version 9.0 and will likely be removed in a future release.
	es     | OpenJDK 64-Bit Server VM warning: UseAVX=2 is not supported on this CPU, setting it to UseAVX=1
	es     | [2019-01-24T10:03:01,941][INFO ][o.e.n.Node               ] [] initializing ...
	es     | [2019-01-24T10:03:02,029][INFO ][o.e.e.NodeEnvironment    ] [SeQUrzx] using [1] data paths, mounts [[/usr/share/elasticsearch/data (/dev/mapper/fedora-root)]], net usable_space [33.1gb], net total_space [48.9gb], types [ext4]
	es     | [2019-01-24T10:03:02,030][INFO ][o.e.e.NodeEnvironment    ] [SeQUrzx] heap size [990.7mb], compressed ordinary object pointers [true]
	es     | [2019-01-24T10:03:02,033][INFO ][o.e.n.Node               ] [SeQUrzx] node name derived from node ID [SeQUrzxwQZW2cvh3rOmcCg]; set [node.name] to override
	es     | [2019-01-24T10:03:02,033][INFO ][o.e.n.Node               ] [SeQUrzx] version[6.3.2], pid[1], build[default/tar/053779d/2018-07-20T05:20:23.451332Z], OS[Linux/4.19.16-200.fc28.x86_64/amd64], JVM["Oracle Corporation"/OpenJDK 64-Bit Server VM/10.0.2/10.0.2+13]
	es     | [2019-01-24T10:03:02,034][INFO ][o.e.n.Node               ] [SeQUrzx] JVM arguments [-Xms1g, -Xmx1g, -XX:+UseConcMarkSweepGC, -XX:CMSInitiatingOccupancyFraction=75, -XX:+UseCMSInitiatingOccupancyOnly, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -XX:-OmitStackTraceInFastThrow, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Djava.io.tmpdir=/tmp/elasticsearch.S5IHZOuq, -XX:+HeapDumpOnOutOfMemoryError, -XX:HeapDumpPath=data, -XX:ErrorFile=logs/hs_err_pid%p.log, -Xlog:gc*,gc+age=trace,safepoint:file=logs/gc.log:utctime,pid,tags:filecount=32,filesize=64m, -Djava.locale.providers=COMPAT, -XX:UseAVX=2, -Des.cgroups.hierarchy.override=/, -Des.path.home=/usr/share/elasticsearch, -Des.path.conf=/usr/share/elasticsearch/config, -Des.distribution.flavor=default, -Des.distribution.type=tar]
	es     | [2019-01-24T10:03:05,044][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [aggs-matrix-stats]
	es     | [2019-01-24T10:03:05,044][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [analysis-common]
	es     | [2019-01-24T10:03:05,044][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [ingest-common]
	es     | [2019-01-24T10:03:05,044][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [lang-expression]
	es     | [2019-01-24T10:03:05,044][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [lang-mustache]
	es     | [2019-01-24T10:03:05,044][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [lang-painless]
	es     | [2019-01-24T10:03:05,044][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [mapper-extras]
	es     | [2019-01-24T10:03:05,044][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [parent-join]
	es     | [2019-01-24T10:03:05,045][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [percolator]
	es     | [2019-01-24T10:03:05,045][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [rank-eval]
	es     | [2019-01-24T10:03:05,045][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [reindex]
	es     | [2019-01-24T10:03:05,045][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [repository-url]
	es     | [2019-01-24T10:03:05,045][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [transport-netty4]
	es     | [2019-01-24T10:03:05,045][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [tribe]
	es     | [2019-01-24T10:03:05,045][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-core]
	es     | [2019-01-24T10:03:05,045][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-deprecation]
	es     | [2019-01-24T10:03:05,045][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-graph]
	es     | [2019-01-24T10:03:05,046][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-logstash]
	es     | [2019-01-24T10:03:05,046][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-ml]
	es     | [2019-01-24T10:03:05,046][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-monitoring]
	es     | [2019-01-24T10:03:05,046][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-rollup]
	es     | [2019-01-24T10:03:05,046][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-security]
	es     | [2019-01-24T10:03:05,046][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-sql]
	es     | [2019-01-24T10:03:05,046][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-upgrade]
	es     | [2019-01-24T10:03:05,046][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded module [x-pack-watcher]
	es     | [2019-01-24T10:03:05,047][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded plugin [ingest-geoip]
	es     | [2019-01-24T10:03:05,047][INFO ][o.e.p.PluginsService     ] [SeQUrzx] loaded plugin [ingest-user-agent]
	es     | [2019-01-24T10:03:09,588][INFO ][o.e.x.s.a.s.FileRolesStore] [SeQUrzx] parsed [0] roles from file [/usr/share/elasticsearch/config/roles.yml]
	es     | [2019-01-24T10:03:10,304][INFO ][o.e.x.m.j.p.l.CppLogMessageHandler] [controller/92] [Main.cc@109] controller (64 bit): Version 6.3.2 (Build 903094f295d249) Copyright (c) 2018 Elasticsearch BV
	es     | [2019-01-24T10:03:11,083][INFO ][o.e.d.DiscoveryModule    ] [SeQUrzx] using discovery type [single-node]
	es     | [2019-01-24T10:03:12,264][INFO ][o.e.n.Node               ] [SeQUrzx] initialized
	es     | [2019-01-24T10:03:12,265][INFO ][o.e.n.Node               ] [SeQUrzx] starting ...
	es     | [2019-01-24T10:03:12,474][INFO ][o.e.t.TransportService   ] [SeQUrzx] publish_address {172.18.0.2:9300}, bound_addresses {[::]:9300}
	es     | [2019-01-24T10:03:12,501][WARN ][o.e.b.BootstrapChecks    ] [SeQUrzx] max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
	es     | [2019-01-24T10:03:12,567][INFO ][o.e.x.s.t.n.SecurityNetty4HttpServerTransport] [SeQUrzx] publish_address {172.18.0.2:9200}, bound_addresses {[::]:9200}
	es     | [2019-01-24T10:03:12,568][INFO ][o.e.n.Node               ] [SeQUrzx] started
	es     | [2019-01-24T10:03:12,698][WARN ][o.e.x.s.a.s.m.NativeRoleMappingStore] [SeQUrzx] Failed to clear cache for realms [[]]
	es     | [2019-01-24T10:03:12,816][INFO ][o.e.g.GatewayService     ] [SeQUrzx] recovered [0] indices into cluster_state
	es     | [2019-01-24T10:03:13,038][INFO ][o.e.c.m.MetaDataIndexTemplateService] [SeQUrzx] adding template [.triggered_watches] for index patterns [.triggered_watches*]
	es     | [2019-01-24T10:03:13,069][INFO ][o.e.c.m.MetaDataIndexTemplateService] [SeQUrzx] adding template [.watches] for index patterns [.watches*]
	es     | [2019-01-24T10:03:13,153][INFO ][o.e.c.m.MetaDataIndexTemplateService] [SeQUrzx] adding template [.watch-history-7] for index patterns [.watcher-history-7*]
	es     | [2019-01-24T10:03:13,239][INFO ][o.e.c.m.MetaDataIndexTemplateService] [SeQUrzx] adding template [.monitoring-logstash] for index patterns [.monitoring-logstash-6-*]
	es     | [2019-01-24T10:03:13,417][INFO ][o.e.c.m.MetaDataIndexTemplateService] [SeQUrzx] adding template [.monitoring-es] for index patterns [.monitoring-es-6-*]
	es     | [2019-01-24T10:03:13,456][INFO ][o.e.c.m.MetaDataIndexTemplateService] [SeQUrzx] adding template [.monitoring-alerts] for index patterns [.monitoring-alerts-6]
	es     | [2019-01-24T10:03:13,500][INFO ][o.e.c.m.MetaDataIndexTemplateService] [SeQUrzx] adding template [.monitoring-beats] for index patterns [.monitoring-beats-6-*]
	es     | [2019-01-24T10:03:13,537][INFO ][o.e.c.m.MetaDataIndexTemplateService] [SeQUrzx] adding template [.monitoring-kibana] for index patterns [.monitoring-kibana-6-*]
	es     | [2019-01-24T10:03:13,611][INFO ][o.e.l.LicenseService     ] [SeQUrzx] license [5701f0fd-0b32-434f-9012-d6bf97b9cf89] mode [basic] - valid
	es     | [2019-01-24T10:03:17,066][INFO ][o.e.c.m.MetaDataCreateIndexService] [SeQUrzx] [sfdata] creating index, cause [auto(bulk api)], templates [], shards [5]/[1], mappings []
	es     | [2019-01-24T10:03:17,587][INFO ][o.e.c.m.MetaDataMappingService] [SeQUrzx] [sfdata/rt5RjW3OTR6J59uCWVCoYQ] create_mapping [truck]
	es     | [2019-01-24T10:03:17,727][INFO ][o.e.c.m.MetaDataMappingService] [SeQUrzx] [sfdata/rt5RjW3OTR6J59uCWVCoYQ] update_mapping [truck]
	es     | [2019-01-24T10:03:17,785][INFO ][o.e.c.m.MetaDataMappingService] [SeQUrzx] [sfdata/rt5RjW3OTR6J59uCWVCoYQ] update_mapping [truck]
	es     | [2019-01-24T10:03:18,356][INFO ][o.e.c.m.MetaDataMappingService] [SeQUrzx] [sfdata/rt5RjW3OTR6J59uCWVCoYQ] update_mapping [truck]
	es     | [2019-01-24T10:03:18,563][INFO ][o.e.c.m.MetaDataMappingService] [SeQUrzx] [sfdata/rt5RjW3OTR6J59uCWVCoYQ] update_mapping [truck]
	web_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
	Gracefully stopping... (press Ctrl+C again to force)
	Stopping foodtrucks_web_1 ... done
	Stopping es               ... done
	
	$ sudo docker network ls   # only default docker networks
	NETWORK ID          NAME                DRIVER              SCOPE
	aa71d2892122        bridge              bridge              local
	09a4096c7d69        host                host                local
	baf3cfdf732b        none                null                local
	
	$ sudo docker-compose up -d
	Creating network "foodtrucks_default" with the default driver
	Creating volume "foodtrucks_esdata1" with local driver
	Creating es ... done
	Creating foodtrucks_web_1 ... done

	$ sudo docker-compose ps
	      Name                    Command               State                Ports              
	--------------------------------------------------------------------------------------------
	es                 /usr/local/bin/docker-entr ...   Up      0.0.0.0:9200->9200/tcp, 9300/tcp
	foodtrucks_web_1   python app.py                    Up      0.0.0.0:5000->5000/tcp          

	$ sudo docker-compose down -v
	Stopping foodtrucks_web_1 ... done
	Stopping es               ... done
	Removing foodtrucks_web_1 ... done
	Removing es               ... done
	Removing network foodtrucks_default
	Removing volume foodtrucks_esdata1
	
So basic create, deletion works, let's dig a little deeper.
::
	
	$ sudo docker-compose up -d
	Creating network "foodtrucks_default" with the default driver
	Creating volume "foodtrucks_esdata1" with local driver
	Creating es ... done
	Creating foodtrucks_web_1 ... done
	
	$ sudo docker ps
	CONTAINER ID        IMAGE                                                 COMMAND                  CREATED             STATUS              PORTS                              NAMES
	058a65ab3666        prakhar1989/foodtrucks-web                            "python app.py"          6 minutes ago       Up 6 minutes        0.0.0.0:5000->5000/tcp             foodtrucks_web_1
	f753db91d1cb        docker.elastic.co/elasticsearch/elasticsearch:6.3.2   "/usr/local/bin/do..."   6 minutes ago       Up 6 minutes        0.0.0.0:9200->9200/tcp, 9300/tcp   es

	[gcollis@neo FoodTrucks]$ sudo docker network ls
	NETWORK ID          NAME                 DRIVER              SCOPE
	aa71d2892122        bridge               bridge              local
	9750b16baa88        foodtrucks_default   bridge              local
	09a4096c7d69        host                 host                local
	baf3cfdf732b        none                 null                local
	
	$ sudo docker network inspect foodtrucks_default
	[
	    {
	        "Name": "foodtrucks_default",
	        "Id": "9750b16baa88d35d9a613526bb164b9c6c87160e26c9a2c85df26769f6a02b78",
	        "Created": "2019-01-24T11:09:51.061011438+01:00",
	        "Scope": "local",
	        "Driver": "bridge",
	        "EnableIPv6": false,
	        "IPAM": {
	            "Driver": "default",
	            "Options": null,
	            "Config": [
	                {
	                    "Subnet": "172.18.0.0/16",
	                    "Gateway": "172.18.0.1"
	                }
	            ]
	        },
	        "Internal": false,
	        "Attachable": true,
	        "Containers": {
	            "058a65ab36662d049a88b2f23b889972ddf87f0c7c3b0e5c9e227bc29a5b3c0b": {
	                "Name": "foodtrucks_web_1",
	                "EndpointID": "b83a4cbbe78698fbcfe90b2221f7287ceaea12d566ab81a072d337823cf14a7c",
	                "MacAddress": "02:42:ac:12:00:03",
	                "IPv4Address": "172.18.0.3/16",
	                "IPv6Address": ""
	            },
	            "f753db91d1cb084464c6b0b80c400641e6a0d747d7d00907ef2feaaf8c711136": {
	                "Name": "es",
	                "EndpointID": "8f8840837c9b0d9c0458cd32878e2c028d2124242bea806e4ddaa538ca1b2e9f",
	                "MacAddress": "02:42:ac:12:00:02",
	                "IPv4Address": "172.18.0.2/16",
	                "IPv6Address": ""
	            }
	        },
	        "Options": {},
	        "Labels": {
	            "com.docker.compose.network": "default",
	            "com.docker.compose.project": "foodtrucks"
	        }
	    }
	]
	
Development Workflow
--------------------

::

	$ sudo docker ps
	CONTAINER ID        IMAGE                                                 COMMAND                  CREATED             STATUS              PORTS                              NAMES
	058a65ab3666        prakhar1989/foodtrucks-web                            "python app.py"          12 minutes ago      Up 12 minutes       0.0.0.0:5000->5000/tcp             foodtrucks_web_1
	f753db91d1cb        docker.elastic.co/elasticsearch/elasticsearch:6.3.2   "/usr/local/bin/do..."   12 minutes ago      Up 12 minutes       0.0.0.0:9200->9200/tcp, 9300/tcp   es
	
	$ curl -I 0.0.0.0:5000/hello  # fails, flask-app/app.py has no "@app.route('/hello')"
	HTTP/1.0 404 NOT FOUND
	Content-Type: text/html
	Content-Length: 233
	Server: Werkzeug/0.11.2 Python/2.7.15rc1
	Date: Thu, 24 Jan 2019 10:23:23 GMT
	
	$ curl -I 0.0.0.0:5000/debug  # works, flask-app/app.py has "@app.route('/debug')"
	HTTP/1.0 200 OK
	Content-Type: application/json
	Content-Length: 104
	Server: Werkzeug/0.11.2 Python/2.7.15rc1
	Date: Thu, 24 Jan 2019 10:29:12 GMT

Now let's add `hello` so `flask-app/app.py`::

	@app.route('/')
	def index():
	  return render_template("index.html")
	
	# add a new hello route
	@app.route('/hello')
	def hello():
	  return "hello world!"

But if we try again, it will still fail, because we are still using `image: prakhar1989/foodtrucks-web`::
	
	# While local app.py has been updated, the container one hasn't
	$ sudo docker-compose run web bash
	Starting es ... done
	root@bceaa248f333:/opt/flask-app# ls
	app.py  package-lock.json  package.json  requirements.txt  static  templates  webpack.config.js
	root@bceaa248f333:/opt/flask-app# grep hello app.py
	root@bceaa248f333:/opt/flask-app# exit


So rather than run the 'web' container, let's use the local one and use `debug` as well::

	$ cat docker-compose.yml 
	version: "3"
	services:
	  es:
	    image: docker.elastic.co/elasticsearch/elasticsearch:6.3.2
	    container_name: es
	    environment:
	      - discovery.type=single-node
	    ports:
	      - 9200:9200
	    volumes:
	      - esdata1:/usr/share/elasticsearch/data
	  web:
	    build: . # replacing image: prakhar1989/foodtrucks-web
	    command: python app.py
	    environment:
	      - DEBUG=True  # add an environment variable for flask
	    depends_on:
	      - es
	    ports:
	      - 5000:5000
	    volumes:
	      - ./flask-app:/opt/flask-app
	volumes:
	    esdata1:
	      driver: local

When specifying `environment` in teh `web` section the application does not work when started as a daemon?::

	$ sudo docker-compose up -d
	$ sudo netstat -tlpn | grep 5000
	tcp6       0      0 :::5000                 :::*                    LISTEN      17166/docker-proxy- 
	
	$ curl -I 0.0.0.0:5000/debug
	curl: (56) Recv failure: Connection reset by peer
	$ curl -I 0.0.0.0:5000/hello
	curl: (56) Recv failure: Connection reset by peer
	$ curl -I 0.0.0.0:5000/hello
	$ sudo docker-compose down -v
	Stopping foodtrucks_web_1 ... done
	Stopping es               ... done
	Removing foodtrucks_web_1 ... done
	Removing es               ... done
	Removing network foodtrucks_default
	Removing volume foodtrucks_esdata1

Staring in the foreground `sudo docker-compose up` works.

Removing `enviroment` section, as show, then the applications works.::

	extract from "docker-compose.yml"
	  web:
	    build: . # replacing image: prakhar1989/foodtrucks-web
	    command: python app.py
	    depends_on:
	      - es
	    ports:
	      - 5000:5000
	    volumes:
	      - ./flask-app:/opt/flask-app

	$ sudo docker-compose up -d
	Creating network "foodtrucks_default" with the default driver
	Creating volume "foodtrucks_esdata1" with local driver
	Creating es ... done
	Creating foodtrucks_web_1 ... done
	
	$ curl -I 0.0.0.0:5000/debug
	HTTP/1.0 200 OK
	Content-Type: application/json
	Content-Length: 104
	Server: Werkzeug/0.11.2 Python/2.7.15rc1
	Date: Wed, 30 Jan 2019 17:52:25 GMT
	
	$ curl -I 0.0.0.0:5000/hello
	HTTP/1.0 200 OK
	Content-Type: text/html; charset=utf-8
	Content-Length: 12
	Server: Werkzeug/0.11.2 Python/2.7.15rc1
	Date: Wed, 30 Jan 2019 17:52:40 GMT
	

	$ sudo docker-compose down -v
	Stopping foodtrucks_web_1 ... done
	Stopping es               ... done
	Removing foodtrucks_web_1 ... done
	Removing es               ... done
	Removing network foodtrucks_default
	Removing volume foodtrucks_esdata1
	$ sudo docker-compose up -d # will list build steps, on first run (not shown)
	Creating network "foodtrucks_default" with the default driver
	Creating volume "foodtrucks_esdata1" with local driver
	Creating es ... done
	Creating foodtrucks_web_1 ... done


AWS Elastic Container Service
=============================

* `Installing the Amazon ECS CLI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html>`_

Download and install ECS CLI::

	$ sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
	$ echo "$(curl -s https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest.md5) /usr/local/bin/ecs-cli" | md5sum -c -
	/usr/local/bin/ecs-cli: OK

Setup GPG keys::

	$ gpg --version
	$ sudo gpg --keyserver hkp://keys.gnupg.net --recv BCE9D9A42D51784F
	gpg: requesting key 2D51784F from hkp server keys.gnupg.net
	gpg: key 2D51784F: public key "Amazon ECS <ecs-security@amazon.com>" imported
	gpg: no ultimately trusted keys found
	gpg: Total number processed: 1
	gpg:               imported: 1  (RSA: 1)

	$ curl -o ecs-cli.asc https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest.asc
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	100   821  100   821    0     0   1225      0 --:--:-- --:--:-- --:--:--  1223
	$ sudo gpg --verify ecs-cli.asc /usr/local/bin/ecs-cli
	gpg: Signature made Thu 13 Dec 2018 08:02:11 PM CET using RSA key ID ADAF8B8E
	gpg: Good signature from "Amazon ECS <ecs-security@amazon.com>"
	gpg: WARNING: This key is not certified with a trusted signature!
	gpg:          There is no indication that the signature belongs to the owner.
	Primary key fingerprint: F34C 3DDA E729 26B0 79BE  AEC6 BCE9 D9A4 2D51 784F
	     Subkey fingerprint: EB3D F841 E2C9 212A 2BD4  2232 DE3C BD61 ADAF 8B8E

Make the binary executable::

	$ ls -al /usr/local/bin/ecs-cli
	-rw-r--r-- 1 root root 28327232 Jan 30 19:46 /usr/local/bin/ecs-cli
	$ sudo chmod +x /usr/local/bin/ecs-cli
	$ ls -al /usr/local/bin/ecs-cli
	-rwxr-xr-x 1 root root 28327232 Jan 30 19:46 /usr/local/bin/ecs-cli
	
	$ ecs-cli --version
	ecs-cli version 1.12.1 (e70f1b1)

Using the `EC2 Console <https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:sort=keyName>`_ create a key-pair.
::

	$ ecs-cli configure --region us-east-1 --cluster foodtrucks
	INFO[0000] Saved ECS CLI cluster configuration default. 
	$ ecs-cli up --keypair ecs --capability-iam --size 2 --instance-type t2.micro
	FATA[0040] Error executing 'up': NoCredentialProviders: no valid providers in chain. Deprecated.
		For verbose messaging see aws.Config.CredentialsChainVerboseErrors 
		
	$ sudo dnf install awscli # install the aws command-line
	$ aws configure get region
	$
	
	$ sudo ecs-cli compose --file aws-compose.yml up
	WARN[0000] Skipping unsupported YAML option for service...  option name=networks service name=es
	WARN[0000] Skipping unsupported YAML option for service...  option name=networks service name=web
	ERRO[0020] Error listing tasks                           error="NoCredentialProviders: no valid providers in chain. Deprecated.\n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" request="{\n  Cluster: \"foodtrucks\",\n  DesiredStatus: \"RUNNING\",\n  Family: \"FoodTrucks\"\n}"
	FATA[0020] NoCredentialProviders: no valid providers in chain. Deprecated.
		For verbose messaging see aws.Config.CredentialsChainVerboseErrors 

* Added `AWS Elastic Container Service - instructions do not work?  <https://github.com/prakhar1989/docker-curriculum/issues/163>`_ to the GutHub issues.

