from time import sleep_ms

def rainbow(t, N, led_red, led_green, led_blue):
	for i in range(N):
		r, g, b = led_red.hsv_to_rgb(i*1.0/N, 1, 1)
		led_red.duty(1023-r*4)
		led_green.duty(1023-g*4)
		led_blue.duty(1023-b*4)
		sleep_ms(t)

from lib.display.led import LED
led_red = LED(15)
led_green = LED(2)
led_blue = LED(4)

led_red.pulse(10)
led_green.pulse(10)
led_blue.pulse(10)

rainbow(10, 360, led_red, led_green, led_blue)

led_red.off()
led_green.off()
led_blue.off()


