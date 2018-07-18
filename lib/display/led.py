from machine import Pin, PWM
import time
import math

class LED ():
    isPWMinit = False
    
    def __init__ (self, pin):
        self.pin = pin
        self.led = Pin(self.pin, Pin.OUT)
        self.led.value(1)
    
    def deinit(self):
        if self.isPWMinit:
            self.led.deinit()
            self.isPWMinit = False
            self.led = Pin(self.pin, Pin.OUT)
            self.led.value(1)
    
    def duty(self, dc):
        if self.isPWMinit:
            self.led.duty(dc)
        else:
            self.led = PWM(Pin(self.pin), freq=1000)
            self.led.init()
            self.isPWMinit = True
            self.led.duty(dc)
    
    def fade_down(self, t):
        for i in range(100):
            self.duty(int(math.sin((i-50) / 100 * math.pi) * 512 + 512))
            time.sleep_ms(t)
    
    def fade_up(self, t):
        for i in range(100):
            self.duty(int(math.sin((i+50) / 100 * math.pi) * 512 + 511))
            time.sleep_ms(t)
    
    def pulse(self, t):
        self.fade_up(t)
        self.fade_down(t)
    
    def on(self):
        self.deinit()
        self.led.value(0)
    
    def off(self):
        self.deinit()
        self.led.value(1)
    
    def toggle(self):
        self.deinit()
        self.led.value((self.led.value() + 1) % 2)
    
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

