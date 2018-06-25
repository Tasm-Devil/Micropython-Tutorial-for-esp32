Micropython Tutorial for esp32
==============================

.. toctree::
   :maxdepth: 3
   :caption: Inhaltsverzeichnis:

   license

Vorwort
-------

Bevor es los ``geht``...

.. code-block:: console

   $ sudo apt-get install python-pip wget
   $ sudo pip install mpfshell
   $ sudo pip install esptool
   $ sudo adduser MeinBenutzername dialout

Beispiel-code

.. code-block:: py
   :linenos:

   import machine
   import time
   led_rot=machine.Pin(15, machine.Pin.OUT)
   led_blau=machine.Pin(14, machine.Pin.OUT)
   led_gruen=machine.Pin(12, machine.Pin.OUT)

   for x in range (3):
       led_rot.high()
       time.sleep(1)
       led_rot.low()
       time.sleep(1)

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
