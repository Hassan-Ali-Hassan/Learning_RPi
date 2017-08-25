import time
import RPi.GPIO as GPIO
import fcntl

a = "0"
b = "0"
path_yaw = "/run/shm/yaw.txt"

while True:
	f = open(path_yaw,"r")
	fcntl.flock(f,fcntl.LOCK_EX)
	a = f.read()
	#fcntl.flock(f,LOCK_UN)
	f.close()
	
	f2 = open("/run/shm/rpm1.txt","r")
	fcntl.flock(f2,fcntl.LOCK_EX)
	b = f2.read()
	f2.close()
	
	print ("yaw and rpm are: %s \t %s"%(a,b))	 
	time.sleep(0.05)

