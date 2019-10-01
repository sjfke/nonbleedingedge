:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/brew.rst

*******************************
Subversion Cheatsheet
*******************************

Useful Links
============

* `Apache Subversion <https://subversion.apache.org/>`_
* `Version Control with Subversion <http://svnbook.red-bean.com/>`_
* `Subversion 1.6 <http://svnbook.red-bean.com/en/1.6/index.html>`_
* `Subversion 1.7 <http://svnbook.red-bean.com/en/1.7/index.html>`_
* `Subversion Nightly build 1.8 <http://svnbook.red-bean.com/nightly/en/index.html>`_

Which version is installed?
===========================

::

	geoff@morph$ svn --version --quiet
	1.6.9

Repository Access Methods
=========================

::

	geoff@morph$ svn checkout http://svn.example.com:9834/repos (WebDAV protocol)
	geoff@morph$ svn checkout https://svn.example.com:9834/repos (SSL WebDAV protocol)
	geoff@morph$ svn checkout file:///var/svn/repos (on local disk)
	geoff@morph$ svn checkout file://localhost/var/svn/repos (on local disk)
	c:\> svn checkout file:///X:/var/svn/repos (on local drive X)
	c:\> svn checkout file:///X|/var/svn/repos (on local drive X)
	geoff@morph$ svn checkout svn://svn.example.com/repos (svnserve port 3690)
	geoff@morph$ svn checkout svn+ssh://svn.example.com/repos (svnserve + ssh tunnel port 22)

SVN Help
========

::

	geoff@morph$ svn help
	geoff@morph$ svn help import

Repository Creation
===================

::

 
	# - you need to checkout into a different location (like CVS)
	geoff@morph$ svnadmin create /var/sv/newrepos
	geoff@morph$ svn import myfile file:///var/svn/trunk/newrepos/some/project -m "initial import"
	geoff@morph$ svn list file:///var/svn/trunk/newrepos/some/project
	geoff@morph$ cd somedir; svn checkout file:///var/svn/newrepos/trunk/some/project

Recommended Repository Layout
=============================

::

	geoff@morph$ svn list file:///var/svn/newrepos
	/trunk
	/branches
	/tags

Basic Work Cycle
================

::

	# update your working copy
	geoff@morph$ svn update # CAUTION will update your local copy
	geoff@morph$ svn status # to get an overview of changes

	# make changes
	geoff@morph$ svn add
	geoff@morph$ svn delete
	geoff@morph$ svn copy 
	geoff@morph$ svn move 

	# examine your changes
	geoff@morph$ svn status
	geoff@morph$ svn diff

	# undo some changes
	geoff@morph$ svn revert

	# resolve conflicts
	geoff@morph$ svn update
	geoff@morph$ svn resolve

	# commit your changes
	geoff@morph$ svn commit


Status prefixes; ``snv status``
===============================

::

	# column 1 = files, column = 2 properties
	geoff@morph$ svn status [$ svn status --verbose (-v) # for more details]
	A item # scheduled for addition
	C item # is in a state of conflict (updates blocked, until resolved)
	D item # scheduled for deletion
	M item # file contents modified
	 M prop # property has been changed ($svn diff item # to see what) 
  
History Commands
================

::

	geoff@morph$ svn log  # log information
	geoff@morph$ svn diff # line-level details
	geoff@morph$ svn cat  # cat version in repository
	geoff@morph$ svn list # display files in a directory
	
	geoff@morph$ svn log foo.c                               # show log history of foo.c
	geoff@morph$ svn log http://foo.com/svn/trunk/code/foo.c # show log history of foo.c
	geoff@morph$ svn log -r 5:19                             # shows logs 5 thru 19 (chronological order)
	geoff@morph$ svn log -r 19:5                             # shows logs 19 thru 5 (reversed order)
	geoff@morph$ svn log -r 8 -v                             # shows verbose log for revision 8
	geoff@morph$ svn log --quiet --verbose                   # show only changed files

Ignoring files and directories
==============================

::

	geoff@morph$ svn propedit svn:ignore . # Opens an editor (SVN_EDITOR, EDITOR)
	geoff@morph$ svn propget svn:ignore .  # So you can see the properties
	geoff@morph$ svn status --no-ignore    # You should see an 'I' next to the ignored files
	geoff@morph$ svn propdel svn:ignore .  # Delete the svn:ignore property
	
	# For Maven project
	geoff@morph$ svn propset svn:ignore '*' target # Ignore everything in target (cannot hide directory)
	geoff@morph$ svn propget svn:ignore target     # List svn:ignore properties
	geoff@morph$ svn status --no-ignore            # You should see an 'I' next to the ignored files

Revision Keywords / Dates
=========================

::

	HEAD                        # latest revision in repository ("youngest")
	BASE                        # revision number of item working copy
	COMMITTED                   # most recent prior to, or equal to BASE
	PREV                        # COMMITTED-1
	{2006-02-17}                # version at 2006-02-16_00:00:00
	{15:30}                     # version at 15:30
	{"2006-02-17 15:30"}
	{"2006-02-17 15:30 +2:30"}
	{2006-11-20}:{2006-11-29}
  
Subversion Properties
=====================

::

	# meta-data: key(ASCII) value (arbitrary value)
	# "svn:" reserved subversion properties
	# versioned like files, but not searchable, can be on files and/or directories
	$ svn propset copyright '(c) 2006 Red-Bean Software' calc/foo.c
	$ svn propedit copyright calc/foo.c # invoke editor (${SVN_EDITOR}, ${VISUAL}, ${EDITOR} + svn options)
	$ svn proplist [-v] calc/foo.c
	$ svn propdel copyright calc/foo.c

Subversion Unversioned Properties 
---------------------------------

::

	# By default disabled (considered dangerous)
	$ svn propset svn:log 'updated log message' -r11 -revprop
	$ svn propset svn:log 'updated log message' -r11 -revprop http://svn.example.com/repos/project
	$ svnadmin setlog repos/project 'updates log message' -r 11
  
Automatic Property Setting
--------------------------

::

  svn:executable (add/import) # no exectable bit on Windows
  svn:mime-type  (add/import) # is it text or not!

Common Useful Properties
------------------------

::

	svn:eol-style native # CRLF/LF conversion; CRLF, LF, CR to force
	svn:ignore "*.class file dir" # syntax like .cvsignore (does not support '!' reset)
	$ svn propset svn:ignore -F .cvsignore . # equivqlent of .cvsignore file
	$ svn status --no-ignore # to override "svn:ignore" flag   
	$ svn propset svn:keywords "Date Author" weather.txt # set on these two keywords
	$ svn -v proplist weather.txt
	  svn:keywords
	    Date Author
	$ svn proplist -v calc/button.c # list proprties of button.c
	$ svn propdel license calc/button.c # delete license property
	$ svn -v proplist src/HellWorld.java
	  Properties on 'src/HelloWorld.java':
	  svn:keywords
	    Date Author Revision HeadURL Id

Subversion Keywords 
===================

::

	# Note: Case Sensitive
	Date     # [LastChangedDate] NOTE local time-zone
	Revision # [LastChangedRevision] last known revision (repository revision)
	Author   # last known user to change the file
	HeadURL  # full URL to the latest version of the file
	Id       # like RCS/CVS "$Id: calc.c 148 2006-07-28 21:30:43Z sally $"

Creating lock entries
=====================

::
	
	# typically use on binary/image files, so no deltas
	$ svn lock raisin.jpg             # lock file, other lock requests will fail
	$ svn unlock raisin.jpg           # unlock file
	$ svn status [-u|--show-updates]  # will list lock status (third/sixth columns)
	$ svn lock --force raisin.jpg     # force/override lock
	$ svn update                      # fetch locked copy
	$ svnadmin lslocks /var/svn/repos

	$ svn status [-u|--show-updates]  # will list lock status (third/sixth columns)
	#  ' ' # file is not locked
	#  K   # file is locked in this working copy
	#  O   # file is locked by another user or directory
	#  B   # file is locked but lock has been broken
	#  T   # file is locked but lock has been stolen

Change-lists
============

::

	# Works only local copy (not on repo)
	$ svn changelist maths-fixes integer.c mathops.c
	$ svn changelist --remove  button.c
	$ svn diff --changelist math-fixes
	$ svn ci -m "maths logic bug fix" --changelist maths-fixes

The ``svnserve`` startup script
===============================

For earlier Fedora versions that do not have ``systemd``.

::

	[root@wallace ~]# cat /etc/init.d/svnserve
	#!/bin/bash
	#
	#   /etc/rc.d/init.d/subversion
	#
	# Starts the Subversion Daemon
	#
	# chkconfig: 2345 90 10
	# description: Subversion Daemon
	# processname: svnserve
	# pidfile: /var/lock/subsys/svnserve
	
	source /etc/rc.d/init.d/functions
	
	[ -x /usr/bin/svnserve ] || exit 1
	
	### Default variables
	REPO_ROOT=/path/to/your/svnrepos
	REPO_OWNER="svn"
	SYSCONFIG="/etc/sysconfig/subversion"
	
	### Read configuration
	[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"
	
	RETVAL=0
	prog="svnserve"
	desc="Subversion Daemon"
	pidfile="/var/run/svnserve/$prog.pid"
	
	start() {
	   echo -n $"Starting $desc ($prog): "
	   daemon --user=$REPO_OWNER $prog -d -r $REPO_ROOT --pid-file $pidfile
	   RETVAL=$?
	   if [ $RETVAL -eq 0 ]; then
	     touch /var/lock/subsys/$prog
	   fi
	   echo
	}
	
	obtainpid() {
	   pidstr=`pgrep $prog`
	   pidcount=`awk -v name="$pidstr" 'BEGIN{split(name,a," "); print length(a)}'`
	   if [ ! -r "$pidfile" ] && [ $pidcount -ge 2 ]; then	
		pid=`awk -v name="$pidstr" 'BEGIN{split(name,a," "); print a[1]}'`
		echo $prog is already running and it was not started by the init script.
	   fi
	}
	
	stop() {
	   echo -n $"Shutting down $desc ($prog): "
	   if [ -r "$pidfile" ]; then
		pid=`cat $pidfile`
		kill -s 3 $pid
		RETVAL=$?
	   else
		RETVAL=1
	   fi
	   [ $RETVAL -eq 0 ] && success || failure
	   echo
	   if [ $RETVAL -eq 0 ]; then
	     rm -f /var/lock/subsys/$prog
	     rm -f $pidfile
	   fi
	   return $RETVAL
	}
	
	restart() {
		stop
		start
	}
	
	forcestop() {
	   echo -n $"Shutting down $desc ($prog): "
	
	   kill -s 3 $pid 
	   RETVAL=$?
	   [ $RETVAL -eq 0 ] && success || failure
	   echo
	   if [ $RETVAL -eq 0 ]; then
	     rm -f /var/lock/subsys/$prog
	     rm -f $pidfile
	   fi
	
	   return $RETVAL
	}
	
	status() {
	   if [ -r "$pidfile" ]; then
		pid=`cat $pidfile`
	   fi
	   if [ $pid ]; then
	           echo "$prog (pid $pid) is running..."
	   else
	        echo "$prog is stopped"
	   fi
	}
	
	obtainpid
	
	case "$1" in
	  start)
	   start
	   ;;
	  stop)
	   stop
	   ;;
	  restart)
	   restart
	   RETVAL=$?
	   ;;
	  condrestart)
	   [ -e /var/lock/subsys/$prog ] && restart	
	   RETVAL=$?
	   ;;
	  status)
	   status
	   ;;
	  forcestop)
	   forcestop
	   ;;
	  *)
	   echo $"Usage: $0 {start|stop|forcestop|restart|condrestart|status}"
	   RETVAL=1
	esac
	
	exit $RETVAL
  
The ``svnserve`` Configuration file
===================================

::

	[root@wallace ~]# cat /etc/sysconfig/subversion 
	REPO_ROOT=/home/svnroot
	REPO_OWNER=svn

