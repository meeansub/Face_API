# -*- coding: utf-8 -*-
import cv2
import datetime
import time
import os
import face_recognition


CAM_ID = 0
path = os.getcwd()  #경로따오
full_path=path + '/Save'        #사진 찍히면 저장되는 폴더경
name = datetime.datetime.now().strftime("%y%m%d_%H%M%S") #시간스탬//


def capture(camid = CAM_ID):

    cam = cv2.VideoCapture(camid)
    if cam.isOpened() == False:
        print ('cant open the cam (%d)' % camid)
        return None

    cv2.namedWindow('Face')

    face_cascade = cv2.CascadeClassifier()
    face_cascade.load('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

    while(True):
        ret, frame = cam.read()

        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grayframe = cv2.equalizeHist(grayframe)

        if frame is None:
            print ('frame is not exist')
            return None

        faces = face_cascade.detectMultiScale(grayframe, 1.1, 3, 0, (30, 30))

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3, 4, 0)

        cv2.imshow('Face',frame)
        time.sleep(3)
        # png로 압축 없이 영상 저장t= time.localtime()
        #사진 저장 하는 라이브러리
        cv2.imwrite(os.path.join(full_path, name + '.jpg' ), frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
        #cv2.imwrite(name+'.jpg',frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
        print(name)
        time.sleep(1)
        cam.release()
        cv2.destroyWindow('Face')
        break;

def featureMatching():
    img1 = cv2.imread(path+'/face_save/test123.jpg',0)
    img2 = cv2.imread(path+'/Save/'+name+'.jpg',0)
    res = None

    sift = cv2.xfeatures2d.SIFT_create()
    kb1, des1 = sift.detectAndCompute(img1, None)
    kb2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = True)
    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x:x.distance)
    res = cv2.drawMatches(img1, kb1, img2, kb2, matches[:30], res, singlePointColor=(0, 255, 0), matchColor=(255,0,0), flags = 0)

    cv.ImageSimilarity(img1, img2, function(err, dissimilarity){
    if (err) throw err;
    console.log('dissimilarity: ', dissimilarity)
    } )
    cv2.imshow('feature Matching', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    capture()
    featureMatching()
