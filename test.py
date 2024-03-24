import json
import requests


def test_generate_pdf_and_upload_to_s3():
    # Mocking the S3 upload and presigned URL generation
    pdf_data = {"first_name": "John", "last_name": "Doe"}

    # Send a POST request to the endpoint
    response = requests.post("http://15.223.51.3/generate_pdf", json=pdf_data)
    return response.json()


print(test_generate_pdf_and_upload_to_s3())
