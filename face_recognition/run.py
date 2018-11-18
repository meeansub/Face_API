import face_recognition
from face_recog import FaceRecog
import camera
import cv2
import os
import datetime
import time
import numpy as np

path = os.getcwd()
full_path = path +'/capture_Face'
name = datetime.datetime.now().strftime("%y%m%d_%H%M%S")


if __name__ == '__main__':
    face_recog = FaceRecog()
    print(face_recog.known_face_names)
    while True:
        frame = face_recog.get_frame()['return0']

        # show the frame
        cv2.imshow("Frame", frame)
        print(face_recog.get_frame()['return1'])
        if face_recog.get_frame()['return1'] > 0.6 :
        # if the `q` key was pressed, break from the loop
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                cv2.imwrite(os.path.join(full_path +'/fail', name + '.jpg' ), frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
                print(name)
                break
        else :
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                cv2.imwrite(os.path.join(full_path +'/success', name + '.jpg' ), frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
                print(name)
                break


    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')
