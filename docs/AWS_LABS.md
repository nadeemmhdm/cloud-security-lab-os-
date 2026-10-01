# AWS Practical Labs — Complete Solve Guide

Use only an AWS account you own or are authorized to administer. Commands below operate on real AWS resources and may incur charges.

## Module 2 — AWS Identity & Access Security
Confirm identity: `aws sts get-caller-identity`. Inspect users with `aws iam list-users`, roles with `aws iam list-roles`, attached policies with `aws iam list-attached-user-policies --user-name NAME`, and access keys with `aws iam list-access-keys --user-name NAME`. Create a dedicated lab user with `aws iam create-user --user-name cslab-student`. Create least-privilege policies as JSON files and attach them with `aws iam put-user-policy --user-name cslab-student --policy-name CSLabPolicy --policy-document file://policy.json`. Verify that no unnecessary wildcard actions/resources are granted. Remove the inline policy and lab user when finished.

## Module 3 — AWS Network Security
Create an isolated VPC: `aws ec2 create-vpc --cidr-block 10.77.0.0/16`. Record the returned VPC ID. Create subnets with `aws ec2 create-subnet --vpc-id VPC_ID --cidr-block 10.77.1.0/24`. Inspect security groups using `aws ec2 describe-security-groups --filters Name=vpc-id,Values=VPC_ID`; inspect NACLs using `aws ec2 describe-network-acls --filters Name=vpc-id,Values=VPC_ID`. Do not expose management ports to `0.0.0.0/0`. Enable VPC Flow Logs only after choosing an authorized CloudWatch/S3 destination and IAM role. Delete dependent resources before deleting the VPC.

## Module 4 — AWS Compute Security
List instances: `aws ec2 describe-instances`. For a dedicated lab instance, verify security-group ingress, encrypted EBS volumes, patch status, and IMDS configuration. Check metadata options with `aws ec2 describe-instances --instance-ids INSTANCE_ID --query "Reservations[].Instances[].MetadataOptions"`. Require IMDSv2 with `aws ec2 modify-instance-metadata-options --instance-id INSTANCE_ID --http-tokens required --http-endpoint enabled`. Restrict inbound ports to your authorized source IP/range. Stop or terminate paid lab instances after the exercise.

## Module 5 — AWS Storage & Data Security
List buckets: `aws s3api list-buckets`. Check public-access block: `aws s3api get-public-access-block --bucket BUCKET`. Enable all four public-access-block settings with `aws s3api put-public-access-block --bucket BUCKET --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true`. Check encryption with `aws s3api get-bucket-encryption --bucket BUCKET`; check versioning with `aws s3api get-bucket-versioning --bucket BUCKET`. For snapshot practice, use an authorized EBS volume and `aws ec2 create-snapshot --volume-id VOLUME_ID --description "Cloud Security Lab"`; delete the snapshot after verification if it is no longer needed.

## Cloud Security Lab OS verification
Open Labs and run the AWS module verification. It performs real read-only AWS CLI queries against the currently authenticated account. A passing provider check proves connectivity/permissions for the queried inventory; it does not claim every resource is secure.
