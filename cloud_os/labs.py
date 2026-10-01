from __future__ import annotations
import json,os,platform,shutil,socket
from pathlib import Path
from .config import APP_DIR
from .platform_info import detect

LABS=[
{"id":"cloud-fundamentals","module":1,"provider":"local","title":"Cloud Security Fundamentals","mode":"Local Practical Lab","topics":["Cloud Computing Fundamentals","Cloud Service Models","Shared Responsibility Model","Cloud IAM Fundamentals","Cloud Networking","Cloud Storage","Cloud Security Tools"]},
{"id":"aws-iam","module":2,"provider":"local","title":"AWS Identity & Access Security","mode":"Local Practical Equivalent","topics":["IAM","Users, Roles & Policies","Least Privilege","Access Keys","Permission Management","IAM Misconfigurations"]},
{"id":"aws-network","module":3,"provider":"local","title":"AWS Network Security","mode":"Local Practical Equivalent","topics":["VPC","Subnets","Security Groups","Network ACLs","Network Exposure","Network Security Monitoring"]},
{"id":"aws-compute","module":4,"provider":"local","title":"AWS Compute Security","mode":"Local Practical Equivalent","topics":["EC2 Security","Open Ports","Patch Management","Instance Metadata","Container Security","Compute Hardening"]},
{"id":"aws-storage","module":5,"provider":"local","title":"AWS Storage & Data Security","mode":"Local Practical Equivalent","topics":["S3 Security","Public Access","Bucket Permissions","Encryption","Data Protection","Snapshots"]},
{"id":"azure-security","module":6,"provider":"local","title":"Microsoft Azure Security","mode":"Local Practical Equivalent","topics":["Microsoft Entra ID","Azure IAM & Permissions","Azure Networking","Azure Storage Security","Azure Compute Security","Azure Security Monitoring"]},
{"id":"sentinel","module":7,"provider":"local","title":"Microsoft Sentinel & SIEM","mode":"Local SIEM Practical","topics":["SIEM Fundamentals","Microsoft Sentinel","Deployment","Log Ingestion","Detection Rules","Security Alerts","Incident Investigation"]},
{"id":"kql","module":8,"provider":"local","title":"KQL for Security Analysis","mode":"Local Query Practical","topics":["KQL Fundamentals","Basic Queries","Filtering & Searching","Sorting","Aggregation","Advanced Security Queries","Log Investigation"]},
{"id":"defender-xdr","module":9,"provider":"local","title":"Microsoft Defender XDR","mode":"Local XDR Concept Practical","topics":["XDR Fundamentals","Threat Detection","Defense Evasion","Execution","Credential Access","Privilege Escalation","Lateral Movement"]}
]
def catalog(): return LABS
def get(lab_id): return next((x for x in LABS if x["id"]==lab_id),None)
def workspace(user,lab_id):
 p=(APP_DIR/"labs"/user/lab_id).resolve(); p.mkdir(parents=True,exist_ok=True); return p
def prepare(user,lab_id):
 lab=get(lab_id)
 if not lab: raise ValueError("Unknown lab")
 p=workspace(user,lab_id); info=detect()
 (p/"README.txt").write_text(f"{lab['title']}\n{lab['mode']}\nHost: {info['system']} {info['release']}\n",encoding="utf-8")
 if lab_id in ("sentinel","kql","defender-xdr"):
  logs=p/"events.jsonl"
  if not logs.exists():
   events=[{"event_id":1,"severity":"info","source":"lab","message":"lab workspace initialized"},{"event_id":2,"severity":"warning","source":"auth","message":"training authentication event"}]
   logs.write_text("\n".join(json.dumps(x) for x in events)+"\n",encoding="utf-8")
 return {"workspace":str(p),"platform":info}
def verify(lab_id,user="admin"):
 lab=get(lab_id)
 if not lab: raise ValueError("Unknown lab")
 p=workspace(user,lab_id); info=detect(); checks=[]
 def add(name,ok,detail): checks.append({"name":name,"ok":bool(ok),"detail":str(detail)[:500]})
 add("Supported host",info["supported"],f"{info['system']} {info['release']}")
 add("Real host shell",bool(info["shells"]),", ".join(info["shells"]) or "none")
 add("Lab workspace",p.exists() and p.is_dir(),p)
 if lab_id=="aws-network":
  add("Network stack",bool(socket.gethostname()),socket.gethostname())
 elif lab_id=="aws-compute":
  add("Compute",info["cpu_count"]>0,f"{info['cpu_count']} logical CPUs")
 elif lab_id=="aws-storage":
  add("Storage write",os.access(p,os.W_OK),p)
 elif lab_id in ("sentinel","kql","defender-xdr"):
  add("Local telemetry",(p/"events.jsonl").exists(),p/"events.jsonl")
 return {"lab":lab_id,"provider":"local","mode":lab["mode"],"passed":all(x["ok"] for x in checks),"checks":checks}
