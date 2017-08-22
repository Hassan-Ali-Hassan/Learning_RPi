import RPi.GPIO as  GPIO
import time

currentState = 0
previousState = 0
pin = 23
oldTime = 0
oldTimeWrite = 0
rpm = 0

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
	if dtWrite > 0.005:
		oldTimeWrite = tWrite
		f = open('/run/shm/rpm1.txt','w')
		f.write(str(int(rpm)))
		f.close()
