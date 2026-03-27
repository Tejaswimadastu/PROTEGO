#!/usr/bin/env python3
"""
Run Protego from root directory (protego_iomp/)
cd into protego/ and exec scripts/run.sh equivalent.
"""

import os
import subprocess
import sys

def main():
    protego_dir = os.path.join(os.path.dirname(__file__), 'protego')
    if not os.path.exists(protego_dir):
        print("Error: protego/ directory not found!")
        sys.exit(1)
    
    # Equivalent to scripts/run.sh but for any OS
    venv_path = os.path.join(protego_dir, 'venv')
    
    # Activate venv logic (cross-platform)
    if sys.platform == 'win32':
        activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
        cmd = f'cd /d "{protego_dir}" && call "{activate_script}" && pip install -r requirements.txt && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload'
        subprocess_kwargs = {'shell': True}
    else:
        activate_script = os.path.join(venv_path, 'bin', 'activate')
        cmd = f'cd "{protego_dir}" && source "{activate_script}" && pip install -r requirements.txt && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload'
        subprocess_kwargs = {'shell': True, 'executable': '/bin/bash'}
    
    print("Starting Protego from root...")
    print("Server: http://localhost:8000")
    print("Docs: http://localhost:8000/docs")
    
    subprocess.run(cmd, **subprocess_kwargs)

if __name__ == '__main__':
    main()

