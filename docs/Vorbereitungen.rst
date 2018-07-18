Vorbereitungen
**************

Bevor es mit dem Programmieren los gehen kann, sind ein paar Vorarbeiten zu erledigen. Auf den Computern sind Programme zu installieren und der ESP32 muss vorbereitet werden um mit ihm programmieren zu können.

1. Die erforderliche Software installieren
------------------------------------------

Auf einem Computer muss zunächst das Programm **esptool** installiert werden. Damit lässt sich die Firmware auf den Mikrocontroller kopieren. Man sagt zu diesem Vorgang auch *flashen*. Am einfachsten ist es, du führst die drei folgenden Befehle auf jedem Computer aus.

..  note::
    Vergiss nicht **MeinBenutzername**  durch den Benutzernamen zu ersetzt. Der Benutzername steht übrigens im Terminal vor dem @-Zeichen.

..  code-block:: console
    
    $ sudo apt-get install python-pip wget fritzing
    $ sudo pip install mpfshell
    $ sudo pip install esptool
    $ sudo adduser MeinBenutzername dialout

Die erste Zeile installiert drei nützliche Programme auf dem Computer. Mit dem zweiten und dritten Befehl werden die beiden Programme **esptool** und **mpfshell** installiert. 

Mit dem vierten Befehl wird der Benutzer der Gruppe *dialout* hinzugefügt. Dadurch erhält der Benutzer die Rechte um auf die serielle Schnittstelle des Computers zugreifen zu dürfen.

..  note::
    Damit die Änderung des vierten Befehls wirksam wird, muss sich der Benutzer einmal ab- und wieder anmelden.

Genauso wie ein Arduino benötigt auch ein ESP32-Mikrocontroller eine Firmware. Aber anders dieser, wird ein ESP32 nicht von Werk aus mit der Micropython-Firmware ausgestattet. Diese muss zunächst in den Speicher des Prozessors geladen (*geflasht*) werden. Erst wenn das getan ist, lassen sich Micropython-Programme darauf ausführen. 
In den Speicher des ESP32 muss sozusagen ein neues Betriebsystem: **Micropython** installiert werden.

Bei einem Arduino wird die Firmware jedes mal, wenn am Programm eine Änderung vorgenommen wurde, überschrieben. Beim ESP32 passiert das nur ein einziges Mal. Das Micropython-*Betriebssystem* hat nämlich ein Dateisystem, in das man mit Hilfe des Programms **mpfshell** ganz leicht Programm-Dateien kopieren oder löschen kann.

2. Die Frimware flashen
-----------------------

Lade dir zuerst die `zip-Datei mit den Treibern <https://github.com/Tasm-Devil/Micropython-Tutorial-for-esp32/archive/master.zip>`_ herunter und entpacke sie in dein home-Verzeichnis. Öffne jetzt ein Terminal in wechsle in den home-Verzeichnis (erster Befehl). Benenne den Ordner ``Micropython-Tutorial-for-esp32-master`` um in ``esp32`` (zweiter Befehl).

..  code-block:: console
    
    $ cd ~
    $ mv Micropython-Tutorial-for-esp32-master esp32
    $ cd esp32/firmware/

Du befindest dich nach dem dritten Befehl im Ordner ``~/esp32/firmware``.

Wenn du aktuellste `Micropython-Firmware <http://micropython.org/download/#esp32>`_ herunter laden möchtest, dann speichere sie in diesen Ordner ab.

Verbinde jetzt des ESP32-Board mit deinem Computer. Mit dem ersten Befehl ``ls /dev/ttyUSB*`` überprüfst du, ob das Board vom Computer erkannt wird. Wird im Terminal ``/dev/ttyUSB0`` oder ``/dev/ttyUSB1`` angezeigt, dann ist alles in Ordnung. Führe jetzt die beiden Befehle mit ``esptool.py`` aus, um die Firmware auf das ESP32-Board zu flashen.

..  note::
    Achtung! Denke daran, vorher ``firmware.bin`` durch den Dateinamen der Firmware zu ersetzen.

..  code-block:: console
    
    $ ls /dev/ttyUSB*
    /dev/ttyUSB0
    $ esptool.py --port /dev/ttyUSB0 erase_flash
    $ esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 firmware.bin

3. Die Treiber auf das Board kopieren
-------------------------------------

Im Verzeichnis ``esp32`` befinden sich drei wichtige Ordner: ``lib``, ``test`` und ``wifi``. Der Inhalt dieser Ordner muss nun auf den ESP32 kopiert werden. Dazu hast du vorhin das Programm ``mpfshell`` installiert. Führe den folgenden Befehl aus um alle erforderlichen Dateien aus den drei Ordnern auf das ESP32-Board zu kopieren.

..  code-block:: console
    
    $ mpfshell -s upload.mpf

Von der Software-Seite her bist du jetzt bereit zu programmieren. Nimm dir aber noch die Zeit um auch jetzt schon deine Hardware vorzubereiten. Du darfst jetzt auch alle Tütchen auspacken.

4. Die Hardware Vorbereiten
---------------------------

Im Sortiment befinden sich 5 Taster und zwei RGB-LEDs. Die Beinchen der Leuchtdioden sind viel zu lang und viel zu nah beieinander. Versuche mit etwas Geschick die Beinchen so wie auf dem Bild zu biegen. Im Anschluss kannst du die Beinchen mit einem Seitenschneider auf die halbe Länge kürzen. Jetzt passt die LED super in das Steckbrett.

..  image:: img/RGB_LED.jpg

..  warning::
    Achte unbedingt darauf, dass die Länge der Beinchen vor und nach dem Kürzen das gleiche Verhältnis zueinander haben. Das längste Beinchen sollte also auch nach dem Kürzen länger als die anderen sein.

Die vier Beinchen der Taster musst du mit der Pinzette um 90° verdrehen damit sie in das Steckbrett passen. Schau dir am besten die beiden Fotos an. Dann weißt du was du machen musst. Alle Taster sollen so wie der rechts im Bild aussehen.

..  image:: img/Taster1.jpg

Schau dir auf dem nächsten Bild die Beinchen an. Sie sind genau um 90° verdreht.

..  image:: img/Taster2.jpg

Fertig? Noch nicht ganz. Einige Sensoren werden mit Stiftleisten geliefert. Diese Stifte müssen noch an die Platine gelötet werden. Lass dir helfen wenn du noch nie gelötet hast.

5. Das Pinout-Diagramm ausdrucken
---------------------------------

Last but not least solltest du dir das Pinout-Diagramm ausdrucken. Klicke dazu mit der rechten Maustaste auf das Bild und wähle anschließend *Bild anzeigen* im Kontextmenü deines Browsers aus. Danach öffnet sich ein neuer Tab in deinem Browser. Drucke das Bild aus indem du auf deiner Tastatur die Tasten **Strg** und **P** gemeinsam drückst.

..  image:: img/ESP32-DOIT_Pinout.png
