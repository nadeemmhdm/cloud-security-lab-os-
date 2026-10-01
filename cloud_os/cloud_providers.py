from __future__ import annotations
import json, shutil, subprocess

MAX_OUTPUT=20000
def _run(argv,timeout=45):
 p=subprocess.run(argv,capture_output=True,text=True,timeout=timeout,shell=False)
 return {"ok":p.returncode==0,"code":p.returncode,"stdout":p.stdout[-MAX_OUTPUT:],"stderr":p.stderr[-MAX_OUTPUT:]}

def status():
 aws=shutil.which("aws"); az=shutil.which("az")
 out={"aws":{"installed":bool(aws),"authenticated":False},"azure":{"installed":bool(az),"authenticated":False}}
 if aws:
  r=_run([aws,"sts","get-caller-identity","--output","json"])
  out["aws"]["authenticated"]=r["ok"]
  if r["ok"]:
   try:
    d=json.loads(r["stdout"]); out["aws"]["account"]=d.get("Account"); out["aws"]["arn"]=d.get("Arn")
   except json.JSONDecodeError: pass
 if az:
  r=_run([az,"account","show","--output","json"])
  out["azure"]["authenticated"]=r["ok"]
  if r["ok"]:
   try:
    d=json.loads(r["stdout"]); out["azure"]["subscription"]=d.get("name"); out["azure"]["tenantId"]=d.get("tenantId")
   except json.JSONDecodeError: pass
 return out

def run(provider,args,timeout=60):
 if provider=="aws":
  exe=shutil.which("aws")
 elif provider=="azure":
  exe=shutil.which("az")
 else: raise ValueError("Unsupported cloud provider")
 if not exe: raise RuntimeError(f"{provider} CLI is not installed")
 if not isinstance(args,list) or not args or len(args)>40 or any(not isinstance(x,str) or len(x)>500 for x in args):
  raise ValueError("Invalid cloud command arguments")
 return _run([exe,*args],timeout)
