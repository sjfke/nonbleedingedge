:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/python.rst

#################
Python Cheatsheet
#################

.. important:: Python-3 only, with an emphasis on using Python as a shell-scripting language.

**********
Background
**********

`Python <https://www.python.org/>`_ has had a long history, and has accumulated a lot of *new features*,
*incompatibilities* and *tech-debt* over the years which can make learning the language complex and confusing.
This is a brief summary of the Python version history derived from the
`Python Wiki page <https://en.wikipedia.org/wiki/Python_(programming_language)>`_.

* Python 0.9.0 was released in 1991.
* Python 2.0 was released in 2000, with last release being Python 2.7.18 released in 2020.
* Python 3.0 was released in 2008, this major revision is not completely backward-compatible.
* Currently only Python 3.9 and later are supported.

In 2021, Python 3.9.2 and 3.8.8 were expedited as all versions of Python (including 2.7) had security issues leading
to possible remote code execution and web cache poisoning.

In 2022, Python 3.7.13, 3.8.13, 3.9.12 and 3.10.4 were expedited, because of many security issues.
Python 3.9.13 was released in May 2022, but it was announced that the 3.9 series, like the 3.8 and 3.7 series would
only receive security fixes in the future

On September 7, 2022, four new releases were made due to a potential denial-of-service attack: 3.10.7, 3.9.14, 3.8.14,
and 3.7.14.

As of November 2024, Python 3.12 and 3.13 are bug-fixed releases, with 3.9, 3.10 and 3.11 security fixes only.

* `Python Developers Guide - Supported versions <https://devguide.python.org/versions/>`_

Python on Linux
===============

Almost all distributions provide Python by default.

Python on Windows
=================

The author is using Python from the `Microsoft Store <https://apps.microsoft.com/store/apps>`_

* `Python - Using Python on Windows <https://docs.python.org/3/using/windows.html>`_
* `Microsoft - Get started using Python on Windows for beginners <https://learn.microsoft.com/en-us/windows/python/beginners>`_
* `Microsoft - Get started using Python for web development on Windows <https://learn.microsoft.com/en-us/windows/python/web-frameworks>`_
* `Microsoft Store - Python 3.13 <https://apps.microsoft.com/detail/9pnrbtzxmb4z>`_
* `Microsoft Store - Python 3.12 <https://apps.microsoft.com/detail/9ncvdn91xzqp>`_
* `Microsoft Store - Python 3.11 <https://apps.microsoft.com/detail/9nrwmjp3717k>`_
* `Anaconda offers the easiest way to perform Python/R data science <https://www.anaconda.com/>`_
* `RealPython - Your Python Coding Environment on Windows: Setup Guide <https://realpython.com/python-coding-setup-windows/>`_

Choosing which installed version to run, is controlled with *App Execution Aliases*

.. code-block:: console

    1. Press "Windows + I" and select "Apps > Advanced app settings";
    2. Under "Choose where to get apps", change the selection to the desired one

If that fails, try:

    * `How to manage App Execution Aliases on Windows 11/10 <https://www.thewindowsclub.com/manage-app-execution-aliases-on-windows-10>`_

*********************
Example Python Script
*********************

An overly simple example, `flintstones.py <https://github.com/sjfke/python-projects/blob/main/flintstones.py>`_

.. code-block:: python

    import argparse
    import sys

    # https://docs.python.org/3/howto/argparse.html
    _dict = {'Fred': 30, 'Wilma': 25, 'Pebbles': 1, 'Dino': 5}


    def get_names() -> list[str]:
        """
        Get Flintstones family firstnames
        :return: list of names
        """
        return list(_dict.keys())


    def get_ages() -> list[int]:
        """
        Get Flintstones family ages
        :return: list of ages
        """
        return list(_dict.values())


    def get_person(name: str = None) -> (dict[str,int] | None):
        """
        Get age of Flintstones family member
        :param name: firstname
        :return: integer age or None
        """
        if name is not None:

            try:
                _ans = {name: _dict[name]}
                return _ans
            except KeyError:
                print(f"KeyError: {name} not found", file=sys.stderr)
                # print("KeyError: {0} not found".format(name))  # prior to Python 3.6
                return None
        else:
            return None


    if __name__ == '__main__':
        arguments = None
        parser = argparse.ArgumentParser(description='Simple Command Line Application')
        parser.add_argument('-n', '--names', action='store_true', default=False, help='display names')
        parser.add_argument('-a', '--ages', action='store_true', default=False, help='display ages')
        parser.add_argument('-p', '--person', type=str, default=None, help='display person age')
        parser.add_argument('-v', '--verbose', action='count', default=0)

        args = parser.parse_args()

        if args.verbose >= 1:
            print(f"args: {args.__str__()}")

        if args.names:
            print(f"{get_names()}")
        elif args.ages:
            print(f"{get_ages()}")
        elif args.person:
            print(f"{get_person(name=args.person)}")
        else:
            parser.print_help()

        sys.exit(0)

While certain statements must occur in the correct sequence, many do not, for example the `import` can appear at
various places. The above format is a good basis for starting:

    * Import the required modules, ``import``
    * Define the functions, ``def``
    * Define the main block, ``if __name__ == '__main__':``
    * Main block, instantiate the ArgumentParser
    * Main block, process the command line input, calling the required functions

Notice the script has to be executed as ``python <script-name>``, see :ref:`using-shebang`.

Function definitions
    Can have *default* arguments values, optional in the function call.

Function calls
    Support *named* and *positional* arguments.

The ``Docstrings``, the text between the *triple double-quotes* after the function definition, are important but
no single agreed format is in use and style varies considerably, see :ref:`python-docstrings`. For consistency the
`PyCharm Community Edition <https://www.jetbrains.com/pycharm/download>`_ Docstrings are used throughout this document.

Example usage

.. code-block:: shell-session

    $ python .\flintstones.py
    usage: flintstones.py [-h] [-n] [-a] [-p PERSON] [-v]

    Simple Command Line Application

    options:
      -h, --help           show this help message and exit
      -n, --names          display names
      -a, --ages           display ages
      -p, --person PERSON  display person age
      -v, --verbose

    $ python .\flintstones.py -n
    ['Fred', 'Wilma', 'Pebbles', 'Dino']

Other simple `argparse` examples are available on `GitHub (sjfke): Python Projects <https://github.com/sjfke/python-projects>`_ :

* `Kitten: Simplistic version of the UNIX cat command <https://github.com/sjfke/python-projects/blob/main/kitten.py>`_
* `Jinja-CLI: Application for using Jinja templates <https://github.com/sjfke/python-projects/blob/main/jinja-cli.py>`_
* `Simple-CLI: Argparse example writing to a file <https://github.com/sjfke/python-projects/blob/main/simple-cli.py>`_

None of these examples include :ref:`python-logging` and probably should.

.. _python-docstrings:

Python Docstrings
=================

Docstrings are covered in `PEP 257 – Docstring Conventions <https://peps.python.org/pep-0257/>`_ and provide the text
for the built-in ``help()`` function.
The top 3 Docstring styles being, *Sphinx*, *Google* and *Numpydoc*, the *Example Python Script* is using *Sphinx*

* `Sphinx: Writing docstrings <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>`_
* `Sphinx: Example on how to document your Python docstrings <https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html>`_
* `Google: Python Style Guide - Docstrings <https://google.github.io/styleguide/pyguide.html#s3.8.1-comments-in-doc-strings>`_
* `Numpydoc Example <https://numpydoc.readthedocs.io/en/latest/example.html>`_

Other references:

* `Documenting Python Code: A Complete Guide <https://realpython.com/documenting-python-code/>`_
* `JetBrains PyCharm: Creating documentation comments for Python functions <https://www.jetbrains.com/help/pycharm/creating-documentation-comments.html>`_
* `VSCode: autoDocstring - Python Docstring Generator <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`_
* `Python Basics: Using docstrings to document functions <https://www.pythontutorial.net/python-basics/python-function-docstrings/>`_

.. _python-logging:

Python Logging
==============

.. code-block:: python

    import logging
    logging.basicConfig(level=logging.INFO)

    logging.info('This message will be logged')       # INFO:root:This message will be logged
    logging.debug('This message will not be logged')

.. code-block:: python

    import logging
    logging.basicConfig(filename='myfirstlog.log', level=logging.DEBUG,
        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

    logging.warning('Testing log formatting!')

.. code-block:: shell-session

    $ cat .\myfirstlog.log
    2023-02-09 20:23:28,339 | root | WARNING | Testing log formatting!

* `Python: Logging HOWTO <https://docs.python.org/3/howto/logging.html>`_
* `6 Python Logging Best Practices You Should Be Aware Of <https://www.loggly.com/use-cases/6-python-logging-best-practices-you-should-be-aware-of/>`_
* `The Hitchhikers Guide to Python: Logging <https://docs.python-guide.org/writing/logging/>`_

.. _module-import:

Module Import
=============

Importing from sub-directories
------------------------------

For illustration the file `Fact.py` which contains a method called `Fact` is copied into different folders.

.. code-block:: dosbatch

    C:\USERS\FACTORIAL
    │   fact-test.py
    │   Fact.py
    │
    └───subdir
        │   Fact.py
        │
        └───subdir
                Fact.py

.. code-block:: shell-session

    $ cat Fact.py
    def Fact(n):
        return 1 if n == 1 else n * Fact(n-1)

.. code-block:: python

    >>> help('modules')                                 # list all modules
    >>> import random                                   # module in sys.path (List) and sys.modules (Dictionary)
    >>> from sys import exit                            # so exit() and not sys.exit(), module in (sys.path, sys.modules)
    >>> dir()                                           # list local namespace, notice 'exit' and 'random'
    ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
     '__package__', '__spec__', 'exit', 'random']

    >>> dir(random)
    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE',
     '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
     '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs',
     '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_parse_args', '_pi',
     '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', 'betavariate',
     'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate',
     'lognormvariate', 'main', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange',
     'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
    >>>

    >>> from Fact import Fact                               # file './fact.py'
    >>> from subdir.Fact import Fact as sub_fact            # file './subdir/Fact.py' as 'sub_fact'
    >>> from subdir.subdir.Fact import Fact as sub_sub_fact # file './subdir/subdir/fact.py' as 'sub_sub_fact'
    >>> from Fact import Fact as factorial                  # file './fact.py' as factorial

    >>> n = random.randrange(1,10,1)
    >>> answer = Fact(n)
    >>> print(f"fact({n}) = {answer}")                      # fact(3) = 6
    >>>
    >>> answer = sub_fact(n)
    >>> print(f"sub_fact({n}) = {answer}")                  # sub_fact(3) = 6
    >>>
    >>> answer = sub_sub_fact(n)
    >>> print(f"sub_sub_fact({n}) = {answer}")              # sub_sub_fact(3) = 6
    >>>
    >>> answer = factorial(n)
    >>> print(f"factorial({n}) = {answer}")                 # factorial(3) = 6

Importing a filename with '-'
-----------------------------

`Python-3.1` introduced an `importlib` module to handle this for the current directory and it's sub-directories.

.. code-block:: python

    >>> import ok_file_name
    >>>
    >>> import importlib
    >>> bad_file_name = importlib.import_module("bad-file-name")
    >>>
    >>> bad_path_name = importlib.import_module("bad-sub-folder.bad-file-name")
    >>> dir()
    ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'importlib', 'bad_path_name', 'bad_file_name', 'ok_file_name']


Import from a parent directory
------------------------------

The parent directory needs to be added to the `PYTHONPATH`

.. code-block:: python

    >>> import sys
    >>> import os
    >>> sys.path.append(os.getcwd() + '/..')

    >>> import ok_parent_filename
    >>>
    >>> import importlib
    >>> bad_parent_filename = importlib.import_module("bad-parent-filename")

    >>> dir()
    ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'sys', 'importlib', 'bad_parent_filename', 'ok_parent_filename']


.. _using-shebang:

Using Shebang with Python
=========================

On ``UNIX`` and ``Linux`` systems it is common to have a ``shebang`` as the first line of the the script, so the
Shell knows which interpreter to use.

.. code-block:: bash

    #!/bin/bash           # execute using bash
    #!/usr/bin/python     # interpreter /usr/bin/python (default Python)
    #!/usr/bin/python3    # interpreter /usr/bin/python3

    #!/usr/bin/env python # search and execute Python interpreter found

Windows does not support ``shebang``, so the it is omitted from the examples, see also:

* `Why is it better to use "#!/usr/bin/env NAME" instead of "#!/path/to/NAME" as my shebang? <https://unix.stackexchange.com/questions/29608/why-is-it-better-to-use-usr-bin-env-name-instead-of-path-to-name-as-my>`_

Print to stderr and stdout
==========================

From `sys — System-specific parameters and functions <https://docs.python.org/3/library/sys.html>`_
    `sys.stdin`, `sys.stdout`, `sys.stderr`, file objects used for standard input, output and errors.

.. code-block:: python

    import sys

    a = 'fred'
    print(f"hello, {a}")                  # 'hello, fred' (stdout)
    print(f"hello, {a}", file=sys.stdout) # 'hello, fred' (stdout)
    print(f"hello, {a}", file=sys.stderr) # 'hello, fred' (stderr)

*********************
Object Class Examples
*********************

``Python`` objects do not support `encapsulation <https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)>`_
or **static type checking** unlike many object-oriented programming languages.

* It is possible to indicate that data is not intended to be modified by prefixing a variable with ``_`` (underscore) or ``__`` (double underscore).
* A constant value is indicated making it **UPPERCASE** which can optionally be prefixed with ``_`` (underscore) or ``__`` (double underscore) but this does not prevent it from being updated.
* By convention ``getter`` and ``setter`` methods are discouraged, if needed see :ref:`person-object-with-attributes`.

It is recommended that `mypy <https://www.mypy-lang.org/>`_ is used to check for **encapsulation violations** and
**static typing** because the ``Python`` language does not enforce it.

The following examples attempt to cover the most common approaches:

* :ref:`simple-person-object`
* :ref:`person-object-with-attributes`
* :ref:`person-object-with-decorators`

With the ``Simple`` being the easiest and ``Decorator`` method being the cleanest.

.. _simple-person-object:

Simple Person Object
====================

This is the *simplest way** way to declare objects, the ``properties`` (or ``attributes``) are accessed directly and
there are no ``getter`` or ``setter`` methods.

.. code-block:: python

    from typing import ClassVar
    import uuid


    class Person:
        GENDER: ClassVar[set] = {'M', 'F', 'N', 'Male', 'Female', 'Neuter'}

        def __init__(self, name: str, age: int, sex: str = 'M') -> None:
            """
            Create person object
            :param name: of person, (str)
            :param age: of person (int)
            :param sex: one of set Gender
            """
            self.name = name

            if not isinstance(age, int):
                raise TypeError(f"Invalid int for age: {age}")
            if not isinstance(sex, str):
                raise TypeError(f"Invalid str for sex: {sex}")

            if age > 150 or age < 0:
                raise ValueError(f"Invalid age: {age}")
            else:
                self.age = age

            if sex in Person.GENDER:
                self.sex = sex
            else:
                raise ValueError(f"Invalid Gender: {sex}")

            self._uuid1 = str(uuid.uuid1())
            self.__uuid4 = str(uuid.uuid4())

        def __str__(self) -> str:
            """
            String representation
            :return: human-readable representation (str)
            """
            __str = 'Person: '
            __str += str(self.name) + ', '
            __str += str(self.age) + ', '
            __str += str(self.sex) + ', '
            __str += str(self._uuid1) + ', '
            __str += str(self.__uuid4)
            return __str

        def __repr__(self) -> str:
            """
            repr() string representation
            :return: programmatic representation (JSON string)
            """
            __str = "{"
            __str += f"'name': '{self.name}', "
            __str += f"'age': '{self.age}', "
            __str += f"'sex': '{self.sex}', "
            __str += f"'_uuid1': '{self._uuid1}', "
            __str += f"'__uuid4': '{self.__uuid4}'"
            __str += "}"
            return __str


.. code-block:: python

    >>> from Person_Simple import Person

    # Can change the value of GENDER constant
    >>> Person.GENDER                      # {'M', 'F', 'Female', 'N', 'Neuter', 'Male'}
    >>> Person.GENDER.add('Non-Binary')    # {'Non-Binary', 'M', 'F', 'Female', 'N', 'Neuter', 'Male'}
    >>> Person.GENDER.remove('Non-Binary') # {'Female', 'Neuter', 'Male', 'N', 'M', 'F'}

    # Typical operations
    >>> fred = Person('Fred', 35)
    >>> fred.name     # 'Fred'
    >>> str(fred)     # 'Person: Fred, 35, M, 248b33a7-f2b1-11ef-bbc7-58961dcb95f2, 6131de2c-5b7a-4a35-b63a-cca6bf83c440'
    >>> repr(fred)    # "{'name': Fred, 'age': '35', 'sex': 'M', '_uuid1': '248b33a7-f2b1-11ef-bbc7-58961dcb95f2', '__uuid4': '6131de2c-5b7a-4a35-b63a-cca6bf83c440'}"
    >>> fred.age      # 35
    >>> fred.age = 36 # 36
    >>> repr(fred)    # "{'name': Fred, 'age': '36', 'sex': 'M', '_uuid1': '248b33a7-f2b1-11ef-bbc7-58961dcb95f2', '__uuid4': '6131de2c-5b7a-4a35-b63a-cca6bf83c440'}"

    # BUT can change the value of '_uuid1' to make it inconsistent
    >>> import uuid
    >>> fred._uuid1                     # '248b33a7-f2b1-11ef-bbc7-58961dcb95f2'
    >>> fred._uuid1 = uuid.uuid1()      # UUID('1d8d3b9e-f2b6-11ef-9664-58961dcb95f2')
    >>> fred._uuid1 = str(uuid.uuid1()) # '2d13a040-f2b6-11ef-9482-58961dcb95f2'
    >>> repr(fred)    # "{'name': 'Fred', 'age': '36', 'sex': 'M', '_uuid1': '2d13a040-f2b6-11ef-9482-58961dcb95f2', '__uuid4': '6131de2c-5b7a-4a35-b63a-cca6bf83c440'}"

    # BUT can change the value of '__uuid4' AFTER it has been updated to make it inconsistent
    >>> fred.__uuid4                     # AttributeError: 'Person' object has no attribute '__uuid4'. Did you mean: '_uuid1'?
    >>> fred.__uuid4 = str(uuid.uuid4())
    >>> fred.__uuid4                     # '2ebfda94-abdc-4a52-b170-4f03476cf6fa'
    # NOTICE '__uuid4' NOW has TWO values, the old and the new
    >>> repr(fred)  # "{'name': Fred, 'age': '36', 'sex': 'M', '_uuid1': '2d13a040-f2b6-11ef-9482-58961dcb95f2', '__uuid4': '6131de2c-5b7a-4a35-b63a-cca6bf83c440'}"


The above example is a very simple ``Person`` object, **BUT** clearly indicates **BE CAREFUL** to manually adhere
to the intended encapsulation, but is short and simple and without ``setter``, ``getter`` methods.

Two other approaches are shown using `property() <https://realpython.com/ref/builtin-functions/property/>`_ which adds managed
*attributes*, also known as **properties** and using Python ``decorators``.

.. _person-object-with-attributes:

Person Object with Attributes
=============================

.. code-block:: python

    from typing import ClassVar
    import uuid


    class Person:
        GENDER: ClassVar[set] = {'M', 'F', 'N', 'Male', 'Female', 'Neuter'}

        def __init__(self, name: str, age: int, sex: str = 'M') -> None:
            """
            Create person object
            :param name: of person, (str)
            :param age: of person (int)
            :param sex: one of set Gender
            """
            self.__name = name

            if not isinstance(age, int):
                raise TypeError(f"Invalid int for age: {age}")
            if not isinstance(sex, str):
                raise TypeError(f"Invalid str for sex: {sex}")

            if age > 150 or age < 0:
                raise ValueError(f"Invalid age: {age}")
            else:
                self.__age = age

            if sex in Person.GENDER:
                self.__sex = sex
            else:
                raise ValueError(f"Invalid Gender: {sex}")

            self.__uuid1 = str(uuid.uuid1())
            self.__uuid4 = str(uuid.uuid4())

        def __get_name(self) -> str:
            """
            Name Getter
            :return: name of person (str)
            """
            return self.__name

        def __set_name(self, value: str) -> None:
            """
            Name Setter
            :param value: new name of person (str)
            :return: None or TypeError
            """
            if not isinstance(value, str):
                raise TypeError(f"Invalid str for name: {value}")
            else:
                self.__name = value

        def __get_age(self) -> int:
            """
            Age Getter
            :return: age of person (int)
            """
            return self.__age

        def __set_age(self, value: int) -> None:
            """
            Age Setter
            :param value: age of person (integer)
            :return: None, TypeError or ValueError
            """

            if not isinstance(value, int):
                raise TypeError(f"Age must be an int: {value}")
            elif value > 150:
                raise ValueError(f"Invalid age: '{value}'")
            elif value > 0:
                self.__age = value
            else:
                self.__age = 0

        def __get_sex(self) -> str:
            """
            Sex (GENDER) Getter
            :return: Person.GENDER
            """
            return self.__sex

        def __set_sex(self, value: str) -> None:
            """
            Sex (GENDER) Setter
            :param value: gender of person (GENDER element)
            :return: None, TypeError or ValueError
            """
            if not isinstance(value, str):
                raise TypeError(f"Sex must be a str: {value}")
            elif value in Person.GENDER:
                self.__sex = value
            else:
                raise ValueError(f"Invalid Gender: {value}")

        def __get_uuid1(self) -> str:
            """
            UUID Getter
            :return: UUID value (string)
            """
            return self.__uuid1

        def __get_uuid4(self) -> str:
            """
            UUID Getter
            :return: UUID value (string)
            """
            return self.__uuid4

        def __str__(self) -> str:
            """
            String representation
            :return: human-readable representation (str)
            """
            __str = 'Person: '
            __str += str(self.__name) + ', '
            __str += str(self.__age) + ', '
            __str += str(self.__sex) + ', '
            __str += str(self.__uuid1) + ', '
            __str += str(self.__uuid4)
            return __str

        def __repr__(self) -> str:
            """
            repr() string representation
            :return: programmatic representation (JSON string)
            """
            __str = "{"
            __str += f"'name': '{self.__name}', "
            __str += f"'age': '{self.__age}', "
            __str += f"'sex': '{self.__sex}', "
            __str += f"'uuid1': '{self.__uuid1}', "
            __str += f"'uuid4': '{self.__uuid4}'"
            __str += "}"
            return __str

        name = property(fget=__get_name, fset=__set_name, fdel=None, doc='Name of Person')
        age = property(fget=__get_age, fset=__set_age, fdel=None, doc='Age of Person')
        sex = property(fget=__get_sex, fset=__set_sex, fdel=None, doc='Gender of Person')
        uuid1 = property(fget=__get_uuid1, fset=None, fdel=None, doc='UUID1 of Person')
        uuid4 = property(fget=__get_uuid4, fset=None, fdel=None, doc='UUID4 of Person')

To make the ``getter`` and ``setter`` methods available remove the ``__`` (double_underscore) prefix in the definitions
and the property statements, for example change ``__get_name`` to ``get_name``.

.. code-block:: python

    >>> from  Person_Attributes import Person

    # Can change the value of GENDER constant
    >>> Person.GENDER                      # {'Female', 'Neuter', 'Male', 'N', 'M', 'F'}
    >>> Person.GENDER.add('Non-Binary')    # {'Female', 'Neuter', 'Non-Binary', 'Male', 'N', 'M', 'F'}
    >>> Person.GENDER.remove('Non-Binary') # {'Female', 'Neuter', 'Male', 'N', 'M', 'F'}

    # Typical operations
    >>> fred = Person('Fred', 35)
    >>> repr(fred)               # "{'name': 'Fred', 'age': '35', 'sex': 'M', 'uuid1': '35b67c72-f469-11ef-bd91-58961dcb95f2', 'uuid4': '00601f5a-ea85-4aab-aeea-9ac1277658de'}"
    >>> fred.name                # 'Fred'
    >>> fred.name = 'Freddy'     # 'Freddy'
    >>> fred.age = 'thirty-five' # TypeError: Age must be an int: thirty-five
    >>> fred.age = 36            # 36
    >>> fred.uuid1               # '35b67c72-f469-11ef-bd91-58961dcb95f2'
    >>> fred.uuid4               # '00601f5a-ea85-4aab-aeea-9ac1277658de'
    >>> repr(fred)               # "{'name': 'Freddy', 'age': '36', 'sex': 'M', 'uuid1': '35b67c72-f469-11ef-bd91-58961dcb95f2', 'uuid4': '00601f5a-ea85-4aab-aeea-9ac1277658de'}"

    # BUT can still mess things up, but that is the 'pythonic' way
    >>> import uuid
    >>> fred.uuid1 = str(uuid.uuid1())   # AttributeError: property 'uuid1' of 'Person' object has no setter
    >>> fred.__uuid1 = str(uuid.uuid1())
    >>> fred.__uuid1                     # 'c07ec018-f46c-11ef-a673-58961dcb95f2'
    >>> fred.uuid1                       # '35b67c72-f469-11ef-bd91-58961dcb95f2'

.. _person-object-with-decorators:

Person Object with Decorators
=============================

.. code-block:: python

    from typing import ClassVar
    import uuid


    class Person:
        GENDER: ClassVar[set] = {'M', 'F', 'N', 'Male', 'Female', 'Neuter'}

        def __init__(self, name: str, age: int, sex: str = 'M') -> None:
            """
            Create person object
            :param name: of person, (str)
            :param age: of person (int)
            :param sex: one of set Gender
            """
            self.__name = name

            if not isinstance(age, int):
                raise TypeError(f"Invalid int for age: {age}")
            if not isinstance(sex, str):
                raise TypeError(f"Invalid str for sex: {sex}")

            if age > 150 or age < 0:
                raise ValueError(f"Invalid age: {age}")
            else:
                self.__age = age

            if sex in Person.GENDER:
                self.__sex = sex
            else:
                raise ValueError(f"Invalid Gender: {sex}")

            self.__uuid1 = str(uuid.uuid1())
            self.__uuid4 = str(uuid.uuid4())

        @property
        def name(self) -> str:
            """
            Name Getter
            :return: name of person (str)
            """
            return self.__name

        @name.setter
        def name(self, value: str) -> None:
            """
            Name Setter
            :param value: new name of person (str)
            :return: None or TypeError
            """
            if not isinstance(value, str):
                raise TypeError(f"Invalid str for name: {value}")
            else:
                self.__name = value

        @property
        def age(self) -> int:
            """
            Age Getter
            :return: age of person (int)
            """
            return self.__age

        @age.setter
        def age(self, value: int) -> None:
            """
            Age Setter
            :param value: age of person (integer)
            :return: None, TypeError or ValueError
            """

            if not isinstance(value, int):
                raise TypeError(f"Age must be an int: {value}")
            elif value > 150:
                raise ValueError(f"Invalid age: '{value}'")
            elif value > 0:
                self.__age = value
            else:
                self.__age = 0

        @property
        def sex(self) -> str:
            """
            Sex (GENDER) Getter
            :return: Person.GENDER
            """
            return self.__sex

        @sex.setter
        def sex(self, value: str) -> None:
            """
            Sex (GENDER) Setter
            :param value: gender of person (GENDER element)
            :return: None, TypeError or ValueError
            """
            if not isinstance(value, str):
                raise TypeError(f"Sex must be a str: {value}")
            elif value in Person.GENDER:
                self.__sex = value
            else:
                raise ValueError(f"Invalid Gender: {value}")

        @property
        def uuid1(self) -> str:
            """
            UUID Getter
            :return: UUID value (string)
            """
            return self.__uuid1

        @property
        def uuid4(self) -> str:
            """
            UUID Getter
            :return: UUID value (string)
            """
            return self.__uuid4

        def __str__(self) -> str:
            """
            String representation
            :return: human-readable representation (str)
            """
            __str = 'Person: '
            __str += str(self.__name) + ', '
            __str += str(self.__age) + ', '
            __str += str(self.__sex) + ', '
            __str += str(self.__uuid1) + ', '
            __str += str(self.__uuid4)
            return __str

        def __repr__(self) -> str:
            """
            repr() string representation
            :return: programmatic representation (JSON string)
            """
            __str = "{"
            __str += f"'name': '{self.__name}', "
            __str += f"'age': '{self.__age}', "
            __str += f"'sex': '{self.__sex}', "
            __str += f"'uuid1': '{self.__uuid1}', "
            __str += f"'uuid4': '{self.__uuid4}'"
            __str += "}"
            return __str


* The ``@property`` decorator must decorate the **getter method**.
* The docstring must go in the **getter method**.
* The **setter and deleter methods** must be decorated with the *"name"* of the getter method plus ``.setter`` and ``.deleter``, respectively.

.. code-block:: python

    >>> from Person_Decorators import Person

    # Can change the value of GENDER constant
    >>> Person.GENDER                      # {'M', 'Female', 'N', 'F', 'Neuter', 'Male'}
    >>> Person.GENDER.add('Non-Binary')    # {'M', 'Female', 'N', 'F', 'Neuter', 'Non-Binary', 'Male'}
    >>> Person.GENDER.remove('Non-Binary') # {'M', 'Female', 'N', 'F', 'Neuter', 'Male'}

    # Typical operations
    >>> fred = Person('Fred', 35)
    >>> repr(fred)                # "{'name': 'Fred', 'age': '35', 'sex': 'M', 'uuid1': 'f4e17619-f50f-11ef-84f8-58961dcb95f2', 'uuid4': '14b3f07c-5e55-4dbe-a48c-428373db619b'}"
    >>> fred.name                 # 'Fred'
    >>> fred.name = 'Freddy'      # 'Freddy'
    >>> fred.get_name()           # AttributeError: 'Person' object has no attribute 'get_name'
    >>> fred.age = 'thirty-five'  # TypeError: Age must be an int: thirty-five
    >>> fred.age = 36             # 36
    >>> fred.uuid1                # 'f4e17619-f50f-11ef-84f8-58961dcb95f2'
    >>> fred.uuid4                # '14b3f07c-5e55-4dbe-a48c-428373db619b'
    >>> repr(fred)                # "{'name': 'Freddy', 'age': '36', 'sex': 'M', 'uuid1': 'f4e17619-f50f-11ef-84f8-58961dcb95f2', 'uuid4': '14b3f07c-5e55-4dbe-a48c-428373db619b'}"

    # BUT can still mess things up, but that is the 'pythonic' way
    >>> import uuid
    >>> fred.uuid1 = str(uuid.uuid1())   # AttributeError: property 'uuid1' of 'Person' object has no setter
    >>> fred.__uuid1 = str(uuid.uuid1()) # 'ce55105f-f510-11ef-847f-58961dcb95f2'
    >>> fred.uuid1                       # 'f4e17619-f50f-11ef-84f8-58961dcb95f2'


*******************
Language Data Types
*******************

Lists
=====

* Mutable
* Ordered collections of arbitrary objects, accessed by offset
* Variable length, heterogeneous, arbitrarily nestable
* `Data Structures: Lists <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>`_
* `Data Structures: Looping techniques <https://docs.python.org/3/tutorial/datastructures.html#looping-techniques>`_

.. code-block:: python

    L1 = []                         # Empty list
    L2 = [0, 1, 2, 3]               # Four items: indexes 0..3
    L3 = ['abc', ['def', 'ghi']]    # Nested lists
    L2[0]                           # 0
    L2[-3]                          # 1
    L3[0][1]                        # 'b'
    L3[1][1]                        # 'ghi'
    L2[0:1]                         # [0]
    L2[0:3]                         # [0, 2, 3]
    L2[2:]                          # [2, 3]
    len(L2)                         # 4
    dir(L3)                         # available methods
    help(L3)                        # description of available methods

    L2 + L3                         # Concatenation -> [0, 1, 2, 3, 'abc', ['def', 'ghi']]
    L2 * 3                          # Repetition -> [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
    for x in L2:                    # Iteration
         print(x)

    3 in L2                         # Membership -> True (False)

    L2.append(7)                    # [0, 1, 2, 3, 7]
    L2.extend([4,5,6])              # [0, 1, 2, 3, 7, 4, 5, 6]
    L2.sort()                       # [0, 1, 2, 3, 4, 5, 6, 7]
    L2.index(4)                     # 4, not 7 because of L2.sort()
    L2.reverse()                    # [7, 6, 5, 4, 3, 2, 1, 0]
    del L2[6]                       # [7, 6, 5, 4, 3, 2, 0]
    del L2[4:6]                     # [7, 6, 5, 4, 0]
    L2.pop()                        # 0, leaving [7, 6, 5, 4]

    L2[2] = 2                       # [7, 2, 2, 4]
    L2[1:2] = [1,3]                 # [7, 1, 3, 2, 4]

    L5 = list(range(4))             # range(0, 4)
    range(0,10)                     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    range(0,10,2)                   # [0, 2, 4, 6, 8]
    range(-5,5)                     # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    range(5,-5,-1)                  # [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

    for x in range(0,4):            # 0, 1, 2, 3, return object (not list) slightly faster
        print(x)

    L4 = [x**2 for x in range(5)]   # [0, 1, 4, 9, 16]

    text = ''.join(map(str, L2))    # '71324', convert List into a string concatenated with ''
    type(L1)                        # <class 'list'>
    type(L3)                        # <class 'list'>
    isinstance(L1, list)            # True, it is a list object
    isinstance(L1, dict)            # False, it is a dict object

Dictionaries
============

* Mutable
* Unordered collections of arbitrary objects, accessed by key
* Variable length, heterogeneous, arbitrarily nestable
* `Data Structures: Dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* `Data Structures: Looping techniques <https://docs.python.org/3/tutorial/datastructures.html#looping-techniques>`_

.. code-block:: python

    D1 = {}                                      # {} Empty dictionary
    D2 = {'email': 'spam', 'total': 3}           # {'email': 'spam', 'total': 3}
    D3 = {'food': {'ham': 2, 'eggs': 3}}         # {'food': {'ham': 2, 'eggs': 3}}
    D2['total']                                  # 3
    D2.get('total')                              # 3
    D3['food']['ham']                            # 2
    D3['food']                                   # {'ham': 2, 'eggs': 3}
    D3['food']['ham'] = 1                        # {'food': {'ham': 1, 'eggs': 3}}

    D3['food']['mushrooms'] = 4                  # {'food': {'ham': 1, 'eggs': 3, 'mushrooms': 4}}
    if 'mushrooms' in D3['food']:                # safe delete using if
         del D3['food']['mushrooms']             # {'food': {'ham': 1, 'eggs': 3}}

    try:                                         # safe delete using try .. except
        del D3['food']['mushrooms']
    except KeyError:
        pass

    'total' in D2                                # True
    'food' in D3                                 # True
    'eggs' in D2                                 # False
    'eggs' in D3['food']                         # True

    D2.keys()                                    # dict_keys(['email', 'total'])
    list(D2.keys())                              # ['email', 'total'],             # <class 'list'>
    D2.values()                                  # dict_values(['spam', 3])
    D2.items()                                   # dict_items([('email', 'spam'), ('total', 3)])
    D3.keys()                                    # dict_keys(['food'])
    D3['food'].keys()                            # dict_keys(['ham', 'eggs'])
    D3.values()                                  # dict_values([{'ham': 1, 'eggs': 3}])
    D3.items()                                   # dict_items([('food', {'ham': 1, 'eggs': 3})])

    len(D2)                                      # 2
    len(D3)                                      # 1

    for key, value in D2.items():                # email spam \n total 3
        print(key, value)

    for key, value in D3.items():                # food {'ham': 1, 'eggs': 3}
        print(key, value)

    D4 = D2.copy()                               # {'email': 'spam', 'total': 3}
    D2.update(D3)                                # {'email': 'spam', 'total': 3, 'food': {'ham': 1, 'eggs': 3}}
    D4.items()                                   # dict_items([('email', 'spam'), ('total', 3)]), so a true copy

    keys = ['email', 'total']                    # list or tuple: keys = ('email', 'total')
    vals = ['spam', 3]                           # list or tuple: vals = ('spam', 3)
    D5 = dict(zip(keys, vals))                   # {'email': 'spam', 'total': 3}

    D2.pop('total')                              # 3, leaving {'email': 'spam'}

    print(D3.__class__.__name__)                 # dict
    print(D3['food'].__class__.__name__)         # dict
    print(D3['food']['eggs'].__class__.__name__) # int
    print(f"{D2.keys()}")                        # "dict_keys(['email', 'total'])" # <class 'str'>
    print(f"{list(D2.keys())}")                  # "['email', 'total']"            # <class 'str'>

    type(D1)                                     # <class 'dict'>
    type(D3)                                     # <class 'dict'>
    type(D3['food'])                             # <class 'dict'>
    type(D3['food']['eggs'])                     # <class 'int'>
    isinstance(D3, dict)                         # True
    isinstance(D3['food'], dict)                 # True
    isinstance(D3['food']['eggs'], dict)         # False


Tuples
======

* Immutable
* Ordered collections of arbitrary objects, accessed by offset
* Variable length, heterogeneous, arbitrarily nestable
* Can be used as dictionary keys
* `Data Structures: Tuples and Sequences <https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences>`_
* `Data Structures: Looping techniques <https://docs.python.org/3/tutorial/datastructures.html#looping-techniques>`_

.. code-block:: python

    t0 = ()                         # () - Empty tuple
    t1 = (42,)                      # (42,) - one-item tuple (not an expression)
    i1 = (42)                       # 42 - integer
    t2 = (0, 'Ni', 1.2, 3)          # (0, 'Ni', 1.2, 3) - four-item tuple
    t2a = 0, 'Ni', 1.2, 3           # (0, 'Ni', 1.2, 3) - four-item tuple (alternative syntax)
    t3 = ('abc', ('def', 'ghi'))    # ('abc', ('def', 'ghi'))

    t1[0]                           # 42
    t3[0]                           # 'abc'
    t3[1]                           # ('def', 'ghi')
    t3[0][1]                        # 'b'
    t3[1][1]                        # 'ghi'
    t3[0:1]                         # ('abc',)
    t3[0:]                          # ('abc', ('def', 'ghi'))

    len(t2)                         # 4
    len(t3)                         # 2

    tx = t1 + t2                    # (42, 0, 'Ni', 1.2, 3)
    tx = t2 * 3                     # (0, 'Ni', 1.2, 3, 0, 'Ni', 1.2, 3, 0, 'Ni', 1.2, 3)

    3 in t2                         # True
    'Ni' in t2                      # True
    4 in t2                         # False

    for x in t2:                    # iteration
        print x                     # 0 \n Ni \n 1.2 \n 3

    type(t0)                        # <class 'tuple'>
    type(t3)                        # <class 'tuple'>
    isinstance(t3, tuple)           # True

Sets
====

* Mutable, but the elements are immutable and unique
* Unordered collections of arbitrary objects, accessed by key
* Variable length, heterogeneous, arbitrarily nestable
* `RealPython: Sets in Python <https://realpython.com/python-sets/>`_
* `GeeksForGeeks: Sets in Python <https://www.geeksforgeeks.org/sets-in-python/>`_

.. code-block:: python

    S0 = set()
    S1 = set(['fred','wilma','pebbles','barney','betty','bam-bam']) # List iterable
    S2 = set(('fred','wilma','pebbles','barney','betty','bam-bam')) # Tuple iterable
    S3 = {'fred','wilma','pebbles','barney','betty','bam-bam'}      # Dict iterable
    S4 = {42, 'foo', 3.14159, None}                                 # mixed content

    L1 = ['fred','wilma','pebbles','barney','betty','bam-bam']
    S11 = set(L1)

    t2 = ('fred','wilma','pebbles','barney','betty','bam-bam')
    S12 = set(t2)

    bool(S0) # False - empty set
    bool(S1) # True  - non-empty set

    'fred' in S1        # True
    'freddie' in S1     # False

    type(S0)            # <class 'set'>
    type(S1)            # <class 'set'>
    isinstance(S1, set) # True

    S1.add('dino')     # {'pebbles', 'barney', 'wilma', 'fred', 'bam-bam', 'dino', 'betty'}
    S1.remove('dino')  # {'pebbles', 'barney', 'wilma', 'fred', 'bam-bam', 'betty'}
    S1.remove('dino')  # KeyError: 'dino'
    S1.discard('dino') # Ignores missing key
    S1.pop()           # 'pebbles', pops random element from set
    S1.clear()         # removes all elements from set

    FS1 = frozenset(['fred','wilma','pebbles']) # set is immutable
    type(FS1)                   # <class 'frozenset'>
    isinstance(FS1, frozenset)  # True

    FS1.add('dino')     # AttributeError: 'frozenset' object has no attribute 'add'
    FS1.remove('dino')  # AttributeError: 'frozenset' object has no attribute 'add'
    FS1 & {'fred'}      # returns frozenset({'fred'})
    FS1 & {'dino'}      # returns empty frozenset()

Available Operators and Methods

.. code-block:: python

    a = {1, 2, 3, 4}
    b = {2, 3, 4, 5}
    c = {3, 4, 5, 6}
    d = {4, 5, 6, 7}

    a.union(b)                # {1, 2, 3, 4, 5}
    a | b                     # {1, 2, 3, 4, 5}
    a.union((2, 3, 4, 5))     # {1, 2, 3, 4, 5}
    a | {2, 3, 4, 5}          # {1, 2, 3, 4, 5}
    a | (2, 3, 4, 5)          # TypeError: unsupported operand type(s) for |: 'set' and 'tuple'

    a.intersection(b)         # {2, 3, 4}
    a & b                     # {2, 3, 4}
    a.intersection(b,c)       # {3, 4}
    a & b & c                 # {3, 4}
    a.intersection(b,c,d)     # {4}
    a & b & c & d             # {4}

    a.difference(b)           # {1} elements in 'a' but not in 'b'
    a - b                     # {1} elements in 'a' but not in 'b'

    a.symmetric_difference(b) # {1, 5} elements in 'a' or 'b', but not both
    a ^ b                     # {1, 5} elements in 'a' or 'b', but not both

.. code-block:: python

    a = {1, 2, 3, 4}
    b = {2, 3, 4, 5}
    e = {6, 7, 8, 9}
    f = {1, 2, 3}

    a.isdisjoint(b)  # False, has {2, 3, 4} in both
    a.isdisjoint(e)  # True, has no common elements

    a.issubset(f)    # False, (subset) every element of 'a' is in 'f'
    a <= f           # False, (subset) every element of 'a' is in 'f'
    a < f            # False, (proper subset) every element of 'a' is in 'f'; 'a' and 'f' are not equal.

    a.issuperset(f)  # True, (superset) 'a' contains every element of 'f'
    a >= f           # True, (superset) 'a' contains every element of 'f'
    a > f            # True, (proper superset) 'a' contains every element of 'f'; 'a' and 'f' are not equal

Augmented Assignment Operators and Methods

.. code-block:: python

    a = {1, 2, 3, 4}
    b = {2, 3, 4, 5}

    a.update(b)                      # {1, 2, 3, 4, 5}
    a |= b                           # {1, 2, 3, 4, 5}

    a = {1, 2, 3, 4}                 # reset 'a', a = {1, 2, 3, 4}
    a.intersection_update(b)         # {2, 3, 4}
    a &= b                           # {2, 3, 4}

    a = {1, 2, 3, 4}                 # reset 'a', a = {1, 2, 3, 4}
    a.difference_update(b)           # {1}
    a -= b                           # {1}

    a = {1, 2, 3, 4}                 # reset 'a', a = {1, 2, 3, 4}
    a.symmetric_difference_update(b) # {1, 5}
    a ^= b                           # {1, 5}


Heapq (binary tree)
===================

Heaps are binary trees for which every parent node has a value less than or equal to any of its children.

* `heapq — Heap queue algorithm <https://docs.python.org/3/library/heapq.html>`_
* `Heap Theory (binary tree sort) <https://docs.python.org/3.0/library/heapq.html#theory>`_

.. code-block:: python

    import heapq

    heap = []
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    for item in data:
        heapq.heappush(heap, item)

    type(heap) # <class 'list'>

    heap = [11, 3, 15, 7, 9, 23, 4, 6, 8, 10]
    heapq.heapify(heap)  # [3, 6, 4, 7, 9, 23, 15, 11, 8, 10]

    print('nlargest(3): {0}'.format(heapq.nlargest(3, heap)))   # [23, 15, 11]
    print('nsmallest(3): {0}'.format(heapq.nsmallest(3, heap))) # [3, 4, 6]

    smallest_item = heapq.heappop(heap) # 3

    # convert to sorted list
    ordered = []
    while heap:
        ordered.append(heapq.heappop(heap))

    print(ordered) # [4, 6, 7, 8, 9, 10, 11, 15, 23]

    # heap of tuples
    data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
    for item in data:
        heapq.heappush(heap, item)

    print('nlargest(3): {0}'.format(heapq.nlargest(3, heap)))   # [(4, 'N'), (3, 'H'), (2, 'O')]
    print('nsmallest(3): {0}'.format(heapq.nsmallest(3, heap))) # [(1, 'J'), (2, 'O'), (3, 'H')]

    smallest_item = heapq.heappop(heap) # (1, 'J')


****************
Python Operators
****************

Arithmetic operators
====================

.. code-block:: python

    (a,b) = (2,3)
    z = 'Abc'
    print(a + b)  # 5
    print(a - b)  # -1
    print(b - a)  # 1
    print(a * b)  # 6
    print(z * a)  # AbcAbc
    print(a / b)  # 0.6666666666666666
    print(b / a)  # 1.5
    print(a % b)  # 2 (modulus)
    print(b % a)  # 1 (modulus)
    print(a ** b) # 8 (exponent)

Comparison operators
====================

.. code-block:: python

    (a,b) = (2,3)
    print(a == b) # False
    print(a != b) # True
    print(a > b)  # False
    print(a < b)  # True
    print(a >= b) # False
    print(a <= b) # True

Bitwise operators
=================

.. code-block:: python

    (a,b) = (10,7)          # a='1010',     b='0111'
    (x,y) = (0b1010, 0b111) # x='1010'(10), y='0111'(7)
    print(bin(a))           # 0b1010
    print(bin(b))           # 0b111

    print(a & b)            #  2      Binary AND
    print(a | b)            # 15      Binary OR
    print(~b)               # -8      Binary OR
    print(a ^ b)            # 13      Binary XOR
    print(~a)               # -11     Ones Complement
    print(bin(~a))          # -0b1011 Ones Complement
    print(a << 1)           # 14      Binary Left Shift
    print(bin(a<<1))        # 0b10100 Binary Left Shift
    print(a >> 1)           # 5       Binary Right Shift
    print(bin(a >> 1))      # 0b101   Binary Right Shift

* `RealPython: Overview of Python’s Bitwise Operators <https://realpython.com/python-bitwise-operators/>`_

Lambda operators
================

Lambda functions, are meant to be small, one-line functions used for a short period

.. code-block:: python

    square = lambda x: x** 2
    print(square(5)) # 25

    add = lambda x,y: x+y
    print(add(3,4)) # 7

    # square each value
    L1 = (1, 2, 3, 4, 5)
    print(list(map(lambda x: x** 2, L1))) # [1, 4, 9, 16, 25]

    # find even numbers
    L2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(list(filter(lambda x: x % 2 == 0, L2))) # [2, 4, 6, 8, 10]

    # reduce
    from functools import reduce
    print(reduce(lambda x,y: x + y, L1)) # 15 = ((((1+2)+3)+4)+5)

    # sort names list by lastname
    names = ["John Smith", "Jane Doe", "Bob Johnson", "Alice Williams"]
    names.sort(key=lambda name: name.split()[-1])
    print(names)  # ['Jane Doe', 'Bob Johnson', 'John Smith', 'Alice Williams']

* `reduce function <https://docs.python.org/3/library/functools.html#functools.reduce>`_

Assignment
==========

.. code-block:: python

    (a,b) = (2,3) # before assignment
    a += b  # a is 5
    a *= b  # a is 6
    a /= b  # a is 0.6666666666666666
    a %= b  # a is 2 (modulus)
    b %= a  # b is 1 (modulus)
    a **= b # a is 8 (exponent operator)
    a //= b # a is 0 (floor division)
    b //= a # b is 1 (floor division)

Logical Operators
=================

.. code-block:: python

    (a,b,c,d) = (2,3,4,5)
    print(a > b and c < d)      # False
    print(a > b or c < d)       # True
    print(not(a > b) and c < d) # True

Rich Comparisons
================

.. code-block:: python

    L1 = [1, ('a', 3)]; L2 = [1, ('a', 3)]; L3 = L1
    L1 == L2                    # True
    L1 is L2                    # False, Not the same object
    L1 == L3                    # True
    L1 is L3                    # True, Are the same object
    1 in L1                     # True
    3 in L1                     # False
    3 in L1[1]                  # True

    S1 = 'spam'; S2 = 'spam'
    S1 == S2                    # True
    S1 is S2                    # True! WTF ** evil-bad caching! ** so same object

    LS1 = 'a longer string text'
    LS2 = 'a longer string text'
    LS3 = 'a longer string message'
    LS4 = 'a bit longer string text'
    LS1 == LS2           # True
    LS1 is LS2           # False
    LS1 == LS3           # False
    LS1 is LS3           # False
    LS1 > LS3            # True '... text' > '... message'
    LS1 > LS4            # True 'a longer ...' > 'a bit longer ...'
    len(LS1) == len(LS2) # True

References:

* `RealPython: Operators and Expressions in Python <https://realpython.com/python-operators-expressions/>`_
* `Python: operator — Standard operators as functions <https://docs.python.org/3/library/operator.html>`_
* `PEP 207 – Rich Comparisons <https://peps.python.org/pep-0207/>`_

Object Checking
===============

List of classinfo types:

.. code-block:: python

    print([t.__name__ for t in __builtins__.__dict__.values() if isinstance(t, type)])


Python-3.13 classinfo types: ::

    ['BuiltinImporter', 'bool', 'memoryview', 'bytearray', 'bytes', 'classmethod', 'complex', 'dict', 'enumerate', 'filter',
    'float', 'frozenset', 'property', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'staticmethod',
    'str', 'super', 'tuple', 'type', 'zip', 'BaseException', 'BaseExceptionGroup', 'Exception', 'GeneratorExit',
    'KeyboardInterrupt', 'SystemExit', 'ArithmeticError', 'AssertionError', 'AttributeError', 'BufferError', 'EOFError',
    'ImportError', 'LookupError', 'MemoryError', 'NameError', 'OSError', 'ReferenceError', 'RuntimeError',
    'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SystemError', 'TypeError', 'ValueError', 'Warning',
    'FloatingPointError', 'OverflowError', 'ZeroDivisionError', 'BytesWarning', 'DeprecationWarning', 'EncodingWarning',
    'FutureWarning', 'ImportWarning', 'PendingDeprecationWarning', 'ResourceWarning', 'RuntimeWarning', 'SyntaxWarning',
    'UnicodeWarning', 'UserWarning', 'BlockingIOError', 'ChildProcessError', 'ConnectionError', 'FileExistsError',
    'FileNotFoundError', 'InterruptedError', 'IsADirectoryError', 'NotADirectoryError', 'PermissionError',
    'ProcessLookupError', 'TimeoutError', 'IndentationError', '_IncompleteInputError', 'IndexError', 'KeyError',
    'ModuleNotFoundError', 'NotImplementedError', 'PythonFinalizationError', 'RecursionError', 'UnboundLocalError',
    'UnicodeError', 'BrokenPipeError', 'ConnectionAbortedError', 'ConnectionRefusedError', 'ConnectionResetError',
    'TabError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeTranslateError', 'ExceptionGroup', 'OSError',
    'OSError', 'OSError']

Checking what an object is:

 .. code-block:: python

    L = [1, 2, 3]; D = {'food': {'ham': 2, 'eggs': 3}}; t = (1, 2, 3); s = "string of text"
    print(L.__class__.__name__) # list
    print(D.__class__.__name__) # dict
    print(t.__class__.__name__) # tuple
    print(s.__class__.__name__) # str

    type(L)                     # <class 'list'>
    type(D)                     # <class 'dict'>
    type(t)                     # <class 'tuple'>
    type(s)                     # <class 'str'>

    isinstance (object, classinfo)

    isinstance('fred', str)               # True
    isinstance(123, int)                  # True
    isinstance(1.23, float)               # True
    isinstance([1, 2, 3], list)           # True
    isinstance((1, 2, 3), tuple)          # True

    D3 = {'food': {'ham': 2, 'eggs': 3}}
    isinstance(D3, dict)                  # True
    isinstance(D3['food'], dict)          # True
    isinstance(D3['food']['eggs'], dict)  # False
    isinstance(D3['food']['eggs'], str)   # False
    isinstance(D3['food']['eggs'], int)   # True
    isinstance(D3['food']['eggs'], float) # False

    L = [1,2,3]
    T = (1, 2, 3)
    isinstance(L, (list, tuple))          # True, because it is a list
    isinstance(T, (list, tuple))          # True, because it is a tuple

*****************
Python Statements
*****************

IF statements
=============

 .. code-block:: python

    if <test1> :
        <statements1>
    elif <test2> :
        <statements2>
    else :
        <statements3>

    a if <test> else b # ternary operator

    # dictionary lookup
    if 'ham' in {'spam' : 1.25, 'ham' : 1.99, 'eggs' : 0.99, 'bacon' : 1.10}:
        print({'spam' : 1.25, 'ham' : 1.99, 'eggs' : 0.99, 'bacon' : 1.10}['ham'])  # 1.99

    print({'spam' : 1.25, 'ham' : 1.99, 'eggs' : 0.99, 'bacon' : 1.10}['ham'])      # 1.99


While Loops
===========

 .. code-block:: python

    while <test1>:
        <statements>
        if <test2> : break     # break out of (nested) loop
        if <test3> : continue  # skip loop start
    else :
        <statement>            # if we did not hit break (or loop not entered)


For Loops
=========

 .. code-block:: python

    for <target> in <object> :
        <statements>
        if <test> : break     # break out of (nested) loop
        if <test> : continue  # skip loop start
    else :
        <statement>           # if we did not hit break (or loop not entered)

    for x in ['spam', 'eggs', 'ham']:
        print(x)

    sum = 0
    for x in [1,2,3,4]:
        sum = sum + x
    print(sum)           # 10

    for x in range(...):
        sum = sum + x
    print(sum)

    range(0,10)          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    range(0,10,2)        # [0, 2, 4, 6, 8]
    range(-5,5)          # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    range(5,-5,-1)       # [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

    S = 'abcdefghijk'
    for i in range(0, len(S), 2):
        print(S[i], end=' ') # a c e g i k

    D = {"spam": None, "eggs": 2, "ham": 1}
    for key,value in D.items():
        print(f"key={key}, value={value}") # key=spam, value=None \n key=eggs, value=2 \n key=ham, value=1

Try/Except
==========

.. code-block:: python

    import sys

    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError as os_error:
            print(f"{os_error}")
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

    #################################################################
    ## A Clumsy File handling and ValueError example

    import sys

    try:
        f = open('filename.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as os_error:
        print(f"{os_error}")
    except ValueError as value_error:
        print(f"{value_error}")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        print("always executed exception or not")

    #################################################################
    ## A better approach using 'with' and predefined clean-up actions

    with open("filename.txt") as f:
        for s in f:
            i = int(s.strip())

    # But displays Traceback if an error occurs
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: 'filename.txt'

    Traceback (most recent call last):
      File "<stdin>", line 3, in <module>
    ValueError: invalid literal for int() with base 10: '<?xml version="1.0" encoding="UTF-8"?>'

    #################################################################
    ## Alternative approach still using 'with' but no Traceback

    try:
        f = open("filename.txt")
    except IOError as io_error:
        print(f"{io_error}")
    else:
        with f:
            for s in f:
                try:
                    i = int(s.strip())
                except ValueError as value_error:
                    print(f"{value_error}")

    # Display only an error message if an error occurs
    [Errno 2] No such file or directory: 'filename.txt'

    invalid literal for int() with base 10: '<?xml version="1.0" encoding="UTF-8"?>'

********************
Dates and Timestamps
********************

DateTime and TimeZone
=====================

.. code-block:: python

    # With/Without TimeZone
    from datetime import datetime, timezone
    now = datetime.now()                     # (naive) No TimeZone
    now = datetime.utcnow()                  # (naive) No TimeZone
    now.tzinfo                               # None
    now.utcoffset()                          # None
    utc = datetime.now(timezone.utc)         # (aware) UTC TimeZone
    utc.tzinfo                               # datetime.timezone.utc
    utc.utcoffset()                          # datetime.timedelta(0)

Timestamps
==========

.. code-block:: python

    # UNIX epoch (UTC)
    import time
    from datetime import datetime, timezone
    utc = datetime.utcnow()                  # (naive) No TimeZone
    time.mktime(utc.timetuple())             # UNIX epoch as float
    int(time.mktime(utc.timetuple()))        # UNIX epoch as int
    round(time.mktime(utc.timetuple()))      # UNIX epoch as int

**************
Python Strings
**************

String Formatting
=================

Python string formatting has evolved over the years, and while all three formats are supported
in Python3, the ***f-string*** format is the one that should be used.

#. **"** *<format-str>* **" % (** *<variable(s)>* **)**
#. **"** *<format-str>*"**.format(** *<variable(s)>* **)**
#. **f"{** *<variable>* **:** *<format-str>* **}"**

A string can be enclosed in `"` (double-quote) or `'`'` (single-quote), for consistency the examples use
double-quote.

* `Pyformat: Using % and .format() for great good! <https://pyformat.info/>`_
* `RealPython: Python 3's f-Strings: An Improved String Formatting Syntax (Guide) <https://realpython.com/python-f-strings/>`_
* `Python: Input and Output - Fancier Output Formatting <https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting>`_
* `Python: Formatted string literals <https://docs.python.org/3/reference/lexical_analysis.html#f-strings>`_
* `Python F-strings <https://www.pythontutorial.net/python-basics/python-f-strings/>`_, covers literal ``{`` and ``}`` characters

For Docstrings
--------------

* `use str() for __str__ <https://docs.python.org/3/library/stdtypes.html#str>`_
* `use repr() for __repr__ <https://docs.python.org/3/library/functions.html#repr>`_

Text
----

.. code-block:: python

    a = 'one'; b = 'two'
    print("%s %s" % (a, b))                       # one two
    print("{} {}".format(a, b))                   # one two
    print(f"{a} {b}")                             # one two

    # Dictionary format
    print("{'a': '%s', 'b': '%s'}" % (a, b))      # {'a': 'one', 'b': 'two'}
    print("{{'a': '{}', 'b': '{}'}}".format(a,b)) # {'a': 'one', 'b': 'two'}
    print(f"{{'a': '{a}', 'b': '{b}'}}")          # {'a': 'one', 'b': 'two'}

    # List format
    print("['a', '%s', 'b', '%s']" % (a, b))      # ['a', 'one', 'b', 'two']
    print("['a', '{}', 'b', '{}']".format(a,b))   # ['a', 'one', 'b', 'two']
    print(f"['a', '{a}', 'b', '{b}']")            # ['a', 'one', 'b', 'two']

    # Tuple format
    print("('a', '%s', 'b', '%s')" % (a, b))      # ('a', 'one', 'b', 'two')
    print("('a', '{}', 'b', '{}')".format(a,b))   # ('a', 'one', 'b', 'two')
    print(f"('a', '{a}', 'b', '{b}')")            # ('a', 'one', 'b', 'two')

    # Concatenation
    print("%s-%s" % (a,b))                        # one-two
    print("{}-{}".format(a,b))                    # one-two
    print(f"{a}-{b}")                             # one-two

    # Concatenation using join
    print("%s" % ("-".join((a,b))))               # one-two
    print("{}".format("-".join((a,b))))           # one-two
    print(f"{'-'.join((a,b))}")                   # one-two


Alignment and Padding
---------------------

.. code-block:: python

    # Padding (10) and aligning strings
    c = 'short'; d = 'long string with more text'
    print("%10s;%10s" % (c,d))           #      short;long string with more text
    print("{:10};{:10}".format(c,d))     #      short;long string with more text
    print(f"{c:10};{d:10}")              #      short;long string with more text

    print("%-10s;%-10s" % (c,d))         # short     ;long string with more text
    print("{:>10};{:>10}".format(c,d))   # short     ;long string with more text
    print(f"{c:>10};{d:>10}")            # short     ;long string with more text

    print("{:_<10};{:_<10}".format(c,d)) # short_____;long string with more text
    print(f"{c:_<10};{d:_<10}")          # short_____;long string with more text

    print("{:^10};{:^10}".format(c,d))   #   short   ;long string with more text
    print(f"{c:^10};{d:^10}")            #   short   ;long string with more text

    # Truncating (7) long strings
    print("%.7s;%.7s" % (c,d))           # short;long st
    print("{:.7};{:.7}".format(c,d))     # short;long st
    print(f"{c:.7};{d:.7}")              # short;long st

    # Truncating (7) and padding (10) long strings
    print("%-10.7s;%-10.7s" % (c,d))     # short     ;long st
    print("{:10.7};{:10.7}".format(c,d)) # short     ;long st
    print(f"{c:10.7};{d:10.7}")          # short     ;long st

Numbers
-------

.. code-block:: python

    n = 42; N = -42; pi = 3.141592653589793
    print("%d;%d" % (n, pi))             # 42;3
    print("%d;%f" % (n, pi))             # 42;3.141593
    print("{:d};{:d}".format(n,pi))      # ValueError: Unknown format code 'd' for object of type 'float'
    print("{:d};{:f}".format(n,pi))      # 42;3.141593
    print(f"{n:d}")                      # 42
    print(f"{n:d};{pi:d}")               # ValueError: Unknown format code 'd' for object of type 'float'
    print(f"{n:d};{pi:f}")               # 42;3.141593

    # Padding numbers
    print("%7d;%7d" % (n, pi))            #      42;      3
    print("%7d;%7.2f" % (n, pi))          #      42;   3.14
    print("{:7d};{:7.2f}".format(n,pi))   #      42;   3.14
    print(f"{n:7d};{pi:7.2f}")            #      42;   3.14
    print("%07d;%07d" % (n, pi))          # 0000042;0000003

    print("%07d;%07d" % (n, pi))          # 0000042;0000003
    print("%07d;%07.2f" % (n, pi))        # 0000042;0003.14
    print("{:07d};{:07.2f}".format(n,pi)) # 0000042;0003.14
    print(f"{n:07d};{pi:07.2f}")          # 0000042;0003.14

    # Signed numbers
    n = 42;  N = -42; pi = 3.141592653589793
    print("%+d;%+d" % (n, N))             # +42;-42
    print("% d;% d" % (n, N))             #  42;-42
    print("%+d;%+7.2f" % (n, pi))         # +42;  +3.14

    print("{:+d};{:+d}".format(n,N))      # +42;-42
    print("{: d};{: d}".format(n,N))      #  42;-42
    print("{:+d};{:+7.2f}".format(n,pi))  # +42;  +3.14
    print("{:=5d};{:=5d}".format(n,N))    #    42;-  42

    print(f"{n:+d};{N:+d}")               # +42;-42
    print(f"{n: d};{N: d}")               #  42;-42
    print(f"{n:+d};{pi:+07.2f}")          # +42;+003.14
    print(f"{n:=5d};{N:=5d}")             #    42;-  42

    # Convert <number> to str
    f"{n!r}"                              # '42'
    f"{N!r}"                              # '-42'
    f"{pi!r}"                             # '3.141592653589793'
    f"{n!r}".zfill(7)                     # '0000042'
    f"{N!r}".zfill(7)                     # '-000042'
    f"{pi!r}".zfill(7)                    # '3.141592653589793'
    str(n).zfill(7)                       # '0000042'
    str(N).zfill(7)                       # '-000042'
    str(pi).zfill(7)                      # '3.141592653589793'

DateTime, UNIX Epoch and TimeStamps
-----------------------------------

.. code-block:: python

    # DateTime Only (CET, CEST TimeZone)
    from datetime import datetime
    now = datetime.now()
    print(now)                                                           # 2023-03-01 16:50:03.393791
    print("{:%Y-%m-%d %H:%M}".format(now))                               # 2023-03-01 16:50
    print("{:{dfmt} {tfmt}}".format(now, dfmt="%Y-%m-%d", tfmt="%H:%M")) # 2023-03-01 16:50
    print(f"{now:%Y-%m-%d %H:%M}")                                       # 2023-03-01 16:50

    # DateTime (Naive, in CET, CEST TimeZone)
    from datetime import datetime, timezone
    now = datetime.utcnow()
    print(now)                                                           # 2023-03-01 15:50:03.393791
    print("{:%Y-%m-%d %H:%M}".format(now))                               # 2023-03-01 15:50
    print("{:{dfmt} {tfmt}}".format(now, dfmt="%Y-%m-%d", tfmt="%H:%M")) # 2023-03-01 15:50
    print(f"{now:%Y-%m-%d %H:%M}")                                       # 2023-03-01 15:50
    print(now.isoformat())                                               # 2023-03-01T15:50:03.393791+00:00
    print(f"{now:%Y-%m-%dT%H:%M:%S+00:00}")                              # 2023-03-01T15:50:03.39+00:00

    # Prior to Python-3.9, DateTime (TimeZone aware, in CET, CEST TimeZone)
    # NOTE: pip install pytz, pip install tzlocal
    import pytz                                                          # python IANA timezone implementation
    import tzlocal                                                       # python local time-zone
    from pytz import timezone
    from tzlocal import get_localzone
    from datetime import datetime
    epoch = 1682490209                                                   # UNIX epoch (naive, no time-zone)
    dt_format = "%Y-%m-%d %H:%M:%S %Z%z"
    dt = datetime.fromtimestamp(epoch).replace(tzinfo=pytz.UTC)          # make UTC datetime (time-zone aware)
    print(dt.strftime(dt_format))                                        # 2023-04-26 08:23:29 UTC+0000
    print(dt.astimezone(timezone('Europe/Zurich')).strftime(dt_format))  # 2023-04-26 10:23:29 CEST+0200
    print(dt.astimezone(get_localzone()).strftime(dt_format))            # 2023-04-26 10:23:29 CEST+0200

    # Python-3.9 or later, DateTime (TimeZone aware, in CET, CEST TimeZone)
    # NOTE: pip install tzdata (IANA timezone data)
    import time
    from zoneinfo import ZoneInfo
    from datetime import datetime, timezone
    epoch = 1682490209                                                   # UNIX epoch (naive, no time-zone)
    dt_format = "%Y-%m-%d %H:%M:%S %Z%z"
    dt = datetime.fromtimestamp(epoch).replace(tzinfo=timezone.utc)      # make UTC datetime (time-zone aware)
    print(dt.strftime(dt_format))                                        # 2023-04-26 08:23:29 UTC+0000
    print(dt.astimezone(ZoneInfo('Europe/Zurich'))).strftime(dt_format)) # 2023-04-26 10:23:29 CEST+0200

    localzone =  datetime.now(tz=timezone.utc).astimezone().tzinfo
    print(dt.astimezone(localzone).strftime(dt_format))                  # 2023-04-26 10:23:29 CEST+0200
    print(dt.astimezone().strftime(dt_format))                           # 2023-04-26 10:23:29 CEST+0200

    # Date Only
    from datetime import date
    today = date.today()
    print(today)                                                         # 2023-03-01
    print("{:%B %d %Y}".format(today))                                   # March 01 2023
    print("{:{dfmt}}".format(today, dfmt="%B %d %Y"))                    # March 01 2023
    print(f"{today:%B %d %Y}")                                           # March 01 2023

Lists
-----

.. code-block:: python

    list = ['Fred', 'Flintstone']
    print("%s %s" % (list[0], list[1]))                                  # Fred Flintstone
    print("{p[0]} {p[1]}".format(p=list))                                # Fred Flintstone
    print(f"{list[0]} {list[1]}")                                        # Fred Flintstone
    print(f"{list[0].lower()} {list[1].upper()}")                        # fred FLINTSTONE

Tuple
-----
.. code-block:: python

    tuple = ('Fred', 'Flintstone')
    print("%s %s" % (tuple))                                             # Fred Flintstone
    print("%s %s" % (tuple[0], tuple[1]))                                # Fred Flintstone
    print("{p[0]} {p[1]}".format(p=tuple))                               # Fred Flintstone
    print(f"{tuple[0].lower()} {tuple[1].upper()}")                      # fred FLINTSTONE

Dictionaries
------------

.. code-block:: python

    dict = {'first': 'Fred', 'last': 'Flintstone'}
    print("%(first)s %(last)s" % dict)                                   # Fred Flintstone
    print("{first} {last}".format(**dict))                               # Fred Flintstone
    print("{p[first]} {p[last]}".format(p=dict))                         # Fred Flintstone
    print(f"{dict['first']} {dict['last']}")                             # Fred Flintstone
    print(f"{dict['first'].lower()} {dict['last'].upper()}")             # fred FLINTSTONE

String Manipulation
===================

* `W3Schools - Built-In Methods <https://www.w3schools.com/python/python_ref_string.asp>`_
* `PythonCheatsheet - Manipulating Strings - <https://www.pythoncheatsheet.org/cheatsheet/manipulating-strings>`_

*************************
Reading and Writing Files
*************************

* `Python3: Input and Output <https://docs.python.org/3/tutorial/inputoutput.html>`_
* `Python3: Reading and Writing Files <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>`_

Text Files
==========

Sequential Access
-----------------

.. code-block:: python

    # mode: r (read), w (write: create/overwrite), a (append), r+ (read/write), + (read/write)
    outfile_handle = open('spam', 'w')                        # 'spam', <_io.TextIOWrapper>
    outfile_handle = open('utf8spam', 'w', encoding="utf-8")  # 'utf8spam' in UTF8, <_io.TextIOWrapper>
    infile_handle = open('data', 'r')                         # open input file

    S = infile_handle.read()                # Read entire file into a single string
    S = infile_handle.read(N)               # Read N bytes (N >= 1)
    S = infile_handle.readline()            # Read next line, len(S) == 0 when no more input
    L = infile_handle.readlines()           # Read entire file into list of line strings

    outfile_handle.write(S)                 # Write string S into file (returns number of chars written)
    outfile_handle.writelines(L)            # Write all strings in list L
    print("lineFour", file=outfile_handle)  # Better than low-level write(), writelines() methods
    outfile_handle.flush()                  # Flush buffered write to file
    outfile_handle.close()                  # May need to flush() to write contents

    # Cleaner but will raise an exception and close cleanly
    with open(filename) as f:
        data = f.read()

    # Alternative, traps and reports any exception raised
    try:
        with open(filename) as f:
        data = f.read()
    except Exception as error:
        print('{0}'.format(error))

    # Example, forcing UTF8 encoding
    outfile_handle = open('utf8spam', 'w', encoding="utf-8")
    for i in range(1,11):
        print("{0:2d}: line number {0}".format(i), file=outfile_handle)

    outfile_handle.flush()
    outfile_handle.close()


Random Access
-------------

.. code-block:: python

    # random access to text files
    import linecache
    linecache.getline('utf8spam',1)  # ' 1: line number 1\n'
    linecache.getline('utf8spam',7)  # ' 7: line number 7\n'
    linecache.getline('utf8spam',0)  # ''
    linecache.getline('utf8spam',15) # ''


* `linecache — Random access to text lines <https://docs.python.org/3/library/linecache.html>`_

File, and Directory Tests
=========================

.. code-block:: python

    import os

    os.path.exists('flintstones.json')  # True
    os.path.exists('flintstones.jsong') # False
    os.path.exists('project')           # True
    os.path.exists('projects')          # False

    os.path.isfile('flintstones.json')  # True
    os.path.isfile('flintstones.jsong') # False
    os.path.isdir('project')            # True
    os.path.isdir('projects')           # False

* `os.path — Common pathname manipulations <https://docs.python.org/3/library/os.path.html>`_
* `pathlib — Object-oriented filesystem paths <https://docs.python.org/3/library/pathlib.html>`_

JSON files
==========

.. code-block:: python

    import json
    f = open('flintstones.json', 'r')
    x = json.load(f)  # {"flintstones": {"Fred": 30, "Wilma": 25, "Pebbles": 1, "Dino": 5}}

    print(x.__class__)          # <class 'dict'>
    print(x.__class__.__name__) # dict
    isinstance(x, dict)         # True

    x['flintstones']['Fred'] = 31
    f = open('flintstones.json', 'w')
    json.dump(x, f)
    f.flush()
    f.close()


XML files
=========

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <family surname = "Flintstones">
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


.. Warning:: xml.etree.ElementTree is insecure, see `Security issues <https://docs.python.org/3/library/xml.html>`_ and `GitHub defusedxml <https://github.com/tiran/defusedxml/>`_

.. code-block:: python

    import xml.etree.ElementTree as ET
    tree = ET.parse('flintstones.xml')

    print(tree.__class__)          # <class 'xml.etree.ElementTree.ElementTree'>
    print(tree.__class__.__name__) # ElementTree

    root = tree.getroot()
    root.tag    # 'family'
    root.attrib # {'surname': 'Flintstones'}

    for member in root.iter('member'):  # Fred: 30 \n Wilma: 25 \n Pebbles: 1 \n Dino: 5
        name = member.find('name').text
        age = member.find('age').text
        print(f"{name}: {age}")

    # Update Fred's age
    root[0][0].text                      # 'Fred'
    root[0][1].text                      # '30'
    root[0][1].text = '31'               # update age, note it is a string!
    ET.indent(root, space="\t", level=0) # pretty-print
    ET.dump(root)                        # display on console

    # Save XML, add UTF-8 header because default encoding is US-ASCII
    tree.write('flintstones.xml', encoding="UTF-8", xml_declaration=True)
    tree.write('flintstones-ascii.xml')

    # Add sub-elements 'sex' and update values
    for member in root.iter('member'):
        subelement = ET.SubElement(member, 'sex')

    sexes = ('M', 'F', 'F', 'N') # Male(Fred), Female(Wilma,Pebbles), Neuter(Dino)
    for i in range(len(sexes)):
        root[i][2].text = sexes[i]

    ET.indent(root, space="\t", level=0) # pretty-print
    ET.dump(root)                        # display on console

    # Remove sub-elements 'sex'
    for member in root.iter('member'):
        for sex in member.findall('sex'):
            member.remove(sex)

    ET.indent(root, space="\t", level=0) # pretty-print
    ET.dump(root)                        # display on console


.. Important:: To secure the above example use `defusedxml 0.7.1 <https://pypi.org/project/defusedxml/>`_, see `GitHub defusedxml <https://github.com/tiran/defusedxml/>`_

Replace ``import xml.etree.ElementTree as ET`` with ``import defusedxml.etree.ElementTree as ET``


References:

* `xml.etree.ElementTree — The ElementTree XML <https://docs.python.org/3/library/xml.etree.elementtree.html>`_
* `XML Processing Modules - Security issues <https://docs.python.org/3/library/xml.html>`_
* `Structured Markup Processing Tools <https://docs.python.org/3/library/markup.html>`_

**********
Decorators
**********

A decorator is a function that takes another function extending its behavior without explicitly modifying it,
a kind of *wrapper*.

* `Primer on Python Decorators <https://realpython.com/primer-on-python-decorators/>`_
* `Decorators in Python <https://www.geeksforgeeks.org/decorators-in-python/>`_
* `Chain Multiple Decorators in Python <https://www.geeksforgeeks.org/chain-multiple-decorators-in-python/>`_
* `Python Decorators Tutorial <https://www.datacamp.com/tutorial/decorators-python>`_
* `PEP 318 – Decorators for Functions and Methods <https://peps.python.org/pep-0318/>`_

Before explaining decorators, it is important to realize that Python functions are first class objects,
meaning a function:

* is an instance of the Object type.
* can be stored in a variable.
* used as a parameter to another function.
* returned from another function.
* can be stored in data structures such as hash tables, lists etc.

Functions as objects, arguments, and return values
==================================================

Functions as objects

.. code-block:: python

    # https://www.geeksforgeeks.org/decorators-in-python/
    def to_upper(text):
        return text.upper()

    print(to_upper("Hello World"))  # HELLO WORLD (function parameter)
    uppercase = to_upper
    print(uppercase("Hello World")) # HELLO WORLD (stored in a variable)

Passing the function as an argument

.. code-block:: python

    def to_upper(text):
        return text.upper()

    def to_lower(text):
        return text.lower()

    def greeting(argument):                   # function as an argument, to_upper, to_lower
        hello_world = argument("Hello World") # function stored in a variable
        print(hello_world)

    greeting(to_upper) # HELLO WORLD
    greeting(to_lower) # hello world

Returning functions from inside another function.

.. code-block:: python

    def prefix(x):
        def concatenate(y):
            return x + ' ' + y
        return concatenate         # return nested function

    hello_prefix = prefix("Hello") # function stored in a variable with x = "Hello",
    hello_prefix                   # <function prefix.<locals>.concatenate at 0x000001A4F2ED49A0>
    print(hello_prefix("World"))   # Hello World


Functions and Methods
=====================

A common use is to wrap functions and methods, to extend their capabilities.

.. code-block:: python

    def decorator1(func):
        def wrapper(*args,**kwargs):
            print("wrapper: before 'func' execution")
            result = func(*args,**kwargs) # func has variable number of arguments
            print("wrapper: after 'func' execution")
            return result
        return wrapper

    @decorator1
    def addition(a, b):
        print(f"addition: {a} + {b}")
        return a + b

    @decorator1
    def subtraction(a, b):
        print(f"subtraction: {a} - {b}")
        return a - b

    >>> print(addition(35,7))
    wrapper: before 'func' execution
    addition: 35 + 7
    wrapper: after 'func' execution
    42
    >>> print(subtraction(35,7))
    wrapper: before 'func' execution
    subtraction: 35 - 7
    wrapper: after 'func' execution
    28


* ``*args,**kwargs`` allows a variable number of arguments to be passed to the function
* ``@`` indicates the decorator function that is being extended

Another simple more realistic execution time example

.. code-block:: python

    import time
    import math

    def execution_time(func):
        def wrapper(*args,**kwargs):
            begin = time.time()
            result = func(*args,**kwargs) # func has variable number of arguments
            end = time.time()
            print(f"execution_time: {func.__name__}, {end - begin}")
            return result
        return wrapper

    @execution_time
    def factorial(num):
        time.sleep(2) # slow to provide time delta
        print(math.factorial(num))

    >>> factorial(10)
    3628800
    execution_time: factorial, 2.0123209953308105


Decorator chaining
==================

.. code-block:: python

    def decorator1(func):
        def wrapper(*args,**kwargs):
            x = func(*args,**kwargs)
            return x * x
        return wrapper

    def decorator2(func):
        def wrapper(*args,**kwargs):
            x = func(*args,**kwargs)
            return 2 * x
        return wrapper

    @decorator1
    @decorator2
    def num12():
        return 10

    @decorator2
    @decorator1
    def num21():
        return 10

    print(num12()) # 400 = (2 * 10) * (2 * 10)
    print(num21()) # 200 = (10 * 10) * 2


*******************
Python Environments
*******************

If using `UNIX`, `Linux` or `MacOS` there is a version of Python installed and used by the operating system.
Your own work should not interfere with this so it is normal to use your own environment, see

* `The Hitchhicker's Guide to Python: Pipenv & Virtual Environments <https://docs.python-guide.org/dev/virtualenvs/>`_

On Windows various Python releases are available from `Microsoft App Store <https://apps.microsoft.com/store/apps>`_.
These releases do not have `pipenv`, only `python` and `idle3` so use `VirtualEnv` with an IDE like:

* `PyCharm Community Edition Download <https://www.jetbrains.com/pycharm/download/?section=windows>`_
* `Eclipse Download <https://www.eclipse.org/downloads/>`_ and `PyDev <https://www.pydev.org/>`_

``pip``
=======

The *original* normally run in a :ref:`virtualenv-label`.

* `Pip - User Guide <https://pip.pypa.io/en/stable/user_guide/>`_
* `Pip - Requirements File Format <https://pip.pypa.io/en/stable/reference/requirements-file-format/>`_
* `pipdev - Requirement version visualizer <https://nok.github.io/pipdev/>`_

.. code-block:: shell

    # Basic operations
    $ pip search SomePackage                                    # Fails, use https://pypi.org/search
    $ pip install SomePackage                                   # latest version
    $ pip install SomePackage==1.0.4                            # specific version
    $ pip install 'SomePackage>=1.0.4'                          # version 1.0.4 or later
    $ pip uninstall SomePackage
    $ pip freeze > requirements.txt                             # UNIX save current installation
    $ pip freeze | Add-Content -Encoding ASCII requirements.txt # Windows save current installation
    $ pip install -r requirements.txt                           # install all the specified packages
    $ pip list                                                  # currently installed packages
    $ pip list --outdated                                       # upgradeable packages

    # Updating all packages
    # - Note: may need several iterations and manual additions to 'requirements.txt'
    $ pip list --outdated
    $ pip freeze > requirements.txt                             # UNIX
    $ pip freeze | Add-Content -Encoding ASCII requirements.txt # Windows
    $ pip install -r requirements.txt --upgrade
    # - Failures edit 'requirements.txt', replace '==' with '<='
    $ pip install -r requirements.txt --upgrade

.. code-block:: shell

    # pip self-update
    $ python -m pip install --upgrade pip


``pipenv``
==========

* `Github: Pipenv <https://github.com/pypa/pipenv>`_
* `Pipenv: A Guide to the New Python Packaging Tool <https://realpython.com/pipenv-guide/>`_
* `Pipenv: Python Dev Workflow for Humans <https://pipenv.pypa.io/en/latest/>`_
* `The Hitchhiker’s Guide to Python!: Installing Pipenv <https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv>`_

.. code-block:: shell-session

    $ cd myproject
    $ pipenv --python 3           # Create a virtual env and install dependencies (if it does not exist already)
    $ pipenv install <package>    # Add the package to the virtual environment and to Pipfile and Pipfile.lock
    $ pipenv uninstall <package>  # Will remove the <package>
    $ pipenv lock                 # Regenerate Pipfile.lock and updates the dependencies inside it
    $ pipenv graph                # Show you a dependency graph of installed dependencies
    $ pipenv shell                # Spawn a shell with the virtualenv activated, deactivated by using exit
    $ pipenv run <program.py>     # Run a <program.py> from the virtualenv, with any arguments forwarded
    $ pipenv check                # Checks for security vulnerabilities, asserts PEP 508 requirements


Eclipse/PyDev

Setup a new Python project in Eclipse, and change the project to use it.

.. code-block:: shell-session

    $ export PIPENV_VENV_IN_PROJECT=1 # force creation of '.venv' in project
    $ cd <eclipse-workspace>/<project>
    $ pipenv --python 3          # python3 project
    $ pipenv install <package>   # updates the Pipfile
    $ pipenv uninstall <package> # updates the Pipfile
    $ pipenv --rm                # remove virtualenv
    $ pipenv shell               # virtualenv interactive shell
    $ pipenv run <program.py>    # virtualenv: run script
    $ pipenv check               # PEP8 check of the Pipfile
    $ pipenv update              # update all packages

.. code-block:: shell-session

    # pipenv self-update
    $ pip install --upgrade pipenv

.. _virtualenv-label:

VirtualEnv
==========

* `RealPython: Python Virtual Environments: A Primer <https://realpython.com/python-virtual-environments-a-primer/>`_
* `Python: venv — Creation of virtual environments <https://docs.python.org/3/library/venv.html>`_
* `PyPA: PIP - Python Packaging User Guide <https://packaging.python.org/en/latest/>`_

The example below is for Windows, but will also work on `UNIX`, `Linux` or `MacOS`, with the exception
of the PowerShell `get-command`.

.. code-block:: pwsh-session

    PS> mkdir myproject
    PS> cd myproject
    PS> python -m venv venv
    PS> venv\Scripts\activate

    (venv) PS> get-command python | format-list
    Name            : python.exe
    CommandType     : Application
    Definition      : C:\Users\sjfke\sandbox\Python\myproject\venv\Scripts\python.exe
    Extension       : .exe
    Path            : C:\Users\sjfke\sandbox\Python\myproject\venv\Scripts\python.exe
    FileVersionInfo : File:             C:\Users\sjfke\sandbox\Python\myproject\venv\Scripts\python.exe
                      InternalName:     Python Launcher
                      OriginalFilename: py.exe
                      FileVersion:      3.9.13
                      FileDescription:  Python
                      Product:          Python
                      ProductVersion:   3.9.13
                      Debug:            False
                      Patched:          False
                      PreRelease:       False
                      PrivateBuild:     False
                      SpecialBuild:     False
                      Language:         Language Neutral

    (venv) PS> pip install flask

    (venv) PS> flask --version
    Python 3.9.13
    Flask 2.2.3
    Werkzeug 2.2.3

    (venv) PS> pip uninstall flask
    Found existing installation: Flask 2.2.3
    Uninstalling Flask-2.2.3:
      Would remove:
        c:\users\sjfke\sandbox\python\myproject\venv\lib\site-packages\flask-2.2.3.dist-info\*
        c:\users\sjfke\sandbox\python\myproject\venv\lib\site-packages\flask\*
        c:\users\sjfke\sandbox\python\myproject\venv\scripts\flask.exe

    (venv) PS> deactivate
    PS>

Updating packages in a `venv` session is done using `pip`.

.. code-block:: shell-session

    # Updating all packages
    # Note: may need several iterations and manual additions to 'requirements.txt'
    $ pip list --outdated
    $ pip freeze > requirements.txt
    $ pip install -r requirements.txt --upgrade
    # edit 'requirements.txt', replace '==' with '<=' on any failures

If you are brave like `ActiveState`, `How to Update All Python Packages <https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/>`_

.. code-block:: pwsh-session

    PS> pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

.. code-block:: shell-session

    $ pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
    $ pip3 list -o | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print}' | cut -d' ' -f1 | xargs -n1 pip3 install -U

.. code-block:: python

    # using python inside a 'venv' session
    import pkg_resources
    from subprocess import callfor dist in pkg_resources.working_set:
        call("python -m pip install --upgrade " + dist.<projectname>, shell=True)


Using `PyCharm` it is a little easier using the Python Interpreter dialogue, but is still manual and can take several
iterations if new packages need to be installed because of dependencies.

.. code-block:: console

    Settings => Project <name> => Python Interpreter
    -or-
    Python Packages Tool Window

``pipx``
========

* `pipx — Install and Run Python Applications in Isolated Environments <https://pipx.pypa.io/stable/>`_
* `pipx — Comparison to Other Tools <https://pipx.pypa.io/stable/comparisons/>`_

**************************
Useful Python 3 references
**************************

Language Fundamentals
=====================

* `Python: Built-in Types <https://docs.python.org/3/library/stdtypes.html>`_
* `Python: Built-in Exceptions <https://docs.python.org/3/library/exceptions.html>`_
* `Python: The import system <https://docs.python.org/3/reference/import.html>`_
* `Python: Modules <https://docs.python.org/3/tutorial/modules.html>`_
* `Python: Errors and Exceptions <https://docs.python.org/3/tutorial/errors.html>`_

Docstrings
==========
* `BetterProgramming: start Writing Python Docstrings <https://betterprogramming.pub/the-guide-to-python-docstrings-3d40340e824b>`_ is limited views per month
* `Sphinx: Writing docstrings <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>`_

f-Strings
=========

* `RealPython: Python 3's f-Strings: An Improved String Formatting Syntax <https://realpython.com/python-f-strings/>`_
* `GeeksForGeeks: f-strings in Python <https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/>`_
* `FreeCodeCampe: Python f-String Tutorial <https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/>`_

.. note::

    Supports almost all the ***.format()**** options in `Pyformat: Using % and .format() for great good! <https://pyformat.info/>`_

Strings
=======

* `W3Schools: Python String Methods <https://www.w3schools.com/python/python_ref_string.asp>`_
* `Python: Text Processing Services <https://docs.python.org/3/library/text.html>`_
* `GeeksForGeeks: str() vs repr() in Python <https://www.geeksforgeeks.org/str-vs-repr-in-python/>`_
* `Python: string — Common string operations <https://docs.python.org/3/library/string.html>`_
* `Python: re — Regular expression operations <https://docs.python.org/3/library/re.html>`_
* `PyFormat: Using % and .format() for great good! <https://pyformat.info/>`_

PEP Guides
==========

* `PEP 0 – Index of Python Enhancement Proposals (PEPs) <https://peps.python.org/pep-0000/>`_
* `PEP 8 – Style Guide for Python Code <https://peps.python.org/pep-0008/>`_
* `PEP 207 – Rich Comparisons <https://peps.python.org/pep-0207/>`_
* `PEP 257 – Docstring Conventions <https://peps.python.org/pep-0257/>`_
* `PEP 318 – Decorators for Functions and Methods <https://peps.python.org/pep-0318/>`_

Introductory Guides
===================

* `Learn Python - the hard way <https://learnpythonthehardway.org/python3/>`_
* `Tutorials Point - Python Tutorial <https://www.tutorialspoint.com/python/index.htm>`_
* `Real Python - Tutorials <https://realpython.com/>`_
* `W3Schools - Python Tutorial <https://www.w3schools.com/python/>`_
* `Online Python-3 Compiler (Interpreter) <https://www.tutorialspoint.com/online_python_compiler.php>`_

Intermediate Guides
===================

* `Packaging Python <https://packaging.python.org/en/latest/tutorials/packaging-projects/>`_
* `Python Modules and Packages – An Introduction <https://realpython.com/python-modules-packages/>`_
* `The Hitchhiker’s Guide to Python <https://docs.python-guide.org/>`_

Graphical User Interfaces
=========================

* `Tkinter - Python interface to Tcl/Tk <https://docs.python.org/3/library/tkinter.html>`_
* `Overview of wxPython <https://wxpython.org/pages/overview/index.html>`_
* `Learn Python PyQt <https://pythonpyqt.com/>`_
* `Welcome to Kivy <https://kivy.org/doc/stable/>`_

Generating Diagrams
===================

* `Diagrams Diagram as Code <https://diagrams.mingrammer.com/>`_





