from time import sleep_ms
from machine import I2C, Pin

# I2C-Bus init
bus = I2C(scl=Pin(22), sda=Pin(21))

# ssd1306 oled Display
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

