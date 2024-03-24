# Create s3 bucket
resource "aws_s3_bucket" "bucket" {
  bucket = "lambton-devops-project"
}

# # Create s3 bucket policy
# resource "aws_s3_bucket_policy" "bucket_policy" {
#   bucket = aws_s3_bucket.bucket.bucket
#   policy = <<EOF
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Effect": "Allow",
#       "Principal": "*",
#       "Action": "s3:GetObject",
#       "Resource": "arn:aws:s3:::${aws_s3_bucket.bucket.bucket}/*"
#     }
#   ]
# }
# EOF
# }

