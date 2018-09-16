Erste Schritte
==============

![image](../img/blink.gif)

Gleich kann es los gehen. Im ersten Kapitel wirst du eine RGB-LED zum
blinken bringen. Das tolle an einer RGB-LED ist, dass sie in allen
Farben leuchten kann. Jede Farbe kann durch das Mischen der drei
Grundfarben Rot, Grün und Blau erzeugt werden.

Aber bevor es los geht, gibt es noch paar Dinge die du wissen solltest.

Das Steckbrett
--------------

Wie du sicher weißt, fließt der Strom immer vom Plus-Pol zum Minus-Pol.
Plus heißt, dass das Potential hier bei 3,3 Volt liegt und Minus steht
für 0 Volt. Auf deinem Steckbrett stehen die roten Linien für Plus
(3,3V) und die beiden blauen Linien für Minus (0V). Die Farbe Schwarz
deutet auch manchmal auf den Minus-Anschluss hin.

::: {.note}
::: {.admonition-title}
Note
:::

Wenn du einen Blick auf den ESP32 wirfst, wirst du erkennen, dass zwei
Pins mit dem Aufdruck `GND` beschriftet sind. `GND` steht für *Ground*
und das heißt im Grunde nichts anderes als Minus.
:::

### Grundaufbau

Baue als erstes die Schaltung genau wie auf dem Bild nach. Achte ganz
penibel darauf, dass alle Kabel genau dort sind, wo sie hin gehören.
Lass dich von den Farben auf dem Bild nicht irritieren. Du wirst in
deinem Steckbrücken-Set selten die gewünschte Farbe in der richtigen
Länge finden. Wähle die Steckbrücke einfach nach der Länge aus.

![image](../img/Grundaufbau_Steckplatine.png)

Die beiden Steckbrücken rechts unten verbinden den Plus- und Minus-Pol
des ESP32 mit dem Steckbrett. 3,3V wird mit der roten Versorgungsleitung
und GND mit der blauen Versorgungsleitung verbunden.

Die beiden Kabel links verbinden den Plus- (rot) und Minus-Pol (blau)
der oberen und unteren Hälfte des Steckbretts miteinander.

Wenn du als nächstes das ESP32-Board einsetzt, wirst du mit ein wenig
Druck und Feinfühligkeit vorgehen müssen um weder das Board noch das
Steckbrett zu beschädigen. Bei manchen Steckbrettern ist das gar nicht
so einfach. Wenn du hier nicht vorsichtig bist, kann es passieren, dass
du später Probleme bekommst. Handle also unbedingt mit Gefühl!

![image](../img/Grundaufbau_mit_LED_Steckplatine.png)

Auf dem zweiten Bild kannst du sehen, wie du die RGB-LED und die drei
Widerstände mit dem ESP32 verbindest.

::: {.warning}
::: {.admonition-title}
Warning
:::

Ließ dir unbedingt zu erst den nächsten Abschnitt durch bevor du die
RGB-LED falsch herum einsetzt! Die Länge der vier Anschlusspins spielt
nämlich eine wichtige Rolle.
:::

Wissenswertes über LEDs
-----------------------

Es zwei wichtige Dinge, die man über LEDs wissen sollte. Normale LEDs
haben zwei Anschlüsse. Eine Kathode (Minus) und eine Anode (Plus).
RGB-LEDs bestehen im Prinzip aus drei normalen LEDs - eine rote, eine
blaue und eine grüne. Müsste eine RGB-LED dann nicht 6 Anschlüsse, für
drei Anoden und drei Kathoden, haben?

Die Antwort ist ganz einfach: Nein, denn innerhalb der RGB-LED werden
die drei Kathoden (Minuspole) der drei LEDs miteinander verbunden. Bei
der RGB-LED im Set handelt es sich um ein Bauteil vom Typ *common
cathode* also gemeinsame Kathode. Die Minuspole der drei LEDs haben also
einen gemeinsamen Anschluss. **Man erkennt ihn am langen Pin!**

**Dieser lange Anschlusspin sollte also immer mit Minus (blau) verbunden
sein.**

Es gibt auch RGB-LEDs vom Typ *common anode* zu kaufen. Sie haben
logischerweise einen gemeinsamen Pluspol.

![image](../img/RGB_LED.jpg)

Eine zweite Sache sollte man auch immer im Hinterkopf behalten. LEDs
dürfen niemals ohne einen Vorwiderstand in einen Stromkreis eingebaut
werden. Die 47Ohm Widerstände sind auf die 3,3V des ESP32 abgestimmt.
Jede LED bekommt einen eigenen Widerstand. Am besten kürzt du die
Beinchen der Widerstände mit einem Seitenschneider auf die halbe Länge.

Das Pinout-Diagramm
-------------------

Das Schaubild zeigt dir welche Funktion(en) die 30 Pins deines
ESP32-Boards haben. Nimm dir einen Moment Zeit und mache dir klar welche
fünf Pins du aktuell in deiner Schaltung benutzt.

![image](../img/ESP32-DOIT_Pinout.png)

Dein erstes Programm
--------------------

Hier ist ein kleines Python-Programm, das die LED dreimal rot blinken
lässt.

``` {.sourceCode .py}
from lib.display.led import LED
from time import sleep_ms

led_red = LED(15)
led_green = LED(4)
led_blue = LED(16)

for x in range(3):
    led_red.on()
    sleep_ms(500)
    led_red.off()
    sleep_ms(500)
```

Wie du das Programm auf den ESP32 kopierst, hängt von deinem
Betriebssystem ab. Wähle Windows oder Linux.

::: {.toctree}
Copy\_Windows Copy\_Linux
:::

Wenn alles geklappt hat, müsste die LED jetzt blinken. Gratulation!

Aufgaben
--------

-   Betrachte die Animation am Anfang der Seite. Um welchen Typ von
    RGB-LED handelt es sich. *common cathode* oder *common anode*?
-   Verändere das Programm so, dassder Pin 2 also `LED(2)` angesprochen
    wird. Was passiert?
-   Lass abwechselnd die rote, die blaue und die grüne LED leuchten.
-   Ändere die Blinkgeschwindigkeit.
-   Lass die LED abwechselnd in den 6 Farben: Rot, Violett, Blau, Cyan,
    Grün und Gelb leuchten.
