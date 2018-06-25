from time import sleep
from machine import Pin, I2C
from lib.sensor.apds9960 import uAPDS9960

# https://github.com/liske/python-apds9960

bus = I2C(scl=Pin(22), sda=Pin(21))
apds = uAPDS9960(bus)

apds.setProximityIntLowThreshold(50)

print("Proximity Sensor Test")
print("=====================")
apds.enableProximitySensor()

oval = -1
while True:
    sleep(0.25)
    val = apds.readProximity()
    if val != oval:
        print("proximity={}".format(val))
        oval = val

