:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/projects/docker-or-podman.rst

================
Docker or Podman
================

* Which is better for containerization development
* Comparison using Windows 11 Home edition (no Hyper-V) both WSLv2 based

#######
Summary
#######

**************
Docker Desktop
**************

* Upsides
    * polished bundled product, docker + desktop
    * infrequent updates
    * leading-edge container (docker) technology
    * 'compose' for multi-container
* Downsides
    * cannot run kubernetes pods
    * kubernetes-style ``secrets`` are not supported (docker swarm only)
    * kubernetes-style ``configMaps`` are not supported (docker swarm only)
    * primarily windows, but available on Linux and MacOS (brew)
    * slow start up


*************************
Podman and Podman Desktop
*************************

* Upsides
    * supports containers and kubernetes manifests (pod, service, deployment)
    * kubernetes-style ``secrets`` are supported
    * kubernetes-style ``configMaps`` are supported
    * primarily Linux, but well supported on Windows and MacOS (brew)
    * importing via ``docker compose`` is supported, not sure advanced features will work
    * exporting of containers to ``pod``, ``deployment`` and ``service`` manifests
* Downsides
    * separate products, podman, podman-desktop
    * frequent updates, active community driven development
    * compose supported natively on Linux and MacOS, Python script on windows

************
Installation
************

``Windows 11 Home edition`` does not support `Hyper-V <https://techcommunity.microsoft.com/t5/educator-developer-blog/step-by-step-enabling-hyper-v-for-use-on-windows-11/ba-p/3745905>`_ so `WSL <https://learn.microsoft.com/en-us/windows/wsl/about>`_ is used.

Essentially this requires:

* checking the platform is virtualization capable
* enabling the additional windows features
* installing WSL 2, typically from the `Microsoft Store <https://apps.microsoft.com/>`_

Follow cheatsheet `WSL - Windows Subsystem for Linux <https://nonbleedingedge.com/cheatsheets/windows-tricks.html#wsl-windows-subsystem-for-linux>`_

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


For ``Podman`` you also need to install ``Podman Desktop``

* `Podman for Windows <https://github.com/containers/podman/blob/main/docs/tutorials/podman-for-windows.md>`_
* `Installing Podman Desktop and Podman on Windows <https://podman-desktop.io/docs/installation/windows-install>`_
* `Github - sjfke - Windows Platform Setup <https://github.com/sjfke/tomcat-containers/blob/main/wharf/PODMAN.md>`_

.. code-block:: console

    $ wsl --list
    Windows Subsystem for Linux Distributions:
    Ubuntu (Default)
    podman-machine-default
    AlmaLinuxOS-9

*******
Testing
*******

An example from CodeJava, `JSP Servlet JDBC MySQL C.R.U.D Example <https://www.codejava.net/coding/jsp-servlet-jdbc-mysql-create-read-update-delete-crud-example>`_ was used the details of
which are on GitHub `sjfke - tomcat containers <https://github.com/sjfke/tomcat-containers>`_

Separate containers will be used for:

* ``bookstore`` the tomcat application
* ``bookstoredb`` the database
* ``adminer`` the web interface used for database administration

The containers can be deployed using

* `Docker <https://www.docker.com/>`_ and `docker compose <https://docs.docker.com/compose/compose-file/>`_
* `Podman <https://podman.io/>`_ and the Python script `podman-compose <https://github.com/containers/podman-compose>`_
* `Kubernetes Pods <https://kubernetes.io/docs/concepts/workloads/pods/>`_ with `podman kube play <https://docs.podman.io/en/latest/markdown/podman-kube-play.1.html>`_

This is aim to provide a multi container example that was integrated with an IDE, such as ``Eclipse``

The `Build README <https://github.com/sjfke/tomcat-containers/blob/main/wharf/BUILD.md>`_ details the steps taken to build, test and modernize the ``Bookstore`` application.

Supplementary README's are used to focus on specific topics and to avoid *writing an epic*.

* `BUILD.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/BUILD.md>`_ - Setup and build within Eclipse, plus corrections to the ``CodeJava Tutorial``
* `CONTAINERS.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/CONTAINERS.md>`_ - How to build and deploy ``Bookstore`` container image to Quay.IO and DockerHub.
* `DOCKER.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/DOCKER.md>`_ - How to build and test ``Bookstore`` using Docker, Docker Compose
* `ECLIPSE.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/ECLIPSE.md>`_ - Eclipse setup
* `MARIADB.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/MARIADB.md>`_ - Install ``MariaDB`` container
* `MAVEN.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/MAVEN.md>`_ - Installing ``maven`` and configuring the version included with ``Eclipse``
* `TOMCAT.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/TOMCAT.md>`_ - How to setup standalone Tomcat to test ``Bookstore`` maven builds
* `PODMAN-KUBE.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/PODMAN-KUBE.md>`_ - How to create and use ``podman play kube`` to test ``Bookstore``
* `PODMAN.md <https://github.com/sjfke/tomcat-containers/blob/main/wharf/PODMAN.md>`_ - How to test ``Bookstore`` using ``podman kube play`` and ``podman-compose.py``

**************
Recommendation
**************

If you want the latest, greatest, Docker technology, and are happy to work with ``docker compose`` for multi-container development, then Docker is the better choice.
It lacks direct Kubernetes support, so forced to use ``Kind``, ``MiniKube``, ``Kubernetes`` and develop and maintain separate files.

If you want to work with Kubernetes for development, testing and deployment then ``Podman`` and ``Podman Desktop`` is the better choice.
Additionally commands like ``podman generate`` permit creating template Kubernetes manifest files from deployed containers,
and ``podman compose`` (executable or Python script) allows your existing ``docker compose`` files to be used.

Personally I found ``podman`` to be easy to use, the command syntax is a bit more consistent, and on the ``Windows 11 Home edition``
laptops used for testing, ``podman`` was quicker to start, deploy and at running containers but noticeably slower when building containers.

Overall I prefer to work with ``Podman`` and ``Podman Desktop`` and avoid using ``Docker compose``

**********
References
**********

* `Docker Reference <https://docs.docker.com/reference/>`_
* `Docker Compose overview <https://docs.docker.com/compose/>`_
* `Podman Commands <https://docs.podman.io/en/latest/Commands.html>`_
* `Github podman-compose <https://github.com/containers/podman-compose>`_
* `podman play kube <https://docs.podman.io/en/v4.2/markdown/podman-play-kube.1.html>`_
* `Podman Releases <https://github.com/containers/podman/releases>`_
* `Openshift API index <https://docs.openshift.com/container-platform/4.15/rest_api/index.html>`_ - pod, deployment etc. specifications
* `Kubernetes manifests <https://loft.sh/blog/kubernetes-manifests-everything-you-need-to-know/>`_
* `Docker Swarm vs Kubernetes <https://phoenixnap.com/blog/kubernetes-vs-docker-swarm>`_
* `Kubernetes Manifests <https://loft.sh/blog/kubernetes-manifests-everything-you-need-to-know/>`_
* `Swarm mode overview <https://docs.docker.com/engine/swarm/>`_ - requires multiple hosts or VM's)
* `Docker SDK for Python <https://docker-py.readthedocs.io/en/stable/>`_
* `Podman Python SDK <https://podman-py.readthedocs.io/en/latest/>`_



