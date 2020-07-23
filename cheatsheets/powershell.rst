:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/powershell.rst

*********************
PowerShell Cheatsheet
*********************

``PowerShell`` is a modern replacement for the familiar ``DOS`` prompt, which is similar to a UNIX Shell, but
is built on ``.Net`` objects, where tasks are performed by ``cmdlets`` (pronounced *command-lets*).

Almost all ``cmdlets`` produce streams of objects which can be redirected in a *UNIX-like* ``>`` ``<``, ``|`` fashion, but some
such as, ``select-string`` produce streams of text which may not be redirectable. Use ``write-output`` to produce a stream of 
objects to be passed to another ``cmdlet``, others like ``write-host``, ``write-warning`` write only to the console.

For ease of learning ``PowerShell`` uses a consistent ``cmdlet`` naming convention, which is cumbersome for the command line, 
and so provides an extensible alias mechanism... to make things more **obvious**  (but less *consistent*). 
For example ``ls`` is probably more intuitive than ``get-childitem``, likewise ``cat`` or ``type`` is more intuitive than ``get-content``.
However aliases like ``gc``, ``gci`` or ``sls`` can be confusing for others. 

The command-line has color-highlighting and has ``TAB`` completion for commands and arguments. Try ``import <tab>``, and cycle 
through the alternatives. Cmdlets are **case-insensitive** but hyphens are often required but some such as ``where-object`` 
can be written as ``where`` which in my opinion is clearer, other ``*-object`` examples include ``select``, ``sort``, ``tee``,  and ``measure``.
Variable names are also **case-insensitive**

My personal preference is to use the lower-case format for ``cmdlets``, so ``get-help`` rather than ``Get-Help``,  and CamelCase for
variables, so ``dateString`` , rather than ``date_string``.

A `Windows Powershell ISE <https://docs.microsoft.com/en-us/powershell/scripting/components/ise/introducing-the-windows-powershell-ise?view=powershell-7>`_  
is provided if you need more interactive assistance.

There are a lot of online documents and tutorials about ``PowerShell`` but unfortunately, as always, this means what you are searching far is 
either a complex subject matter or not well understood by the author or both... be careful about blindly doing a *copy-paste* of examples.

While learning I found the following helpful:

* `PowerShell GitHub - Learning Powershell <https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell>`_
* `PowerShell equivalents for common Linux/bash commands <https://mathieubuisson.github.io/powershell-linux-bash/>`_
* `10 PowerShell cmdlets you can use instead of CMD commands <https://www.techrepublic.com/article/pro-tip-migrate-to-powershell-from-cmd-with-these-common-cmdlets/>`_

Getting Started
===============

You should become familiar with ``get-help`` and ``get-member`` cmdlets::

   PS> get-help get-childitem         # Help on Get-ChildItem
   PS> get-help get-childiten -online # Online Web based documentation from Microsoft
   PS> get-childitem | get-member     # What is the object type, its methods and properties
   PS> get-help get-content           # notice its aliases 'gc', 'cat', 'type'
   PS> get-help select-string         # regular-expression based string search (UNIX grep)
   
   PS> get-help get-location          # alias 'gl' and 'pwd'.
   PS> get-help get-command           # what commands are available
   PS> get-help select-object         # 'select' or set object properties
   PS> get-help where-object          # 'where' filter on object property
   PS> get-help tee-object            # 'tee' like the UNIX command
   PS> get-help sort-object           # object property based sorting, (UNIX 'sort')
   PS> get-help measure-object        # count lines, characters (UNIX 'wc')
   PS> get-help out-host              # Similar to UNIX 'more' and 'less'

Quick Introduction
==================

::

   $ set-location dir                            # change directory, ('sl','cd')
   $ get-childitem                               # directory listing, ('gci','ls','dir')
   $ mkdir dir1, dir2                            # make two directories (in dir)
   $ set-location dir2                           # change directory to dir2
   
   $ new-item example1.txt, example2.txt         # create two empty files.
   
   $ write-output "" > fred.txt                  # create non-empty file
   $ write-output "some text to the stdout"      # can be piped ('write','echo')
   $ write-host "some text to the console"            
   $ write-host -BackgroundColor Blue "BLOD"     # Blue Line of Death (SIC)
   $ write-warning "warning console message"
   $ write-output "write some text" > fred.txt   # redirect stdout to a Unicode file
   $ write-output "append some text" >> fred.txt # append stdout to a Unicode file
   
   $ get-content fred.txt                        # display contents, ('gc','cat','type')
   $ remove-item example.txt                     # delete file, ('ri','rm','rmdir', 'del','erase','rd')
   
   # Starting applications, quotes, pathname and file extension are optional ('saps','start')
   $ start-process 'notepad'                     # open notepad.exe (can use notepad.exe)
   $ start-process 'https://nonbleedingedge.com' # open URL with browser (MicroSoftEdge)
   $ start-process 'explorer'                    # start explorer.exe (can use explorer.exe)
   $ start-process explorer C:\Windows\          # start explorer.exe in C:\Windows\
   $ start-process explorer $PWD                 # start explorer.exe in current directory
   $ start-process chrome                        # start google chrome (if installed)
   $ start-process notepad++                     # start Notepad++ (if installed)


Variables
=========

Powershell variables are loosely-type, and can be *integers*, *strings*, *arrays*, and *hash-tables*, but also ``.Net`` objects that represent 
*processes*, *services*, *event-logs*, and even *computers*.

Common forms::

   $age = 5                       # System.Int32
   [int]$age = "5"                # System.Int32
   $name = "Dino"                 # System.String
   $name + $age                   # Fails; System.String + System.Int32
   $name + [string]$age           # Dino5; System.String + System.String

   $a = (5, 30, 25, 1)            # array of System.Int32
   $a = (5, "Dino")               # array of (System.Int32, System.String)

   $h = @{ Fred = 30; Wilma  = 25; Pebbles = 1; Dino = 5 } # hash table
   
   $d = Get-ChildItem C:\Windows  # directory listing, FileInfo and DirectoryInfo types, 
   $d | get-member                # FileInfo, DirectoryInfo Properties and Methods
   
   $p = Get-Process               # System.Diagnostics.Process type

Less common forms::
 
   set-variable -name age 5       # same as $age = 5
   set-variable -name name Dino   # same as $name = "Dino"
 
   clear-variable -name age       # clear $age; $name = $null
   clear-variable -name p         # clear $p; $p = $null
   
   remove-variable -name age      # delete variable $age
   remove-item -path variable:\p  # delete variable $p
   
   set-variable -name pi -option Constant 3.14159 # constant variable
   $pi = 42                                       # Fails $pi is a constant


Array Variables
===============

Array variables are a fixed size, can have mixed values and can be multi-dimensional.

::
  
   $a = 1, 2, 3                    # array of integers
   $a = (1, 2, 3)                  # array of integers (my personal preference)
   $a = ('a','b','c')
   $a = (1, 2, 3, 'x')             # array of System.Int32's, System.String
   [int[]]$a = (1, 2, 3, 'x')      # will fail 'x', array of System.Int32 only
   
   $a = ('fred','wilma','pebbles')
   $a[0]             # fred
   $a[2]             # pebbles
   $a.length         # 3
   $a[0] = 'freddie' # fred becomes freddie
   $a[4] = 'dino'    # Error: Index was outside the bounds of the array.
   $a = ($a, 'dino') # correct way to add 'dino'
   
   $b = ('barbey', 'betty', 'bamm-bamm')
   $a = ($a, $b)    # [0]:fred [1]:wilma [2]:pebbles [3]:barney [4]:betty [5]:bamm-bamm 
   $a.length        # 6
   $a = ($a, ($b))  # [0]:fred [1]:wilma [2]:pebbles [3][0]:barney [3][1]:betty [3][2]:bamm-bamm 
   $a.length        # 4
   
   $ages = (30, 25, 1, 5)                      # flintstones ages
   $names = ('fred','wilma','pebbles', 'dino') # flintstones names
   $a = (($names),($ages))                     # multi-dimensional array example
   $a.length                                   # 4
   $a[0]                                       # fred wilma pebbles dino
   $a[1]                                       # 30 25 1 5
   $a[0][0]                                    # fred
   $a[0][1]                                    # 30
   
   
HashTables
==========

Unordered collection of key:value pairs, later versions of ``PowersShell`` support ``$hash = [ordered]@{}``

::

   $h = @{}              # empty hash
   $key = 'Fred'         # set key name
   $value = 30           # set key value
   $h.add($key, $value)  # add key:value to the hash-table
   
   $h.add('Wilma', 25 )  # add Wilma
   $h['Pebbles'] = 1     # add Pebbles
   $h.Dino = 5           # add Dino
   
   $h                    # actual hash-table, printed if on command-line
   $h['Fred']            # how old is Fred? 30
   $h[$key]              # how old is Fred? 30
   $h.fred               # how old is Fred? 30
   
   # creating a populated hash
   $h = @{
       Fred = 30
       Wilma  = 25
       Pebbles = 1
       Dino = 5
   }
   
   # creating a populated hash, one-liner
   $h = @{ Fred = 30; Wilma = 25; Pebbles = 1; Dino = 5 }
   
   $h.keys            # unordered: Dino, Pebbles, Fred, Wilma
   $h.values          # unordered: 5, 1, 30, 25 (but same as $h.keys order)
   
   # key order is random
   foreach($key in $h.keys) {
       write-output ('{0} Flintstone is {1:D} years old' -f $key, $h[$key])
   }
   
   # ascending alphabetic order (Dino, Fred, Pebbles, Wilma)
   foreach($key in $h.keys | sort) {
       write-output ('{0} Flintstone is {1:D} years old' -f $key, $h[$key])
   }
   
   # descending alphabetic order (Wilma, Pebbles, Fred, Dino)
   foreach($key in $h.keys | sort -descending) {
       write-output ('{0} Flintstone is {1:D} years old' -f $key, $h[$key])
   }
   
   # specfific order (Fred, Wilma, Pebbles, Dino)
   $keys = ('fred', 'wilma', 'pebbles', 'dino')
   for ($i = 0; $i -lt $keys.length; $i++) {
      write-output ('{0} Flintstone is {1:D} years old' -f $keys[$i], $h[$keys[$i]])
   }
   
   if ($h.ContainsKey('fred')) { ... }   # true 
   if ($h.ContainsKey('barney')) { ... } # false
   
   $h.remove('Dino')                # remove Dino, because he ran away
   $h.clear()                       # family deceased

Excellent review of PowerShell HashTables:

* `Powershell: Everything you wanted to know about hashtables <https://powershellexplained.com/2016-11-06-powershell-hashtable-everything-you-wanted-to-know-about/>`_

PowerShell Environment
======================

::

   $ get-childitem variable:        # list PowerShell environment variables, 'PSHome', 'PWD' etc.
   $ $pshome                        # variable containing which PowerShell and version
   $ $pwd                           # variable containing the working directory
   
   $ get-childitem env:             # get 'cmd.exe' enviroment variables, UCASE by convention
   $ $env:SystemRoot                # variable containing C:\Windows
   $ $env:COMPUTERNAME              # variable containing MYLAPTOP001
   $ $env:USERNAME                  # variable containing username
   $ $env:TMP, $env:TEMP            # variable containingtemp directory
   $ $env:LIB_PATH='/usr/local/lib' # setting LIB_PATH variable 
   
   $ $psversiontable                # variable containing PowerShell version information.
   $ get-host                       # PowerShell version information.

Processes
=========

::

   $ get-process | get-member                                       # show returned object
   $ get-process | select -first 10                                 # first 10 processes
   $ get-process | select -last 10                                  # last 10 processes
   $ get-process | sort -property ws | select -last 10              # last 10 sorted
   $ get-process | sort -property ws | select -first 10             # first 10 sorted
   $ get-process | sort -property ws -descending | select -first 10 # reverse sort first 10
   $ get-process | where {$_.processname -match "^p.*"}             # all processes starting with "p"
   $ get-process | select -property Name,Id,WS | out-host -paging   # paged (more/less) output

Viewing Files
=============
::

   $ get-content <file> | select -last 20             # get last 20 lines
   $ get-content <file> -wait                         # tailing a log-file
   $ get-content <file> | select -first 10            # first 10 lines
   $ get-content <file> | select -last 10             # last 10 lines
   
   $ get-content <file> | measure -line -word         # count lines, words   
   $ get-content <file> | measure -character          # count characters   
 
   $ select-string 'str1' <file>                      # all lines containing 'str1'
   $ select-string -NotMatch 'str1' <file>            # all lines *not* containing 'str1'
   $ select-string ('str1','str2') <file>             # all lines containing 'str1' or 'str2'
   $ select-string -NotMatch ('str1','str2') <file>   # all lines *not* containing 'str1' or 'str2'
   $ select-string <regex> <file> | select -last 10   # last 10 lines containing <regex>
   
   $ select-string <regex> <file> | select -first 10  # first 10 lines containing <regex>
   $ select-string <regex> <file> | select -last 10   # last 10 lines containing of <regex>


Computer Information
====================
::

   # Classnames: Win32_BIOS, Win32_Processor, Win32_ComputerSystem, Win32_LocalTime, 
   #             Win32_LogicalDisk, Win32_LogonSession, Win32_QuickFixEngineering, Win32_Service

   $ get-ciminstance -classname Win32_BIOS                # bios version
   $ get-ciminstance -classname Win32_Processor           # processor information
   $ get-ciminstance -classname Win32_ComputerSystem      # computer name, model etc.
   $ get-ciminstance -classname Win32_QuickFixEngineering # hotfixes installed
   $ get-ciminstance -classname Win32_QuickFixEngineering -property HotFixID | select -property hotfixid

Windows EventLog
================

::

   $ get-eventlog -list                                                    # list a summary of the events
   $ get-eventlog -logname system -newest 5                                # last 5 system events
   $ get-eventlog -logname system -entrytype error | out-host -paging      # system error events
   
   $ get-eventlog -logname application | out-host -paging                  # application events 
   $ get-eventlog -logname application -Index 14338 | select -Property *   # details of application event 14338

   $ $events = get-eventlog -logname system -newest 1000                            # capture last 1000 system events
   $ $events | group -property source -noelement | sort -property count -descending # categorize them
   
   $ get-eventlog -logname application -source MSSQLSERVER | out-host -paging
   $ get-eventlog -logname application -source MSSQLSERVER -after 18/6/2019 | out-host -paging
   
   # Gets events from event logs and event tracing log files (less useful)
   $ (Get-WinEvent -ListLog Application).ProviderNames | out-host -paging # who is writing Application logs
   
   $ get-winevent -filterhashtable @{logname='application'} | get-member
   
   $ get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | out-host -paging
   $ get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | where {$_.Message -like '*error*'} | out-host -paging

* `Event Log Parsing <http://colleenmorrow.com/2012/09/20/parsing-windows-event-logs-with-powershell/>`_
* `Get-WinEvent <https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Diagnostics/Get-WinEvent>`_

HotFixes
========

::

   $ get-hotfix                    # list all installed hot fixes 
   $ get-hotfix -Id KB4516115      # when was hotfix installed
   
   # To get hotfix details
   $ start-process "https://www.catalog.update.microsoft.com/Search.aspx?q=KB4516115" 


Command Line History
====================

You can recall and repeat commands::

   $ get-history
   $ invoke-history 1
   $ get-history | select-string -pattern 'ping'
   $ get-history | where {$_.CommandLine -like "*ping*"} 
   $ get-history | format-list -property *               # execution time and status             
   $ get-history -count 100                              # get 100 lines
   $ clear-history
   
Formatting Output
=================

Very similar to Python ``-f`` operator, examples use ``write-host`` but can be other output commands.
Specified as ``{<index>, <alignment><width>:<format_spec>}``

::

   $shortText = "Align me"
   $longerText = "Please Align me, but I am very wide"
   
   $ write-host("{0,-20}" -f $shortText)         # Left-align; no overflow.
   $ write-host("{0,20}"  -f $shortText)         # Right-align; no overflow.
   $ write-host("{0,-20}" -f $longerText)        # Left-align; data overflows width.
   
   $ write-host("Room: {0:D}" -f 232)            # Room: 232
   $ write-host("Invoice No.: {0:D8}" -f 17)     # Invoice No.: 00000017
   $ $invoice = "{0}-{1}" -f 00017, 007          # (integers) so invoice = 17-7  
   $ $invoice = "{0}-{1}" -f '00017', '007'      # (strings) so invoice = 00017-007  
   
   $ write-host("Temp: {0:F}°C" -f 18.456)       # Temp: 18.46°C
   $ write-host("Grade: {0:p}" -f 0.875)         # Grade: 87.50%
   $ write-host('Grade: {0:p0}' -f 0.875)        # Grade: 88%  
   $ write-host('{1}: {0:p0}' -f 0.875, 'Maths') # Maths: 88%
   
   # Custom formats
   $ write-output('{1:00000}' -f 'x', 1234)      # 01234
   $ write-output('{0:0.000}' -f [Math]::Pi)     # 3.142
   $ write-output('{0:00.0000}' -f 1.23)         # 01.2300
   $ write-host('{0:####}' -f 1234.567)          # 1235
   $ write-host('{0:####.##}' -f 1234.567)       # 1234.57
   $ write-host('{0:#,#}' -f 1234567)            # 1,234,567
   $ write-host('{0:#,#.##}' -f 1234567.891)     # 1,234,567.89
   
   $ write-host('{0:000}:{1}' -f 7, 'Bond')      # 007:Bond
   
   $ get-date -Format 'yyyy-MM-dd:hh:mm:ss'      # 2020-04-27T07:19:05
   $ get-date -Format 'yyyy-MM-dd:HH:mm:ss'      # 2020-04-27T19:19:05
   $ get-date -UFormat "%A %m/%d/%Y %R %Z"       # Monday 04/27/2020 19:19 +02

More examples:
* `Formatting Output <http://powershellprimer.com/html/0013.html>`_
* `Get-Date <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-date?view=powershell-6>`_
