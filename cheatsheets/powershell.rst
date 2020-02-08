:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/powershell.rst

**********************
PowerShell Cheatsheet
**********************

About Powershell
================

PowerShell is a task automation and configuration management framework from Microsoft, with a command-line shell and 
associated scripting language. It is a modern replacement for the familiar ``DOS`` propmpt. Tasks are performed by cmdlets 
(pronounced *command-lets*), which are specialized ``.NET`` classes implementing a particular operation which can be connected 
a UNIX like way.

While there are similarties to a UNIX Shell, ``PowerShell`` uses ``.Net`` objects, so you pipe ``objects`` not ``strings`` 
which some consider more powerful, others confusing, if you are from a UNIX Shell background you will find it frustrating.  

Useful Links
------------

* `PowerShell Explained <https://powershellexplained.com/>`_ ** Excellent Reference **
* `MicroSoft PowerShell examples <https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-3.0>`_
* `Powershell Linux <https://mathieubuisson.github.io/powershell-linux-bash/>`_

Introduction
============

PowerShell enforces a consistent naming convention for ease of learning, then promptily provides a set of aliases, 
which you can extend... to make things less consistent. There are ``Setters`` and ``Getters`` like most Object Oriented 
languages, and there is a Get-Help cmdlet, which provides help. This document tries to use the **consistent** form.

The <TAB> key will do command expansion, and because the PowerShell usually returns objects, ``get-member`` comes to the rescue.
 

::

	PS> get-help get-location         # help on the cmd-let.
	PS> get-help get-location -online # opens the help in your browser
	PS> get-location | get-member     # what object is returned?


There are many online guides and tutorials.

* `Learning PowerShell <https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell>`_
* `PowerShell 3.0 <https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-3.0>`_
* `TutorialsPoint PowerShell <https://www.tutorialspoint.com/powershell/index.htm>`_
* `PowerShell Tutorial <http://powershelltutorial.net/>`_


PowerShell Variables
====================


    Advanced DOS Commands:

    - starting services: services.msc

     

    DOS Commands:

    - https://en.wikipedia.org/wiki/List_of_DOS_commands

    - find /?     # https://www.robvanderwoude.com/find.php

    - findstr /?  # https://www.robvanderwoude.com/findstr.php

    - more /?

     

    UNIX-isms

    $ wc -l          # find /v /c "" <filename>

    $ tail -f <file> # https://stackify.com/13-ways-to-tail-a-log-file-on-windows-unix/

    $ history        # https://www.howtogeek.com/298244/how-to-use-your-command-history-in-windows-powershell/

     

 
     

    DOS Tips: https://www.dostips.com/

    PowerShell: https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell

    Grep/Powershell: https://communary.net/2014/11/10/grep-the-powershell-way/

    PowerShell Intro: https://programminghistorian.org/en/lessons/intro-to-powershell#open-powershell

    PowerShell Cmds: https://devblogs.microsoft.com/scripting/table-of-basic-powershell-commands/

    DOS Batch: https://www.robvanderwoude.com/batchfiles.php

     

    PS> $PSVersionTable           # PowerShell version information.

    PS> Y:\> get-host             # PowerShell version information.

     

    Format strings (Python-like)

    http://powershellprimer.com/html/0013.html

     

    Powershell Hashes

    https://powershellexplained.com/2016-11-06-powershell-hashtable-everything-you-wanted-to-know-about/

     

    Powershell Arrays

    https://www.tutorialspoint.com/powershell/powershell_array.htm

     

    PowerShell Objects

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

    PS Y:\> $loc = get-location                    # assign 'get-location' output object to $loc

    PS Y:\> $loc | Get-Member -MemberType Property # shows $loc is a PathInfo object

     

    PS Y:\> Get-Command -Noun Variable | Format-Table -Property Name,Definition -AutoSize -Wrap

    > Clear-Variable, Get-Variable, New-Variable, Remove-Variable, Set-Variable

     

    PS Y:\> clear-variable loc                     # clears '$loc'

    PS Y:\> remove-variable loc                    # removes '$loc'

     

    PS Y:\> get-childitem variable:                # list PowerShell environment variables, 'PSHome', 'PWD' etc.

    PS Y:\> $pshome                                # which PowerShell and version

    PS Y:\> $pwd

     

    PS Y:\> Get-ChildItem env:                     # get 'cmd.exe' enviroment variables, UCASE by convention

    PS Y:\> $env:SystemRoot                        # C:\Windows

    PS Y:\> $env:COMPUTERNAME                      # MYCHCWHQLT01080

    PS Y:\> $env:LIB_PATH='/usr/local/lib'         # setting LIB_PATH

     

    PS Y:\> $PSVersionTable                        # PowerShell version information.

    PS Y:\> get-host                               # PowerShell version information.

     

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
