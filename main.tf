provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "dev_ec2"{
    ami = "ami-0ec18f6103c5e0491"
    instance_type = "t2.micro"
  tags = {
 Name = "Dev-EC2"
 Enviorment = "Dev"
 Autostop =  "True"
  }
}  
