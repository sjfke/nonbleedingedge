:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/powershell.rst

*********************
PowerShell Cheatsheet
*********************

This is the companion to ``PowerShell Scripts Cheatsheet``, which focuses on command line usage.

``PowerShell`` is a modern replacement for the familiar ``DOS`` prompt, which is similar to a UNIX Shell, but
is built on ``.Net`` objects, where tasks are performed by ``cmdlets`` (pronounced *command-lets*).

Unlike most shells, which accept and return text, ``PowerShell`` is built on top of the ``.NET Common Language Runtime`` (CLR), 
and accepts and returns ``.NET objects``. The ``.Net objects`` produce by ``cmdlets`` can be chained together, assigned to 
variables and redirected in a *UNIX-like* ``>`` ``<``, ``|`` fashion.

For ease of learning ``PowerShell`` uses a consistent ``cmdlet`` naming convention, which is cumbersome for a command line, 
and so provides an extensible alias mechanism... which make things *easier*  (but less *consistent*). 
For example ``ls`` is probably more intuitive than ``get-childitem``, likewise ``cat`` or ``type`` are more intuitive than ``get-content``.
Aliases like ``gc``, ``gci`` or ``sls`` can be confusing when starting. 

The command-line has color-highlighting and has ``TAB`` completion for commands and arguments, try ``import <tab>``, or ``get-help -<tab>`` and cycle 
through the alternatives. Cmdlets are **case-insensitive** but hyphens are significant, but for many ending in ``-object`` can be shortened, so ``where-object`` 
can be written as ``where``, which in my opinion is clearer. Other ``*-object`` examples include ``select``, ``sort``, ``tee``,  and ``measure``.

Variable names are also **case-insensitive**, can include ``_``, and **camelCase** can be used to make variable names more human readable, but *camelCase* is 
irrelevent to ``PowerShell``, so ``dogCat``, ``dogcat`` and ``DogCat`` are the same variable.

My personal preference:

* lower-case format for ``cmdlets``, so ``get-help`` rather than ``Get-Help``;
* camelCase for variable names, so ``dateString`` , rather than ``date_string``;

A `Windows Powershell ISE <https://docs.microsoft.com/en-us/powershell/scripting/components/ise/introducing-the-windows-powershell-ise?view=powershell-7>`_  
is provided if you need more interactive assistance and is very useful when learning. You might also want to consider `Windows Terminal <https://github.com/microsoft/terminal>`_ which supports various command-line tools and shells like 
Command Prompt, PowerShell, WSL, and includes multiple tabs, panes, Unicode and UTF-8 character support, a GPU accelerated text rendering engine, and 
custom themes, styles, and configurations.

There are a lot of online documents and tutorials about ``PowerShell`` but unfortunately, as is often the case, this means what you are searching for is 
either not simple to explain or not well understood by the author(s) or both... so be careful about blindly doing a *copy-and-paste* of examples.

While learning I found the following helpful when starting:

* `PowerShell GitHub - Recommended Training and Reading <https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell#recommended-training-and-reading>`_ **a very good place to start**
* `PowerShell GitHub - Learning Powershell <https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell>`_
* `PowerShell equivalents for common Linux/bash commands <https://mathieubuisson.github.io/powershell-linux-bash/>`_
* `10 PowerShell cmdlets you can use instead of CMD commands <https://www.techrepublic.com/article/pro-tip-migrate-to-powershell-from-cmd-with-these-common-cmdlets/>`_

Getting Started
===============

Like any shell, PowerShell provides an environment which allows interaction with files, folders, processes, the computer and network interfaces etc, but as 
objects, for example:

* An ``Item`` object, which can be a *file*, *directory*, *link*, *registry-key* etc;
* A ``ChildItem`` object, children of the current folder (location);
* A ``Location`` object, where you are in the file system;
* A ``Process`` object, details of running process(es);
* An ``MSFT_NetAdapter`` object, for network interfaces;
* A ``ComputerInfo`` object, providing details of the computer, operating system etc;

::

   PS> get-childitem                      # directory listing
   PS> get-computerinfo                   # computer information
   PS> get-netadapter                     # network interfaces
   PS> get-process                        # running processes
   PS> get-command                        # powershell commands

You should become familiar with ``get-help`` and ``get-member`` cmdlets::

   PS> get-help get-childitem             # Help on Get-ChildItem
   PS> get-help get-childiten -online     # Online Web based documentation from Microsoft
   PS> get-help get-childitem -showWindow # Help in a separate window
   PS> get-childitem | get-member         # What is the object type, its methods and properties

    
   PS> get-help get-content               # notice its aliases 'gc', 'cat', 'type'
   PS> get-help select-string             # regular-expression based string search (like UNIX grep)
   PS> get-help get-location              # alias 'gl' and 'pwd'.
   PS> get-help get-command               # what commands are available
   PS> get-help select-object             # 'select' or set object properties
   PS> get-help where-object              # 'where' filter on object property
   PS> get-help tee-object                # 'tee' like the UNIX command
   PS> get-help sort-object               # object property based sorting, (like UNIX 'sort')
   PS> get-help measure-object            # count lines, characters (like UNIX 'wc')
   PS> get-help out-host                  # Similar to UNIX 'more' and 'less'

Quick Introduction
==================

Examples of common commands.

::

   PS> set-location dir                            # change directory, ('sl', 'cd', 'chdir')
   PS> cd dir                                      # using the 'cd' alias to change directory
   PS> get-childitem                               # directory listing, ('gci','ls','dir')
   PS> ls                                          # using the 'ls' alias to get directory listing
   PS> new-item -ItemType Directory dir1           # create directory dir1 ('ni')
   PS> mkdir dir1, dir2                            # *convenience function* make two directories ('md')
   PS> remove-item dir2                            # delete a directory
   PS> rmdir dir2                                  # using the 'rmdir' alias to delete a directory
   
   PS> new-item fred.txt, wilma.txt                # create two empty files ('ni')
   PS> remove-item fred.txt                        # delete file ('ri','rm','rmdir','del','erase','rd')
   PS> rm fred.txt                                 # using the 'rm' alias to delete a file
   
   PS> write-output "" > fred.txt                  # create an empty file ('write','echo')
   PS> echo "" > fred.txt                          # using alias to create an empty file
   PS> write-output "some text to the stdout"      # can be piped ('write','echo')
   PS> write-host "some text to the console"       # cannot be piped
   PS> write-host -BackgroundColor Blue "BLOD"     # Blue Line of Death (SIC)
   PS> write-warning "console message"             # WARNING: console message - color highlighting
   PS> write-output "write some text" > fred.txt   # redirect stdout to a Unicode file
   PS> write-output "append some text" >> fred.txt # append stdout to a Unicode file
   
   PS> write-output "ascii text" | add-content -encoding ASCII fred.txt # 7-bit ASCII file
   PS> write-error "stack trace like message"
   
   PS> get-item <file> | select -property Name,Length,Mode,CreationTime
   
   PS> get-content fred.txt                        # display contents, ('gc','cat','type')
   PS> cat fred.txt                                # using the 'cat' alias to display contents
   PS> remove-item fred.txt                        # delete a file, ('ri','rm','rmdir', 'del','erase','rd')
   PS> rm fred.txt                                 # using the 'rm' alias to delete a file
   
   # Starting applications, start-process ('saps','start')
   #   Note: quotes, pathnames and file extensions are typically optional
   PS> start-process 'notepad'                     # open notepad.exe (can use notepad.exe)
   PS> start-process 'https://nonbleedingedge.com' # open URL with browser (Microsoft-Edge)
   PS> start-process 'explorer'                    # start explorer.exe (can use explorer.exe)
   PS> start-process explorer C:\Windows\          # start explorer.exe in C:\Windows\
   PS> start-process explorer $PWD                 # start explorer.exe in current directory
   PS> start-process chrome                        # start google chrome (if installed)
   PS> start-process notepad++                     # start Notepad++ (if installed)
   
   PS> get-service | out-host -paging              # paged listing of the services
   PS> get-process | out-host -paging              # paged listing of the processes

   PS> get-computerinfo                            # computer information
   PS> get-disk                                    # disk serial number, state etc.
   PS> get-volume                                  # volumes on your disk.

Some references which may help at the beginning.

* `PowerShell for Experienced Bash users <https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell#map-book-for-experienced-bash-users>`_
* `10 basic PowerShell commands that every Windows 10 user should know <https://www.thewindowsclub.com/basic-powershell-commands-windows>`_
* `10 PowerShell commands every Windows admin should know <https://www.techrepublic.com/blog/10-things/10-powershell-commands-every-windows-admin-should-know/>`_

Environment
===========

::

   PS> get-childitem variable:        # list PowerShell environment variables, 'PSHome', 'PWD' etc.
   PS> $pshome                        # variable containing which PowerShell and version
   PS> $pwd                           # variable containing the working directory
   
   PS> get-childitem env:             # get 'cmd.exe' enviroment variables, UCASE by convention
   PS> $env:SystemRoot                # variable containing C:\Windows
   PS> $env:COMPUTERNAME              # variable containing MYLAPTOP001
   PS> $env:USERNAME                  # variable containing username
   PS> $env:TMP, $env:TEMP            # variable containing temp directory
   PS> $env:LIB_PATH='/usr/local/lib' # setting LIB_PATH variable 
   
   PS> $psversiontable                # variable containing PowerShell version information.
   PS> get-host                       # PowerShell version information.

Processes
=========

::

   PS> get-process | get-member                                       # show returned object
   PS> get-process | select -first 10                                 # first 10 processes
   PS> get-process | select -last 10                                  # last 10 processes
   PS> get-process | sort -property workingset | select -last 10      # last 10 sorted on workingset
   PS> get-process | sort -property workingset | select -first 10     # first 10 sorted on workingset
   PS> get-process | sort -property ws -descending | select -first 10 # reversed first 10 (ws=workingset)
   PS> get-process | where {$_.processname -match "^p.*"}             # all processes starting with "p"
   PS> get-process | select -property Name,Id,WS | out-host -paging   # paged (more/less) output
   PS> get-process | out-gridview                                     # interactive static table view
   
   PS> start-process notepad                # start notepad
   PS> $p = get-process -name notepad       # finds all notepad processes! (Array like)
   PS> stop-process -name notepad           # terminate all notepad processes!
   PS> stop-process -name notepad -whatif   # what would happen if run :-)
   PS> stop-process -id $p.id               # terminate by id, (confirmation prompt if not yours)
   PS> stop-process -id $p[0].id            # terminate by id, (confirmation prompt if not yours)
   PS> stop-process -id $p.id -force        # terminate by id, (no confirmation prompt if not yours)
   
   PS> $p = start-process notepad -passthru # start notepad, -passthru to return the process object
   PS> $p | get-member                      # methods and properties, (only 4 examples shown)
   PS> $p.cpu                               # how much CPU has notepad used
   PS> $p.Modules                           # which .dll's are being used
   PS> $p.Threads.Count                     # how many threads
   PS> $p.kill()                            # terminate
   PS> stop-process -id $p.id               # terminate by id
   PS> remove-variable -name p              # $p is not $null after process termination
   
Executables
===========

::

   PS> get-command notepad
   
   CommandType     Name                                               Version    Source
   -----------     ----                                               -------    ------
   Application     notepad.exe                                        10.0.19... C:\WINDOWS\system32\notepad.exe
   
   
   PS> get-command notepad -All
   
   CommandType     Name                                               Version    Source
   -----------     ----                                               -------    ------
   Application     notepad.exe                                        10.0.19... C:\WINDOWS\system32\notepad.exe
   Application     notepad.exe                                        10.0.19... C:\WINDOWS\notepad.exe
   
   PS> get-command notepad | format-list
   
   Name            : notepad.exe
   CommandType     : Application
   Definition      : C:\WINDOWS\system32\notepad.exe
   Extension       : .exe
   Path            : C:\WINDOWS\system32\notepad.exe
   FileVersionInfo : File:             C:\WINDOWS\system32\notepad.exe
                     InternalName:     Notepad
                     OriginalFilename: NOTEPAD.EXE.MUI
                     FileVersion:      10.0.19041.1766 (WinBuild.160101.0800)
                     FileDescription:  Notepad
                     Product:          Microsoft® Windows® Operating System
                     ProductVersion:   10.0.19041.1766
                     Debug:            False
                     Patched:          False
                     PreRelease:       False
                     PrivateBuild:     False
                     SpecialBuild:     False
                     Language:         English (United Kingdom)

Files and Folders
=================
::

   PS> new-item fred.txt, wilma.txt                     # create two empty files ('ni')
   PS> remove-item fred.txt                             # delete file ('ri','rm','rmdir','del','erase','rd')
   PS> rm fred.txt                                      # using the 'rm' alias to delete a file
   
   PS> new-item -ItemType Directory dir1                # create directory dir1 ('ni')
   PS> mkdir dir1, dir2                                 # *convenience function* make two directories ('md')
   PS> remove-item dir2                                 # delete a directory
   PS> rmdir dir2                                       # using the 'rmdir' alias to delete a directory

   PS> get-childitem -path 'C:\Program Files\'          # list folder contents (gci,ls)          
   PS> ls 'C:\Program Files\'                           # list folder contents A => Z
   PS> get-childitem -path 'C:\Program Files\' -recurse # recursively list folder contents
   
   PS> get-childitem -path 'C:\Program Files\' | sort -Descending   # sorted Z => A
   PS> get-childitem -path 'C:\Program Files\' | select -property * # every childitem property
   
   PS> write-output 'fred' > fred.txt                   # create file and add content (UTF8 encoded)
   
   PS> set-content -value "Fred" fred.txt               # create file and add content (see -encoding)
   PS> add-content -value "Freddie" fred.txt            # append content
   PS> write-output "Freddy" | add-content fred.txt     # append content
   PS> get-content fred.txt                             
   Fred
   Freddie
   Freddy
   PS> set-content -value $null fred.txt                # empty content

   PS> get-content <file> -wait                         # tailing a log-file
   PS> get-content <file> | select -first 10            # first 10 lines
   PS> get-content <file> | select -last 10             # last 10 lines
   
   PS> get-content <file> | measure -line -word         # count lines, words   
   PS> get-content <file> | measure -character          # count characters   
 
   PS> select-string 'str1' <file>                      # all lines containing 'str1'
   PS> select-string -NotMatch 'str1' <file>            # all lines *not* containing 'str1'
   PS> select-string ('str1','str2') <file>             # all lines containing 'str1' or 'str2'
   PS> select-string -NotMatch ('str1','str2') <file>   # all lines *not* containing 'str1' or 'str2'
   
   PS> select-string <regex> <file> | select -first 10  # first 10 lines containing <regex>
   PS> select-string <regex> <file> | select -last 10   # last 10 lines containing of <regex>

Command Line History
====================

You can recall and repeat commands::

   PS> get-history
   PS> invoke-history 10                                   # execute 10 in your history (aliases 'r' and 'ihy')
   PS> r 10                                                # same using the alias
   PS> get-history | select-string -pattern 'get'          # all the get-commands in your command history
   PS> get-history | where {$_.CommandLine -like "*get*"}  # all the get-commands in your command history
   PS> get-history | format-list -property *               # execution Start/EndExecutiontimes and status             
   PS> get-history -count 100                              # get 100 lines
   PS> clear-history

Computer Information
====================
::

   PS> systeminfo | more                                          # summary of the computer and more 
   PS> systeminfo | select-string 'System Boot Time'              # boot time
   PS> systeminfo | select-string @('System Model', 'OS Version') # model, os and bios
   
   # Classnames: Win32_BIOS, Win32_Processor, Win32_ComputerSystem, Win32_LocalTime, 
   #             Win32_LogicalDisk, Win32_LogonSession, Win32_QuickFixEngineering, Win32_Service
   PS> get-cimclass | out-host -paging                      # lists all available classes

   PS> get-ciminstance -classname Win32_BIOS                # bios version
   PS> get-ciminstance -classname Win32_Processor           # processor information
   PS> get-ciminstance -classname Win32_ComputerSystem      # computer name, model etc.
   PS> get-ciminstance -classname Win32_QuickFixEngineering # hotfixes installed on which date
   PS> get-ciminstance -classname Win32_QuickFixEngineering -property HotFixID | select -property hotfixid

Further reading:

* `Introduction to CIM Cmdlets <https://devblogs.microsoft.com/powershell/introduction-to-cim-cmdlets/>`_
* `Microsoft Docs: Get-CimInstance <https://docs.microsoft.com/en-us/powershell/module/cimcmdlets/get-ciminstance>`_

Network Information
===================

A lot more information is available than shown here, see further reading.

::

   PS> Get-NetAdapter -physical                  # Physical interfaces: Name, Status, Mac Address, Speed
   PS> Get-NetAdapter                            # All interfaces: Name, Status, Mac Address, Speed
   PS> Get-NetAdapterAdvancedProperty -Name Wifi # Properties of Wifi interface
   PS> Get-NetIPAddress | Format-Table           # IP address per interface, for ifIndex, see Get-NetAdapter

Further reading:

* `Microsoft Docs: NetTCPIP <https://docs.microsoft.com/en-us/powershell/module/nettcpip>`_

Services
========

::

   PS> get-service | out-host -Paging                     # paged listing of the services
   PS> get-service | where -property Status -eq 'running' # all running services
   PS> start-service <service name>
   PS> stop-service <service name>
   PS> suspend-service <service name>
   PS> resume-service <service name>
   PS> restart-service <service name>


Windows EventLog
================

::

   # Gets events from event logs and event tracing log files
   PS> (Get-WinEvent -ListLog Application).ProviderNames | out-host -paging  # who is writing Application logs
   
   PS> get-winevent -filterhashtable @{logname='application'} | get-member # slow ... be patient :-)
   
   PS> get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | out-host -paging
   PS> get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | where {$_.Message -like '*error*'} | out-host -paging

   # Uses deprecated Win32 API, last reference PowerShell 5 docs, but still works on Windows 10 Home
   PS> get-eventlog -list                                                    # list a summary count of the events
   PS> get-eventlog -logname system -newest 5                                # last 5 system events
   PS> get-eventlog -logname system -entrytype error | out-host -paging      # system error events

   PS> get-eventlog -logname application | out-host -paging                  # lists application events (with index number)
   PS> get-eventlog -logname application -Index 14338 | select -Property *   # details of application event 14338

   PS> $events = get-eventlog -logname system -newest 1000                   # capture last 1000 system events
   PS> $events | group -property source -noelement | sort -property count -descending # categorize them
   
   PS> get-eventlog -logname application -source MSSQLSERVER | out-host -paging
   PS> get-eventlog -logname application -source MSSQLSERVER -after '11/18/2020' | out-host -paging
   
Further reading:

* `Collen M. Morrow: Parsing Windows event logs with PowerShell <https://colleenmorrow.com/2012/09/20/parsing-windows-event-logs-with-powershell/>`_
* `Microsoft Docs: Get-WinEvent <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent>`_
* `Microsoft Docs: Get-EventLog <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-eventlog>`_

HotFixes
========

::

   PS> get-hotfix                    # list all installed hot fixes and their ID
   PS> get-hotfix -Id KB4516115      # when was hotfix installed
   
   # To get hotfix details (example is a random choice, happens to be an Adobe Flash update)
   PS> start-process "https://www.catalog.update.microsoft.com/Search.aspx?q=KB4516115" 

Network TCPIP
=============

::

   PS> test-netconnection                                  # ping internetbeacon.msedge.net
   PS> test-netconnection -computername localhost          # ping oneself
   PS> test-netconnection -computername localhost -port 80 # ping local web-server
   PS> test-netconnection -computername "www.google.com" -informationlevel "detailed" -port 80
   PS> test-netconnection -computername "www.google.com" -informationlevel "detailed" -port 443
   PS> test-netconnection -traceroute -computername "www.google.com"


   PS> get-netipaddress | format-table                     # configured IP addresses
   PS> get-netipaddress -suffixorigin dhcp                 # DHCP IP address
   PS> get-netipaddress -suffixorigin manual               # Manual IP address
   
DNS Resolver
============

::

   PS> resolve-dnsname -name www.google.com               # IP address of google.com
   PS> resolve-dnsname -name 172.217.168.4                # reverse IP of www.google.com
   PS> resolve-dnsname -name 2a00:1450:400a:801::2004     # reverse IP of www.google.com

   PS> resolve-dnsname -Name www.gmail.com                # Address records
   PS> resolve-dnsname -Name www.gmail.com -Type MX       # Mail Exchange records
   
   PS> resolve-dnsname www.google.com -Server 192.168.1.1 # Specific name server
   
   PS> $dnsServer = @('8.8.8.8','8.8.4.4')                # Google Public DNS Server IPs
   PS> resolve-dnsname www.google.com -server $dnsServer  # Specific name servers
   
   PS> get-dnsclientcache                                 # list your DNS cache
   PS> clear-dnsclientcache                               # empty you DNS cache
   
   PS> ipconfig /all                                      # DNS servers DOS command
   PS> get-dnsclientserveraddress                         # DNS servers 

The examples are very simple, much more is possible, but remember an object is returned not text.

More detailed examples:


* `AdamTheAutomator: Resolving DNS Records with PowerShell <https://adamtheautomator.com/resolve-dnsname/>`_
* `Microsoft Docs: Resolve-DnsName <https://docs.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname>`_
* `Microsoft Docs: DnsClient Module <https://docs.microsoft.com/en-us/powershell/module/dnsclient/>`_


Web-Pages and REST API's
========================

::

   # web-pages
   PS> (Invoke-WebRequest -uri "https://www.nonbleedingedge.com/missing.html").statuscode       # error: (404) Not Found.
   PS> (Invoke-WebRequest -uri "https://www.nonbleedingedge.com").statuscode                    # 200
   PS> Invoke-WebRequest -uri "https://www.nonbleedingedge.com/index.html" -outfile "index.htm" # index.htm
   
   # rest-api
   PS> Invoke-RestMethod -uri https://blogs.msdn.microsoft.com/powershell/feed/
   PS> Invoke-RestMethod -uri https://blogs.msdn.microsoft.com/powershell/feed/ | Format-Table -Property Title, pubDate
   
   title                                                             pubDate
   -----                                                             -------
   SecretStore Release Candidate 3                                   Mon, 15 Mar 2021 22:12:04 +0000
   Updating help for the PSReadLine module in Windows PowerShell 5.1 Thu, 11 Mar 2021 15:29:00 +0000
   Announcing PSReadLine 2.2-beta.2 with Dynamic help                Fri, 05 Mar 2021 20:09:10 +0000
   SecretManagement and SecretStore Release Candidate 2              Wed, 03 Mar 2021 18:55:58 +0000
   PowerShell Team 2021 Investments                                  Tue, 02 Mar 2021 14:19:46 +0000
   PowerShell for Visual Studio Code Updates – February 2021         Thu, 25 Feb 2021 20:52:17 +0000
   Announcing PowerShell Community Blog                              Thu, 18 Feb 2021 17:28:05 +0000
   SecretManagement and SecretStore Release Candidates               Thu, 07 Jan 2021 18:19:44 +0000
   PowerShell 7.2 Preview 2 release                                  Wed, 16 Dec 2020 00:08:04 +0000
   Announcing PowerShell Crescendo Preview.1                         Tue, 08 Dec 2020 17:20:18 +0000

::
   
   PS> [system.web.httputility]::urlencode("https://test.com/q?name=fred flinstone&age=35")
   https%3a%2f%2ftest.com%2fsearch%3fname%3dfred+flinstone%26age%3d35

   PS> [system.web.httputility]::urldecode("https%3a%2f%2ftest.com%2fsearch%3fname%3dfred+flinstone%26age%3d35")
   https://test.com/search?name=fred flinstone&age=35

   PS> [system.web.httputility]::htmlencode("https://test.com/search?name=fred flinstone&age=35")
   https://test.com/search?name=fred flinstone&amp;age=35   

   PS> [system.web.httputility]::htmldecode("https://test.com/search?name=fred flinstone&amp;age=35")
   https://test.com/search?name=fred flinstone&age=35
   
   PS> [uri]::escapedatastring("https://test.com/search?name=fred flinstone&age=35")
   https%3A%2F%2Ftest.com%2Fsearch%3Fname%3Dfred%20flinstone%26age%3D35

   PS> [uri]::unescapedatastring("https%3A%2F%2Ftest.com%2Fsearch%3Fname%3Dfred%20flinstone%26age%3D35")
   https://test.com/search?name=fred flinstone&age=35

   PS> [uri]::escapeuristring("https://test.com/search?name=fred flinstone&age=35")
   https://test.com/search?name=fred%20flinstone&age=35

 
More detailed examples:

* `Microsoft Docs: Get content from a web page <https://docs.microsoft.com/powershell/module/Microsoft.PowerShell.Utility/Invoke-WebRequest>`_
* `Microsoft Docs: Send an HTTP or HTTPS request to a RESTful web service <https://docs.microsoft.com/powershell/module/Microsoft.PowerShell.Utility/Invoke-RestMethod>`_
* `AdamTheAutomator: Invoke-WebRequest - PowerShell’s Web Swiss Army Knife <https://adamtheautomator.com/invoke-webrequest/>`_
* `Microsoft Docs: HttpUtility Class <hhttps://docs.microsoft.com/en-us/dotnet/api/system.web.httputility>`_

Active Directory
================

Generic examples are stolen from further reading reference.

:: 

   PS> Get-ADDomain                      # Basic Domain Information
   PS> Get-ADUser username -Properties * # Get User and List All Properties
   PS> Search-ADAccount -LockedOut       # Find All Locked User Accounts
   PS> Search-ADAccount -AccountDisabled # List all Disabled User Accounts
   
   PS> get-wmiobject win32_useraccount                   # List SID (Security Identifier)
   PS> get-wmiobject win32_useraccount | Select name,sid # List name, SID only
   
   PS> new-guid                          # 7bf86414-c4a6-4e05-aedd-e792f5df63d2
   PS> [guid]::NewGuid().ToString()      # 067ca88d-f94d-47a0-ac73-14f8f62b55e8 (full-syntax)
   

Further reading:

* `Microsoft Docs: ActiveDirectory Module <https://docs.microsoft.com/en-us/powershell/module/activedirectory>`_
* `AdamTheAutomator: Active Directory Scripts Galore: Come and Get It! <https://adamtheautomator.com/active-directory-scripts/>`_
* `Huge List Of PowerShell Commands for Active Directory, Office 365 and more <https://activedirectorypro.com/powershell-commands/>`_

Formatting Output
=================

By default Powershell appears to render *cmdlet* output, using ``format-table``.

Others such as ``format-list``, ``out-gridview`` are available as illustrated here.

::

   PS> Get-Service | Format-List | out-host -paging
   Name                : AarSvc_191cbe5f
   DisplayName         : Agent Activation Runtime_191cbe5f
   Status              : Running
   DependentServices   : {}
   ServicesDependedOn  : {}
   CanPauseAndContinue : False
   CanShutdown         : False
   CanStop             : True
   ServiceType         : 240
   
   Name                : ACCSvc
   DisplayName         : ACC Service
   Status              : Running
   DependentServices   : {}
   ServicesDependedOn  : {}
   CanPauseAndContinue : False
   CanShutdown         : True
   CanStop             : True
   ServiceType         : Win32OwnProcess

   PS> Get-Service | select -property Name,Status | Format-List 
   Name   : AarSvc_191cbe5f
   Status : Running
   
   Name   : ACCSvc
   Status : Running

   PS> Get-Service | Format-table | select -first 10 # this produces the same output
   PS> Get-Service | select -first 10                # this produces the same output
   Status   Name               DisplayName
   ------   ----               -----------
   Running  AarSvc_191cbe5f    Agent Activation Runtime_191cbe5f
   Running  ACCSvc             ACC Service
   Stopped  AJRouter           AllJoyn Router Service
   Stopped  ALG                Application Layer Gateway Service
   Stopped  AppIDSvc           Application Identity
   
   PS> Get-Service | where -Property Status -eq 'Running' | Format-List # All running services
   PS> Get-Service | where -Property Status -ne 'Running' | Format-List # All services not running

The *cmdlet* ``out-gridview`` produces a graphical table than can be ordered and filtered, as shown 
in the example which is shows only running services in alphabetic *DisplayName* order.

.. image:: ../images/running-services.png
    :width: 500px
    :align: center
    :height: 350px

The ``out-gridview`` in combination with ``import-csv`` *cmdlets* can quickly render CSV files, 
and avoids having to use ``Microsoft Excel`` or ``Microsoft Access``.

::

   PS> import-csv -Path file.csv -Delimeter "`t" | out-gridview # <TAB> separated file.
   PS> import-csv -Path file.csv -Delimeter ";" | out-gridview  # ';' separated file.
   PS> import-csv -Path file.csv -Delimeter "," | out-gridview  # ',' separated file.
   
   
.. image:: ../images/file-csv-gridview.png
    :width: 300px
    :align: center
    :height: 160px

Formatting Variables
====================

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


More detailed examples:

* `PowershellPrimer.com: Formatting Output <https://powershellprimer.com/html/0013.html>`_
* `Microsoft Docs: Get-Date <https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/get-date?view=powershell-6>`_


