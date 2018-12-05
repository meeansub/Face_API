import boto3
import botocore

BUCKET_NAME = 'hosick-test'
KEY = 'test.jpg'

s3 = boto3.resource('s3')

try:
    #s3.Bucket(BUCKET_NAME).download_file(KEY, 'test.jpg')
    s3.meta.client.download_file('face-images-storage', 'gangaji.jpg', 'downtest.jpg')
    print("complete download!")
except botocore.exceptions.ClientError as e:
    if e.response['ERROR']['CODE']=="404":
        print("The object does not exist")
    else:
        raise
