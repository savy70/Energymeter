import RPi.GPIO as GPIO
import time

#Define settings
number_of_tics = 20
read_interval = 0.01
start_time = time.time()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

#Define the read function
def read_data(n,read_interval):
    total = 0
    previous_state = 0
    current_state = 0
    for i in range(n):
        total = total + 1
	print total
        time.sleep(read_interval)
	while current_state !=  previous_state:  
		if current_state == 0:
			time.sleep(read_interval)
			if GPIO.input(4) == 1:
				current_state = 1;
		
		if current_state == 1:
			time.sleep(read_interval)	
			if GPIO.input(4) == 0:
				current_state = 0;
 
	while previous_state == current_state:
		time.sleep(read_interval)
       		if GPIO.input(4) != current_state:
			current_state = GPIO.input(4)
			
			
print "time consumed:" 
elapsed_time = time.time() - start_time
print elapsed_time
read_data(number_of_tics,read_interval)
