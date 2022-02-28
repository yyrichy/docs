How To Start Building
=====================
.. tip:: 
    
    Ask in our `Discord <https://discord.gg/Gx3d28v>`_ for any questions!

Joining the Minecraft Server
----------------------------
* **JAVA**: Use the IP address ``play.btene.com``, download the modpack installer for your Operating System from `this faq <https://buildtheearth.net/faq>`_, then watch `this video <https://www.youtube.com/watch?v=T174gWwD1MU>`_
* **Bedrock**: There is currently no bedrock support, this is likely to change, so keep a close eye on our Discord

When joining the server you will be prompted to link your account. Follow the directions given on your screen or in the chat, then rejoin the Minecraft server.

Going to the Application Area
--------------------------------
We have designated application areas for builders to create a trial build. You can build anywhere in the Northeastern US *after* you have been accepted.

#. Type the command ``/apply`` in chat
#. If you in spectator mode you will be automatically teleported to the Suburban application area, else pick an application area: Suburban or Urban
#. If you want to choose a different application area, or you weren't given a choice, use the command ``/apply`` again

Choosing a Building
--------------------
.. note:: 
    
    Keep in mind ONE Minecraft block is the equivalent of ONE METER cubed

* Fly around in the application area in Minecraft and find an area with no building below you
* Use the command ``/where`` and open the Google Maps link. The map is your Minecraft location in real life.

Creating Outline
----------------
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

Creating Walls
--------------
* :ref:`Measure <Measuring>` the height of the walls. You can quickly stack up the walls with WorldEdit by following the example below. Alternatively you can simply place blocks by hand.

.. topic:: Example: Stacking up walls

    :ref:`Select <Creating a Selection>` the entire outline and the height of the wall above it. :ref:`<mask> <Mask>` and :ref:`<pattern> <Pattern>` are the :ref:`block ID <Block ID>` for the :ref:`single block pattern <Single Block>` you used creating the outline. The ``>`` is an :ref:`offset mask <Offset>`.

    Command::

        //replace ><mask> <pattern>
    
    Example for yellow wool::

        //replace >35:4 35:4

    .. image:: ../_static/start/outline.mp4
        :width: 700
        :alt: Click Here

Adding House Features
---------------------
* :doc:`Create the roof <roofs/index>` of the building

You should now have a basic "shell" of the building.

* Place the :ref:`doors, windows, chimneys, fence, patio, every part <Detailing>` of the building

You should now have a completed building!

* Submit the build `here <https://buildtheearth.net/bte-northeast>`_ using `imgur <https://imgur.com>`_ to create links

.. tip::
    
    For the question "URL to screenshots(s) of previous builds..." use your newly created build