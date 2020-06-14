:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/powershell.rst

*********************
PowerShell Cheatsheet
*********************

``PowerShell`` is a modern replacement for the familiar ``DOS`` prompt, which is similar to a DOS, and UNIX Shell, but
is built on ``.Net`` objects, where tasks are performed by ``cmdlets`` (pronounced *command-lets*).

Almost all ``cmdlets`` produce streams of objects which can be redirected in a *UNIX-like* ``>`` ``<``, ``|`` fashion, but be
careful, ``select-string`` produce streams of text. Note ``write-output`` should be used to produce a stream of 
objects to be passed to another ``cmdlet``, and ``write-host``, ``write-warning`` to write only to the console.

``PowerShell`` has a consistent naming convention for ease of learning, which is cumbersome, especially for the command line, 
and so provides an alias mechanism, which is extensible... to make things more **obvious**  (but less *consistent*). 
For example ``ls`` is probably more intuitive than ``get-childitem``, likewise ``cat`` or ``type`` is more intuitive than ``get-content``.
However aliases like ``gc``, ``gci`` or ``sls`` can be confusing. Some ``cmdlets`` can be shortened, for 
example ``where`` as opposed to ``where-object``, other examples include ``select``, ``sort``, ``tee``,  and ``measure``.

The command-line has color-highlighting and ``TAB`` completion for commands and arguments. Try ``import <tab>``, and cycle 
through the alternatives. Cmdlets are **case-insensitive** but hyphens are often required, I try to consistently
use a lower-case format ``get-help`` and not ``Get-Help``. Variable names are also **case-insensitive**, my personal preference 
is to use CamelCase, so ``dateString`` , rather than ``date_string`` although both are supported.

A `Windows Powershell ISE <https://docs.microsoft.com/en-us/powershell/scripting/components/ise/introducing-the-windows-powershell-ise?view=powershell-7>`_  
is provided if you need more interactive assistance.

There are a lot of online documents and tutorials about ``PowerShell`` but as always that means what you are searching far is 
either a complex subject or not well understood or both... so be careful about blindly doing a *copy-paste* of examples.

While learning I found the following helpful:

* `PowerShell GitHub - Learning Powershell <https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell>`_
* `PowerShell equivalents for common Linux/bash commands <https://mathieubuisson.github.io/powershell-linux-bash/>`_
* `10 PowerShell cmdlets you can use instead of CMD commands <https://www.techrepublic.com/article/pro-tip-migrate-to-powershell-from-cmd-with-these-common-cmdlets/>`_

Getting Started
===============

You should become familiar with ``get-help`` and ``get-member`` cmdlets::

   PS> get-help get-childitem         # Help on Get-ChildItem
   PS> get-help get-childiten -online # Online Web based documentation from Microsoft
   PS> get-childitem | get-member     # What is object type, its methods and properties
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

Variables
=========

Powershell variables are loosely-type, and can be integers, strings, arrays, and hash tables, but also objects that represent 
processes, services, event logs, and computers.

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
   mak$d | get-member                # FileInfo, DirectoryInfo Properties and Methods
   
   $p = Get-Process               # System.Diagnostics.Process type

Less common forms::
 
   set-variable -name age 5       # same as $age = 5
   set-variable -name name Dino   # same as $name = "Dino"
   
   set-variable -name pi -option Constant 3.14159
   $pi = 42                       # Fails $pi is a constant
   
   clear-variable -name age       # clear $age; $name = $null
   clear-variable -name p         # clear $p; $p = $null
   
   remove-variable -name age      # delete variable $age
   remove-item -path variable:\p  # delete variable $p


Array Variables
===============

Array variables are a fixed size, can have mixed values and can be multi-dimensional.

::
  
   $a = 1, 2, 3                    # array of integers
   $a = (1, 2, 3)                  # array of integers
   $a = ('a','b','c')
   $a = (1, 2, 3, 'x')             # array of System.Int32's, System.String
   [int[]]$a = (1, 2, 3, 'x')      # will fail 'x', array of System.Int32 only
   
   $a = ('fred','wilma','pebbles')
   $a[0]             # fred
   $a[2]             # pebbles
   $a.length         # 3
   $a[0] = 'freddie' # fred becomes freddie
   $a[4] = 'dino'    # Error: Index was outside the bounds of the array.
   
   $b = ('barbey', 'betty', 'bambam')
   $a = ($a, $b)    # [0]:fred [1]:wilma [2]:pebbles [3]:barney [4]:betty [5]:bambam 
   $a.length        # 6
   $a = ($a, ($b))  # [0]:fred [1]:wilma [2]:pebbles [3][0]:barney [3][1]:betty [3][2]:bambam 
   $a.length        # 4
   
   $ages = (30, 25, 1, 5)
   $names = ('fred','wilma','pebbles', 'dino')
   $a = (($names),($ages))
   $a.length # 4
   $a[0]     # fred wilma pebbles dino
   $a[1]     # 30 25 1 5
   $a[0][0]  # fred
   $a[0][1]  # 30
   
   
Hashe Tables
============

Unordered collection of key:value pairs, later versions of ``PowersShell`` support ``$hash = [ordered]@{}``

::

   $h = @{}              # empty hash
   $key = 'Fred'
   $value = 30
   $h.add($key, $value)
   
   $h.add('Wilma', 25 )
   $h['Pebbles'] = 1
   $h.Dino = 5
   
   $h                 # actual hash, printed if on command-line
   $h['Fred']         # 30
   $h[$key]           # 30
   $h.fred            # 30
   
   # creating a populated hash
   $h = @{
       Fred = 30
       Wilma  = 25
       Pebbles = 1
       Dino = 5
   }
   # creating a populated hash, one-liner
   $h = @{ Fred = 30; Wilma  = 25; Pebbles = 1; Dino = 5 }
   
   $h.keys            # unordered: Dino, Pebbles, Fred, Wilma
   $h.values          # unordered: 5, 1, 30, 25 (same as .keys order)
   
   # random order
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
   
   $h.remove('Dino')                # remove Dino ran away
   $h.clear()                       # family deceased

Excellent review:
* `Hashtables <https://powershellexplained.com/2016-11-06-powershell-hashtable-everything-you-wanted-to-know-about/>`_

Environment
===========

::

   $ get-childitem variable:        # list PowerShell environment variables, 'PSHome', 'PWD' etc.
   $pshome                          # which PowerShell and version
   $pwd                             # working directory
   
   $ get-childitem env:             # get 'cmd.exe' enviroment variables, UCASE by convention
   $env:SystemRoot                  # C:\Windows
   $env:COMPUTERNAME                # MYLAPTOP001
   $env:USERNAME                    # username
   $env:TMP, $env:TEMP              # temp directory
   $env:LIB_PATH='/usr/local/lib'   # setting LIB_PATH     
   
   $psversiontable                  # PowerShell version information.
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

   $ get-content <file> | select-object -last 20             # get last 20 lines
   $ get-content <file> -wait                                # tailing a log-file
   $ get-content <file> | select-object -first 10            # first 10 lines
   $ get-content <file> | select-object -last 10             # last 10 lines
   
   $ select-string <regex> <file> | select-object -first 10  # first 10 occurences of <regex>
   $ select-string <regex> <file> | select-object -last 10   # last 10 occurences of <regex>


Compter Information
===================
::

   # Classnames: Win32_BIOS, Win32_Processor, Win32_ComputerSystem, Win32_LocalTime, 
   #             Win32_LogicalDisk, Win32_LogonSession, Win32_QuickFixEngineering, Win32_Service

   $ get-ciminstance -classname Win32_BIOS                # bios version
   $ get-ciminstance -classname Win32_Processor           # processor information
   $ get-ciminstance -classname Win32_ComputerSystem      # computer name, model etc.
   $ get-ciminstance -classname Win32_QuickFixEngineering # hotfixes installed
   $ get-ciminstance -classname Win32_QuickFixEngineering -property HotFixID | select -property hotfixid

Viewing EventLog
================

* `Event Log Parsing <http://colleenmorrow.com/2012/09/20/parsing-windows-event-logs-with-powershell/>`_
* `Get-WinEvent <https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Diagnostics/Get-WinEvent>`_

::

   $ get-eventlog -logname application | out-host -paging
   $ get-eventlog -logname application -source MSSQLSERVER | out-host -paging
   $ get-eventlog -logname application -source MSSQLSERVER -after 18/6/2019 | out-host -paging
   
   $ (Get-WinEvent -ListLog Application).ProviderNames | out-host -paging
   $ get-winevent -filterhashtable @{logname='application'} | get-member
   $ get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | out-host -paging
   $ get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | where {$_.Message -like '*error*'} | out-host -paging


Formatting Output
=================

Very similar to Python ``-f`` operator, examples use ``write-host`` but can be other output commands.
Specified as ``{<index>, <alignment><width>:<format_spec>}``

::

	$shortText = "Align me"
	$longerText = "Please Align me, but I am very wide"
	PS> write-host("{0,-20}" -f $shortText)		# Left-align; no overflow.
	PS> write-host("{0,20}"  -f $shortText)		# Right-align; no overflow.
	PS> write-host("{0,-20}" -f $longerText)	# Left-align; data overflows width.
	
	PS> write-host("Room: {0:D}" -f 232)		# Room: 232
	PS> write-host("Invoice No.: {0:D8}" -f 17)	# Invoice No.: 00000017
	
	PS> write-host("Temp: {0:F}°C" -f 18.456)	# Temp: 18.46°C
	PS> write-host("Grade: {0:p}" -f 0.875)		# Grade: 87.50%
	PS> write-host('Grade: {0:p0}' -f 0.875)	# Grade: 88%
	
	PS> write-host('{1}: {0:p0}' -f 0.875, 'Maths')	# Maths: 88%
	
	# Custom formats
	PS> write-output('{1:00000}' -f 'x', 1234)	# 01234
	PS> write-output('{0:0.000}' -f [Math]::Pi)	# 3.142
	PS> write-output('{0:00.0000}' -f 1.23)		# 01.2300
	PS> write-host({0:####}' -f 1234.567)		# 1235
	PS> write-host('{0:####.##}' -f 1234.567)	# 1234.57
	PS> write-host('{0:#,#}' -f 1234567)		# 1,234,567
	PS> write-host('{0:#,#.##}' -f 1234567.891)	# 1,234,567.89
	
	PS> get-date -Format 'yyyy-MM-dd:hh:mm:ss'  # 2020-04-27T07:19:05
	PS> get-date -Format 'yyyy-MM-dd:HH:mm:ss'  # 2020-04-27T19:19:05
	PS> get-date -UFormat "%A %m/%d/%Y %R %Z"   # Monday 04/27/2020 19:19 +02

More examples:
* `Formatting Output <http://powershellprimer.com/html/0013.html>`_
* `Get-Date <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-date?view=powershell-6>`_

Command Line History
====================

You can recall and repeat commands::

   $ get-history
   $ invoke-history 1
   $ get-history | select-string -pattern 'ping'
   $ get-history | format-list -property *
   $ get-history -count 100 # get 100 lines (default is 32)
   $ clear-history
   
    Pipelines

    ---------

    PS Y:\> get-childitem -path c:\windows\system32 | out-host -paging # UNIX more command

    


     

     



     

    Classnames: Win32_BIOS, Win32_Processor, Win32_ComputerSystem, Win32_LocalTime, Win32_LogicalDisk, Win32_LogonSession, Win32_QuickFixEngineering, Win32_Service

     

    Out-* cmd-lets

    --------------

    PS Y:\> get-service| format-list | out-host -paging                    # formatted process list

    PS Y:\> get-command | out-null                                         # stdout to /dev/null

    PS Y:\> get-command | out-printer -name "printer-name"                 # send to printer

     

    # Wraps to screen width, add -Width w (1 <= w <= 2147483647)

    PS Y:\> Get-Process | Out-File -FilePath C:\temp\ps.txt                # write unicode text to 'ps.txt'

    PS Y:\> Get-Process | Out-File -FilePath C:\temp\ps.txt -Encoding ASII # write ASCII text output to 'ps.txt'

     

    *** CHK ***

    PS> dir *.ps1 |Select-String function.*NIC$ -Context 1 # 1 line  before/after

    PS> dir *.ps1 |Select-String function.*NIC$ -Context 3 # 3 lines before/after

    https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/compare-object?view=powershell-3.0

    *** KHC ***

     


     

    For MG ProviderName={MGENGINE|MGVPlusIF|ASMSSender|MGBINFO|AppMngSvc.exe}

    Others ProviderName={McAfee Endpoint Security|AVLogEvent|Microsoft-Windows-Security-SPP|SceCli|TPPrn|

                         Desktop Window Manager|Microsoft-Windows-CertificateServices|MSSQLSERVER|

                         Microsoft-Windows-Winlogon|VSS|vmStatsProvider|DSM|SQLSEVERAGENT|MSQLServerOLAPService|VMUpgradeHelper|

                         NetBackup Client Service|NetBackup Legacy Network Service}

     

    PowerShell Quick Intro

    ======================

     

    C:\Users\fred> sl <dir>; cd <dir>                             # set-location, alias 'cd'

    C:\Users\fred> gci                                            # equivalent of 'ls' or 'dir'

    C:\Users\fred> mkdir dir, dir1, dir2                          # make >=1 directories

    C:\Users\fred> sl dir

    C:\Users\fred\dir> ni example.txt, example1.txt, example2.txt # create >=1 empty files.

    C:\Users\fred\dir> write "" > fred.txt                        # create non-empty file

    C:\Users\fred\dir> write "some text to the screen"            # alias 'echo' or 'cat'

    C:\Users\fred\dir> write "some text to the file" > fred.txt   # redirect stdout to a file

    C:\Users\fred\dir> write "add some more text" >> fred.txt     # append stdout to a file

    C:\Users\fred\dir> gc *.txt                                   # 'cat' all '.txt' files (muddled output)

     

    C:\Users\fred\dir> gc fred.txt -totalcount 10                 # head -10 fred.txt ('-head 10' also works)

    C:\Users\fred\dir> gc fred.txt -tail 10                       # tail -10 fred.txt

    C:\Users\fred\dir> gc *.txt -exclude bigben.txt > bigben.txt  # cat all files using wild-card

     

    C:\Users\fred\dir> sls "yet" .\fred.txt                       # Select-String

    fred.txt:3:yet more text

    measuree

    C:\Users\fred> Get-Help gc                                    # man page

    C:\Users\fred> Get-Help gc -online                            # web page help

     

    C:\Users\fred> gc .\fred.txt | measure -l -w -c               # 'wc' of file, Measure-Object

    Lines Words Characters Property

    ----- ----- ---------- --------

        3    19        116

     

    C:\Users\fred> gc .\fred.txt | measure

    Count    : 3

    Average  :

    Sum      :

    Maximum  :

    Minimum  :

    Property :
