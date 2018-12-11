import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sensor = 23

GPIO.setup(sensor, GPIO.IN)


print "Waiting for sensor to settle"
time.sleep(2)
while True:
	if GPIO.input(sensor):
        import sucOrFail
		time.sleep(2)

	time.sleep(2)
	break

GPIO.cleanup()
