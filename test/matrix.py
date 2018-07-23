from machine import Pin, SPI
from lib.display.max7219 import Matrix8x8
from time import sleep_ms

# Initialisiere den SPI-Bus
sck = Pin(18, Pin.OUT)
mosi = Pin(23, Pin.OUT)
miso = Pin(19, Pin.IN)
cs = Pin(2, Pin.OUT)
spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

display = Matrix8x8(spi, cs, 4)
display.brightness(0)

display.fill(1)
display.text('Halo',0,0,0)
display.show()
sleep_ms(2000)

display.fill(0)
display.text('Welt',0,0,1)
display.show()
sleep_ms(2000)

display.fill(0)
display.rect(0,0,32,8,1)
display.show()
