import boto3
import botocore

s3= boto3.client('s3') # s3객체생성

# 버킷 이름 모두 출력
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List: %s" % buckets)

# upload_file로 업로드하기
file_name='minsub.png' #올릴파일
bucket_name='face-images-storage' #버킷이름
s3.upload_file(file_name,bucket_name,'GG.png',ExtraArgs={'ACL':'public-read', 'ContentType': 'image/png'})
#GG.png가 파일이 버킷에 올라갈 이름
