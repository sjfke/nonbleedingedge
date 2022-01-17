:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/powershell-scripts.rst

*******************************
PowerShell Scripting Cheatsheet
*******************************

This is the companion to ``PowerShell Cheatsheet``, which focuses on writing PowerShell scripts.

.. topic:: According to Microsoft ``PowerShell``

   Is a cross-platform task automation and configuration management framework, consisting of a *command-line shell* and 
   *scripting language* that is built on top of the ``.NET Common Language Runtime`` (CLR), accepts and returns ``.NET objects``.
   This brings entirely new tools and methods for automation.
      
This means learning new skills and thinking differently which can be frustrating while learning. 

To simplify maintenance I write PowerShell scripts as standalone utilities deployed in a single file, this means I have to *copy-and-paste* 
my favourite frequently used functions, such as *dumpArrayList*, *dumpHashTable* because there is no mechanism to textually include 
your favourite functions into the source when writing and testing. 

It is possible to split your script into multiple files, create libraries of your favoutite utilities etc. 
I do not cover this topic, the example script shows where/how to ``source`` you library files, and if you wish to create your 
own modules, see `How to Write a PowerShell Script Module <https://docs.microsoft.com/en-us/powershell/scripting/developer/module/how-to-write-a-powershell-script-module>`_.

Introduction
============

Unfortunately because ``PowerShell`` is very powerful scripting language, often used to automate routine tasks, makes it an ideal
target for **would-be** hackers. To mitigate this Microsoft limits if/when PowerShell scripts can be executed, although 
individual ``cmdlets`` can always be executed. 

* *Windows Pro/Home* usually disallows ``PowerShell scripts`` but permits ``cmdlets`` to be executed;
* *Windows Server* usually allows ``RemoteSigned`` scripts to be run on the ``LocalMachine``;

The execution policy governs whether a ``PowerShell`` script can be executed, ``get-executionpolicy`` displays this for 
the current ``PowerShell``, and ``get-executionpolicy -list`` shows all the policies in highest to lowest priority (*scope*) order. 

In the example below only the ``LocalMachine`` policy is defined, and this is set to ``restricted`` so ``PowerShell`` scripts cannot be executed, but 
indiviual commands, ``cmdlets`` can.

:: 

   PS> Get-ExecutionPolicy
   Restricted

   PS> Get-ExecutionPolicy -List
   
           Scope ExecutionPolicy
           ----- ---------------
   MachinePolicy       Undefined  # highest priority
      UserPolicy       Undefined
         Process       Undefined
     CurrentUser       Undefined
    LocalMachine      Restricted  # lowest priority


If your *ExecutionPolicy* is as above, a quick fix is to start a *PowerShell as Administrator* and set it to *RemoteSigned* as shown, but you 
should still read the `PowerShell Exection Policies`_ section.

::

   # Set *ONE* of: 'LocalMachine RemoteSigned' or 'CurrentUser RemoteSigned' not both
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   PS C:\WINDOWS\system32> Get-ExecutionPolicy -List
   
           Scope ExecutionPolicy
           ----- ---------------
   MachinePolicy       Undefined  # highest priority
      UserPolicy       Undefined
         Process       Undefined
     CurrentUser       Undefined
    LocalMachine    RemoteSigned  # lowest priority
 

Language
========

The language makes use of `.Net Framework <https://en.wikipedia.org/wiki/.NET_Framework>`_ and is built on 
top of the `.NET Common Language Runtime (CLR) <https://docs.microsoft.com/en-us/dotnet/standard/clr>`_ , and 
manipulates `.NET objects <https://docs.microsoft.com/en-us/dotnet/api/system.object>`_. If the language itself 
does not provide what you need, there may be a `Popular PowerShell Module <https://social.technet.microsoft.com/wiki/contents/articles/4308.popular-powershell-modules.aspx>`_
you can download or you can access the `.Net APIs <https://docs.microsoft.com/en-us/dotnet/api>`_ directly, a good example being `ArrayLists <https://docs.microsoft.com/en-us/dotnet/api/system.collections.arraylist>`_ which 
are dynamic in size unlike a *PowerShell Array*.


In common with other object oriented languages, ``PowerShell`` has features such *inheritance*, *subclasses*, *getters*, *setters*, *modules* etc.
Functions support both ``named`` and ``positional`` arguments, which can be mixed, this can be confusing, so in 
most cases it is clearer to use `splatting <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting>`_ rather 
than individual name or positional parameters.

Useful starting points when learning about the language:

* `PowerShell GitHub - Recommended Training and Reading <https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell#recommended-training-and-reading>`_
* `PowerShell GitHub - Learning Powershell <https://github.com/PowerShell/PowerShell/tree/master/docs/learning-powershell>`_
* `Windows PowerShell Portal <https://social.technet.microsoft.com/wiki/contents/articles/24187.windows-powershell-portal.aspx>`_

Unlike most texts on programming languages this starts with a simple but realistic PowerShell example, with many of the language details being covered in subsequent sections.

Example Script
==============

This is a contrived but realistic PowerShell script to illustrate several important points.
It is based on a `gist template from 9to5IT <https://gist.github.com/9to5IT/9620683>`_, which is extremely useful, but is augmented to force 
the syntax version and to be more strict on the use of uninitialized variables.

::

   #requires -version 4
   <#
   .SYNOPSIS
   
      9to5IT Template for PowerShell scripts.
      
   .DESCRIPTION
   
      Displays the names and ages of the flintstones.
      
   .PARAMETER names
   
      List the names only
   
   .PARAMETER ages
   
      List the ages only
   
   .PARAMETER person <name>
   
      List person's age
   
   .INPUTS
   
      None
   
   .OUTPUTS
   
      The Requested text.
   
   .NOTES
   
      Version:        1.0
   
      Author:         sjfke
   
      Creation Date:  2021.01.03
   
      Purpose/Change: Initial script development  
   
   .EXAMPLE
   
      families.ps1 -names
   
   .EXAMPLE
   
      families.ps1 -person fred
      
   #>
   param(
      [switch]$names = $false,
      [switch]$ages = $false,
      [string]$person = $null,
      [switch]$stackTrace = $false
   )
   Set-StrictMode -Version 2
   
   #---------------------------------------------------------[Initialisations]--------------------------------------------------------
   
   # Set Error Action to Silently Continue
   # $ErrorActionPreference = "SilentlyContinue"
   
   # Dot Source required Function Libraries
   # . "C:\Scripts\Functions\Logging_Functions.ps1"
   
   #----------------------------------------------------------[Declarations]----------------------------------------------------------
   $scriptName = "flintstones.ps1"
   $scriptVersion = "1.0"
   
   #Log File Info
   # $sLogPath = "C:\Windows\Temp"
   # $sLogName = "<script_name>.log"
   # $sLogFile = Join-Path -Path $sLogPath -ChildPath $sLogName
   
   $hash = $null
   
   #-----------------------------------------------------------[Functions]------------------------------------------------------------
   
   function initializeHash {
      return @{ Fred = 30; Wilma = 25; Pebbles = 1; Dino = 5 }
   }
   
   function getNames {
      return $hash.keys
   }
   
   function getAges {
      return $hash.values
   }
   
   function getPerson {
      param(
         [string]$name = ''
      )
      return $hash[$name]
   }
   
   #-----------------------------------------------------------[Execution]------------------------------------------------------------
   $hash = initializeHash
   
   if ($names) {
      getNames
   }
   elseif ($ages) {
      getAges
   }
   elseif (($person -ne '') -and ($person -ne $null)) {
      $arguments = @{
         name = $person
      }
      getPerson @arguments
   }
   else {
      if ($stackTrace) {
         write-error("invalid or missing argument") # stack-trace like error message
      }
      else {
         write-warning("{0} v{1}: invalid or missing argument" -f $scriptName, $scriptVersion)
         exit(1)     
      }
   }

Things to note:

* The `#requires -version 4 <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_requires>`_ PowerShell version 4 syntax, (use *version 2*, if windows is very old);
* Initial comment block ``.SYNOPSIS...`` provides the ``get-help`` text, **note** line-spacing is important;
* The `param() <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters>`_ block must be the first *non-comment line* for command-line arguments;
* The `Set-StrictMode -Version 2 <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/set-strictmode>`_ checks the usage of uninitialized variables;

Variables
=========

Powershell variables can be any of the `Basic DataTypes`_ such as *integers*, *characters*, *strings*, *arrays*, and *hash-tables*, but also ``.Net`` objects that represent such things as
*processes*, *services*, *event-logs*, and even *computers*.

::

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

   PS> set-variable -name age 5         # same as $age = 5
   PS> set-variable -name name Dino     # same as $name = "Dino" (variable's name is *name*)
 
   PS> clear-variable -name age         # clear $age; $age = $null
   PS> clear-variable -name name        # clear $name; $name = $null
   
   PS> remove-variable -name age        # delete variable $age
   PS> remove-item -path variable:\name # delete variable $name
   
   PS> set-variable -name pi -option Constant 3.14159 # constant variable
   PS> $pi = 42                                       # Fails $pi is a constant


Basic DataTypes
===============

+-----------+------------------------------------------------------------------------------+
| Data Type | Definition                                                                   |
+===========+==============================================================================+
| Boolean   | True or False Condition                                                      |
+-----------+------------------------------------------------------------------------------+
| Byte      | An 8-bit unsigned whole number from 0 to 255                                 |
+-----------+------------------------------------------------------------------------------+
| Char      | A 16-bit unsigned whole number from 0 to 65,535                              |
+-----------+------------------------------------------------------------------------------+
| Date      | A calendar date                                                              |
+-----------+------------------------------------------------------------------------------+
| Decimal   | A 128-bit decimal value, such as 3.14159                                     |
+-----------+------------------------------------------------------------------------------+
| Double    | A double-precision 64-bit floating point number, narrower range than Decimal |
+-----------+------------------------------------------------------------------------------+
| Integer   | A 32-bit signed whole number from -2,147,483,648 to 2,147,483,647            |
+-----------+------------------------------------------------------------------------------+
| Long      | A 64-bit signed whole number, very big integer, 9,233,372,036,854,775,807    |
+-----------+------------------------------------------------------------------------------+
| Object    |                                                                              |
+-----------+------------------------------------------------------------------------------+
| Short     | A 16-bit unsigned whole number, -32,768 to 32,767                            |
+-----------+------------------------------------------------------------------------------+
| Single    | A single-precision 32-bit floating point number                              |
+-----------+------------------------------------------------------------------------------+
| String    | Text, a character string                                                     |
+-----------+------------------------------------------------------------------------------+


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
   PS> $a[3] = 'dino'    # Error: Index was outside the bounds of the array.
   PS> $a += 'dino'      # correct way to add 'dino' (note does an array copy)
   PS> $a[1,3,2]         # wilma, dino, pebbles
   PS> $a[1..3]          # wilma, pebbles, dino
   PS> $a = $a[0..2]     # dino ran away (note does an array copy)
   
   
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
   
 
Useful references:

* `TutorialsPoint Powershell Array for more detailed explanation <https://www.tutorialspoint.com/powershell/powershell_array.htm>`_
* `PowerShellExplained ArrayList for dynamically resizable arrays <https://powershellexplained.com/2018-10-15-Powershell-arrays-Everything-you-wanted-to-know/>`_
* `Microsoft Docs ArrayList Class for dynamically resizable arrays <https://docs.microsoft.com/en-us/dotnet/api/system.collections.arraylist>`_
* `Kevin Blumenfeld's GitHub Gist Collection Type Guidence <https://gist.github.com/kevinblumenfeld/4a698dbc90272a336ed9367b11d91f1c>`_


HashTables
==========

A HashTable is an unordered collection of key:value pairs, synonymous with an object and its properties. 
Later versions support known/fixed order hash elements, ``$hash = [ordered]@{}``.

::

   PS> $h = @{}              # empty hash
   PS> $key = 'Fred'         # set key name
   PS> $value = 30           # set key value
   PS> $h.add($key, $value)  # add key:value ('fred':30) to the hash-table
   
   PS> $h.add('Wilma', 25 )  # add 'Wilma':25
   PS> $h['Pebbles'] = 1     # add 'Pebbles':1
   PS> $h.Dino = 5           # add 'Dino':5
   
   PS> $h                    # actual hash-table, printed if on command-line
   PS> $h['Fred']            # how old is Fred? 30
   PS> $h[$key]              # how old is Fred? 30
   PS> $h.fred               # how old is Fred? 30
   
   # creating a populated hash, multi-line.
   PS> $h = @{
       Fred = 30
       Wilma  = 25
       Pebbles = 1
       Dino = 5
   }
   
   # creating the same populated hash, on single-line
   PS> $h = @{ Fred = 30; Wilma = 25; Pebbles = 1; Dino = 5 }
   
   PS> $h.keys            # unordered: Dino, Pebbles, Fred, Wilma
   PS> $h.values          # unordered: 5, 1, 30, 25 (but same as $h.keys order)
   
   # later PowerShell versions allow the order to be fixed.
   PS> $h = [ordered]@{ Fred = 30; Wilma = 25; Pebbles = 1; Dino = 5 }
   PS> $h.keys            # ordered: Fred, Wilma, Pebbles, Dino
   PS> $h.values          # ordered: 30, 25, 1, 5 
   
   # key order is random, unless [ordered] was used in the declaration
   PS> foreach ($key in $h.keys) {
       write-output ('{0} Flintstone is {1:D} years old' -f $key, $h[$key])
   }
   
   # ascending alphabetic order (Dino, Fred, Pebbles, Wilma)
   PS> foreach ($key in $h.keys | sort) {
       write-output ('{0} Flintstone is {1:D} years old' -f $key, $h[$key])
   }
   
   # descending alphabetic order (Wilma, Pebbles, Fred, Dino)
   PS> foreach ($key in $h.keys | sort -descending) {
       write-output ('{0} Flintstone is {1:D} years old' -f $key, $h[$key])
   }
   
   # specfific order (Fred, Wilma, Pebbles, Dino)
   PS> $keys = ('fred', 'wilma', 'pebbles', 'dino')
   for ($i = 0; $i -lt $keys.length; $i++) {
      write-output ('{0} Flintstone is {1:D} years old' -f $keys[$i], $h[$keys[$i]])
   }
   
   PS> if ($h.ContainsKey('fred')) { ... }   # true 
   PS> if ($h.ContainsKey('barney')) { ... } # false
   PS> if ($h.fred) { ... }                  # avoid, works most of the time.
   PS> if ($h['barney']) { ... }             # avoid, works most of the time.
   
   PS> $h.remove('Dino')                # remove Dino, because he ran away :-)
   PS> $h.clear()                       # flintstone family deceased

For more details read the excellent review by Kevin Marquette:
 
* `Powershell: Everything you wanted to know about hashtables <https://powershellexplained.com/2016-11-06-powershell-hashtable-everything-you-wanted-to-know-about/>`_

Objects
=======

If you cannot create what you need from *Arrays, HashTables, ArrayLists, Queues, Stacks etc.*, then 
it is possible to create custom PowerShell objects, but to date I have never needed to do this.
For more details, read:

* `David Bluemenfeld: Collection Type Guidence <https://gist.github.com/kevinblumenfeld/4a698dbc90272a336ed9367b11d91f1c>`_;
* `Microsoft TechNet: Creating Custom Objects <https://social.technet.microsoft.com/wiki/contents/articles/7804.powershell-creating-custom-objects.aspx>`_;
* `Kevin Marquette: Everything you wanted to know about PSCustomObject <https://powershellexplained.com/2016-10-28-powershell-everything-you-wanted-to-know-about-pscustomobject/>`_;

Functions
=========

Function arguments and responses are passed by reference, so an arugment can be changed inside the function and remains 
unchanged outside the function, **but** this is considered *"bad programming practice"*, so better to avoid doing this. 
Functions return references to objects, as illustrated in the `Example Script`_ where references to *HashTable* and *Array* objects are returned.

While each function call returns a reference to a new (*different*) object, be careful about the scope of the variable you assign this reference too, 
it is easy to create multiple references to the same object.

While mixing named (*order indepedent*) and positional (*order dependent*) arguments is permitted it can cause strange errors, so unless you are only 
supplying one or two arguments, a better approach is to use `splatting <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting>`_.
The following contrived example illustrates the basics but the ``param ( ... )`` section has many options not shown here. 

::
  
   #requires -version 4
   Set-StrictMode -Version 2
   
   function createPerson {
      param (
         [string]$name = '',
         [int]$age = 0,
         [switch]$verbose = $false,
         [switch]$debug = $false
      )
      
      if (($name -eq $null) -or ($name.length -eq 0)) {
         if ($verbose) {
            write-warning("createPerson - name is missing")
            return $null
         }
         elseif ($debug) {
            write-error("createPerson - name is missing")
            exit(1)
         }
         else {
            return $null
         }
      }
      
      if (($age -le 0) -or ($age -gt 130)) {
         if ($verbose) {
         write-warning("createPerson - age, {0:D}, is incorrect" -f $age)
            return $null
         }
         elseif ($debug) {
            write-error("createPerson - age, {0:D}, is incorrect" -f $age)
            exit(1)
         }
         else {
            return $null
         }
      }
      
      $hash = @{}
      $hash[$name] = $age 
      
      return $hash
   
   }
   
   createPerson 'fred' 30 -verbose            # positional arguments
   createPerson 30 'fred' -verbose            # positional arguments, breaks name=30
   createPerson -name 'fred' -age 30 -verbose # named arguments
   createPerson -age 30 'fred' -verbose       # mixed arguments, be careful, no-named taken param order
   
   $arguments = @{                            # splatting
      name = 'fred'
      age = 30
      verbose = $true
   }
   createPerson @arguments
   
   $arguments = @{name = 'wilma'; age = 25; verbose = $true} # splatting one-line
   createPerson @arguments
   
   $arguments = @{
      name = 'fred'
      verbose = $true
      debug = $false
   }
   createPerson @arguments                   # fails, age default is 0
   
   $arguments = @{
      age = 21
      verbose = $true
      debug = $false
   }
   createPerson @arguments                   # fails, name default is an empty string

Further reading:

* Microsoft Docs, `Chapter 9 - Functions <https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/09-functions>`_ 
* Microsoft Docs, `About Functions Advanced Parameters <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters>`_.

ArrayList
=========

::

   PS> $names = New-Object -TypeName System.Collections.ArrayList
   PS> $names = [System.Collections.ArrayList]::new()
   PS> $names.gettype()              # ArrayList
   
   PS> $index = $names.Add('fred')   # returns array-list index: i.e. 0
   PS> [void]$names.Add('wilma')     # discard array-list index
   PS> [void]$names.Add('pebbles')
   PS> [void]$names.Add('dino')
   
   # one-line creation, empty or populated
   PS> [System.Collections.ArrayList]$names = @()
   PS> [System.Collections.ArrayList]$names = @('fred','wilma','pebbles', 'dino')
   
   PS> $names.Count                  # returns 4
   PS> $names[1]                     # wilma
   PS> $names.remove(3)              # dino ran away or did he?
   PS> $names.Count                  # 4, no dino is still there
   PS> $names.[3]                    # dino
   PS> $names.RemoveAt(3)            # dino, has really gone this time
   PS> [void]$names.Add('dino')      # dino found 
   PS> $names.Remove('dino')         # dino, escaped again
   PS> [void]$names.Add('dino')      # dino found ... again
  
   PS> 'fred' -in $names             # True  (not supported in PowerShell 2)
   PS> 'barney' -in $names           # False (not supported in PowerShell 2)
   PS> $names -contains 'fred'       # True
   PS> $names -contains 'barney'     # False
    
   PS> [void]$names.Insert(3,'fido')
   PS> $names                        # 0:fred, 1:wilma, 2:pebbles, 3:fido, 4:dino
   PS> $names.remove('fido')
   PS> $names                        # 0:fred, 1:wilma, 2:pebbles, 3:dino
   
   # Generic List are ArrayList's of a fixed type
   PS> [System.Collections.Generic.List[string]]$names = @()
   PS> [System.Collections.Generic.List[string]]$names = @('fred','wilma','pebbles', 'dino')
   
   PS> [System.Collections.Generic.List[int]]$ages = @()
   PS> [System.Collections.Generic.List[int]]$ages = (30, 25, 1, 5)
   
   $names.add(30)                    # 0:fred, 1:wilma, 2:pebbles, 3:dino, 4:30
   $ages.add('fred')                 # fails, throws conversion exception

Further reading:

* `The .Net ArrayList Class <https://docs.microsoft.com/en-us/dotnet/api/system.collections.arraylist>`_
* `Powershell: Everything you wanted to know about arrays <https://powershellexplained.com/2018-10-15-Powershell-arrays-Everything-you-wanted-to-know/>`_    

IF/Switch commands
==================

The conditions that can be tested in an ``if`` statement are very extensive:

* Equality/inequality: ``-eq|-ieq|-ceq / -ne|-ine|-cne``;
* Greater/less than: ``-gt|-igt|-cgt|-ge|-ige / -lt|-ilt|-clt|-le|-ile|-cle``;
* Wildcard: ``-like|-ilike|-clike|-notlike|-inotlike|-cnotlike``;
* Regular Expressions: ``-match|-imatch|-cmatch|-notmatch|-inotmatch|-cnotmatch``;
* Object type check: ``-is|-isnot``;
* Array <op> value: ``-contains|-icontains|-ccontains|-notcontains|-inotcontains|-cnotcontains``;
* Value <op> array: ``-in|-iin|-cin|-notin|-inotin|-cnotin``
* Logical operators: ``-not|!|-and|-or|-xor``
* Bitwise operators: ``-band|-bor|-bxor|-bnot|-shl|-shr``;
* PowerShell expressions: ``Test-Path|Get-Process``;
* PowerShell pipeline: ``(Get-Process | Where Name -eq Notepad)``;
* Null checking: ``($null -eq $value)``;

There is also a ``switch`` statement for comparing against multiple values.

::

   #requires -version 2
   Set-StrictMode -Version 2
   
   $apple = 10
   $pear = 20
   if ( $apple -gt $pear ) {
      write-host('apple is higher than pear')
   }
   elseif ( $apple -lt $pear ) {
      write-host('apple is lower than pear')
   }
   else {
      write-host('apple and pear are equal')
   }
   
   $path = 'file.txt'
   $alternatePath = 'folder1'
   if ( Test-Path -Path $path -PathType Leaf ) {
      Move-Item -Path $path -Destination $alternatePath
   }
   elseif ( Test-Path -Path $path ) {
      Write-Warning "A file is required but a folder was given."
   }
   else {
      Write-Warning "$path could not be found."
   }
   
   $fruit = 10
   switch ( $fruit ) {
      10  {
         write-host('fruit is an apple')
      }
      20 {
         write-host('fruit is an apple')
      }
      Default {
         write-host('unknown fruit')
      }
   }
   
Further reading:

   `PowerShell Explained: If .. then .. else .. equals operator <https://powershellexplained.com/2019-08-11-Powershell-if-then-else-equals-operator/>`_


Try/Catch
=========

Exception handling uses *Try/Catch*, but  the *Catch block* is only invoked on *terminating errors*.

::

   #requires -version 4
   Set-StrictMode -Version 2
   
   $error.clear()
   # $Error is an array of recent errors, index 0 being the latest
   # $Error[0] | get-member                 # what does an error return
   # $Error[0].tostring()                   # error text message
   # $Error[0].Exception | get-member       # method, properties of the exception
   # $Error[0].Exception.GetType().FullName # how to catch-it :-)
   
   $cwd =  get-childitem variable:pwd
   $filename = 'cannot-readme.txt'
   $path = Join-Path -path $cwd.value -childpath $filename
   try {
      $content = get-content -path $path -ErrorAction Stop
   }
   catch [System.Management.Automation.ItemNotFoundException] {
      write-warning $Error[0].ToString()
      exit(1) 
   }
   catch {
      write-warning $Error[0].ToString()
      write-warning $Error[0].Exception.GetType().FullName # exception message type
      exit(1) 
   }
   finally {
      write-warning("Resetting the Error Array")
      $error.clear()
   }
   write-host("Fetched the content of {0}" -f $path)
   exit(0)   

Note the following two points in the example:

* Addition of ``-ErrorAction Stop`` to ``get-content`` to make it a terminating error;
* The ``finally`` block is **always executed**, whether an exception is thrown or not!

Further reading:

* `Tutotials Point: Explain Try/Catch/Finally block in PowerShell <https://www.tutorialspoint.com/explain-try-catch-finally-block-in-powershell>`_

Loops
=====

There are several loop constructirs ``for``, ``foreach``, ``while`` and ``do .. while``.

::

   #requires -version 4
   Set-StrictMode -Version 2
   
   $names = ('Fred', 'Wilma', 'Pebbles', 'Dino')
   
   for ($index = 0; $index -lt $names.length; $index++) {
      write-host ('{0} Flintstone' -f $names[$index])
   }
   
   # Index often written as $i, $j, $k    
   for ($i = 0; $i -lt $names.length; $i++) {
      write-host ('{0} Flintstone' -f $names[$i])
   }
   
   foreach ($name in $names) {
      write-host ('{0} Flintstone' -f $name)
   }

   $hash = @{ Fred = 30; Wilma = 25; Pebbles = 1; Dino = 5 }   
   foreach ($key in $hash.keys) {
      write-host ('{0} Flintstone is {1:D} years old' -f $key, $hash[$key])
   }

   $index = 0;
   while ($index -lt $names.length){
      write-host ('{0} Flintstone' -f $names[$index])
      $index += 1
   }
   
   $index = 0;
   do {
      write-host ('{0} Flintstone' -f $names[$index])
      $index += 1
   } while($index -lt $names.length)



Operators
=========

``PowerShell`` supports the almost all the common programming language operators, with parenthesis to alter operator precedence.

::

   #requires -version 4
   Set-StrictMode -Version 2
   
   $a = 20
   $b = 10
   $c = 2
   
   # Arithmetic
   $a + $b + $c    # addition = 32
   $a - $b - $c    # subtraction = 8
   $a - $b + $c    # subtraction, addition = 12
   $a + $b - $c    # addition, subtraction = 28
   
   $a * $b * $c    # multiplication = 400
   $a + $b * $c    # addition, multiplication = 40
   $a * $b + $c    # multiplication, addition = 202
   $a * ($b + $c)  # multiplication, addition = 240
   
   $a / $b / $c    # division = 1
   $a + $b / $c    # addition, division = 15
   $a / $b + $c    # division, addition = 4
   $a / ($b + $c)  # division, addition = 1.66666666666667
   
   $a % $b         # modulus = 0
   $b % $a         # modulus = 10
   $c % $b         # modulus = 2
   
   # Comparison
   $a -eq $b       # equals = False
   $a -ne $b       # not equals = True
   $a -gt $b       # greater than = True
   $a -ge $a       # greater than or equal = True
   $a -lt $b       # less than = False
   $a -le $a       # less than or equal = True
   
   # Assignment
   $d = $a + $b    # assignment = 30
   $d += $c        # addition, assignment = 32
   $d -= $c        # subtraction, assiginment = 30
   
   $a = $true
   $b = $false
   
   # Logical
   $a -and $b      # and = False
   $a -or $b       # or = True
   -not $a         # not = False
   -not $a -and $b # not, and = False
   $a -and -not $b # and, not  = True


Backtick Operator
=================

The ````` is used for line continuation and to identify a *"tab"* and *"new line"* character.

* Word-wrap operator `````
* Newline ```n``
* Tab ```t``

Regular Expressions
===================

PowerShell supports *regular expressions* in much the same was as ``Perl`` or ``Python``.


Table taken from `TutorialsPoint.com - Regular Expression <https://www.tutorialspoint.com/powershell/powershell_regex.htm>`_

+-------------+----------------------------------------------------------------------------------------+
| Subquery    | Match description                                                                      |
+=============+========================================================================================+
| ^           | The beginning of the line.                                                             |
+-------------+----------------------------------------------------------------------------------------+
| $           | The end of the line.                                                                   |
+-------------+----------------------------------------------------------------------------------------+
| .           | Any single character except newline. Using m option it to matches the newline as well. |
+-------------+----------------------------------------------------------------------------------------+
| [...]       | Any single character in brackets.                                                      |
+-------------+----------------------------------------------------------------------------------------+
| [^...]      | Any single character not in brackets.                                                  |
+-------------+----------------------------------------------------------------------------------------+
| \\A         | Beginning of the entire string.                                                        |
+-------------+----------------------------------------------------------------------------------------+
| \\z         | End of the entire string.                                                              |
+-------------+----------------------------------------------------------------------------------------+
| \\Z         | End of the entire string except allowable final line terminator.                       |
+-------------+----------------------------------------------------------------------------------------+
| re*         | 0 or more occurrences of the preceding expression.                                     |
+-------------+----------------------------------------------------------------------------------------+
| re+         | 1 or more of the previous thing.                                                       |
+-------------+----------------------------------------------------------------------------------------+
| re?         | 0 or 1 occurrence of the preceding expression.                                         |
+-------------+----------------------------------------------------------------------------------------+
| re{ n}      | Exactly n number of occurrences of the preceding expression.                           |
+-------------+----------------------------------------------------------------------------------------+
| re{ n,}     | n or more occurrences of the preceding expression.                                     |
+-------------+----------------------------------------------------------------------------------------+
| re{ n, m}   | At least n and at most m occurrences of the preceding expression.                      |
+-------------+----------------------------------------------------------------------------------------+
| a¦b         | Either a or b.                                                                         |
+-------------+----------------------------------------------------------------------------------------+
| (re)        | Groups regular expressions and remembers the matched text.                             |
+-------------+----------------------------------------------------------------------------------------+
| (?: re)     | Groups regular expressions without remembering the matched text.                       |
+-------------+----------------------------------------------------------------------------------------+
| (?> re)     | Matches the independent pattern without backtracking.                                  |
+-------------+----------------------------------------------------------------------------------------+
| \\w         | The word characters.                                                                   |
+-------------+----------------------------------------------------------------------------------------+
| \\W         | The nonword characters.                                                                |
+-------------+----------------------------------------------------------------------------------------+
| \\s         | The whitespace. Equivalent to [\t\n\r\f].                                              |
+-------------+----------------------------------------------------------------------------------------+
| \\S         | The nonwhitespace.                                                                     |
+-------------+----------------------------------------------------------------------------------------+
| \\d         | The digits. Equivalent to [0-9].                                                       |
+-------------+----------------------------------------------------------------------------------------+
| \\D         | The nondigits.                                                                         |
+-------------+----------------------------------------------------------------------------------------+
| \\A         | The beginning of the string.                                                           |
+-------------+----------------------------------------------------------------------------------------+
| \\Z         | The end of the string. If a newline exists, it matches just before newline.            |
+-------------+----------------------------------------------------------------------------------------+
| \\z         | The end of the string.                                                                 |
+-------------+----------------------------------------------------------------------------------------+
| \\G         | The point where the last match finished.                                               |
+-------------+----------------------------------------------------------------------------------------+
| \\n         | Back-reference to capture group number "n".                                            |
+-------------+----------------------------------------------------------------------------------------+
| \\b         | The word boundaries. Matches the backspace (0x08) when inside the brackets.            |
+-------------+----------------------------------------------------------------------------------------+
| \\B         | The nonword boundaries.                                                                |
+-------------+----------------------------------------------------------------------------------------+
| \\n,\\t,\\r | Newlines, carriage returns, tabs, etc.                                                 |
+-------------+----------------------------------------------------------------------------------------+
| \\Q         | Escape (quote) all characters up to \E.                                                |
+-------------+----------------------------------------------------------------------------------------+
| \\E         | Ends quoting begun with \Q.                                                            |
+-------------+----------------------------------------------------------------------------------------+

Examples::

   #requires -version 4
   Set-StrictMode -Version 2

   "fred" -match "f..d"           # True (same as imatch)
   "fred" -imatch "F..d"          # True
   "fred" -cmatch "F..d"          # False
   "fred" -notmatch "W..ma"       # True
   "fred" -match "re"             # (match 're') True
   
   "dog" -match "d[iou]g"         # (dig, dug) True
   "ant" -match "[a-e]nt"         # (bnt, cnt, dnt, ent) True
   "ant" -match "[^brt]nt"        # True
   "fred" -match "^fr"            # (starts with 'fr') True
   "fred" -match "ed$"            # (ends with 'ed') True
   "doggy" -match "g*"            # True
   "doggy" -match "g?"            # True

   "Fred Flintstone" -match "\w+" # (matches word Fred) True
   "FredFlintstone" -match "\w+"  # (matches word Fred) True
   "Fred Flintstone" -match "\W+" # (matches >= 1 non-word) True
   "FredFlintstone" -match "\W+"  # (matches >= 1 non-word) False
   
   "Fred Flintstone" -match "\s+" # (matches >= 1 white-space) True
   "FredFlintstone" -match "\s+"  # (matches >= 1 white-space) False
   "Fred Flintstone" -match "\S+" # (matches >= 1 non white-space) True
   "FredFlintstone" -match "\S+"  # (matches >= 1 non white-space) True
   
   "Fred Flintstone" -match "\d+" # (matches >= 1 digit 0..9) False
   "Fred is 30" -match "\d+"      # (matches >= 1 digit 0..9) True
   "Fred Flintstone" -match "\D+" # (matches >= 1 non-digit 0..9) True
   "Fred is 30" -match "\D+"      # (matches >= 1 non-digit 0..9) True

   "Fred Flintstone" -match "\w?"     # (match >= 0 preceding pattern) True
   "Fred Flintstone" -match "\w{2}"   # (match 2 preceding pattern) True
   "Fred Flintstone" -match "\W{2}"   # (match 2 preceding pattern) False
   "Fred Flintstone" -match "\w{2,}"  # (match >2 preceding pattern) True
   "Fred Flintstone" -match "\W{2,}"  # (match >2 preceding pattern) False
   "Fred Flintstone" -match "\w{2,3}" # (match >2 <=3 preceding pattern) True
   "Fred Flintstone" -match "\W{2,3}" # (match >2 <=3 preceding pattern) False
   
   'Fred Flinstone' -replace '(\w+) (\w+)', 'Wilma $2' # Wilma Flinstone
   'fred Flinstone' -ireplace 'Fred (\w+)', 'Wilma $1' # Wilma Flinstone
   'fred Flinstone' -replace 'Fred (\w+)', 'Wilma $1'  # Wilma Flinstone
   'fred Flinstone' -creplace 'Fred (\w+)', 'Wilma $1' # fred Flinstone


Entire technical books are dedicated to Regular Expressions, the above is very brief.
For more details see:

* `Jeffrey Friedl: Mastering Regular Expressions <https://www.oreilly.com/library/view/mastering-regular-expressions/0596528124/>`_
* `Microsoft Docs: About Regular Expressions <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_regular_expressions>`_
* `Powershell: The many ways to use regex <https://powershellexplained.com/2017-07-31-Powershell-regex-regular-expression/>`_
* `Test and Debug: Regular Expression 101 <https://regex101.com/>`_
* `Test and Debug: RegEx <https://www.regextester.com/>`_
* `Test and Debug: Regular Expression Tester <https://www.freeformatter.com/regex-tester.html>`_

Reading Files
=============

Simple example, with the filename specified in the script.

::

   #requires -version 4
   Set-StrictMode -Version 2
   
   $filename = 'file.txt'
   $addCWD = $false
   $path = $filename 
   if ($addCWD) {
      $path = Join-Path -path $cwd.value -childpath $filename
   }
   
   write-host("if...then...else")
   if (-not (Test-Path -path $path -pathtype leaf) ) {
      write-warning("Filename, {0}, does not exist" -f $path)
      exit(1)
   }
   else {
      $count = 1
      foreach ($line in get-content $path) {
         write-host("{0:D3}:{1}" -f $count, $line)
         $count += 1
      }
      $fh = get-childitem $path # get file attributes
   }
   
   write-host("try...catch")
   try {
      $count = 1
      foreach ($line in get-content $path -ErrorAction Stop) {
         write-host("{0:D3}:{1}" -f $count, $line)
         $count += 1
      }
      $fh = get-childitem $path # get file attributes
   }
   catch {
      write-warning $Error[0].ToString()
      write-warning $Error[0].Exception.GetType().FullName # exception message type
      exit(1)
   }
   
   exit(0) 

If the filename(s) are supplied on the command line, then ``globbing`` (file pattern matching) will treat several files as one file.
This following accepts a single file name argument and expands the ``glob`` before processing so the name can be displayed.

::

   #requires -version 4
   Set-StrictMode -Version 2
   
   $pattern = $Args[0]  # 'file*'
   if ($Args[0] -eq $null) {
      write-warning("Missing file pattern argument")
      exit(1)
   }
   $filenames = get-childitem -Name $pattern
   
   write-host("Simple file pattern")
   foreach ($filename in $filenames) {
      $addCWD = $false
      $path = $filename
      if ($addCWD) {
         $path = Join-Path -path $cwd.value -childpath $filename
      }
      
      if (-not (Test-Path -path $path -pathtype leaf) ) {
         write-warning("Filename, {0}, does not exist" -f $path)
         exit(1)
      }
      else {
         $count = 1
         write-host("filename: {0}" -f $filename)
         foreach ($line in get-content $path) {
           write-host("  {0:D3}:{1}" -f $count, $line)
           $count += 1
         }
         $fh = get-childitem $path # get file attributes
      }
   }

This example accepts all commandline arguments as file names and does not consider any ``globbing`` (file pattern matching).

::

   #requires -version 4
   Set-StrictMode -Version 2
   
   write-host("All file arguments")
   foreach ($filename in $Args) {
      $addCWD = $false
      $path = $filename
      if ($addCWD) {
         $path = Join-Path -path $cwd.value -childpath $filename
      }
      
      if (-not (Test-Path -path $path -pathtype leaf) ) {
         write-warning("Filename, {0}, does not exist" -f $path)
         exit(1)
      }
      else {
         $count = 1
         write-host("filename: {0}" -f $filename)
         foreach ($line in get-content $path) {
           write-host("  {0:D3}:{1}" -f $count, $line)
           $count += 1
         }
         $fh = get-childitem $path # get file attributes
      }
   }


Writing Files
=============

Simplest approach is to use `set-content <https://docs.microsoft.com/powershell/module/microsoft.powershell.management/set-content>`_, 
`add-content <https://docs.microsoft.com/powershell/module/microsoft.powershell.management/add-content>`_ and 
`clear-content <https://docs.microsoft.com/powershell/module/microsoft.powershell.management/clear-content>`_ *cmd-lets*, 
which have many options not covered here.

::

   #requires -version 4
   Set-StrictMode -Version 2
      
   $h = @{ Fred = 30; Wilma = 25; Pebbles = 1; Dino = 5 }
   
   set-content -path "file.obj" -value $h    # writes hash-table object 
   
   $path = "file.txt"
   
   # add one line at a time, note no need to close the file
   set-content -path $path -value $null # creates and closes an empty file
   foreach ($key in $h.keys) {
       add-content -path $path -value ("{0}:{1:D}" -f $key, $h[$key]) # adds content and closes
       # ("{0}:{1:D}" -f $key, $h[$key]) | add-content -path $path    # same, less intuative
   }
   
   clear-content -path $path # clear the file contents

   # string with line continuation characters.
   $text = "Fred:30`
   Wilma:25`
   Pebbles:1`
   Dino:5"
   $text | set-content -path $path
   
   clear-content -path $path # clear the file contents

   # string containing new-line characters.
   $text = "Fred:30`nWilma:25`nPebbles:1`nDino:5"
   $text | set-content -path $path

   clear-content -path $path # clear the file contents
   
   # string containing new-line characters using out-file
   $text | Out-File -FilePath $path

See also:

* `Microsoft docs: set-content <https://docs.microsoft.com//powershell/module/microsoft.powershell.management/set-content>`_
* `Microsoft docs: add-content <https://docs.microsoft.com//powershell/module/microsoft.powershell.management/add-content>`_
* `Microsoft docs: out-file <https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/out-file>`_
* `Microsoft docs: new-temporaryfile <https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/new-temporaryfile>`_

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

* `Microsoft docs: Import-CSV <https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/import-csv>`_
* `Microsoft docs: Out-GridView <https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/out-gridview>`_

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

Further reading:
   
* `ConvertTo-Json converts an object to a JSON-formatted string. <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertto-json>`_
* `ConvertFrom-Json converts a JSON-formatted string to a custom object or a hash table. <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-json>`_
* `W3Schools: Introduction to JSON <https://www.w3schools.com/js/js_json_intro.asp>`_

Reading XML files
=================

``Powershell`` supports full manipulation of the XML DOM, read the `Introduction to XML <https://www.w3schools.com/XML/xml_whatis.asp>`_ 
and `.NET XmlDocument Class <https://docs.microsoft.com/en-us/dotnet/api/system.xml.xmldocument>`_ for more detailed information. The examples shown 
are very redimentary, and only show a few of the manipulations you can perform on XML objects.

**Note**, cmdlets `Export-Clixml <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-clixml>`_ and 
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

**Note**, cmdlets `Export-Clixml <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-clixml>`_ and 
`Import-Clixml <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-clixml>`_ provide a simplified way to save 
and reload your ``PowerShell`` objects and are ``Microsoft`` specific.

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

Log files
=========

::

   # tailing a log file
   PS> get-content -wait -last 10 "application.log"
   PS> get-content -wait "application.log" | out-host -paging
   
   # writing a time-stamped log message
   PS> $LogFile = "application.log"
   PS> $DateTime = "[{0:MM/dd/yy} {0:HH:mm:ss}]" -f (Get-Date) # [03/22/21 21:07:06]
   PS> $LogMessage = "$Datetime: $LogString"
   PS> add-content $LogFile -value $LogMessage

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


More detailed formatting examples:

* `PowershellPrimer.com: Formatting Output <https://powershellprimer.com/html/0013.html>`_
* `Microsoft documentation: Get-Date <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-date>`_

Ouput methods:

* `Microsoft Docs: Write Output <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-output>`_
* `Microsoft Docs: Write Warning <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-warning>`_
* `Microsoft Docs: Write Host <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-host>`_
* `Microsoft Docs: Write Error <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-error>`_

Running PowerShell scripts
==========================

PowerShell is an often abused hackers attack vector, so modern versions of Windows prevent PowerShell scripts from
being executed *out-of-the-box*, although the ``cmd-lets`` can be run. 

Many articles suggest the disabling this security feature... **DO NOT DO THIS** 

Furthermore most companies harden their Windows laptop and server installations, so disabling may not work anyway.

Ways to work with this restriction, are not intuitive... it took me some time to figure it out, and I am 
still be no means an expert, hopefully this will get you started, and you are always welcome to contact me to improve this section.

The execution-policy, controls the execution of PowerShell scripts, good references to read are:

* `Allow other to run your PowerShell scripts... <https://blog.danskingdom.com/allow-others-to-run-your-powershell-scripts-from-a-batch-file-they-will-love-you-for-it/>`_
* `Setup Powershell scripts for automatic execution <https://stackoverflow.com/questions/29645/set-up-powershell-script-for-automatic-execution/8597794#8597794>`_
* `Get-ExecutionPolicy <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-executionpolicy?view=powershell-7>`_

If you start ``PowerShell`` as administrator, then you can change the *'execution-policy'*, and you should  
change the *'CurrentUser'*, which is *your* execution-policy rights, see Get-ExecutionPolicy link.
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
downloaded from the Internet will run as you, and with your privileges, so *Avoid Doing This*.

When developing your scripts you can try using the following to avoid having certificates installed and updating the signature each time you change the script.

::

  PS> powershell.exe -noprofile -executionpolicy bypass -file .\script.ps1 

This may not be permitted on Corporate laptops which usually have additional security restrictions.
  

PowerShell Exection Policies
============================ 

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
   

Generating and Installing Certificates
======================================

This section will show how to use ``openssl`` and ``WLS2`` to generate self-signed certificates

::

   To come shortly.
   
How to sign scripts for your own use.
=====================================

::

   Draft and not completely finished.


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
--------------------------------

Some proposals to avoid signing PowerShell scripts.

* `Provide A Batch File To Run Your PowerShell Script From <https://blog.danskingdom.com/allow-others-to-run-your-powershell-scripts-from-a-batch-file-they-will-love-you-for-it/>`_
* `Set Up Powershell Script For Automatic Execution <https://stackoverflow.com/questions/29645/set-up-powershell-script-for-automatic-execution/8597794#8597794>`_

Some internet posts recommend disabling the execution policy, but I would advise against.

::

   ### DO NOT DO THE FOLLOWING, UNLESS YOU KNOW WHAT YOU ARE DOING  ###
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
   PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Unrestricted

   