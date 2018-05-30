**********************
Python Django Tutorial
**********************

Installing ``pipenv``
=====================

Setup pipenv::

	$ sudo pip install pipenv   # system-wide considered dangerous
	$ pip install --user pipenv # user-wide safer
	
	$ mkdir my project && cd myproject
	$ pipenv install requests
	$ cat > main.py <<EOT
	import requests
	response = requests.get('https://httpbin.org/ip')
	print('Your IP is {0}'.format(response.json()['origin']))
	EOT
	
	$ pipenv run python main.py # Alternative: $ pipenv shell; python main.py


Useful Links

* `Installing Python 3 on Linux <http://docs.python-guide.org/en/latest/starting/install3/linux/>`_
* `Pipenv & Virtual Environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref>`_
* `Basic Usage of Pipenv <https://docs.pipenv.org/basics/#general-recommendations-version-control>`_
* `Pipenv: Python Dev Workflow for Humans <https://docs.pipenv.org/>`_


Setting up Django project
=========================

Create project directory and install Django::

	$ mkdir django; cd django
	$ pipenv --three # for python3
	$ pipenv install django
	$ pipenv shell
	$ python -m django --version


Create the Django project::

	$ django-admin startproject mysite
	$ cd mysite 
	$ python manage.py runserver      # http://127.0.0.1:8000/
	$ python manage.py runserver 8080 # http://127.0.0.1:8080/
	
	# Get rid of warning
	$ vi +/ALLOWED mysite/settings.py 
	$ vi +/mystic/settings.py
	# ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.42']


Note on Fedora may need to open the port on the firewall::

	$ sudo firewall-cmd --add-port=8000/tcp # punch firewall hole for external access
	$ python manage.py runserver 0:8080     # http://<ext-ip>:8000/


Create the Django App (A Django project can have many apps)::

	$ python manage.py startapp polls
	$ cat > polls/views.py <<EOT
	from django.http import HttpResponse
	
	def index(request):
	    return HttpResponse("Hello, world. You're at the polls index.")
	EOT
	
	$ cat > polls/urls.py <<EOT
	from django.urls import path
	from . import views
	
	urlpatterns = [
	    path('', views.index, name='index'),
	]
	EOT
	
	$ cat mysite/urls.py <<EOT
	from django.contrib import admin
	from django.urls import include, path
	
	urlpatterns = [
	    path('polls/', include('polls.urls')),
	    path('admin/', admin.site.urls),
	]
	EOT
	 
	$ python manage.py runserver 0:8000    # http://<ext-ip>:8000/polls


Useful Links
============

* `Fedora 26: Firewall with Firewalld <https://www.hiroom2.com/2017/07/12/fedora-26-firewalld-en/>`_
* `Introduction to Sphinx <http://www.writethedocs.org/guide/tools/sphinx/>`_
* `reStructuredText Basics <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `Quick reStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
* `A ReStructuredText Primer <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_
* `HTML theming support <http://www.sphinx-doc.org/en/master/theming.html>`_

Tutorial Links
==============

* `Writing your first Django app <https://docs.djangoproject.com/en/2.0/intro>`_
* `Django 2.0 intro tutorial01 <https://docs.djangoproject.com/en/2.0/intro/tutorial01/>`_ *Done*
* `Django 2.0 intro tutorial03 <https://docs.djangoproject.com/en/2.0/intro/tutorial03/>`_ *Done*
* `Django 2.0 intro tutorial04 <https://docs.djangoproject.com/en/2.0/intro/tutorial04/>`_ *Done*
* `Django 2.0 intro tutorial05 <https://docs.djangoproject.com/en/2.0/intro/tutorial05/>`_ *Done*
* `Django 2.0 intro tutorial06 <https://docs.djangoproject.com/en/2.0/intro/tutorial06/>`_ *Done*
* `Django 2.0 intro tutorial07 <https://docs.djangoproject.com/en/2.0/intro/tutorial07/>`_ *Done*
* `Advanced tutorial: How to write reusable apps <https://docs.djangoproject.com/en/2.0/intro/reusable-apps/>`_ *ToDo*
* `What to read next <https://docs.djangoproject.com/en/2.0/intro/whatsnext/>`_ *ToDo*
* `Writing your first patch for Django <https://docs.djangoproject.com/en/2.0/intro/contributing/>`_ *ToDo*


Installing Databases
====================

Installing sqlite::

	$ sudo dnf install sqlite
	$ sqlite3 db.sqlite3
	sqlite> .schema
	sqlite> ^d


Installing MariaDB::

	$ sudo dnf install mariadb
	$ sudo dnf install mariadb-devel
	$ sudo dnf install mariadb-server
	$ sudo systemctl start mariadb.service

