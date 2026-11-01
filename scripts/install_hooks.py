"""Enable this checkout's public-catalogue audit hooks; config is local only."""
import subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
subprocess.run(['git','-C',str(root),'config','--local','core.hooksPath','.githooks'],check=True)
print('Enabled .githooks/pre-commit and pre-push for this fishing checkout.')
