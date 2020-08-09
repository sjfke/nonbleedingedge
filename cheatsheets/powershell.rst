:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/powershell.rst

*********************
PowerShell Cheatsheet
*********************

``PowerShell`` is a modern replacement for the familiar ``DOS`` prompt, which is similar to a UNIX Shell, but
is built on ``.Net`` objects, where tasks are performed by ``cmdlets`` (pronounced *command-lets*).

Almost all ``cmdlets`` produce streams of objects which can be redirected in a *UNIX-like* ``>`` ``<``, ``|`` fashion, but some
such as, ``select-string`` produce streams of text which may not be redirectable.

For ease of learning ``PowerShell`` uses a consistent ``cmdlet`` naming convention, which is cumbersome for the command line, 
and so provides an extensible alias mechanism... to make things more **obvious**  (but less *consistent*). 
For example ``ls`` is probably more intuitive than ``get-childitem``, likewise ``cat`` or ``type`` is more intuitive than ``get-content``.
However aliases like ``gc``, ``gci`` or ``sls`` can be confusing. 

The command-line has color-highlighting and has ``TAB`` completion for commands and arguments. Try ``import <tab>``, and cycle 
through the alternatives. Cmdlets are **case-insensitive** but hyphens are significant, but in some cases optional like ``where-object`` 
can be written as ``where``, which in my opinion is clearer. Other ``*-object`` examples include ``select``, ``sort``, ``tee``,  and ``measure``.

Variable names are also **case-insensitive**, can include ``_``, and camelCase can be used to make variable names more human readable, but is 
irrelevent to ``PowerShell``.

My personal preference:

* lower-case format for ``cmdlets``, so ``get-help`` rather than ``Get-Help``;
* camelCase for variable names, so ``dateString`` , rather than ``date_string``;

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

   PS> set-location dir                            # change directory, ('sl', 'cd', 'chdir')
   PS> cd dir                                      # using an alias to change directory
   PS> get-childitem                               # directory listing, ('gci','ls','dir')
   PS> ls                                          # using an alias to get directory listing
   PS> new-item -ItemType Directory dir1           # create directory dir1 ('ni')
   PS> mkdir dir1, dir2                            # *convenience function* make two directories ('md')
   PS> remove-item dir2                            # delete a directory
   PS> rmdir dir2                                  # using an alias to delete a directory
   
   PS> new-item fred.txt, wilma.txt                # create two empty files ('ni')
   PS> remove-item fred.txt                        # delete file ('ri','rm','rmdir','del','erase','rd')
   PS> rm fred.txt                                 # using an alias to delete a file
   
   PS> write-output "" > fred.txt                  # create an empty file ('write','echo')
   PS> echo "" > fred.txt                          # using alias to create an empty file
   PS> write-output "some text to the stdout"      # can be piped ('write','echo')
   PS> write-host "some text to the console"       # cannot be piped
   PS> write-host -BackgroundColor Blue "BLOD"     # Blue Line of Death (SIC)
   PS> write-warning "console message"             # WARNING: console message - color highlighting
   PS> write-output "write some text" > fred.txt   # redirect stdout to a Unicode file
   PS> write-output "append some text" >> fred.txt # append stdout to a Unicode file
   
   PS> get-content fred.txt                        # display contents, ('gc','cat','type')
   PS> cat fred.txt                                # using an alias to display contents
   PS> remove-item fred.txt                        # delete a file, ('ri','rm','rmdir', 'del','erase','rd')
   PS> rm fred.txt                                 # using an alias to delete file
   
   # Starting applications, start-process ('saps','start')
   #   Note: quotes, pathnames and file extensions are optional
   PS> start-process 'notepad'                     # open notepad.exe (can use notepad.exe)
   PS> start-process 'https://nonbleedingedge.com' # open URL with browser (Microsoft-Edge)
   PS> start-process 'explorer'                    # start explorer.exe (can use explorer.exe)
   PS> start-process explorer C:\Windows\          # start explorer.exe in C:\Windows\
   PS> start-process explorer PS>PWD                 # start explorer.exe in current directory
   PS> start-process chrome                        # start google chrome (if installed)
   PS> start-process notepad++                     # start Notepad++ (if installed)


Variables
=========

Powershell variables are loosely-type, and can be *integers*, *strings*, *arrays*, and *hash-tables*, but also ``.Net`` objects that represent 
*processes*, *services*, *event-logs*, and even *computers*.

Common forms::

   PS> $age = 5                       # System.Int32
   PS> [int]$age = "5"                # System.Int32, cast System.String + System.Int32
   PS> $name = "Dino"                 # System.String
   PS> $name + $age                   # Fails; System.String + System.Int32
   PS> $name + [string]$age           # Dino5; System.String + System.String

   PS> $a = (5, 30, 25, 1)            # array of System.Int32
   PS> $a = (5, "Dino")               # array of (System.Int32, System.String)

   PS> $h = @{ Fred = 30; Wilma  = 25; Pebbles = 1; Dino = 5 } # hash table
   
   PS> $d = Get-ChildItem C:\Windows  # directory listing, FileInfo and DirectoryInfo types, 
   PS> $d | get-member                # FileInfo, DirectoryInfo Properties and Methods
   
   PS> $p = Get-Process               # System.Diagnostics.Process type

Less common forms::
 
   PS> set-variable -name age 5       # same as PS>age = 5
   PS> set-variable -name name Dino   # same as PS>name = "Dino"
 
   PS> clear-variable -name age       # clear PS>age; PS>name = PS>null
   PS> clear-variable -name p         # clear PS>p; PS>p = PS>null
   
   PS> remove-variable -name age      # delete variable PS>age
   PS> remove-item -path variable:\p  # delete variable PS>p
   
   PS> set-variable -name pi -option Constant 3.14159 # constant variable
   PS> $pi = 42                                       # Fails PS>pi is a constant


Array Variables
===============

Array variables are a fixed size, can have mixed values and can be multi-dimensional.

::
  
   PS> $a = 1, 2, 3                    # array of integers
   PS> $a = (1, 2, 3)                  # array of integers (my personal preference)
   PS> $a = ('a','b','c')
   PS> $a = (1, 2, 3, 'x')             # array of System.Int32's, System.String
   PS> [int[]]$a = (1, 2, 3, 'x')      # will fail 'x', array of System.Int32 only
   
   PS> $a = ('fred','wilma','pebbles')
   PS> $a[0]             # fred
   PS> $[2]              # pebbles
   PS> $a.length         # 3
   PS> $a[0] = 'freddie' # fred becomes freddie
   PS> $a[4] = 'dino'    # Error: Index was outside the bounds of the array.
   PS> $a = ($a, 'dino') # correct way to add 'dino'
   
   PS> $b = ('barbey', 'betty', 'bamm-bamm')
   PS> $a = ($a, $b)    # [0]:fred [1]:wilma [2]:pebbles [3]:barney [4]:betty [5]:bamm-bamm 
   PS> $a.length        # 6
   PS> $a = ($a, ($b))  # [0]:fred [1]:wilma [2]:pebbles [3][0]:barney [3][1]:betty [3][2]:bamm-bamm 
   PS> $a.length        # 4
   
   PS> $ages = (30, 25, 1, 5)                      # flintstones ages
   PS> $names = ('fred','wilma','pebbles', 'dino') # flintstones names
   PS> $a = ($names),($ages))                      # multi-dimensional array example
   PS> $a.length                                   # 4
   PS> $a[0]                                       # fred wilma pebbles dino
   PS> $a[1]                                       # 30 25 1 5
   PS> $a[0][0]                                    # fred
   PS> $a[0][1]                                    # 30
   
   
HashTables
==========

Unordered collection of key:value pairs, later versions of ``PowersShell`` support ``PS>hash = [ordered]@{}``

::

   PS> $h = @{}              # empty hash
   PS> $key = 'Fred'         # set key name
   PS> $value = 30           # set key value
   PS> $h.add(PS>key, PS>value)  # add key:value to the hash-table
   
   PS> $h.add('Wilma', 25 )  # add Wilma
   PS> $h['Pebbles'] = 1     # add Pebbles
   PS> $h.Dino = 5           # add Dino
   
   PS> $h                    # actual hash-table, printed if on command-line
   PS> $h['Fred']            # how old is Fred? 30
   PS> $h[$key]              # how old is Fred? 30
   PS> $h.fred               # how old is Fred? 30
   
   # creating a populated hash
   PS> $h = @{
       Fred = 30
       Wilma  = 25
       Pebbles = 1
       Dino = 5
   }
   
   # creating a populated hash, one-liner
   PS> $h = @{ Fred = 30; Wilma = 25; Pebbles = 1; Dino = 5 }
   
   PS> $h.keys            # unordered: Dino, Pebbles, Fred, Wilma
   PS> $h.values          # unordered: 5, 1, 30, 25 (but same as $h.keys order)
   
   # key order is random
   PS> foreach($key in $h.keys) {
       write-output ('{0} Flintstone is {1:D} years old' -f $key, $h[$key])
   }
   
   # ascending alphabetic order (Dino, Fred, Pebbles, Wilma)
   PS> foreach($key in $h.keys | sort) {
       write-output ('{0} Flintstone is {1:D} years old' -f $key, $h[$key])
   }
   
   # descending alphabetic order (Wilma, Pebbles, Fred, Dino)
   PS> foreach($key in $h.keys | sort -descending) {
       write-output ('{0} Flintstone is {1:D} years old' -f $key, $h[$key])
   }
   
   # specfific order (Fred, Wilma, Pebbles, Dino)
   PS> $keys = ('fred', 'wilma', 'pebbles', 'dino')
   for ($i = 0; $i -lt $keys.length; $i++) {
      write-output ('{0} Flintstone is {1:D} years old' -f $keys[$i], $h[$keys[$i]])
   }
   
   PS> if ($h.ContainsKey('fred')) { ... }   # true 
   PS> if ($h.ContainsKey('barney')) { ... } # false
   
   PS> $h.remove('Dino')                # remove Dino, because he ran away
   PS> $h.clear()                       # family deceased

Excellent review of PowerShell HashTables:

* `Powershell: Everything you wanted to know about hashtables <https://powershellexplained.com/2016-11-06-powershell-hashtable-everything-you-wanted-to-know-about/>`_

PowerShell Environment
======================

::

   PS> get-childitem variable:        # list PowerShell environment variables, 'PSHome', 'PWD' etc.
   PS> $pshome                        # variable containing which PowerShell and version
   PS> $pwd                           # variable containing the working directory
   
   PS> get-childitem env:             # get 'cmd.exe' enviroment variables, UCASE by convention
   PS> $env:SystemRoot                # variable containing C:\Windows
   PS> $env:COMPUTERNAME              # variable containing MYLAPTOP001
   PS> $env:USERNAME                  # variable containing username
   PS> $env:TMP, $env:TEMP            # variable containingtemp directory
   PS> $env:LIB_PATH='/usr/local/lib' # setting LIB_PATH variable 
   
   PS> $psversiontable                # variable containing PowerShell version information.
   PS> get-host                       # PowerShell version information.

Processes
=========

::

   PS> get-process | get-member                                       # show returned object
   PS> get-process | select -first 10                                 # first 10 processes
   PS> get-process | select -last 10                                  # last 10 processes
   PS> get-process | sort -property ws | select -last 10              # last 10 sorted
   PS> get-process | sort -property ws | select -first 10             # first 10 sorted
   PS> get-process | sort -property ws -descending | select -first 10 # reverse sort first 10
   PS> get-process | where {PS>_.processname -match "^p.*"}             # all processes starting with "p"
   PS> get-process | select -property Name,Id,WS | out-host -paging   # paged (more/less) output
   PS> get-process | out-gridview                                     # interactive static table view

Viewing Files
=============
::

   PS> get-content <file> | select -last 20             # get last 20 lines
   PS> get-content <file> -wait                         # tailing a log-file
   PS> get-content <file> | select -first 10            # first 10 lines
   PS> get-content <file> | select -last 10             # last 10 lines
   
   PS> get-content <file> | measure -line -word         # count lines, words   
   PS> get-content <file> | measure -character          # count characters   
 
   PS> select-string 'str1' <file>                      # all lines containing 'str1'
   PS> select-string -NotMatch 'str1' <file>            # all lines *not* containing 'str1'
   PS> select-string ('str1','str2') <file>             # all lines containing 'str1' or 'str2'
   PS> select-string -NotMatch ('str1','str2') <file>   # all lines *not* containing 'str1' or 'str2'
   PS> select-string <regex> <file> | select -last 10   # last 10 lines containing <regex>
   
   PS> select-string <regex> <file> | select -first 10  # first 10 lines containing <regex>
   PS> select-string <regex> <file> | select -last 10   # last 10 lines containing of <regex>


Computer Information
====================
::

   # Classnames: Win32_BIOS, Win32_Processor, Win32_ComputerSystem, Win32_LocalTime, 
   #             Win32_LogicalDisk, Win32_LogonSession, Win32_QuickFixEngineering, Win32_Service

   PS> get-ciminstance -classname Win32_BIOS                # bios version
   PS> get-ciminstance -classname Win32_Processor           # processor information
   PS> get-ciminstance -classname Win32_ComputerSystem      # computer name, model etc.
   PS> get-ciminstance -classname Win32_QuickFixEngineering # hotfixes installed on which date
   PS> get-ciminstance -classname Win32_QuickFixEngineering -property HotFixID | select -property hotfixid

Windows EventLog
================

::

   PS> get-eventlog -list                                                    # list a summary of the events
   PS> get-eventlog -logname system -newest 5                                # last 5 system events
   PS> get-eventlog -logname system -entrytype error | out-host -paging      # system error events
   
   PS> get-eventlog -logname application | out-host -paging                  # application events 
   PS> get-eventlog -logname application -Index 14338 | select -Property *   # details of application event 14338

   PS> PS>events = get-eventlog -logname system -newest 1000                   # capture last 1000 system events
   PS> PS>events | group -property source -noelement | sort -property count -descending # categorize them
   
   PS> get-eventlog -logname application -source MSSQLSERVER | out-host -paging
   PS> get-eventlog -logname application -source MSSQLSERVER -after 18/6/2019 | out-host -paging
   
   # Gets events from event logs and event tracing log files (less useful)
   PS> (Get-WinEvent -ListLog Application).ProviderNames | out-host -paging # who is writing Application logs
   
   PS> get-winevent -filterhashtable @{logname='application'} | get-member
   
   PS> get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | out-host -paging
   PS> get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | where {PS>_.Message -like '*error*'} | out-host -paging

* `Event Log Parsing <http://colleenmorrow.com/2012/09/20/parsing-windows-event-logs-with-powershell/>`_
* `Get-WinEvent <https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Diagnostics/Get-WinEvent>`_

HotFixes
========

::

   PS> get-hotfix                    # list all installed hot fixes 
   PS> get-hotfix -Id KB4516115      # when was hotfix installed
   
   # To get hotfix details (random choice, happens to be an Adobe Flash update)
   PS> start-process "https://www.catalog.update.microsoft.com/Search.aspx?q=KB4516115" 


Command Line History
====================

You can recall and repeat commands::

   PS> get-history
   PS> invoke-history 1
   PS> get-history | select-string -pattern 'ping'
   PS> get-history | where {PS>_.CommandLine -like "*ping*"} 
   PS> get-history | format-list -property *               # execution time and status             
   PS> get-history -count 100                              # get 100 lines
   PS> clear-history
   
CSV Files
=========

Powershell provides ``cmdlets`` for handling these which avoid importing into ``Excel`` and ``MS Access``.
The ``out-gridview`` renders the output the data in an interactive table. 

::

   PS> import-csv -Path file.csv -Delimeter "`t" | out-gridview # load and display a <TAB> separated file.
   PS> import-csv -Path file.csv -Delimeter ";" | out-gridview  # load and display a ';' separated file.
   
   PS> get-content file.csv
       Name;Age
       Fred;30
       Wilma;25
       Pebbles;1
       Dino;5
   PS> $f = import-csv -delimiter ';' file.csv
   PS> $f.Name    # Fred Wilma Pebbles Dino
   PS> $f[1].Name # Wilma
   PS> $f.Age     # 30 25 1 5
   PS> $f[3].Age  # 5
   PS> for ($i =0; $i -lt $f.length; $i++) { 
           write-output("{0,-7} is {1:D} years" -f $f[$i].Name, $f[$i].Age) 
       }

Formatting Output
=================

Very similar to Python ``-f`` operator, examples use ``write-host`` but can be used with other cmdlets, such as assigment.
Specified as ``{<index>, <alignment><width>:<format_spec>}``

::

   PS> $shortText = "Align me"
   PS> $longerText = "Please Align me, but I am very wide"
   
   PS> write-host("{0,-20}" -f $shortText)         # Left-align; no overflow.
   PS> write-host("{0,20}"  -f $shortText)         # Right-align; no overflow.
   PS> write-host("{0,-20}" -f $longerText)        # Left-align; data overflows width.
   
   PS> write-host("Room: {0:D}" -f 232)            # Room: 232
   PS> write-host("Invoice No.: {0:D8}" -f 17)     # Invoice No.: 00000017
   PS> $invoice = "{0}-{1}" -f 00017, 007          # (integers) so invoice = 17-7  
   PS> $invoice = "{0}-{1}" -f '00017', '007'      # (strings) so invoice = 00017-007  
   
   PS> write-host("Temp: {0:F}°C" -f 18.456)       # Temp: 18.46°C
   PS> write-host("Grade: {0:p}" -f 0.875)         # Grade: 87.50%
   PS> write-host('Grade: {0:p0}' -f 0.875)        # Grade: 88%  
   PS> write-host('{1}: {0:p0}' -f 0.875, 'Maths') # Maths: 88%
   
   # Custom formats
   PS> write-output('{1:00000}' -f 'x', 1234)      # 01234
   PS> write-output('{0:0.000}' -f [Math]::Pi)     # 3.142
   PS> write-output('{0:00.0000}' -f 1.23)         # 01.2300
   PS> write-host('{0:####}' -f 1234.567)          # 1235
   PS> write-host('{0:####.##}' -f 1234.567)       # 1234.57
   PS> write-host('{0:#,#}' -f 1234567)            # 1,234,567
   PS> write-host('{0:#,#.##}' -f 1234567.891)     # 1,234,567.89
   
   PS> write-host('{0:000}:{1}' -f 7, 'Bond')      # 007:Bond
   
   PS> get-date -Format 'yyyy-MM-dd:hh:mm:ss'      # 2020-04-27T07:19:05
   PS> get-date -Format 'yyyy-MM-dd:HH:mm:ss'      # 2020-04-27T19:19:05
   PS> get-date -UFormat "%A %m/%d/%Y %R %Z"       # Monday 04/27/2020 19:19 +02

More examples:
* `Formatting Output <http://powershellprimer.com/html/0013.html>`_
* `Get-Date <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-date?view=powershell-6>`_
