import RPi.GPIO as GPIO
import time

#Define settings
number_of_tics = 50
read_interval = 0.005
#start_time = time.time()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

#Define consumption function for electricity
def elec_cost(time_s, number_of_tics):
   unit_price = 0.115 
   consumed_time_h = 3600/time_s
   kokonaiskulutus = number_of_tics * consumed_time_h *24*365/10000
   total_price = unit_price * kokonaiskulutus				 
   return total_price, kokonaiskulutus

#Define the read function
def read_data(n,read_interval):
    total = 0
    start_time = time.time()
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

    return  time.time() - start_time			
			

elapsed_time = read_data(number_of_tics,read_interval)
print
print "Time consumed:", elapsed_time, "seconds"
print
print "euros consumed per year: %f2 and kWh consumed %f2" % elec_cost(elapsed_time, number_of_tics) 

