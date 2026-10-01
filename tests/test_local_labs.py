from cloud_os.platform_info import detect
from cloud_os.labs import catalog,prepare,verify
def test_platform_detection_has_required_fields():
 d=detect()
 assert d["family"] in ("windows","ubuntu","linux","darwin")
 assert isinstance(d["shells"],list)
 assert d["cpu_count"]>=1
def test_all_nine_syllabus_modules_exist():
 assert [x["module"] for x in catalog()]==list(range(1,10))
 assert all(x["provider"]=="local" for x in catalog())
def test_local_lab_prepare_and_verify(tmp_path,monkeypatch):
 import cloud_os.labs as l
 monkeypatch.setattr(l,"APP_DIR",tmp_path)
 r=prepare("student","cloud-fundamentals")
 assert "workspace" in r
 v=verify("cloud-fundamentals","student")
 assert v["provider"]=="local"
def test_security_telemetry_workspace(tmp_path,monkeypatch):
 import cloud_os.labs as l
 monkeypatch.setattr(l,"APP_DIR",tmp_path)
 l.prepare("student","kql")
 assert (tmp_path/"labs"/"student"/"kql"/"events.jsonl").exists()
