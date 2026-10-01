import shutil
from cloud_os import terminal

def test_available_shells_matches_installed_executables():
 shells=terminal.available_shells()
 if terminal._powershell(): assert "powershell" in shells
 if terminal._bash(): assert "bash" in shells

def test_shell_argv_is_argument_vector():
 for shell in terminal.available_shells():
  argv=terminal._argv(shell,"echo cloud-security-lab")
  assert isinstance(argv,list)
  assert argv[0]
  assert "echo cloud-security-lab" in argv

def test_unknown_shell_is_rejected():
 import pytest
 with pytest.raises(ValueError): terminal._argv("cmd","whoami")
