# How To Start Building

```eval_rst
.. tip:: 
    
    Ask in our `Discord <https://discord.gg/Gx3d28v>`_ for any questions!

```

## Joining the Minecraft Server

- **JAVA**: `play.btene.com` Download the modpack installer for your operating system from the [bte faq](https://buildtheearth.net/faq), then watch [this installer tutorial video](https://www.youtube.com/watch?v=T174gWwD1MU)
- **Bedrock**: There is **currently no bedrock support**, however this is **likely to change**, so keep a close eye on our Discord

When joining the server you will be prompted to link your account. Follow the directions given on your screen or in the chat, then rejoin the Minecraft server.

## Going to the Application Area
We have designated application areas for builders to create a trial build. You can build **anywhere** in the Northeastern US **after** you have been accepted. Where you choose to make your application area **does not matter in the future**.

1. Type the command `/apply` in chat
2. If you are in spectator mode you will be automatically teleported to the **Suburban** application area, else pick an application area: **Suburban** or **Urban**
3. If you want to choose a different application area, or you weren't given a choice, use the command `/apply` again

## Choosing a Building
1. Fly around in the application area in Minecraft and find an area with no building below you
2. Use the command `/terra where` and open the Google Maps link. The map is your Minecraft location in real life.

## Creating Outline

```eval_rst
.. topic:: Example: Creating an outline

    Mark each corner of the building, then select the two corners of and connect them for each wall with ``//line``. We use ``//line`` to create a straight line at any angle.
    
    This command uses a :ref:`pattern <Pattern>`. For this case use a :ref:`single block pattern <Single Block>`.

    Command::

        //line <pattern>

    Example for yellow wool::

        //line 35:4

    .. image:: ../_static/start/outline.mp4
        :width: 700
        :alt: Click Here

```

## Creating Walls
- [Measure](./measure.md) the height of the walls. You can quickly stack up the walls with WorldEdit by following the example below. Alternatively you can simply place blocks by hand.

```eval_rst
.. topic:: Example: Stacking up walls

    :ref:`Select <Creating a Selection>` the entire outline and the height of the wall above it. :ref:`<mask> <Mask>` and :ref:`<pattern> <Pattern>` are the :ref:`block ID <Block ID>` for the :ref:`single block pattern <Single Block>` you used creating the outline. The ``>`` is an :ref:`offset mask <Offset>`.

    Command::

        //replace ><mask> <pattern>
    
    Example for yellow wool::

        //replace >35:4 35:4

    .. image:: ../_static/start/outline.mp4
        :width: 700
        :alt: Click Here

```

## Adding House Features

```eval_rst
.. note:: 
    
    Keep in mind ONE Minecraft block is the equivalent of ONE METER cubed in real life

```
- [Create the roof](./roofs/index.md) of the building

You should now have a basic "shell" of the building.

- Place the [doors, windows, chimneys, fence, patio, every part](./detail.md) of the building. You can find examples of application builds [here](./examples.md)

You should now have a completed building!

- Submit the build [here](https://buildtheearth.net/bte-northeast) using [imgur](https://imgur.com) to create links

```eval_rst
.. tip::
    
    For the question "URL to screenshots(s) of previous builds..." use your newly created build
```