:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/linux-tricks.rst

***********************
Linux Tricks Cheatsheet
***********************

Password Generators
===================

* `OSTechNix passwords <https://www.ostechnix.com/4-easy-ways-to-generate-a-strong-password-in-linux/>`_
* `MUO passwords <https://www.makeuseof.com/tag/5-ways-generate-secure-passwords-linux/>`_

.. code-block:: console

    # pwgen
    $ brew install pwgen            # MacOS
    $ sudo dnf install pwgen        # Fedora
    $ pwgen 12
    sei9AhPiokai jaezooThahn4 yahghooCh5ha uquiCh7soog0 Pahthe0fe5Ku owaht4xooPhu
    eet2eijeeT6E Chie8oz1Enee Piemu7pi1uqu TheebohNg8se eil2AhNeiF2s WueGh8guoxie

    # apg
    $ sudo dnf install apg          # Fedora
    $ apg -n 3 -m 12 -M SNCL        # pronounceable
    tit8OdcigEp~
    Plaf@dryRec6
    JavJu%Wudek6
    $ apg -a 1 -n 3 -m 12 -M SNCL   # random
    ,+c"e3P[Me%H
    ZlL0qw_8L)Ff
    1x=2nizg}x!X

    # gpg
    $ brew install gpg              # MacOS
    $ sudo dnf install gpg          # Fedora
    $ gpg --gen-random --armor 1 14
    spdhuOS2il2JjhOq2ZU=


``tree`` Directory Viewer
=========================

* `nixCraft tree <https://www.cyberciti.biz/faq/linux-show-directory-structure-command-line/>`_
* `OSTechNix tree <https://www.ostechnix.com/view-directory-tree-structure-linux/>`_
* `GeeksForGeeks tree <https://www.geeksforgeeks.org/tree-command-unixlinux/>`_
* `hier - description of the file system hierarchy <https://man.cx/hier>`_

.. code-block:: console

	$ brew install tree     # MacOS
	$ sudo dnf install tree # Fedora
	
	$ tree
	$ tree /path/to/directory
	$ tree [options]
	$ tree [options] /path/to/directory

``dnf`` Useful Commands
=======================

* `25 Useful DNF Command Examples For Package Management In Linux <https://www.rootusers.com/25-useful-dnf-command-examples-for-package-management-in-linux/>`_

.. code-block:: console

    $ sudo dnf check-update                             # check for available updates
    $ sudo dnf update                                   # update installed packages
    $ sudo dnf upgrade                                  # a more aggressive update which may remove installed packages
    $ sudo dnf install httpd                            # install httpd
    $ sudo dnf install httpd-manual -y                  # assume yes
    $ sudo dnf install unbound-1.4.20-28.el7.x86_64.rpm # install local package
    $ sudo dnf remove httpd                             # remove package
    $ sudo dnf reinstall httpd -y                       # reinstall package
    $ sudo dnf search php                               # search for a package
    $ sudo dnf provides /etc/httpd/conf/httpd.conf      # which package provides the file (installed or not)
    $ sudo dnf provides httpd                           # which package provides 'httpd' (installed or not)
    $ sudo dnf info httpd                               # package info (installed or not)
    $ sudo dnf repoquery --list httpd                   # list the files (to be) installed by package
    $ sudo dnf history                                  # installation history
    $ sudo dnf history info 13                          # what did install 13 do
    $ sudo dnf history undo 13 -y                       # undo install 13
    $ sudo dnf history redo 13 -y                       # redo install 13
    $ sudo dnf list installed                           # list installed packages
    $ sudo dnf grouplist                                # list which groups are available, installed, not-installed
    $ sudo dnf groupinfo "System Tools"                 # what is installed by this group
    $ sudo dnf repolist                                 # reports being used
    $ sudo dnf clean all                                # clean dnf caches


``dnf5`` Useful Commands
========================

Fedora package installer changed from ``DNF`` to ``DNF5`` starting with ``Fedora 41``.

* `DNF vs. DNF5: Key Differences and Improvements <https://www.tecmint.com/dnf-vs-dnf5/>`_
* `DNF vs. DNF5: A Detailed Analysis of Performance Improvements <https://linuxlock.org/blog/dnf-vs-dnf5-compression/>`_
* `How to Use dnf5 Command for Fedora Package Management <https://www.tecmint.com/dnf5-command/>`_

.. code-block:: console

    $ sudo dnf check-update                             # check for available updates
    $ sudo dnf update                                   # update installed packages
    $ sudo dnf upgrade                                  # upgrade installed packages and dependencies
    $ sudo dnf install httpd                            # install httpd
    $ sudo dnf install httpd-manual -y                  # assume yes
    $ sudo dnf downgrade httpd                          # if possible downgrade
    $ sudo dnf upgrade httpd                            # if possible upgrade
    $ sudo dnf reinstall httpd                          # reinstall httpd
    $ sudo dnf remove httpd                             # remove package
    $ sudo dnf dnf check-update                         # check for available updates
    $ sudo dnf update                                   # update installed packages
    $ sudo dnf install unbound-1.4.20-28.el7.x86_64.rpm # install local package
    $ sudo dnf search php                               # search for a package
    $ sudo dnf provides /etc/httpd/conf/httpd.conf      # which package provides the file (installed or not)
    $ sudo dnf provides httpd                           # which package provides 'httpd' (installed or not)
    $ sudo dnf info httpd                               # package info (installed or not)
    $ sudo dnf repoquery --list httpd                   # list the files (to be) installed by package
    $ sudo dnf history list                             # installation history
    $ sudo dnf history info 13                          # what did install 13 do
    $ sudo dnf history undo 13 -y                       # undo install 13
    $ sudo dnf history redo 13 -y                       # redo install 13
    $ sudo dnf list --installed                         # list installed packages
    $ sudo dnf group list                               # list which groups are available, installed, not-installed
    $ sudo dnf group install system-tools               # installed this group
    $ sudo dnf group info system-tools                  # what is installed by this group
    $ sudo dnf repolist                                 # reports being used
    $ sudo dnf clean all                                # clean dnf caches

LS commands
===========

* `lshw Command in Linux: Get Hardware Details  <https://linuxhandbook.com/lshw-command/>`_
* `ls* Commands Are Even More Useful Than You May Have Thought <https://www.cyberciti.biz/open-source/command-line-hacks/linux-ls-commands-examples/>`_

+-------------+---------------------------------------------------------------------------------------------------------------------------+
| Command     | Description                                                                                                               |
+=============+===========================================================================================================================+
| lsblk       | `list block devices <https://linuxhandbook.com/lsblk-command/>`_                                                          |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lsb_release | `provides LSB (Linux Standard Base) information.  <https://commandmasters.com/commands/lsb_release-linux/>`_              |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lscpu       | `display information about the CPU architecture <https://linuxhint.com/lscpu-command/>`_                                  |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lsipc       | `show information on IPC facilities currently employed in the system <https://commandmasters.com/commands/lsipc-linux/>`_ |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lslocks     | `list local system locks <https://www.thegeekdiary.com/lslocks-command-examples-in-linux/>`_                              |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lslogins    | `display information about known users in the system <https://commandmasters.com/commands/lslogins-linux/>`_              |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lsmem       | `list the ranges of available memory with their online status <https://www.man7.org/linux/man-pages/man1/lsmem.1.html>`_  |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lsns        | `list namespaces <https://commandmasters.com/commands/lsns-linux/>`_                                                      |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lspci       | `list all PCI devices <https://commandmasters.com/commands/lspci-linux/>`_                                                |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lsusb       | `list USB devices <https://commandmasters.com/commands/lsusb-linux/>`_                                                    |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| lsof        | `list open files <https://linuxhandbook.com/lsof-command/>`_                                                              |
+-------------+---------------------------------------------------------------------------------------------------------------------------+

``ss`` an alternative to ``netstat``
====================================

Some Linux distributions do not provide ``netstat``, but may provide ``ss``

* `ss - another utility to investigate sockets <https://www.man7.org/linux/man-pages/man8/ss.8.html>`_

.. code-block::

    $ ss -tlp
    State              Recv-Q              Send-Q                           Local Address:Port                            Peer Address:Port             Process
    LISTEN             0                   4096                                127.0.0.11:43225                                0.0.0.0:*
    LISTEN             0                   80                                     0.0.0.0:3306                                 0.0.0.0:*
    LISTEN             0                   80                                        [::]:3306                                    [::]:*
    $ ss --help

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
	$ export PAGER=pspg; pgcli ...  # PostgreSQL CLI example

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

JSON, YAML File Filtering
=========================

* ``jq`` is a lightweight command-line JSON processor, similar to ``sed``.
* ``yq`` is a Python command-line (``jq`` wrapper) YAML/XML processor.

.. code-block:: console

    # Installation
    $ sudo dnf install jq      # Fedora
    $ brew install jq          # MacOS
    $ pip install yq           # Python
    $ winget install jqlang.jq # Windows

    # Command Line examples
    $ echo '{"fruit":{"name":"apple","color":"green","price":1.20}}' | jq '.' # pretty-print
    {
      "fruit": {
        "name": "apple",
        "color": "green",
        "price": 1.2
      }
    }

    # Get International Space Station Current Location
    $ curl http://api.open-notify.org/iss-now.json | jq '.' # pretty-print HTTP response
    {
      "message": "success",
      "iss_position": {
        "longitude": "103.2534",
        "latitude": "-44.3309"
      },
      "timestamp": 1719322950
    }

.. code-block:: console

    # Installation
    # Linux
    $ VERSION=v4.43.1
    $ BINARY=yq_linux_amd64
    $ sudo wget https://github.com/mikefarah/yq/releases/download/${VERSION}/${BINARY} -O /usr/bin/yq
    $ sudo chmod +x /usr/bin/yq

    $ brew install yq                  # MacOS
    $ winget install --id MikeFarah.yq # Windows

    # Command Line examples
    $ echo '{"fruit":{"name":"apple","color":"green","price":1.20}}' | yq '.'
    {"fruit": {"name": "apple", "color": "green", "price": 1.20}}

    # Get International Space Station Current Location
    $ curl http://api.open-notify.org/iss-now.json | yq '.' # pretty-print HTTP GET response
    {"message": "success", "iss_position": {"longitude": "103.9546", "latitude": "-44.0234"}, "timestamp": 1719322960}

* `JSON Examples, see "jq JSON Cheatsheet" <https://nonbleedingedge.com/cheatsheets/jq.html>`_
* `YAML, JSON Examples, see "yq YAML/JSON Cheatsheet" <https://nonbleedingedge.com/cheatsheets/yq.html>`_

XML, HTML File Filtering
========================

* `xq <https://github.com/sibprogrammer/xq>`_ XML and HTML beautifier and content extractor
* `GitHub: sibprogrammer/xq <https://github.com/sibprogrammer/xq>`_
* `jq, xq and yq - Handy tools for the command line <https://blog.lazy-evaluation.net/posts/linux/jq-xq-yq.html>`_

.. code-block:: console

    # Installation
    $ sudo dnf install xq                               # Fedora
    $ brew install xq                                   # MacOS
    $ curl -sSL https://bit.ly/install-xq | sudo bash   # Linux, installs into /usr/local/bin

    # Command Line example
    $ curl -s https://www.w3schools.com/xml/note.xml | xq
    <?xml version="1.0" encoding="UTF-8"?>
    <note>
      <to>Tove</to>
      <from>Jani</from>
      <heading>Reminder</heading>
      <body>Don't forget me this weekend!</body>
    </note>

* `XML, HTML Examples, see "xq XML/HTML Cheatsheet" <https://nonbleedingedge.com/cheatsheets/xq.html>`_

Repology
=========

* `Repology, the packaging hub <https://repology.org>`_

Repology shows you in which repositories a given project is packaged, which version is the latest and which
needs updating, who maintains the package, and other related information.

HTTP Header Checking
====================

.. code-block:: console

    $ curl -I 127.0.0.1:8080
    HTTP/1.1 200 OK
    Server: nginx/1.27.0
    Date: Sat, 01 Jun 2024 15:14:01 GMT
    Content-Type: text/html
    Content-Length: 4253
    Last-Modified: Sat, 01 Jun 2024 14:14:45 GMT
    Connection: keep-alive
    ETag: "665b2cd5-109d"
    Accept-Ranges: bytes

    $ wget -S --spider 127.0.0.1:8080
    Spider mode enabled. Check if remote file exists.
    --2024-06-01 17:13:56--  http://127.0.0.1:8080/
    Connecting to 127.0.0.1:8080... connected.
    HTTP request sent, awaiting response...
      HTTP/1.1 200 OK
      Server: nginx/1.27.0
      Date: Sat, 01 Jun 2024 15:13:56 GMT
      Content-Type: text/html
      Content-Length: 4253
      Last-Modified: Sat, 01 Jun 2024 14:14:45 GMT
      Connection: keep-alive
      ETag: "665b2cd5-109d"
      Accept-Ranges: bytes
    Length: 4253 (4.2K) [text/html]
    Remote file exists and could contain further links,
    but recursion is disabled -- not retrieving.


Email Checking
==============

Shameless copy of the LinkedIn post by `Jan Schaumann <https://www.netmeister.org/>`_

.. code-block:: console

    $ sudo dnf install bind-utils                            # Install dig, if necessary
    $ dig +short MX yahoo.com                                # DNS MX records
    $ dig +short TXT yahoo.com | grep spf                    # domain spoofing check
    $ dig +short TXT selector._domainkey.yahoo.com           # DKIM email authentication method
    $ dig +short TXT _dmarc.yahoo.com                        # DMARC (spf and/or DKIM)
    $ dig +short TXT _mta-sts.yahoo.com                      # MTA-STS (is TLS enforced)
    $ curl https://mta-sts.yahoo.com/.well-known/mta-sts.txt # MTA-STS (is TLS enforced)
    $ dig +short TXT _smtp._tls.yahoo.com                    # SMTP TLS Reporting
    $ dig +short TLSA _port._tcp.yahoo.com                   # DANE check (no results?)
    $ dig +short TXT default._bimi.yahoo.com                 # BIMI check (no results?)

To help understand these commands

* `Sender Policy Framework <http://www.open-spf.org/>`_
* `DomainKeys Identified Mail <https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail>`_
* `Domain-based Message Authentication, Reporting and Conformance (DMARC) <https://en.wikipedia.org/wiki/DMARC>`_
* `What is MTA-STS, and Why Do You Need It? <https://easydmarc.com/blog/what-is-mta-sts-and-why-do-you-need-it/>`_
* `What is SMTP TLS Reporting? <https://dmarcadvisor.com/smtp-tls-reporting/>`_
* `How DANE Improves the Security of Email (SMTP) Communication <https://dmarcadvisor.com/dane-for-smtp/>`_
* `BIMI an emerging technology to display a brand’s logo next to authenticated emails. <https://www.smtp.com/blog/technical/bimi-what-it-means-for-marketers-and-businesses/>`_

Gnome Desktop Custom Launcher
=============================

Using `PyCharm Community Edition <https://www.jetbrains.com/pycharm/>`_ as an example,
`download the PyCharm Community Edition <https://www.jetbrains.com/pycharm/download/?section=linux>`_ and unpack the
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

* `Adding a Custom Launcher to Gnome Shell <https://hackeradam.com/adding-a-custom-launcher-to-gnome-shell/>`_
* `Guide to Desktop Entry Files in Linux <https://www.baeldung.com/linux/desktop-entry-files/>`_
* `KDE and GNOME desktop environments have adopted a similar format <https://specifications.freedesktop.org/desktop-entry-spec/latest/index.html#introduction>`_
* `DBUS Specification Message Protocol Names <https://dbus.freedesktop.org/doc/dbus-specification.html#message-protocol-names>`_

Base 64 Encode/Decode
=====================

.. code-block:: console

    $ echo -n "EncodeMe-in-Base64" | base64
    RW5jb2RlTWUtaW4tQmFzZTY0

    $ echo -n "RW5jb2RlTWUtaW4tQmFzZTY0" | base64 -d
    EncodeMe-in-Base64

Using ``Python``

.. code-block:: python

    >>> import base64
    >>> _ascii = "EncodeMe-in-Base64".encode("ascii")
    >>> _b64bytes = base64.b64encode(_ascii)
    >>> print(_b64bytes.decode("ascii"))
    RW5jb2RlTWUtaW4tQmFzZTY0

    >>> import base64
    >>> _ascii = "RW5jb2RlTWUtaW4tQmFzZTY0".encode("ascii")
    >>> _b64bytes = base64.b64decode(_ascii)
    >>> print(_b64bytes.decode("ascii"))
    EncodeMe-in-Base64


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

Update Ubuntu
=============

.. code-block:: console

    $ man apt-get
    $ sudo apt-get update  # sync the package index files
    $ sudo apt-get upgrade # install the newest versions
    $ sudo reboot

    $ man apt
    $ sudo apt update      # sync the package index files
    $ sudo apt upgrade     # install the newest versions
    $ sudo reboot

    $ apt --help

Testing Remote Connections
==========================

The examples are testing for ``SSH`` daemon (port 22) on host ``192.168.0.1``

`ncat - Concatenate and redirect sockets <https://www.man7.org/linux/man-pages/man1/ncat.1.html>`_
--------------------------------------------------------------------------------------------------

.. code-block:: console

    $ nc [-options] [HostName or IP] [PortNumber]
    $ nc -zvw10 192.168.0.1 22
    #    z: zero-I/O mode which is used for scanning
    #    v: verbose output
    #    w10: timeout wait 10 seconds

`nmap - Network exploration tool and security / port scanner <https://www.commandlinux.com/man-page/man1/nmap.1.html>`_
-----------------------------------------------------------------------------------------------------------------------

.. code-block:: console

    $ nmap [-options] [HostName or IP] [-p] [PortNumber]
    $ nmap 192.168.0.1 -p 22
    #    v: verbose output
    #    z: only scan for open ports

Using `telnet - user interface to the TELNET protocol <https://www.commandlinux.com/man-page/man1/telnet.1.html>`_

.. code-block:: console

    # Maybe not installed
    $ telnet [HostName or IP] [PortNumber]
    $ telnet 192.168.0.1 22


**Python:** `telnetlib — Telnet client <https://docs.python.org/3.11/library/telnetlib.html>`_
----------------------------------------------------------------------------------------------

.. warning:: 'telnetlib' was deprecated in Python 3.12 and removed in Python 3.13

.. code-block:: console

    $ python3.12 -c "import telnetlib; tel=telnetlib.Telnet('192.168.0.1','22',10); print(tel.host,tel.port); tel.close()"
    $ python
    >>> import telnetlib
    >>> tel = telnetlib.Telnet('192.168.0.1', 22, 10) # 10 second timeout
    >>> print(tel.host, tel.port) # 192.168.0.1 22
    >>> tel.close()
    >>> exit()

**Python:** `socket — Low-level networking interface <https://docs.python.org/3/library/socket.html>`_
------------------------------------------------------------------------------------------------------

.. code-block:: console

    $ python3 -c "import socket; s = socket.socket(); s.settimeout(10); s.connect(('192.168.0.1', 22)); print(s)"
    $ python3
    >>> import socket
    >>> s = socket.socket()
    >>> s.settimeout(10)
    >>> s.connect(('192.168.0.1', 22))
    >>> print(s) # "<socket.socket fd=1376, family=2, type=1, proto=0, laddr=('127.0.0.1', 52243), raddr=('192.168.0.1', 22)>"
    >>> exit()

`curl - transfer a URL <https://www.man7.org/linux/man-pages/man1/curl.1.html>`_
--------------------------------------------------------------------------------

cURL can do *much much more* see, `cURL - The Ultimate Reference Guide <https://www.petergirnus.com/blog/curl-command-line-ultimate-reference-guide>`_
and `Everything curl <https://everything.curl.dev/http/post/simple.html>`_

.. code-block:: console

    $ curl -v telnet://<remote server>:port
    $ curl -v telnet://192.168.0.1:22

Linux Network Tools
===================

+----------------------------------------------------------------------+----------------------------------------------------+
| Command                                                              | Description                                        |
+======================================================================+====================================================+
| `ping <https://man.cx/ping>`_                                        | Send ICMP ECHO_REQUEST to network hosts            |
| `ping6 <https://man.cx/ping6>`_                                      |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `hping3 <https://man.cx/hping3>`_                                    | TCP/IP equivalent of ping                          |
+----------------------------------------------------------------------+----------------------------------------------------+
| `curl <https://man.cx/curl>`_                                        | Access URL meta-data or content                    |
| `wget <https://man.cx/wget>`_                                        |                                                    |
| `HTTPie <https://httpie.io/docs/cli>`_                               |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `tc <https://man.cx/tc>`_                                            | Show / manipulate traffic control settings         |
+----------------------------------------------------------------------+----------------------------------------------------+
| `dig <https://man.cx/dig>`_                                          | DNS lookup utilities                               |
| `nslookup <https://man.cx/nslookup>`_                                |                                                    |
| `host <https://man.cx/host>`_                                        |                                                    |
| `whois <https://man.cx/whois>`_                                      |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ssh <https://man.cx/ssh>`_                                          | Secure client connection and copy                  |
| `scp <https://man.cx/scp>`_                                          |                                                    |
| `sftp <https://man.cx/sftp>`_                                        |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `telnet <https://man.cx/telnet>`_                                    | Insecure client connection and copy                |
| `ftp <https://man.cx/ftp>`_                                          |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `rsync <https://man.cx/rsync>`_                                      | Sophisticated remote/local file-copying            |
+----------------------------------------------------------------------+----------------------------------------------------+
| `tcpdump <https://man.cx/tcpdump>`_                                  | Dump and analyze network traffic                   |
| `wireshark <https://man.cx/wireshark>`_                              |                                                    |
| `tshark <https://man.cx/tshark>`_                                    |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ngrep <https://man.cx/ngrep>`_                                      | Network grep                                       |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ifconfig <https://man.cx/ifconfig>`_                                | Show/manipulate ip routing, devices, and tunnels   |
| `route <https://man.cx/route>`_                                      |                                                    |
| `ethtool <https://man.cx/ethtool>`_                                  |                                                    |
| `ip <https://man.cx/ip>`_                                            |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `iw <https://man.cx/iw>`_                                            | Configure a wireless network interface             |
| `iwconfig <https://man.cx/iwconfig>`_                                |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `nmap <https://man.cx/nmap>`_                                        | Network exploration tool and security/port scanner |
| `zenmap <https://man.cx/zenmap>`_                                    |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `p0f <https://man.cx/p0f>`_                                          | Identify remote systems passively                  |
+----------------------------------------------------------------------+----------------------------------------------------+
| `openvpn <https://man.cx/openvpn>`_                                  | Secure VPN tunnels                                 |
| `wireguard <https://www.wireguard.com/>`_                            |                                                    |
| `stunnel <https://man.cx/stunnel>`_                                  |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `nc <https://man.cx/nc>`_                                            | Arbitrary TCP and UDP connections and listeners    |
| `socat <https://man.cx/socat>`_                                      |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `netstat <https://man.cx/netstat>`_                                  | Troubleshoot connections, processes, file usage    |
| `ss <https://man.cx/ss>`_                                            | Dump socket statistics                             |
| `lsof <https://man.cx/lsof>`_                                        | List open files                                    |
| `fuser <https://man.cx/fuser>`_                                      | Identify processes using files or sockets          |
+----------------------------------------------------------------------+----------------------------------------------------+
| `iptables <https://man.cx/iptables>`_                                | Firewall, TCP/IP packet filtering and NAT          |
| `ip6tables <https://man.cx/iptables>`_                               |                                                    |
| `nftables <https://www.netfilter.org/projects/nftables/index.html>`_ |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `arp <https://man.cx/arp>`_                                          | Manipulate the system ARP cache                    |
| `arptables <https://man.cx/arptables>`_                              |                                                    |
+----------------------------------------------------------------------+----------------------------------------------------+
| `traceroute <https://man.cx/traceroute>`_                            | Print the route packets take to network host       |
| `mtr <https://man.cx/mtr>`_                                          | Combined traceroute and ping                       |
| `tcptraceroute <https://man.cx/tcptraceroute>`_                      | Traceroute implementation using TCP packets        |
+----------------------------------------------------------------------+----------------------------------------------------+
| `iptraf <https://man.cx/iptraf>`_                                    | Interactive Colorful IP LAN Monitor                |
| `nethogs <https://man.cx/nethogs>`_                                  | Net top tool grouping bandwidth per process        |
| `iftop <https://man.cx/iftop>`_                                      | Display bandwidth usage on an interface by host    |
| `ntop <https://man.cx/ntop>`_                                        | Display top network users                          |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ab <https://man.cx/ab>`_                                            | Apache HTTP server benchmarking tool               |
| `nload <https://man.cx/nload>`_                                      | Displays the current network usage                 |
| `iperf <https://man.cx/iperf>`_                                      | Throughput, latency, link capacity, responsiveness |
+----------------------------------------------------------------------+----------------------------------------------------+
| `ipcalc <https://man.cx/ipcalc>`_                                    | An IPv4 Netmask/broadcast/etc calculator           |
| `ipv6calc <https://man.cx/ipv6calc>`_                                | Format, calculate, show, filter IPv6/IPv4/MAC      |
+----------------------------------------------------------------------+----------------------------------------------------+
| `nsenter <https://man.cx/nsenter>`_                                  | Run program in different namespaces                |
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

.. note:: Fedora 37, 38 and 39 `Install media don’t boot in UEFI mode on certain motherboards <https://discussion.fedoraproject.org/t/install-media-dont-boot-in-uefi-mode-on-certain-motherboards/71376>`_

Of course backup everything you want to keep because you are going to reformat the HDD or SSD!

The *live* installation is process is well documented and robust so simply follow:

* `Download Fedora 36 Workstation <https://fedoraproject.org/en/workstation/download/>`_
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
