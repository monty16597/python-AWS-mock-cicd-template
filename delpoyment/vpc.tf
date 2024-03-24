# VPC with 1 public subnet and 1 private subnet

resource "aws_vpc" "vpc" {
  cidr_block = "10.15.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.vpc.id
  map_public_ip_on_launch = true
  cidr_block        = "10.15.0.0/24"
    availability_zone = "ca-central-1a"
}

resource "aws_internet_gateway" "igw" {
    vpc_id = aws_vpc.vpc.id
}

resource "aws_route_table" "public" {
    vpc_id = aws_vpc.vpc.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.igw.id
    }
}

resource "aws_route_table_association" "public" {
    subnet_id      = aws_subnet.public.id
    route_table_id = aws_route_table.public.id
}
