"""
AtlasTech Configuration
-----------------------
Centralized configuration for the AtlasTech Security Assessment Framework.
"""

import os

class Config:
    # --- Project Metadata ---
    PROJECT_NAME = "AtlasTech Solutions Security Assessment"
    REPO_URL = "https://github.com/jalalmansour/AtlasTech.git"
    
    # --- VMware vSphere Settings ---
    # REPLACE WITH ACTUAL LAB CREDENTIALS
    VM_HOST = "192.168.1.50"           # vCenter/ESXi IP
    VM_USER = "administrator@vsphere.local"
    VM_PASS = "VMwarePass123!"         # vCenter Password
    TEMPLATE_NAME = "Ubuntu-22.04-Template" # Existing Template Name
    TARGET_VM_NAME = "AtlasTech-Vuln-Server"
    DATASTORE = "datastore1"

    # --- Target Lab Network ---
    NETWORK_RANGE = "192.168.1.0/24"
    GATEWAY_IP = "192.168.1.1"
    INTERFACE = "Eth0" # Interface for Scapy/Nmap

    # --- Credentials for Lab Access ---
    # These are the credentials we will inject/use in the lab
    LAB_SSH_USER = "atlas"
    LAB_SSH_PASS = "AtlasInitial123!"
    
    LAB_DB_ROOT_PASS = "SuperSecretRootPassword!"
    LAB_DB_APP_PASS = "AppUserPassword123!"

    # --- Attack Suite Settings ---
    WORDLIST_PATH = "/usr/share/wordlists/rockyou.txt" # Path on the attacking machine (Kali/Linux)
    THREADS = 10
