:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/linux-tricks.rst

***********************
Linux Tricks Cheatsheet
***********************

Password Generators
===================

* `OSTechNix passwords <https://www.ostechnix.com/4-easy-ways-to-generate-a-strong-password-in-linux/>`_
* `MUO passwords <https://www.makeuseof.com/tag/5-ways-generate-secure-passwords-linux/>`_

.. code-block:: console

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
* `hier - description of the file system hierarchy <https://linux.die.net/man/7/hier>`_

.. code-block:: console

	$ brew install tree     # MacOS
	$ sudo dnf install tree # Fedora
	
	$ tree
	$ tree /path/to/directory
	$ tree [options]
	$ tree [options] /path/to/directory



``dnf`` Useful Commands
=======================

Fedora package installer `DNF <https://www.rootusers.com/25-useful-dnf-command-examples-for-package-management-in-linux/>`_

.. code-block:: console

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
	$ sudo dnf repoquery --list httpd                   # list the files installed
	$ sudo dnf history                                  # installation history
	$ sudo dnf history info 13                          # what did install 13 do
	$ sudo dnf history undo 13 -y                       # undo install 13
	$ sudo dnf history redo 13 -y
	$ sudo dnf list installed
	$ sudo dnf grouplist                                # list which groups are available, installed, not-installed.
	$ sudo dnf groupinfo "Web Server"                   # what is installed by this group

Terminal Pagers
===============

Stolen from the `Fedora Magazine: 5 cool terminal pages <https://fedoramagazine.org/5-cool-terminal-pagers-in-fedora/#more-29502>`_ post.

.. code-block:: console

	$ more --help                   # trusty original with limited features
	$ more <file>                   # 
	$ more <file1> <file2> <file3>  # ':n' next file, ':p' previous file

	$ less --help                   # many features
	$ less <file>                   # 
	$ less <file1> <file2> <file3>  # ':n' next file, ':p' previous file, ':e' new file

	$ most --help                   # good for 'wide' files
	$ most <file>                   # screens: 'ctl-x 2' split, 'ctl-x 1' close , 'ctl-x o' switch 
	$ most <file1> <file2> <file3>  # split-screen and ':n' next file, ':p' previous file

	$ pspg --help                   # table friendly pager
	$ cat t.csv
	a;b;c;d;e
	1;2;3;4;5
	$ cat t.csv | pspg --csv
	
	mysql> pager pspg;              # replace less or more as pager	
	$ export PAGER=pspg; mycli ...  # MySQL CLI example
	$ export PAGER=pspg; pgcli ...  # PostygreSQL CLI example	

Cat File Tricks
===============

.. code-block:: console

    $ cat -n <filename>                      # adds line number prefix
    $ cat -e <filename>                      # shows crlf ending (Unix, DOS, MacOS)
    $ cat -n <filename> | head -5            # (beginning) first 5 lines
    $ cat -n <filename> | tail -5            # (ending) last 5 lines
    $ cat -n <filename> | tail -10 | head -5 # (middle) first 5 of last 10 lines

Grep File Tricks
================

.. code-block:: console

    $ cat flintstones.yaml
    ---
    family: flintstones
    members:
      - Name: Fred
        Age: 35
        Gender: male
      - Name: Wilma
        Age: 25
        Gender: female
      - Name: Pebbles
        Age: 1
        Gender: female
      - Name: Dino
        Age: 5
        Gender: male

    $ grep Fred flintstones.yaml
      - Name: Fred

    $ grep Name flintstones.yaml
      - Name: Fred
      - Name: Wilma
      - Name: Pebbles
      - Name: Dino

    $ grep "Name|Age" flintstones.yaml    # no output
    $ grep -E "Name|Age" flintstones.yaml # Extended (a.k.a egrep)
      - Name: Fred
        Age: 35
      - Name: Wilma
        Age: 25
      - Name: Pebbles
        Age: 1
      - Name: Dino
        Age: 5

    $ grep Age flintstones.yaml -A 1     # one line After match
        Age: 35
        Gender: male
    --
        Age: 25
        Gender: female
    --
        Age: 1
        Gender: female
    --
        Age: 5
        Gender: male

    $ grep Age flintstones.yaml -B 1     # one line Before match
      - Name: Fred
        Age: 35
    --
      - Name: Wilma
        Age: 25
    --
      - Name: Pebbles
        Age: 1
    --
      - Name: Dino
        Age: 5

    $ grep Age flintstones.yaml -C 1     # one line Context (before/after) match
      - Name: Fred
        Age: 35
        Gender: male
      - Name: Wilma
        Age: 25
        Gender: female
      - Name: Pebbles
        Age: 1
        Gender: female
      - Name: Dino
        Age: 5
        Gender: male

JSON File Tricks
================

* ``jq`` is a lightweight command-line JSON processor, similar to ``sed``.
* ``yq`` is a Python command-line (``jq`` wrapper) YAML/XML/TOML processor.

.. code-block:: console

    $ sudo dnf install jq # Fedora
    $ brew install jq     # MacOS
    $ pip install yq      # Python

    # Command Line examples
    $ echo '{"fruit":{"name":"apple","color":"green","price":1.20}}' | jq '.' # pretty-print
    $ curl http://api.open-notify.org/iss-now.json | jq '.' # pretty-print HTTP response

    # Simple JSON file example
    $ jq '.' fruit.json
    {
        "fruit": {
        "name": "apple",
        "color": "green",
        "price": 1.2
        }
    }
    $ jq '.' fruit.json                         # pretty-print file
    $ jq '.fruit.color' fruit.json              # extract colors
    $ jq '.fruit.color,.fruit.price' fruit.json # extract colors and price
    $ jq '.fruit | keys' fruit.json             # keys

    # JSON array example
    $ jq '.' fruits.json
    [
      {
        "name": "apple",
        "color": "green",
        "price": 1.2
      },
      {
        "name": "banana",
        "color": "yellow",
        "price": 0.5
      },
      {
        "name": "kiwi",
        "color": "green",
        "price": 1.25
      }
    ]

    $ jq '.' fruits.json           # pretty-print
    $ jq '.[] | .name' fruits.json # list all fruits in the array
    $ jq '.[].name' fruits.json    # list all fruits in the array
    $ jq '.[1]' fruits.json        # array element 1

* `Guide to Linux jq Command for JSON Processing <https://www.baeldung.com/linux/jq-command-json>`_
* `Querying JSON and XML with jq and xq <https://www.ashbyhq.com/blog/engineering/jq-and-yq>`_
* `yq: Command-line YAML/XML/TOML processor - jq wrapper for YAML, XML, TOML documents <https://github.com/kislyuk/yq>`_
* `jq, xq and yq - Handy tools for the command line <https://blog.lazy-evaluation.net/posts/linux/jq-xq-yq.html>`_
* `TOML [Tom's Obvious Minimal Language] (.INI like) <https://toml.io/en/>`_


Gnome Desktop Custom Launcher
=============================

Using `PyCharm Community Edition <https://www.jetbrains.com/pycharm/>`_ as an example,
`download the PyCharm Community Edition <https://www.jetbrains.com/pycharm/download/#section=linux>`_ and unpack the
``tar.gz`` file into ``$HOME/Applications``

Create the ``com.jetbrains.pycharm.community.desktop`` file, modify it as necessary, and then copy it to
``$HOME/.local/share/applications``

.. code-block:: console

    $ cat com.jetbrains.pycharm.community.desktop
    [Desktop Entry]
    Encoding=UTF-8
    Name=PyCharm
    Exec=/home/<user>/Applications//bin/pycharm.sh
    Icon=/home/<user>/Applications/pycharm-community/bin/pycharm.png
    Type=Application
    Version=2022.2.2
    Terminal=false
    Categories=Development;

    $ cp ./com.jetbrains.pycharm.community.desktop $HOME/.local/share/applications

* `Adding a Custom Launcher to Gnome Shell <https://hackeradam.com/post/custom-launcher-gnome-shell/>`_
* `Guide to Desktop Entry Files in Linux <https://www.baeldung.com/linux/desktop-entry-files>`_
* `KDE and GNOME desktop environments have adopted a similar format <https://specifications.freedesktop.org/desktop-entry-spec/latest/index.html#introduction>`_
* `DBUS Specification Message Protocol Names <https://dbus.freedesktop.org/doc/dbus-specification.html#message-protocol-names>`_

WSL2 on Windows
===============

Read the `prerequisites` in, `Install Linux on Windows with WSL <https://learn.microsoft.com/en-us/windows/wsl/install>`_

Installation can now be done via the `Microsoft Store`

First enable Windows optional features to run WSL, so the sequence is as follows.

::

    1. Windows -> Settings -> Optional Features -> More Windows Features
        - [x] Virtual Machine Platform
        - [x] Windows Subsystem for Linux
    2. Reboot
    3. Install WSL from Microsoft Store
    4. Reboot
    5. Install Ubuntu (20.04.6 LTS) from Microsoft Store

Linux Network Tools
===================

+----------------------------------------------------------------------+----------------------------------------------------+
| Command                                                              | Description                                        |
+======================================================================+====================================================+
| `ping, ping6 <https://linux.die.net/man/8/ping>`_                    | Send ICMP ECHO_REQUEST to network hosts            |
+----------------------------------------------------------------------+----------------------------------------------------+
| `hping3 <https://linux.die.net/man/8/hping3>`_                       | TCP/IP equivalent of ping                          |
+----------------------------------------------------------------------+----------------------------------------------------+
| `curl <https://linux.die.net/man/1/curl>`_,                          | Access URL meta-data or content                    |
| `wget <https://linux.die.net/man/1/wget>`_,                          |                                                    |
| `HTTPie <https://httpie.io/docs/cli>`_                               |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `tc <https://linux.die.net/man/8/tc>`_                               | Show / manipulate traffic control settings         |
+----------------------------------------------------------------------+----------------------------------------------------+
| `dig <https://linux.die.net/man/1/dig>`_,                            | DNS lookup utilities                               |
| `nslookup <https://linux.die.net/man/1/nslookup>`_,                  |                                                    |
| `host <https://linux.die.net/man/1/host>`_,                          |                                                    |
| `whois <https://www.baeldung.com/linux/whois-command>`_              |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ssh <https://linux.die.net/man/1/ssh>`_,                            | Secure client connection and copy                  |
| `scp <https://linux.die.net/man/1/scp>`_                             |                                                    |
| `sftp <https://linux.die.net/man/1/sftp>`_                           |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `telnet <https://linux.die.net/man/1/telnet>`_,                      | Insecure client connection and copy                |
| `ftp <https://linux.die.net/man/1/ftp>`_,                            |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `rsync <https://linux.die.net/man/1/rsync>`_                         | Sophisticated remote/local file-copying            |
+----------------------------------------------------------------------+----------------------------------------------------+
| `tcpdump <https://linux.die.net/man/8/tcpdump>`_,                    | Dump and analyze network traffic                   |
| `wireshark <https://linux.die.net/man/1/wireshark>`_,                |                                                    |
| `tshark <https://linux.die.net/man/1/tshark>`_                       |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ngrep <https://linux.die.net/man/8/ngrep>`_                         | Network grep                                       |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ifconfig <https://linux.die.net/man/8/ifconfig>`_,                  | Show/manipulate ip routing, devices, and tunnels   |
| `route <https://linux.die.net/man/8/route>`_,                        |                                                    |
| `ethtool <https://linux.die.net/man/8/ethtool>`_,                    |                                                    |
| `ip <https://linux.die.net/man/8/ip>`_                               |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `iw <https://linux.die.net/man/8/iw>`_,                              | Configure a wireless network interface             |
| `iwconfig <https://linux.die.net/man/8/iwconfig>`_                   |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `nmap <https://linux.die.net/man/1/nmap>`_,                          | Network exploration tool and security/port scanner |
| `zenmap <https://linux.die.net/man/1/zenmap>`_                       |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `p0f <https://linux.die.net/man/1/p0f>`_                             | Identify remote systems passively                  |
+----------------------------------------------------------------------+----------------------------------------------------+
| `openvpn <https://linux.die.net/man/8/openvpn>`_,                    | Secure VPN tunnels                                 |
| `wireguard <https://www.wireguard.com/>`_                            |                                                    |
| `stunnel <https://linux.die.net/man/8/stunnel>`_                     |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `nc <https://linux.die.net/man/1/nc>`_,                              | Arbitrary TCP and UDP connections and listeners    |
| `socat <https://linux.die.net/man/1/socat>`_                         |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `netstat <https://linux.die.net/man/8/netstat>`_,                    | Troubleshoot connections, processes, file usage    |
| `ss <https://linux.die.net/man/8/ss>`_,                              |                                                    |
| `lsof <https://linux.die.net/man/8/lsof>`_,                          |                                                    |
| `fuser <https://linux.die.net/man/1/fuser>`_                         |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `iptables <https://linux.die.net/man/8/netstat>`_,                   | Firewall, TCP/IP packet filtering and NAT          |
| `ip6tables <https://linux.die.net/man/8/ip6tables>`_,                |                                                    |
| `nftables <https://www.netfilter.org/projects/nftables/index.html>`_ |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `arp <https://linux.die.net/man/8/arp>`_,                            | Manipulate the system ARP cache                    |
| `arptables <https://linux.die.net/man/8/arptables>`_,                |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `traceroute <https://linux.die.net/man/8/traceroute>`_,              | Troubleshoot connections, processes, file usage    |
| `mtr <https://linux.die.net/man/8/mtr>`_,                            |                                                    |
| `tcptraceroute <https://linux.die.net/man/1/tcptraceroute>`_         |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `iptraf <https://linux.die.net/man/8/iptraf>`_,                      | Troubleshoot network bandwidth issues              |
| `nethogs <https://linux.die.net/man/8/nethogs>`_,                    |                                                    |
| `iftop <https://linux.die.net/man/8/iftop>`_,                        |                                                    |
| `ntop <https://linux.die.net/man/8/ntop>`_                           |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ab <https://linux.die.net/man/1/ab>`_,                              | Benchmarking tools                                 |
| `nload <https://linux.die.net/man/1/nload>`_,                        |                                                    |
| `iperf <https://linux.die.net/man/1/iperf>`_                         |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ipcalc <https://linux.die.net/man/1/ipcalc>`_                       | Simple manipulation of IP addresses                |
+----------------------------------------------------------------------+----------------------------------------------------+
| `nsenter <https://linuxhint.com/nsenter-linux-command/>`_            | Enter container process's namespace                |
+----------------------------------------------------------------------+----------------------------------------------------+
| `Python HTTP modules <https://docs.python.org/3/library/http.html>`_ | HTTP serve files in CWD, ``python -m http.server`` |
+----------------------------------------------------------------------+----------------------------------------------------+

Brendan Gregg's Homepage
========================

*G'Day. I use this site to share and bookmark various things, mostly my work with computers.
While I currently work on large scale cloud computing performance at Intel (previously Netflix), this site
reflects my own opinions and work from over the years. I have a personal blog, and I'm also on twitter.*

*This page lists everything: Documentation, Videos, Software, Misc.
For a short selection of most popular content, see my Overview page.*

* `Overview <https://www.brendangregg.com/overview.html>`_
* `Linux Performance <https://www.brendangregg.com/linuxperf.html>`_
* `Blog Posts <https://www.brendangregg.com/blog/index.html>`_


Managing ``.rc`` files
======================

* `Managing dotfiles with rcm on Fedora <https://fedoramagazine.org/managing-dotfiles-rcm/>`_

By default, rcm uses ``~/.dotfiles`` for storing all the dotfiles it manages.

A managed dotfile is actually stored inside ``~/.dotfiles``, and a symlinked.

For example, if ``~/.bashrc`` is tracked by ``rcm``, a long listing would look like this.

::

	$ ls -l ~/.bashrc
	lrwxrwxrwx. 1 link link 27 Dec 16 05:19 .bashrc -> /home/geoff/.dotfiles/bashrc
	
	
``rcm`` consists of 4 commands:

* ``mkrc`` – convert a file into a dotfile managed by rcm
* ``lsrc`` – list files managed by rcm
* ``rcup`` – synchronize dotfiles managed by rcm
* ``rcdn`` – remove all the symlinks managed by rcm

Fedora 36 Live CD install
=========================

Of course backup everything you want to keep because you are going to reformat the HDD or SSD!

The *live* installation is process is well documented and robust so simply follow:

* `Download Fedora 36 Workstation <https://getfedora.org/en/workstation/download/>`_
* `Creating and using a live installation image <https://docs.fedoraproject.org/en-US/quick-docs/creating-and-using-a-live-installation-image/index.html>`_

Next add the `RPM Fusion <https://rpmfusion.org/RPM%20Fusion>`_ repositories, by installing and configuring them as
described in `RPMFusion Configuration <https://rpmfusion.org/Configuration>`_

Finally consult `Fedora Quick Docs <https://docs.fedoraproject.org/en-US/quick-docs/>`_ especially the *Adding and managing software* section.

Some of the perennial *audio* and *video* playback issues are still there, so follow these instructions.

* `Installing plugins for playing movies and music <https://docs.fedoraproject.org/en-US/quick-docs/assembly_installing-plugins-for-playing-movies-and-music/>`_

.. code-block:: console

    $ sudo dnf install gstreamer1-plugins-{bad-\*,good-\*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel
    $ sudo dnf install lame\* --exclude=lame-devel
    $ sudo dnf group upgrade --with-optional Multimedia
