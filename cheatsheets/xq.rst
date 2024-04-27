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
    > <!doctype html><html>
    <head><title>Example Page Title</title>
    <meta name="description" content="Simple HTML example">
    <meta name="keywords" content="html basic example"></head>
    <body>Example page content</body></html>
    > EOF

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
    $ xq -q Name,Age flintstones.xml
    Fred
    35
    Wilma
    25
    Pebbles
    1
    Dino
    5

XPath Extraction
----------------

* `w3schools: XML and XPath <https://www.w3schools.com/xml/xml_xpath.asp>`_

.. code-block:: console

    # Note: quotation maybe needed to avoid SHELL interpretation of certain symbols

    $ xq -x //@Lastname flintstones.xml
    Flintstones

    $ xq -x //Name flintstones.xml
    Fred
    Wilma
    Pebbles
    Dino

    $ xq -x "//Name | //Age" flintstones.xml
    Fred
    Wilma
    Pebbles
    Dino
    35
    25
    1
    5

    $ xq -x "/family/member[2]/Name" flintstones.xml
    Wilma

    $ xq -x "/family/member[Age>10]/Name" flintstones.xml
    Fred
    Wilma

    $ xq -x "/family/member[Age>10]/Name | /family/member[Age>10]/Age" flintstones.xml
    Fred
    Wilma
    35
    25
