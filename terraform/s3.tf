# Create s3 bucket
resource "aws_s3_bucket" "bucket" {
  bucket = "${var.project_name}-${var.env}-assets"
}

resource "aws_s3_bucket_ownership_controls" "bucket" {
  bucket = aws_s3_bucket.bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

