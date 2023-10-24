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

    sjfke@WALLACE:/mnt/c/Users/geoff$

Oh My Posh
==========

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

    $ notepad $PROFILE                          # If errors create it, using New-Item
    $ New-Item -Path $PROFILE -Type File -Force # Create $PROFILE
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


