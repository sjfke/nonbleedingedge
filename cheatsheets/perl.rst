****************
Perl Cheatsheet
****************

Useful Links
=============

* `Perl <https://www.perl.org/docs.html>`_
* `Perldoc Documentation <http://perldoc.perl.org/>`_
* `Perl meta::cpan <https://metacpan.org/>`_
* `Perl Tutorialspoint <https://www.tutorialspoint.com/perl/perl_introduction.htm>`_
* `Perl Online books <https://www.perl.org/books/library.html>`_
* `Perl DateTime <https://metacpan.org/pod/DateTime>`_


Perl Reference Tutorial
=======================

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

Deferencing an array reference::

	
	Perl                           Perlref                       Notes
	----                           -------                       -----
	@a;                            @{$aref};                     # An array
	reverse @a;                    reverse @{$aref}              # Reverse the array
	$a[3];                         ${$aref}[3]                   # An array element
	$a[3] = 17;                    ${$aref}[3] = 17              # Assigning to an element
	
	for my $element (@array) {     for my $element (@{$aref})    # Hint: s/array/{\$aref}/g
	  ...                              ...
	}                              }


Dereferencing a hash reference::


	Perl                                 Perlref                                 Notes
	----                                 -------                                 -----
	%h;                                  %{$href}                               # A hash
	keys %h;                             keys %{$href}                          # Get the keys from hash
	$h{'red'};                           ${$href}{'red'}                        # An element of the hash
	
	for my $key (keys %hash) {           for my $key (keys %{$href}) {          # Hint: s/hash/{\$href}/g
	    print "$key => $hash{$key}\n";       print "$key => ${$href}{$key}\n";
	}                                    }                                    


Use Rule 2
----------

* "Use Rule 1" cumbersome, more elegant syntax

::

	Perlref               Elegant Perlref
	-------               ---------------
	${$aref}[3];          $aref->[3]           # instead
	${$href}{'red'};      $href->{'red'}         # instead

	for my $key (keys %{$href}) {
	    print "$key => $href->{$key}\n";
	}                                    

Warning::

	$aref[3]     # 4th element of deceptively named array @aref (i.e $aref(reference) and @aref(array) are unrelated)
	$href{'red'} # part of deceptively named hash %href         (i.e $href(reference) and %href(hash) are unrelated)

Building a hash from an array
=============================

* `Perl Arrays <http://www.tutorialspoint.com/perl/perl_arrays.htm>`_

::
	
	my @array('fred', 'barney', 'wilma', 'betty');
	my %hash = map { $_, 1 } @array;    # convert to hash.
	# my %hash {'wilma' => 1, 'betty' => 1, 'barney' => 1, 'fred' => 1};
	
	my @array('fred', 'barney', 'wilma', 'betty');
	my $i =0; 
	my %hash = map { $_, $i++ } @array; # ‘fred’ => 0, ‘barney’ => 1 etc.
	# %hash = {'fred' => 0, 'barney' => 1, 'wilma' => 2, 'betty' => 3};
	
	# create a value sorted array from the hash
	my @stats_indices;
	foreach my $key (sort { $stats_hash{$a} <=> $stats_hash{$b} } keys %stats_hash) {
	   push(@stats_indices, $stats_hash{$key};
	}
   

Perl Excel Spreadsheet
======================

* Writing Excel: ``Excel::Writer::XLSX (plugin-replacement for Spreadsheet::WriteExcel)``

  * `Excel::Writer::XLSX <https://metacpan.org/pod/Excel::Writer::XLSX>`_
  
* Reading Excel: ``Spreadsheet::ParseExcel``

  * `Spreadsheet-ParseExcel <https://metacpan.org/pod/Spreadsheet::WriteExcel>`_


Perl DBI
========

* `Perl DBI <https://dbi.perl.org/>`_
* `Perldoc DBI <https://metacpan.org/pod/DBI>`_

Perl DBI DB connection::

	my $dsn = "DBI:mysql:host=$dbhost:database=$dbase";
	my $dbh = DBI->connect( $dsn, $dbuser, $dbpass ) or die("Connot connect to $dbhost:$dbase");

Perl DBI Select Examples::

	my @array;
	my $sth = $dbh->prepare("SELECT DISTINCT $column FROM $table") or die $dbh->errstr;
	$sth->execute() or die $sth->errstr;
	while ( my @row = $sth->fetchrow_array ) {
	   push( @array, $row[0] );
	}
	
	my %hash = map { $_, 1 } @array;
	my $sth = $dbh->prepare("SELECT id,name FROM $table") or die $dbh->errstr;
	$sth->execute() or die $sth->errstr;
	while ( my @row = $sth->fetchrow_array ) {
	   if (exists $hash{$row[1]}) {
	      $hash{$row[1]} = $row[0];
	   } else {
	      $hash{$row[1]} = -1; # should not happen
	   }
	}

Perl DBI Insert Examples::

	my $prefix = "INSERT INTO " . $table . " (name)";
	my $qry = "$prefix VALUES (?)";
	my $sth = $dbh->prepare($qry);
	
	my @values;
	push( @values, $name );
	print("$prefix VALUES (". join (',', @values) . ")\n"), if ( $verbose > 1 );
	my $affected = $sth->execute(@values) or $log->logdie( $sth->errstr );
	my $id = $dbh->{'mysql_insertid'}; # returns AUTO_INCREMENT ID, caution lock table if multi-user/threaded app.
	
	if ($force_update) {
	   $prefix = "REPLACE INTO $metro_traffic_table (metroid,out99pct,outsum,ctime,ymd)";
	} else {
	   $prefix = "INSERT IGNORE INTO $metro_traffic_table (metroid,out99pct,outsum,ctime,ymd)";
	}

