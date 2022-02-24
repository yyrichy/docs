How To Start Building
=====================

.. note:: 
    
    Ask in our Discord server for any questions!

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

Building
--------
.. note:: 
    
    Keep in mind ONE Minecraft block is the equivalent of ONE METER cubed

* Fly around in the application area in Minecraft and find an area with no building below you
* Use the command ``/where`` and open the Google Maps link
* Create an outline of your building following the video below:

.. figure:: ../_static/start/outline.mp4
    :width: 600
    :alt: Click Here

    The command ``//line <pattern>`` uses a :ref:`pattern <Pattern>`. I suggest using a :ref:`single block pattern <Single Block>` of a :ref:`block ID <Block ID>`.

* :ref:`Measure <Measuring>` then create the walls. You can quickly stack up the walls by using an :ref:`offset mask <Offset>` with the ``//replace`` command, then repeatedly execute the command.

.. topic:: Example: Stacking up walls

    :ref:`Select <Creating a Selection>` the entire outline and the height of the wall above it. ``x`` is the :ref:`pattern <Pattern>`/:ref:`block ID <Block ID>` you used creating the oultine.

    Command::

        //replace >x x

* :doc:`Create the roof <roofs/index>` of the building

You should now have a basic "shell" of the building.

* Place the :ref:`doors, windows, chimneys, every part <Detailing>` of the building

You should now have a completed building!

* Submit the build `here <https://buildtheearth.net/bte-northeast>`_ using `imgur <https://imgur.com>`_ to create links

.. tip::
    
    For the question "URL to screenshots(s) of previous builds..." use your newly created build