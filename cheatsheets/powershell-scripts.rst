:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/powershell-scripts.rst

*******************************
PowerShell Scripting Cheatsheet
*******************************

This is the companion to ``PowerShell Cheatsheet``, which focuses on writing scripts using PowerShell

``PowerShell`` is a cross-platform task automation and configuration management framework, consisting of a 
command-line shell and scripting language. It is built on top of the ``.NET Common Language Runtime`` (CLR), accepts and 
returns ``.NET objects``. This brings entirely new tools and methods for automation, and news levels of frustration and confusion. :-)

Unlike traditional command-line interfaces, PowerShell cmdlets are designed to deal with objects. An object is 
structured information that is more than just the string of characters appearing on the screen, it carries extra information 
that you can use if you need it.


Introduction
============

``PowerShell`` is very powerful scripting language and is often abused by **would-be** hackers, so by default laptop versions 
of Windows will not execute ``PowerShell scripts`` although individual ``cmdlets`` can be executed, but Windows servers will 
usually allow ``RemoteSigned`` scripts to be run.

Whether a ``PowerShell`` script can be executed is governed by the execution policy, ``get-executionpolicy`` displays this for 
the current ``PowerShell``, add the ``-List`` parameter and it shows all the policies in highest to lowest priority (scope) order. 

In the example only the ``LocalMachine`` policy is defined, and is set to ``restricted`` so PowerShell scripts cannot be run. 

:: 

   PS> Get-ExecutionPolicy -List
   
           Scope ExecutionPolicy
           ----- ---------------
   MachinePolicy       Undefined  # highest priority
      UserPolicy       Undefined
         Process       Undefined
     CurrentUser       Undefined
    LocalMachine      Restricted  # lowest priority
    
   PS> Get-ExecutionPolicy
   Restricted

See: `About Execution Policies <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies>`_ for more details.

PowerShell's execution policies:

* ``Restricted`` does not permit any scripts to run (*.ps1xml, .psm1, .ps1*);
* ``AllSigned``, prevents running scripts that do not have a digital signature;
* ``RemoteSigned`` prevents running downloaded scripts that do not have a digital signature;
* ``Unrestricted`` runs scripts without a digital signature, warning about non-local intranet zone scripts;
* ``Bypass`` allows running of scripts without any digital signature, and without any warnings;
* ``Undefined`` no execution policy is defined;

PowerShell's execution policy scope:

* ``MachinePolicy`` set by a Group Policy for all users of the computer;
* ``UserPolicy`` set by a Group Policy for the current user of the computer;
* ``Process`` current PowerShell session, environment variable ``$env:PSExecutionPolicyPreference``;
* ``CurrentUser`` affects only the current user, ``HKEY_CURRENT_USER`` registry subkey;
* ``LocalMachine`` all users on the current computer, ``HKEY_LOCAL_MACHINE`` registry subkey;

By default on a Windows Server the execution policy is, ``LocalMachine RemoteSigned``, but for your Windows Laptop or Desktop it will be ``LocalMachine Restricted``.
To change the execution policy, you must start a PowerShell as Administrator and use ``Set-ExecutionPolicy`` as shown, you will be prompted to confirm this action.

In a commercial or industrial environment ask your Windows Adminstrator, but company policy may be *AllSigned*.

::

   # Stops running of downloaded scripts
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned # sets: LocalMachine RemoteSigned
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Restricted   # sets: LocalMachine Restricted
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Undefined    # sets: LocalMachine Undefined
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # just me
   
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy AllSigned    # mandate code-signing   
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Default      # restore: LocalMachine defaults
   
   
How to sign scripts for your own use.
=====================================

To add a digital signature to a script you must sign it with a code signing certificate:

* Purchased from a certification authority, which allows executing your script on other computers;
* A free self-signed certificate which will only work on your computer;

Typically, a *self-signed certificate* is only used to sign your own scripts and to sign scripts that you get 
from other sources that you have verified to be safe, and should be used in an industrial or commercial enviroment.


Microsoft's official guide:

* `About Signing <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_signing>`_
* `How to Create a Self-Signed Certificate with PowerShell <https://www.cloudsavvyit.com/3274/how-to-create-a-self-signed-certificate-with-powershell/>`_
* `Add an Authenticode signature to a PowerShell script or other file. <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-authenticodesignature>`_
* `New-SelfSignedCertificate <https://docs.microsoft.com/en-us/powershell/module/pkiclient/new-selfsignedcertificate>`_
* `Generating self-signed certificates on Windows <https://medium.com/the-new-control-plane/generating-self-signed-certificates-on-windows-7812a600c2d8>`_
* `Generate and export certificates for Point-to-Site using PowerShell <https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-certificates-point-to-site>`_

How to get around signed scripts
================================

Some proposals to avoid signing PowerShell scripts.

* `Provide A Batch File To Run Your PowerShell Script From <https://blog.danskingdom.com/allow-others-to-run-your-powershell-scripts-from-a-batch-file-they-will-love-you-for-it/>`_
* `Set Up Powershell Script For Automatic Execution <https://stackoverflow.com/questions/29645/set-up-powershell-script-for-automatic-execution/8597794#8597794>`_

Some internet posts recommend disabling the execution policy, but I would advise against.

::

   ### DO NOT DO THE FOLLOWING, UNLESS YOU KNOW WHAT YOU ARE DOING  ###
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Unrestricted


PowerShell Language
===================

The language makes use of `.Net Framework <https://en.wikipedia.org/wiki/.NET_Framework>`_ and is based on is built on 
top of the `.NET Common Language Runtime (CLR) <https://docs.microsoft.com/en-us/dotnet/standard/clr>`_ , and 
manipulates `.NET objects <https://docs.microsoft.com/en-us/dotnet/api/system.object>`_.


Like other object oriented languages, ``PowerShell`` has features such *inheritance*, *subclasses*, *getters*, *setters*, *modules* etc.
Function support both ``named`` and ``positional`` arguments are supported, and allows them to be mixed, which can be confusing, so in 
most cases it is clearer to use `splatting <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting>`_ rather than individual name or positional parameters.

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
 
   PS> set-variable -name age 5         # same as PS>age = 5
   PS> set-variable -name name Dino     # same as PS>name = "Dino"
 
   PS> clear-variable -name age         # clear $age; $name = $null
   PS> clear-variable -name name        # clear $name; $name = $null
   
   PS> remove-variable -name age        # delete variable $age
   PS> remove-item -path variable:\name # delete variable $name
   
   PS> set-variable -name pi -option Constant 3.14159 # constant variable
   PS> $pi = 42                                       # Fails $pi is a constant


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
   PS> $h.add($key, $value)  # add key:value to the hash-table
   
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


Cruft that needs to be cleaned up
=================================

The command-line has colour-highlighting and ``TAB`` completion for commands and arguments. Try ``import <tab>``, and cycle 
through the alternatives. Cmdlets are **case-insensitive** but hyphens are important, I try to avoid Camel-Case and try use a consistent 
lower-case format ``get-help`` and not ``Get-Help``. Variable names are also **case-insensitive** but I often use CamelCase 
to make them more readable ``dateString`` , rather than underscore ``date_string``.

A `Windows Powershell ISE <https://docs.microsoft.com/en-us/powershell/scripting/components/ise/introducing-the-windows-powershell-ise?view=powershell-7>`_  
is provided if you need more interactive assistance, which is also useful for checking your scripts are consistent with Mircosoft's conventions.

There have been many `Powershell versions <https://en.wikipedia.org/wiki/PowerShell>`_ which are mainly backwards compatible, 
be careful if writing for older Windows releases, writing scripts with ``#Requires -version X`` as the very first line is a good habit.
 

Commonly used cmdlets when starting are ``get-help`` and ``get-member``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	PS> get-help get-childitem         # Help on GetChildItem
	PS> get-help get-childiten -online # Online Web based documentation from Microsoft
	PS> get-childitem | get-member     # What is object type, its methods and properties
	PS> get-help get-content           # notice its aliases 'gc', 'cat', 'type'
	PS> get-help select-string         # regular expressions based string searching (grep like)


	PS> get-help get-location          # alias 'gl' and 'pwd'.
	PS> get-help get-command           # what commands are available
	PS> get-help select-object         # 'select' or set object properties
	PS> get-help where-object          # 'where' filter on object property
	PS> get-help tee-object            # 'tee' like the UNIX command
	PS> get-help out-host              # Similar to UNIX 'more' and 'less'

There are many online guides and tutorials, which usually means the subject matter is complex or misunderstood, the ones I found most useful.

* `Learning PowerShell <https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell>`_
* `PowerShell 3.0 <https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-3.0>`_
* `TutorialsPoint PowerShell <https://www.tutorialspoint.com/powershell/index.htm>`_
* `PowerShell Tutorial <http://powershelltutorial.net/>`_

Running PowerShell scripts
==========================

PowerShell is an often abused hackers attack vector, so modern versions of Windows prevent PowerShell scripts from
being executed *out-of-the-box*, although the command line will work. 

Many articles suggest the disabling this security feature... **DO NOT DO THIS** 

Furthermore most companies harden their Windows laptop and server installations, so disabling may not work anyway.

Ways to work with this restriction, are not intuitive... it took me some time to figure it out, and I am 
still be no means an expert, hopefully this will get you started, and you can inform me once you have mastered ``PowerShell``.

The execution-policy, controls this and you should probably look at the following:

* `Allow other to run your PowerShell scripts... <https://blog.danskingdom.com/allow-others-to-run-your-powershell-scripts-from-a-batch-file-they-will-love-you-for-it/>`_
* `Setup Powershell scripts for automatic execution <https://stackoverflow.com/questions/29645/set-up-powershell-script-for-automatic-execution/8597794#8597794>`_
* `Get-ExecutionPolicy <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-executionpolicy?view=powershell-7>`_

If you start ``PowerShell`` as administrator, then some of these settings can be changed. 
The execution policy to change is 'CurrentUser', *your* rights, see Get-ExecutionPolicy link.
A default install will most likely look as shown.

::

	PS> Get-ExecutionPolicy -list
	MachinePolicy    Undefined
	   UserPolicy    Undefined
	      Process    Undefined
	  CurrentUser    Restricted
	 LocalMachine    Restricted
	 
	# Permit yourself to run PowerShell scripts
	PS> Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser    # Must be Signed
	PS> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # Must be RemotelySigned
	PS> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser # Disable

Choosing **Unrestricted** means that any PowerShell script, even ones inadvertently or unknowingly 
downloaded from the Internet will run as you, and with your privileges, so **be careful**

When developing the following avoids having certificates installed and updating the signature each time.
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

  PS> powershell.exe -noprofile -executionpolicy bypass -file .\script.ps1 
  
Generating and Installing Certificates
======================================

To come shortly. 

Variables
---------
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
