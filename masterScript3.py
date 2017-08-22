import time
import RPi.GPIO as GPIO

a = "0"
b = "0"


while True:
	f = open("/run/shm/yaw.txt","r")
	a = f.read()
	f.close()
	
	f = open("/run/shm/rpm1.txt","r")
	b = f.read()
	f.close()
	
	print ("yaw and rpm are: %s \t %s"%(a,b))	 
	time.sleep(0.05)

