:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/xq.rst

#################
``xq`` Cheatsheet
#################

***************************************
``xq`` beautifier and content extractor
***************************************

* `xq <https://github.com/sibprogrammer/xq>`_ XML and HTML beautifier and content extractor
* `GitHub: sibprogrammer/xq <https://github.com/sibprogrammer/xq>`_
* `jq, xq and yq - Handy tools for the command line <https://blog.lazy-evaluation.net/posts/linux/jq-xq-yq.html>`_
* `Introduction to XML <https://www.w3schools.com/xml/xml_whatis.asp>`_
* `XML DTD <https://www.w3schools.com/xml/xml_dtd.asp>`_
* `XML Schema <https://www.w3schools.com/xml/xml_schema.asp>`_
* `XML Validator <https://jsonformatter.org/xml-validator>`_

Installation
============

.. code-block:: console

    $ sudo dnf install xq                               # Fedora
    $ brew install xq                                   # MacOS
    $ curl -sSL https://bit.ly/install-xq | sudo bash   # Linux, installs into /usr/local/bin

Windows executable not available, so run the Linux version under WSL or in a Docker container.
It is written in 'golang' so also runnable using ``go``, see `Go Installation <https://go.dev/doc/install>`_

Basic Usage
===========

.. code-block:: console

    $ echo '<?xml version="1.0" encoding="UTF-8"?><fruit><name>apple</name><color>green</color><price>1.20</price></fruit>' | xq
    <?xml version="1.0" encoding="UTF-8"?>
    <fruit>
      <name>apple</name>
      <color>green</color>
      <price>1.20</price>
    </fruit>

    $ curl -s https://www.w3schools.com/xml/note.xml | xq
    <?xml version="1.0" encoding="UTF-8"?>
    <note>
      <to>Tove</to>
      <from>Jani</from>
      <heading>Reminder</heading>
      <body>Don't forget me this weekend!</body>
    </note>

    $ cat > test.html <<EOF
    <!doctype html><html>
    <head><title>Example Page Title</title>
    <meta name="description" content="Simple HTML example">
    <meta name="keywords" content="html basic example"></head>
    <body>Example page content</body></html>
    EOF

    $ xq test.html
    <!doctype html>
    <html>
      <head>
        <title>Example Page Title</title>
        <meta name="description" content="Simple HTML example"/>
        <meta name="keywords" content="html basic example"/>
      </head>
      <body>
    Example page content
    </body>
    </html>


XML Example
===========

.. code-block:: console

    $ cat flintstones.xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <family Lastname="Flintstones">
      <member><Name>Fred</Name><Age>35</Age><Gender>male</Gender></member>
      <member><Name>Wilma</Name><Age>25</Age><Gender>female</Gender></member>
      <member><Name>Pebbles</Name><Age>1</Age><Gender>female</Gender></member>
      <member><Name>Dino</Name><Age>5</Age><Gender>male</Gender></member>
    </family>

Pretty print (in color)
-----------------------

.. code-block:: console

    $ xq flintstones.xml
    <?xml version="1.0" encoding="UTF-8"?>
    <family Lastname="Flintstones">
      <member>
        <Name>Fred</Name>
        <Age>35</Age>
        <Gender>male</Gender>
      </member>
      <member>
        <Name>Wilma</Name>
        <Age>25</Age>
        <Gender>female</Gender>
      </member>
      <member>
        <Name>Pebbles</Name>
        <Age>1</Age>
        <Gender>female</Gender>
      </member>
      <member>
        <Name>Dino</Name>
        <Age>5</Age>
        <Gender>male</Gender>
      </member>
    </family>

Querying
--------

.. code-block:: console

    $ xq -q Name flintstones.xml
    Fred
    Wilma
    Pebbles
    Dino

    $ xq -n -q Name flintstones.xml
    <name>Fred</name>
    <name>Wilma</name>
    <name>Pebbles</name>
    <name>Dino</name>

    $ xq -q Name,Age flintstones.xml
    Fred
    35
    Wilma
    25
    Pebbles
    1
    Dino
    5

    $ xq -nq Name,Age flintstones.xml
    <name>Fred</name>
    <age>35</age>
    <name>Wilma</name>
    <age>25</age>
    <name>Pebbles</name>
    <age>1</age>
    <name>Dino</name>
    <age>5</age>

XPath Extraction
----------------

* `w3schools: XML and XPath <https://www.w3schools.com/xml/xml_xpath.asp>`_

.. code-block:: console

    # Note: quotation maybe needed to avoid SHELL interpretation of certain symbols

    $ xq -x //@Lastname flintstones.xml
    Flintstones
    $ xq -nx //@Lastname flintstones.xml
    <Lastname>flintstones</Lastname>

    $ xq -x //Name flintstones.xml
    Fred
    Wilma
    Pebbles
    Dino

    $ xq -n -x //Name flintstones.xml
    <Name>Fred</Name>
    <Name>Wilma</Name>
    <Name>Pebbles</Name>
    <Name>Dino</Name>

    $ xq -x "//Name | //Age" flintstones.xml
    Fred
    Wilma
    Pebbles
    Dino
    35
    25
    1
    5

    $ xq -nx "//Name | //Age" flintstones.xml
    <Name>Fred</Name>
    <Name>Wilma</Name>
    <Name>Pebbles</Name>
    <Name>Dino</Name>
    <Age>35</Age>
    <Age>25</Age>
    <Age>1</Age>
    <Age>5</Age>

    $ xq -x "/family/member[2]/Name" flintstones.xml
    Wilma

    $ xq -nx "/family/member[2]/Name" flintstones.xml
    <Name>Wilma</Name>

    $ xq -x "/family/member[Age>10]/Name" flintstones.xml
    Fred
    Wilma

    $ xq -nx "/family/member[Age>10]/Name" flintstones.xml
    <Name>Fred</Name>
    <Name>Wilma</Name>

    $ xq -x "/family/member[Age>10]/Name | /family/member[Age>10]/Age" flintstones.xml
    Fred
    Wilma
    35
    25

    $ xq -nx "/family/member[Age>10]/Name | /family/member[Age>10]/Age" flintstones.xml
    <Name>Fred</Name>
    <Name>Wilma</Name>
    <Age>35</Age>
    <Age>25</Age>

HTML Example
============

.. code-block:: console

    $ cat flintstones.html
    <!doctype html><html>
    <head><title>Title Flintstones</title>
      <meta name="description" content="Flintstones family">
      <meta name="keywords" content="HTML, CSS, JavaScript">
      <meta name="author" content="Sjfke">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head><body>
      <h1 style="color:blue;">Heading Flintstones</h1>
      <p style="color:red;">members</p>
      <table>
        <tr><th>Name</th><th>Age</th><th>Gender</th></tr>
        <tr><td>Fred</td><td>35</td><td>male</td></tr>
        <tr><td>Wilma</td><td>25</td><td>female</td></tr>
        <tr><td>Pebbles</td><td>1</td><td>female</td></tr>
        <tr><td>Dino</td><td>5</td><td>male</td></tr>
      </table>
      <hr>
    <script>let d = Date(Date.now()); a = d.toString() document.write(a); </script>
    </body></html>

Pretty print (in color)
-----------------------

.. code-block:: console

    $ xq -m flintstones.html      # '-m' is optional
    <!doctype html>
    <html>
      <head>
        <title>Title Flintstones</title>
        <meta name="description" content="Flintstones family"/>
        <meta name="keywords" content="HTML, CSS, JavaScript"/>
        <meta name="author" content="Sjfke"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      </head>
      <body>
        <h1 style="color:blue;">Heading Flintstones</h1>
        <p style="color:red;">members</p>
        <table>
          <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Gender</th>
          </tr>
          <tr>
            <td>Fred</td>
            <td>35</td>
            <td>male</td>
          </tr>
          <tr>
            <td>Wilma</td>
            <td>25</td>
            <td>female</td>
          </tr>
          <tr>
            <td>Pebbles</td>
            <td>1</td>
            <td>female</td>
          </tr>
          <tr>
            <td>Dino</td>
            <td>5</td>
            <td>male</td>
          </tr>
        </table>
        <hr/>
        <script>let d = Date(Date.now()); a = d.toString() document.write(a);</script>
      </body>
    </html>

Querying
--------

.. code-block:: console

    $ xq -q head flintstones.html
    Title Flintstones

    $ xq -q meta flintstones.html  # returns 4 blank lines

    $ xq -nq meta flintstones.html
    <meta name="description" content="Flintstones family"/></meta>
    <meta name="keywords" content="HTML, CSS, JavaScript"/></meta>
    <meta name="author" content="Sjfke"/></meta>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/></meta>

    $ xq -q meta -a name flintstones.html
    description
    keywords
    author
    viewport

    $ xq -nq meta -a name flintstones.html # '-a' supersedes '-n'
    description
    keywords
    author
    viewport

    $ xq -q meta -a content flintstones.html
    Flintstones family
    HTML, CSS, JavaScript
    Sjfke
    width=device-width, initial-scale=1.0

    $ xq -q "body > h1" flintstones.html
    Heading Flintstones

    $ xq -nq "body > h1" flintstones.html
    <h1 style="color:blue;">Heading Flintstones</h1>

    $ xq -q "body > h1" -a style flintstones.html
    color:blue;

    $ xq -q "body > p" flintstones.html
    members

    $ xq -nq "body > p" flintstones.html
    <p style="color:red;">members</p>

    $ xq -q "body > p" -a style flintstones.html
    color:red;

    $ xq -q "script" flintstones.html
    let d = Date(Date.now()); a = d.toString() document.write(a);

    $ xq -nq "script" flintstones.html
    <script>let d = Date(Date.now()); a = d.toString() document.write(a);</script>

    $ xq -q "body > table" flintstones.html
    NameAgeGender
        Fred35male
        Wilma25female
        Pebbles1female
        Dino5male

    $ xq -nq "body > table" flintstones.html
    <table>
      <tbody>
        <tr>
          <th>Name</th>
          <th>Age</th>
          <th>Gender</th>
        </tr>
        <tr>
          <td>Fred</td>
          <td>35</td>
          <td>male</td>
        </tr>
        <tr>
          <td>Wilma</td>
          <td>25</td>
          <td>female</td>
        </tr>
        <tr>
          <td>Pebbles</td>
          <td>1</td>
          <td>female</td>
        </tr>
        <tr>
          <td>Dino</td>
          <td>5</td>
          <td>male</td>
        </tr>
      </tbody>
    </table>

    $ xq -q tr flintstones.html
    NameAgeGender
    Fred35male
    Wilma25female
    Pebbles1female
    Dino5male

    $ xq -nq tr flintstones.html
    <tr>
      <th>Name</th>
      <th>Age</th>
      <th>Gender</th>
    </tr>
    <tr>
      <td>Fred</td>
      <td>35</td>
      <td>male</td>
    </tr>
    <tr>
      <td>Wilma</td>
      <td>25</td>
      <td>female</td>
    </tr>
    <tr>
      <td>Pebbles</td>
      <td>1</td>
      <td>female</td>
    </tr>
    <tr>
      <td>Dino</td>
      <td>5</td>
      <td>male</td>
    </tr>