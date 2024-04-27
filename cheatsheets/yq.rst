:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/yq.rst

#################
``yq`` Cheatsheet
#################

**********************************
``yq`` command-line YAML processor
**********************************

* `YAML - YAML Ain't Markup Language <https://yaml.org/>`_
* `YAML - Specification version 1.2 <https://yaml.org/spec/1.2.2/>`_
* `GitBook - yq <https://mikefarah.gitbook.io/yq>`_
* `GitHub - mikefarah/yq <https://github.com/mikefarah/yq>`_
* `JSON - Introduction <https://www.w3schools.com/js/js_json_intro.asp>`_
* `JSON Schema <https://json-schema.org/>`_ enables the confident and reliable use of the JSON data format.
* `JSON Online <https://jsononline.net/>`_

Installation
============

* `yq Install <https://github.com/mikefarah/yq?tab=readme-ov-file#install>`_
* `Download the latest binary <https://github.com/mikefarah/yq/releases/tag/v4.43.1>`_

.. code-block:: console

    # Fedora
    $ VERSION=v4.43.1
    $ BINARY=yq_linux_amd64
    $ wget https://github.com/mikefarah/yq/releases/download/${VERSION}/${BINARY} -O /usr/bin/yq && chmod +x /usr/bin/yq

    $ brew install yq                  # MacOS
    $ winget install --id MikeFarah.yq # Windows


YAML Example
============

.. code-block:: console

    $ cat flintstones.yaml
    ---
    family: Flintstones
    members:
      - Name: Fred
        Age: 35
        Gender: male
      - Name: Wilma
        Age: 25
        Gender: female
      - Name: Pebbles
        Age: 1
        Gender: female
      - Name: Dino
        Age: 5
        Gender: male

Pretty print (in color)
-----------------------

Also color pretty-prints 'flintstones.json' and pretty-prints flintstones.xml

.. code-block:: console

    $ yq flintstones.yaml
    ---
    family: flintstones
    members:
      - Name: Fred
        Age: 35
        Gender: male
      - Name: Wilma
        Age: 25
        Gender: female
      - Name: Pebbles
        Age: 1
        Gender: female
      - Name: Dino
        Age: 5
        Gender: male

    $ yq '.members' flintstones.yaml # or 'flintstones.json'
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

Evaluate
--------

* `Evaluate the given expression against each yaml document in each file, in sequence <https://mikefarah.gitbook.io/yq/commands/evaluate>`_

Filtering
^^^^^^^^^

.. code-block:: console

    $ yq '.members[].Name' flintstones.yaml
    Fred
    Wilma
    Pebbles
    Dino

    $ yq '.members[] | .Name' flintstones.yaml
    Fred
    Wilma
    Pebbles
    Dino

    $ yq '.members[].Name,.members[].Age' flintstones.yaml
    Fred
    Wilma
    Pebbles
    Dino
    35
    25
    1
    5

    # equivalent: $ jq '.members[] | .Name,.Age' flintstones.json
    $ yq '.members[] | with_entries(select(.key | test("Name|Age")))' flintstones.yaml
    Name: Fred
    Age: 35
    Name: Wilma
    Age: 25
    Name: Pebbles
    Age: 1
    Name: Dino
    Age: 5

    # Does not work in 'yq' but does work in 'jq'
    "Fred"
    "Wilma"
    "Pebbles"
    "Dino"
    null

    $ yq '.members[1].Name,.members[1].Age' flintstones.yaml
    Wilma
    25

Keys and lengths
^^^^^^^^^^^^^^^^

.. code-block:: console

    $ yq '. | keys' flintstones.yaml
    - family
    - members

    $ yq '.members[0] | keys' flintstones.yaml
    - Name
    - Age
    - Gender

    $ yq '. | length' flintstones.yaml                # 2
    $ yq '.members | length' flintstones.yaml         # 4
    $ yq '.members[] | length' flintstones.yaml       # 3 3 3 3
    $ yq '.members[].Name | length' flintstones.yaml  # 4 5 7 4

Conversion
----------

Various conversions and formatting options are possible see, `Usage <https://mikefarah.gitbook.io/yq/usage/output-format>`_

.. code-block:: console

    $ yq -oy '.' flintstones.toml   # convert TOML to YAML
    $ yq -oy '.' flintstones.xml    # convert XML to YAML
    $ yq -oy '.' flintstones.json   # convert JSON to YAML

    $ yq -oj '.' flintstones.yaml   # convert YAML to JSON
    $ yq -oj '.' flintstones.xml    # convert XML to JSON
    $ yq -oj '.' flintstones.toml   # convert TOML to JSON

    $ yq -ox '.' flintstones.yaml   # convert YAML to XML
    $ yq -ox '.' flintstones.json   # convert JSON to XML
    $ yq -ox '.' flintstones.toml   # convert TOML to XML
