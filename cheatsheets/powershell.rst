:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/powershell.rst

*********************
PowerShell Cheatsheet
*********************

PowerShell is a modern replacement for the familiar ``DOS`` prompt, and while there are similarities to a DOS, and UNIX Shell, 
``PowerShell`` is built on ``.Net`` objects, where tasks are performed by ``cmdlets`` (pronounced *command-lets*).

It has a consistent naming convention for ease of learning, which is cumbersome, especially for the command line, 
and so provides an alias mechanism, which is extensible... to make things more **obvious**  (but less *consistent*). 
For example ``ls`` is probably more intuitive than ``get-childitem``, likewise ``cat`` or ``type`` is more intuitive than ``get-content``.
Likewise ``tee``, ``select``, ``where``, ``sort`` and easier on the eye than the ``*-object`` full-name form.
Some aliases like ``gc``, ``gci`` or ``sls`` can be confusing and frustrating.

The ``cmdlets`` produce streams of objects which can be redirected in a *UNIX-like* ``>`` ``<``, ``|`` fashion, but some
such as ``select-string`` produce streams of text, so be careful. Note ``write-output`` should be used to produce a stream of 
objects, ``write-host``, ``write-warning`` write to the console.

The command-line has color-highlighting and ``TAB`` completion for commands and arguments. Try ``import <tab>``, and cycle 
through the alternatives. Cmdlets are **case-insensitive** but hyphens are often required, I will try to consistently
use a lower-case format ``get-help`` and not ``Get-Help``. Variable names are also **case-insensitive**, my personal preference 
is to use CamelCase to make things more readable, so ``dateString`` , rather than ``date_string``. 

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

   PS> $age = 5                       # System.Int32
   PS> [int]$age = "5"                # System.Int32
   PS> $name = "Dino"                 # System.String
   PS> $name + $age                   # Fails; System.String + System.Int32
   PS> $name + [string]$age           # Dino5; System.String + System.String

   PS> $c = (5, 30, 25, 1)            # array of System.Int32
   PS> $c = (5, "Dino")               # array of (System.Int32, System.String)

   PS> $f = @{ Fred = 30; Wilma  = 25; Pebbles = 1; Dino = 5 } # hash table
   
   PS> $d = Get-ChildItem C:\Windows  # directory listing, FileInfo and DirectoryInfo types, 
   PS> $d | get-member                # FileInfo, DirectoryInfo Properties and Methods
   
   PS> $p = Get-Process               # System.Diagnostics.Process type

Less common forms::
 
   PS> set-variable -name age 5       # same as $age = 5
   PS> set-variable -name name Dino   # same as $name = "Dino"
   
   PS> set-variable -name pi -option Constant 3.14159 # Declare a constant
   PS> $pi = 42                       # Fails $pi is a constant
   
   PS> clear-variable -name age       # clear $age, ($null)
   PS> clear-variable -name p         # clear $p ($null)
   
   PS> remove-variable -name age      # delete variable $age
   PS> Remove-Item -Path Variable:\p  # delete variable $p


Array Variables
===============

::   
   $c = 1, 2, 3                    # array of integers
   $c = (1, 2, 3)                  # array of integers
   $c = (1, 2, 3, 'x')             # array of System.Int32's, System.String
   [int[]]$c = (1, 2, 3, 'x')      # will fail 'x', array of System.Int32 only

   
   

::


	PS> $loc = get-location                    # assign 'get-location' output object to $loc
    PS> $loc | get-member -membertype property # shows $loc is a PathInfo object
     
    
    PS> get-command -noun variable             # What commands work with variables
    > clear-variable, get-variable, new-variable, remove-variable, set-variable
     
    PS> clear-variable loc                     # clears '$loc', NOTE the missing '$'
    PS> remove-variable loc                    # removes '$loc', NOTE the missing '$'

    PS> get-childitem variable:                # list PowerShell environment variables, 'PSHome', 'PWD' etc.
    PS> $pshome                                # which PowerShell and version
    PS> $pwd

    PS> get-childitem env:                     # get 'cmd.exe' enviroment variables, UCASE by convention
    PS> $env:SystemRoot                        # C:\Windows
    PS> $env:COMPUTERNAME                      # MYLAPTOP001
    PS> $env:LIB_PATH='/usr/local/lib'         # setting LIB_PATH     

    PS> $psversiontable                        # PowerShell version information.
    PS> get-host                               # PowerShell version information.

Command Line History
--------------------

You can recall and repeat commands::

	PS> get-history
	PS> invoke-history 1
	PS> get-history | select-string -pattern 'ping'
	PS> get-history | format-list -property *
	PS> get-history -count 100 # get 100 lines (default is 32)
	PS> clear-history
	
	
Formatting Output
-----------------
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

Powershell Hashes
-----------------
::

	$flintstones = @{}              # empty hash
	$key = 'Fred'
	$value = 30
	$flintstones.add($key, $value)
	
	$flintstones.add('Wilma', 25 )
	$flintstones['Pebbles'] = 1
	$flintstones.Dino = 5
	
	$flinstones                  # actual hash, printed if on command-line
	$flintstones['Fred']         # 30
	$flintstones[$key]           # 30
	$flintstones.fred            # 30
	
	# creating a populated hash
	$flintstones = @{
	    Fred = 30
	    Wilma  = 25
	    Pebbles = 1
	    Dino = 5
	}
	# creating a populated hash, one-liner
	$flintstones = @{ Fred = 30; Wilma  = 25; Pebbles = 1; Dino = 5 }
	
	# Order not guaranteed in the folloiwng, use sort or $hash = [ordered]@{}, if supported
	
	foreach($key in $flintstones.keys) {
	    write-output ('{0} Flintstone is {1:D} years old' -f $key, $flintstones[$key])
	}
	
	$flintstones.keys                          # Fred, Wilma, Pebbles, Dino
	$flintstones.values                        # 30, 25, 1, 5 
	
	if ($flintstones.ContainsKey('fred')) {}   # true 
	if ($flintstones.ContainsKey('barney')) {} # false

	
	$flintstones.remove('Dino')                # Dino ran away
	$flintstones.clear()                       # family deceased

Excellent review:
* `Hashtables <https://powershellexplained.com/2016-11-06-powershell-hashtable-everything-you-wanted-to-know-about/>`_

Functions
---------
Write something

Function Arguments
------------------
PowerShell allows mixed named and positional arguments which is not always clear.
Safest way of passing function arguments, is to use ``splatting`` 

::
  
	$arguments = @{
		Name        = 'TestNetwork'
		StartRange  = '10.0.0.2'
		EndRange    = '10.0.0.254'
		SubnetMask  = '255.255.255.0'
		Description = 'Network for testlab A'
		LeaseDuration = (New-TimeSpan -Days 8)
		Type = "Both"
	}
	Add-DhcpServerv4Scope @arguments   

Powershell Arrays
-----------------
Arrays are a fixed size, can have mixed values, and be multi-dimensional.
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	$A = (1, 2, 3, 4)                 # 1, 2, 3, 4
	$A = 1..4                         # 1, 2, 3, 4
	$B = ('F', 'W', 'P', 'D')         # 'F', 'W', 'P', 'D'
	$C = (5.6, 4.5, 3.3, 13.2)        # 5.6, 4.5, 3.3, 13.2
	$D = ('Apple', 3.3, 13.2, $B)     # 'Apple', 3.3, 13.2, 'F', 'W', 'P', 'D'
	
	[char[]]$E = ('F', 'W', 'P', 'D') # only [char] values


* `Arrays TutorialsPoint <https://www.tutorialspoint.com/powershell/powershell_array.htm>`_

PowerShell ArrayList and Generic List
-------------------------------------

* `ArrayList PowerS<https://powershellexplained.com/2018-10-15-Powershell-arrays-Everything-you-wanted-to-know/>`_
* `ArrayList Microsoft <https://docs.microsoft.com/en-us/dotnet/api/system.collections.arraylist?view=netframework-4.8>`_
* `Collections in General <https://gist.github.com/kevinblumenfeld/4a698dbc90272a336ed9367b11d91f1c>`_ 

PowerShell Objects
------------------

    https://powershellexplained.com/2016-10-28-powershell-everything-you-wanted-to-know-about-pscustomobject/

     

    Powershell ArrayList

    https://docs.microsoft.com/en-us/dotnet/api/system.collections.arraylist.remove?view=netframework-4.8

    https://powershellexplained.com/2018-10-15-Powershell-arrays-Everything-you-wanted-to-know/

     

    https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-error?view=powershell-3.0

     

    String Splitting

    ================

    The string.split() method does not support regex, but -Split() operator does; confusing!

     

    PS Y:\> "A B     CD".split('\s+')

    A B     CD

     

    PS Y:\> "A B     CD" -Split('\s+')

    A

    B

    CD

     

    PowerShell Intro

    ================

    https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell

    https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-3.0

    https://www.tutorialspoint.com/powershell/index.htm

    http://powershelltutorial.net/

     

    Commands

    --------

    PS Y:\> get-command [<pattern>]           # what commands are available

    PS Y:\> get-command get-help -syntax      # syntax of get-help

    PS Y:\> get-command -CommandType Alias    # list all Aliases

    PS Y:\> get-command -CommandType Alias gc # 'gc' maps to what, throws exception if missing

    PS Y:\> get-command -CommandType <type>   # Alias|Function|Script

     

    Variables

    ---------

 
     

    Pipelines

    ---------

    PS Y:\> get-childitem -path c:\windows\system32 | out-host -paging # UNIX more command

    


     

    # https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-object?view=powershell-3.0

    # https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/sort-object?view=powershell-3.0

    # https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-3.0

     

    PS Y:\> get-process | get-member                                                     # show returned object

    PS Y:\> get-process | select-object -first 10                                        # first 10 processes

    PS Y:\> get-process | select-object -last 10                                         # last 10 processes

    PS Y:\> get-process | sort-object -property WS | select-object -last 10              # last 10 sorted

    PS Y:\> get-process | sort-object -property WS | select-object -first 10             # first 10 sorted

    PS Y:\> get-process | sort-object -property WS -descending | select-object -first 10 # reverse sort first 10

    PS Y:\> Get-Process | Where-Object {$_.ProcessName -Match "^p.*"}                    # find all processes that start with "p"

    PS Y:\> get-content <file> | select-object -last 20                                  # get last 20 lines

    PS Y:\> get-content <file> -wait                                                     # tailing a log-file

    PS Y:\> get-process | select-object -property Name,Id,WS | out-host -paging

     

    PS Y:\> get-content <file> | select-object -first 10                                 # first 10 lines

    PS Y:\> get-content <file> | select-object -last 10                                  # last 10 lines

    PS Y:\> select-string <regex> <file> | select-object -first 10                       # first 10 occurences of <regex>

    PS Y:\> select-string <regex> <file> | select-object -last 10                        # last 10 occurences of <regex>

     

    Compter Info

    ------------

    PS Y:\> get-ciminstance -classname Win32_BIOS                # bios version

    PS Y:\> get-ciminstance -classname Win32_Processor           # processor information

    PS Y:\> get-ciminstance -classname Win32_ComputerSystem      # computer name, model etc.

    PS Y:\> get-ciminstance -classname Win32_QuickFixEngineering # hotfixes installed

    PS Y:\> get-ciminstance -classname Win32_QuickFixEngineering -property HotFixID | select-object -property hotfixid

     

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

     

    Event Log Parsing

    -----------------

    http://colleenmorrow.com/2012/09/20/parsing-windows-event-logs-with-powershell/

     

    PS> get-eventlog -logname application -source MSSQLSERVER | out-host -paging

    PS> get-eventlog -logname application -source MSSQLSERVER -after 18/6/2019 | out-host -paging

    PS> get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | out-host -paging

    PS> get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | where-object {$_.Message -like '*error*'} | out-host -paging

    PS> get-winevent -filterhashtable @{logname='application'} | get-member

    PS> get-winevent -filterhashtable @{logname='application'} | get-member

    PS> (Get-WinEvent -ListLog Application).ProviderNames | select-string "^MG"

     

    PS> (Get-WinEvent -ListLog Application).ProviderNames

    https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Diagnostics/Get-WinEvent?view=powershell-3.0

     

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
