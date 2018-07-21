Ausgabe
*******

Jedes datenverarbeitende System - wie ein Mensch oder ein Computer - gliedert sich in die drei Teile: Eingabe, Verarbeitung und Ausgabe. Eine Möglichkeit etwas auszugeben haben wir im letzten Kapitel kennen gelernt. In diesem Kapitel gehen wir etwas genauer auf die Klasse LED ein und lernen im Anschluss, wie man ein Display und einen Summer an den ESP32 anschließt.

Spaß mit LEDs
=============

Die Datei ``test/led.py`` demonstriert die Möglichkeiten der Klassen ``LED`` und ``RGB_LED``

..  code-block:: py
    :linenos:
    
    from lib.display.led import LED, RGB_LED

    led_red = LED(15)
    led_green = LED(4)
    led_blue = LED(16)

    led_red.pulse(10)
    led_green.pulse(10)
    led_blue.pulse(10)

    rgb = RGB_LED(led_red, led_green, led_blue)
    rgb.rainbow()
    
    led_red.off()
    led_green.off()
    led_blue.off()


..  code-block:: py
    
    import test.led

Das LED-Matrix Display
======================

..  code-block:: py
    
    import test.matrix

Das OLED-Display
================


Töne Erzeugen mit einem Summer
==============================

