:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/mysql.rst

****************
MySQL Cheatsheet
****************

Useful Links
=============

* `Developer Zone MySQL <https://dev.mysql.com/>`_
* `MySQL Documentation <https://dev.mysql.com/doc/>`_
* `MySQL 5.7 Reference manual <https://dev.mysql.com/doc/refman/5.7/en/>`_
* `MariaDB an OpenSource alternative <https://mariadb.org/about/>`_


Useful Commands
===============

Common table manipulation commands
----------------------------------

Copy a table::

	mysql> CREATE TABLE mail2 like mail;
	mysql> INSERT INTO mail2 SELECT * FROM mail [WHERE ...];
	mysql> INSERT INTO dbase2.table1 SELECT * FROM dbase1.table1; # across DB's

Add, create or delete an index::

	mysql> CREATE INDEX sku_name ON node(sku_name);
	mysql> ALTER TABLE <table> ADD INDEX (<column>);
	mysql> ALTER TABLE <table> ADD UNIQUE INDEX (<column>);
	mysql> ALTER TABLE RequestDetails ADD INDEX (request_id);

Add, delete or modify a column::

	mysql> ALTER TABLE <table> ADD <col> INDEX <col> (<col>);
	mysql> ALTER TABLE DROP <col>;
	
	mysql> ALTER TABLE <table> ADD <col> VARCHAR(20) AFTER <some-col>;
	
	mysql> ALTER TABLE table1 MODIFY COLUMN name VARCHAR(95);

Creating a TSV, mysqld must be able to write, i.e use "/tmp"::

	# Produces: /tmp/<table>.txt (and empty /tmp/<table>.sql)
	mysqldump -u root --no-create-info --tab=/tmp <db> <table>

`Loading data from a TSV file <https://dev.mysql.com/doc/refman/5.7/en/load-data.html>`_::

	mysql> LOAD LOCAL DATA INFILE '/home/user/table1.txt' INTO TABLE table1;
	mysql> SHOW WARNINGS;
	
	# Ignore first line in TSV file, and update the 'id' auto-increment
	mysql> LOAD DATA LOCAL INFILE '/home/user/vendor.tsv' INTO TABLE vendors (english,oracle,legal,short);
	mysql> DESCRIBE vendors;
	+----------+--------------+------+-----+---------+----------------+
	| Field    | Type         | Null | Key | Default | Extra          |
	+----------+--------------+------+-----+---------+----------------+
	| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
	| english  | varchar(100) | NO   | MUL | NULL    |                |
	| oracle   | varchar(100) | NO   |     | NULL    |                |
	| legal    | varchar(100) | NO   |     | NULL    |                |
	| short    | varchar(80)  | NO   | MUL | NULL    |                |
	+----------+--------------+------+-----+---------+----------------+

Exporting a Table in CSV format::

	$ mysqldump -u root --no-create-info --tab=/tmp dbase2 table1
	$ mysqldump -u root --tab=/tmp dbase2 table1

Common User commands
--------------------

Show users::

	mysql> SELECT User,Host FROM mysql.user;

Show User Grants::

	mysql> select * from information_schema.user_privileges;

Show User Grants on Databases::

	mysql> SELECT user,host,db,select_priv,insert_priv,grant_priv FROM mysql.db WHERE db IN ('dbase1','dbase2') ORDER BY db;

Change User password::

	mysql> use mysql
	mysql> update mysql.user SET Password=PASSWORD('<new-password>') WHERE User='<user>' AND Host='<host-name>';

Show Userr grants::

	mysql> SHOW GRANTS FOR 'readonly.user'@'localhost';
	mysql> GRANT SELET ON <db>.* TO 'readonly.user'@'<remote-host>' IDENTIFIED BY '<passwd>'; # passwd from SHOW GRANTS
	mysql> REVOKE SELECT ON <db>.* FROM 'readonly.user'@'localhost';

Which Users have access to which database::

	mysql> SELECT user,host,db,select_priv,insert_priv,grant_priv FROM mysql.db WHERE db IN ('dbase1','dbase2') ORDER BY db;
	+--------------+-------------------------------+----------+-------------+-------------+------------+
	| user         | host                          | db       | select_priv | insert_priv | grant_priv |
	+--------------+-------------------------------+----------+-------------+-------------+------------+
	| rw_user      | server2.corp.dc1.xyzab.com    | dbase1   | Y           | Y           | N          |
	| rw_user      | desktop1.corp.xyzab.com       | dbase1   | Y           | Y           | N          |
	| ro_user      | server2.corp.dc1.xyzab.com    | dbase1   | Y           | N           | N          |
	| rw_user      | server2.corp.dc2.xyzab.com    | dbase2   | Y           | N           | N          |
	| ro_user      | server2.corp.ne1.xyzab.com    | dbase2   | Y           | N           | N          |
	| rw_user      | server2.corp.dc1.xyzab.com    | dbase2   | Y           | Y           | N          |
	| ro_user      | server2.corp.dc1.xyzab.com    | dbase2   | Y           | N           | N          |
	+--------------+-------------------------------+----------+-------------+-------------+------------+

Changing Password::

	$ mysql -u root
	mysql> set password for 'readonly.user'@'localhost' = password('LB4wK81Mp2BEFwxOQ7saVq2PEOgss3hUYVF2.cqKfkk-');

Display Table details
---------------------

Table structure::

	mysql> SHOW CREATE TABLE <table>\G
	mysql> DESCRIBE <table>;
	mysql> SHOW INDEXES FROM <table>

Deleting data from a table
--------------------------

Deleting rows which match::

	mysql> DELETE FROM <table> WHERE start_date >= '2014.02.02';

Deleting the entire contents of a table::

	mysql> TRUNCATE TABLE <table>;
	mysql> DELETE FROM <table>;


MySQL Select examples
---------------------

**Note** to cancel a query ``\c``

Calculated column in where clause::

	mysql> SELECT a,b,c,(a*b+c) AS d, n FROM table HAVING d > n ORDER by d; # NB ’n’ is in SELECT

Data in t1 and NOT in t2::

	mysql> SELECT t1.name,t1.qty,t1.id FROM table1 AS t1 LEFT JOIN table2 AS t2 ON t1.id=t2.id WHERE t2.id IS NULL;

Non-ASCII data `manual <https://dev.mysql.com/doc/refman/5.7/en/binary-varbinary.html>`_::

	mysql> SELECT name FROM table1 WHERE BINARY provider='X';

Using aggregates in filters::

	# WHERE is applied before GROUP BY
	# HAVING is applied after GROUP BY and hence can filter on aggregates
	mysql> SELECT intfid,COUNT(id) AS num FROM missed_polls GROUP BY intfid HAVING COUNT(id) > 10;
	mysql> SELECT intfid,COUNT(id) AS count FROM missed_polls GROUP BY intfid HAVING count > 10;

Inner Join example::

	mysql> SELECT MAX(t2.outmax) FROM table1 AS t1 INNER JOIN table2 AS t2 ON t1.id = t2.id WHERE t1.dc='dc1' AND RIGHT(t1.rtr,3)<>'dc1' AND t2.start_date>='2013.03.01' AND t2.end_date<='2014.06.28';

``SELECT DISTINCT`` like on first part of string, e.g. john-to-paul::

	mysql> SELECT LEFT(name,INSTR(name,'-to-')-1) AS gift FROM presents GROUP BY gift;
	mysql> SELECT LEFT(name,INSTR(name,'-to-')-1) AS gift FROM presents GROUP BY gift;

Confirming week numbers::

	mysql> SELECT start_date,WEEK(REPLACE(start_date, '.', '-')) AS Week from traffic WHERE start_date>='2015.02.15' AND end_date<='2015.03.21' GROUP BY start_date ORDER BY start_date;

Testing arithmetic functions
----------------------------
::

	mysql> SELECT MD5(RAND());
	mysql> SELECT UPPER(LEFT(CONVERT(MD5(RAND()),CHAR),3));
	mysql> SELECT CONCAT('Request ',UPPER(LEFT(CONVERT(MD5(RAND()),CHAR),3)));

Miscellaneous MySQL information
-------------------------------

Schema information::

	mysql> SELECT TABLE_NAME,ENGINE FROM information.schema.TABLES WHERE TABLE_SCHEMA='dbname';

MySQL status::

	mysql> STATUS; # \s

Flushing Replication::

	mysql> SHOW MASTER LOGS;
	mysql> FLUSH LOGS;
	mysql> RESET MASTER;

BLOB sizing

	============ ===========================
	Data Type    Size in CHARS
	============ ===========================
	TINYBLOB     255 (2^8 -1) CHARS
	BLOB         65535 (2^16 -1) CHARS
	MEDIUMBLOB   16777215 (2^24 -1) CHARS
	LONGBLOB     4294967295 (2^32 -1) CHARS
	============ ===========================


Handling Databases forced to read-only mode
===========================================

Full Read-Write access to the database::

	mysql> CREATE USER 'admin.user'@'localhost' IDENTIFIED BY 'JizrAjPpd_1o8pQEXm4UzJb_k_R7KS2UPV.1YJ59k34-';
	mysql> SHOW GRANTS FOR 'admin.user'@'localhost';
	+---------------------------------------------------------------------------------------------------------------------+
	| Grants for admin.user@localhost                                                                                   |
	+---------------------------------------------------------------------------------------------------------------------+
	| GRANT USAGE ON *.* TO 'admin.user'@'localhost' IDENTIFIED BY PASSWORD '*8FBE06BA12F769A27C408DE19A951866541D018E' |
	+---------------------------------------------------------------------------------------------------------------------+
	
	mysql> GRANT SUPER ON *.* TO 'admin.user'@'localhost' IDENTIFIED BY PASSWORD '*8FBE06BA12F769A27C408DE19A951866541D018E'
	mysql> GRANT ALL ON dbase2.* TO 'admin.user'@'localhost';
	mysql> CREATE USER 'readonly.user'@'localhost' IDENTIFIED BY 'bj1NJMvEjTGM_rgcSGCD.LDPOoyTy.5.vMfBaB3g4uk-';
	mysql> GRANT SELECT ON dbase2.* TO 'readonly.user'@'localhost';
	mysql> GRANT SELECT ON dbase2.* TO 'readonly.user'@'server2.corp.dc1.xyzab.com' IDENTIFIED BY PASSWORD '*1C4A2249CAD2B46EC5B71D84DC72F555276F06D5';
	mysql> FLUSH PRIVILEGES;
	
	mysql> SHOW GRANTS FOR 'admin.user'@'localhost';
	+---------------------------------------------------------------------------------------------------------------------+
	| Grants for admin.user@localhost                                                                                   |
	+---------------------------------------------------------------------------------------------------------------------+
	| GRANT SUPER ON *.* TO 'admin.user'@'localhost' IDENTIFIED BY PASSWORD '*8FBE06BA12F769A27C408DE19A951866541D018E' |
	| GRANT ALL PRIVILEGES ON `transpeer`.* TO 'admin.user'@'localhost'                                                 |
	| GRANT ALL PRIVILEGES ON `fullmonty`.* TO 'admin.user'@'localhost'                                                 |
	+---------------------------------------------------------------------------------------------------------------------+

Read-Only access to the database::

	mysql> SHOW GRANTS FOR 'readonly.user'@'localhost';
	+----------------------------------------------------------------------------------------------------------------------+
	| Grants for readonly.user@localhost                                                                                   |
	+----------------------------------------------------------------------------------------------------------------------+
	| GRANT USAGE ON *.* TO 'readonly.user'@'localhost' IDENTIFIED BY PASSWORD '*1C4A2249CAD2B46EC5B71D84DC72F555276F06D5' |
	| GRANT SELECT ON `transpeer`.* TO 'readonly.user'@'localhost'                                                         |
	| GRANT SELECT ON `fullmonty`.* TO 'readonly.user'@'localhost'                                                         |
	+----------------------------------------------------------------------------------------------------------------------+

