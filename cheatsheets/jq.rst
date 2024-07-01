:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/jq.rst

######################
``jq`` JSON Cheatsheet
######################

************************
``jq`` sed for JSON data
************************

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
        "family": "Flintstones",
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
      "family": "Flintstones",
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
* `jq, xq and yq - Handy tools for the command line <https://blog.lazy-evaluation.net/posts/linux/jq-xq-yq.html>`_
