:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/brew.rst

###############
Brew Cheatsheet
###############

************
Useful Links
************

* `Homebrew - The missing package manager for macOS (or Linux) <https://brew.sh/>`_
* `Install Homebrew - Complete Guide <https://mac.install.guide/homebrew/>`_ by Daniel Kehoe

**************
Basic Commands
**************

.. code-block:: console

    # Example usage:
    $ brew search [TEXT|/REGEX/]
    $ brew info [FORMULA...]
    $ brew install FORMULA...
    $ brew update
    $ brew upgrade [FORMULA...]
    $ brew uninstall FORMULA...
    $ brew list [FORMULA...]

    # Troubleshooting:
    $ brew config
    $ brew doctor
    $ brew install --verbose --debug FORMULA

    # Contributing:
    $ brew create [URL [--no-fetch]]
    $ brew edit [FORMULA...]

    # Further help:
    $ brew commands
    $ brew help [COMMAND]
    $ man brew

* `Homebrew Documentation <https://docs.brew.sh>`_

*****************
Homebrew Updating
*****************

* ``brew update`` to refresh the package definitions
* ``brew upgrade`` to install the lastest version of the installed packages

Typical workflow

.. code-block:: console

    $ brew update  [--verbose]  # update the formulae and Homebrew itself
    $ brew upgrade [--verbose]  # upgrade installed packages

Full workflow

.. code-block:: console

    $ brew doctor  [--verbose]  # ensure brew is clean and consistent
    $ brew update  [--verbose]  # update the formulae and Homebrew itself
    $ brew outdated             # what packages are outdated
    $ brew upgrade [--verbose]  # upgrade installed packages
    $ brew upgrade <formula>    # upgrade a specific formula
    $ brew doctor  [--verbose]  # ensure brew is still clean and consistent


**************
Homebrew Casks
**************

The ``--cask`` extension is built on top of `Homebrew <https://brew.sh/>`_ to simplify the
installation and updating of applications such as `Google Chrome <https://www.google.com/chrome/>`_,
`Firefox <https://www.mozilla.org/en-US/firefox/new/>`_, `Alfred <https://www.alfredapp.com/>`_,
`Docker <https://www.docker.com/>`_ etc. (avoids manually downloading and installing the ``.dmg`` file)

.. code-block:: console

    $ brew search --cask firefox                 # search, incomplete names permitted
    $ brew install --cask [--verbose] firefox    # install
    $ brew uninstall --cask [--verbose] firefox  # uninstall


* `Browsing all casks available via the Homebrew package manager <https://formulae.brew.sh/cask/>`_
