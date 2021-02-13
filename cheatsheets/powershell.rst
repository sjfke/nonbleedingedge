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
   PS> get-process | sort -property workingset | select -last 10      # last 10 sorted
   PS> get-process | sort -property workingset | select -first 10     # first 10 sorted
   PS> get-process | sort -property ws -descending | select -first 10 # reversed first 10 (ws=workingset)
   PS> get-process | where {$_.processname -match "^p.*"}             # all processes starting with "p"
   PS> get-process | select -property Name,Id,WS | out-host -paging   # paged (more/less) output
   PS> get-process | out-gridview                                     # interactive static table view
   
   PS> start-process notepad                # start notepad
   PS> $p = get-process -name notepad       # finds all notepad processes!
   PS> stop-process -name notepad           # terminate all notepad processes!
   PS> stop-process -name notepad -whatif   # what would happen if run :-)
   PS> stop-process -id $p.id               # terminate by id, (confirmation prompt if not yours)
   PS> stop-process -id $p.id -force        # terminate by id, (no confirmation prompt if not yours)
   
   PS> $p = start-process notepad -passthru # start notepad, -passthru to return the process object
   PS> $p | get-member                      # methods and properties, (only 3 examples shown)
   PS> $p.cpu                               # how much CPU has notepad used
   PS> $p.Modules                           # which .dll's are being used
   PS> $p.kill()                            # terminate
   PS> stop-process -id $p.id               # terminate by id
   PS> remove-variable -name p              # $p is not $null after process termination
   

Viewing Files
=============
::

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


Computer Information
====================
::

   # Classnames: Win32_BIOS, Win32_Processor, Win32_ComputerSystem, Win32_LocalTime, 
   #             Win32_LogicalDisk, Win32_LogonSession, Win32_QuickFixEngineering, Win32_Service
   PS> get-cimclass | out-host -paging                      # lists all available classes

   PS> get-ciminstance -classname Win32_BIOS                # bios version
   PS> get-ciminstance -classname Win32_Processor           # processor information
   PS> get-ciminstance -classname Win32_ComputerSystem      # computer name, model etc.
   PS> get-ciminstance -classname Win32_QuickFixEngineering # hotfixes installed on which date
   PS> get-ciminstance -classname Win32_QuickFixEngineering -property HotFixID | select -property hotfixid
   
 * `Get-CimInstance <https://docs.microsoft.com/en-us/powershell/module/cimcmdlets/get-ciminstance>`_

Windows EventLog
================

::

   PS> get-eventlog -list                                                    # list a summary count of the events
   PS> get-eventlog -logname system -newest 5                                # last 5 system events
   PS> get-eventlog -logname system -entrytype error | out-host -paging      # system error events

   PS> get-eventlog -logname application | out-host -paging                  # lists application events (with index number)
   PS> get-eventlog -logname application -Index 14338 | select -Property *   # details of application event 14338

   PS> $events = get-eventlog -logname system -newest 1000                   # capture last 1000 system events
   PS> $events | group -property source -noelement | sort -property count -descending # categorize them
   
   PS> get-eventlog -logname application -source MSSQLSERVER | out-host -paging
   PS> get-eventlog -logname application -source MSSQLSERVER -after '11/18/2020' | out-host -paging
   
   # Gets events from event logs and event tracing log files (less useful)
   PS> (Get-WinEvent -ListLog Application).ProviderNames | out-host -paging  # who is writing Application logs
   
   PS> get-winevent -filterhashtable @{logname='application'} | get-member
   
   PS> get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | out-host -paging
   PS> get-winevent -filterhashtable @{logname='application'; providername='MSSQLSERVER'} | where {$_.Message -like '*error*'} | out-host -paging

* `Event Log Parsing <http://colleenmorrow.com/2012/09/20/parsing-windows-event-logs-with-powershell/>`_
* `Get-WinEvent <https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Diagnostics/Get-WinEvent>`_

HotFixes
========

::

   PS> get-hotfix                    # list all installed hot fixes and their ID
   PS> get-hotfix -Id KB4516115      # when was hotfix installed
   
   # To get hotfix details (example is a random choice, happens to be an Adobe Flash update)
   PS> start-process "https://www.catalog.update.microsoft.com/Search.aspx?q=KB4516115" 


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

   PS> import-csv -delimiter ';' file.csv | out-gridview


JSON files
==========

PowerShell requires that ``ConvertTo-Json`` and ``ConvertFrom-Json`` modules are installed.

::

   PS> get-content file2.json
   {
           "family":"flintstone",
           "members":
                   [
                           {"Name":"Fred", "Age":"30"},
                           {"Name":"Wilma", "Age":"25"},
                           {"Name":"Pebbles", "Age":"1"},
                           {"Name":"Dino", "Age":"5"}
                   ]
   }

   PS> get-content file2.json | ConvertFrom-Json
   family     members
   ------     -------
   flintstone {@{Name=Fred; Age=30}, @{Name=Wilma; Age=25}, @{Name=Pebbles; Age=1}, @{Name=Dino; Age=5}}


   PS> $obj = get-content file2.json | convertfrom-json
   PS> $obj
   family     members
   ------     -------
   flintstone {@{Name=Fred; Age=30}, @{Name=Wilma; Age=25}, @{Name=Pebbles; Age=1}, @{Name=Dino; Age=5}}
   
   PS> $obj.family                                      # returns flintstone
   PS> $obj.members[0].name                             # returns Fred
   PS> $obj.members[0].age                              # returns 30
   PS> $obj.members[0].age = 35                         # set Fred's age to 35
   PS> $obj.members[0].age                              # now returns 35
   PS> $obj | convertto-json | add-content newfile.json # save as JSON
   
   PS> $obj.members.name                                # returns: Fred Wilma Pebbles Dino
   PS> $obj.members.age                                 # returns: 35 25 1 5
   PS> $obj.members.age[0]                              # returns  35
   PS> $obj.members.age[0] = 37                         # immutable, silently fails, no error
   PS> $obj.members.age[0]                              # returns 35
   
   PS> remove-variable -name obj                        # cleanup
   
   PS> get-content newfile.json
   {
       "family":  "flintstone",
       "members":  [
                       {
                           "Name":  "Fred",
                           "Age":  35
                       },
                       {
                           "Name":  "Wilma",
                           "Age":  "25"
                       },
                       {
                           "Name":  "Pebbles",
                           "Age":  "1"
                       },
                       {
                           "Name":  "Dino",
                           "Age":  "5"
                       }
                   ]
   }
   
* `ConvertTo-Json converts an object to a JSON-formatted string. <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertto-json>`_
* `ConvertFrom-Json converts a JSON-formatted string to a custom object or a hash table. <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-json>`_
* `Introduction to JSON courtesy of W3Schools <https://www.w3schools.com/js/js_json_intro.asp>`_

Reading XML files
=================

``Powershell`` supports full manipulation of the XML DOM, read the `Introduction to XML <https://www.w3schools.com/XML/xml_whatis.asp>`_ 
and `.NET XmlDocument Class <https://docs.microsoft.com/en-us/dotnet/api/system.xml.xmldocument>`_ for more information. The examples shown 
are very redimentary, and only show a few of the manipulations you can perform on XML objects.

Note, the Common Language Infrastructure (CLI) cmdlets `Export-Clixml <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-clixml>`_ and 
`Import-Clixml <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-clixml>`_ provide a simplified way to save 
and reload your ``PowerShell`` objects and are ``Microsoft`` specific.

::

   PS> get-content .\file2.xml
   <?xml version="1.0" encoding="UTF-8"?>
   <family surname = "Flintstone">
           <member>
                   <name>Fred</name>
                   <age>30</age>
           </member>
           <member>
                   <name>Wilma</name>
                   <age>25</age>
           </member>
           <member>
                   <name>Pebbles</name>
                   <age>1</age>
           </member>
           <member>
                   <name>Dino</name>
                   <age>5</age>
           </member>
   </family>
   
   PS> $obj = [XML] (get-content .\file2.xml) # returns a System.Xml.XmlDocument object
   
   PS> $obj.childnodes                        # returns all the child nodes
   PS> $obj.xml                               # returns version="1.0" encoding="UTF-8"
   PS> $obj.childnodes.surname                # Flintstone
   PS> $obj.childnodes.member.name            # returns Fred Wilma Pebbles Dino
   PS> $obj.childnodes.member.age             # returns 30 25 1 5
   
   PS> $obj.ChildNodes[0].NextSibling
   surname    member
   -------    ------
   Flintstone {Fred, Wilma, Pebbles, Dino}

   PS> $obj.GetElementsByTagName("member");
   name    age
   ----    ---
   Fred    30
   Wilma   25
   Pebbles 1
   Dino    5

   PS> $obj.GetElementsByTagName("member")[0].name       # returns Fred
   PS> $obj.GetElementsByTagName("member")[0].age        # returns 30
   PS> $obj.GetElementsByTagName("member")[0].age = 35   # Errors, only strings can be used.
   PS> $obj.GetElementsByTagName("member")[0].age = "35" # Fred is now older
   PS> $obj.GetElementsByTagName("member")[0].age        # returns 35
   PS> $obj.Save("$PWD\newfile.xml")                     # needs a full pathname

   PS> get-content newfile.xml
   <?xml version="1.0" encoding="UTF-8"?>
   <family surname="Flintstone">
     <member>
       <name>Fred</name>
       <age>35</age>
     </member>
     <member>
       <name>Wilma</name>
       <age>25</age>
     </member>
     <member>
       <name>Pebbles</name>
       <age>1</age>
     </member>
     <member>
       <name>Dino</name>
       <age>5</age>
     </member>
   </family>


Writing XML files
=================

To generate an XML file, use the `XmlTextWriter Class <https://docs.microsoft.com/en-us/dotnet/api/system.xml.xmltextwriter>`_

Note, the Common Language Infrastructure (CLI) cmdlets `Export-Clixml <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-clixml>`_ and 
`Import-Clixml <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-clixml>`_ provide a simplified way to save 
and reload your ``PowerShell`` objects.

::

   $settings = New-Object System.Xml.XmlWriterSettings  # to update XmlWriterSettings
   $settings.Indent = $true                             # indented XML
   $settings.IndentChars = "`t"                         # <TAB> indents
   $settings.Encoding = [System.Text.Encoding]::UTF8    # force the default UTF8 encoding; others ASCII, Unicode...
   
   $obj = [System.XML.XmlWriter]::Create("C:\users\geoff\bedrock.xml", $settings) # note full-pathname
   
   # Simpler approach but no encoding is specified in XML header and again note full-pathname
   # $obj = New-Object System.XMl.XmlTextWriter('C:\users\geoff\bedrock.xml', $null)
   # $obj.Formatting = 'Indented'
   # $obj.Indentation = 1
   # $obj.IndentChar = "`t"
   
   $obj.WriteStartDocument()                          # start xml document, <?xml version="1.0"?>
   $obj.WriteComment('Bedrock Families')              # add a comment, <!-- Bedrock Families -->
   $obj.WriteStartElement('family')                   # start element <family>
   $obj.WriteAttributeString('surname', 'Flintstone') # add surname attribute
   
   $obj.WriteStartElement('member')                   # start element <member>
   $obj.WriteElementString('name','Fred')             # add <name>Fred</name>
   $obj.WriteElementString('age','30')                # add <age>30</age>
   $obj.WriteEndElement()                             # end element </member>
   
   $obj.WriteStartElement('member')                   # start element <member>
   $obj.WriteElementString('name','Wilma')            # add <name>Wilma</name>
   $obj.WriteElementString('age','25')                # add <age>25</age>
   $obj.WriteEndElement()                             # end element </member>
   
   $obj.WriteStartElement('member')                   # start element <member>
   $obj.WriteElementString('name','Pebbles')          # add <name>Pebbles</name>
   $obj.WriteElementString('age','1')                 # add <age>1</age>
   $obj.WriteEndElement()                             # end element </member>
   
   $obj.WriteStartElement('member')                   # start element <member>
   $obj.WriteElementString('name','Dino')             # add <name>Dino</name>
   $obj.WriteElementString('age','5')                 # add <age>5</age>
   $obj.WriteEndElement()                             # end element </member>
   
   $obj.WriteEndElement()                             # end element <family>
   
   $obj.WriteEndDocument()                            # end document
   $obj.Flush()                                       # flush
   $obj.Close()                                       # close, writes the file
   
   PS> get-content C:\users\geoff\bedrock.xml
   <?xml version="1.0" encoding="utf-8"?>
   <!--Bedrock Families-->
   <family surname="Flintstone">
           <member>
                   <name>Fred</name>
                   <age>30</age>
           </member>
           <member>
                   <name>Wilma</name>
                   <age>25</age>
           </member>
           <member>
                   <name>Pebbles</name>
                   <age>1</age>
           </member>
           <member>
                   <name>Dino</name>
                   <age>5</age>
           </member>
   </family>
   
   PS> remove-variable -name settings
   PS> remove-variable -name obj
   PS> remove-item C:\users\geoff\bedrock.xml

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


More detailed examples:

* `PowershellPrimer.com: Formatting Output <https://powershellprimer.com/html/0013.html>`_
* `Microsoft documentation: Get-Date <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-date?view=powershell-6>`_
