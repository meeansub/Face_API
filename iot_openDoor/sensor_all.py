#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sensor = 23



print ("Waiting for sensor to settle")
time.sleep(2)
while True:
	GPIO.setup(sensor, GPIO.IN)

	if GPIO.input(sensor):
		import sucOrFail
		time.sleep(2)
		break
		
	

	
	


