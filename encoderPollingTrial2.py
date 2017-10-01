import RPi.GPIO as  GPIO
import time
import fcntl
import os
import sys

currentState = 0
previousState = 0
pin = 24
oldTime = 0
oldTimeWrite = 0
rpm = 0
#path = "/run/shm/rpm"
path = "/tmp/rpm2"
#path = "/home/pi/hiMan/MPU6050-Pi-Demo/temp2"
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)

while True:
	#print "we are still here"
	currentState = GPIO.input(pin)
	if(previousState != currentState):
		previousState = currentState
		if(currentState == 1):
			T = time.time()
			dt = T - oldTime
			rpm = 60/(dt*16)
			#rpm = 60/dt
			oldTime = T
			print rpm
			#f = open('/run/shm/rpm1.txt','w')
			#f.write(str(int(rpm)))
			#f.close()
	
	tWrite = time.time()
	dtWrite = tWrite - oldTimeWrite
	if dtWrite > 0.02:
		#print rpm
		oldTimeWrite = tWrite
		#print "opening the can"
		f = open(path,'w',os.O_WRONLY | os.O_NONBLOCK)
		f.write(str(int(rpm)))
		f.flush()
		f.close()
