from lib.display.led import LED
from time import sleep_ms

led_red = LED(15)
led_green = LED(2)
led_blue = LED(4)

for x in range(3):
    led_red.on()
    sleep_ms(500)
    led_red.off()
    sleep_ms(500)
