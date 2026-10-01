from __future__ import annotations
import json,re,secrets
from datetime import datetime,timezone
from .config import APP_DIR
from .cloud_providers import run
STATE=APP_DIR/"lab-runtime.json"
SAFE=re.compile(r"^[a-zA-Z0-9_.-]{1,64}$")
def _load():
 try:return json.loads(STATE.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError):return {}
def _save(d):
 APP_DIR.mkdir(parents=True,exist_ok=True); STATE.write_text(json.dumps(d,indent=2),encoding="utf-8")
def _name(user,lab): return "cslab-"+re.sub("[^a-z0-9-]","-",user.lower())[:20]+"-"+lab[:24]+"-"+secrets.token_hex(3)
def start(user,lab):
 if lab not in {"aws-iam","aws-network","aws-compute","aws-storage","azure-security","sentinel","kql","defender-xdr"}: raise ValueError("Unknown lab")
 d=_load(); key=user+":"+lab
 if key in d and d[key].get("status")=="active": return d[key]
 name=_name(user,lab); provider="aws" if lab.startswith("aws-") else "azure"
 # Real provider preflight. Resource-specific work is performed through the authenticated cloud tools.
 check=run("aws",["sts","get-caller-identity","--output","json"]) if provider=="aws" else run("azure",["account","show","--output","json"])
 if not check["ok"]: raise RuntimeError(check["stderr"] or "Cloud authentication failed")
 d[key]={"id":secrets.token_hex(8),"lab":lab,"user":user,"provider":provider,"name":name,"status":"active","started":datetime.now(timezone.utc).isoformat()}
 _save(d); return d[key]
def stop(user,lab):
 d=_load(); key=user+":"+lab
 if key not in d: raise ValueError("Lab session not found")
 d[key]["status"]="completed"; d[key]["completed"]=datetime.now(timezone.utc).isoformat(); _save(d); return d[key]
def sessions(user=None):
 d=_load(); vals=list(d.values()); return [x for x in vals if not user or x.get("user")==user]
