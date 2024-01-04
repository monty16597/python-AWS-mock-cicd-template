import os
class Config:
    AWS_S3_BUCKET_NAME = 'myapp-pub-assets'
    AWS_ENDPOINT_URL = os.environ.get('AWS_ENDPOINT_URL', None)
    print(AWS_ENDPOINT_URL)
    AWS_ACCESS_KEY_ID='TEST'
    AWS_SECRET_ACCESS_KEY='TEST'
    AWS_REGION_NAME='us-east-1'