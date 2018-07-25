from machine import Pin, PWM
from time import sleep_ms
from math import sin, pi, exp
#from math import log, pow, log10

class LED ():
    isPWMinit = False
    
    def __init__ (self, pin, freq=1000):
        self.pin = pin
        self.freq = freq
        self.led = Pin(self.pin, Pin.OUT)
        #self.pwmIntervals = 255
        #self.R = self.pwmIntervals /log(1023)            #R = 36.79391
    
    def deinit(self):
        if self.isPWMinit:
            self.led.deinit()
            self.isPWMinit = False
            self.led = Pin(self.pin, Pin.OUT)
            self.led.value(1)
    
    def brightness(self, value=None):
        if value == None:
            if self.isPWMinit:
                return (self.led.duty() >> 2)
            else:
                return self.led.value()
        elif not 0 <= value <= 255:
            raise ValueError("Brightness out of range")
        else:
            if not self.isPWMinit:
                self.led = PWM(Pin(self.pin), self.freq)
                self.led.init()
                self.isPWMinit = True
            self.led.duty(value << 2)
            
            # Next Line was inspired by
            # https://diarmuid.ie/blog/pwm-exponential-led-fading-on-arduino-or-other-platforms/
            # but i dropped it because it doesn't look better than linear fading for me.
            #self.led.duty(int(exp(   (value / 36.79391)) - 1))
            # Next Line was inspired by this post:
            # https://electronics.stackexchange.com/a/11100
            # but it looked even worse
            #self.led.duty(int(1 / (1 + exp( ((value / 21) -6) * -1)) * 1024))
    
    def fade_up(self, delay=5):
        for i in range(100):
            self.brightness(int(sin((i-50) / 100 * pi) * 128 + 128))
            sleep_ms(delay)
    
    def fade_down(self, delay=5):
        for i in range(100):
            self.brightness(int(sin((i+50) / 100 * pi) * 128 + 127))
            sleep_ms(delay)
    
    def pulse(self, delay=5):
        self.fade_up(delay)
        self.fade_down(delay)
    
    def on(self):
        self.deinit()
        self.led.value(1)
    
    def off(self):
        self.deinit()
        self.led.value(0)
    
    def toggle(self):
        self.deinit()
        self.led.value((self.led.value() + 1) % 2)

class LED_a ():
    isPWMinit = False
    
    def __init__ (self, pin, freq=1000):
        self.pin = pin
        self.freq = freq
        self.led = Pin(self.pin, Pin.OUT)
        self.led.value(1)
    
    def deinit(self):
        if self.isPWMinit:
            self.led.deinit()
            self.isPWMinit = False
            self.led = Pin(self.pin, Pin.OUT)
            self.led.value(1)
    
    def brightness(self, value=None):
        if value == None:
            if self.isPWMinit:
                return 255 - (self.led.duty() >> 2)
            else:
                return (self.led.value() + 1) % 2
        elif value >= 255:
            value = 255
            self.on()
        elif value <= 0:
            value = 0
            self.off()
        else:
            if not self.isPWMinit:
                self.led = PWM(Pin(self.pin),self.freq)
                self.led.init()
                self.isPWMinit = True
            self.led.duty(((256-value) << 2) - 1)
    
    def fade_up(self, delay=5):
        # pwmIntervals = 100
        # R = (pwmIntervals * math.log10(2))/(math.log10(255));
        # for i in range(pwmIntervals):
            # led_red.brightness(int(math.pow(2, (i / R)) - 1))
            # time.sleep_ms(t)
        for i in range(100):
            self.brightness(int(sin((i-50) / 100 * pi) * 128 + 128))
            sleep_ms(delay)
    
    def fade_down(self, delay=5):
        for i in range(100):
            self.brightness(int(sin((i+50) / 100 * pi) * 128 + 127))
            sleep_ms(delay)
    
    def on(self):
        self.deinit()
        self.led.value(0)
    
    def off(self):
        self.deinit()
        self.led.value(1)
    
    def toggle(self):
        self.deinit()
        self.led.value((self.led.value() + 1) % 2)

class RGB_LED ():
    
    def __init__ (self, led_red, led_green, led_blue):
        self.led_red = led_red
        self.led_green = led_green
        self.led_blue = led_blue
    
    def hsv_to_rgb(self, h, s, v):
        """
        Convert HSV to RGB (based on colorsys.py).
        
            Args:
                h (float): Hue 0 to 1.
                s (float): Saturation 0 to 1.
                v (float): Value 0 to 1 (Brightness).
        """
        if s == 0.0:
            return v, v, v
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6

        v = int(v * 255)
        t = int(t * 255)
        p = int(p * 255)
        q = int(q * 255)

        if i == 0:
            return v, t, p
        if i == 1:
            return q, v, p
        if i == 2:
            return p, v, t
        if i == 3:
            return p, q, v
        if i == 4:
            return t, p, v
        if i == 5:
            return v, p, q
    
    def rainbow(self, t=10):
        for i in range(360):
            r, g, b = self.hsv_to_rgb(i*1.0/360, 1, 1)
            self.led_red.brightness(r)
            self.led_green.brightness(g)
            self.led_blue.brightness(b)
            sleep_ms(t)
