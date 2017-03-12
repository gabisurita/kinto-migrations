Kinto Migrations
################

CLI tool to perform high level migrations using the HTTP API on a Kinto Server.

Installation
============

With pip::

    $ pip install kinto-migrations

Getting stated
==============

Let's imagine we want to create initialize our Kinto server with some stuff:


.. code-block:: yaml

    $buckets:

        private_data:
            description: Data that is mine and I may share with frieds.

            $groups:
                frieds:
                    members:
                        - portier:myfriend@gmail.com

            $collections:
                expenses:
                    description: Money stuff.

                pictures:
                    $permissions:
                        read:
                            - "/buckets/private_data/friends"

        public_data:
            description: My public data.

            $permissions:
                read:
                    - "system.Everyone"

            $collections:
                blog_posts:
                    url: "me.github.io"

                    $records:
                        hello_world: {}


Let's save this to a YAML file and run::

    $ kinto-migrate --file models.yml --server https://kinto.dev.mozaws.net/v1/ --auth admin:pass

You should specify the server and an authentication token. By default the
migrate tool will prompt for a ``models.yml`` file on the current directory or
you can specify a file using `--file`` or ``-f``.


This will crete if not exist all the listed endpoints on the Kinto API.


Schema reference
================

Resources and other reserved words start with a dollar-sign ($). This package
supports the basic structure of the Kinto HTTP API.

.. code-block:: yaml

    $buckets:
        (...)
        $groups:
            (...)
        $collections:
            (...)
            $records:
                (...)


Any resource data can be included inline under the resource attributes. By default,
if no collection schema is provided, any attribute is accepted as in the Kinto API.

.. code-block:: yaml

    $buckets:
        my_bucket:
            name: My Bucket
            tags:
                - Mine
                - Not yours


Permissions can be setted under any resource using the ``$permissions`` attribute.

.. code-block:: yaml

    $buckets:
        my_public_bucket:
            $permissions:
                read:
                    - system.Everyone
