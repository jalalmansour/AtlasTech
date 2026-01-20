"""
AtlasTech Security Framework - Professional Edition
---------------------------------------------------
Enterprise-grade automated security assessment framework.
Authorized use only under Law 07-03.

Copyright (c) 2024 AtlasTech Solutions.
"""

import os
import sys
import logging
import argparse
import time
import subprocess
from datetime import datetime

# Adjust path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import Config
from infrastructure.vm_manager import VMwareManager
from infrastructure.provisioner import Provisioner
from attack_suite.recon import ReconScanner
from attack_suite.exploits import SSHBruteForcer, SQLInjector

# Configure Logging
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(module)s: %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/atlastech_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("AtlasTech.CLI")

class AtlasConsole:
    def __init__(self):
        self.target_ip = None
        
    def print_banner(self):
        print(r"""
    _   _   _            _____         _      
   /_\ | |_| | __ _ ___ |_   _|__  ___| |__   
  //_\\| __| |/ _` / __|  | |/ _ \/ __| '_ \  
 /  _  \ |_| | (_| \__ \  | |  __/ (__| | | | 
 \_/ \_/\__|_|\__,_|___/  |_|\___|\___|_| |_| 
        Security Assessment Framework v2.0
        [AUTHORIZED PERSONNEL ONLY]
        """)

    def init_git_repo(self):
        """Initializes and syncs the Git repository."""
        logger.info("Initializing Git Repository...")
        cmds = [
            ["git", "init"],
            ["git", "add", "."],
            ["git", "commit", "-m", "feat: AtlasTech Security Framework Update"],
            ["git", "branch", "-M", "main"],
            ["git", "remote", "remove", "origin"],
            ["git", "remote", "add", "origin", Config.REPO_URL],
            ["git", "push", "-u", "origin", "main", "--force"]
        ]
        
        for cmd in cmds:
            try:
                if "remove" in cmd:
                    subprocess.run(cmd, stderr=subprocess.DEVNULL, check=False)
                    continue
                subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                logger.debug(f"Executed: {' '.join(cmd)}")
            except subprocess.CalledProcessError as e:
                if "push" in cmd:
                    logger.error("Git Push Failed. Verify credentials/network.")
                elif "remote" not in cmd:
                    logger.error(f"Git Error: {e}")
                continue
        logger.info("Repository setup complete.")

    def deploy_lab(self):
        """Provisions the testing environment."""
        logger.info("Starting Lab Deployment Sequence...")
        
        vm_mgr = VMwareManager()
        if vm_mgr.connect():
            self.target_ip = vm_mgr.deploy_vm()
        else:
            logger.warning("VMware connection failed. Requesting manual IP.")
            self.target_ip = input(">> Enter Target IP Manually: ").strip()

        if not self.target_ip:
            logger.error("No target IP provided. Aborting deployment.")
            return

        logger.info(f"Target identified at {self.target_ip}. Configuring...")
        prov = Provisioner(self.target_ip)
        if prov.connect():
            prov.deploy_vulnerable_stack()
            logger.info("Lab Deployment Successful.")
            print(f"\n[+] Target: http://{self.target_ip}/rh_crud/login.php")
        else:
            logger.error(f"Failed to connect to target {self.target_ip} via SSH.")

    def run_recon(self):
        """Executes the Reconnaissance module."""
        print("\n[*] Starting Professional Reconnaissance...")
        target = self.target_ip if self.target_ip else input(">> Enter Target Network/IP: ").strip()
        scanner = ReconScanner(target)
        
        hosts = scanner.scan_network()
        if not hosts:
            logger.warning("No hosts discovered.")
            return

        print(f"\n[+] Discovered {len(hosts)} Host(s):")
        print(f"{'IP Address':<20} {'MAC Address':<20} {'Vendor'}")
        print("-" * 60)
        for host in hosts:
            print(f"{host['ip']:<20} {host['mac']:<20} {host['vendor']}")
            
            # Deep scan choice
            if input(f"\n[?] Deep scan {host['ip']}? (y/n): ").lower() == 'y':
                details = scanner.scan_host(host['ip'])
                print(details)

    def run_exploitation(self):
        """Executes the Exploitation module."""
        print("\n[*] Starting Exploitation Framework...")
        if not self.target_ip:
             self.target_ip = input(">> Enter Target IP: ").strip()

        print("\nSelect Attack Vector:")
        print("1. SSH Brute Force")
        print("2. SQL Injection Auth Bypass")
        
        choice = input(">> Selection: ")
        
        if choice == '1':
            user = input("User (default: root): ") or "root"
            bruter = SSHBruteForcer(self.target_ip, [user], Config.WORDLIST_PATH)
            creds = bruter.run()
            if creds:
                print(f"\n[!] SUCCESS: Credentials Found: {creds}")
            else:
                print("\n[-] Attack Finished. No credentials found.")
                
        elif choice == '2':
            url = f"http://{self.target_ip}/rh_crud/login.php"
            print(f"Targeting: {url}")
            sqli = SQLInjector(url)
            success, payload = sqli.test_bypass()
            if success:
                print(f"\n[!] VULNERABILITY CONFIRMED: Auth Bypass with payload '{payload}'")
            else:
                print("\n[-] Target appears not vulnerable to simple bypass.")

    def main_menu(self):
        while True:
            self.print_banner()
            if self.target_ip:
                print(f"Target: {self.target_ip}")
            else:
                print("Target: Not Set")
                
            print("\n1. [GIT] Initialize/Sync Repository")
            print("2. [LAB] Deploy Vulnerable Environment")
            print("3. [OPS] Network Reconnaissance")
            print("4. [OPS] Launch Exploitation")
            print("5. [SYS] Exit")
            
            try:
                choice = input("\nroot@atlastech:~# ")
                if choice == '1':
                    self.init_git_repo()
                elif choice == '2':
                    self.deploy_lab()
                elif choice == '3':
                    self.run_recon()
                elif choice == '4':
                    self.run_exploitation()
                elif choice == '5':
                    print("Exiting...")
                    sys.exit(0)
                else:
                    print("Invalid command.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\nDetected Ctrl+C. Exiting...")
                sys.exit(0)

if __name__ == "__main__":
    console = AtlasConsole()
    
    # Simple argument parsing for automation
    parser = argparse.ArgumentParser(description='AtlasTech Security Framework')
    parser.add_argument('--deploy', action='store_true', help='Deploy Lab automatically')
    args = parser.parse_args()
    
    if args.deploy:
        console.deploy_lab()
    else:
        console.main_menu()
