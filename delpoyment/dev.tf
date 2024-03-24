module "dev" {
  source = "./modules"
  project_name = "devops-project"
  env = "dev"
}

output "dev_ec2_public_ip" {
  value = module.dev.ec2_public_ip
}

output "dev_bucket_name" {
  value = module.dev.bucket_name
}