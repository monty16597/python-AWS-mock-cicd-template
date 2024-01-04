# Python AWS mocking using Localstack and pytest
This project shows how we can integrate localstack in our testing suit to run test cases on AWS without actually using AWS. Localstack is well developed and popular open source tool which allows users to run AWS on local machine.

## Run project on local

### To run pytest on local machine with localstack running in Docker
```bash
pip install -r requirements.txt
docker-compose up -d localstack
pytest -s
```


### To run app on localstack
```bash
pip install -r requirements.txt
docker-compose up -d localstack
AWS_ENDPOINT_URL=http://localhost:4566 flask run
curl -X POST -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe"}' http://localhost:5000/generate_pdf
aws s3 ls s3://myapp-pub-assets --endpoint-url=http://localhost:4566
```