Vorbereitungen
**************

Bevor es mit dem Programmieren los gehen kann, sind ein paar Vorarbeiten zu erledigen. Auf den Computern sind Programme zu installieren und der ESP32 muss vorbereitet werden um mit ihm programmieren zu können.


Software installieren
---------------------

Auf wenigsten einem Computer muss zunächst das Programm **esptool** installiert werden. Damit lässt sich die Firmware auf den Mikrocontroller kopieren. Man sagt zu diesem Vorgang auch *flashen*. Am einfachsten ist es, Sie führen die drei folgenden Befehle auf jedem Computer aus.

.. note::
   
   Vergessen Sie nicht **MeinBenutzername**  durch den Benutzernamen zu ersetzt. Der Benutzername steht übrigens vor dem @-Zeichen.

.. code-block:: console
   
   $ sudo apt-get install python-pip wget fritzing
   $ sudo pip install mpfshell
   $ sudo pip install esptool
   $ sudo adduser MeinBenutzername dialout

Die erste Zeile installiert drei nützliche Programme auf dem Computer. Mit dem zweiten und dritten Befehl werden die beiden Programme **esptool** und **mpfshell** installiert. 

Mit dem vierten Befehl wird der Benutzer der Gruppe dialout hinzugefügt. Dadurch erhält er die Rechte um auf die Serielle Schnittstelle des PCs zuzugreifen.

.. note::
   
   Damit die Änderung des vierten Befehls wirksam wird, muss sich der Benutzer einmal ab- und wieder anmelden.

Genauso wie ein Arduino benötigt auch ein ESP32-Mikrocontroller eine Firmware. Aber anders dieser, wird ein ESP32 nicht von Werk aus mit der Micropython-Firmware ausgestattet. Diese muss zunächst in den Speicher des Prozessors geladen (*geflasht*) werden. Erst wenn das getan ist, lassen sich Micropython-Programme darauf ausführen. 
In den Speicher des ESP32 muss sozusagen ein neues Betriebsystem: **Micropython** installiert werden.

Bei einem Arduino wird die Firmware jedes mal, wenn am Programm eine Änderung vorgenommen wurde, überschrieben. Beim ESP32 passiert das nur ein einziges Mal. Das Micropython*-Betriebssystem* hat nämlich ein Dateisystem in das man mit Hilfe des Programms **mpfshell** ganz leicht Programm-Dateien kopieren oder löschen kann.

Die Frimware flashen
--------------------

Als erstes sollten Sie sich die aktuellste `Micropython-Firmware <http://micropython.org/download/#esp32>`_ herunter und speichert sie im Ordner ``firmware`` ab. Im gleichen Ordner startet man jetzt ein Terminal.
Mit dem Befehl ``ls /dev/ttyUSB*`` kann man überprüfen, ob ein Board vom Computer erkannt wurde.
Jetzt wird der erste ESP32 mit dem Computer verbunden und anschließend werden die beiden folgenden Befehle ausgeführt:

.. code-block:: console
   
   esptool.py --port /dev/ttyUSB0 erase_flash
   esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 firmware.bin

.. note::
   
   Denken Sie daran, vorher ``firmware.bin`` durch den Dateinamen der Firmware zu ersetzen.



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
