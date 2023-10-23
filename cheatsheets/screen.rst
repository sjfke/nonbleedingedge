:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/screen.rst

*****************
Screen Cheatsheet
*****************

Useful Links
=============

* `GNU: Screen User’s Manual <https://www.gnu.org/software/screen/manual/screen.html>`_
* `Screen Quick Reference <http://aperiodic.net/screen/quick_reference>`_
* `Howto Geek: How to Use Linux's screen Command <https://www.howtogeek.com/662422/how-to-use-linuxs-screen-command/>`_
* `GNU 'screen' Status Line(s) <https://www.gilesorr.com/blog/screen-status-bar.html>`_
* `Howto Geek: How to Use tmux on Linux, and Why It's Better Than Screen <https://www.howtogeek.com/671422/how-to-use-tmux-on-linux-and-why-its-better-than-screen/>`_


Basic commands ``screen``
-------------------------

.. code-block:: console

    $ screen         # create and attach to a screen session
    $ screen -S Work # create and attach to a named session, 'Work'
    $ screen -ls     # list your screen sessions
    $ screen -r <id> # reattach, or list your existing sessions if no <id>
    $ exit           # exit and close a screen session

Screen key bindings
-------------------

Command key:  ^A   Literal ^A:  a::

  break       ^B b         clear       C            colon       :
  copy        ^[ [         detach      ^D d         digraph     ^V
  displays    *            dumptermcap .            fit         F
  flow        ^F f         focus       ^I           hardcopy    h
  help        ?            history     { }          info        i
  kill        K k          lastmsg     ^M m         license     ,
  lockscreen  ^X x         log         H            login       L
  meta        a            monitor     M            next        ^@ ^N
  sp n   number      N     only        Q            other       ^A
  pow_break   B            pow_detach  D            prev        ^H ^P p ^?
  quit        \            readbuf     <            redisplay   ^L l
  remove      X            removebuf   =            reset       Z
  screen      ^C c         select      '            silence     _
  split       S            suspend     ^Z z         time        ^T t
  title       A            width       W            windows     ^W w
  wrap        ^R r         writebuf    >            xoff        ^S s
  xon         ^Q q

Working across screen sessions::

	^]  paste .
	"   windowlist -b
	-   select -
	0   select session 0
	1   select session 1
	2   select session 2
	3   select session 3
	4   select session 4
	5   select session 5
	6   select session 6
	7   select session 7
	8   select session 8
	9   select session 9
	I   logging on
	O   logging off
	]   paste .



See also, `Tmux Cheat Sheet & Quick Reference <https://tmuxcheatsheet.com/>`_ and `Tmux Homepage <https://github.com/tmux/tmux/wiki>`_

Basic Commands ``tmux``
-----------------------

.. code-block:: console

    $ tmux           # create and attach to a screen session
    $ Ctrl+B x       # prompt to close a tmux session
    $ exit           # exit and close a tmux session

