# AWS Practical Labs — Real Account Walkthrough

Use only an AWS account/role you own or are authorized to administer. Commands below operate on the real account selected by the AWS CLI.

## Module 2 — AWS Identity & Access Security
1. Confirm identity: `aws sts get-caller-identity`.
2. Inventory: `aws iam list-users`, `aws iam list-roles`, `aws iam list-policies --scope Local`.
3. Inspect attached/inline policies for a lab identity.
4. Identify wildcard actions/resources and replace them with only the actions/resources required by the lab workload.
5. Review access keys with `aws iam list-access-keys --user-name <LAB_USER>`; disable/remove unused keys.
6. Re-run the Cloud Security Lab OS AWS IAM Verify action and record the result.

## Module 3 — AWS Network Security
1. `aws ec2 describe-vpcs`
2. `aws ec2 describe-subnets`
3. `aws ec2 describe-security-groups`
4. `aws ec2 describe-network-acls`
5. Review inbound rules, especially 0.0.0.0/0 or ::/0 on administrative ports. Restrict sources to the authorized lab network.
6. Enable/review VPC Flow Logs in the lab VPC when your course exercise requires monitoring.
7. Run AWS Network Verify.

## Module 4 — AWS Compute Security
1. `aws ec2 describe-instances`
2. Inspect the selected lab instance security groups and public addressing.
3. Check instance metadata options and require IMDSv2 for the lab instance.
4. Apply OS patches through the instance's authorized management method.
5. Review container runtime configuration if the exercise uses containers.
6. Run AWS Compute Verify.

## Module 5 — AWS Storage & Data Security
1. `aws s3api list-buckets`
2. For the lab bucket inspect Public Access Block, bucket policy, encryption and versioning.
3. Keep public access blocked unless the instructor's isolated exercise explicitly requires otherwise.
4. Enable encryption and data-protection controls required by the exercise.
5. For snapshot practice use the appropriate EBS volume/snapshot workflow for the lab compute volume; S3 itself is object storage and does not use EBS snapshots.
6. Run AWS Storage Verify.

## Cleanup
Delete only resources you deliberately created for the lab. Confirm account, region, ARN/resource ID and dependencies before destructive commands. Cloud Security Lab OS does not silently destroy account resources.
