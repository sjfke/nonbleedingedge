****************
Perl Cheatsheet
****************

Useful Links
=============

* `Perl <https://www.perl.org/docs.html>`_
* `Perldoc Documentation <http://perldoc.perl.org/>`_
* `Perl meta::cpan <https://metacpan.org/>`_
* `Perl Online books <https://www.perl.org/books/library.html>`_


Perl perlreftut
===============

* `perlreftut <http://perldoc.perl.org/perlreftut.html>`_ tutorial
* `perlref <http://perldoc.perl.org/perlref.html>`_ manual

Make Rule 1
-----------
::

	$aref = \@array;    # $aref now holds a reference to @array
	$href = \%hash;     # $href now holds a reference to %hash
	$sref = \$scalar;   # $sref now holds a reference to $scalar

Once the reference is stored in a variable like $aref or $href, you can::

	$xy = $aref;      # $xy now holds a reference to @array
	$p[3] = $href;    # $p[3] now holds a reference to %hash
	$z = $p[3];       # $z now holds a reference to %hash

Make Rule 2
-----------

Anonymous

* [ ITEMS ] creates an anonymous array, and returns a ref
* { ITEMS } creates an anonymous hash, and returns a ref

::

	$aref = [ 1, "foo", undef, 13 ];    # $aref now holds a reference to an array
	$href = { APR => 4, AUG => 8 };     # $href now holds a reference to a hash

	Note: $aref = [ 1, 2, 3 ]; is equivalent to:
	  @array = (1, 2, 3);
	  $aref = \@array;

Use Rule 1
----------

* { dereference }

+------------------------+------------------------------+------------------------+
|Arrays                  |perlref                       |Comment                 |
+========================+==============================+========================+
|@a;                     |@{$aref};                     |An array                |
+------------------------+------------------------------+------------------------+
|reverse @a;             |reverse @{$aref}              |Reverse the array       |
+------------------------+------------------------------+------------------------+
|$a[3];                  |${$aref}[3]                   |An element of the array |
+------------------------+------------------------------+------------------------+
|$a[3] = 17;             |${$aref}[3] = 17              |Assigning an element    |
+--------------------------+----------------------------+------------------------+
|for my $element (@array) {|for my $element (@{$aref}) {|Hint: s/array/{\$aref}/g|
|  ...                     |   ...                      |                        |
|}                         |}                           |                        |
+--------------------------+----------------------------+------------------------+

+----------------------------------+-------------------------------------+--------------------------+
|Hashes                            |                                     |                          |
+==================================+=====================================+==========================+
|%h;                               |%{$href}                             |A hash                    |
+----------------------------------+-------------------------------------+--------------------------+
|keys %h;                          |keys %{$href}                        |Get the keys from the hash|
+----------------------------------+-------------------------------------+--------------------------+
|$h{'red'};                        |${$href}{'red'}                      |An element of the hash    |
+----------------------------------+-------------------------------------+--------------------------+
|$h{'red'} = 17;                   |${$href}{'red'} = 17                 |Assigning an element      |
+----------------------------------+-------------------------------------+--------------------------+
|for my $key (keys %hash) {        |for my $key (keys %{$href}) {        |Hint: s/hash/{\$href}/g   |
|    print "$key => $hash{$key}\n";|    print "$key => ${$href}{$key}\n";|                          |
|}                                 |}                                    |                          |
+----------------------------------+-------------------------------------+--------------------------+


Use Rule 2
----------

* "Use Rule 1" cumbersome, more elegant syntax
::

	${$aref}[3];     $aref->[3]           # instead
	${$href}{red};   $href->{red}         # instead

Warning::

	$aref[3]     # 4th element of deceptively named array @aref (i.e $aref(reference) and @aref(array) are unrelated)
	$href{'red'} # part of deceptively named hash %href         (i.e $href(reference) and %href(hash) are unrelated)

