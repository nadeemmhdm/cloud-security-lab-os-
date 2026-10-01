import json
def test_lab_catalog_covers_cloud_curriculum():
 from cloud_os.labs import catalog
 ids={x["id"] for x in catalog()}
 assert {"aws-iam","aws-network","aws-compute","aws-storage","azure-security","sentinel","kql","defender-xdr"} <= ids

def test_cloud_provider_rejects_unknown_provider():
 import pytest
 from cloud_os.cloud_providers import run
 with pytest.raises(ValueError): run("unknown",["status"])

def test_cloud_provider_rejects_empty_arguments():
 import pytest
 from cloud_os.cloud_providers import run
 with pytest.raises(ValueError): run("aws",[])

def test_lab_checks_are_read_only_catalog_commands():
 from cloud_os.labs import catalog
 forbidden={"create","delete","put","update","terminate","run-instances","authorize","revoke"}
 for lab in catalog():
  for cmd in lab["checks"]:
   assert not any(x in forbidden for x in cmd)

def test_progress_is_per_user(tmp_path,monkeypatch):
 import cloud_os.progress as p
 p.APP_DIR=tmp_path; p.DB=tmp_path/"progress.json"
 p.set_result("alice","aws-iam",{"passed":True})
 assert p.all_for("alice")["aws-iam"]["passed"] is True
 assert p.all_for("bob")=={}
