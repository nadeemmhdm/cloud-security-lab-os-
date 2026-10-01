def test_lab_access_requires_enable_and_assignment(tmp_path,monkeypatch):
 import cloud_os.lab_access as a
 a.APP_DIR=tmp_path; a.DB=tmp_path/"access.json"
 assert not a.allowed("student","aws-iam")
 a.configure("aws-iam",True)
 assert not a.allowed("student","aws-iam")
 a.assign("student","aws-iam",True)
 assert a.allowed("student","aws-iam")
 assert a.allowed("admin","aws-iam",True)

def test_disabled_lab_denies_even_assigned(tmp_path):
 import cloud_os.lab_access as a
 a.APP_DIR=tmp_path; a.DB=tmp_path/"access.json"
 a.configure("aws-iam",True); a.assign("student","aws-iam",True); a.configure("aws-iam",False)
 assert not a.allowed("student","aws-iam")

def test_runtime_rejects_unknown_lab():
 import pytest,cloud_os.lab_runtime as r
 with pytest.raises(ValueError): r.start("student","not-a-lab")
