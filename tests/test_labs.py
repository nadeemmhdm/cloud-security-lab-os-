def test_lab_catalog_covers_all_nine_curriculum_modules():
 from cloud_os.labs import catalog
 labs=catalog()
 assert [x["module"] for x in labs] == list(range(1,10))
 assert {"cloud-fundamentals","aws-iam","aws-network","aws-compute","aws-storage","azure-security","sentinel","kql","defender-xdr"} == {x["id"] for x in labs}

def test_catalog_does_not_claim_external_cloud_runtime():
 from cloud_os.labs import catalog
 for lab in catalog():
  assert lab["provider"] == "local"
  assert "mode" in lab
  assert "Practical" in lab["mode"]

def test_local_verification_has_no_cloud_cli_commands():
 import inspect
 import cloud_os.labs as labs
 source=inspect.getsource(labs.verify).lower()
 forbidden=("aws ","az ","run-instances","terminate-instances","authorize-security-group","revoke-security-group")
 assert not any(x in source for x in forbidden)

def test_lab_workspace_is_scoped_by_user(tmp_path,monkeypatch):
 import cloud_os.labs as l
 monkeypatch.setattr(l,"APP_DIR",tmp_path)
 alice=l.workspace("alice","aws-iam")
 bob=l.workspace("bob","aws-iam")
 assert alice != bob
 assert tmp_path.resolve() in alice.parents
 assert tmp_path.resolve() in bob.parents

def test_progress_is_per_user(tmp_path,monkeypatch):
 import cloud_os.progress as p
 p.APP_DIR=tmp_path; p.DB=tmp_path/"progress.json"
 p.set_result("alice","aws-iam",{"passed":True})
 assert p.all_for("alice")["aws-iam"]["passed"] is True
 assert p.all_for("bob")=={}
