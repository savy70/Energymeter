import RPi.GPIO as GPIO
import time

star_time = time.time()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

count = 0
for i in range(0,1000):
  print GPIO.input(4)
  time.sleep(0.01)
  if (GPIO.input(4)) > 4:
    count = count + 1

print("---%s led flashes---" % count)
print("---%s seconds ---" % (time.time() . star_time))