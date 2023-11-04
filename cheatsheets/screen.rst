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

``Screen`` commands start with ``Ctrl+A`` followed by a *subcommand key* such as ``C``, invokes a new ``screen``
session. If an uppercase *subcommand key* is required it is shown as ``Shift+S``, horizontal window split.

.. code-block:: console

    # Detaching
    $ Ctrl+A D               # detach
    $ Ctrl+A Shift+D Shift+D # detach and logout

    # Reattaching - from UNIX shell
    $ screen -x              # reattach
    $ screen -r <id>         # reattach to specific session



.. code-block:: console
    :force:

    # Window Management
    $ Ctrl+A C               # create new window
    $ Ctrl+A Ctrl+A          # previous active new window
    $ Ctrl+A <number>        # connect to a given screen (0..9)
    $ Ctrl+A ' <title>       # connect to a given screen title or number
    $ Ctrl+A N               # next window in list
    $ Ctrl+A <space-key>     # next window in list
    $ Ctrl+A P               # next window in list
    $ Ctrl+A <backspace-key> # next window in list
    $ Ctrl+A W               # display window bar
    $ Ctrl+A Shift+A         # rename current window
    $ Ctrl+A "               # window list

.. code-block:: console

    # Split Screen Regions
    $ Ctrl+A Shift+S         # split horizontally
    $ Ctrl+A |               # split vertically
    $ Ctrl+A <tab-key>       # jump to next window region
    $ Ctrl+A Shift+X         # remove current region
    $ Ctrl+A Shift+Q         # remove all regions except current one

.. code-block:: console

    # Miscellaneous
    $ Ctrl+A ?               # help, list key bindings
    $ Ctrl+A Ctrl+L          # redraw window
    $ Ctrl+A M               # monitor window for activity
    $ Ctrl+A _               # monitor window for silence
    $ Ctrl+A x               # lock, password protect session
    $ Ctrl+A H               # enable screen session logging
    $ Ctrl+A ?               # help, list key bindings

****

``Tmux``
========

Useful Links
------------

* `Howto Geek: How to Use tmux on Linux, and Why It's Better Than Screen <https://www.howtogeek.com/671422/how-to-use-tmux-on-linux-and-why-its-better-than-screen/>`_
* `Tmux Cheat Sheet & Quick Reference <https://tmuxcheatsheet.com/>`_
* `Tmux Homepage <https://github.com/tmux/tmux/wiki>`_
* `Github: Tmux Getting Started <https://github.com/tmux/tmux/wiki/Getting-Started>`_

Basic Commands
--------------

.. code-block:: console

    $ tmux                          # create and attach to a tmux session
    $ tmux new -s <name>            # create and attach to a named session
    $ tmux ls                       # list your tmux sessions
    $ tmux list-session             # list your tmux sessions
    $ tmux a                        # reattach
    $ tmux at                       # reattach
    $ tmux attach                   # reattach
    $ tmux attach-session           # reattach
    $ tmux attach-session -t <name> # reattach to specific session
    $ Ctrl+d                        # exit and close a tmux session
    $ exit                          # exit and close a tmux session

Inside a tmux Session
^^^^^^^^^^^^^^^^^^^^^

``tmux`` commands start with ``Ctrl+B`` followed by a *subcommand key* such as ``C``, invokes a new ``screen``
session.

In ``tmux`` there are **NO uppercase** *subcommand keys* and the **menu bar** is always shown.

.. code-block:: console

    # Detaching
    $ Ctrl+B D                      # detach
    $ Ctrl+B &                      # close current window

    # Reattaching - from UNIX shell
    $ tmux attach-session           # reattach
    $ tmux attach-session -t <name> # reattach to specific session


.. code-block:: console
    :force:

    # Window Management
    $ Ctrl+B C                       # create new window
    $ Ctrl+B L                       # previous active new window
    $ Ctrl+B <number>                # connect to a given screen (0..9)
    $ Ctrl+B ' <title>               # connect to a given screen title or number
    $ Ctrl+B N                       # next window in list
    $ Ctrl+B P                       # next window in list
    $ Ctrl+B ,                       # rename current window
    $ Ctrl+B W                       # window list
    $ Ctrl+B : swap-window -s 2 -t 1 # reorder windows, swap window number 2(src) and 1(dst)
    $ Ctrl+B : swap-window -t -1     # move current window to the left one position

.. code-block:: console
    :force:

    # Split Window into Panes
    $ Ctrl+B "                 # split horizontally
    $ Ctrl+B : split-window -h # split horizontally
    $ Ctrl+B %                 # split vertically
    $ Ctrl+B : split-window -v # split vertically
    $ Ctrl+B ;                 # toggle last active pane

    $ Ctrl+B O                 # jump to next pane
    $ Ctrl+B <up-arrow>        # select pane up
    $ Ctrl+B <down-arrow>      # select pane down
    $ Ctrl+B <left-arrow>      # select pane left
    $ Ctrl+B <right-arrow>     # select pane right

    $ Ctrl+B Q                 # show pane numbers
    $ Ctrl+B Q <number>        # switch/select pane by number

    $ Ctrl+B }                  # move pane right
    $ Ctrl+B {                  # move pane left

    $ Ctrl+B Ctrl+<up-arrow>    # adjust pane height
    $ Ctrl+B Ctrl+<down-arrow>  # adjust pane height
    $ Ctrl+B Ctrl+<left-arrow>  # adjust pane width
    $ Ctrl+B Ctrl+<right-arrow> # adjust pane width

    $ Ctrl+B X                  # close current pane
    $ Ctrl+B !                  # convert current pane to a window

.. code-block:: console

    # Miscellaneous
    $ Ctrl+B $                  # rename session
    $ Ctrl+B S                  # list tmux sessions
