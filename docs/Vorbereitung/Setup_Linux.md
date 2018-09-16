Linux Setup
===========

Software installieren
---------------------

Auf einem Computer muss zunächst das Programm **esptool** installiert
werden. Damit lässt sich die Firmware auf den Mikrocontroller kopieren.
Man sagt zu diesem Vorgang auch *flashen*. Am einfachsten ist es, du
führst die drei folgenden Befehle auf jedem Computer aus.

> **Hinweis**
> Vergiss nicht **MeinBenutzername** durch den Benutzernamen zu ersetzt.
> Der Benutzername steht übrigens im Terminal vor dem @-Zeichen.

```shell
$ sudo apt-get install python-pip wget fritzing
$ sudo pip install mpfshell
$ sudo pip install esptool
$ sudo adduser MeinBenutzername dialout
```

Die erste Zeile installiert drei nützliche Programme auf dem Computer.
Mit dem zweiten und dritten Befehl werden die beiden Programme
**esptool** und **mpfshell** installiert.

Mit dem vierten Befehl wird der Benutzer der Gruppe *dialout*
hinzugefügt. Dadurch erhält der Benutzer die Rechte um auf die serielle
Schnittstelle des Computers zugreifen zu dürfen.

> **Hinweis**
> Damit die Änderung des vierten Befehls wirksam wird, muss sich der
> Benutzer einmal ab- und wieder anmelden.


Genauso wie ein Arduino benötigt auch ein ESP32-Mikrocontroller eine
Firmware. Aber anders dieser, wird ein ESP32 nicht von Werk aus mit der
Micropython-Firmware ausgestattet. Diese muss zunächst in den Speicher
des Prozessors geladen (*geflasht*) werden. Erst wenn das getan ist,
lassen sich Micropython-Programme darauf ausführen. In den Speicher des
ESP32 muss sozusagen ein neues Betriebsystem: **Micropython**
installiert werden.

Bei einem Arduino wird die Firmware jedes mal, wenn am Programm eine
Änderung vorgenommen wurde, überschrieben. Beim ESP32 passiert das nur
ein einziges Mal. Das Micropython-*Betriebssystem* hat nämlich ein
Dateisystem, in das man mit Hilfe des Programms **mpfshell** ganz leicht
Programm-Dateien kopieren oder löschen kann.

Frimware flashen
----------------

Lade dir zuerst die [zip-Datei mit den
Treibern](https://github.com/Tasm-Devil/Micropython-Tutorial-for-esp32/archive/master.zip)
herunter und entpacke sie in dein home-Verzeichnis. Öffne jetzt ein
Terminal in wechsle in den home-Verzeichnis (erster Befehl). Benenne den
Ordner `Micropython-Tutorial-for-esp32-master` um in `esp32` (zweiter
Befehl).

```console
$ cd ~
$ mv Micropython-Tutorial-for-esp32-master esp32
$ cd esp32/firmware/
```

Du befindest dich nach dem dritten Befehl im Ordner `~/esp32/firmware`.

Wenn du aktuellste
[Micropython-Firmware](http://micropython.org/download/#esp32) herunter
laden möchtest, dann speichere sie in diesen Ordner ab.

Verbinde jetzt des ESP32-Board mit deinem Computer. Mit dem ersten
Befehl `ls /dev/ttyUSB*` überprüfst du, ob das Board vom Computer
erkannt wird. Wird im Terminal `/dev/ttyUSB0` oder `/dev/ttyUSB1`
angezeigt, dann ist alles in Ordnung. Führe jetzt die beiden Befehle mit
`esptool.py` aus, um die Firmware auf das ESP32-Board zu flashen.

> **Achtung**
> Denke daran, vorher `firmware.bin` durch den Dateinamen der Firmware zu ersetzen.

```bash
$ ls /dev/ttyUSB*
/dev/ttyUSB0
$ esptool.py --port /dev/ttyUSB0 erase_flash
$ esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 firmware.bin
```

Treiber auf das Board kopieren
------------------------------

Im Verzeichnis `esp32` befinden sich drei wichtige Ordner: `lib`, `test`
und `wifi`. Der Inhalt dieser Ordner muss nun auf den ESP32 kopiert
werden. Dazu hast du vorhin das Programm `mpfshell` installiert. Führe
den folgenden Befehl aus um alle erforderlichen Dateien aus den drei
Ordnern auf das ESP32-Board zu kopieren.

```console
$ mpfshell -s upload.mpf
```
