import RPi.GPIO as GPIO
import time

#Define settings
number_of_tics = 10
start_time = time.time()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

#Define the read function
def read_data(n):
    total = 0
    previous_state = 0
    current_state = 0
    for i in range(n):
        total = total + 1
	print total
        
	while current_state !=  previous_state:  
		if current_state == 0:
			if GPIO.input(4) == 1:
				
		if GPIO.input(4) == 0:
			current_state = 0
 
	while previous_state == current_state:
       		
		if GPIO.input(4) == 0:
			
			current_state = 0
			
			
print "time consumed:" 
elapsed_time = time.time() - start_time
print elapsed_time
read_data(number_of_tics)
