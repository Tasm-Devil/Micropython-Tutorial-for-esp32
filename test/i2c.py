from time import sleep_ms
from machine import I2C, Pin

# I2C-Bus init
bus = I2C(scl=Pin(22), sda=Pin(21))

# ssd1306 oled Display
# https://github.com/adafruit/micropython-adafruit-ssd1306
# ToDo: Watch this -> https://github.com/peterhinch/micropython-samples/tree/master/SSD1306
oled=None
try:
    from lib.display.ssd1306 import SSD1306_I2C
    oled = SSD1306_I2C(128, 64, bus)
    oled.text("Hello World", 10, 20)
    oled.show()
except OSError:
    print("No ssd1306 on I2C-Bus")
except ImportError:
    print("There is no ssd1306 driver in /lib/display/ssd1306.mpy")
except KeyboardInterrupt:
    print("Exiting ssd1306 test")


# Bosch bme280 Pres, Temp and Humidity Sensor
# Driver from: https://github.com/kevbu/micropython-bme280
bme = None
try:
    from lib.sensor.bme280 import BME280
    bme = BME280(i2c=bus)
    while True:
        temp = bme.temperature()
        pres = bme.pressure()
        hum  = bme.humidity()
        if oled:
            oled.fill(0)
            oled.text("Temp: " + "{:6.2f}".format(temp),10,0)
            oled.text("Pres: " + "{:6.2f}".format(pres),10,15)
            oled.text("Hum:  " + "{:6.2f}".format(hum), 10,30)
            oled.show()
        print("Temp: ", "{:6.2f}".format(temp), "Pres: ", "{:6.2f}".format(pres), "Hum:  ", "{:6.2f}".format(hum))
        sleep_ms(500)
except OSError:
    print("No bme280 on I2C-Bus")
except ImportError:
    print("There is no bme280 driver in /lib/sensor/bme280.mpy")
except KeyboardInterrupt:
    print("Exiting bme280 test")


# bh1750 light sensor
# https://github.com/PinkInk/upylib/tree/master/bh1750
lum=None
try:
    from lib.sensor.bh1750 import BH1750
    lum = BH1750(bus)
    while True:
        lumen = lum.luminance(BH1750.ONCE_HIRES_1)
        if oled:
            oled.fill(0)
            oled.text("Lumen: " + "{:5.0f}".format(lumen),10,0)
            oled.show()
        print("Lumen: " + "{:5.0f}".format(lumen))
        sleep_ms(500)
except OSError:
    print("No bh1750 on I2C-Bus")
except ImportError:
    print("There is no bh1750 driver in /lib/sensor/bh1750.mpy")
except KeyboardInterrupt:
    print("Exiting bh1750 test")


# adxl345 G-Force sensor
# http://andidinata.com/download/
adxl=None
try:
    from lib.sensor.adxl345 import ADXL345
    adxl = ADXL345(bus)
    while True:
        axes = adxl.sample(True)
        if oled:
            oled.fill(0)
            oled.text("x = " + "{:6.3f}".format(axes['x']),10,0)
            oled.text("y = " + "{:6.3f}".format(axes['y']),10,15)
            oled.text("z = " + "{:6.3f}".format(axes['z']),10,30)
            oled.show()
        print("x =", "{:6.3f}".format(axes['x']),
              " y =", "{:6.3f}".format(axes['y']),
              " z =", "{:6.3f}".format(axes['z']))
        sleep_ms(500)
except OSError:
    print("No adxl345 on I2C-Bus")
except ImportError:
    print("There is no adxl345 driver in /lib/sensor/adxl345.mpy")
except KeyboardInterrupt:
    print("Exiting adxl345 test")

# RGB-Color, Light, Proximity and Gesture sensor
# https://github.com/liske/python-apds9960
apds=None
try:
    from lib.sensor.apds9960 import uAPDS9960
    apds = uAPDS9960(bus)
    apds.enableLightSensor()
    while True:
        vala = apds.readAmbientLight()
        valr = apds.readRedLight()
        valg = apds.readGreenLight()
        valb = apds.readBlueLight()
        if oled:
            oled.fill(0)
            oled.text("ambi  = " + "{:5.0f}".format(vala) ,10,0) 
            oled.text("red   = " + "{:5.0f}".format(valr) ,10,15) 
            oled.text("green = " + "{:5.0f}".format(valg) ,10,30) 
            oled.text("blue  = " + "{:5.0f}".format(valb) ,10,45)
            oled.show()
        print("Ambient Light: " + "{:5.0f}".format(vala))
        print("Red Light: "     + "{:5.0f}".format(valr))
        print("Green Light: "   + "{:5.0f}".format(valg))
        print("Blue Light: "    + "{:5.0f}".format(valb))
        sleep_ms(500)
except OSError:
    print("No apds9960 on I2C-Bus")
except ImportError:
    print("There is no apds9960 driver in /lib/sensor/adxl345.mpy")
except KeyboardInterrupt:
    print("Exiting apds9960 test")

# ToDo Add Proximity and gesture test here
