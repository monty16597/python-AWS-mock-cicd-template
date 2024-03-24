import os


class AppConfig:
    AWS_S3_BUCKET_NAME = os.environ.get("AWS_S3_BUCKET_NAME", None)
    AWS_ENDPOINT_URL = os.environ.get("AWS_ENDPOINT_URL", None)
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", None)
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
    AWS_REGION_NAME = os.environ.get("AWS_REGION_NAME", "us-east-1")
