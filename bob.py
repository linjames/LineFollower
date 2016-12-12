#!/usr/bin/python3

import math as Math
from wheel import Wheel
from sensor import Sensor
from time import sleep

class Robot:
  lw = None
  rw = None
  maxSpeed = 4
  sensor = None
  
  def __init__(self, maxSpeed=4, lwComp=0, rwComp=0):
    self.lw = Wheel("XIO-P1", "XIO-P0", 50, lwComp)
    self.rw = Wheel("XIO-P3", "XIO-P2", 50, rwComp)
    self.maxSpeed = maxSpeed
    self.sensor = Sensor(0x09, 2)

  def run(self):
    while True:
      reading = self.sensor.getReading()
      print(reading)
      if Math.isnan(reading):
        reading = 0
      self.bob(reading)
      sleep(0.05)

  def bob(self,stuart):
    lwSpeed = self.maxSpeed
    rwSpeed = self.maxSpeed
    if stuart<0:
      lwSpeed = self.maxSpeed*(1 + stuart/3.5)
    elif stuart>0:
      rwSpeed = self.maxSpeed*(1 - stuart/3.5)

    self.lw.setSpeed(lwSpeed)
    self.rw.setSpeed(rwSpeed)
    print('lwSpeed: ' + str(lwSpeed))
    print('rwSpeed: ' + str(rwSpeed))

if __name__ == "__main__":
  robot = Robot(1, 0, 5)
  robot.run();
        

