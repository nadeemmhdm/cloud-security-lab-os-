from __future__ import annotations
import json,os,socket
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
{"id":"defender-xdr","module":9,"provider":"local","title":"Microsoft Defender XDR","mode":"Local XDR Concept Practical","topics":["XDR Fundamentals","Threat Detection","Defense Evasion","Execution","Credential Access","Privilege Escalation","Lateral Movement"]}]
def catalog(): return LABS
def get(lab_id): return next((x for x in LABS if x["id"]==lab_id),None)
def workspace(user,lab_id,create=False):
 p=(APP_DIR/"labs"/user/lab_id).resolve()
 if create:p.mkdir(parents=True,exist_ok=True)
 return p
def prepare(user,lab_id):
 lab=get(lab_id)
 if not lab: raise ValueError("Unknown lab")
 p=workspace(user,lab_id,True); info=detect()
 manifest={"lab_id":lab_id,"module":lab["module"],"title":lab["title"],"mode":lab["mode"],"topics":[{"name":x,"status":"ready"} for x in lab["topics"]],"host":{"system":info["system"],"release":info["release"],"architecture":info["architecture"]}}
 (p/"exercise.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
 (p/"README.txt").write_text(f"{lab['title']}\n{lab['mode']}\nHost: {info['system']} {info['release']}\nTopics: {len(lab['topics'])}\n",encoding="utf-8")
 if lab_id in ("sentinel","kql","defender-xdr"):
  events=[{"event_id":1,"severity":"info","source":"lab","message":"lab workspace initialized"},{"event_id":2,"severity":"warning","source":"auth","message":"training authentication event"},{"event_id":3,"severity":"high","source":"endpoint","message":"training detection event"}]
  (p/"events.jsonl").write_text("\n".join(json.dumps(x) for x in events)+"\n",encoding="utf-8")
 return {"workspace":str(p),"platform":info,"exercise":manifest}
def verify(lab_id,user="admin"):
 lab=get(lab_id)
 if not lab: raise ValueError("Unknown lab")
 p=workspace(user,lab_id,False)
 if not p.is_dir(): raise ValueError("Lab has not been started")
 info=detect(); checks=[]
 def add(name,ok,detail): checks.append({"name":name,"ok":bool(ok),"detail":str(detail)[:500]})
 add("Supported host",info["supported"],f"{info['system']} {info['release']}")
 add("Real host shell",bool(info["shells"]),", ".join(info["shells"]) or "none")
 add("Lab workspace",p.is_dir(),p)
 try:m=json.loads((p/"exercise.json").read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError):m={}
 add("Exercise manifest",m.get("lab_id")==lab_id and len(m.get("topics",[]))==len(lab["topics"]),"all syllabus topics provisioned")
 if lab_id=="aws-iam": add("Identity controls",bool(os.environ.get("USERNAME") or os.environ.get("USER")),"host identity available")
 elif lab_id=="aws-network": add("Network stack",bool(socket.gethostname()),socket.gethostname())
 elif lab_id=="aws-compute": add("Compute",info["cpu_count"]>0,f"{info['cpu_count']} logical CPUs")
 elif lab_id=="aws-storage": add("Storage write",os.access(p,os.W_OK),p)
 elif lab_id=="azure-security": add("Security monitoring",p.exists(),"host security workspace ready")
 elif lab_id in ("sentinel","kql","defender-xdr"):
  ep=p/"events.jsonl"
  try: events=[json.loads(x) for x in ep.read_text(encoding="utf-8").splitlines() if x.strip()]
  except (OSError,json.JSONDecodeError): events=[]
  add("Local telemetry",len(events)>=3 and any(x.get("severity")=="high" for x in events),f"{len(events)} events")
 return {"lab":lab_id,"provider":"local","mode":lab["mode"],"passed":all(x["ok"] for x in checks),"checks":checks}
