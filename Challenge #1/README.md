# Challenge 1 : Terraform - Deploy 3-tier Application
This Terraform code will create 3-tier application in AWS.

## Prerequisites
Install Terraform
Install the AWS CLI
Sign up for an AWS Account
Your preferred IDE

## Structure of the Code
1. Modules:
   Contains the reusable terraform code. This will create VPC, Subnet, EC2, Internet Gateway and other resources.
2. Dev:
   This contains the terraform code, which make use of Terraform modules and passes parameters to it.
   This is used to deploy the Application to **Dev** environment.
3. QA:
   This is used to deploy the Application to **Dev** environment.
4. Prod:
   This is used to deploy the Application to **Dev** environment.

## Commands to be Executed
1. Please navigate to the your desired directory(Dev, QA or Prod).
2. This will Initiate/download the Terraform provider executeble files
   ```
   Terraform init
   ```
3. This will **validate** and check for any syntactical error
   ```
   Terraform validate
   ```
4. This will generate the plan. If required the plan can be saved for future reference.
   ```
   terraform plan
   ```
5. Once the plan is validated and approved to create the resource, please run
   ```
   terraform apply
   ```
   > a prompt will be made seeking approval to create the resource, this can be avoided by passing `--auto-approve` to terraform apply command

created resources can be deleted by running `terraform destroy` command.