from machine import Pin, ADC
from time import sleep_ms
from lib.display.led import LED, RGB_LED

led = LED(2)

adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_9BIT)
try:
    while True:
        value = adc.read() // 2
        led.brightness(value)
        print(value)
        sleep_ms(50)
except KeyboardInterrupt:
    led.off()
    print("Bye")

