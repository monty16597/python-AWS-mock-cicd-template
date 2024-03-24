# Create s3 bucket
resource "aws_s3_bucket" "bucket" {
  bucket = "${var.project_name}-${var.env}-assets"
}
