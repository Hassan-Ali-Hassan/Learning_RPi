import RPi.GPIO as  GPIO
import time
import fcntl
import os
import sys

currentState = 0
previousState = 0
pin = 23
oldTime = 0
oldTimeWrite = 0
rpm = 0
path = "/run/shm/tempo2"

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)

while True:
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
		oldTimeWrite = tWrite
		f = open(path,'w',0)
		f.write(str(int(rpm)))
		f.flush()
		f.close()
