:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/php.rst

**************
PHP CheatSheet
**************

General Notes
=============

Perl split type functions::

	$words = explode(" ", "hypertext language, programming");
	$words = preg_split("/[\s,]+/", "hypertext language, programming");

Equiv on Linux seq::

	range($start, $end [, $step = 1 ]);

`Null, Empty isset() <https://www.virendrachandak.com/techtalk/php-isset-vs-empty-vs-is_null/>`_
::

	(bool) is an array, a numeric/float/int/string/object
	is_array( $var );
	is_numeric( $var );
	is_float( $var );
	is_int( $var ); (is_integer)
	is_string( $var );
	is_object( $var );

End of line::

	PHP_EOL (cf. “\n”;)

Ternary operator::

	$var_is_greater_than_two = ($var > 2 ? true : false);

String operations
=================
::

	strlen ( $str )
	ucfirst( $str )
	lcfirst( $str )
	ucwords( $str )
	strtolower( $str )
	strtoupper( $str )
	substr( $str , $start [,$length] ); #  shorten a string
	str_replace( $search , $replace , $subject [, $count ] ) # Replace all occurrences 'search' string 'replace' string
	strstr( $haystack , $needle [,$before_needle = false ] ) # Find the first occurrence of a string
	stristr( $haystack , $needle [,$before_needle = false ] ) # Case-insensitive strstr()
	sprintf( "format", $str ); # sprintf as in other languages.
	trim( $str ); # strip leading/trailing white-space (ltrim(), rtrim()) 

Numeric operations
==================
::

	ceil($float)  # round up
	floor($float) # round down
	round($float[,$precision]) # round, PHP_ROUND_HALF_UP, PHP_ROUND_HALF_DOWN, PHP_ROUND_HALF_EVEN, PHP_ROUND_HALF_ODD
	(float) $float # trims trailing zeros

Date/Time formatting
====================
::

	$today = getdate(); # $today[‘seconds’,’minutes’,’hours’,’mday’,’wday’,’mon’,’year’,’yday’,’weekday’,’month’,0]
	strftime ($format, $timestamp) # http://php.net/manual/en/function.strftime.php

Currency formatting
===================
::

	setlocale(LC_MONETARY, 'en_US');
	echo money_format('%.2n', $number) . "\n";

HTML operations
===============
::

	$data = array('foo'=>'bar', 'baz'=>'boom','cow'=>'milk','php'=>'hypertext processor');
	$query_str = http_build_query($data) # build HTTP request query part
	$url = 'select.php?' . htmlentities($query_str);
	
	$array = $parse_url($url); # keys: scheme host port user pass path query fragment
	# query - after the question mark ?;  fragment - after the hashmark # 
	
	$str = $parse_url($url, $what); # PHP_URL_SCHEME, PHP_URL_HOST, PHP_URL_USER, PHP_URL_PASS, PHP_URL_PATH, PHP_URL_QUERY PHP_URL_FRAGMENT 
	$int = $parse_url($url, PHP_URL_PORT);


Arrays crash course
===================
::

	array_key_exists($key, $array); # equiv of Perl exists
	$arr0 = array(); # empty array
	
	unset($array); $array = array (); # clearing array contents, unset and re-create
	
	$arr1 = array ( 0 => 'fred', 1 => 'barney' ); # creating a populate array
	$arr2 = array ( 'fred' => 'flintstone', 'barney' => 'rubble'); # creating a populate array
	
	$arr1[0] = "fred"; # array element assignment
	$arr1[1] = "barney"; # array element assignment
	$arr2['fred'] = "flintstone"; # array element assignment
	$arr2['barney'] = "rubble"; # array element assignment
	
	var arr1 = array();
	foreach (range(0, 12) as $int) {
		arr1[] = $int;
	}
	
	$int = count($array); # number of elements
	in_array ( mixed $needle , array $haystack [, bool $strict = FALSE ] ) # Checks if a value exists in an array

Relative array index
====================
::

	$value = current($array);
	$value = next($array);
	$value = prev($array);
	$value = end($array); # last element

Looping over an array
=====================
::

	foreach ($arr1 as $value) {
		echo $value; # fred, barney
	}

	foreach ($arr2 as $key => $value) {
		echo "$key:$value "; # fred:flintstone barney:rubble
	}

Skipping to next foreach iteration
==================================
::
 
	continue; # equivalent of Perl next;

Perl-like split/join operators
==============================
::

	explode ( string $delimiter , string $string [, int $limit ] ) # simple split
	preg_split ( string $pattern , string $subject [, int $limit = -1 [, int $flags = 0 ]] ) # split with regex like Perl
	implode ( string $glue , array $pieces ); # join, $glue defaults to empty string
	list ( mixed $var1 [, mixed $... ] ); # one line assignment so Perl like split into a list.
	list($drink, $color, $power) = explode(', ' , "coffee, brown, caffeine");

Week numbers
============
::

	$datestr = str_replace(".", "/", '2014.10.26');
	$sdate = strtotime($datestr);
	$week = 'Wk' . date('W', $sdate);


Random Notes
============
::

	<?php echo "Hello my good web browser" ; ?> # <? ... ?> form is deprecated >= PHP5
	
	# comment, CANNOT be on same line as PHP code
	// comment, CAN be added to the end of the PHP code line
	/* ... */ multi-line comment block

Variables
=========
::

	$ + (_[a-zA-Z]) + (_[a-zA-Z0-9)* and are CASE Sensitive
	$firstname, $FirstName, $_a1, $_2, etc
	$this reserved for Object Orientated PHP.
	# globally scoped unless inside a function

	Data-Types:
	- Boolean        - (TRUE|FALSE)
	- Integer        - whole numbers
	- Float (double) - 12.56 ..
	- String         - characters, letter, or numbers in ".." or '..' 
	- Array          - multi-dimenstional arrays
	- Object         - basics for class definitions
	- NULL           - like MySQL
	- Resource       - reference to functions, databases, files outside of PHP

Defined Constants
=================
::

	delcared using define()
	global scope
	(_[a-zA-Z]) + (_[a-zA-Z0-9)* and are CASE Sensitive, convention use UPPERCASSE
	define("SYS_OWNER", "Peter");
	echo "System owner is:" . SYS_OWNER . "<br/>" ;

Expressions - collective term for code statements
=================================================
::

	examples, NB function returns value => expression 
	function myName() {
	   Return "Peter";
	}
	$name = MyName();
	$name ? $last = "MacIntyre" : $last = "" ;

If...Then...Else...
===================
::

	Note with: '==' the string is converted to a number prior to comparison (passes)
	Note with:  '===' no conversion compared on content and type (fails on type: number vs string)
	
	if (1 == '1') echo "true 1 equals '1' <br/>";
	
	if (1 === '1') echo "true 1 equals '1'";
	else echo "false 1 does not equal '1' " ;
	
	Better form than one-line form above:
	
	if ($weekday == "Monday") {
	    $discount = $tax_rate * 0.05 ;
	}
	
	if ($weekday == "Monday") {
	    $discount = $tax_rate * 0.05 ;
	}
	else {
	    $discount = $tax_rate * 0.25 ;
	}
	
	if ($weekday == "Monday") {
	    $discount = $tax_rate * 0.05 ;
	} elseif ($weekday == "Tuesday") {
	    $discount = $tax_rate * 0.06 ;
	} elseif ($weekday == "Wednesday") {
	    $discount = $tax_rate * 0.07 ;
	} elseif ($weekday == "Thursday") {
	    $discount = $tax_rate * 0.08 ;
	} elseif ($weekday == "Friday") {
	    $discount = $tax_rate * 0.09 ;
	} elseif ($weekday == "Saturday" || $weekday == "Sunday") {
	    $discount = $tax_rate * 0.10 ;
	}


Switch...Case
=============
::

    $today = date("l") ;
    if ($today == "Monday")     { $tax_rate += 2 ; }
    if ($today == "Tuesday")    { $tax_rate += 3 ; }
    if ($today == "Wednesday")  { $tax_rate += 4; }
    if ($today == "Thursday")   { $tax_rate += 5 ; }
    if ($today == "Friday")     { $tax_rate += 6 ; }
    if ($today == "Saturday")   { $tax_rate += 7 ; }
    if ($today == "Sunday")     { $tax_rate += 8; }

    switch ($today) {
        case "Monday" :
            $tax_rate += 2 ;
            $wages = $salary * 0.2 ;
            $msg_color = "red" ;
            break;
        case "Tuesday" :
            $tax_rate += 3 ;
            $wages = $salary * 0.3 ;
            $msg_color = "yellow" ;
            break;
        case "Wednesday" :
            $tax_rate += 4 ;
            $wages = $salary * 0.4 ;
            $msg_color = "black" ;
            break;
        case "Thursday" :
            $tax_rate += 5 ;
            $wages = $salary * 0.5 ;
            $msg_color = "green" ;
            break;
        case "Friday" :
            $tax_rate += 6 ;
            $wages = $salary * 0.6 ;
            $msg_color = "orange" ;
            break;
        case "Saturday" :
        case "Sunday" :
            $tax_rate += 7 ;
            $wages = $salary * 0.7 ;
            $msg_color = "purple" ;
            break;
        }


While...
========
::

	# typical while loop
	$repeat = 1 ;
	while ($repeat <= 25) {
	    echo "the counter is: " . $repeat . "<br/>" ;
	    $repeat ++ ;
	}
    
	# typical repeat loop
	$repeat = 0 ;
	do {
	    $repeat ++ ;
	       echo "the counter is: " . $repeat . "<br/>" ;
	} while ($repeat <= 25);

For...
======
::

	# typical for loop (foreach also exists)
	for ($i = 0; $i <= 25; $i++) {
	    echo "the counter is: " . $i . "<br/>" ;
	}

