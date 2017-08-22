import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
inPin = 23
outPin = 24
GPIO.setup(inPin,GPIO.IN)
GPIO.setup(outPin,GPIO.OUT)
status = 0
counter = 0
oldTime = 0
a = "0"
b = "0"
def myCallback(channel):
	global counter
	global status
	global oldTime
	T = time.time()
	dt = T - oldTime
	oldTime = T
	speed = 60/(dt*20)
	counter = counter + 1
	status = ~status
	print "the counter value is  "
	print speed 
	GPIO.output(outPin,status)


GPIO.add_event_detect(inPin,GPIO.FALLING,callback=myCallback,bouncetime=1)


while True:
	f = open("/run/shm/yaw.txt","r")
	a = f.read()
	f.close()
	if not a:
		print b
	else:
		print a		
		b = a	 
	time.sleep(0.5)

