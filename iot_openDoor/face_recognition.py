
import cv2
import numpy as np
import os
import json
from collections import OrderedDict
import datetime
import sys

newCode="sudo modprobe bcm2835-v4l2"
os.system(newCode)

# 얼굴인식 값 json 파일 변수, 이름, 날짜(시간포함)
file_data = OrderedDict()

# Save the captured image into 출입 성공 시(얼굴인식 성공시)
def successCap(id):
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                cv2.imwrite("successCap/"+ id + ".png", gray[y:y+h,x:x+w])
                cv2.imshow('image', img)
                return  True
                
# 출입성공시 출입로그 json 저장
def create_json(id):
                # 출입로그에 저장할 값: 이름, 현재시간
                file_data["name"] = id
                file_data["dateTime"] =datetime.datetime.now().strftime("%Y-%m-%d//%H:%M:%S")
                print(json.dumps(file_data))
                
                # 출입로그 save
                with open('result/' + id + '.json', 'w') as make_file:
                    json.dump(file_data, make_file)
    
# 얼굴 트레이너 불러오기
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'minsub', 'jihun', 'hosic', 'taehoon', 'jieun']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    # 얼굴 인식전 상태
    face_recog_state = False

    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}".format(round(100 - confidence))

            # 얼굴인식 일치 정도가 60% 이상일때
            if (int(confidence) > 70):

                # 출입성공시 출입로그 json 저장
                create_json(id)
                
                # 출입성공시 캡쳐, 얼굴인식상태 true
                face_recog_state=successCap(id)

                print("얼굴인식이 되었습니다. 문이 열립니다.")
                

        else:
            id = "unknown"
            confidence = "  {0}".format(round(100 - confidence))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)


    cv2.imshow('camera',img)

    # if r == 20:
    #     break

    if face_recog_state == True:
        break

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break




# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
