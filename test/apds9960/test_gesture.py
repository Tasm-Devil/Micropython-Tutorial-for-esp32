from time import sleep
from machine import Pin, I2C
from lib.sensor.apds9960 import uAPDS9960

# https://github.com/liske/python-apds9960

bus = I2C(scl=Pin(22), sda=Pin(21))
apds = uAPDS9960(bus)

dirs = {
    0: "none",
    1: "left",
    2: "right",
    3: "up",
    4: "down",
    5: "near",
    6: "far",
}

apds.setProximityIntLowThreshold(50)

print("Gesture Test")
print("============")
apds.enableGestureSensor()

while True:
    sleep(0.5)
    if apds.isGestureAvailable():
        motion = apds.readGesture()
        print("Gesture={}".format(dirs.get(motion, "unknown")))

