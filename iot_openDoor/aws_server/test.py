import boto3
import botocore

s3  = boto3.resource('s3') # s3객체생성

# 버킷 이름 모두 출력
for bucket in s3.buckets.all():
    print(bucket.name)

file = 'minsub.png' #파일 경로, default는 py파일 폴더와 같음
data = open(file, 'rb') #파일 읽기전용으로 오픈

# 파일 업로드 메소드 만들기
def upload(s3, key, data) :
    s3.Bucket('face-images-storage').put_object(Key=key, Body=data,ContentType='image/png') #Key=버킷안에 저장될 이름, body=업로드 할 파일


upload(s3, 'siba.png', data)
