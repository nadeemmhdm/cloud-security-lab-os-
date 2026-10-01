from __future__ import annotations
import json,os
from .config import APP_DIR
DB=APP_DIR/"lab-access.json"
def _load():
 try:
  d=json.loads(DB.read_text(encoding="utf-8")); return d if isinstance(d,dict) else {"enabled":{},"assignments":{}}
 except (OSError,json.JSONDecodeError): return {"enabled":{},"assignments":{}}
def _save(d):
 APP_DIR.mkdir(parents=True,exist_ok=True); t=DB.with_suffix(".tmp"); t.write_text(json.dumps(d,indent=2),encoding="utf-8")
 if os.name!="nt": t.chmod(0o600)
 t.replace(DB)
 if os.name!="nt": DB.chmod(0o600)
def configure(lab_id,enabled):
 d=_load(); d.setdefault("enabled",{})[lab_id]=bool(enabled); _save(d); return bool(enabled)
def assign(username,lab_id,allowed=True):
 d=_load(); a=d.setdefault("assignments",{}).setdefault(username,[])
 if allowed and lab_id not in a:a.append(lab_id)
 if not allowed and lab_id in a:a.remove(lab_id)
 _save(d); return sorted(a)
def allowed(username,lab_id,is_admin=False):
 d=_load()
 if not d.get("enabled",{}).get(lab_id,False): return False
 return is_admin or lab_id in d.get("assignments",{}).get(username,[])
def assigned(username,is_admin=False):
 d=_load(); enabled={x for x,v in d.get("enabled",{}).items() if v}
 return sorted(enabled if is_admin else enabled.intersection(d.get("assignments",{}).get(username,[])))
def state(): return _load()
