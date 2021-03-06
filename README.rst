Lighthouse API client
=====================

This project provides a ready to go implementation of the `Lighthouse
API Client <https://github.com/opengear/oglhclient>`__ as a Slack Bot.

It has also a `Docker
image <https://hub.docker.com/r/opengeardev/oglhslack/>`__ for launching
the slack bot in minutes.

Authentication
--------------

The **Lighthouse API Client** expects to find the following environment
variables:

-  **(required)** ``OGLH_API_USER`` a valid Lighthouse user
-  **(required)** ``OGLH_API_PASS`` a valid Lighthouse user's password
-  **(required)** ``OGLH_API_URL`` the Lighthouse API url without
   ``/api/v1``

Lighthouse Slack Bot
--------------------

It expects to find the following environment variables:

-  **(required)** ``SLACK_BOT_TOKEN`` which is provided by Slack at the
   moment of `creating a bot <https://api.slack.com/bot-users>`__.
-  **(required)** ``SLACK_BOT_NAME`` is the name given to the Slack bot.
-  **(required)** ``SLACK_BOT_DEFAULT_CHANNEL`` a default Slack channel
   name used for warnings.
-  **(optional)** ``SLACK_BOT_DEFAULT_LOG_CHANNEL`` a Slack channel name
   for logs, if it is not provided, logs will be printed to a file only,
   but logs classified as high priority like warnings and errors will be
   printed to the ``SLACK_BOT_DEFAULT_CHANNEL`` when
   ``SLACK_BOT_DEFAULT_LOG_CHANNEL`` is not set.
-  **(optional)** ``SLACK_BOT_ADMIN_CHANNEL`` is the name for the
   administrator channel, if no name is informed, it is assumed to be
   **oglhadmin**.

The **Lighhouse** Slack bot can be triggered as simple as:

.. code:: python

    >>> from oglhslack import OgLhSlackBot
    >>> slack_bot = OgLhSlackBot()
    >>> slack_bot.listen()

Or, straight from the terminal:

.. code:: bash

    $ python oglhslack.py

Commands
--------

It is possible to interact with the Slack Bot in private messages (PM),
private or public channels. When commands are not performed in private
messages, they must be prefixed by ``@mybot``, where ``mybot`` is the
bot's name.

Built in commands
~~~~~~~~~~~~~~~~~

There is a small set of commands which can be found the bot's help, they
are pretty straight in what they do. It is possible this list of
commands through:

::

    @mybot help

Some commands have **(admin only)** on theirs descriptions, indicating
that they can be performed in the ``oglhadmin`` channel.

API client commands
~~~~~~~~~~~~~~~~~~~

This commands follow the `Lighthouse API
Client <https://github.com/opengear/oglhclient>`__ conventions.

For listing objects like ``nodes`` it is possible to perform:

::

    @mybot list nodes

For listing tags belonging to a node with id *my-node-name*:

::

    @mybot list tags from node my-node-name

For listing smartgroups:

::

    @mybot list smartgroups from nodes

For getting information regarding to a specific node:

::

    @mybot find node my-node-name

For getting systems's information:

::

    @mybot get hostname from system

It works basically as:

Listing objects of a given type, like **nodes**, **ports**, and so on. >
**list** *objects*

Listing objects of a given type, belonging to a parent object, like
**system**. > **list** *objects* **from** *parent-object*

Listing objects of a given type, belonging to a parent object specified
by its id. > **list** *objects* **from** *parent-object* *parent-name*

Find specific objects by their ids. > **find** *object* *object-name*

Find specific objects by their ids, when belonging to parent objects. >
**find** *object* *object-name* **from** *parent-object*

    **find** *object* *object-name* **from** *parent-object*
    *parent-name*

Get objects when **list** and **find** do not apply > **get** *object*
**from** *parent-object*

Channels conventions
--------------------

Administration channel
~~~~~~~~~~~~~~~~~~~~~~

Commands that make changes in Lighthouse are not allowed in normal
channels or in private messages.

In order to execute such commands, it is required that the Slack
administrator creates a channel named **oglhadmin**, or with the name
specified in the ``SLACK_BOT_ADMIN_CHANNEL`` environment variable. This
channel is supposed to be open for authorized members only.

Docker image
------------

The Opengear Lighthouse docker image is available at
https://hub.docker.com/r/opengeardev/oglhslack/.

It requires a file containing the environment variables as specified
`here <https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e-env-env-file>`__.

It is supposed to be like:

::

    SLACK_BOT_TOKEN=xoxb-************-************************
    SLACK_BOT_NAME=mybotname
    SLACK_BOT_DEFAULT_CHANNEL=myDefaultChannel
    SLACK_BOT_DEFAULT_LOG_CHANNEL=myDefaultLogChannel
    SLACK_BOT_ADMIN_CHANNEL=oglhadmin
    OGLH_API_USER=myOgLhUser
    OGLH_API_PASS=myOgLhPassword
    OGLH_API_URL=https://oglh-octo.opengear.com

For launching the Slack bot just run:

.. code:: bash

    $ sudo docker run --env-file /path/to/my/env.list opengeardev/oglhslack
