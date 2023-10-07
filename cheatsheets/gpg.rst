:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/brew.rst


*********************
The GNU Privacy Guard
*********************

.. attention:: Fledgling page, needs more work

Useful Links
============
* `The GNU Privacy Handbook <https://www.gnupg.org/gph/en/manual.pdf>`_
* `Generating a new GPG key <https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key>`_
* `Adding a GPG key to your GitHub account <https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account>`_
* `Telling Git about your signing key <https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key>`_


Basic Command Examples
======================

.. code-block:: console

    $ gpg --version
    $ gpg -gen-key
    $ gpg --list-keys
    $ gpg --list-secret-keys
    $ gpg --output geoffreycollis-hotmail-pub.gpg --armor --export geoffreycollis@hotmail.com
    $ gpg --output sjfke-pool-shark-hotmail-pub.gpg --armor --export 49220AC61317062D


Git GPG integrations
====================

.. code-block:: console

    $ git config --list
    $ git config commit.gpgsign true

    $ git config --local --list
    $ git config --local commit.gpgsign true
