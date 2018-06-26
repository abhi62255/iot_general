import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.IN)

GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(22,0)

while 1:
	if GPIO.input(24)==0 :
		GPIO.output(17,0)
		GPIO.output(27,1)
		GPIO.output(22,0)
		print "button presss power low"
	else:
		GPIO.output(17,1)
		GPIO.output(27,0)
		GPIO.output(22,1)
		print "lbutton relese power high "
	time.sleep(0.3)		
