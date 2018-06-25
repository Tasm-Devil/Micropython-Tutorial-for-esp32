Micropython Tutorial for esp32
==============================

.. toctree::
   :maxdepth: 2
   :caption: Inhaltsverzeichnis:

   license

Vorwort
-------

.. warning::
    Diese Dokumentation befindet sich im Aufbau.

Bevor es los geht...
Diese Dokumentation richtet sich an 
Wie ist dies Tutorial entstanden?
Im Netz finden sich fast keine deutschsprachigen Anleitungen zu Micropython. Nachdem  ich mich intensiv mit dem esp8266 und dem Nachfolger esp32 auseinandergesetzt habe, viele Blogs und englischsprachige Tutorials gelesen und die Vor- und Nachteile gegenüber dem erprobten Arduino abgewägt habe, bin ich zu der Entscheidung gelangt, dass endlich ein deutschsprachiges Tutorial für den Schulunterricht oder das Selbststudium her muss.

.. note::
    Wie ist der Aufbau dieses Kurses?

#. Hardware (IOT Box)
#. Software (Firmware, Treiber, Bibliotheken, Tools)
#. Dieses Tutorial und die Referenz

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

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Was
     - Wo
     - Wie viel
   * - ESP32
     - AliExpress
     - 7,68 €
   * - Steckplatine groß
     - AliExpress
     - 1,95 €
