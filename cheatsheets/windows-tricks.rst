:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/windows-tricks.rst

*************************
Windows Tricks Cheatsheet
*************************

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


