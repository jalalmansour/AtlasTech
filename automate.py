#!/usr/bin/env python3
"""
AtlasTech Security Framework - Master Automation Controller
============================================================
Fully automated deployment and control system for the AtlasTech Security Assessment Lab.

Features:
- VMware Workstation VM control (start/stop/snapshot)
- Automated vulnerable application deployment
- Screenshot capture at each phase
- Git repository synchronization
- Dashboard launch

Usage:
    python automate.py --full        # Run complete automation
    python automate.py --deploy      # Deploy app only
    python automate.py --git         # Sync to GitHub only
    python automate.py --dashboard   # Launch dashboard only
"""

import os
import sys
import time
import subprocess
import argparse
import logging
import shutil
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('atlastech_automation.log')
    ]
)
logger = logging.getLogger("AtlasTech.Automation")

# ============================================================================
# CONFIGURATION
# ============================================================================

class AutomationConfig:
    """Centralized configuration for automation"""
    
    # VMware Settings
    VMRUN_PATH = r"C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe"
    VMX_PATH = r"C:\Users\jalal\Documents\Virtual Machines\Windows Server 2025\Windows Server 2025.vmx"
    
    # Credentials
    VM_USER = "Administrator"
    VM_PASS = "AtlasAdmin123!"
    
    # Paths
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    WEBAPP_DIR = os.path.join(PROJECT_ROOT, "webapp", "rh_crud")
    SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT, "screenshots")
    
    # Git
    REPO_URL = "https://github.com/jalalmansour/AtlasTech.git"
    
    # Target Paths (on Windows Server)
    GUEST_WEB_ROOT = r"C:\inetpub\wwwroot\rh_crud"
    GUEST_MYSQL_PATH = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def ensure_dir(path):
    """Ensure directory exists"""
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"Created directory: {path}")

def take_screenshot(phase_name):
    """Capture screenshot for documentation"""
    try:
        import pyautogui
        ensure_dir(AutomationConfig.SCREENSHOTS_DIR)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{phase_name}_{timestamp}.png"
        filepath = os.path.join(AutomationConfig.SCREENSHOTS_DIR, filename)
        
        screenshot = pyautogui.screenshot()
        screenshot.save(filepath)
        logger.info(f"📸 Screenshot saved: {filename}")
        return filepath
    except ImportError:
        logger.warning("pyautogui not installed. Skipping screenshot.")
        return None
    except Exception as e:
        logger.error(f"Screenshot failed: {e}")
        return None


# ============================================================================
# VMWARE CONTROL MODULE
# ============================================================================

class VMController:
    """Controls VMware Workstation VMs via vmrun"""
    
    def __init__(self):
        self.vmrun = AutomationConfig.VMRUN_PATH
        self.vmx = AutomationConfig.VMX_PATH
        self.user = AutomationConfig.VM_USER
        self.password = AutomationConfig.VM_PASS
        
    def _run_vmrun(self, *args):
        """Execute vmrun command"""
        cmd = [self.vmrun] + list(args)
        logger.debug(f"Executing: {' '.join(cmd)}")
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if result.returncode != 0:
                logger.error(f"vmrun error: {result.stderr}")
            return result.returncode == 0, result.stdout.strip()
        except subprocess.TimeoutExpired:
            logger.error("vmrun command timed out")
            return False, ""
        except Exception as e:
            logger.error(f"vmrun exception: {e}")
            return False, ""
    
    def is_running(self):
        """Check if VM is running"""
        success, output = self._run_vmrun("list")
        return success and self.vmx in output
    
    def start(self, gui=True):
        """Start the VM"""
        logger.info("🚀 Starting VM...")
        mode = "gui" if gui else "nogui"
        
        if self.is_running():
            logger.info("VM is already running.")
            take_screenshot("vm_already_running")
            return True
            
        success, _ = self._run_vmrun("start", self.vmx, mode)
        if success:
            logger.info("✅ VM started successfully. Waiting for boot...")
            time.sleep(30)  # Wait for Windows to boot
            take_screenshot("vm_started")
        return success
    
    def stop(self, soft=True):
        """Stop the VM"""
        logger.info("🛑 Stopping VM...")
        cmd = "stop" if not soft else "stop"
        mode = "soft" if soft else "hard"
        success, _ = self._run_vmrun(cmd, self.vmx, mode)
        if success:
            logger.info("✅ VM stopped.")
            take_screenshot("vm_stopped")
        return success
    
    def get_ip(self):
        """Get VM IP address"""
        logger.info("🔍 Getting VM IP address...")
        for attempt in range(10):
            success, ip = self._run_vmrun("getGuestIPAddress", self.vmx, "-wait")
            if success and ip:
                logger.info(f"📍 VM IP: {ip}")
                return ip
            time.sleep(5)
        logger.error("Could not get VM IP")
        return None
    
    def create_snapshot(self, name):
        """Create a VM snapshot"""
        logger.info(f"📷 Creating snapshot: {name}...")
        success, _ = self._run_vmrun("snapshot", self.vmx, name)
        if success:
            logger.info(f"✅ Snapshot '{name}' created.")
            take_screenshot(f"snapshot_{name}")
        return success
    
    def copy_file_to_guest(self, host_path, guest_path):
        """Copy file from host to guest"""
        logger.debug(f"Copying {host_path} -> {guest_path}")
        success, _ = self._run_vmrun(
            "-gu", self.user, "-gp", self.password,
            "copyFileFromHostToGuest", self.vmx,
            host_path, guest_path
        )
        return success
    
    def run_script_in_guest(self, interpreter, script):
        """Run a script inside the guest VM"""
        logger.debug(f"Running script in guest ({interpreter})")
        success, output = self._run_vmrun(
            "-gu", self.user, "-gp", self.password,
            "runScriptInGuest", self.vmx,
            interpreter, script
        )
        return success, output
    
    def run_powershell(self, command):
        """Execute PowerShell command in guest"""
        # Write command to temp file, copy to guest, execute
        temp_ps1 = os.path.join(AutomationConfig.PROJECT_ROOT, "temp_cmd.ps1")
        guest_ps1 = r"C:\Windows\Temp\atlas_cmd.ps1"
        
        with open(temp_ps1, 'w') as f:
            f.write(command)
        
        try:
            self.copy_file_to_guest(temp_ps1, guest_ps1)
            success, output = self._run_vmrun(
                "-gu", self.user, "-gp", self.password,
                "runProgramInGuest", self.vmx,
                "powershell.exe", "-ExecutionPolicy", "Bypass", "-File", guest_ps1
            )
            return success, output
        finally:
            if os.path.exists(temp_ps1):
                os.remove(temp_ps1)


# ============================================================================
# DEPLOYMENT MODULE  
# ============================================================================

class Deployer:
    """Deploys the vulnerable application to the target VM"""
    
    def __init__(self, vm_controller):
        self.vm = vm_controller
        self.webapp_dir = AutomationConfig.WEBAPP_DIR
        self.guest_root = AutomationConfig.GUEST_WEB_ROOT
        
    def install_iis(self):
        """Install IIS with PHP support on Windows Server"""
        logger.info("📦 Installing IIS and PHP support...")
        
        ps_script = """
        # Install IIS
        Install-WindowsFeature -Name Web-Server -IncludeManagementTools
        Install-WindowsFeature -Name Web-CGI
        
        # Create web directory
        New-Item -Path 'C:\\inetpub\\wwwroot\\rh_crud' -ItemType Directory -Force
        
        # Set permissions
        $acl = Get-Acl 'C:\\inetpub\\wwwroot\\rh_crud'
        $rule = New-Object System.Security.AccessControl.FileSystemAccessRule('IIS_IUSRS', 'FullControl', 'ContainerInherit,ObjectInherit', 'None', 'Allow')
        $acl.SetAccessRule($rule)
        Set-Acl 'C:\\inetpub\\wwwroot\\rh_crud' $acl
        
        Write-Host "IIS Installation Complete"
        """
        
        success, _ = self.vm.run_powershell(ps_script)
        if success:
            logger.info("✅ IIS installed successfully.")
            take_screenshot("iis_installed")
        return success
    
    def deploy_webapp(self):
        """Deploy the HR CRUD application files"""
        logger.info("📂 Deploying web application files...")
        
        # Create directory on guest
        self.vm.run_powershell(f"New-Item -Path '{self.guest_root}' -ItemType Directory -Force")
        
        # Copy each file
        files = ['config.php', 'index.php', 'add.php', 'edit.php', 'delete.php', 
                 'login.php', 'style.css', 'setup.sql']
        
        for filename in files:
            host_path = os.path.join(self.webapp_dir, filename)
            guest_path = os.path.join(self.guest_root, filename).replace('/', '\\')
            
            if os.path.exists(host_path):
                success = self.vm.copy_file_to_guest(host_path, guest_path)
                if success:
                    logger.info(f"  ✅ Copied: {filename}")
                else:
                    logger.error(f"  ❌ Failed: {filename}")
            else:
                logger.warning(f"  ⚠️ Not found: {filename}")
        
        take_screenshot("webapp_deployed")
        logger.info("✅ Web application deployed.")
        return True
    
    def setup_database(self):
        """Initialize the MySQL database"""
        logger.info("🗄️ Setting up database...")
        
        # This assumes MySQL is installed on the Windows Server
        ps_script = f"""
        $mysqlPath = "{AutomationConfig.GUEST_MYSQL_PATH}"
        $sqlFile = "{self.guest_root}\\setup.sql"
        
        if (Test-Path $mysqlPath) {{
            & $mysqlPath -u root -e "source $sqlFile"
            Write-Host "Database setup complete"
        }} else {{
            Write-Host "MySQL not found - manual setup required"
        }}
        """
        
        success, output = self.vm.run_powershell(ps_script)
        take_screenshot("database_setup")
        return success


# ============================================================================
# GIT SYNCHRONIZATION MODULE
# ============================================================================

class GitSync:
    """Handles Git repository operations"""
    
    def __init__(self, project_root):
        self.root = project_root
        self.repo_url = AutomationConfig.REPO_URL
        
    def sync(self, message=None):
        """Initialize, commit, and push to GitHub"""
        logger.info("🐙 Synchronizing with GitHub...")
        
        if message is None:
            message = f"Auto-sync: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        commands = [
            ["git", "init"],
            ["git", "add", "."],
            ["git", "commit", "-m", message],
            ["git", "branch", "-M", "main"],
        ]
        
        # Try to remove existing remote (ignore errors)
        subprocess.run(["git", "remote", "remove", "origin"], 
                      cwd=self.root, capture_output=True)
        
        commands.extend([
            ["git", "remote", "add", "origin", self.repo_url],
            ["git", "push", "-u", "origin", "main", "--force"]
        ])
        
        for cmd in commands:
            try:
                logger.debug(f"Running: {' '.join(cmd)}")
                result = subprocess.run(cmd, cwd=self.root, capture_output=True, text=True)
                if result.returncode != 0 and "push" in cmd:
                    logger.error(f"Git push failed: {result.stderr}")
                    return False
            except Exception as e:
                logger.error(f"Git command failed: {e}")
                
        take_screenshot("git_synced")
        logger.info(f"✅ Repository synced to {self.repo_url}")
        return True


# ============================================================================
# DASHBOARD LAUNCHER
# ============================================================================

class DashboardLauncher:
    """Launches the Streamlit command center"""
    
    def __init__(self, project_root):
        self.root = project_root
        self.app_path = os.path.join(project_root, "dashboard", "app.py")
        
    def launch(self):
        """Start the Streamlit dashboard"""
        logger.info("🚀 Launching AtlasTech Command Center...")
        
        if not os.path.exists(self.app_path):
            logger.error(f"Dashboard not found: {self.app_path}")
            return False
        
        take_screenshot("dashboard_launching")
        
        # Launch Streamlit (non-blocking)
        subprocess.Popen(
            ["streamlit", "run", self.app_path],
            cwd=self.root,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        
        time.sleep(5)  # Wait for startup
        take_screenshot("dashboard_running")
        logger.info("✅ Dashboard launched at http://localhost:8501")
        return True


# ============================================================================
# MAIN AUTOMATION ORCHESTRATOR
# ============================================================================

class AutomationOrchestrator:
    """Master controller for the entire automation workflow"""
    
    def __init__(self):
        self.vm = VMController()
        self.deployer = Deployer(self.vm)
        self.git = GitSync(AutomationConfig.PROJECT_ROOT)
        self.dashboard = DashboardLauncher(AutomationConfig.PROJECT_ROOT)
        
    def run_full_automation(self):
        """Execute the complete automation workflow"""
        logger.info("=" * 60)
        logger.info("🎯 ATLASTECH FULL AUTOMATION STARTING")
        logger.info("=" * 60)
        
        take_screenshot("automation_start")
        
        # Phase 1: Git Sync
        logger.info("\n📌 PHASE 1: Git Repository Sync")
        self.git.sync("feat: AtlasTech Security Framework - Full Automation")
        
        # Phase 2: VM Control
        logger.info("\n📌 PHASE 2: VM Control")
        if not self.vm.start(gui=True):
            logger.error("Failed to start VM. Aborting.")
            return False
        
        # Wait for VMware Tools
        time.sleep(10)
        vm_ip = self.vm.get_ip()
        
        # Phase 3: Create Baseline Snapshot
        logger.info("\n📌 PHASE 3: Create Baseline Snapshot")
        self.vm.create_snapshot("Pre-Deployment-Baseline")
        
        # Phase 4: Deploy Application
        logger.info("\n📌 PHASE 4: Deploy Vulnerable Application")
        self.deployer.install_iis()
        self.deployer.deploy_webapp()
        self.deployer.setup_database()
        
        # Phase 5: Post-Deployment Snapshot
        logger.info("\n📌 PHASE 5: Create Post-Deployment Snapshot")
        self.vm.create_snapshot("Post-Deployment-Ready")
        
        # Phase 6: Launch Dashboard
        logger.info("\n📌 PHASE 6: Launch Command Center")
        self.dashboard.launch()
        
        # Final Summary
        logger.info("\n" + "=" * 60)
        logger.info("✅ AUTOMATION COMPLETE!")
        logger.info("=" * 60)
        logger.info(f"  VM IP: {vm_ip}")
        logger.info(f"  HR App: http://{vm_ip}/rh_crud/")
        logger.info(f"  Dashboard: http://localhost:8501")
        logger.info(f"  Screenshots: {AutomationConfig.SCREENSHOTS_DIR}")
        logger.info("=" * 60)
        
        take_screenshot("automation_complete")
        return True


# ============================================================================
# CLI ENTRY POINT
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="AtlasTech Security Framework Automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python automate.py --full        Run complete automation
  python automate.py --deploy      Deploy app to VM
  python automate.py --git         Sync to GitHub
  python automate.py --dashboard   Launch dashboard
  python automate.py --vm-start    Start VM only
  python automate.py --vm-stop     Stop VM
  python automate.py --screenshot  Take a test screenshot
        """
    )
    
    parser.add_argument('--full', action='store_true', help='Run full automation')
    parser.add_argument('--deploy', action='store_true', help='Deploy webapp to VM')
    parser.add_argument('--git', action='store_true', help='Sync to GitHub')
    parser.add_argument('--dashboard', action='store_true', help='Launch dashboard')
    parser.add_argument('--vm-start', action='store_true', help='Start VM')
    parser.add_argument('--vm-stop', action='store_true', help='Stop VM')
    parser.add_argument('--screenshot', action='store_true', help='Take test screenshot')
    
    args = parser.parse_args()
    
    # Initialize components
    orchestrator = AutomationOrchestrator()
    
    if args.full:
        orchestrator.run_full_automation()
    elif args.deploy:
        orchestrator.vm.start()
        orchestrator.deployer.deploy_webapp()
    elif args.git:
        orchestrator.git.sync()
    elif args.dashboard:
        orchestrator.dashboard.launch()
    elif args.vm_start:
        orchestrator.vm.start()
    elif args.vm_stop:
        orchestrator.vm.stop()
    elif args.screenshot:
        take_screenshot("test_screenshot")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
