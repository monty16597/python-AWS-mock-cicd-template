import boto3
import pytest
from config import TestingConfig

import sys
import os
from config import TestingConfig

# Add the parent directory of app to the Python path
current_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(current_dir)

from app import create_app


@pytest.fixture
def client():
    app = create_app(TestingConfig)
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def aws_client():
    def _create_client(service_name):
        session = boto3.Session(
            aws_access_key_id=TestingConfig.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=TestingConfig.AWS_SECRET_ACCESS_KEY,
            region_name=TestingConfig.AWS_REGION_NAME,
        )

        return session.client(service_name, endpoint_url=TestingConfig.AWS_ENDPOINT_URL)

    return _create_client


def create_test_bucket(func):
    def wrapper(client, aws_client, *args, **kwargs):
        # Create a test bucket
        s3_client = aws_client("s3")
        try:
            s3_client.head_bucket(Bucket=TestingConfig.AWS_S3_BUCKET_NAME)
        except s3_client.exceptions.ClientError:
            s3_client.create_bucket(Bucket=TestingConfig.AWS_S3_BUCKET_NAME)
            print(f"Created a test bucket: {TestingConfig.AWS_S3_BUCKET_NAME}")

        # Run the test
        func(client, aws_client, *args, **kwargs)

        # Delete all objects in the bucket
        response = s3_client.list_objects_v2(Bucket=TestingConfig.AWS_S3_BUCKET_NAME)
        if response.get("Contents"):
            for obj in response["Contents"]:
                s3_client.delete_object(
                    Bucket=TestingConfig.AWS_S3_BUCKET_NAME, Key=obj["Key"]
                )
                print(f'Deleted the object: {obj["Key"]}')
        s3_client.delete_bucket(Bucket=TestingConfig.AWS_S3_BUCKET_NAME)
        print(f"Deleted the test bucket: {TestingConfig.AWS_S3_BUCKET_NAME}")

    return wrapper
