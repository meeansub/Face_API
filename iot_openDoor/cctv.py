import picamera
import time
import datetime

with picamera.picamera() as camera:
    camera.resolution = (640, 480)
    now = datetime.datetime.now()
    filename = now.strftime('%Y-%m-%d %H:%M:%S')
    camera.start_recording(output = filename + '.h264')
    camera.wait_recording(5)
    camera.stop_recording()
