$ErrorActionPreference = "Stop"
$py = if (Get-Command py -ErrorAction SilentlyContinue) { "py" } elseif (Get-Command python -ErrorAction SilentlyContinue) { "python" } else { throw "Python 3.10+ is required" }
& $py -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -e .
& .\.venv\Scripts\cloud-os.exe setup
Write-Host "Installed. Start with: .\.venv\Scripts\cloud-os.exe start"
