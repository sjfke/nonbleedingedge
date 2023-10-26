:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/screen.rst

**************************
Screen and Tmux Cheatsheet
**************************

``Screen``
==========

Useful Links
------------

* `GNU: Screen User’s Manual <https://www.gnu.org/software/screen/manual/screen.html>`_
* `Screen Quick Reference <http://aperiodic.net/screen/quick_reference>`_
* `Howto Geek: How to Use Linux's screen Command <https://www.howtogeek.com/662422/how-to-use-linuxs-screen-command/>`_
* `GNU 'screen' Status Line(s) <https://www.gilesorr.com/blog/screen-status-bar.html>`_

Basic commands
--------------

.. code-block:: console

    $ screen           # create and attach to a screen session
    $ screen -S <name> # create and attach to a named session, 'Work'
    $ screen -ls       # list your screen sessions
    $ screen -x        # reattach
    $ screen -r <id>   # reattach to specific session, or list your existing sessions if no <id>
    $ exit             # exit and close a screen session
    $ Ctrl+d           # exit and close a screen session

Inside a Screen Session
^^^^^^^^^^^^^^^^^^^^^^^

``Screen`` commands start with ``Ctrl+A`` followed by a sub-command key such as ``C`` which invokes a new ``screen``
session. If an uppercase subcommand key is required it is shown as ``Shift+S``, horizontal window split.

.. code-block:: console

    # Detaching
    $ Ctrl+A d               # detach
    $ Ctrl+A Shift+D Shift+D # detach and logout


::

    # Window Management
    $ Ctrl+A C               # create new window
    $ Ctrl+A Ctrl+A          # previous active new window
    $ Ctrl+A <number>        # connect to a given screen (0..9)
    $ Ctrl+A '<title>        # connect to a given screen title or number
    $ Ctrl+A n               # next window in list
    $ Ctrl+A <space-key>     # next window in list
    $ Ctrl+A p               # next window in list
    $ Ctrl+A <backspace-key> # next window in list
    $ Ctrl+A "               # window list
    $ Ctrl+A w               # window
    $ Ctrl+A A               # rename current window


.. code-block:: console

    # Split Screen Regions
    $ Ctrl+A Shift+S         # split horizontally
    $ Ctrl+A |               # split vertically
    $ Ctrl+A V               # split vertically
    $ Ctrl+A <tab-key>       # jump to next window region
    $ Ctrl+A X               # remove current region
    $ Ctrl+A Q               # remove all regions except current one

.. code-block:: console

    # Miscellaneous
    $ Ctrl+A ?               # help, list key bindings
    $ Ctrl+A Ctrl+L          # redraw window
    $ Ctrl+A M               # monitor window for activity
    $ Ctrl+A _               # monitor window for silence
    $ Ctrl+A x               # lock, password protect session
    $ Ctrl+A H               # enable screen session logging
    $ Ctrl+A ?               # help, list key bindings

.. code-block:: console

    # Clipboard
    $ Ctrl+A [               # freely navigate buffer
    $ Ctrl+A <escape-key>    # freely navigate buffer
    $ <space-key>            # toggle selection to copy
    $ Ctrl+A ]               # paste

.. code-block:: console

    # Copy Mode Scrollback Buffer
    $ Ctrl+A u               # half page up (back)
    $ Ctrl+A b               # full page up (back)
    $ Ctrl+A d               # half page down (forward)
    $ Ctrl+A f               # full page down (forward)
    $ Ctrl+A h/j/k/l         # full page down (forward)

****

``Tmux``
========

Useful Links
------------

* `Howto Geek: How to Use tmux on Linux, and Why It's Better Than Screen <https://www.howtogeek.com/671422/how-to-use-tmux-on-linux-and-why-its-better-than-screen/>`_
* `Tmux Cheat Sheet & Quick Reference <https://tmuxcheatsheet.com/>`_
* `Tmux Homepage <https://github.com/tmux/tmux/wiki>`_

Basic Commands
--------------

.. code-block:: console

    $ tmux           # create and attach to a screen session
    $ Ctrl+B x       # prompt to close a tmux session
    $ exit           # exit and close a tmux session

