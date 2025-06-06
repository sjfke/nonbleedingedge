:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/powershell-scripts.rst

===============================
PowerShell Scripting Cheatsheet
===============================

This is the companion to ``PowerShell Cheatsheet``, which focuses on writing PowerShell scripts.

.. topic:: According to Microsoft ``PowerShell``

   Is a cross-platform task automation and configuration management framework, consisting of a *command-line shell* and 
   *scripting language* that is built on top of the ``.NET Common Language Runtime`` (CLR), accepts and returns ``.NET objects``.
   This brings entirely new tools and methods for automation.
      
This means learning new skills and thinking differently which can be frustrating while learning. 

To simplify maintenance I write PowerShell scripts as standalone utilities deployed in a single file, this means I have to *copy-and-paste* 
my favourite frequently used functions, such as *dumpArrayList*, *dumpHashTable* because there is no mechanism to textually include 
your favourite functions into the source when writing and testing. 

It is possible to split your script into multiple files, create libraries of your favourite utilities etc.
I do not cover this topic, the example script shows where/how to ``source`` you library files, and if you wish to create your 
own modules, see `How to Write a PowerShell Script Module <https://learn.microsoft.com/en-us/powershell/scripting/developer/module/how-to-write-a-powershell-script-module>`_.

************
Introduction
************

``PowerShell`` is very powerful scripting language, often used to automate routine tasks, which makes it an ideal
target for *would-be hackers*. To mitigate this Microsoft limits PowerShell execution, even though the
individual ``cmdlets`` can always be run.

If your ``Get-ExecutionPolicy`` is like this

.. code-block:: pwsh-session

   PS> Get-ExecutionPolicy
   Restricted

   PS> Get-ExecutionPolicy -List

           Scope ExecutionPolicy
           ----- ---------------
   MachinePolicy       Undefined
      UserPolicy       Undefined
         Process       Undefined
     CurrentUser       Undefined
    LocalMachine       Restricted

The ``PowerShell`` script will not execute!

.. code-block:: pwsh-session

    PS1> .\hello-world.ps1
    .\hello-world.ps1 : File C:\Users\sjfke\hello-world.ps1 cannot be loaded because running scripts is disabled on this
    system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
    At line:1 char:1
    + .\hello-world.ps1
    + ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : SecurityError: (:) [], PSSecurityException
        + FullyQualifiedErrorId : UnauthorizedAccess

.. warning::
    Many articles on the internet suggest the disabling or trying to work around this security feature... **PLEASE AVOID DOING THIS**!

Windows often provides *Developer* section in ``Settings``, which allows local ``PowerShell``  scripts to be
executed by the ``CurrentUser`` by setting the ``ExecutionPolicy`` to ``RemoteSigned``.

Alternatively run a ``PowerShell`` as ``Administrator`` set the following, choosing the ``[A]`` option.

.. code-block:: pwsh-session

    PS-ADM> set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

    Execution Policy Change
    The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the security risks
    described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
    [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): A


Suggested Laptop settings
=========================

Locally developed ``PowerShell scripts`` will be executed but those from any other source will need to be signed.

.. code-block:: pwsh-session

    PS C:\WINDOWS\system32> Get-ExecutionPolicy -List
            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser    RemoteSigned
     LocalMachine       Undefined

    PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


Suggested Server settings
=========================

All ``PowerShell scripts`` should be signed, if *too restrictive* for your environment use
`Suggested Laptop settings`_

.. code-block:: pwsh-session

    PS C:\WINDOWS\system32> Get-ExecutionPolicy -List
            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser       AllSigned
     LocalMachine       AllSigned

    PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
    PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope LocalMachine


*****************
Language Overview
*****************

The language makes use of `.Net Framework <https://en.wikipedia.org/wiki/.NET_Framework>`_ and is built on 
top of the `.NET Common Language Runtime (CLR) <https://learn.microsoft.com/en-us/dotnet/standard/clr>`_ , and
manipulates `.NET objects <https://learn.microsoft.com/en-us/dotnet/api/system.object>`_. If the language itself
does not provide what you need, there may be a `Popular PowerShell Module <https://learn.microsoft.com/en-us/archive/technet-wiki/4308.popular-powershell-modules>`_
you can download or you can access the `.Net APIs <https://learn.microsoft.com/en-us/dotnet/api>`_ directly, a good example being `ArrayLists <https://learn.microsoft.com/en-us/dotnet/api/system.collections.arraylist>`_ which
are dynamic in size unlike a *PowerShell Array*.

In common with other object oriented languages, ``PowerShell`` has features such *inheritance*, *subclasses*, *getters*, *setters*, *modules* etc.
Functions and methods support both ``named`` and ``positional`` arguments, that can be mixed liberally, but done inappropriately can make the intention
more confusing. Often it is clearer to use `splatting <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting>`_ rather
than individual name or positional parameters.

Useful starting points when learning about the language:

* `Introduction to scripting in PowerShell <https://learn.microsoft.com/en-us/training/modules/script-with-powershell/>`_
* `*tutorials*point - Powershell Tutorial <https://www.tutorialspoint.com/powershell/index.htm>`_

Unlike most texts on programming languages, let us starts with a simple but realistic PowerShell example, with many of
the language details being covered in subsequent sections.

**************
Example Script
**************

This is a contrived but realistic PowerShell script to illustrate several important points.
It is based on a `gist template from 9to5IT <https://gist.github.com/9to5IT/9620683>`_, which is augmented to force
the syntax version and to be more strict on the use of uninitialized variables.

.. code-block:: powershell

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

* The `#requires -version 4 <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_requires>`_ PowerShell version 4 syntax, (use *version 2*, if windows is very old);
* Initial comment block ``.SYNOPSIS...`` provides the ``get-help`` text, **note** line-spacing is important;
* The `param() <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters>`_ block must be the first *non-comment line* for command-line arguments;
* The `Set-StrictMode -Version 2 <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/set-strictmode>`_ checks the usage of uninitialized variables;


*******************
Language Keypoint's
*******************

Variables
=========

Powershell variables can be any of the `Basic DataTypes`_ such as *integers*, *characters*, *strings*, *arrays*, and *hash-tables*, but also ``.Net`` objects that represent such things as
*processes*, *services*, *event-logs*, and even *computers*.

.. code-block:: pwsh-session

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

.. code-block:: pwsh-session

  
   PS> $a = 1, 2, 3                    # array of integers
   PS> $a = (1, 2, 3)                  # array of integers (my personal preference)
   PS> $a = ('a','b','c')
   PS> $a = (1, 2, 3, 'x')             # array of System.Int32's, System.String
   PS> [int[]]$a = (1, 2, 3, 'x')      # will fail 'x', array of System.Int32 only
   
   PS> $a = ('fred','wilma','pebbles')
   PS> $a[0]             # fred
   PS> $a[2]             # pebbles
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
* `Microsoft Docs ArrayList Class for dynamically resizable arrays <https://learn.microsoft.com/en-us/dotnet/api/system.collections.arraylist>`_
* `Kevin Blumenfeld's GitHub Gist Collection Type Guidance <https://gist.github.com/kevinblumenfeld/4a698dbc90272a336ed9367b11d91f1c>`_


HashTables
==========

A HashTable is an unordered collection of key:value pairs, synonymous with an object and its properties. 
Later versions support known/fixed order hash elements, ``$hash = [ordered]@{}``.

.. code-block:: pwsh-session

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

    PS> $h.keys                    # unordered: Dino, Pebbles, Fred, Wilma
    PS> $h.values                  # unordered: 5, 1, 30, 25 (but same as $h.keys order)
    PS> $h.keys | sort             # sorted: Dino, Fred, Pebbles, Wilma
    PS> $h.keys | sort -Descending # reverse-sorted: Wilma, Pebbles, Fred, Dino

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

    # specific order (Fred, Wilma, Pebbles, Dino)
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
 
* `Powershell: Everything you wanted to know about a hashtable <https://powershellexplained.com/2016-11-06-powershell-hashtable-everything-you-wanted-to-know-about/>`_

Objects
=======

If you cannot create what you need from *Arrays, HashTables, ArrayLists, Queues, Stacks etc.*, then 
it is possible to create custom PowerShell objects, but to date I have never needed to do this.
For more details, read:

* `David Bluemenfeld: Collection Type Guidance <https://gist.github.com/kevinblumenfeld/4a698dbc90272a336ed9367b11d91f1c>`_;
* `Microsoft TechNet: Creating Custom Objects <https://learn.microsoft.com/en-us/archive/technet-wiki/7804.powershell-creating-custom-objects>`_;
* `Kevin Marquette: Everything you wanted to know about PSCustomObject <https://powershellexplained.com/2016-10-28-powershell-everything-you-wanted-to-know-about-pscustomobject/>`_;

Functions
=========

Function arguments and responses are passed by reference, so an argument can be changed inside the function and remains
unchanged outside the function, **but** this is considered *"bad programming practice"*, so better to avoid doing this. 
Functions return references to objects, as illustrated in the `Example Script`_ where references to *HashTable* and *Array* objects are returned.

While each function call returns a reference to a new (*different*) object, be careful about the scope of the variable you assign this reference too, 
it is easy to create multiple references to the same object.

While mixing named (*order independent*) and positional (*order dependent*) arguments is permitted it can cause strange errors, so unless you are only
supplying one or two arguments, a better approach is to use `splatting <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting>`_.
The following contrived example illustrates the basics but the ``param ( ... )`` section has many options not shown here. 

.. code-block:: powershell
  
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
    createPerson @arguments                   # fails,  WARNING: createPerson - age, 0, is incorrect

    $arguments = @{
        age = 21
        verbose = $true
        debug = $false
    }
    createPerson @arguments                   # fails, WARNING: createPerson - name is missing

Further reading:

* Microsoft Docs, `Chapter 9 - Functions <https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/09-functions>`_
* Microsoft Docs, `About Functions Advanced Parameters <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters>`_.

ArrayList
=========

.. code-block:: pwsh-session

    PS> $names = New-Object -TypeName System.Collections.ArrayList
    PS> $names.gettype()              # ArrayList

    PS> $firstnames = [System.Collections.ArrayList]::new() # alternative syntax
    PS> $firstnames.gettype()         # ArrayList

    PS> $index = $names.Add('fred')   # returns array-list index: i.e. 0
    PS> [void]$names.Add('wilma')     # discard array-list index
    PS> [void]$names.Add('pebbles')
    PS> [void]$names.Add('dino')

    # one-line creation, empty or populated
    PS> [System.Collections.ArrayList]$names = @()
    PS> [System.Collections.ArrayList]$names = @('fred','wilma','pebbles', 'dino')

    PS> $names.Count                  # returns 4
    PS> $names[1]                     # wilma
    PS> $names.Remove(3)              # dino ran away or did he?
    PS> $names.Count                  # 4, no dino is still there
    PS> $names.[3]                    # dino
    PS> $names.RemoveAt(3)            # dino, has really gone this time
    PS> $names.Count                  # returns 3
    PS> [void]$names.Add('dino')      # dino found
    PS> $names.Remove('dino')         # dino, escaped again
    PS> [void]$names.Add('dino')      # dino found ... again

    PS> 'fred' -in $names             # True  (not supported in PowerShell 2)
    PS> 'barney' -in $names           # False (not supported in PowerShell 2)
    PS> $names -contains 'fred'       # True
    PS> $names -contains 'barney'     # False

    PS> [void]$names.Insert(3,'baby puss')
    PS> $names                        # 0:fred, 1:wilma, 2:pebbles, 3:baby puss, 4:dino
    PS> $names.remove('fido')
    PS> $names                        # 0:fred, 1:wilma, 2:pebbles, 3:dino

    # Generic List are ArrayList's of a fixed type
    PS> [System.Collections.Generic.List[string]]$names = @()                                 # empty
    PS> [System.Collections.Generic.List[string]]$names = @('fred','wilma','pebbles', 'dino') # populated

    PS> [System.Collections.Generic.List[int]]$ages = @()                                     # empty
    PS> [System.Collections.Generic.List[int]]$ages = (30, 25, 1, 5)                          # populated

    PS> [void]$names.add(30)          # 0:fred, 1:wilma, 2:pebbles, 3:dino, 4:30              # auto-casting
    PS> $ages.add('baby puss')        # fails, throws System.Int32 conversion exception

Further reading:

* `The .Net ArrayList Class <https://learn.microsoft.com/en-us/dotnet/api/system.collections.arraylist>`_
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

.. code-block:: powershell

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

.. code-block:: powershell

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

* `Tutorials Point: Explain Try/Catch/Finally block in PowerShell <https://www.tutorialspoint.com/explain-try-catch-finally-block-in-powershell>`_

Loops
=====

There are several loop constructors ``for``, ``foreach``, ``while`` and ``do .. while``.

.. code-block:: powershell

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

.. code-block:: powershell

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
    $d -= $c        # subtraction, assignment = 30

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
| \\W         | The non-word characters.                                                               |
+-------------+----------------------------------------------------------------------------------------+
| \\s         | The whitespace. Equivalent to [\t\n\r\f].                                              |
+-------------+----------------------------------------------------------------------------------------+
| \\S         | The non-whitespace.                                                                    |
+-------------+----------------------------------------------------------------------------------------+
| \\d         | The digits. Equivalent to [0-9].                                                       |
+-------------+----------------------------------------------------------------------------------------+
| \\D         | The non-digits.                                                                        |
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
| \\B         | The non-word boundaries.                                                               |
+-------------+----------------------------------------------------------------------------------------+
| \\n,\\t,\\r | Newlines, carriage returns, tabs, etc.                                                 |
+-------------+----------------------------------------------------------------------------------------+
| \\Q         | Escape (quote) all characters up to \E.                                                |
+-------------+----------------------------------------------------------------------------------------+
| \\E         | Ends quoting begun with \Q.                                                            |
+-------------+----------------------------------------------------------------------------------------+

Examples

.. code-block:: powershell

    #requires -version 4
    Set-StrictMode -Version 2

    "fred" -match "f..d"               # True (same as imatch)
    "fred" -imatch "F..d"              # True
    "fred" -cmatch "F..d"              # False
    "fred" -notmatch "W..ma"           # True
    "fred" -match "re"                 # (match 're') True

    "dog" -match "d[iou]g"             # (dig, dug) True
    "ant" -match "[a-e]nt"             # (bnt, cnt, dnt, ent) True
    "ant" -match "[^brt]nt"            # True
    "fred" -match "^fr"                # (starts with 'fr') True
    "fred" -match "ed$"                # (ends with 'ed') True
    "doggy" -match "g*"                # True
    "doggy" -match "g?"                # True

    "Fred Flintstone" -match "\w+"     # (matches word Fred) True
    "FredFlintstone" -match "\w+"      # (matches word Fred) True
    "Fred Flintstone" -match "\W+"     # (matches >= 1 non-word) True
    "FredFlintstone" -match "\W+"      # (matches >= 1 non-word) False

    "Fred Flintstone" -match "\s+"     # (matches >= 1 white-space) True
    "FredFlintstone" -match "\s+"      # (matches >= 1 white-space) False
    "Fred Flintstone" -match "\S+"     # (matches >= 1 non white-space) True
    "FredFlintstone" -match "\S+"      # (matches >= 1 non white-space) True

    "Fred Flintstone" -match "\d+"     # (matches >= 1 digit 0..9) False
    "Fred is 30" -match "\d+"          # (matches >= 1 digit 0..9) True
    "Fred Flintstone" -match "\D+"     # (matches >= 1 non-digit 0..9) True
    "Fred is 30" -match "\D+"          # (matches >= 1 non-digit 0..9) True

    "Fred Flintstone" -match "\w?"     # (match >= 0 preceding pattern) True
    "Fred Flintstone" -match "\w{2}"   # (match 2 preceding pattern) True
    "Fred Flintstone" -match "\W{2}"   # (match 2 preceding pattern) False
    "Fred Flintstone" -match "\w{2,}"  # (match >2 preceding pattern) True
    "Fred Flintstone" -match "\W{2,}"  # (match >2 preceding pattern) False
    "Fred Flintstone" -match "\w{2,3}" # (match >2 <=3 preceding pattern) True
    "Fred Flintstone" -match "\W{2,3}" # (match >2 <=3 preceding pattern) False

    'Fred Flintstone' -replace '(\w+) (\w+)', 'Wilma $2' # Wilma Flintstone
    'fred Flintstone' -ireplace 'Fred (\w+)', 'Wilma $1' # Wilma Flintstone
    'fred Flintstone' -replace 'Fred (\w+)', 'Wilma $1'  # Wilma Flintstone
    'fred Flintstone' -creplace 'Fred (\w+)', 'Wilma $1' # fred Flintstone

Entire technical books are dedicated to Regular Expressions, the above is very brief.
For more details see:

* `Jeffrey Friedl: Mastering Regular Expressions <https://www.oreilly.com/library/view/mastering-regular-expressions/0596528124/>`_
* `Microsoft Docs: About Regular Expressions <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters>`_
* `Powershell: The many ways to use regex <https://powershellexplained.com/2017-07-31-Powershell-regex-regular-expression/>`_
* `Test and Debug: Regular Expression 101 <https://regex101.com/>`_
* `Test and Debug: RegEx <https://www.regextester.com/>`_
* `Test and Debug: Regular Expression Tester <https://www.freeformatter.com/regex-tester.html>`_

**********************
Typical Usage Examples
**********************

Reading Files
=============

Simple example, with the filename specified in the script.

.. code-block:: powershell

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

.. code-block:: powershell

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

.. code-block:: powershell

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

Simplest approach is to use `set-content <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-content>`_,
`add-content <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/add-content>`_ and
`clear-content <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/clear-content>`_ *cmd-lets*,
which have many options not covered here.

.. code-block:: powershell

    #requires -version 4
    Set-StrictMode -Version 2

    $h = @{ Fred = 30; Wilma = 25; Pebbles = 1; Dino = 5 }

    set-content -path "file.obj" -value $h    # writes hash-table object

    $path = "file.txt"

    # add one line at a time, note no need to close the file
    set-content -path $path -value $null # creates and closes an empty file
    foreach ($key in $h.keys) {
        add-content -path $path -value ("{0}:{1:D}" -f $key, $h[$key]) # adds content and closes
        # ("{0}:{1:D}" -f $key, $h[$key]) | add-content -path $path    # same, less intuitive
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

* `Microsoft docs: set-content <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-content>`_
* `Microsoft docs: add-content <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/add-content>`_
* `Microsoft docs: out-file <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/out-file>`_
* `Microsoft docs: new-temporaryfile <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/new-temporaryfile>`_

Displaying CSV Files
====================

Powershell provides ``cmdlets`` for handling these which avoid importing into ``Excel`` and ``MS Access``.
The ``out-gridview`` renders the output the data in an interactive table. 

.. code-block:: pwsh-session

    PS> import-csv -Path file.csv -Delimeter "`t" | out-gridview # load and display a <TAB> separated file.
    PS> import-csv -Path file.csv -Delimeter ";" | out-gridview  # load and display a ';' separated file.

    PS> get-content file.csv
    Name;Age
    Fred;30
    Wilma;25
    Pebbles;1
    Dino;5

    PS> $f = import-csv -delimiter ';' file.

    PS> $f.Name    # Fred Wilma Pebbles Dino
    PS> $f[1].Name # Wilma
    PS> $f.Age     # 30 25 1 5
    PS> $f[3].Age  # 5

    PS> for ($i =0; $i -lt $f.length; $i++) {
        write-output("{0,-7} is {1:D} years" -f $f[$i].Name, $f[$i].Age)
    }

    PS> import-csv -delimiter ';' file.csv | out-gridview

* `Microsoft docs: Import-CSV <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-csv>`_
* `Microsoft docs: Out-GridView <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/out-gridview>`_

Reading and Writing JSON Files
==============================

PowerShell requires that ``ConvertTo-Json`` and ``ConvertFrom-Json`` modules are installed.

.. code-block:: pwsh-session

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
   
* `ConvertFrom-Json converts a JSON-formatted string to a custom object or a hash table. <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-json>`_
* `ConvertTo-Json converts an object to a JSON-formatted string. <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertto-json>`_
* `W3Schools: Introduction to JSON <https://www.w3schools.com/js/js_json_intro.asp>`_

Reading XML Files
=================

``Powershell`` supports full manipulation of the XML DOM, read the `Introduction to XML <https://www.w3schools.com/XML/xml_whatis.asp>`_ 
and `.NET XmlDocument Class <https://learn.microsoft.com/en-us/dotnet/api/system.xml.xmldocument>`_ for more detailed information. The examples shown
are very rudimentary, and only show a few of the manipulations you can perform on XML objects.

**Note**, cmdlets `Export-Clixml <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-clixml>`_ and
`Import-Clixml <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-clixml>`_ provide a simplified way to save
and reload your ``PowerShell`` objects and are ``Microsoft`` specific.

.. code-block:: pwsh-session

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


Writing XML Files
=================

To generate an XML file, use the `XmlTextWriter Class <https://learn.microsoft.com/en-us/dotnet/api/system.xml.xmltextwriter>`_

**Note**: cmdlets `Export-Clixml <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-clixml>`_ and
`Import-Clixml <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-clixml>`_ provide a simplified way to save
and reload your ``PowerShell`` objects and are ``Microsoft`` specific.

.. code-block:: powershell

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

Log Files: tail, write time-stamped message
===========================================

.. code-block:: pwsh-session

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

Very similar to Python ``-f`` operator, examples use ``write-host`` but can be used with other cmdlets, such as assignment.
Specified as ``{<index>, <alignment><width>:<format_spec>}``

.. code-block:: pwsh-session

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
* `Microsoft documentation: Get-Date <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-date>`_

Output methods:

* `Microsoft Docs: Write Output <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-output>`_
* `Microsoft Docs: Write Warning <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-warning>`_
* `Microsoft Docs: Write Host <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-host>`_
* `Microsoft Docs: Write Error <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-error>`_

***********************
Security Considerations
***********************

Running PowerShell scripts
==========================

``PowerShell`` is very powerful scripting language, often used to automate routine tasks, which makes it an ideal
target for *would-be hackers*. To mitigate this Microsoft limits PowerShell execution, even though the
individual ``cmdlets`` can always be run.

Many articles on the internet suggest the disabling or trying to work around this security feature... **PLEASE AVOID DOING THIS**!

Many Windows distributions provide *Developer* section in ``Settings``, which allows local ``PowerShell``  scripts to be
executed by the ``CurrentUser`` by setting the ``ExecutionPolicy`` to ``RemoteSigned``.

Alternatively this can also be done manually by running ``PowerShell`` as ``Administrator``

.. code-block:: pwsh-session

    PS-ADM> set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

    Execution Policy Change
    The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the security risks
    described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
    [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): A


A sensible working setup for your personal laptop

.. code-block:: pwsh-session

    PS> Get-ExecutionPolicy -list
            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser    RemoteSigned
     LocalMachine       Undefined

A sensible working setup for a typical windows server installation

.. code-block:: pwsh-session

    PS> Get-ExecutionPolicy -list
            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser       AllSigned
     LocalMachine       AllSigned


PowerShell Execution Policies
=============================

`Execution policies <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies>`_
are a safety feature to control the conditions under which ``PowerShell`` loads configuration
files and runs scripts, with the intention to prevent the execution of malicious scripts. This is augmented with the notion
of a ``Execution Policy Scope``, conditions under which the ``Execution Policy`` is applied

Execution policies (highest to lowest):

* ``Restricted`` does not permit any scripts to run (*.ps1xml, .psm1, .ps1*)
* ``AllSigned`` prevents running scripts that do not have a digital signature
* ``RemoteSigned`` prevents running downloaded scripts that do not have a digital signature
* ``Unrestricted`` runs without a digital signature, warns about non-local intranet zone scripts
* ``Bypass`` allows running of scripts without any digital signature, and without any warnings
* ``Undefined`` no execution policy is defined

Execution Policy Scope (highest to lowest):

* ``MachinePolicy`` set by a Group Policy for all users of the computer
* ``UserPolicy`` set by a Group Policy for the current user of the computer
* ``Process`` current PowerShell session, environment variable ``$env:PSExecutionPolicyPreference``
* ``CurrentUser`` affects only the current user, ``HKEY_CURRENT_USER`` registry subkey
* ``LocalMachine`` all users on the current computer, ``HKEY_LOCAL_MACHINE`` registry subkey

In a commercial or industrial environment this is usually managed by your local Windows Administrators, hence
``MachinePolicy`` and ``UserPolicy`` in ``Execution Policy Scope`` and you maybe prevented from changing anything.

Example ``Set-ExecutionPolicy`` commands, these need to be executed in ``PowerShell`` running as ``Administrator``

.. code-block:: pwsh-session

   PS-ADM> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned # sets: LocalMachine RemoteSigned
   PS-ADM> Set-ExecutionPolicy -ExecutionPolicy Restricted   # sets: LocalMachine Restricted
   PS-ADM> Set-ExecutionPolicy -ExecutionPolicy Undefined    # sets: LocalMachine Undefined

   PS-ADM> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   PS-ADM> Set-ExecutionPolicy -ExecutionPolicy AllSigned    # mandate AllSigned for LocalMachine
   PS-ADM> Set-ExecutionPolicy -ExecutionPolicy Default      # restore: LocalMachine defaults

PowerShell Code Signing
=======================

Microsoft uses a proprietary technique called ``Authenticode`` for code signing ``PowerShell``

* `Authenticode (I): Understanding Windows Authenticode <https://reversea.me/index.php/authenticode-i-understanding-windows-authenticode/>`_
* `Authenticode (II): Verifying Authenticode with OpenSSL <https://reversea.me/index.php/authenticode-ii-verifying-authenticode-with-openssl/>`_
* `Verifying Windows binaries, without Windows <https://blog.trailofbits.com/2020/05/27/verifying-windows-binaries-without-windows/>`_

Apart from the proprietary nature, which impacts its generation, it is an asymmetric keypair, signed by
an approved Certificate Authority (CA), installed in the Windows certificate stores, and so involves creating a
code signing request (CSR) with an associated keypair and having it signed by an approved Certificate Authority.

Within a commercial organization there is probably an existing process that needs to be followed to generate the CSR
and have it approved by the internally Certificate Authority.

Externally available applications or product should probably use an external commercially available service,
the following guides may be useful.

* `SSLshopper:  Microsoft Authenticode Certificates <https://www.sslshopper.com/microsoft-authenticode-certificates.html>`_
* `SSLstore: Sign Code with Microsoft Authenticode <https://www.thesslstore.com/knowledgebase/code-signing-sign-code/sign-code-microsoft-authenticode/>`_
* `SSL.com: Microsoft Authenticode Code Signing in Linux with Jsign <https://www.ssl.com/how-to/microsoft-authenticode-code-signing-in-linux-with-jsign/>`_

For an internal development it is possible to use *Self-Signed Authenticode Certificates*, the generation of which is
covered in the following section.

Self-Signed Authenticode Certificates
=====================================

PowerShell Generating, Installing and Using a Self-Signed Certificate
---------------------------------------------------------------------

This section stolen from `Adam the Automator <https://adamtheautomator.com>`_ articles below, demonstrates
using PowerShell ``New-SelfSignedCertificate``, which supports stores **cert:\CurrentUser\My** or **cert:\LocalMachine\My**.

* `New-SelfSignedCertificate: Creating Certificates with PowerShell <https://adamtheautomator.com/new-selfsignedcertificate/>`_
* `How to Sign PowerShell Script (And Effectively Run It) <https://adamtheautomator.com/how-to-sign-powershell-script/>`_

Self-Signed Certificates Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requires creating the following certificates using a ``PowerShell`` in *Administrative mode*.

* **LocalMachine\\My Personal** - public/private key and certificate for signing;
* **LocalMachine\\Root** - certificate for authentication;
* **LocalMachine\\TrustedPublisher** - certificate for authentication;

.. code-block:: pwsh-session

    # Certificate Manager tools
    PS> C:\Windows\system32\certmgr.msc # Current User
    PS> C:\Windows\system32\certlm.msc  # Local Machine
    PS> C:\Windows\system32\mmc.exe     # MMC tool

    PS-ADM> Get-ExecutionPolicy -List
            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser    RemoteSigned
     LocalMachine       Undefined

    PS-ADM> $authenticode = New-SelfSignedCertificate -Subject "ATA Authenticode" -CertStoreLocation Cert:\LocalMachine\My -Type CodeSigningCert

    # Add the self-signed Authenticode to LocalMachine\Root certificate store
    PS-ADM> $rootStore = [System.Security.Cryptography.X509Certificates.X509Store]::new("Root","LocalMachine")
    PS-ADM> $rootStore.Open("ReadWrite")             ## Open LocalMachine\Root certificate store for read/write
    PS-ADM> $rootStore.Add($authenticode)            ## Add the certificate stored in the $authenticode variable.
    PS-ADM> $rootStore.Close()                       ## Close the root certificate store.

    # Add the self-signed Authenticode to LocalMachine\TrustedPublisher certificate store.
    PS-ADM> $publisherStore = [System.Security.Cryptography.X509Certificates.X509Store]::new("TrustedPublisher","LocalMachine")
    PS-ADM> $publisherStore.Open("ReadWrite")        ## Open LocalMachine\TrustedPublisher certificate store for read/write
    PS-ADM> $publisherStore.Add($authenticode)       ## Add the certificate stored in the $authenticode variable.
    PS-ADM> $publisherStore.Close()                  ## Close the TrustedPublisher certificate store.

    # Verify all certificates are created and the Thumbprint same
    PS-ADM> Get-ChildItem Cert:\LocalMachine\My | Where-Object {$_.Subject -eq "CN=ATA Authenticode"}
       PSParentPath: Microsoft.PowerShell.Security\Certificate::LocalMachine\My
    Thumbprint                                Subject
    ----------                                -------
    F71A096EFCDC99DFAC109A228565B427B66DF49F  CN=ATA Authenticode

    PS-ADM> Get-ChildItem Cert:\LocalMachine\Root | Where-Object {$_.Subject -eq "CN=ATA Authenticode"}
       PSParentPath: Microsoft.PowerShell.Security\Certificate::LocalMachine\Root
    Thumbprint                                Subject
    ----------                                -------
    F71A096EFCDC99DFAC109A228565B427B66DF49F  CN=ATA Authenticode

    PS-ADM> Get-ChildItem Cert:\LocalMachine\TrustedPublisher | Where-Object {$_.Subject -eq "CN=ATA Authenticode"}
       PSParentPath: Microsoft.PowerShell.Security\Certificate::LocalMachine\TrustedPublisher
    Thumbprint                                Subject
    ----------                                -------
    F71A096EFCDC99DFAC109A228565B427B66DF49F  CN=ATA Authenticode


Using the Authenticode, Signing and Running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: pwsh-session

    # Enforce AllSigned, select '[A] Yes to All' option
    PS-ADM> set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
    PS-ADM> set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope LocalMachine

    PS-ADM> PS C:\Users\geoff> Get-ExecutionPolicy -List
            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser       AllSigned
     LocalMachine       AllSigned

    # Get the *ATA Authenticode*
    PS-ADM> $codeCertificate = Get-ChildItem Cert:\LocalMachine\My | Where-Object {$_.Subject -eq "CN=ATA Authenticode"}

    PS C:\> Get-Content C:\Users\sjfke\hello-world.ps1
    #requires -version 4
    Set-StrictMode -Version 2
    write-host 'host: hello world!'
    write-output 'output: hello world!'
    exit(0)

    PS-ADM> Set-AuthenticodeSignature -FilePath C:\Users\sjfke\hello-world.ps1  -Certificate $codeCertificate
    # Appends a signature, makes it immutable, any changes require Set-AuthenticodeSignature again.
    PS C:\> Get-Content C:\Users\sjfke\hello-world.ps1
    #requires -version 4
    Set-StrictMode -Version 2
    write-host 'host: hello world!'
    write-output 'output: hello world!'
    exit(0)
    # SIG # Begin signature block
    <-- text-removed -->
    # SIG # End signature block

    PS-ADM> C:\Users\sjfke\hello-world.ps1
    host: hello world!
    output: hello world!

    PS> C:\Users\sjfke\hello-world.ps1
    host: hello world!
    output: hello world!

Adding a TimeStampServer should ensure that your code will not expire when the signing certificate expires.

.. code-block:: pwsh-session

    PS-ADM> Set-AuthenticodeSignature -FilePath C:\Users\sjfke\hello-world.ps1  -Certificate $codeCertificate -TimeStampServer http://timestamp.digicert.com
    # Freely available TimeStampServers
    - http://timestamp.digicert.com
    - http://timestamp.comodoca.com
    - http://timestamp.globalsign.com
    - http://tsa.starfieldtech.com
    - http://timestamp.entrust.net/TSS/RFC3161sha2TS
    - http://sha256timestamp.ws.symantec.com/sha256/timestamp
    - http://tsa.swisssign.net

OpenSSL: Generating, Installing and Using a Self-Signed Certificate
-------------------------------------------------------------------

In `PowerShell Generating, Installing and Using a Self-Signed Certificate`_ the sequence is:

1. Generate *ata-authenticode* (certificate, private key) in certificate store,  **LocalMachine\\My**
2. Import *ata-authenticode* into certificate store **LocalMachine\\Root** for authentication;
#. Import *ata-authenticode* into certificate store **LocalMachine\\TrustedPublisher** for authentication;

OpenSSL uses the *CurrentUser Execution Policy Scope*, with the same sequence and requires a few more steps

1. Generate *atb-authenticode* (certificate, private key) in certificate store,  **CurrentUser\\My**
    a. Generate *atb-authenticode.key* and *atb-authenticode.csr*
    b. Generate self-signed *atb-authenticode.crt*
    #. Merge *atb-authenticode.crt* *and authenticode.key* into *authenticode.pfx*
    #. Import *authenticode.pfx* into certificate store **CurrentUser\\My**
2.  Import *authenticode.pfx* into certificate store **CurrentUser\\Root** for authentication;
#.  Import *authenticode.pfx* into certificate store **CurrentUser\\TrustedPublisher** for authentication;

The following was done using `Git Bash shell <https://gitforwindows.org/>`_ but the of *atb-authenticode* could
be built on any system with OpenSSL because all that is needed is the ``authenticode.pfx`` file.

An explicit OpenSSL configuration file, ``authenticode-selfsign-openssl.cnf`` is used to avoid issues resulting from
differences in the default configuration in the OpenSSL installation.

OpenSSL: Self-Signed Certificates Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    Step 1a - generate atb-authenticode.key and atb-authenticode.csr
    $ openssl req -new -newkey rsa:2048 -nodes -keyout authenticode.key -out authenticode.csr -config authenticode-selfsign-openssl.cnf
    Generating a RSA private key
    ......................................................+++++
    .....................................................+++++
    writing new private key to 'authenticode.key'
    -----
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [CH]:.
    State or Province Name (full name) [Zurich]:.
    Locality Name (eg, city) [Zurich]:.
    Organization Name (eg, company) [Highly Dubious Inc]:.
    Organizational Unit Name (eg, section) []:.
    Common Name (eg, YOUR name) [HighlyDubious]:ATB Authenticode
    Email Address []:.

.. code-block:: bash

    Step 1b - generate self-signed atb-authenticode.crt
    # Note options: -extensions v3_req -extfile authenticode-selfsign-openssl.cnf
    $ openssl x509 -req -extensions v3_req -extfile authenticode-selfsign-openssl.cnf -days 366 -in authenticode.csr -signkey authenticode.key -out authenticode.crt
    Signature ok                                                                                                                                               .
    subject=CN = ATB Authenticode
    Getting Private key

    # Check the certificate for the following section
    $ openssl x509 -noout -text -in authenticode.crt | less
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Subject Key Identifier:
                39:04:14:30:74:B8:00:51:2F:30:11:E6:D3:D5:FF:A9:3B:2A:21:53
            X509v3 Extended Key Usage: critical
                Code Signing, Microsoft Individual Code Signing

.. code-block:: bash

    Step 1c - merge atb-authenticode.crt and authenticode.key -into- authenticode.pfx
    Note: an empty password can be used
    $ openssl pkcs12 -export -out authenticode.pfx -inkey authenticode.key -in authenticode.crt
    Enter Export Password:
    Verifying - Enter Export Password:

The next few steps involve importing the ``authenticode.pfx`` into the Windows certificate store, unlike
`PowerShell Generating, Installing and Using a Self-Signed Certificate`_ it uses *CurrentUser\\My*, *CurrentUser\\Root* and
*CurrentUser\\TrustedPublisher*.

.. code-block:: pwsh-session

    # Certificate Manager tools
    PS1> C:\Windows\system32\certmgr.msc # Current User
    PS1> or C:\Windows\system32\mmc.exe  # MMC tool

    Step 1d - import authenticode.pfx -into- CurrentUser\My
    Step 2  - import authenticode.pfx -into- CurrentUser\Root - certificate trust/authentication;
    Step 3  - import authenticode.pfx -into- CurrentUser\TrustedPublisher - certificate for trust/authentication;


OpenSSL: Using the Authenticode, Signing and Running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requires using a ``PowerShell`` in *Administrative mode* to execute ``set-ExecutionPolicy`` commands, prompt ``PS-ADM>``
and a normal ``PowerShell``, prompt ``PS1>`` for the rest.

.. code-block:: pwsh-session

    # Enforce AllSigned, select '[A] Yes to All' option
    PS-ADM> set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
    PS-ADM> set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope LocalMachine

    PS-ADM> PS C:\Users\sjfke> Get-ExecutionPolicy -List
            Scope ExecutionPolicy
            ----- ---------------
    MachinePolicy       Undefined
       UserPolicy       Undefined
          Process       Undefined
      CurrentUser       AllSigned
     LocalMachine       AllSigned

.. code-block:: pwsh-session

    PS1> Get-Content -Path C:\Users\sjfke\hello-world.ps1
    #requires -version 4
    Set-StrictMode -Version 2
    write-host 'host: hello world!'
    write-output 'output: hello world!'
    exit(0)

    PS1> Get-ChildItem Cert:\CurrentUser\My | Where-Object {$_.Subject -eq "CN=ATB Authenticode"}
    PSParentPath: Microsoft.PowerShell.Security\Certificate::CurrentUser\My
    Thumbprint                                Subject
    ----------                                -------
    A6567CF9C6D5B0DCE4B7823B3DAF4CC4058DB396  CN=ATB Authenticode

    PS1> $codeCertificate = Get-ChildItem Cert:\CurrentUser\My | Where-Object {$_.Subject -eq "CN=ATB Authenticode"}
    PS1> Set-AuthenticodeSignature -FilePath C:\Users\sjfke\hello-world.ps1 -Certificate $codeCertificate
    Directory: C:\Users\geoff
    SignerCertificate                         Status                                                                    Path
    -----------------                         ------                                                                    ----
    A6567CF9C6D5B0DCE4B7823B3DAF4CC4058DB396  Valid                                                                     hello-world.ps1

    PS1> C:\Users\sjfke\hello-world.ps1
    host: hello world!
    output: hello world!

    PS1> Get-Content -Path C:\Users\sjfke\hello-world.ps1
    #requires -version 4
    Set-StrictMode -Version 2
    write-host 'host: hello world!'
    write-output 'output: hello world!'
    exit(0)

    # SIG # Begin signature block
    # MIIFhQYJKoZIhvcNAQcCoIIFdjCCBXICAQExCzAJBgUrDgMCGgUAMGkGCisGAQQB
    <-- text-removed -->
    # dtUw8zNoZUTIq1eKdNJW+kxdDRPL56l3qQ==
    # SIG # End signature block

OpenSSL file: authenticode-selfsign-openssl.cnf
-----------------------------------------------

This is the result of many iterations and consulting many references, most relevant being:

* `OpenSSL Cookbook - 3rd Edition by Ivan Ristic <https://www.feistyduck.com/library/openssl-cookbook/online/>`_
* `openssl-req, req - PKCS#10 certificate request and certificate generating utility <https://docs.openssl.org/1.1.1/man1/req/>`_
* `openssl-x509 - Certificate display and signing command <https://docs.openssl.org/master/man1/openssl-x509/>`_
* `x509v3_config - X509 V3 certificate extension configuration format <https://docs.openssl.org/3.0/man5/x509v3_config/>`_ v3_req, v3_ca
* `openssl-pkcs12 - PKCS#12 file command <https://docs.openssl.org/master/man1/openssl-pkcs12/>`_

.. code-block:: ini

    ####################################################################
    # CA Definition
    [ ca ]
    default_ca      = CA_default            # The default ca section

    [ CA_default ]

    dir             = .                      # Where everything is kept
    certs           = $dir/certsdb           # Where the issued certs are kept
    new_certs_dir   = $certs                 # default place for new certs.
    database        = $dir/index.txt         # database index file.
    certificate     = $dir/cacert.pem        # The CA certificate
    private_key     = $dir/private/cakey.pem # The private key
    serial          = $dir/serial            # The current serial number
    RANDFILE        = $dir/private/.rand     # private random number file
    default_days    = 365                    # how long to certify for
    default_md      = sha256                 # which md to use.
    preserve        = no                     # keep passed DN ordering
    email_in_dn  = no
    policy          = policy_match
    crldir          = $dir/crl
    crlnumber       = $dir/crlnumber         # the current crl number
    crl             = $crldir/crl.pem        # The current CRL
    #crl_extensions        = crl_ext
    default_crl_days= 30                    # how long before next CRL

    ####################################################################
    # The default policy for the CA when signing requests
    [ policy_match ]
    countryName             = match         # Must be the same as the CA
    stateOrProvinceName     = match         # Must be the same as the CA
    organizationName        = match         # Must be the same as the CA
    organizationalUnitName  = optional      # not required
    commonName              = supplied      # must be there, whatever it is
    emailAddress            = optional      # not required

    ####################################################################
    # This is where we define how to generate CSRs
    [ req ]
    default_bits            = 2048
    default_keyfile         = privkey.pem
    default_md              = sha256                 # which md to use.
    # prompt = no
    distinguished_name      = req_distinguished_name # where to get DN for reqs
    attributes              = req_attributes         # req attributes
    string_mask             = nombstr
    # string_mask             = utf8only
    req_extensions          = v3_req        # The extensions to add to req's
    x509_extensions         = v3_ca         # The extentions to add to self signed certs

    [ req_distinguished_name ]
    countryName                     = Country Name (2 letter code)
    countryName_default             = CH
    countryName_min                 = 2
    countryName_max                 = 2
    stateOrProvinceName             = State or Province Name (full name)
    stateOrProvinceName_default     = Zurich
    localityName                    = Locality Name (eg, city)
    localityName_default            = Zurich
    0.organizationName              = Organization Name (eg, company)
    0.organizationName_default      = Highly Dubious Inc
    organizationalUnitName          = Organizational Unit Name (eg, section)
    1.commonName                    = Common Name (eg, YOUR name)
    1.commonName_default            = HighlyDubious
    1.commonName_max                = 64
    emailAddress                    = Email Address
    emailAddress_max                = 64

    ####################################################################
    # We don't want these, but the section must exist
    [ req_attributes ]
    #challengePassword              = A challenge password
    #challengePassword_min          = 4
    #challengePassword_max          = 20
    #unstructuredName               = An optional company name

    ####################################################################
    # Extension for requests
    [ v3_req ]
    basicConstraints=critical,CA:FALSE
    subjectKeyIdentifier = hash
    #subjectAltName      = @alternate_names
    # * ATA Authenticate - Code Signing (1.3.6.1.5.5.7.3.3)
    # * extendedKeyUsage=critical,codeSigning,1.3.6.1.5.5.7.3.3
    extendedKeyUsage=critical,codeSigning,msCodeInd

    ####################################################################
    # Convert a certificate request into a self signed certificate using extensions for a CA:
    # https://www.openssl.org/docs/man1.1.1/man1/x509.html
    [ v3_ca ]
    #subjectAltName        = @alternate_names
    # * ATA Authenticate - Code Signing (1.3.6.1.5.5.7.3.3)
    # * extendedKeyUsage=critical,codeSigning,1.3.6.1.5.5.7.3.3
    extendedKeyUsage=critical,codeSigning,msCodeInd
    subjectKeyIdentifier   = hash
    authorityKeyIdentifier = keyid:always,issuer

    #[alternate_names]
