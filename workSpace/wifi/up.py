import network
from time import sleep_ms
from machine import I2C, Pin

# I2C-Bus init
bus = I2C(scl=Pin(22), sda=Pin(21))

SSID, PASSWORD = "ssid", "password"

oled=None
try:
    from lib.display.ssd1306 import SSD1306_I2C
    oled = SSD1306_I2C(128, 64, bus)
except OSError:
    print("No ssd1306 on I2C-Bus")
except ImportError:
    print("There is no ssd1306 driver in /lib/display/ssd1306.mpy")
except KeyboardInterrupt:
    print("Exiting wifi setup")


sta_if = network.WLAN(network.STA_IF)
counter = 0

while not sta_if.isconnected() and counter < 10:
    if oled:
        oled.fill(0)
        oled.text('Connecting to', 0, 25)
        oled.text(SSID, 0, 40)
        oled.show()
    sta_if.active(True)
    sta_if.connect(SSID, PASSWORD)
    sleep_ms(1000)
    counter += 1

if sta_if.isconnected():
    if oled:
        oled.fill(0)
        oled.text('Connected to', 0, 15)
        oled.text(SSID, 0, 30)
        oled.text('IP:' + sta_if.ifconfig()[0], 0, 45) 
        oled.show()
else:
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(False)
    if oled:
        oled.fill(0)
        oled.text('Cannot con to', 0, 25)
        oled.text(SSID, 0, 40)
        oled.show()
