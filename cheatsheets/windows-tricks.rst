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

.. code-block:: console

    $ dsim.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all
    $ dsim.exe /online /enable-feature /featurename:VirtualMachinePlatform /norestart

Reboot your computer.

From the ``Microsoft Store`` install ``Windows Subsystem for Linux`` and ``Ubuntu 22.04.2 LTS`` or ``Ubuntu``.

Alternatively directly install ``Ubuntu`` from the command line.

.. code-block:: console

    $ wsl --install

A further reboot maybe necessary, but ``Ubuntu 22.04.2 LTS`` or ``Ubuntu`` should now work.

.. code-block:: console

    $ wsl --list
    $ wsl --help
    $ wsl
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

.. code-block::

    $ Get-ExecutionPolicy -List

            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser    RemoteSigned
     LocalMachine       Undefined

* `Oh My Posh Docs <https://ohmyposh.dev/docs>`_
* `Nerd Fonts <https://www.nerdfonts.com/>`_
* `Meslo LGM NF download <https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/Meslo.zip>`_

1. Install `Windows Terminal <https://github.com/microsoft/terminal>`_ from the ``Microsoft Store``

2. Install ``oh-my-posh`` from the ``Microsoft Store``, or from the command line.

.. code-block:: console

    $ winget install JanDeDobbeleer.OhMyPosh -s

3. Download `Meslo LGM NF fonts <https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/Meslo.zip>`_ and unzip them.

4. In the font folder select all the 73 font files, ``.ttf`` and `right-click` to install them.

5. Open `Windows Terminal <https://github.com/microsoft/terminal>`_

    * ``Settings`` > ``Windows PowerShell`` > ``Appearance`` > ``Color Scheme`` choose ``Campbell PowerShell``
    * ``Settings`` > ``Windows PowerShell`` > ``Appearance`` > ``Font face`` choose ``MesloLGM Nerd Font``

6. Configure  `Oh My Posh prompt <https://ohmyposh.dev/docs/installation/prompt>`_ by choosing a `Theme <https://ohmyposh.dev/docs/themes>`_

.. code-block:: console

    $ Test-Path $PROFILE -PathType Leaf         # If FALSE, then create it using New-Item
    $ New-Item -Path $PROFILE -Type File -Force # Create the PowerShell_profile.ps1 file

    $ notepad $PROFILE                          # Choose your theme and Invoke it

    $ Get-Content -Path $PROFILE
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\paradox.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\dracula.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\remk.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\jtracey93.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\mt.omp.json" | Invoke-Expression
    oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\agnoster.omp.json" | Invoke-Expression
    # oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\agnosterplus.omp.json" | Invoke-Expression

    $ . $PROFILE                                # If errors open a new PowerShell

Update notifications via the ``Microsoft Store`` do not work, ``oh-my-posh`` update command line update alerts
do not always trigger, so manually check on a regular basis, see
`Oh My Posh upgrades <https://ohmyposh.dev/docs/installation/windows#update>`_

.. code-block:: console

    $ oh-my-posh notice                                # Is an upgrade is available?

    $ oh-my-posh version                               # Existing version
    $ winget upgrade JanDeDobbeleer.OhMyPosh -s winget # Upgrade
    $ oh-my-posh version                               # New version

Summary of the ``oh-my-posh`` commands

.. code-block:: console

    $ oh-my-posh help        # help summary
    $ oh-my-posh help --help # help on the 'help' command

Use ``Terminal Icons`` to add color and icons to ``oh-my-posh`` directory listings

.. code-block:: console

    $ Install-Module -Name Terminal-Icons -Repository PSGallery -Scope CurrentUser
    $ Import-Module -Name Terminal-Icons

    # Add to $PROFILE
    $ Get-Content -Path $PROFILE
    oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\agnoster.omp.json" | Invoke-Expression
    Import-Module -Name Terminal-Icons

.. warning:: Exercise caution when installing from `PowerShell Gallery <https://www.powershellgallery.com/>`_

Want more, see `My Ultimate PowerShell prompt with Oh My Posh and the Windows Terminal <https://www.hanselman.com/blog/my-ultimate-powershell-prompt-with-oh-my-posh-and-the-windows-terminal>`_

Are Files Identical?
====================

One novel approach is to use ``certutil`` to compute a hash to see if they are the same.

* ``certutil`` supports hash algorithms: ``MD2``, ``MD4``, ``MD5``, ``SHA1``, ``SHA256``, ``SHA384`` ``SHA512``
* Commonly used hash algorithms being, ``SHA1`` default, ``MD5`` and ``SHA256``

.. code-block:: console

    $ certutil -hashfile file1.txt
    SHA1 hash of file1.txt:
    2236964ee87bff078491008b506044391975e2a6
    CertUtil: -hashfile command completed successfully.

    $ certutil -hashfile file1.txt MD5
    MD5 hash of file1.txt:
    4ead6a1f65b3f97d86a093dfb87a8be2
    CertUtil: -hashfile command completed successfully.

    $ certutil -hashfile file1.txt SHA256
    SHA256 hash of file1.txt:
    dde3f13078dae2baf1d1a12ad3be20ce6cc0d370cbab0f579fca16dcc4791394
    CertUtil: -hashfile command completed successfully.

    $ certutil -hashfile Fred_Flintstone.png SHA256
    SHA256 hash of Fred_Flintstone.png:
    a4c8843ce4fb12654ccbe7aa14256c7e0243739d42874d42b531e74bc27ba32c
    CertUtil: -hashfile command completed successfully.

    $ sha256_hash = Invoke-Expression "certutil -hashfile Fred_Flintstone.png SHA256 | Select-Object -Index 1"
    $ write($sha256_hash) # a4c8843ce4fb12654ccbe7aa14256c7e0243739d42874d42b531e74bc27ba32c

    $ certutil -hashfile .\kustomize.exe SHA256
    SHA256 hash of .\kustomize.exe:
    2cd041a2e4d3533ffa6f5f03dc2d9e0828bae7931021cc5d11dfcd644bd8b4c0
    CertUtil: -hashfile command completed successfully.

Utility `certutil <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil>`_ is
intended for manipulating certificates and so can do much more.

Base 64 Encode/Decode
=====================

.. code-block:: console

    $ [Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("EncodeMe-in-Base64"))
    RW5jb2RlTWUtaW4tQmFzZTY0

    $ [System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String('RW5jb2RlTWUtaW4tQmFzZTY0'))
    EncodeMe-in-Base64

Using ``wsl``, if installed

.. code-block:: console

    $ wsl
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