# Create EC2 instance with Amzaon Linux 2 AMI and lambton key pair. Attach IAM role with S3 full access and SSM connection access. Install minikube and kubectl on the instance.
resource "aws_instance" "ec2" {
  ami = data.aws_ami_ids.amazon-linux2.ids[0]
  instance_type = "t2.micro"
  key_name = "lambton"
  subnet_id = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.ec2.id]
  tags = {
    Name = "${var.project_name}-${var.env}-app"
  }

  iam_instance_profile = aws_iam_instance_profile.ec2-s3-ssm.name
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker
              service docker start
              usermod -a -G docker ec2-user
              echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDXfDm+36wbQVC3pdt+gTYp3gmF6PjC73VHstJ73MNQWCBoruNUI0+4+63+2ok5aUtlARiVNFW9x9e7r+DVuJFlFSnJ/ZjROYebUAfjswTcbyGtI8RLbBCgh+I8pujbObj2iM6ySB6JoAtzMPrtKVNJW0kmtrR2D1WGbVyvkNHnAW0xhTA/3j2X9ZdtR1YRSMz/M+J8+jT3WKrqA3alRo0XDxG4iIepo1gF9EHCD8Em21ViMhz09da9X76BTIDng1q84Ef7uzPCCR9zRMj7qwLPct0ehbn8JKmX9Eb5AOrvbZgCnE/1HkdFm602jZHXosuX7Ov9+w8mMzSDYqLI3uVgrJY7xnl6O3kMyn2FDIU7d7VGp63aNC0RRn8rYRRISjgDDInKjKsJUYD0QBpszJbD2ZqNrYU+ww0DZxjic0Aq91KwEvj3GWLLF8XXxO6HQForMSit+B4wn+dUYjFLKxo9IId1EG45U5MTkP4jLPna8ypa+hlgafBxEsJDQwFgH9E= alonj@Divy" >> /home/ec2-user/.ssh/authorized_keys
              EOF
}

# security group for ec2 instance
resource "aws_security_group" "ec2" {
  name = "${var.project_name}-${var.env}-ec2-sg"
  vpc_id = aws_vpc.vpc.id

    egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    }

    ingress = [ 
        {
            from_port = 80
            to_port = 80
            protocol = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
            description = "Allow HTTP inbound traffic"
            ipv6_cidr_blocks = []
            prefix_list_ids = []
            security_groups = []
            self = true
        },
        {
            from_port = 22
            to_port = 22
            protocol = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
            description = "Allow SSH traffic"
            ipv6_cidr_blocks = []
            prefix_list_ids = []
            security_groups = []
            self = true
        }
    ]
}


data "aws_ami_ids" "amazon-linux2" {
  owners = ["amazon"]
  filter {
    name = "name"
    values = ["amzn2-ami-hvm-2.0.*-x86_64*"]
  }
}

resource "aws_eip" "eip" {
  instance = aws_instance.ec2.id
  vpc = true
}