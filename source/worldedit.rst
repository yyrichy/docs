WorldEdit
=========
`WorldEdit <https://enginehub.org/worldedit/>`_ has many and many commands this document only covers some of them.

.. important::

    Arguments surrounded by "[" and "]" are optional, those surrounded by "<" and ">" are required.

Other Resources
---------------
* `Building Guidebook <https://docs.google.com/document/d/1L7fzjEC3KnxSA-1OKdTy_4xBpbkG-4aTQ1ogXlqRJPA/edit#heading=h.km1t1mqmynvf>`_
* `Official WorldEdit Docs <https://worldedit.enginehub.org/en/latest/commands/>`_ (Documents a WorldEdit version more recent than the one we use, so some things act differently)
* `Grian's Video <https://www.youtube.com/watch?v=SOOvommDpUA>`_
* `Unofficial Fandom <https://minecraft-worldedit.fandom.com/wiki/Worldedit_Commands>`_

Replace
-------
Uses a :ref:`pattern <Pattern>`.

.. code-block::

    //replace [mask] <pattern>

Pattern
-------
`Detailed explanation <https://worldedit.enginehub.org/en/latest/usage/general/patterns/>`_ of a pattern, including advanced types of patterns. (Explanation uses 1.13+ names, keep in mind we use :doc:`1.12.2 IDs <id>`. It also contains features not present in our older version of WorldEdit)

Basic
`````

Single
''''''
Inorder to WorldEdit with a singular block, use a singular :doc:`block ID <id>`.

.. topic:: Example: Setting Orange Wool

    Pattern::

        35:1

    Setting a selection to orange wool::

        //set 35:1

Random
''''''
Inorder to WorldEdit with random blocks, use multiple patterns/:doc:`block IDs <id>`.

You can specify weights by adding a ``x%`` in front of the pattern.

.. note:: Percentage weights do not need to add up to 100. They are a ratio to each other.

.. topic:: Example: Equally Setting Orange Wool Magenta Wool Yellow Wool

    Pattern::

        35:1,35:2,35:4

    Setting a selection to orange wool::

        //set 35:1,35:2,35:4

.. topic:: Example: Setting 1/5 Orange Wool, 1/5 Magenta Wool, 3/5 Yellow Wool

    Pattern::

        20%35:1,20%35:2,60%35:4

    Setting a selection to orange wool::

        //set 20%35:1,20%35:2,60%35:4