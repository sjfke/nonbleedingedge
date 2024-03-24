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

.. code-block:: console

    $ wsl --list
    Windows Subsystem for Linux Distributions:
    Ubuntu (Default)
    podman-machine-default
    AlmaLinuxOS-9

*******
Testing
*******



