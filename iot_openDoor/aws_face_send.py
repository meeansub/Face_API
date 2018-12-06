import boto3
import botocore
import face_recognition

s3= boto3.client('s3') # s3객체생성

detect_face_name=face_recognition.face_name


# upload_file로 업로드하기

#버킷이름
bucket_name='face-images-storage'

#인식 성공한 얼굴파일
file_name='successCap/'+detect_face_name+'.png' 
#s3에 png 파일 보내기
s3.upload_file(file_name,bucket_name,detect_face_name+'.png',ExtraArgs={'ACL':'public-read', 'ContentType': 'image/png'})

#인식 성공시점 로그 json 파일
json_name='result/'+detect_face_name+'.json' 
#s3에 json 파일 보내기
s3.upload_file(json_name,bucket_name,detect_face_name+'.json',ExtraArgs={'ACL':'public-read', 'ContentType': 'application/json'})

#detect_face_name+'.png'/ detect_face_name+'.json' 파일이 버킷에 올라갈 이름

# 버킷 이름 모두 출력
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List: %s 에 저장되었습니다" % buckets)
