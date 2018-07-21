from lib.display.led import LED, RGB_LED

led_red = LED(15)
led_green = LED(4)
led_blue = LED(16)

led_red.pulse(10)
led_green.pulse(10)
led_blue.pulse(10)

rgb = RGB_LED(led_red, led_green, led_blue)
rgb.rainbow()

led_red.off()
led_green.off()
led_blue.off()
