import time

a = "0"
b = "0"


while True:
	f = open("/run/shm/yaw.txt","r")
	a = f.read()
	f.close()
	if not a:
		print b
	else:
		print a		
		b = a	 
	time.sleep(0.01)
