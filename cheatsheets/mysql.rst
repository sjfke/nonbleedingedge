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
	mysql> INSERT INTO topn.site_list SELECT * FROM capplan.site_list; # across DB's

Add, create or delete an index::

	mysql> CREATE INDEX sku_name ON node(sku_name);
	mysql> ALTER TABLE <table> ADD INDEX (<column>);
	mysql> ALTER TABLE <table> ADD UNIQUE INDEX (<column>);
	mysql> ALTER TABLE RequestDetails ADD INDEX (request_id);

Add, delete or modify a column::

	mysql> ALTER TABLE <table> ADD <col> INDEX <col> (<col>);
	mysql> ALTER TABLE DROP <col>;
	
	mysql> ALTER TABLE <table> ADD <col> VARCHAR(20) AFTER <some-col>;
	
	mysql> ALTER TABLE interfaces MODIFY COLUMN mrtg VARCHAR(95);

Creating a TSV, mysqld must be able to write, i.e use "/tmp"::

	# Produces: /tmp/<table>.txt (and empty /tmp/<table>.sql)
	mysqldump -u root --no-create-info --tab=/tmp <db> <table>

`Loading data from a TSV file <https://dev.mysql.com/doc/refman/5.7/en/load-data.html>`_::

	mysql> LOAD LOCAL DATA INFILE '/home/gcollis/newpat/site_list.txt' INTO TABLE site_list;
	mysql> SHOW WARNINGS;
	
	# Ignore first line in TSV file, and update the 'id' auto-increment
	mysql> LOAD DATA LOCAL INFILE '/home/gcollis/plutus/vendor.tsv' INTO TABLE vendors (english,oracle,english2,short);
	mysql> DESCRIBE vendors;
	+----------+--------------+------+-----+---------+----------------+
	| Field    | Type         | Null | Key | Default | Extra          |
	+----------+--------------+------+-----+---------+----------------+
	| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
	| english  | varchar(100) | NO   | MUL | NULL    |                |
	| oracle   | varchar(100) | NO   |     | NULL    |                |
	| english2 | varchar(100) | NO   |     | NULL    |                |
	| short    | varchar(80)  | NO   | MUL | NULL    |                |
	+----------+--------------+------+-----+---------+----------------+

Exporting a Table in CSV format::

	$ mysqldump -u root --no-create-info --tab=/tmp topn site_list
	$ mysqldump -u root --tab=/tmp topn site_list

Common User commands
--------------------

Show users::

	mysql> SELECT User,Host FROM mysql.user;

Show User Grants::

	mysql> select * from information_schema.user_privileges;

Show User Grants on Databases::

	mysql> SELECT user,host,db,select_priv,insert_priv,grant_priv FROM mysql.db WHERE db IN ('pdbclone','ypeering') ORDER BY db;

Change User password::

	mysql> use mysql
	mysql> update mysql.user SET Password=PASSWORD('<new-password>') WHERE User='<user>' AND Host='<host-name>';

Show Userr grants::

	mysql> SHOW GRANTS FOR 'prod.dcn.user'@'localhost';
	mysql> GRANT SELET ON <db>.* TO 'prod.dcn.user'@'<remote-host>' IDENTIFIED BY '<passwd>'; # passwd from SHOW GRANTS
	mysql> REVOKE SELECT ON <db>.* FROM 'prod.dcn.user'@'localhost';

Which Users have access to which database::

	mysql> SELECT user,host,db,select_priv,insert_priv,grant_priv FROM mysql.db WHERE db IN ('pdbclone','ypeering') ORDER BY db;
	+--------------+-------------------------------+----------+-------------+-------------+------------+
	| user         | host                          | db       | select_priv | insert_priv | grant_priv |
	+--------------+-------------------------------+----------+-------------+-------------+------------+
	| peeringdb    | netops2.corp.gq1.yahoo.com    | pdbclone | Y           | Y           | N          |
	| peeringdb    | growschose.corp.gq1.yahoo.com | pdbclone | Y           | Y           | N          |
	| peeringdb_ro | netops2.corp.gq1.yahoo.com    | pdbclone | Y           | N           | N          |
	| peeringdb    | netops2.corp.ne1.yahoo.com    | ypeering | Y           | N           | N          |
	| peeringdb_ro | netops2.corp.ne1.yahoo.com    | ypeering | Y           | N           | N          |
	| peeringdb    | netops2.corp.gq1.yahoo.com    | ypeering | Y           | Y           | N          |
	| peeringdb_ro | netops2.corp.gq1.yahoo.com    | ypeering | Y           | N           | N          |
	+--------------+-------------------------------+----------+-------------+-------------+------------+

Changing Password::

	$ mysql -u root
	mysql> set password for 'prod.dcn.user'@'localhost' = password('LB4wK81Mp2BEFwxOQ7saVq2PEOgss3hUYVF2.cqKfkk-');

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

Deleting the entire conetnts of a table::

	mysql> TRUNCATE TABLE <table>;
	mysql> DELETE FROM <table>;


MySQL Select examples
---------------------

**Note** to cancel a query ``\c``

Calculated column in where clause::

	mysql> SELECT a,b,c,(a*b+c) AS d, n FROM table HAVING d > n ORDER by d; # NB ’n’ is in SELECT

Data in t1 and NOT in t2::

	mysql> SELECT t1.name,t1.ltype,t1.id FROM interfaces AS t1 LEFT JOIN traffic AS t2 ON t1.id=t2.id WHERE t2.id IS NULL;

Non-ASCII data `manual <https://dev.mysql.com/doc/refman/5.7/en/binary-varbinary.html>`_::

	mysql> SELECT name FROM interfaces WHERE BINARY provider='X';

Using aggregates in filters::

	- WHERE is applied before GROUP BY
	- HAVING is applied after and so can filter on aggregates
	mysql> SELECT intfid,COUNT(id) AS num FROM missed_polls GROUP BY intfid HAVING COUNT(id) > 10;
	mysql> SELECT intfid,COUNT(id) AS count FROM missed_polls GROUP BY intfid HAVING count > 10;

Inner Join example::

	mysql> SELECT MAX(t2.outmax) FROM lsp_interfaces AS t1 INNER JOIN lsp_traffic AS t2 ON t1.id = t2.lspid WHERE t1.dc='ams' AND RIGHT(t1.dst_rtr,3)<>'ams' AND t2.start_date>='2013.03.01' AND t2.end_date<='2014.06.28';

``SELECT DISTINCT`` like on first part of string, e.g. Wash_DC-to-Amsterdam::

	mysql> SELECT LEFT(name,INSTR(name,'-to-')-1) AS metro FROM lsp_metros GROUP BY metro;

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

	mysql> CREATE USER 'prod.dcn.adm'@'localhost' IDENTIFIED BY 'JizrAjPpd_1o8pQEXm4UzJb_k_R7KS2UPV.1YJ59k34-';
	mysql> SHOW GRANTS FOR 'prod.dcn.adm'@'localhost';
	+---------------------------------------------------------------------------------------------------------------------+
	| Grants for prod.dcn.adm@localhost                                                                                   |
	+---------------------------------------------------------------------------------------------------------------------+
	| GRANT USAGE ON *.* TO 'prod.dcn.adm'@'localhost' IDENTIFIED BY PASSWORD '*8FBE06BA12F769A27C408DE19A951866541D018E' |
	+---------------------------------------------------------------------------------------------------------------------+
	
	mysql> GRANT SUPER ON *.* TO 'prod.dcn.adm'@'localhost' IDENTIFIED BY PASSWORD '*8FBE06BA12F769A27C408DE19A951866541D018E'
	mysql> GRANT ALL ON topn2.* TO 'prod.dcn.adm'@'localhost';
	mysql> CREATE USER 'prod.dcn.user'@'localhost' IDENTIFIED BY 'bj1NJMvEjTGM_rgcSGCD.LDPOoyTy.5.vMfBaB3g4uk-';
	mysql> GRANT SELECT ON topn2.* TO 'prod.dcn.user'@'localhost';
	mysql> GRANT SELECT ON topn2.* TO 'prod.dcn.user'@'netops2.corp.gq1.yahoo.com' IDENTIFIED BY PASSWORD '*1C4A2249CAD2B46EC5B71D84DC72F555276F06D5';
	mysql> FLUSH PRIVILEGES;
	
	mysql> SHOW GRANTS FOR 'prod.dcn.adm'@'localhost';
	+---------------------------------------------------------------------------------------------------------------------+
	| Grants for prod.dcn.adm@localhost                                                                                   |
	+---------------------------------------------------------------------------------------------------------------------+
	| GRANT SUPER ON *.* TO 'prod.dcn.adm'@'localhost' IDENTIFIED BY PASSWORD '*8FBE06BA12F769A27C408DE19A951866541D018E' |
	| GRANT ALL PRIVILEGES ON `transpeer`.* TO 'prod.dcn.adm'@'localhost'                                                 |
	| GRANT ALL PRIVILEGES ON `fullmonty`.* TO 'prod.dcn.adm'@'localhost'                                                 |
	+---------------------------------------------------------------------------------------------------------------------+

Read-Only access to the database::

	mysql> SHOW GRANTS FOR 'prod.dcn.user'@'localhost';
	+----------------------------------------------------------------------------------------------------------------------+
	| Grants for prod.dcn.user@localhost                                                                                   |
	+----------------------------------------------------------------------------------------------------------------------+
	| GRANT USAGE ON *.* TO 'prod.dcn.user'@'localhost' IDENTIFIED BY PASSWORD '*1C4A2249CAD2B46EC5B71D84DC72F555276F06D5' |
	| GRANT SELECT ON `transpeer`.* TO 'prod.dcn.user'@'localhost'                                                         |
	| GRANT SELECT ON `fullmonty`.* TO 'prod.dcn.user'@'localhost'                                                         |
	+----------------------------------------------------------------------------------------------------------------------+
