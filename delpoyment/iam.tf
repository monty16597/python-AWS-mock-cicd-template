resource "aws_iam_instance_profile" "ec2-s3-ssm" {
  name = "ec2-s3-ssm"
  role = aws_iam_role.ec2-s3-ssm.name
}

resource "aws_iam_role" "ec2-s3-ssm" {
  name = "ec2-s3-ssm"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "ec2-s3-ssm" {
  name = "ec2-s3-ssm"
  description = "Allow S3 and SSM access"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "ssm:*"
      ],
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "ec2-s3-ssm" {
  role = aws_iam_role.ec2-s3-ssm.name
  policy_arn = aws_iam_policy.ec2-s3-ssm.arn
}