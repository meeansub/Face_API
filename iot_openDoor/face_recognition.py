# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os
import json
from collections import OrderedDict
import datetime
import sys
import RPi.GPIO as GPIO
import time

newCode="sudo modprobe bcm2835-v4l2"
os.system(newCode)

GPIO.setmode(GPIO.BCM)

# 각 숫자는 라즈베리 파이의 숫자를 의미한다.
#pin 23은 감지 센서, pin20은 성공했을 때의 LED불 pin 21은 실패했을 때의 LED불
sensor = 23
Sled = 20
Fled = 21

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(Sled, GPIO.OUT)
GPIO.setup(Fled, GPIO.OUT)

# 얼굴인식 값 json 파일 변수, 이름, 날짜(시간포함)
file_data = OrderedDict()
face_name="unkown"

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

# Save the captured image into 출입 실패시(얼굴인식 실패시)
def failCap():
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imwrite("successCap/unkwon.png", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
        return  True
                


time.sleep(2)
print ("센서 작동중")


#얼굴 id 값 초기화, 초기 None
id = 0

# 얼굴 트레이너 불러오기
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

# id에 맞는 이름 출력을 위해
names = ['None', 'minsub', 'jihoon', 'hosic', 'taehoon', 'jieun']

# 얼굴인식 서비스 사용을 위한 카메라 사이즈 설정 및 시작
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# 얼굴인식된 부분만 자른다.
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

time.sleep(4)

while True:
    state=False
    count=0
    if GPIO.input(sensor):
        print ("움직임이 감지되었습니다")
        print ("얼굴을 인식합니다")
        while True:
            # 얼굴 인식전 상태
            face_recog_state = False
            fail_state=False
            
            #카메라에 비춰진 상황 읽기
            ret, img =cam.read()
            img = cv2.flip(img, 1)

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

                #얼굴인식 퍼센트 100센트까지
                if (confidence < 100):
                    id = names[id]
                    confidence = "  {0}".format(round(100 - confidence))

                    # 얼굴인식 일치 정도가 50% 이상일때
                    if (int(confidence) > 50):

                        # 출입성공시 출입로그 json 저장
                        create_json(id)

                        # 출입성공시 캡쳐, 얼굴인식상태 true
                        face_recog_state=successCap(id)

                        face_name=id
                        GPIO.output(Sled, True)
                        print("얼굴인식이 되었습니다. 문이 열립니다")
                        time.sleep(2)
                    

                else:
                    id = "unknown"
                    confidence = "  {0}".format(round(100 - confidence))                 
                    print("얼굴인식에 실패했습니다")
                    count=count+1
                    print(count)
                    if count==5:
                        GPIO.output(Fled, True)
                        fail_state=True
                        face_recog_state=True
                        
                    
                    break

                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
                
            cv2.imshow('camera',img)

            if face_recog_state == True:
                time.sleep(4)
                GPIO.output(Sled, False)
                GPIO.output(Fled, False)
                state=True
                
                break

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                state=True
                break
                
    if state == True:
        break




# Do a bit of cleanup
print("\n[INFO]얼굴인식 종료")
cam.release()
cv2.destroyAllWindows()
GPIO.cleanup()
