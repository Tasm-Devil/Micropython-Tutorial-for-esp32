from time import sleep_ms

# RFID-Modul Anschlussplan für ESP32
# SDA   =   GPIO 5
# SCK   =   GPIO 18
# MOSI  =   GPIO 23
# MISO  =   GPIO 19
# 3.3   =   3.3
# GND   =   GND
# IRQ und RST werden nicht benötigt

# 8x8-LED-Modul Anschlussplan für ESP32
# CS    =   GPIO 2
# SCK   =   GPIO 18
# MOSI  =   GPIO 23
# VCC   =   VIN
# GND   =   GND
# MISO wird nicht benötigt


# SPI-BUS INIT
from machine import Pin, SPI
sck = Pin(18, Pin.OUT)
mosi = Pin(23, Pin.OUT)
miso = Pin(19, Pin.OUT)
spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

# Testing rfid module
# https://github.com/wendlers/micropython-mfrc522
from lib.rfid.mfrc522 import MFRC522
sda = Pin(5, Pin.OUT)

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


# Testing 8x8 LED-Display
# https://github.com/mcauser/micropython-max7219
from lib.display.max7219 import Matrix8x8
cs = Pin(2, Pin.OUT)
display = Matrix8x8(spi, cs, 4)
display.brightness(0)
display.fill(0)
display.text('Helo',0,0,1)
display.show()
sleep_ms(1000)
display.fill(1)
display.text('Helo',0,0,0)
display.show()



