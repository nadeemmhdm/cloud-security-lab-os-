from __future__ import annotations
from .cloud_providers import run

LABS=[
{"id":"aws-iam","module":2,"provider":"aws","title":"AWS Identity & Access Security","topics":["IAM","Users, Roles & Policies","Least Privilege","Access Keys","Permission Management","IAM Misconfigurations"],"checks":[["iam","list-users","--output","json"],["iam","list-roles","--output","json"]]},
{"id":"aws-network","module":3,"provider":"aws","title":"AWS Network Security","topics":["VPC","Subnets","Security Groups","Network ACLs","Network Exposure","Network Security Monitoring"],"checks":[["ec2","describe-vpcs","--output","json"],["ec2","describe-security-groups","--output","json"]]},
{"id":"aws-compute","module":4,"provider":"aws","title":"AWS Compute Security","topics":["EC2 Security","Open Ports","Patch Management","Instance Metadata","Container Security","Compute Hardening"],"checks":[["ec2","describe-instances","--output","json"]]},
{"id":"aws-storage","module":5,"provider":"aws","title":"AWS Storage & Data Security","topics":["S3 Security","Public Access","Bucket Permissions","Encryption","Data Protection","Snapshots"],"checks":[["s3api","list-buckets","--output","json"]]},
{"id":"azure-security","module":6,"provider":"azure","title":"Microsoft Azure Security","topics":["Microsoft Entra ID","Azure IAM & Permissions","Azure Networking","Azure Storage Security","Azure Compute Security","Azure Security Monitoring"],"checks":[["account","show","--output","json"],["group","list","--output","json"]]},
{"id":"sentinel","module":7,"provider":"azure","title":"Microsoft Sentinel & SIEM","topics":["SIEM Fundamentals","Microsoft Sentinel","Deployment","Log Ingestion","Detection Rules","Security Alerts","Incident Investigation"],"checks":[["account","show","--output","json"]]},
{"id":"kql","module":8,"provider":"azure","title":"KQL for Security Analysis","topics":["KQL Fundamentals","Basic Queries","Filtering & Searching","Sorting","Aggregation","Advanced Security Queries","Log Investigation"],"checks":[["account","show","--output","json"]]},
{"id":"defender-xdr","module":9,"provider":"azure","title":"Microsoft Defender XDR","topics":["XDR Fundamentals","Threat Detection","Defense Evasion","Execution","Credential Access","Privilege Escalation","Lateral Movement"],"checks":[["account","show","--output","json"]]}
]
def catalog(): return LABS
def get(lab_id):
 return next((x for x in LABS if x["id"]==lab_id),None)
def verify(lab_id):
 lab=get(lab_id)
 if not lab: raise ValueError("Unknown lab")
 results=[]
 for args in lab["checks"]:
  r=run(lab["provider"],args)
  results.append({"command":" ".join(args),"ok":r["ok"],"code":r["code"],"stderr":r["stderr"][-1000:]})
 return {"lab":lab_id,"provider":lab["provider"],"passed":all(x["ok"] for x in results),"checks":results}
