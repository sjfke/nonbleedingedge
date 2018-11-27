:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/howtos/fedora29-install.rst

****************************
Fedora 29 Live Media Install
****************************

Introduction
============

This HOWTO explains how to install `fedora29` from the `live DVD media`.

**FIRST** backup everthing you want to reinstall afterwords, usually `/home/<user>` selective directories.

Tutorial Links
==============

* `Fedora Installation Guide <https://docs.fedoraproject.org/en-US/fedora/f29/install-guide/>`_
* `Enable Fastestmirror <http://www.theironsamurai.com/dnf-slow-on-fedora-add-fastestmirror-to-your-dnf-conf/>`_
* `25 Useful DNF Command Examples <https://www.rootusers.com/25-useful-dnf-command-examples-for-package-management-in-linux/>`_

Upgrade rather than Fresh Installation
======================================

Simpler, safer, but you you should still backup your data and then follow:

* `DNF system upgrade <https://fedoraproject.org/wiki/DNF_system_upgrade>`_

Fresh Installation
==================

* Boot the system with the live media in the DVD.
* Delete all LV's **erasing ALL your user data**
* Reboot the system.

Post Installation
=================

Disable `selinux`::

	$ sudo vi /etc/sysconfig/seliniux
	:%s/enforcing/disabled/g
	:x
	
Set the hostname if you forgot::

	$ sudo hostnamectl set-hostname newhostname
	
 
Setup Fastestmirror::

	$ sudo vi /etc/dnf/dnf.conf # add fastestmirror=true
	[main]
	gpgcheck=1
	installonly_limit=3
	clean_requirements_on_remove=True
	fastestmirror=true
	
Update Packages::

	$ sudo dnf upgrade
	$ sudo reboot

Install RMP Fusion repos
========================

* `RPM Fusion <https://rpmfusion.org/Configuration>`_

Click on the appropriate links and use install (default) action.

Suggest `RPM Fusion free` and `RPM Fusion nonfree`.

Additional Updates
==================

If you want to `ssh` from another host to finish updating your new system::

	$ sudo systemctl status sshd # confirm it is not running
	$ sudo systemctl start sshd  # start the daemon
	$ sudo systemctl enable sshd # enable restarting the daemon on reboot
	$ sudo systemctl status sshd # confirm it is running

Despite all attempts to kill `Adobe Flash`, some sites still use it::

	$ sudo dnf install http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.norach rpm
	$ sudo dnf flash-plugin
	
Install Chromium (not Google Chrome)::

	$ sudo dnf install chromium # bad? see Multimedia post-install
	
Stolen from mjmwired.net, but still seems relevant
==================================================

* `Fedora 19 Installation Guide <https://www.mjmwired.net/resources/mjm-fedora-f19.html>`_

There should be a better way to do this... so try skipping this section and see what doesn't work.

XMMS: simple, older GUI, minimalistic features (but still popular)::

	$ sudo dnf install xmms xmms-mp3 xmms-faad2 xmms-flac xmms-pulse
	
Rhythmbox/Gstreamer - A simple audio application similar to iTunes layout::

	$ sudo dnf install install rhythmbox gstreamer-plugins-ugly gstreamer-plugins-bad gstreamer-ffmpeg gstreamer-plugins-bad-nonfree
	
**Note**: `rhythmbox` should already be installed, so ignore the warning.

MPlayer - MPlayer comes in a command line only interface or skinable GUI::

	$ sudo dnf install mplayer mplayer-gui mencoder

Xine - Xine is similar to MPlayer::

	$ sudo dnf install xine xine-lib-extras xine-lib-extras-freeworld
	
	
Install Additional groups
=========================

::

	$ sudo dnf grouplist
	$ sudo dnf groupinfo 'Infrastructure Server'
	$ sudo dnf groupinstall 'Infrastructure Server'
	$ sudo dnf groupinfo 'Web Server'
	$ sudo dnf groupinstall 'Web Server'
	
Install AppStream metadata
==========================

::

	$ sudo dnf groupupdate core

Multimedia post-install
=======================

::

	$ sudo dnf groupupdate Multimedia
	$ sudo dnf groupupdate sound-and-video

At the time of writing 2018.11.26 the `dnf groupupdate Multimedia`, produces the following error::

	$ sudo dnf groupupdate Multimedia
	Last metadata expiration check: 1:20:48 ago on Mon 26 Nov 2018 02:54:29 PM CET.
	Error: 
	 Problem: problem with installed package chromium-70.0.3538.77-4.fc29.x86_64
	  - conflicting requests
	  - nothing provides chromium-libs(x86-64) = 69.0.3497.100-1.fc29 needed by chromium-libs-media-freeworld-69.0.3497.100-1.fc29.x86_64

So `chromium` seems to break `Rhythmbox <https://ask.fedoraproject.org/en/question/91677/rhythmbox-does-not-see-music-files-there-are-tons-of-them/>`_ 
because you cannot groupupdate `Multimedia`.

Remove `chromium` and try `easily install Chrome & Steam on Fedora <https://fedoramagazine.org/third-party-repositories-fedora/>`_

::

	$ sudo dnf remove chromium -y
	$ sudo dnf install fedora-workstation-repositories
	$ sudo dnf config-manager --set-enabled google-chrome # Need to enable repo
	$ sudo dnf search google-chrome
	====================== Name Matched: google-chrome ==========================
	google-chrome-beta.x86_64 : Google Chrome (beta)
	google-chrome-stable.x86_64 : Google Chrome
	google-chrome-unstable.x86_64 : Google Chrome (unstable)
	====================== Summary Matched: google-chrome =======================
	$ sudo dnf install google-chrome

**Note**: also check `Workstation/Third Party Software Repositories <https://fedoraproject.org/wiki/Workstation/Third_Party_Software_Repositories>`_

Other Groups to Consider
========================

::

	$ sudo dnf groupinstall 'Administration Tools' -y
	$ sudo dnf groupinstall 'C Development Tools and Libraries' -y
	$ sudo dnf groupinstall 'Development Tools' -y
	$ sudo dnf groupinfo 'Fedora Eclispe'
	$ sudo dnf groupinfo 'Graphical Internet'   # want filezilla only
	$ sudo dnf install filezilla -y
	$ sudo dnf groupinstall 'Python Classroom' -y
	$ sudo dnf groupinfo 'Python Science'
	$ sudo dnf groupinfo 'Security Lab'
	$ sudo dnf groupinfo 'Sound and Video'
	$ sudo dnf groupinfo 'System Tools'
	
	# Some personal preferences
	$ sudo dnf install perl-libwww-perl -y # $ sudo dnf provides HEAD
	$ sudo dnf install vim-enhanced vim-X11 -y
	$ sudo dnf install vim-syntastic-perl.noarch vim-syntastic-json.noarch vim-syntastic-sh.noarch vim-syntastic-yaml.noarch -y


