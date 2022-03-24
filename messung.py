import lm75
import time
from gpiozero import RGBLED
from colorzero import color

rgb = RGBLED(21,20,26)

class RGB(object):
  def init(self, rgb):
    self.r = 0
    self.g = 0
    self.b = 0
    self.a = 0
    self.f = 0

  def update(self):
    while True:
      sensor = lm75.LM75()
      time.sleep(1)
      self.a = float(sensor.getTemp())
      print (self.a)
      rgb.color = (self.r, self.g, self.b)
      self.f = self.a -70
      self.rot()
      self.blau()
      self.gruen()

  def rot(self):
    if self.f >= 11:
      if self.f <= 10:
        self.r = ((self.f - 10) / 10)
      else:
        self.r = 1
    else:
      self.r = 0

  def blau(self):
    if self.f >= 0:
      if self.f <= 9:
        self.b = (1 - (self.f / 10))
      else:
        self.b = 0
    else:
      self.b = 1

  def gruen(self):
    if self.f == 10:
      self.g = 0,5
    elif self.f > 10:
      if self.f < 17:
        self.g = (1 - (self.f / 17))
      else:
        self.g = 0
    elif self.f < 10:
      if self.f > 3:
        self.g = (self.f / 17)
      else:
        self.g = 0
    else:
      self.g = 0

LED = RGB(0)
LED.update()