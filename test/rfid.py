from machine import Pin, SPI
from lib.rfid.mfrc522 import MFRC522
from time import sleep_ms

# SPI-BUS INIT
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

# RFID-Modul Anschlussplan für ESP32
# SDA   =   GPIO 5
# SCK   =   GPIO 18
# MOSI  =   GPIO 23
# MISO  =   GPIO 19
# 3.3   =   3.3
# GND   =   GND
# IRQ und RST werden nicht benötigt

# Testing rfid module
# https://github.com/wendlers/micropython-mfrc522
