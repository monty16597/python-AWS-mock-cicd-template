import json
from custom_fixtures import client, aws_client, create_test_bucket


@create_test_bucket
def test_generate_pdf_and_upload_to_s3(client, aws_client):
    # Mocking the S3 upload and presigned URL generation
    pdf_data = {"first_name": "John", "last_name": "Doe"}

    # Send a POST request to the endpoint
    response = client.post("/generate_pdf", json=pdf_data)

    # Assertions
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "download_url" in data
    # Add more assertions as needed


def test_invalid_request_method(client):
    response = client.get("/generate_pdf")
    assert response.status_code == 405
