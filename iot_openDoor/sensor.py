import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

sensor = 23
Sled = 20
Fled = 21

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(Sled, GPIO.OUT)
GPIO.setup(Fled, GPIO.OUT)

print ("Waiting for sensor to settle")
time.sleep(2)
print ("Detecting motion")

while True:
	if GPIO.input(sensor):
		print ("Motion Detected")
		GPIO.output(Sled, True)
		time.sleep(2)
	GPIO.output(Fled, False)
	time.sleep(2)


print ("Open Door")

GPIO.cleanup()
