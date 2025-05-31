import os
import tempfile
import shutil
import git  # You need to install GitPython: pip install GitPython
from urllib.parse import urlparse

def get_repo_source():
    input_path = input("Enter GitHub repo URL or local folder path: ").strip()

    # Case 1: GitHub URL
    if input_path.startswith("http://") or input_path.startswith("https://"):
        try:
            print("[+] Cloning GitHub repository...")
            tmp_dir = tempfile.mkdtemp()
            git.Repo.clone_from(input_path, tmp_dir)
            print(f"[✓] Cloned to temporary folder: {tmp_dir}")
            return tmp_dir  # Return path to cloned repo
        except Exception as e:
            print(f"[!] Failed to clone repo: {e}")
            return None

    # Case 2: Local folder path
    elif os.path.isdir(input_path):
        print(f"[✓] Using local folder: {input_path}")
        return input_path

    else:
        print("[!] Invalid input. Please enter a valid GitHub URL or existing folder path.")
        return None
