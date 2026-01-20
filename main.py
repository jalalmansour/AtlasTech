"""
AtlasTech Main Controller
-------------------------
Entry point for the framework.
- Initializes Git Repo
- Provisions Infrastructure
- Launches Attack Dashboard
"""

import os
import sys
import subprocess
import time
from config import Config
from infrastructure.vm_manager import VMwareManager
from infrastructure.provisioner import Provisioner

def init_git_repo():
    """Initializes Git and Pushes to GitHub"""
    print("--------------------------------------------------")
    print(" 🐙 GIT REPOSITORY INITIALIZATION")
    print("--------------------------------------------------")
    
    cmds = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-m", "feat: AtlasTech Security Framework Initial Release"],
        ["git", "branch", "-M", "main"],
        ["git", "remote", "remove", "origin"], # clean slate
        ["git", "remote", "add", "origin", Config.REPO_URL],
        ["git", "push", "-u", "origin", "main", "--force"]
    ]

    for cmd in cmds:
        try:
            # Handle remote remove failing if it doesn't exist
            if "remove" in cmd:
                subprocess.run(cmd, stderr=subprocess.DEVNULL, check=False)
                continue
            
            print(f"Executing: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            if "push" in cmd:
                print("❌ Push failed. Check credentials.")
            else:
                print(f"❌ Error: {e}")
            return
            
    print("✅ Repository setup complete.")

def deploy_lab():
    """Orchestrates the Lab Deployment"""
    print("--------------------------------------------------")
    print(" 🏗️ INFRASTRUCTURE DEPLOYMENT")
    print("--------------------------------------------------")
    
    # 1. VMware Provisioning
    vm_mgr = VMwareManager()
    if vm_mgr.connect():
        target_ip = vm_mgr.deploy_vm()
    else:
        target_ip = input("Enter Target IP manually: ")

    # 2. Server Configuration
    print(f"⚡ Provisioning Target at {target_ip}...")
    prov = Provisioner(target_ip)
    if prov.connect():
        prov.deploy_vulnerable_stack()
        print(f"✅ Lab Ready! Target: {target_ip}")
        print(f"   HR App: http://{target_ip}/hr/login.php")
    else:
        print("❌ Could not connect via SSH to provision.")

def start_dashboard():
    """Launches the Streamlit GUI"""
    print("--------------------------------------------------")
    print(" 🚀 LAUNCHING COMMAND CENTER")
    print("--------------------------------------------------")
    cmd = ["streamlit", "run", "dashboard/app.py"]
    subprocess.run(cmd)

def main():
    while True:
        print("\n=== ATLASTECH SECURITY FRAMEWORK ===")
        print("1. 🐙 Initialize Git Repository")
        print("2. 🏗️ Deploy Vulnerable Lab")
        print("3. 🚀 Start Attack Dashboard")
        print("4. 🚪 Exit")
        
        choice = input("Select Option: ")
        
        if choice == '1':
            init_git_repo()
        elif choice == '2':
            deploy_lab()
        elif choice == '3':
            start_dashboard()
        elif choice == '4':
            sys.exit(0)
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
