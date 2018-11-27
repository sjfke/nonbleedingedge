:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/linux-tricks.rst

***********************
Linux Tricks Cheatsheet
***********************

Password Generators
===================

* `OSTechNix passwords <https://www.ostechnix.com/4-easy-ways-to-generate-a-strong-password-in-linux/>`_
* `MUO passwords <https://www.makeuseof.com/tag/5-ways-generate-secure-passwords-linux/>`_

::

	$ brew install pwgen     # MacOS
	$ sudo dnf install pwgen # Fedora
	$ pwgen 12
	sei9AhPiokai jaezooThahn4 yahghooCh5ha uquiCh7soog0 Pahthe0fe5Ku owaht4xooPhu
	eet2eijeeT6E Chie8oz1Enee Piemu7pi1uqu TheebohNg8se eil2AhNeiF2s WueGh8guoxie
	
	$ sudo dnf install apg   # Fedora
	$ apg -n 3 -m 12 -M SNCL
	|OgFeOcVask6
	Aw*SwuKalap7
	Nagnec8swif?
	
	$ brew install gpg       # MacOS
	$ sudo dnf install gpg   # Fedora
	$ gpg --gen-random --armor 1 14
	spdhuOS2il2JjhOq2ZU=


``tree`` Directory Viewer
=========================

* `nixCraft tree <https://www.cyberciti.biz/faq/linux-show-directory-structure-command-line/>`_
* `OSTechNix tree <https://www.ostechnix.com/view-directory-tree-structure-linux/>`_
* `GeeksForGeeks tree <https://www.geeksforgeeks.org/tree-command-unixlinux/>`_

::

	$ brew install tree     # MacOS
	$ sudo dnf install tree # Fedora
	
	$ tree
	$ tree /path/to/directory
	$ tree [options]
	$ tree [options] /path/to/directory

``dnf`` Useful Commands
=======================

* `dnf examples <https://www.rootusers.com/25-useful-dnf-command-examples-for-package-management-in-linux/>`_

Fedora package installer::

	$ sudo dnf install httpd                            # install httpd
	$ sudo dnf install httpd-manual -y                  # assume yes
	$ sudo dnf dnf check-update                         # check for available updates
	$ sudo dnf update                                   # updateb installed packages
	$ sudo dnf install unbound-1.4.20-28.el7.x86_64.rpm # install local package
	$ sudo dnf remove httpd                             # remove package
	$ sudo dnf reinstall httpd -y                       # reinstall package
	$ sudo dnf search php                               # search for a package
	$ sudo dnf provides /etc/httpd/conf/httpd.conf      # which package provides the file
	$ sudo dnf info httpd                               # 
	$ sudo dnf history                                  # installation history
	$ sudo dnf history info 13                          # what did install 13 do
	$ sudo dnf history undo 13 -y                       # undo install 13
	$ sudo dnf history redo 13 -y
	$ sudo dnf list installed
	$ sudo dnf grouplist                                # list which groups are available, installed, not-installed.
	$ sudo dnf groupinfo "Web Server"                   # what is installed by this group
	
	
	
	