# WorldEdit

[WorldEdit](https://enginehub.org/worldedit/) has many and many abilities this document only covers some of them.

```eval_rst
.. attention::

    Arguments surrounded by ``[ ]`` are optional, those surrounded by ``< >`` are required.

```

## Other Resources

* [Building Guidebook](https://docs.google.com/document/d/1L7fzjEC3KnxSA-1OKdTy_4xBpbkG-4aTQ1ogXlqRJPA/edit#heading=h.km1t1mqmynvf)
* [Official WorldEdit Docs](https://worldedit.enginehub.org/en/latest/commands/) (Documents a WorldEdit version more recent than the one we use, so some things act differently)
* [Grian's Video](https://www.youtube.com/watch?v=SOOvommDpUA)
* [Unofficial Fandom](https://minecraft-worldedit.fandom.com/wiki/Worldedit_Commands)

## Creating A Selection

**Selections are an important part of WorldEdit and you need to learn it first.** Read [this](https://worldedit.enginehub.org/en/latest/usage/regions/selections/)

## Commands
### //set
Sets selection to the given pattern. Uses a [pattern](#pattern).
```eval_rst
.. code-block::

    //set <pattern>

```
### //replace
Replaces "from" to "to". "from" is a [mask](#mask) and "to" is a [pattern](#pattern).
```eval_rst
.. code-block::

    //replace [from] <to>

```
## Pattern
A pattern determines what blocks a command places.

- [Detailed explanation of a pattern](https://worldedit.enginehub.org/en/latest/usage/general/patterns/) including advanced types of patterns. (Explanation uses 1.13+ names, keep in mind we use [1.12.2 IDs](id) It also contains features not present in our older version of WorldEdit)

[single block pattern]: #single-block-pattern
### Single Block
Inorder to WorldEdit with a singular block, use a singular [block ID](id).
```eval_rst
.. topic:: Example: Setting Orange Wool

    Pattern::

        35:1

    Setting a selection to orange wool::

        //set 35:1

```
### Random
Inorder to WorldEdit with multiple blocks in a random pattern, use multiple patterns/[block IDs](id)

You can specify weights by adding a `x%` in front of the pattern.
```eval_rst
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

```
## Mask
[Detailed explanation of a mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/), including advanced types of patterns. (Explanation uses 1.13+ names, keep in mind we use [1.12.2 IDs](id) It also contains features not present in our older version of WorldEdit)

### Block
Works the same as a [single block](#single-block) or [random block](#random) pattern.
```eval_rst
.. topic:: Example: Replacing orange wool with magenta wool

    Mask::

        35:1

    Command::

        //replace 35:1 35:2

```
### Negation
Adding a `!` negates everything after it. Another way to look at it: the result does the opposite of the mask after the `!`.
```eval_rst
.. topic:: Example: Replacing everything that isn't orange wool with stone

    Without the ``!``, the command would replace orange wool with stone. ``35:1`` is the :ref:`block mask <Block>` that is negated.

    Mask::

        !35:1

    Command::

        //replace !35:1 1

```
### Offset
Adding a `>` before another mask matches blocks above the mask, adding a `<` matches blocks below the mask.
```eval_rst
.. topic:: Example: Replacing everything above orange wool with polished diroite

    The mask ``35:1`` matches all orange wool, adding a ``>`` matches everything above orange wool.

    Mask::

        >35:1

    Command::

        //replace >35:1 1:4

```