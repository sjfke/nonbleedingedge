:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/windows-tricks.rst

*************************
Windows Tricks Cheatsheet
*************************

WSL - Windows Subsystem for Linux
=================================

* `How to download and install Linux <https://learn.microsoft.com/en-us/linux/install>`_
* `How to install Linux on Windows with WSL <https://learn.microsoft.com/en-us/windows/wsl/install-manual>`_

Before you can install ``WSL 2`` it is necessary to ensure your processor is capable of supporting Virtualization,
and ``VT-x`` or ``AMD-V`` is enabled in the BIOS.

* `How to Find Out If Intel VT-x or AMD-V Virtualization Technology is Supported? <https://www.auslogics.com/en/articles/how-to-find-out-if-intel-vt-x-or-amd-v-virtualization-technology-is-supported/>`_

Next make sure `Virtualization` is configured in ``Windows``, search for ``Turn Windows features on or off``

* ``Virtual Machine Platform`` - enabled
* ``Windows Subsystem for Linux`` - enabled
* ``Windows Hypervisor Platform`` - only enable if you want Hyper-V and have a license that supports it

It should also be possible to do this from the command line

.. code-block:: pwsh-session

    PS> dsim.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all
    PS> dsim.exe /online /enable-feature /featurename:VirtualMachinePlatform /norestart

Reboot your computer.

From the ``Microsoft Store`` install ``Windows Subsystem for Linux`` and ``Ubuntu 22.04.2 LTS`` or ``Ubuntu``.

Alternatively directly install ``Ubuntu`` from the command line.

.. code-block:: pwsh-session

    PS> wsl --install

A further reboot maybe necessary, but ``Ubuntu 22.04.2 LTS`` or ``Ubuntu`` should now work.

.. code-block:: pwsh-session

    PS> wsl --list
    PS> wsl --help
    PS> wsl
    Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.90.1-microsoft-standard-WSL2 x86_64)

     * Documentation:  https://help.ubuntu.com
     * Management:     https://landscape.canonical.com
     * Support:        https://ubuntu.com/advantage

    sjfke@wallace:~$                       # UNIX home directory, /home/sjfke
    sjfke@wallace:~$ cd /mnt/c/Users/geoff # Change to Windows home directory
    sjfk@eWALLACE:/mnt/c/Users/geoff$ ls   # Windows home directory


Oh My Posh
==========

.. note:: Laptop must be configured to run scripts, `PowerShell  Scripting Cheatsheet - Introduction <https://nonbleedingedge.com/cheatsheets/powershell-scripts.html#introduction>`_

For all users

.. code-block:: pwsh-session

    PS> Get-ExecutionPolicy -List

            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser       Undefined
     LocalMachine       RemoteSigned

For just for your account

.. code-block:: pwsh-session

    PS> Get-ExecutionPolicy -List

            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser    RemoteSigned
     LocalMachine       Undefined


* `Oh My Posh Docs <https://ohmyposh.dev/docs>`_
* `PowerShell - Customizing your shell environment <https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/creating-profiles>`_
* `PowerShell - about_Profiles <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles/>`_
* `Nerd Fonts <https://www.nerdfonts.com/>`_
* `Meslo LGM NF font download <https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/Meslo.zip>`_

.. warning:: `Oh My Posh <https://ohmypo.sh/docs>`_ installation and configuration instructions are **incorrect**

1. Install `Windows Terminal <https://github.com/microsoft/terminal>`_ from the ``Microsoft Store``

2. Install ``oh-my-posh`` from the ``Microsoft Store``, the ``winget`` command line **does not** work properly.

3. Check the ``oh-my-posh`` installation

.. code-block:: pwsh-session

    PS> get-childitem Env: | where {$_.Name -like 'POSH*' -or $_.Name -like 'POWER*'}
    Name                           Value
    ----                           -----
    POSH_CURSOR_COLUMN             1
    POSH_CURSOR_LINE               7
    POSH_INSTALLER                 ws
    POSH_SESSION_ID                81500ca2-d587-4be6-8429-d38ca5c50117
    POSH_SHELL                     pwsh
    POSH_SHELL_VERSION             5.1.26100.7462
    POSH_THEMES_PATH               C:\Users\sjfke\AppData\Local\Programs\oh-my-posh\themes\
    POWERLINE_COMMAND              oh-my-posh

4. Install ``Meslo LGM NF fonts`` which include the required ``Nerd fonts``.

.. code-block:: pwsh-session

    PS> oh-my-posh font install meslo

5. Open `Windows Terminal <https://github.com/microsoft/terminal>`_

    * ``Settings`` > ``Windows PowerShell`` > ``Appearance`` > ``Color Scheme`` choose ``Campbell PowerShell``
    * ``Settings`` > ``Windows PowerShell`` > ``Appearance`` > ``Font face`` choose ``MesloLGM Nerd Font``

6. Configure  `Oh My Posh prompt <https://ohmyposh.dev/docs/installation/prompt>`_ by choosing a `Theme <https://ohmyposh.dev/docs/themes>`_

.. warning:: `Oh My Posh <https://ohmypo.sh/docs>`_ configuration instructions are **incorrect**, the following works

.. code-block:: pwsh-session

    PS> Test-Path $PROFILE -PathType Leaf         # If FALSE, then create it using New-Item
    PS> New-Item -Path $PROFILE -Type File -Force # Create the PowerShell_profile.ps1 file

    PS> notepad $PROFILE                          # Choose your theme and update your profile

    PS> Get-Content -Path $PROFILE
    # oh-my-posh init pwsh | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\paradox.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\dracula.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\remk.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\jtracey93.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\mt.omp.json" | Invoke-Expression
    oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\agnoster.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\agnosterplus.omp.json" | Invoke-Expression

    # This will probably fail, documentation is incorrect
    PS> . $PROFILE                                # IGNORE errors

Open the ``Terminal`` from the task bar, and the PowerShell should be using your chosen theme.

``Microsoft Store`` will provide update notifications, but to do manually.

.. code-block:: pwsh-session

    PS> oh-my-posh notice                                # Upgrade available? (unreliable)
    PS> oh-my-posh version                               # Existing version
    PS> winget upgrade JanDeDobbeleer.OhMyPosh -s winget # Upgrade (do weekly, upgrades are frequent)
    PS> oh-my-posh version                               # New version

Summary of the ``oh-my-posh`` commands

.. code-block:: pwsh-session

    PS> oh-my-posh help        # help summary
    PS> oh-my-posh help --help # help on the 'help' command

It is recommended to use ``Terminal Icons`` to add color and icons to ``PowerShell`` directory listings,
for your account ``-Scope CurrentUser``, and for all users ``-Scope LocalMachine``.

.. code-block:: pwsh-session

    PS> Install-Module -Name Terminal-Icons -Repository PSGallery -Scope CurrentUser
    PS> Import-Module -Name Terminal-Icons

    # Append to $PROFILE
    PS> Get-Content -Path $PROFILE
    oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\agnoster.omp.json" | Invoke-Expression
    Import-Module -Name Terminal-Icons

Want more, see `My Ultimate PowerShell prompt with Oh My Posh and the Windows Terminal <https://www.hanselman.com/blog/my-ultimate-powershell-prompt-with-oh-my-posh-and-the-windows-terminal>`_

.. warning:: Exercise caution when installing from `PowerShell Gallery <https://www.powershellgallery.com/>`_

Updating Git For Windows
========================

`Git for Windows <https://gitforwindows.org/>`_ We bring the awesome Git SCM to Windows

.. code-block:: pwsh-session

    PS> git update-git-for-windows
    Git for Windows 2.50.0.windows.2 (64-bit)
    Update 2.50.1.windows.1 is available
    Download and install Git for Windows 2.50.1 [N/y]? y
    ######################################################################################### 100.0%
    PS> git update-git-for-windows
    Git for Windows 2.50.1.windows.1 (64-bit)
    Up to date

Are Files Identical?
====================

One novel approach is to use ``certutil`` to compute a hash to see if they are the same.

* ``certutil`` supports hash algorithms: ``MD2``, ``MD4``, ``MD5``, ``SHA1``, ``SHA256``, ``SHA384`` ``SHA512``
* Commonly used hash algorithms being, ``SHA1`` default, ``MD5`` and ``SHA256``

.. code-block:: pwsh-session

    PS> certutil -hashfile file1.txt
    SHA1 hash of file1.txt:
    2236964ee87bff078491008b506044391975e2a6
    CertUtil: -hashfile command completed successfully.

    PS> certutil -hashfile file1.txt MD5
    MD5 hash of file1.txt:
    4ead6a1f65b3f97d86a093dfb87a8be2
    CertUtil: -hashfile command completed successfully.

    PS> certutil -hashfile file1.txt SHA256
    SHA256 hash of file1.txt:
    dde3f13078dae2baf1d1a12ad3be20ce6cc0d370cbab0f579fca16dcc4791394
    CertUtil: -hashfile command completed successfully.

    PS> certutil -hashfile Fred_Flintstone.png SHA256
    SHA256 hash of Fred_Flintstone.png:
    a4c8843ce4fb12654ccbe7aa14256c7e0243739d42874d42b531e74bc27ba32c
    CertUtil: -hashfile command completed successfully.

    PS> sha256_hash = Invoke-Expression "certutil -hashfile Fred_Flintstone.png SHA256 | Select-Object -Index 1"
    PS> write($sha256_hash) # a4c8843ce4fb12654ccbe7aa14256c7e0243739d42874d42b531e74bc27ba32c

    PS> certutil -hashfile .\kustomize.exe SHA256
    SHA256 hash of .\kustomize.exe:
    2cd041a2e4d3533ffa6f5f03dc2d9e0828bae7931021cc5d11dfcd644bd8b4c0
    CertUtil: -hashfile command completed successfully.

Utility `certutil <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil>`_ is
intended for manipulating certificates and so can do much more.

Base 64 Encode/Decode
=====================

.. code-block:: pwsh-session

    PS> [Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("EncodeMe-in-Base64"))
    RW5jb2RlTWUtaW4tQmFzZTY0

    PS> [System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String('RW5jb2RlTWUtaW4tQmFzZTY0'))
    EncodeMe-in-Base64

Using ``wsl``, if installed

.. code-block:: console

    PS> wsl
    $ echo -n 'EncodeMe-in-Base64' | base64
    RW5jb2RlTWUtaW4tQmFzZTY0

    $ echo -n 'RW5jb2RlTWUtaW4tQmFzZTY0' | base64 -d
    EncodeMe-in-Base64

Using ``Python``, if installed

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

JSON, YAML File Filtering
=========================

* ``jq`` is a lightweight command-line JSON processor, similar to ``sed``.
* ``yq`` is a Python command-line (``jq`` wrapper) YAML/XML processor.

.. code-block:: pwsh-session

    # Installation
    PS> winget install jqlang.jq

    # Command Line examples
    PS> Write-Output '{"fruit":{"name":"apple","color":"green","price":1.20}}' | jq '.' # pretty-print
    {
      "fruit": {
        "name": "apple",
        "color": "green",
        "price": 1.2
      }
    }

    # {JSON} Placeholder - Free fake and reliable API for testing and prototyping.
    PS> Invoke-RestMethod -uri https://jsonplaceholder.typicode.com/todos/1 | ConvertTo-Json -Depth 10 | jq '.'
    {
      "userId": 1,
      "id": 1,
      "title": "delectus aut autem",
      "completed": false
    }

    # Get International Space Station Current Location
    PS> Invoke-RestMethod -uri http://api.open-notify.org/iss-now.json | ConvertTo-Json -Depth 10 | jq '.'
    # -or-
    PS> Invoke-RestMethod -uri http://api.open-notify.org/iss-now.json -outfile iss-now.json
    PS> jq '.' .\iss-now.json # pretty-print
    {
      "message": "success",
      "iss_position": {
        "latitude": "-1.5479",
        "longitude": "-51.8420"
      },
      "timestamp": 1719839316
    }

.. code-block:: pwsh-session

    # Installation
    PS> winget install --id MikeFarah.yq

    # Command Line examples
    PS> Write-Output '{"fruit":{"name":"apple","color":"green","price":1.20}}' | yq '.'
    {"fruit": {"name": "apple", "color": "green", "price": 1.20}}

    # {JSON} Placeholder - Free fake and reliable API for testing and prototyping.
    PS> Invoke-RestMethod -uri https://jsonplaceholder.typicode.com/todos/1 | ConvertTo-Json -Depth 10 | yq '.'
    {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}

    # Get International Space Station Current Location
    PS> Invoke-RestMethod -uri http://api.open-notify.org/iss-now.json | ConvertTo-Json -Depth 10 | yq '.'
    # -or-
    PS> Invoke-RestMethod -uri http://api.open-notify.org/iss-now.json -outfile iss-now.json
    PS> yq '.' .\iss-now.json # pretty-print
    {
      "message": "success",
      "iss_position": {
        "latitude": "-32.9725",
        "longitude": "-24.9078"
      },
      "timestamp": 1719839968
    }

* `JSON Examples, see "jq JSON Cheatsheet" <https://nonbleedingedge.com/cheatsheets/jq.html>`_
* `YAML, JSON Examples, see "yq YAML/JSON Cheatsheet" <https://nonbleedingedge.com/cheatsheets/yq.html>`_
* `{JSON} Placeholder <https://jsonplaceholder.typicode.com/>`_ Free fake and reliable API for testing and prototyping.

Wipe a USB drive on Windows 11
==============================

Start a `CMD` shell as `Administrator`

.. code-block:: bat

    C:\Windows\System32>diskpart
    DISKPART> list disk

      Disk ###  Status         Size     Free     Dyn  Gpt
      --------  -------------  -------  -------  ---  ---
      Disk 0    Online          476 GB  2048 KB        *
      Disk 1    Online           57 GB      0 B        *

    DISKPART> select disk 1

    Disk 1 is now the selected disk.

    DISKPART> clean all

.. note:: The `clean all` may appear to hang, unplug USB device if this happens.

Testing Remote Connections
==========================

The examples are testing for ``SSH`` daemon (port 22) on host ``192.168.0.1``

Test-NetConnection
------------------

``PowerShell`` provides `Test-NetConnection <https://learn.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection>`_

.. code-block:: pwsh-session

    PS> Test-NetConnection -ComputerName 192.168.0.1 -Port 22
    PS> get-help Test-NetConnection

**Python:** `telnetlib — Telnet client <https://docs.python.org/3.11/library/telnetlib.html>`_
----------------------------------------------------------------------------------------------

.. warning:: 'telnetlib' was deprecated in Python 3.12 and removed in Python 3.13

.. code-block:: pwsh-session

    PS> python3.12 -c "import telnetlib; tel=telnetlib.Telnet('192.168.0.1','22',10); print(tel.host,tel.port); tel.close()"
    PS> python
    >>> import telnetlib
    >>> tel = telnetlib.Telnet('192.168.0.1', 22, 10) # 10 second timeout
    >>> print(tel.host, tel.port) # 192.168.0.1 22
    >>> tel.close()
    >>> exit()

**Python:** `socket — Low-level networking interface <https://docs.python.org/3/library/socket.html>`_
------------------------------------------------------------------------------------------------------

.. code-block:: pwsh-session

    PS> python3 -c "import socket; s = socket.socket(); s.settimeout(10); s.connect(('192.168.0.1', 22)); print(s)"
    PS> python3
    >>> import socket
    >>> s = socket.socket()
    >>> s.settimeout(10)
    >>> s.connect(('192.168.0.1', 22))
    >>> print(s) # "<socket.socket fd=1376, family=2, type=1, proto=0, laddr=('127.0.0.1', 52243), raddr=('192.168.0.1', 22)>"
    >>> exit()

`curl - transfer a URL <https://www.man7.org/linux/man-pages/man1/curl.1.html>`_
--------------------------------------------------------------------------------

cURL can do *much much more* see, :ref:`curl-on-windows`

.. code-block:: pwsh-session

    PS> winget install cURL.cURL                  # installation
    PS> curl.exe -v telnet://<remote server>:port # typical command
    PS> curl.exe -v telnet://192.168.0.1:22       # test

.. _curl-on-windows:

cURL on Windows
===============

There are a vast amount of use-cases for curl, such as:

* FTP upload, Proxy support, SSL connections, HTTP post

It also supports the use of all the following protocols: ``DICT``, ``FILE``, ``FTP``, ``FTPS``, ``GOPHER``, ``HTTP``,
``HTTPS``, ``IMAP``, ``IMAPS``, ``LDAP``, ``LDAPS``, ``POP3``, ``POP3S``, ``RTMP``, ``RTSP``, ``SCP``, ``SFTP``,
``SMB``, ``SMBS``, ``SMTP``, ``SMTPS``, ``TELNET``, and ``TFTP``.

* `curl - transfer a URL <https://www.man7.org/linux/man-pages/man1/curl.1.html>`_
* `cURL - The Ultimate Reference Guide <https://www.petergirnus.com/blog/curl-command-line-ultimate-reference-guide>`_
* `keycdn - Popular curl Examples <https://www.keycdn.com/support/popular-curl-examples>`_
* `Everything curl <https://everything.curl.dev/http/post/simple.html>`_

cURL installation
-----------------

.. code-block:: pwsh-session

    # Package Installation: '%localappdata%\Microsoft\WinGet\Packages'
    # Package Links: '%localappdata%\Microsoft\WinGet\Links\'
    PS> winget install cURL.cURL # installation
    PS> winget list curl         # version installed
    PS> curl.exe -h              # help

.. warning:: Use ``curl.exe`` because ``Invoke-WebRequest`` has a ``curl`` alias

cURL examples
-------------

.. code-block:: pwsh-session

    PS> curl.exe https://www.nonbleedingedge.com  # HTTP GET
    PS> curl.exe -I https://nonbleedingedge.com   # get HTTP headers
    PS> curl.exe -D - https://nonbleedingedge.com # store the HTTP headers that a site sends back

    PS> curl.exe -o favicon.ico https://nonbleedingedge.com/_static/favicon.ico # get/save icon image

    PS> curl.exe --request POST https://nonbleedingedge.com   # examples see 'Everything curl' URL above
    PS> curl.exe --request DELETE https://nonbleedingedge.com # examples see 'Everything curl' URL above
    PS> curl.exe --request PUT https://nonbleedingedge.com    # examples see 'Everything curl' URL above

    PS> curl.exe -v telnet://<remote server>:port # test remote connection
    PS> curl.exe -v telnet://192.168.0.1:22 # test for ssh (port 22) on server 192.168.0.1

Simple `PUT <https://blog.marcnuri.com/curl-put-request-examples>`_ and `DELETE <https://blog.marcnuri.com/curl-delete-request-examples>`_ examples