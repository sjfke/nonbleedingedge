:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/gpg.rst

#######################
GPG - GNU Privacy Guard
#######################

************
Useful Links
************

* `The GNU Privacy Handbook <https://www.gnupg.org/gph/en/manual.pdf>`_
* `Generating a new GPG key <https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key>`_
* `Adding a GPG key to your GitHub account <https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account>`_
* `Telling Git about your signing key <https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key>`_

**********************
Basic Command Examples
**********************

.. code-block:: console

    $ gpg --version                                   # gpg version - gpg (GnuPG) 2.4.0
    $ gpg --generate-key                              # (interactive) key generation
    $ gpg --list-keys                                 # list public keys
    $ gpg --list-secret-keys                          # list private keys
    $ gpg --fingerprint                               # list all fingerprints
    $ gpg --fingerprint sjfke.pool.shark@hotmail.com  # list specific fingerprint
    $ gpg --help

    $ gpg --output geoffreycollis-hotmail-pub.gpg --armor --export geoffreycollis@hotmail.com
    $ gpg --output sjfke-pool-shark-hotmail-pub.gpg --armor --export 49220AC61317062D

******************
GPG key generation
******************

.. code-block:: console

    $ gpg --generate-key
    gpg (GnuPG) 2.4.3; Copyright (C) 2023 g10 Code GmbH
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

    GnuPG needs to construct a user ID to identify your key.

    Real name: Fred (Frederick Flintstone)
    Email address: fred.flinstone@bedrock.ak
    You selected this USER-ID:
        "Fred (Frederick Flintstone) <fred.flintstone@bedrock.ak>"

    Change (N)ame, (E)mail, or (O)kay/(Q)uit? O
    We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.
    We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.
    gpg: revocation certificate stored as 'C:\\Users\\sjfke\\AppData\\Roaming\\gnupg\\openpgp-revocs.d\\44D306AEC3F45F976A9F9B24BDF6A4906F018A02.rev'
    public and secret key created and signed.

    pub   ed25519 2024-01-09 [SC] [expires: 2027-01-08]
          44D306AEC3F45F976A9F9B24BDF6A4906F018A02
    uid                      Fred (Frederick Flintstone) <fred.flintstone@bedrock.ak>
    sub   cv25519 2024-01-09 [E] [expires: 2027-01-08]


.. note:: Use ``gpg --full-generate-key`` to adjust expiry date etc.

*****************************
Sign and Encrypt/Decrypt Keys
*****************************

Notice, that ``--list-keys`` and ``--list-secret-keys`` produce the same output.

.. code-block:: console

    gpg --list-keys sjfke.pool.shark@hotmail.com
    pub   ed25519 2024-03-05 [SC] [expires: 2027-03-05]
          2B0A468BE38C555D1EBB89A20045294821C0C792
    uid           [ultimate] Sjfke (Hotmail) <sjfke.pool.shark@hotmail.com>
    sub   cv25519 2024-03-05 [E] [expires: 2027-03-05]

    gpg --list-secret-keys sjfke.pool.shark@hotmail.com
    sec   ed25519 2024-03-05 [SC] [expires: 2027-03-05]
          2B0A468BE38C555D1EBB89A20045294821C0C792
    uid           [ultimate] Sjfke (Hotmail) <sjfke.pool.shark@hotmail.com>
    ssb   cv25519 2024-03-05 [E] [expires: 2027-03-05]

Where ``[SC]`` means sign and certify and ``[E]`` means encrypt/decrypt

* E = encrypt/decrypt (decrypt a message you received encrypted for you to read)
* S = sign (sign data. For example a file or to send signed e-mail)
* C = certify (sign another key, establishing a trust-relation)
* A = authentication (log in to SSH with a PGP key; this is relatively new usage)

References

* `GPG - why am I encrypting with subkey instead of primary key? <https://serverfault.com/questions/397973/gpg-why-am-i-encrypting-with-subkey-instead-of-primary-key>`_
* `Anatomy of a GPG Key <https://davesteele.github.io/gpg/2014/09/20/anatomy-of-a-gpg-key/>`_ by Dave Steele

********************
Git GPG integrations
********************

* `Telling Git about your signing key <https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key>`_
* `Use GPG Signing Keys with Git (and GitHub) on Windows 10 <https://medium.com/@ryanmillerc/use-gpg-signing-keys-with-git-on-windows-10-github-4acbced49f68>`_
* `Git Tools - Signing Your Work <https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work>`_

.. code-block:: console

    $ gpg --list-secret-keys --keyid-format=long | grep -E "sec|uid"               # Unix
    $ gpg --list-secret-keys --keyid-format=long | select-string @('sec ', 'uid ') # Windows
    sec   ed25519/09D708FAED728E4C 2022-07-27 [SC] [expires: 2024-07-27]
    uid                 [ultimate] Geoffrey Collis <geoffreycollis@hotmail.com>
    sec   ed25519/49220AC61317062D 2023-03-31 [SC] [expires: 2024-01-25]
    uid                 [ultimate] Sjfke <sjfke.pool.shark@hotmail.com>

    # On Windows with 'Git for Windows' installed
    $ where.exe gpg  # C:\Program Files (x86)\GnuPG\bin\gpg.exe
    $ git config --global gpg.program "C:\Program Files (x86)\GnuPG\bin\gpg.exe"

    # Global auto-sign commits and tags
    $ git config --global --list
    $ git config --global user.email geoffreycollis@hotmail.com
    $ git config --global user.signingKey 09D708FAED728E4C
    $ git config --global commit.gpgSign true
    $ git config --global tag.gpgSign true

    # Project (local) auto-sign commits and tags
    $ git config --local --list
    $ git config --local user.email sjfke.pool.shark@hotmail.com
    $ git config --local user.signingKey 49220AC61317062D
    $ git config --local commit.gpgSign true
    $ git config --local tag.gpgSign true

    # Remove GPG signing
    $ git config --global --unset user.signingKey
    $ git config --global --unset commit.gpgSign
    $ git config --global --unset tag.gpgSign
    $ git config --local --unset user.signingKey
    $ git config --local --unset commit.gpgSign
    $ git config --local --unset tag.gpgSign

For `GitHub <https://github.com>`_  add these keys to `SSH and GPG keys <https://github.com/settings/keys>`_

******************
Exporting GPG keys
******************

* Listing your *public* and *private* keys.

.. code-block:: console

    $ gpg --list-keys --keyid-format LONG           # list all your public keys
    $ gpg --list-secret-keys --keyid-format LONG    # list all your private keys

* Exporting your *public* key is a commonly used technique for importing it into other applications.

.. code-block:: console

    $ gpg --armor --export sjfke.pool.shark@hotmail.com
    $ gpg --output export-public.gpg --armor --export sjfke.pool.shark@hotmail.com

* Exporting your *private* key requires your pass-phrase and is **NOT RECOMMENDED** even though it is unusable without the pass-phrase

.. code-block:: console

    $ gpg --armor --export-secret-key sjfke.pool.shark@hotmail.com
    $ gpg --output export-private.gpg --armor --export-secret-key sjfke.pool.shark@hotmail.com # private key

.. _backup-or-transfer-keys:

***************************
Backup or Transfer GPG keys
***************************

* Listing your *public* and *private* keys.

.. code-block:: console

    $ gpg --list-keys --keyid-format LONG                                               # public keys
    $ gpg --list-secret-keys --keyid-format LONG                                        # private keys

Backup single key-pair
======================

.. code-block:: console

    $ gpg --export-secret-keys --export-options backup --output backup-private.gpg sjfke.pool.shark@hotmail.com
    $ gpg --export --export-options backup --output backup-public.gpg sjfke.pool.shark@hotmail.com

    * Each *private* key prompts for it's pass-phrase
    * Exported *private* keys remain protected with their pass-phrase

Backup the key ring
===================


.. code-block:: console

    # All public and private keys and trust
    $ gpg --export --export-options backup --output backup-all-public.gpg               # public keys
    $ gpg --export-secret-keys --export-options backup --output backup-all-private.gpg  # private keys
    $ gpg --export-ownertrust > backup-all-trust.gpg                                    # UNIX trust database
    $ gpg --export-ownertrust | add-content -Encoding ASCII backup-all-trust.gpg        # Windows trust database

Note:
    * Each *private* key prompts for it's pass-phrase
    * Exported *private* keys remain protected by their pass-phrases
    * Trust file ``backup-all-trust.gpg`` **MUST BE** in **ASCII**

Backup references
=================

* `StackExchange: Correct way to create a GPG backup <https://security.stackexchange.com/questions/243959/what-is-the-correct-way-to-create-a-backup-copy-of-a-pgp-key-pair>`_
* `HackerThink: How to export a GPG private key and public key to a file <https://hackerthink.com/solutions/how-to-export-a-gpg-private-key-and-public-key-to-a-file/>`_
* `How-To-Geek: Back Up and Restore Your GPG Keys on Linux <https://www.howtogeek.com/816878/how-to-back-up-and-restore-gpg-keys-on-linux/>`_
* `JWillikers:  Backup and Restore GPG key <https://www.jwillikers.com/backup-and-restore-a-gpg-key>`_

******************
Importing GPG keys
******************

Assumes existence of the files in :ref:`backup-or-transfer-keys`, and as always a *private* key will prompt it's pass-phrase

Import single key-pair
======================

* To import a *key-pair*, only the *private* key backup is required

.. code-block:: console

    $ gpg --list-keys sjfke.pool.shark@hotmail.com         # check public key does not exist
    $ gpg --list-secret-keys sjfke.pool.shark@hotmail.com  # check private key does not exist
    $ gpg --import export-private.gpg                      # import 'sjfke.pool.shark@hotmail.com' key-pair
    $ gpg --list-keys sjfke.pool.shark@hotmail.com         # check public sjfke.pool.shark@hotmail.com key exists
    $ gpg --list-secret-keys sjfke.pool.shark@hotmail.com  # check private sjfke.pool.shark@hotmail.com key exists

Now add the *trust*, see :ref:`trusting-imported-keys`

Import the key ring
===================

* The ASCII ``backup-all-trust.gpg`` file is needed to restore the *trusts*
* Only the *private* keys backup, ``backup-all-private.gpg`` file is required

.. code-block:: console

    $ gpg --list-keys                             # check is empty
    $ gpg --list-secret-keys                      # check is empty
    $ gpg --import backup-all-private.gpg         # import all key-pairs
    $ gpg --import-ownership backup-all-trust.gpg # import all key-pairs
    $ gpg --list-keys                             # check public keys exist and are trusted
    $ gpg --list-secret-keys                      # check private key exists and are trusted

*****************
Deleting GPG keys
*****************

Delete a public key
===================

.. note:: This will fail if the *public* key has a corresponding *private* key

.. code-block:: console

    $ gpg --list-keys                                      # list public keys
    $ gpg --delete-key sjfke.pool.shark@hotmail.com        # delete public key

Delete a key-pair
=================

1. delete the `private` key acknowledging **all warnings** (**All FOUR** on Windows)
2. delete the `public` key

.. code-block:: console

    $ gpg --list-secret-keys                               # private keys
    $ gpg --delete-secret-key sjfke.pool.shark@hotmail.com # delete private key
    $ gpg --list-keys                                      # list public keys
    $ gpg --delete-key sjfke.pool.shark@hotmail.com        # delete public key

.. _trusting-imported-keys:

**************************
Trusting Imported GPG keys
**************************

.. code-block:: console

    $ gpg --list-secret-keys sjfke.pool.shark@hotmail.com  | grep 'uid '          # UNIX check if trusted
    $ gpg --list-secret-keys sjfke.pool.shark@hotmail.com  | select-string 'uid ' # Windows check if trusted
    uid           [ unknown] Sjfke <sjfke.pool.shark@hotmail.com>

    $ gpg --edit-key sjfke.pool.shark@hotmail.com                                 # edit key to add trust
    $ gpg> trust
    Please decide how far you trust this user to correctly verify other users' keys
    (by looking at passports, checking fingerprints from different sources, etc.)

      1 = I don't know or won't say
      2 = I do NOT trust
      3 = I trust marginally
      4 = I trust fully
      5 = I trust ultimately
      m = back to the main menu

    Your decision? 5
    $ gpg quit
    $ gpg --list-secret-keys sjfke.pool.shark@hotmail.com  | grep 'uid '          # UNIX check if trusted
    $ gpg --list-secret-keys sjfke.pool.shark@hotmail.com  | select-string 'uid ' # Windows check if trusted
    uid           [ultimate] Sjfke <sjfke.pool.shark@hotmail.com>
