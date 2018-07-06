*****************
Screen Cheatsheet
*****************

Useful Links
=============

* `GNU Screen <https://www.gnu.org/software/screen/manual/screen.html>`_
* `Screen Quick Reference <http://aperiodic.net/screen/quick_reference>`_

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