output "ec2_public_ip" {
  value = aws_eip.eip.public_ip
}

output "bucket_name" {
  value = aws_s3_bucket.bucket.bucket
}
