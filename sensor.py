#!/usr/bin/python3

from i2cdev import I2C
from time import sleep
from numpy import std,mean,abs

class Sensor:
  i2c = None

  def __init__(self, addr, bus):
    self.i2c = I2C(addr, bus)

  def getRawReading(self):
    return self.i2c.read(16)[::2] 

  def getReading(self):
    raw = self.getRawReading()
    val = [int(x) for x in raw]
    outlier = [abs(mean(val)-x)>2*std(val) for x in val]
    index = [x+1 for x in list(range(0, len(outlier)))]
    return (sum([a*b for a,b in zip(outlier,list(range(1,9)))])/sum(outlier)-4.5)*2

  def getReading2(self):
    raw = self.getRawReading()
    val = [int(x) for x in raw]
    outlier = [max(val)-x>20 for x in val]
    index = [x+1 for x in list(range(0, len(outlier)))]
    return (sum([a*b for a,b in zip(outlier,list(range(1,9)))])/max(1,sum(outlier))-4.5)*2


if __name__ == "__main__":
  sensor = Sensor(0x09, 2)
  try:
    while True:
      value = sensor.getRawReading()
      for i in range(0, 8):
        print(value[i],end=' ')
      print(sensor.getReading2())
      sleep(1)
  except KeyboardInterrupt:
    pass



