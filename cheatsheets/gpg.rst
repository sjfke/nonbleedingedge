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
    $ gpg --gen-key
    $ gpg --list-keys
    $ gpg --list-secret-keys
    $ gpg --output geoffreycollis-hotmail-pub.gpg --armor --export geoffreycollis@hotmail.com
    $ gpg --output sjfke-pool-shark-hotmail-pub.gpg --armor --export 49220AC61317062D


Git GPG integrations
====================

* `Telling Git about your signing key <https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key>`_
* `Use GPG Signing Keys with Git (and GitHub) on Windows 10 <https://medium.com/@ryanmillerc/use-gpg-signing-keys-with-git-on-windows-10-github-4acbced49f68>`_
* `Git Tools - Signing Your Work <https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work>`_

.. code-block:: console

    $ gpg --list-secret-keys --keyid-format=long | select-string @('sec ', 'uid ')
    sec   ed25519/09D708FAED728E4C 2022-07-27 [SC] [expires: 2024-07-27]
    uid                 [ultimate] Geoffrey Collis <geoffreycollis@hotmail.com>
    sec   ed25519/49220AC61317062D 2023-03-31 [SC] [expires: 2024-01-25]
    uid                 [ultimate] Sjfke <sjfke.pool.shark@hotmail.com>

    # Global auto-sign commits
    $ git config --global --list
    $ git config --global user.email geoffreycollis@hotmail.com
    $ git config --global user.signingkey 09D708FAED728E4C
    $ git config --global commit.gpgsign true

    # On Windows
    $ C:\Windows\System32\where.exe gpg # C:\Program Files (x86)\GnuPG\bin\gpg.exe
    $ git config --global gpg.program "C:\Program Files (x86)\GnuPG\bin\gpg.exe"

    # Project (local) auto-sign commits
    $ git config --local --list
    $ git config --local user.email sjfke.pool.shark@hotmail.com
    $ git config --local user.signingkey 49220AC61317062D
    $ git config --local commit.gpgsign true

For `GitHub <https://github.com>`_  add these keys to `SSH and GPG keys <https://github.com/settings/keys>`_

Exporting GPG keys
==================

.. note:: Private key(s) will prompt for a pass-phrase

.. code-block:: console

    $ gpg --list-keys --keyid-format LONG                                                      # public keys
    $ gpg --list-secret-keys --keyid-format LONG                                               # private keys

    $ gpg --output export-public.gpg --armor --export sjfke.pool.shark@hotmail.com             # public key
    $ gpg --output export-private.gpg --armor --export-secret-key sjfke.pool.shark@hotmail.com # private key

Backup or Transfer GPG keys
===========================

.. note:: Each private key will prompt for it's pass-phrase

* `How to export a GPG private key and public key to a file <https://hackerthink.com/solutions/how-to-export-a-gpg-private-key-and-public-key-to-a-file/>`_
* `How-To-Geek Back Up and Restore Your GPG Keys on Linux <https://www.howtogeek.com/816878/how-to-back-up-and-restore-gpg-keys-on-linux/>`_
* `JWillikers  Backup and Restore GPG key<https://www.jwillikers.com/backup-and-restore-a-gpg-key>`_

.. code-block:: console

    $ gpg --list-keys --keyid-format LONG                                               # public keys
    $ gpg --list-secret-keys --keyid-format LONG                                        # private keys

    # All keys
    $ gpg --export --export-options backup --output backup-all-public.gpg               # public keys
    $ gpg --export-secret-keys --export-options backup --output backup-all-private.gpg  # private keys
    $ gpg --export-ownertrust > backup-all-trust.gpg                                    # trust database

    # Single key only
    $ gpg --export-secret-keys --export-options backup --output backup-private.gpg sjfke.pool.shark@hotmail.com
    $ gpg --export-secret-keys --export-options backup --output backup-private.gpg sjfke.pool.shark@hotmail.com
