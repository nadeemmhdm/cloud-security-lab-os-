from __future__ import annotations
import json,secrets,shutil
from datetime import datetime,timezone
from .config import APP_DIR
from .labs import get,prepare,workspace
STATE=APP_DIR/"lab-runtime.json"
def _load():
 try:
  d=json.loads(STATE.read_text(encoding="utf-8")); return d if isinstance(d,dict) else {}
 except (OSError,json.JSONDecodeError):return {}
def _save(d):
 APP_DIR.mkdir(parents=True,exist_ok=True); t=STATE.with_suffix(".tmp"); t.write_text(json.dumps(d,indent=2),encoding="utf-8"); t.replace(STATE)
def start(user,lab):
 if not get(lab): raise ValueError("Unknown lab")
 d=_load(); key=user+":"+lab
 if key in d and d[key].get("status")=="active": return d[key]
 env=prepare(user,lab)
 d[key]={"id":secrets.token_hex(8),"lab":lab,"user":user,"provider":"local","mode":get(lab)["mode"],"workspace":env["workspace"],"status":"active","started":datetime.now(timezone.utc).isoformat()}
 _save(d); return d[key]
def active(user,lab):
 return _load().get(user+":"+lab,{}).get("status")=="active"
def stop(user,lab):
 d=_load(); key=user+":"+lab
 if key not in d or d[key].get("status")!="active": raise ValueError("Active lab session not found")
 d[key]["status"]="completed"; d[key]["completed"]=datetime.now(timezone.utc).isoformat(); _save(d); return d[key]
def reset(user,lab):
 if not get(lab): raise ValueError("Unknown lab")
 p=workspace(user,lab,False)
 if p.exists(): shutil.rmtree(p)
 d=_load(); d.pop(user+":"+lab,None); _save(d)
 return {"ok":True,"lab":lab}
def sessions(user=None):
 vals=list(_load().values()); return [x for x in vals if not user or x.get("user")==user]
