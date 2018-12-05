import boto3
import botocore

s3= boto3.client('s3') # s3객체생성

# 버킷 이름 모두 출력
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List: %s" % buckets)

# upload_file로 업로드하기
file_name='taehoon.png'
bucket_name='face-images-storage'
s3.upload_file(file_name,bucket_name,'taehoon.png')
