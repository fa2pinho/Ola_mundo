from machine import Pin
import time

led1 = Pin (22, Pin.OUT)
led2 = Pin (23, Pin.OUT)
led3 = Pin (21, Pin.OUT)
timer=4
led1.off()
led2.off()
led3.off()
time.sleep(1)

while True:
  led1.on ()
  time.sleep(timer)
  led1.off()
  led2.on()
  time.sleep(timer)
  led2.off()
  led3.on()
  time.sleep(timer)
  led3.off()
  timer=timer-0.5
  print = "timer"
