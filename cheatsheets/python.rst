:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/python.rst

*****************
Python Cheatsheet
*****************

Useful Links
============

* `Pipenv <https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv>`_
* `Tutorialspoint <https://www.tutorialspoint.com/python/>`_
* `Learn Python - the hard way <https://learnpythonthehardway.org/python3/>`_
* `Execute Python-3 Online (Python v3.6.2) <https://www.tutorialspoint.com/execute_python3_online.php>`_
* `Python IDE Online (Python v2.7.13) <https://www.tutorialspoint.com/online_python_ide.php>`_

Lists
=====

* mutable
* ordered collections of abitrary objects, accessed by offset
* variable length, hetrogeneous, aribtrarily nestable

::

	L1 = []                         # Empty list 
	L2 = [0, 1, 2, 3]               # Four items: indexes 0..3
	L3 = ['abc', ['def', 'ghi']]    # Nested sublists
	L2[0]                           # 0; L2[-3] => 1
	L3[0][1]                        # 'b'
	L3[1][1]                        # 'ghi'
	L2[0:1]                         # [0] 
	L2[0:3]                         # [0, 2, 3]; L2[2:] => [2, 3]
	len(L2)                         # 4
	
	L2 + L3                         # Concatenation -> [0, 1, 2, 3, 'abc', ['def', 'ghi']]
	L2 * 3                          # Repetition -> [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3] 
	for x in L2: print(x)           # Iteration
	3 in L2                         # Membership -> True (False)
	
	L2.append(4)                    # [0, 1, 2, 3, 4]
	L2.extend([5,6,7])              # [0, 1, 2, 3, 4, 5, 6, 7]
	L2.sort()                       # [0, 1, 2, 3, 4, 5, 6, 7]
	L2.index(1)                     # 1
	L2.reverse()                    # [7, 6, 5, 4, 3, 2, 1, 0]
	del L2[6]                       # [0, 1, 2, 3, 4, 5, 7]
	del L2[4:6]                     # [0, 1, 2, 3, 7]
	L2.pop()                        # 7, leaving [0, 1, 2, 3]
	
	L2[1] = 2                       # [0, 2, 2, 3]
	L2[1:2] = [1,4]                 # [0, 1, 4, 2, 3]
	L5 = range(4)                   # [0, 1, 2, 3]
	
	for x in xrange(0,4): print x   # return object (not list) slightly faster
	L4 = [x**2 for x in range(5)]   # [0, 1, 4, 9, 16]
	
	textstr = ''.join(map(str, L2)) # convert List into a string concateneated with ''
	isinstance(L1, list)            # list object? 
	
Dictionaries
============

* mutable
* unordered collections of abitrary objects, accessed by key
* variable length, hetrogeneous, aribtrarily nestable


::

	D1 = {}                               # Empty dictionary
	D2 = {'spam': 2, 'eggs': 3}           # {'eggs': 3, 'spam': 2}
	D3 = {'food': {'ham': 2, 'eggs': 3}}  # {'food': {'eggs': 3, 'ham': 2}}
	D2['eggs']                            # 3; D2.get('eggs') => 3
	D3['food']['ham']                     # 2; D3['food'] => {'eggs': 3, 'ham': 2}
	D2.has_key('eggs'), 'eggs' in D2      # True, 'eggs' in D3 => False
	
	D2.keys()                             # ['eggs', 'spam']
	D2.values()                           # [3, 2]
	D3.keys()                             # ['food']; D3['food'].keys() => ['eggs', 'ham']
	D3.values()                           # [{'eggs': 3, 'ham': 2}]; D3['food'].values() => [3, 2]
	D2.items()                            # [('eggs', 3), ('spam', 2)]

	D4 = D2.copy()
	D2.update(D3)                         # {'food': {'eggs': 3, 'ham': 2}, 'eggs': 3, 'spam': 2}
	
	len(D2)                               # 3; len(D1) => 0; len(D3) => 1
	
	keys = ['spam', 'eggs']               # or tuple: keys = ('spam', 'eggs')
	vals = [2, 3]                         # or tuple: vals = (2, 3)
	D4 = dict(zip(keys, vals))            # {'eggs': 3, 'spam': 2}
	
	isinstance(D3, dict)                  # True
    isinstance(D3['food'], dict)          # True
    isinstance(D3['food']['eggs'], dict)  # False

	
Tuples
======

* ordered collections of abitrary objects, accessed by offset
* variable length, hetrogeneous, aribtrarily nestable
* can be used as dictionary keys

::

	t0 = ()                         # Empty tuple
	t1 = (0,)                       # one-item tuple (not an expression)
	t2 = (0, 'Ni', 1.2, 3)          # four-item tuple
	t2 = 0, 'Ni', 1.2, 3            # four-item tuple (alternative syntax)
	t3 = ('abc', ('def', 'ghi'))    # ('abc', ('def', 'ghi'))
	
	t1 = (42,)                      # tuple
	t1 = (42)                       # integer
	
	t1[0]                           # 0
	t3[0]                           # 'abc'; t3[1] => ('def', 'ghi')
	t3[0][1]                        # 'b'
	t3[1][1]                        # 'ghi'
	t3[0:1]                         # ('abc',); t3[0:] => ('abc', ('def', 'ghi'))
	
	len(t2)                         # 4; len(t0) => 0, len(t1) => 1, len(t3) => 2
	
	tx = t1 + t2                    # (0, 0, 'Ni', 1.2, 3)
	tx = t2 * 3                     # (0, 'Ni', 1.2, 3, 0, 'Ni', 1.2, 3, 0, 'Ni', 1.2, 3)
	
	for x in t2 : print x           # Iteration
	3 in t2                         # True, 'Ni' in t2 => True, 4 in t2 => False
	
Files
=====

* `Input and Output <https://docs.python.org/3/tutorial/inputoutput.html>`_
* `Wrting files using Python <https://stackabuse.com/writing-files-using-python/>`_
* `Python 101: Redirecting stdout <https://www.blog.pythonlibrary.org/2016/06/16/python-101-redirecting-stdout/>`_


Sequential access::

	output = open('tmp/spam', 'w')  # create/overwrite output file
	input = open('data', 'r')       # open input file
	S = input.read()				# Read entire file into a single string
	S = input.read(N)               # Read N bytes ( N >= 1)
	S = input.readline()            # Read next line, len(S) == 0 when no more input
	L = input.readlines()           # Read entire file into list of line strings
	output.write(S)                 # Write string S into file (returns number of chars written)
	output.writelines(L)            # Write all strings in list L
	print("lineFour", file=output)  # Better than low-level write(), writelines() methods
	output.flush()                  # Flush buffered write to file
	output.close()                  # May need to flush() to write contents
	
	# Cleaner but will raise an exception and close cleanly
	with open(filename) as f:
		data = f.read()

	# Cleaner and will trap any exception raised
	try:
		with open(filename) as f:
		data = f.read()
	except Exception as error:	
		print('{0}'.format(error))


Random access::

    # "Anchovies? You've got the wrong man! I spell my name DANGER! (click)"
    # %
    # "Benson, you are so free of the ravages of intelligence."
    #         ― Time Bandits
    # %

    with open(filename, 'r') as fd:
	    current_offset = fd.tell()  # save file cursor
	    fd.seek(offset)
	    cookie_text = fd.readline()

		# Cannot use for..loop and .tell() method, use repeat..until loop
	    while True:
	        line = fd.readline()
	        if not line:
	            break
	        elif re.match(r'^%$', line):
	            break
	        else:
	            cookie_text += line
	
	    fd.seek(current_offset)  # restore file cursor

       
Comparisons, Equality, and Truth
================================

::

	L1 = [1, ('a', 3)]
	L2 = [1, ('a', 3)]
	L3 = L1
	L1 == L2, L1 is L2                   # (True, False); Not the same object
	L1 == L2, L1 is L2, L1 > L2, L2 > L1 # (True, False, False, False)
	L1 == L3, L1 is L3                   # (True, True); Are the same object
	
	S1 = 'spam'
	S2 = 'spam'
	S1 == S2, S1 is S2     # (True, True); WTF evil-bad caching! so same object
	
	S1 = 'a longer string'
	S2 = 'a longer string'
	S1 == S2, S1 is S2     # (True, False)
	
Object Checking
===============

List of classinfo types::
	
	print([t.__name__ for t in __builtins__.__dict__.values() if isinstance(t, type)])
	
	['BuiltinImporter', 'bool', 'memoryview', 'bytearray', 'bytes', 'classmethod', 'complex', 
	'dict', 'enumerate', 'filter', 'float', 'frozenset', 'property', 'int', 'list', 'map', 
	'object', 'range', 'reversed', 'set', 'slice', 'staticmethod', 'str', 'super', 'tuple', 
	'type', 'zip', 'BaseException', 'Exception', 'TypeError', 'StopAsyncIteration', 
	'StopIteration', 'GeneratorExit', 'SystemExit', 'KeyboardInterrupt', 'ImportError', 
	'ModuleNotFoundError', 'OSError', 'OSError', 'OSError', 'EOFError', 'RuntimeError', 
	'RecursionError', 'NotImplementedError', 'NameError', 'UnboundLocalError', 
	'AttributeError', 'SyntaxError', 'IndentationError', 'TabError', 'LookupError', 'IndexError', 
	'KeyError', 'ValueError', 'UnicodeError', 'UnicodeEncodeError', 'UnicodeDecodeError', 
	'UnicodeTranslateError', 'AssertionError', 'ArithmeticError', 'FloatingPointError', 
	'OverflowError', 'ZeroDivisionError', 'SystemError', 'ReferenceError', 'MemoryError', 
	'BufferError', 'Warning', 'UserWarning', 'DeprecationWarning', 'PendingDeprecationWarning', 
	'SyntaxWarning', 'RuntimeWarning', 'FutureWarning', 'ImportWarning', 'UnicodeWarning', 
	'BytesWarning', 'ResourceWarning', 'ConnectionError', 'BlockingIOError', 'BrokenPipeError', 
	'ChildProcessError', 'ConnectionAbortedError', 'ConnectionRefusedError', 
	'ConnectionResetError', FileExistsError', 'FileNotFoundError', 'IsADirectoryError', 
	'NotADirectoryError', 'InterruptedError', 'PermissionError', 'ProcessLookupError', 
	'TimeoutError']

Object is::

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
	isinstance(L, (list, tuple))          # True
	isinstance(T, (list, tuple))          # True

IF statements
=============

::

	if <test1> :
		<statements1>
	elif <test2> :
		<statements2>
	else :
		<statements3>

	{ 'spam' : 1.25, 'ham' : 1.99, 'eggs' : 0.99, 'bacon' : 1.10}['ham'] # 1.99
	
	a if <test> else b # ternary operator
	
While Loops
===========

::

	while <test1>:
		<statements>
		if <test2> : break     # break out of (nested) loop
		if <test3> : continue  # skip loop start
	else :
		<statement>            # if we did not hit break (or loop not entered)


For Loops
=========

::

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

Objects
=======

Simple **Person** object in file named *Person.py* ::

	#!/usr/bin/env python3
	#
	import os
	
	class Person:
		__NEXT_UUID = 0
		def __init__(self, name, age, sex='M'):
			self.__name = name
			self.__age = age
			self.__sex = sex
			Person.__NEXT_UUID += 1
			self.__uuid = Person.__NEXT_UUID
		
		def get_name(self):
			return self.__name
		
		def set_name(self, value):
			self.__name = value
		
		def get_age(self):
			return self.__age
		
		def set_age(self, value):
			self.__age = value
		
		def get_sex(self):
			return self.__sex
		
		def set_sex(self, value):
			self.__sex = value
		
		def get_uuid(self):
			return self.__uuid
		
		def __str__(self):
			''' String representation '''
			__str = ''
			__str += str(self.__name) + ', '
			__str += str(self.__age) + ', '
			__str += str(self.__sex) + ', '
			__str += str(self.__uuid)
			return __str
		
		def __repr__(self):
			''' YAML like string representation '''
			 __str = ''
			 __str += "{0:<13s}: {1}".format('name', self.__name) + os.linesep
			 __str += "{0:<13s}: {1}".format('age', self.__age) + os.linesep
			 __str += "{0:<13s}: {1}".format('sex', self.__sex) + os.linesep
			 __str += "{0:<13s}: {1}".format('uuid', self.__uuid)
			 return __str
		
		# property(fget=None, fset=None, fdel=None, doc=None)	
		username = property(get_name, set_name, None, None)
		age = property(get_age, set_age, None, None)
		sex = property(get_sex, set_sex, None, None)
		version = property(get_uuid, None, None, None)
		
The **Person** object supports Python attribute style and also Java-like getters/setters style  ::

	>>> import Person
	>>> f = Person.Person(name='fred',age=99)
	>>> b = Person.Person(name='barney',age=9)
	>>> b.__str__()
	'barney, 9, M, 2'
	>>> f.__repr__()
	'name         : fred\nage          : 99\nsex          : M\nuuid         : 1'
	>>> f.name='freddy'
	>>> f.name
	'freddy'
	>>> f.get_name()
	'freddy'
	>>> f.uuid
	1
	>>> f.uuid = 99
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: can't set attribute

Try/Except
==========

::

	import sys
	
	for arg in sys.argv[1:]:
	    try:
	        f = open(arg, 'r')
	    except OSError:
	        print('cannot open', arg)
	    else:
	        print(arg, 'has', len(f.readlines()), 'lines')
	        f.close()
	
	# Clumsy file handling
	try:
	    f = open('myfile.txt')
	    s = f.readline()
	    i = int(s.strip())
	except OSError as err:
	    print("OS error: {0}".format(err))
	except ValueError:
	    print("Could not convert data to an integer.")
	except:
	    print("Unexpected error:", sys.exc_info()[0])
	    raise
	finally:
		print("always executed exception or not")	    

	# Better using the predefined clean-up actions	    
	with open("myfile.txt") as f:
	    for line in f:
	        print(line, end="")

Decorators
==========

A decorator is a function that takes another function and extends the behavior of the latter function without
explicitly modifying it, a kind of *wrapper*.

* `Primer on Python Decorators <https://realpython.com/primer-on-python-decorators/>`_
* `Decorators in Python <https://www.geeksforgeeks.org/decorators-in-python/>`_
* `Python Decorators Tutorial <https://www.datacamp.com/tutorial/decorators-python>`_
* `PEP 318 – Decorators for Functions and Methods <https://peps.python.org/pep-0318/>`_

Basic example
-------------

::

    >>> def add_one(number):
    ...     return number + 1
    ...
    >>> add_one(42) # 43

Functions as arguments (say_hello, say_hi)
------------------------------------------

::

    >>> def say_hello(name):
    ...     return f"Hello {name}"
    ...
    >>> def say_hi(name):
    ...     return f"Hi {name}"
    ...

    >>> say_hello("Fred") # 'Hello Fred'
    >>> say_hi("Fred")    # 'Hi Fred'
    >>> say_hello         # <function say_hello at 0x000001C8E4F6E9D0>
    >>> say_hi            # <function say_hi at 0x000001C8E4F6EB80>

    #
    >>> def greet_fred(greeting):
    ...     return greeting("Fred")
    ...

    >>> greet_fred(say_hello) # 'Hello Fred'
    >>> greet_fred(say_hi)    # 'Hi Fred'

Functions and Methods
---------------------

::

    >>> def my_decorator(func):
    ...     def wrapper(*args,**kwargs):
    ...             print("before execution")
    ...             ans = func(*args,**kwargs)
    ...             print("after execution")
    ...             return ans
    ...     return wrapper

    >>> @my_decorator
    ... def add_numbers(a, b):
    ...     print("inside the function")
    ...     return a + b
    ...
    >>> print(add_numbers(4,5))
    before execution
    inside the function
    after execution
    9

Heapq
=====

* `builtin heap implementation <https://docs.python.org/3.0/library/heapq.html>`_

::
	
	import heapq
	
	heap = []
	data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
	for item in data:
	    heapq.heappush(heap, item)
	
	heap = [11, 3, 15, 7, 9, 23, 4, 6, 8, 10]
	heapq.heapify(heap)
	
	print('nlargest(3): {0}'.format(heapq.nlargest(3, heap)))
	print('nsmallest(3): {0}'.format(heapq.nsmallest(3, heap)))
	
	smallest_item = heapq.heappop(heap)
	
	# convert to sorted list
	ordered = []
	while heap:
	    ordered.append(heapq.heappop(heap))
	
	# heap of tuples
	data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
	for item in data:
	    heapq.heappush(heap, item)

	        
Pipenv
======

* `Pipenv <https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv>`_
* `Basic Usage <https://pipenv.readthedocs.io/en/latest/>`_
* `Advanced Usage <https://pipenv.readthedocs.io/en/latest/advanced/#configuration-with-environment-variables>`_
* `Which VirtualEnv <https://github.com/pypa/pipenv/issues/796>`_

Using pipenv with Eclipse PyDev
::

	$ export PIPENV_VENV_IN_PROJECT=1 # force creation of '.venv' in project
	$ cd <eclipse-workspace>/<project>
	$ pipenv --three             # python3 project
	$ pipenv install <package>   # updates the Pipfile
	$ pipenv uninstall <package> # updates the Pipfile
	$ pipenv --rm                # remove virtualenv
	$ pipenv shell               # virtualenv interactive shell 
	$ pipenv run <program.py>    # virtualenv: run script 
	$ pipenv check               # PEP8 check of the Pipfile

	
Setup a new Python interpretor in Eclipse, and change the project to use it.

* `PyDev and virtualenv <https://www.michaelpollmeier.com/eclipse-pydev-and-virtualenv>`_
	
	
	



