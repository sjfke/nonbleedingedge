:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/daemontools.rst

**********************
Daemontools Cheatsheet
**********************

Installing ``daemontools``
==========================

Setup pipenv

.. code-block:: console

	$ sudo dnf install daemontools   # Fedora installation
	$ sudo brew install daemontools  # MacOS  installation

Useful Links

* `Installing Python 3 on Linux <http://docs.python-guide.org/en/latest/starting/install3/linux/>`_


Common commands
===============

.. code-block:: console

	$ sudo svstat /service/netsnmpd
	$ sudo svc -d /service/netsnmpd # terminate and leave down
	$ sudo svc -u /service/netsnmpd # bring-up (down service)
	$ sudo svc -t /service/netsnmpd # terminate and immediate restart
	$ sudo svc -h /service/netsnmpd # send HUP signal
	$ sudo svc -o /service/netsnmpd # run service once

What is managed by Daemontools
==============================

.. code-block:: console

	$ ls -al /service/netsnmpd/
	netsnmpd -> /home/y/var/daemontools/netsnmpd


