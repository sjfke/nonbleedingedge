:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/projects/docker-or-podman.rst

================
Docker or Podman
================

* Which is better for containerization development?
* Comparison using Windows 11 Home edition (no Hyper-V) both WSLv2 based

#######
Summary
#######

**************
Docker Desktop
**************

* Upsides
    * polished bundled product, ``Docker Desktop``
    * infrequent updates
    * leading-edge container (docker) technology
    * ``docker compose`` for multi-container
    * Command line completions ``Bash``, ``Zsh``
* Downsides
    * cannot run kubernetes pods
    * kubernetes-style ``secrets`` are not supported, ``docker swarm`` *only*
    * kubernetes-style ``configMaps`` are not supported, ``docker swarm`` *only*
    * primarily Windows, but available on Linux and MacOS (brew)
    * application slow to start and upgrade
    * releases ``v4.29``, ``v4.30`` have issues, try manually starting service ``Docker Desktop Service``


*************************
Podman and Podman Desktop
*************************

* Upsides
    * supports containers and kubernetes manifests (*pod*, *service*, *deployment*)
    * supports kubernetes-style ``secrets``, ``podman secret``
    * supports kubernetes-style ``configMaps``, ``podman kube play``
    * primarily Linux, but well supported on Windows and MacOS (brew)
    * supports importing basic ``docker compose`` using ``podman compose``
    * exporting of *containers* to ``pod``, ``deployment`` and ``service`` manifests
    * Command line completions ``Bash``, ``Zsh``, ``Fish``, ``PowerShell``
* Downsides
    * separate products, ``podman``, ``podman-desktop``
    * frequent updates, `active community <https://github.com/containers/>`_ driven *development* and *support*
    * ``podman-compose`` supported natively on Linux and MacOS, Python script on Windows
    * ``MacOS`` ``podman v5`` is only supported on ``macOS 13 (Ventura)`` or later
    * ``MacOS`` ``podman v4`` download and install ``dmg`` from `podman releases <https://github.com/containers/podman/releases>`_
    * ``Windows`` ``podman v4`` and ``podman v5`` use different a ``podman-machine`` version

************
Installation
************

``Windows 11 Home edition`` does not support `Hyper-V <https://techcommunity.microsoft.com/t5/educator-developer-blog/step-by-step-enabling-hyper-v-for-use-on-windows-11/ba-p/3745905>`_
so `WSL <https://learn.microsoft.com/en-us/windows/wsl/about>`_ is used.

WSL
===

Essentially this requires:

1. checking the platform is virtualization capable
2. enabling the additional Windows features
3. installing WSL 2, typically from the `Microsoft Store <https://apps.microsoft.com/>`_

Follow cheatsheet `WSL - Windows Subsystem for Linux <https://nonbleedingedge.com/cheatsheets/windows-tricks.html#wsl-windows-subsystem-for-linux>`_

Docker Desktop
==============

Installing ``Docker Desktop`` is very simple follow,
`Install Docker Desktop on Windows <https://docs.docker.com/desktop/install/windows-install/>`_

.. note::

    **Docker Desktop terms**

    Commercial use of Docker Desktop in larger enterprises (more than 250 employees OR more
    than $10 million USD in annual revenue) requires a paid subscription

.. code-block:: console

    $ wsl --list
    Windows Subsystem for Linux Distributions:
    Ubuntu-22.04 (Default)
    docker-desktop-data
    docker-desktop
    AlmaLinuxOS-9

Podman and Podman Desktop
=========================

To be equivalent to ``Docker Desktop`` both ``Podman`` and ``Podman Desktop`` need to be installed

* `Podman for Windows <https://github.com/containers/podman/blob/main/docs/tutorials/podman-for-windows.md>`_
* `Installing Podman Desktop and Podman on Windows <https://podman-desktop.io/docs/installation/windows-install>`_
* `Setup of Podman for tomcat-containers <https://github.com/sjfke/tomcat-containers/blob/main/wharf/PODMAN.md>`_

.. note::

    On Windows ``Podman v5`` upgrade requires stopping and deleting the ``podman-default-machine``

.. code-block:: console

    $ wsl --list
    Windows Subsystem for Linux Distributions:
    Ubuntu (Default)
    podman-machine-default
    AlmaLinuxOS-9

*******
Testing
*******

A modified example from `CodeJava <https://codejava.net/all-tutorials>`_, `JSP Servlet JDBC MySQL C.R.U.D Example <https://www.codejava.net/coding/jsp-servlet-jdbc-mysql-create-read-update-delete-crud-example>`_ is used the details of
which are on GitHub `sjfke - tomcat containers <https://github.com/sjfke/tomcat-containers>`_

Separate containers are used for:

* ``bookstore`` the tomcat application
* ``bookstoredb`` the MariaDB database
* ``adminer`` the web interface used for database administration

and additionally

* ``bookstoredb`` uses a ``volume`` for persistent storage, "*jsp_bookstoredata*"
* all three containers use a dedicated ``network``, "*tomcat-containers_jspnet*"

The containers are deployed using

* `Docker <https://www.docker.com/>`_ and `docker compose <https://docs.docker.com/compose/compose-file/>`_
* `Podman <https://podman.io/>`_ and the Python script `podman-compose <https://github.com/containers/podman-compose>`_
* `Kubernetes Pods <https://kubernetes.io/docs/concepts/workloads/pods/>`_ with `podman kube play <https://docs.podman.io/en/latest/markdown/podman-kube-play.1.html>`_

Like the `CodeJava example <https://www.codejava.net/coding/jsp-servlet-jdbc-mysql-create-read-update-delete-crud-example>`_, the
development uses `Eclipse <https://www.eclipse.org/downloads/>`_ and the
`Build README <https://github.com/sjfke/tomcat-containers/blob/main/wharf/BUILD.md>`_ details the steps taken to build,
test and modernize the ``Bookstore`` application.

Typical Docker Session
======================

.. code-block:: pwsh-session

    # Volumes
    PS> docker volume create jsp_bookstoredata

    # Initial build and deploy
    PS> mvn -f .\Bookstore\pom.xml clean package
    PS> docker compose -f .\compose.yaml build bookstore
    PS> docker compose -f .\compose.yaml up -d
    PS> start "http://localhost:8080/Bookstore"

    # Develop, build and test (wash repeat) cycle
    PS> docker compose -f .\compose.yaml down bookstore
    PS> mvn -f .\Bookstore\pom.xml clean package
    PS> docker compose -f .\compose.yaml build bookstore
    PS> docker compose -f .\compose.yaml up -d bookstore

    # Clean-up
    PS> docker compose -f .\compose.yaml down
    PS> docker volume rm jsp_bookstoredata


    # Helpful
    PS> docker compose ps --all
    PS> docker volume ls
    PS> docker network ls
    PS> docker image ls --all
    PS> docker image ls | select-string bookstore   # get docker-compose 'name' (tomcat-containers-bookstore)
    PS> docker image rm tomcat-containers-bookstore # delete specific image
    PS> docker image prune                          # remove all 'dangling' images
    PS> docker image prune --all                    # remove 'ALL' images

Typical Podman Session
======================

.. code-block:: pwsh-session

    # Volumes, networks and secrets
    PS> podman volume create jsp_bookstoredata
    PS> podman network create jspnet
    PS> podman kube play secrets.yaml (or podman secret create)

    # Initial build and deploy
    PS> mvn -f .\Bookstore\pom.xml clean package
    PS> podman play kube --start --network jspnet .\adminer-pod.yaml
    PS> podman play kube --network jspnet .\bookstoredb-pod.yaml        # --start is default
    PS> podman play kube --network jspnet .\bookstore-pod.yaml
    PS> start "http://localhost:8080/Bookstore"

    # Develop, build and test (wash repeat) cycle
    PS> podman play kube --down .\bookstore-pod.yaml                    # --network optional
    PS> mvn -f .\Bookstore\pom.xml clean package
    PS> podman build --tag localhost/bookstore --squash -f .\Dockerfile
    PS> podman play kube --network jspnet .\bookstore-pod.yaml

    # Clean-up
    PS> podman play kube --down .\bookstore-pod.yaml
    PS> podman play kube --down .\adminer-pod.yaml
    PS> podman play kube --down .\bookstoredb-pod.yaml
    PS> podman network rm jspnet
    PS> podman volume rm jsp_bookstoredata

    # Helpful
    PS> podman volume ls
    PS> podman network ls
    PS> podman secret ls
    PS> podman image prune                  # remove all 'dangling' images
    PS> podman image rm localhost/bookstore # delete image by name
    PS> podman image rm ba3f9f9af813        # delete image by id (alias: podman rmi)

Github ``tomcat-containers`` Example
====================================

The `tomcat-containers Github repository <https://github.com/sjfke/tomcat-containers>`_ contains all the details of
the work done for this review.

In addition to main **README**, supplementary README's are used to focus on specific topics

* `BUILD.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/BUILD.md>`_ - Setup and build within Eclipse, plus corrections to the ``CodeJava Tutorial``
* `CONTAINERS.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/CONTAINERS.md>`_ - Build and deploy ``Bookstore`` container to `Quay.IO <https://quay.io/>`_ and `dockerhub <https://hub.docker.com/>`_
* `DOCKER.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/DOCKER.md>`_ - Build and test ``Bookstore`` using ``docker``, ``docker compose``
* `ECLIPSE.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/ECLIPSE.md>`_ - Eclipse setup
* `MARIADB.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/MARIADB.md>`_ - Install ``MariaDB`` container
* `MAVEN.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/MAVEN.md>`_ - Installing ``maven`` and configuring the version included with ``Eclipse``
* `TOMCAT.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/TOMCAT.md>`_ - Setup standalone Tomcat to test ``Bookstore`` maven builds
* `PODMAN-KUBE.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/PODMAN-KUBE.md>`_ - Create and use ``podman play kube`` to test ``Bookstore``
* `PODMAN.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/PODMAN.md>`_ - Test ``Bookstore`` using ``podman kube play`` and ``podman-compose.py``

**************
Recommendation
**************

If you want the latest, greatest, Docker technology, and are happy to work with ``docker compose`` for multi-container
*development* and *testing*, then ``Docker Desktop`` is the better choice. However, it lacks *Kubernetes-like* features,
so other technologies are needed to test *deployments*, such as `Kind <https://kind.sigs.k8s.io/>`_,
`minikube <https://minikube.sigs.k8s.io/docs/>`_, or
`Red Hat Openshift Local <https://developers.redhat.com/products/openshift-local/overview>`_
Also note ``Docker-Desktop`` may need to be `licensed <https://docs.docker.com/subscription/desktop-license/>`_

To work directly with *Kubernetes-like* features for *development*, *testing* and *deployment* then the combination of
`Podman <https://podman.io/>`_ and `Podman Desktop <https://podman-desktop.io/>`_ is the better choice.
Commands like ``podman generate`` permit creating Kubernetes manifest files from running containers, and
``podman compose`` (executable or Python script) allows your existing ``docker compose`` files to be used.
However, `active community <https://github.com/containers/>`_ development and support means frequent updates
may be needed to be latest stable release

On the ``Windows 11 Home edition`` laptops used for testing, ``podman`` was quicker to start, deploy and at running
containers, especially using ``podman kube play`` but appeared slower at building when the base container image was
not cached locally and had to be pulled.

Updates to ``Podman`` and ``Podman Desktop`` are much quicker to apply, but with ``podman`` in particular need to be done
more frequently to be on the latest stable release.

Personally I found ``podman`` to be a bit easier to learn and use because the command syntax is slightly more
consistent than ``docker``, and ``Podman Desktop`` while *less polished* than ``Docker-Desktop`` is more than adequate

Based on this investigation I now prefer to avoid ``docker compose`` and to work with ``Podman`` and ``Podman Desktop``
using ``podman kube play``. This way every phase of *development*, *testing* and *deployment* is using
*Kubernetes-like* features, and ``podman secret`` can be used to avoid **hard-coding passwords** in
*configuration files*, which tend to creep into your Git repositories! |:wink:|

**********
References
**********

* `Docker Reference <https://docs.docker.com/reference/>`_
* `Docker Compose overview <https://docs.docker.com/compose/>`_
* `Podman Commands <https://docs.podman.io/en/latest/Commands.html>`_
* `Github podman-compose <https://github.com/containers/podman-compose>`_
* `podman kube play <https://docs.podman.io/en/latest/markdown/podman-kube-play.1.html>`_
* `Podman Releases <https://github.com/containers/podman/releases>`_
* `Openshift API index <https://docs.openshift.com/container-platform/4.15/rest_api/index.html>`_ - pod, deployment etc. specifications
* `Kubernetes manifests <https://loft.sh/blog/kubernetes-manifests-everything-you-need-to-know/>`_
* `Compose file version 3 reference <https://docs.docker.com/compose/compose-file/compose-file-v3/>`_
* `Docker Swarm vs Kubernetes <https://phoenixnap.com/blog/kubernetes-vs-docker-swarm>`_
* `Kubernetes Manifests <https://loft.sh/blog/kubernetes-manifests-everything-you-need-to-know/>`_
* `Swarm mode overview <https://docs.docker.com/engine/swarm/>`_ - requires multiple hosts or VM's
* `Docker SDK for Python <https://docker-py.readthedocs.io/en/stable/>`_
* `Podman Python SDK <https://podman-py.readthedocs.io/en/latest/>`_



