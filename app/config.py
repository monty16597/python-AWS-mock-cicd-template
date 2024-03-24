import os


class AppConfig:
    AWS_S3_BUCKET_NAME = "myapp-pub-assets"
    AWS_ENDPOINT_URL = os.environ.get("AWS_ENDPOINT_URL", None)
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "TEST")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "TEST")
    AWS_REGION_NAME = os.environ.get("AWS_REGION_NAME", "us-east-1")
