import face_recognition
from face_recog import FaceRecog
import camera
import cv2
import os
import datetime
import time
import numpy as np
#import Picamera
import json
from collections import OrderedDict


path = os.getcwd()
full_path = path +'/capture_Face'
file_Name = datetime.datetime.now().strftime("%y%m%d_%H%M%S")


if __name__ == '__main__':
    face_recog = FaceRecog()
    print(face_recog.known_face_names)
    group_Data = OrderedDict()


    while True:
        try :
            frame = face_recog.get_frame()['return0']
            # show the frame
            cv2.imshow("Frame", frame)
            similarity = face_recog.get_frame()['return1']

        except similarity as sim :
            sim == 0

        else:
            if similarity > 0.6 :
            # if the `q` key was pressed, break from the loop
                cv2.imwrite(os.path.join(full_path +'/fail', file_Name + '.jpg' ), frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
                print(file_Name)
                print('Failed')
                group_Data["name"] = "Unknown"
                group_Data["time"] = file_Name
                break
            else :
                cv2.imwrite(os.path.join(full_path +'/success', file_Name + '.jpg' ), frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
                print(file_Name)
                print('Success')
                group_Data["name"] = face_recog.known_face_names
                group_Data["time"] = file_Name
                break

    with open('log/log_'+ file_Name +'.json', 'w') as make_file:
        json.dump(group_Data, make_file)
        #print(json.dump(group_Data, make_file, ensure_ascii=False, indent="\t") )

    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')
