WorldEdit
=========
`WorldEdit <https://enginehub.org/worldedit/>`_ has many and many abilities this document only covers some of them.

.. attention::

    Arguments surrounded by ``[ ]`` are optional, those surrounded by ``< >`` are required.

Other Resources
---------------
* `Building Guidebook <https://docs.google.com/document/d/1L7fzjEC3KnxSA-1OKdTy_4xBpbkG-4aTQ1ogXlqRJPA/edit#heading=h.km1t1mqmynvf>`_
* `Official WorldEdit Docs <https://worldedit.enginehub.org/en/latest/commands/>`_ (Documents a WorldEdit version more recent than the one we use, so some things act differently)
* `Grian's Video <https://www.youtube.com/watch?v=SOOvommDpUA>`_
* `Unofficial Fandom <https://minecraft-worldedit.fandom.com/wiki/Worldedit_Commands>`_

Creating A Selection
--------------------
**Selections are an important part of WorldEdit and you need to learn it first.** Read `this <https://worldedit.enginehub.org/en/latest/usage/regions/selections/>`_.

//set
-----
Sets selection to the given pattern. Uses a :ref:`pattern <Pattern>`.

.. code-block::

    //set <pattern>

//replace
---------
Replaces "from" to "to". Uses a :ref:`mask <Mask>` and :ref:`pattern <Pattern>`.

.. code-block::

    //replace [from (mask)] <to (pattern)>

Pattern
-------
A pattern determines what blocks a command places.

`Detailed explanation of a pattern <https://worldedit.enginehub.org/en/latest/usage/general/patterns/>`_, including advanced types of patterns. (Explanation uses 1.13+ names, keep in mind we use :doc:`1.12.2 IDs <id>`. It also contains features not present in our older version of WorldEdit)

Single Block
````````````
Inorder to WorldEdit with a singular block, use a singular :doc:`block ID <id>`.

.. topic:: Example: Setting Orange Wool

    Pattern::

        35:1

    Setting a selection to orange wool::

        //set 35:1

Random
``````
Inorder to WorldEdit with multiple blocks in a random pattern, use multiple patterns/:doc:`block IDs <id>`.

You can specify weights by adding a ``x%`` in front of the pattern.

.. note:: Percentage weights do not need to add up to 100. They are a ratio to each other.

.. topic:: Example: Setting equal percentages of orange, magenta, and yellow wool

    Pattern::

        35:1,35:2,35:4

    Command::

        //set 35:1,35:2,35:4

.. topic:: Example: Setting 1/5 orange, 1/5 magenta, and 3/5 yellow wool

    Pattern::

        20%35:1,20%35:2,60%35:4

    Command::

        //set 20%35:1,20%35:2,60%35:4

Mask
----
`Detailed explanation of a mask <https://worldedit.enginehub.org/en/latest/usage/general/masks/>`_, including advanced types of patterns. (Explanation uses 1.13+ names, keep in mind we use :doc:`1.12.2 IDs <id>`. It also contains features not present in our older version of WorldEdit)

Block
`````
Works the same as a :ref:`single block <Single Block>` or :ref:`random block <Random>` pattern.

.. topic:: Example: Replacing orange wool with magenta wool

    Mask::

        35:1

    Command::

        //replace 35:1 35:2
        
Negation
````````
Adding a ``!`` negates everything after it. Another way to look at it: the result does the opposite of the mask after the ``!``.

.. topic:: Example: Replacing everything that isn't orange wool with stone

    Without the ``!``, the command would replace orange wool with stone. ``35:1`` is the :ref:`block mask <Block>` that is negated.

    Mask::

        !35:1

    Command::

        //replace !35:1 1

Offset
``````
Adding a ``>`` before another mask matches blocks above the mask, adding a ``<`` matches blocks below the mask.

.. topic:: Example: Replacing everything above orange wool with polished diroite

    The mask ``35:1`` matches all orange wool, adding a ``>`` matches everything above orange wool.

    Mask::

        >35:1

    Command::

        //replace >35:1 1:4