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
    
    # --- VMware Settings ---
    VM_PROVIDER = "workstation" # Options: "vsphere", "workstation"
    
    # vSphere Settings (if VM_PROVIDER == "vsphere")
    VM_HOST = "192.168.1.50"
    VM_USER = "administrator@vsphere.local"
    VM_PASS = "VMwarePass123!"
    DATASTORE = "datastore1"

    # Workstation Settings (if VM_PROVIDER == "workstation")
    VMRUN_PATH = r"C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe"
    VMX_PATH = r"C:\Users\jalal\Documents\Virtual Machines\Windows Server 2025\Windows Server 2025.vmx" # Example Path

    TEMPLATE_NAME = "Windows Server 2025" 
    TARGET_VM_NAME = "AtlasTech-Windows-Target"

    # --- Target Lab Network ---
    NETWORK_RANGE = "192.168.1.0/24"
    GATEWAY_IP = "192.168.1.1"
    INTERFACE = "Eth0" # Interface for Scapy/Nmap

    # --- Credentials for Lab Access ---
    LAB_USER = "Administrator"
    LAB_PASS = "AtlasAdmin123!" # Stronger pass for Windows
    
    LAB_DB_ROOT_PASS = "SuperSecretRootPassword!"
    LAB_DB_APP_PASS = "AppUserPassword123!"

    # --- Attack Suite Settings ---
    WORDLIST_PATH = r"C:\Users\jalal\OneDrive\Documents\python\JobinTech_PFE\wordlists\rockyou.txt"
    THREADS = 10
