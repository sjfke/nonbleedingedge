:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/brew.rst


***************************
Brew / Brew Cask Cheatsheet
***************************


Useful Links
============

* `HomeBrew - The missing package manager for macOS (or Linux) <https://brew.sh/>`_
* `Install Homebrew - Complete Guide <https://mac.install.guide/homebrew/>`_ by Daniel Kehoe


Basic Commands
==============

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

.. code-block:: console

    $ brew doctor            # ensure brew is clean and consistent
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

.. code-block:: console

    $ brew cask install firefox

* `Listing of all casks available via the Homebrew package manager <https://formulae.brew.sh/cask/>`_
