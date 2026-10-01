import pytest
LAB_IDS=["cloud-fundamentals","aws-iam","aws-network","aws-compute","aws-storage","azure-security","sentinel","kql","defender-xdr"]

@pytest.fixture()
def isolated(tmp_path,monkeypatch):
 import cloud_os.labs as l,cloud_os.lab_runtime as r,cloud_os.progress as p
 monkeypatch.setattr(l,"APP_DIR",tmp_path)
 monkeypatch.setattr(r,"APP_DIR",tmp_path); monkeypatch.setattr(r,"STATE",tmp_path/"runtime.json")
 monkeypatch.setattr(p,"APP_DIR",tmp_path); monkeypatch.setattr(p,"DB",tmp_path/"progress.json")
 return tmp_path

@pytest.mark.parametrize("lab_id",LAB_IDS)
def test_every_lab_full_lifecycle(isolated,lab_id):
 import cloud_os.lab_runtime as r,cloud_os.labs as l,cloud_os.progress as p
 user="student"
 assert not r.active(user,lab_id)
 session=r.start(user,lab_id)
 assert session["status"]=="active" and r.active(user,lab_id)
 w=isolated/"labs"/user/lab_id
 assert (w/"exercise.json").is_file()
 result=l.verify(lab_id,user)
 assert result["passed"],result
 p.set_result(user,lab_id,result)
 assert p.passed(user,lab_id)
 done=r.stop(user,lab_id)
 assert done["status"]=="completed"
 r.reset(user,lab_id); p.clear(user,lab_id)
 assert not w.exists()
 assert not p.passed(user,lab_id)
 assert not r.active(user,lab_id)

@pytest.mark.parametrize("lab_id",LAB_IDS)
def test_verify_requires_started_workspace(isolated,lab_id):
 import cloud_os.labs as l
 with pytest.raises(ValueError,match="not been started"):
  l.verify(lab_id,"student")

def test_all_lab_manifests_cover_every_catalog_topic(isolated):
 import cloud_os.labs as l
 for lab in l.catalog():
  r=l.prepare("student",lab["id"])
  assert [x["name"] for x in r["exercise"]["topics"]]==lab["topics"]
