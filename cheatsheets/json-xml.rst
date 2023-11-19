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

Examples
========

Simple Example
--------------

.. code-block:: console

    $ echo '{"fruit":{"name":"apple","color":"green","price":1.20}}' > fruit.json
    $ jq '.' fruit.json                         # pretty-print; see 'Basic Usage'
    $ jq '.fruit.color' fruit.json              # extract color; "green"
    $ jq '.fruit.color,.fruit.price' fruit.json # extract colors and price; "green", 1.20
    $ jq '.fruit | .color,.price' fruit.json    # extract colors and price, alternative syntax
    $ jq '.fruit | keys' fruit.json             # extract keys; "color", "name", "price"

Array Example
-------------

.. code-block:: console

    $ echo '{"fruit":[{"name":"apple","color":"green","price":1.20},{"name":"banana","color":"yellow","price":0.60}]}' > fruits.json
    $ jq '.' fruits.json
    {
      "fruit": [
        {
          "name": "apple",
          "color": "green",
          "price": 1.20
        },
        {
          "name": "banana",
          "color": "yellow",
          "price": 0.60
        }
      ]
    }
    $ jq '.fruit[].name' fruits.json                 # extract names; "apple", "banana"
    $ jq '.fruit[].color,.fruit[].price' fruits.json # extract color/price; "green", "yellow", 1.20, 0.60
    $ jq '.fruit[] | .color,.price' fruits.json      # extract color/price; "green", 1.20, "yellow", 0.60
    $ jq '.fruit[1] | .color,.price' fruits.json     # extract color/price; "yellow", 0.60
    $ jq '.fruit | keys' fruits.json                 # extract keys; [0,1]
    $ jq '.fruit[] | keys' fruits.json               # extract keys; ["color", "name","price"]["color","name","price"]

*********************************************
XML - ``xq`` beautifier and content extractor
*********************************************

* `xq <https://github.com/sibprogrammer/xq>`_ XML and HTML beautifier and content extractor

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


Examples
========

Simple Example
--------------

.. code-block:: console

    $ cat > fruit.xml <<EOF
    > <?xml version="1.0" encoding="UTF-8"?><fruit><name>apple</name><color>green</color><price>1.20</price></fruit>
    > EOF

    $ xq fruit.xml
    <?xml version="1.0" encoding="UTF-8"?>
    <fruit>
      <name>apple</name>
      <color>green</color>
      <price>1.20</price>
    </fruit>

    $ xq -q color fruit.xml                     # extract color; "green"
    $ xq -q color,price fruit.xml               # extract colors and price; "green", 1.20

Array Example
-------------

.. code-block:: console

    $ cat > fruits.xml <<EOF
    <fruits>
    <fruit><name>apple</name><color>green</color><price>1.20</price></fruit>
    <fruit><name>banana</name><color>yellow</color><price>0.60</price></fruit>
    </fruits>
    > EOF

    $ xq fruits.xml
    <?xml version="1.0" encoding="UTF-8"?>
    <fruits>
      <fruit>
        <name>apple</name>
        <color>green</color>
        <price>1.20</price>
      </fruit>
      <fruit>
        <name>banana</name>
        <color>yellow</color>
        <price>0.60</price>
      </fruit>
    </fruits>

    $ xq -q name fruits.xml        # extract name; apple, banana
    $ xq -q color fruits.xml       # extract color; green, yellow
    $ xq -q color,price fruits.xml # extract color/price; green, 1.20, yellow, 0.60

