from time import sleep
from machine import Pin, I2C
from lib.sensor.apds9960 import uAPDS9960

# https://github.com/liske/python-apds9960

bus = I2C(scl=Pin(22), sda=Pin(21))
apds = uAPDS9960(bus)

print("Light Sensor Test")
print("=================")
apds.enableLightSensor()

oval = -1
while True:
    sleep(0.25)
    vala = apds.readAmbientLight()
    valr = apds.readRedLight()
    valg = apds.readGreenLight()
    valb = apds.readBlueLight()
    print("Ambient Light={}".format(vala))
    print("Red Light={}".format(valr))
    print("Green Light={}".format(valg))
    print("Blue Light={}".format(valb))

