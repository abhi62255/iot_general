import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

try:
	while True :
		GPIO.output(17,0)
		GPIO.output(27,0)
		GPIO.output(22,0)
		time.sleep(0.3)
		GPIO.output(17,1)
		GPIO.output(27,0)
		GPIO.output(22,0)
		time.sleep(0.3)
		GPIO.output(17,0)
		GPIO.output(27,1)
		GPIO.output(22,0)
		time.sleep(0.3)
		GPIO.output(17,0)
		GPIO.output(27,0)
		GPIO.output(22,1)
		time.sleep(0.3)
except KeyboardInterrupt :
	print 'hello'