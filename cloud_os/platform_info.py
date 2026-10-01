from __future__ import annotations
import os,platform,shutil,sys
def detect():
 system=platform.system().lower()
 release=platform.release()
 version=platform.version()
 if system=="windows": family="windows"
 elif system=="linux": family="ubuntu" if "ubuntu" in platform.freedesktop_os_release().get("ID","").lower() else "linux"
 else: family=system
 shells=[]
 if shutil.which("powershell") or shutil.which("powershell.exe") or shutil.which("pwsh"): shells.append("powershell")
 if shutil.which("bash") or shutil.which("bash.exe"): shells.append("bash")
 return {
  "family":family,"system":platform.system(),"release":release,"version":version,
  "architecture":platform.machine(),"python":sys.version.split()[0],"cpu_count":os.cpu_count() or 1,
  "shells":shells,"docker":bool(shutil.which("docker")),"podman":bool(shutil.which("podman")),
  "wsl":system=="linux" and ("microsoft" in release.lower() or "wsl" in version.lower()),
  "supported":family in ("windows","ubuntu")
 }
