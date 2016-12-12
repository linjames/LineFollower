#!/usr/bin/python3

import CHIP_IO.SOFTPWM as SPWM
import sys
from math import fabs
from time import sleep

class Wheel:   
  pinA = None
  pinB = None
  speed = 0
  freq = 50
  comp = 0

  def __init__(self, pinA, pinB, freq=50,comp=0):
    self.pinA = pinA
    self.pinB = pinB
    self.freq = freq
    self.comp = comp
    SPWM.start(pinA, 0)
    SPWM.start(pinB, 0)
    SPWM.set_frequency(pinA, freq)
    SPWM.set_frequency(pinB, freq)

  def setSpeed(self, speed):
    self.speed = speed
    pinA_DC = 0
    pinB_DC = 0
    DC = fabs(speed)*10+20+self.comp
    if speed>0:
       pinA_DC = DC
    elif speed<0:
       pinB_DC = DC

    SPWM.set_duty_cycle(self.pinA, pinA_DC)
    SPWM.set_duty_cycle(self.pinB, pinB_DC)

  def setFreq(self, freq):
    self.freq = freq
    SPWM.set_frequency(self.pinA, freq)
    SPWM.set_frequency(self.pinA, freq)

  def __del__(self):
    SPWM.stop(self.pinA)
    SPWM.stop(self.pinB)
    SPWM.cleanup()

if __name__ == "__main__":
  lw = Wheel("XIO-P1", "XIO-P0", 50, 0)
  rw = Wheel("XIO-P3", "XIO-P2", 50, 10)

  lw.setSpeed(int(sys.argv[1]))
  rw.setSpeed(int(sys.argv[2]))
  sleep(5)
  lw.setSpeed(0)
  rw.setSpeed(0)


    


