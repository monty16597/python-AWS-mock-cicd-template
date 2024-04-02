import boto3
from botocore.exceptions import ClientError
from botocore.client import Config

from flask import current_app

with current_app.app_context():
    # boto3 session with AWS credentials ##
    session = boto3.Session(
        aws_access_key_id=current_app.config.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=current_app.config.get("AWS_SECRET_ACCESS_KEY"),
        region_name=current_app.config.get("AWS_REGION_NAME"),
    )

    s3_client = session.client(
        "s3", endpoint_url=current_app.config.get("AWS_ENDPOINT_URL"), config=Config(signature_version='s3v4')
    )

    def upload_pdf_file(pdf_filename):
        # Upload the generated PDF to S3
        try:
            s3_client.upload_file(
                pdf_filename, current_app.config.get("AWS_S3_BUCKET_NAME"), pdf_filename
            )
        except ClientError as e:
            raise e

    def generate_presigned_url(pdf_filename):
        # Generate a presigned URL for the uploaded file
        try:
            presigned_url = s3_client.generate_presigned_url(
                "get_object",
                Params={
                    "Bucket": current_app.config.get("AWS_S3_BUCKET_NAME"),
                    "Key": pdf_filename,
                },
                ExpiresIn=3600,  # URL expiration time in seconds (adjust as needed)
            )
            return presigned_url
        except ClientError as e:
            raise e
