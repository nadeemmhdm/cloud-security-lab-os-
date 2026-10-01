from __future__ import annotations
import os,shutil,subprocess
from .files import storage_root
MAX_OUTPUT=20000
MAX_COMMAND=2000
ALLOWED_SHELLS={"powershell","bash"}

def _powershell():
 return shutil.which("pwsh") or shutil.which("powershell") or shutil.which("powershell.exe")
def _bash():
 return shutil.which("bash") or shutil.which("bash.exe")

def available_shells():
 out=[]
 if _powershell(): out.append("powershell")
 if _bash(): out.append("bash")
 return out

def _argv(shell,command):
 if shell not in ALLOWED_SHELLS: raise ValueError("Unsupported shell")
 if shell=="powershell":
  exe=_powershell()
  if not exe: raise ValueError("PowerShell is not installed")
  return [exe,"-NoLogo","-NoProfile","-NonInteractive","-Command",command]
 exe=_bash()
 if not exe: raise ValueError("Bash is not installed")
 return [exe,"--noprofile","--norc","-c",command]

def execute(command,timeout=20,shell=None,privileged=False):
 if not isinstance(command,str) or not command.strip() or len(command)>MAX_COMMAND: raise ValueError("Invalid command")
 shells=available_shells()
 if not shells: raise ValueError("No supported shell is installed")
 shell=shell or ("powershell" if os.name=="nt" and "powershell" in shells else "bash" if "bash" in shells else shells[0])
 if privileged:
  if os.name=="nt":
   raise PermissionError("Privileged terminal requires an already-elevated Cloud OS host process; UAC is never bypassed")
  if not shutil.which("sudo"): raise PermissionError("sudo is not installed")
  argv=["sudo","-n","--"]+_argv(shell,command)
 else:
  argv=_argv(shell,command)
 proc=subprocess.run(argv,cwd=str(storage_root()),capture_output=True,text=True,timeout=timeout,shell=False)
 return {"code":proc.returncode,"stdout":proc.stdout[-MAX_OUTPUT:],"stderr":proc.stderr[-MAX_OUTPUT:],"shell":shell,"privileged":bool(privileged)}
