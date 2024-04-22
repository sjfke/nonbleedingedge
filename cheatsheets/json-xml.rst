:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/json-xml.rst

#######################
JSON and XML Cheatsheet
#######################

*******************************
JSON - ``jq`` sed for JSON data
*******************************

* `jq <https://jqlang.github.io/jq/>`_ is like ``sed`` for JSON data
* `jq Manual (development version) <https://jqlang.github.io/jq/manual/>`_
* `JSON - Introduction <https://www.w3schools.com/js/js_json_intro.asp>`_
* `JSON Schema <https://json-schema.org/>`_ enables the confident and reliable use of the JSON data format.
* `JSON Online <https://jsononline.net/>`_

Installation
============

.. code-block:: console

    $ sudo dnf install jq      # Fedora
    $ brew install jq          # MacOS
    $ winget install jqlang.jq # Windows

Basic Usage
===========

.. code-block:: console

    $ echo '{"fruit":{"name":"apple","color":"green","price":1.20}}' | jq '.'
    {
      "fruit": {
        "name": "apple",
        "color": "green",
        "price": 1.20
      }
    }

    $ curl --no-progress-meter http://api.open-notify.org/iss-now.json | jq '.'
    {
      "iss_position": {
        "longitude": "158.4700",
        "latitude": "-2.8688"
      },
      "message": "success",
      "timestamp": 1700410500
    }

JSON Example
============

.. code-block:: console

    $ cat flintstones.json
    {
        "family": "flintstones",
        "members": [
            { "Name": "Fred", "Age": 35, "Gender": "male" },
            { "Name": "Wilma", "Age": 25, "Gender": "female" },
            { "Name": "Pebbles", "Age": 1, "Gender": "female" },
            { "Name": "Dino", "Age": 5, "Gender": "male" }
        ]
    }

Pretty print (in color)
-----------------------

.. code-block:: console

    $ jq '.' flintstones.json
    {
      "family": "flintstones",
      "members": [
        {
          "Name": "Fred",
          "Age": 35,
          "Gender": "male"
        },
        {
          "Name": "Wilma",
          "Age": 25,
          "Gender": "female"
        },
        {
          "Name": "Pebbles",
          "Age": 1,
          "Gender": "female"
        },
        {
          "Name": "Dino",
          "Age": 5,
          "Gender": "male"
        }
      ]
    }
    $ jq '.members' flintstones.json
    [
      {
        "Name": "Fred",
        "Age": 35,
        "Gender": "male"
      },
      {
        "Name": "Wilma",
        "Age": 25,
        "Gender": "female"
      },
      {
        "Name": "Pebbles",
        "Age": 1,
        "Gender": "female"
      },
      {
        "Name": "Dino",
        "Age": 5,
        "Gender": "male"
      }
    ]

Filtering
---------

.. code-block:: console

    $ jq '.members[].Name' flintstones.json
    "Fred"
    "Wilma"
    "Pebbles"
    "Dino"
    $ jq '.members[] | .Name' flintstones.json
    "Fred"
    "Wilma"
    "Pebbles"
    "Dino"

    $ jq '.members[].Name,.members[].Age' flintstones.json
    "Fred"
    "Wilma"
    "Pebbles"
    "Dino"
    35
    25
    1
    5
    $ jq '.members[] | .Name,.Age' flintstones.json
    "Fred"
    35
    "Wilma"
    25
    "Pebbles"
    1
    "Dino"
    5

    $ jq '.members[1].Name,.members[1].Age' flintstones.json
    "Wilma"
    25

Keys and lengths
----------------

.. code-block:: console

    $ jq '. | keys' flintstones.json
    [
      "family",
      "members"
    ]
    $ jq '.members[0] | keys' flintstones.json
    [
      "Age",
      "Gender",
      "Name"
    ]
    $ jq '. | length' flintstones.json                        # 2
    $ jq '.members | length' flintstones.json                 # 4
    $ jq '.members[] | length' flintstones.json               # 3 3 3 3
    $ jq '.members[].Name | length' flintstones.json          # 4 5 7 4


* `Guide to Linux jq Command for JSON Processing <https://www.baeldung.com/linux/jq-command-json>`_
* `Querying JSON and XML with jq and xq <https://www.ashbyhq.com/blog/engineering/jq-and-yq>`_
* `yq: Command-line YAML/XML/TOML processor - jq wrapper for YAML, XML, TOML documents <https://github.com/kislyuk/yq>`_
* `jq, xq and yq - Handy tools for the command line <https://blog.lazy-evaluation.net/posts/linux/jq-xq-yq.html>`_
* `TOML [Tom's Obvious Minimal Language] (.INI like) <https://toml.io/en/>`_

*********************************************
XML - ``xq`` beautifier and content extractor
*********************************************

* `xq <https://github.com/sibprogrammer/xq>`_ XML and HTML beautifier and content extractor
* `GitHub: sibprogrammer/xq <https://github.com/sibprogrammer/xq>`_

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
    <family Lastname="flintstones">
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
    <family Lastname="flintstones">
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
    flintstones

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
