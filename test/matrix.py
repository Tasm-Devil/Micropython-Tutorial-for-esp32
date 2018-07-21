from machine import Pin, SPI
from lib.display.max7219 import Matrix8x8
from time import sleep_ms

# SPI-BUS INIT
sck = Pin(18, Pin.OUT)
mosi = Pin(23, Pin.OUT)
miso = Pin(19, Pin.OUT)
cs = Pin(2, Pin.OUT)
spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

display = Matrix8x8(spi, cs, 4)
display.brightness(0)

display.fill(1)
display.text('Helo',0,0,0)
display.show()
sleep_ms(2000)

display.fill(0)
display.text('Helo',0,0,1)
display.show()
sleep_ms(2000)

display.fill(0)
display.rect(0,0,32,8,1)
display.show()


# 8x8-LED-Modul Anschlussplan für ESP32
# VCC   =   3.3V    (oder 5V)
# GND   =   GND
# DIN   =   GPIO 23 (MOSI)
# CS    =   GPIO 2
# CLK   =   GPIO 18 (CLK)

# Testing 8x8 LED-Display
# https://github.com/mcauser/micropython-max7219
