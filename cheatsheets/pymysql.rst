:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/pymysql.rst

******************
PyMySQL CheatSheet
******************

Example
=======

Create a simple table

.. code-block:: none

    CREATE TABLE `users` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `email` varchar(255) COLLATE utf8_bin NOT NULL,
        `password` varchar(255) COLLATE utf8_bin NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    AUTO_INCREMENT=1

Now try inserting and selecting

.. code-block:: python

    import pymysql.cursors

    # Connect to the database
    connection = pymysql.connect(host='localhost',
        user='user',
        password='passwd',
        db='db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection is not autocommit by default. So you must commit to save your changes.
            connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

Which will print

.. code-block:: python

    {'password': 'very-secret', 'id': 1}

Simple Example (row[0] etc)
===========================

.. code-block:: python

    import pymysql.cursors

    dbhost = 'localhost'
    dbase  = 'db1'
    dbuser = 'user1'
    dbpass = 'stupidPasswd'

    connection = pymysql.connect(host=dbhost, user=dbuser, password=dbpass, db=dbase, charset='utf8')
    name = 'barney'
    sql = "SELECT id FROM " + table + " WHERE name=%s"

    cursor = connection.cursor()
    cursor.execute(sql, name.strip() )
    for row in cursor:
        print(row['id'])

    cursor.close()
    connection.close()


Simple Example (row[‘id’] etc)
==============================

.. code-block:: python

    import pymysql.cursors

    dbhost = 'localhost'
    dbase  = 'db1'
    dbuser = 'user1'
    dbpass = get_password(dbuser) # assume method exists to get the password secret
    connection = pymysql.connectionect(host=dbhost, user=dbuser, password=dbpass, db=dbase, charset='utf8', cursorsorclass=pymysql.cursorsors.Dictcursorsor)
    name = 'barney'
    sql = "SELECT id FROM " + table + " WHERE name=%s"

    cursor = connection.cursorsor()
    cursor.execute(sql, name.strip() )
    for row in cursor:
        print(row['id'])
    cursor.close()
    connection.close()


    # try select statement
    cursor.execute("SHOW TABLES")
    print(cursor.description)

    # try insert statement
    sql = "INSERT INTO `test` (`email`, `password`) VALUES (%s, %s)"
    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    connection.commit()

    cursor.close()
    connection.close()

PlaceHolders
============

* use ‘%s’ (not ‘?’ like Perl DBI and other API’s)

Hint: following is an example of getting it wrong ‘?’ (instead of ‘%s’).

.. code-block:: console

    # Traceback (most recent call last):
    #   File "./pymysql-test.py", line 81, in <module>
    #     import_billing_info()
    #   File "./pymysql-test.py", line 36, in import_billing_info
    #     cur.execute(sql, ('9', '2500.0', '2016', '0', '1.0', '2500.0') )
    #   File "/home/y/lib/python2.7/site-packages/pymysql/cursors.py", line 156, in execute
    #     query = self.mogrify(query, args)
    #   File "/home/y/lib/python2.7/site-packages/pymysql/cursors.py", line 135, in mogrify
    #     query = query % self._escape_args(args, conn)
    # TypeError: not all arguments converted during string formatting


