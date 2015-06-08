import RPi.GPIO as GPIO
import time

number_of_tics = 10

start_time = time.time()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)


i = 0
for i in range(number_of_tics):
    total = 0
    while GPIO.input(4) == 1:
        while GPIO.input(4) == 0:
	    total = total + 1
	    print total
	    i = i + 1
    elapsed_time = time.time() - start_time
			
print "measured"
print elapsed_time


"""count = 0 for i in 
range(0,1000):
  print GPIO.input(4)
  time.sleep(0.01)
  if (GPIO.input(4)) > 4:
    count = count + 1

print("---%s led flashes---" % count)
print("---%s seconds ---" % (time.time() . star_time)) """
