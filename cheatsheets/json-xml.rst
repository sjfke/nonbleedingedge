:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/json-xml.rst

#######################
JSON and XML Cheatsheet
#######################

*******************************
JSON - ``jq`` sed for JSON data
*******************************

* `jq <https://jqlang.github.io/jq/>`_ is like ``sed`` for JSON data

Installation
============

.. code-block:: console

    $ sudo dnf install jq      # Fedora
    $ brew install jq          # MacOS
    $ winget install jqlang.jq # Windows

Basic Usage
-----------

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
