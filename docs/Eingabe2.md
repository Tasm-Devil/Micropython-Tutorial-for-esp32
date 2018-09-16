Eingabe Teil 2
==============

Umweltsensoren
--------------

Die beiden Umweltsensoren bme280 und bh1750 \... Am besten schließt du
vorher das oled-Display an.

``` {.sourceCode .py}
import test.i2c
```

### Quellen

-   <https://github.com/kevbu/micropython-bme280>
-   <https://github.com/PinkInk/upylib/tree/master/bh1750>

Beschleunigungssensor
---------------------

### Quellen

-   <http://andidinata.com/download/>

RFID
----

Verbinde **3.3V** mit der roten Versorgungsspannung auf den Steckbrett
und **GND** mit der blauen. Verbinde **MOSI** mit **GPIO23 (SPI MOSI)**,
**MISO** mit **GPIO19 (SPI MISO)**, **SCK** mit **GPIO18 (SPI CLK)** und
**SDA** mit **GPIO5 (SPI CS0)**. Die Pins **IRQ** und **RST** brauchst
du nicht anzuschließen.

``` {.sourceCode .py}
from machine import Pin, SPI
from lib.rfid.mfrc522 import MFRC522
from time import sleep_ms

# Initialisiere den SPI-Bus
sck = Pin(18, Pin.OUT)
mosi = Pin(23, Pin.OUT)
miso = Pin(19, Pin.OUT)
sda = Pin(5, Pin.OUT)
spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

try:
    while True:
        rdr = MFRC522(spi, sda)
        uid = ""
        (stat, tag_type) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                print(uid)
                sleep_ms(100)
except KeyboardInterrupt:
    print("Bye")
```

``` {.sourceCode .py}
import test.rfid
```

### Quellen

-   <https://github.com/wendlers/micropython-mfrc522>
