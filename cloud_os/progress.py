from __future__ import annotations
import json,os
from datetime import datetime,timezone
from .config import APP_DIR
DB=APP_DIR/"lab-progress.json"
def _load():
 try:
  d=json.loads(DB.read_text(encoding="utf-8")); return d if isinstance(d,dict) else {}
 except (OSError,json.JSONDecodeError): return {}
def _save(d):
 APP_DIR.mkdir(parents=True,exist_ok=True); t=DB.with_suffix(".tmp"); t.write_text(json.dumps(d,indent=2),encoding="utf-8")
 if os.name!="nt": t.chmod(0o600)
 t.replace(DB)
 if os.name!="nt": DB.chmod(0o600)
def all_for(user): return _load().get(user,{})
def set_result(user,lab,result):
 d=_load(); d.setdefault(user,{})[lab]={"passed":bool(result.get("passed")),"updated":datetime.now(timezone.utc).isoformat()}; _save(d); return d[user][lab]
