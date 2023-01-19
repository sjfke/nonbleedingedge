:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/outdated/javascript.rst

*********************
JavaScript Cheatsheet
*********************

Comments
========
::

	// everything up to end of line.
	
	/*
	Multi-line comment
	Note does not need *-prefix on enclosed lines
	*/

String Methods:
===============

Useful Links:

* `String Methods <http://www.w3schools.com/js/js_string_methods.asp>`_
* `String Objects <http://www.w3schools.com/jsref/jsref_obj_string.asp>`_

::

    var pos = str.indexOf(“findme”);     // first occurrence 0..N, -1 not found
    var pos = str.lastIndexOf(“findme”); // last occurrence 0..N, -1 not found
    var pos = str.search(“regexStr”);    // first occurrence 0..N, -1 not found

::

    var str = "Apple, Banana, Kiwi";
    var res = str.slice(7,13);     // “Banana”
    var res = str.slice(-12,-6);   // “Banana” (index from end of string)
    var res = str.slice(7);        // “Banana, Kiwi”
    var res = str.slice(-12);      // “Banana, Kiwi” (index from end of string)
    var res = str.substring(7,13); // “Banana” (+ve index only).
    var res = str.substring(7);    // “Banana, Kiwi” (+ve index only)
    var res = str.substr(7,6);     // "Banana" substr(start, length)
    var res = str.substr(-12,6);   // "Banana" substr(start, length)

::

    str = "Please visit Microsoft!";
    var n = str.replace("Microsoft","Yahoo");  // Str: ”Please visit Yahoo!”; str unchanged.
    var n = str.replace(/Microsoft/g,"Yahoo"); // RegEx: ”Please visit Yahoo!”; str unchanged.

::

    var text1 = "Hello World!";
    var text2 = text1.toUpperCase();        // text2 is text1 converted to upper
    var text2 = text1.toLowerCase();        // text2 is text1 converted to lower
    var text2 = text1.toLocaleLowerCase();  // text2 is text1 converted to lower
    var text2 = text1.toLocaleUpperCase();  // text2 is text1 converted to upper


Split / Join strings

::

    var txt = "a,b,c,d,e";   // String
    txt.split(",");          // Split on commas, ["a", "b", "c", "d", "e"]
    txt.split("")            // Split on chars, ["a", ",", "b", ",", "c", ",", "d", ",", "e"]

    var text1 = "Hello";
    var text2 = "World";
    var text3 = text1.concat(" ",text2);
    var text3 = text1 + “ “ + text2;

Indexing strings (accessing string as an array is unsafe!)

::

    var str = "HELLO WORLD";  // Accessing string as an array is unsafe!
    str.charAt(0);            // returns H
    str.charCodeAt(0);        // returns 72

Searching strings

::

    var text1 = "Hello World!";
    text1.startsWith("Hello");         // true
    text1.endsWith('World!');          // true

    var text2 = " a,b,c,d,e ";
    var str = text2.trim();            // trim leading/trailing white-space, ”a,b,c,d,e”
    text2.includes('c,d');             // Str: true (RegEx no-work)
    var matches = text2.match(/c,d/);  // RegEx: returns matches, [“c,d”]

Objects - Nested
================
::

    > obj = {'Jan':{}, 'Feb':{}}
    > obj.Jan['a']="why"
    > obj.Feb=[{c: "yes", d: "no"},{e: "yes", f: "no"}]
    > obj.Feb.push({e: "yes", f: "no"})
    > obj['Mar']=[{"a":"why","b":"not"}]
    > obj['Mar'].push({"c":"may","d":"be"})
    > var jsonStr = JSON.stringify(obj)
    > jsonStr
    "{"Jan":{"a":"why"},"Feb":[{"c":"yes","d":"no"},{"e":"yes","f":"no"},{"e":"yes","f":"no"}],"Mar":[{"a":"why","b":"not"},{"c":"may","d":"be"}]}"

Comment Block
=============
::

    <!--
     var chartView = new google.visualization.DataView(data);
     chartView.setColumns([0,2,5,8]);
     chart.setDataTable(chartView);
    // -->

Ternary operator
================
::

    "The fee is " + (isMember ? "$2.00" : "$10.00")

querySelectorAll: finding all elements on a page
================================================
::

    x = document.querySelectorAll("input[type='checkbox']"); // finds all the checkboxes.

