import cv2
import time
import os
import datetime

path = 'cctv/'

class Camera_cctv():
    camera = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object to save the video
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

    video_writer = cv2.VideoWriter( 'output.mp4', fourcc, 30.0, (640, 480))


    while True:

        (grabbed, frame) = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640,480))
        cv2.imshow("Frame", frame)  # show the frame to our screen
        key = cv2.waitKey(33) & 0xFF
        video_writer.write(frame)  # Write the video to the file system

         # I don't really have an idea what this does, but it works..
        if key == 27:
             break

    # cleanup the camera and close any open windows
    camera.release()
    video_writer.release()
    cv2.destroyAllWindows()
    print("\n\nBye bye\n")
