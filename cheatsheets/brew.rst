git:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/brew.rst


***************************
Brew / Brew Cask Cheatsheet
***************************


Useful Links
============

* `HomeBrew - The missing package manager for macOS (or Linux) <https://brew.sh/>`_
* `HomeBrew Installation <http://0pointer.de/blog/projects/systemd-docs.html>`_


Basic Command Comparison
========================

::

 Example usage:
   brew search [TEXT|/REGEX/]
   brew info [FORMULA...]
   brew install FORMULA...
   brew update
   brew upgrade [FORMULA...]
   brew uninstall FORMULA...
   brew list [FORMULA...]

 Troubleshooting:
   brew config
   brew doctor
   brew install --verbose --debug FORMULA

 Contributing:
   brew create [URL [--no-fetch]]
   brew edit [FORMULA...]

 Further help:
   brew commands
   brew help [COMMAND]
   man brew
   https://docs.brew.sh

Brew Update vs Upgrade
======================

The **"update"** updates Homebrew itself, where as **"upgrade"** updates the installed packages.

::

  $ brew update            # update the formulae and Homebrew itself
  $ brew outdated          #  what is outdated
  $ brew upgrade           # Upgrade everything
  $ brew upgrade <formula> # Or upgrade a specific formula
  
  
HomeBrew Casks
==============

Homebrew-Cask is an extension built on top of `HomeBrew <https://brew.sh/>`_ which speeds up the 
installation process of large binary files with the use of the Terminal App. Applications such 
as Google Chrome, Firefox, Alfred, and Docker can be easily installed without having to 
download the .dmg file. 

::

    $ brew cask install firefox

* `Listing of all casks available via the Homebrew package manager <https://formulae.brew.sh/cask/>`_


Fixing the pesky 'depends_on macos' value: ":lion"
--------------------------------------------------

* `Fixing casks with **depends_on** that reference pre-Mavericks <https://github.com/Homebrew/homebrew-cask/issues/58046>`_

Catalina Upgrade
================

Unsurprisingly ``brew`` is broken by the upgrade and the effects of trying to force ``zsh`` as the default shell need to be seen.

* `Use zsh as the default shell on your Mac <https://support.apple.com/en-us/HT208050>`_
* `MacOS Catalina <https://www.apple.com/macos/catalina/>`_
* `Why macOS Catalina is breaking so many apps, and what to do about it <https://www.theverge.com/2019/10/12/20908567/apple-macos-catalina-breaking-apps-32-bit-support-how-to-prepare-avoid-update>`_

Steps taken post Catlaina upgrade

::

  $ brew doctor   # report git missing and other issues
  $ brew update   # update brew, to fix git warning
  $ brew upgrade  # upgrade just to be safe

  $ brew doctor # now complains of missing xcode and ``sbin`` not being in your path.
  $ xcode-select --install
  $ echo 'export PATH="/usr/local/sbin:$PATH"' >> ~/.bash_profile
  $ brew doctor # still report missing ``sbin`` need to exist and open a new terminal

  $ brew doctor       # reports clean
  $ brew cask list    # good my casks are still there
  $ brew cask upgrade # nothing to be upgraded.




