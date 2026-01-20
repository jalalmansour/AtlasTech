"""
VMware Manager
--------------
Handles interaction with vSphere/ESXi or VMware Workstation to deploy the target infrastructure.
"""

import ssl
import time
import logging
import atexit
import subprocess
import os
from ..config import Config

# Try importing pyVmomi, handle if not present (dev environment)
try:
    from pyVmomi import vim
    from pyVim.connect import SmartConnect, Disconnect
    PYVMOMI_AVAILABLE = True
except ImportError:
    PYVMOMI_AVAILABLE = False

logger = logging.getLogger("AtlasTech.VM")

class VMwareManager:
    def __init__(self):
        self.si = None
        self.provider = Config.VM_PROVIDER

    def connect(self):
        """Connects to the configured Hypervisor"""
        if self.provider == "workstation":
            return self._connect_workstation()
        else:
            return self._connect_vsphere()

    def _connect_workstation(self):
        if not os.path.exists(Config.VMRUN_PATH):
            logger.error(f"vmrun.exe not found at {Config.VMRUN_PATH}")
            return False
        logger.info("VMware Workstation (vmrun) detected.")
        return True

    def _connect_vsphere(self):
        if not PYVMOMI_AVAILABLE:
            logger.warning("pyVmomi not installed. Running in MOCK mode.")
            return True

        try:
            context = ssl._create_unverified_context()
            self.si = SmartConnect(
                host=Config.VM_HOST, 
                user=Config.VM_USER, 
                pwd=Config.VM_PASS, 
                sslContext=context
            )
            atexit.register(Disconnect, self.si)
            logger.info("Successfully connected to vCenter.")
            return True
        except Exception as e:
            logger.error(f"vCenter Connection Failed: {e}")
            return False

    def deploy_vm(self):
        """Orchestrates VM deployment based on provider"""
        if self.provider == "workstation":
            return self._deploy_workstation()
        else:
            return self._deploy_vsphere()

    def _deploy_workstation(self):
        """
        Controls local VMware Workstation.
        For Workstation, we typically 'Start' an existing VM rather than clone 
        (cloning via vmrun is limited/slow).
        """
        vmx_path = Config.VMX_PATH
        logger.info(f"Starting VM at {vmx_path}...")

        if not os.path.exists(vmx_path):
            logger.error(f"VMX file not found: {vmx_path}")
            return None

        # Check if running
        cmd_list = [Config.VMRUN_PATH, "list"]
        try:
            result = subprocess.check_output(cmd_list, text=True)
            if vmx_path in result:
                logger.info("VM is already running.")
            else:
                # Start VM
                subprocess.run([Config.VMRUN_PATH, "start", vmx_path, "nogui"], check=True)
                logger.info("VM Started successfully.")
                time.sleep(10) # Wait for boot
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to start VM: {e}")
            return None

        return self._get_vm_ip_workstation()

    def _get_vm_ip_workstation(self):
        """Uses vmrun getGuestIPAddress"""
        logger.info("Waiting for IP address (VMware Tools)...")
        vmx_path = Config.VMX_PATH
        for _ in range(30):
            try:
                cmd = [Config.VMRUN_PATH, "getGuestIPAddress", vmx_path, "-wait"]
                ip = subprocess.check_output(cmd, text=True).strip()
                if ip:
                    logger.info(f"VM IP Found: {ip}")
                    return ip
            except subprocess.CalledProcessError:
                pass
            time.sleep(5)
        
        logger.warning("Could not get IP via vmrun. Returning manual default or failure.")
        return None

    def _deploy_vsphere(self):
        """Clones the template to a new VM (vSphere Code)"""
        logger.info(f"Deploying VM '{Config.TARGET_VM_NAME}' from '{Config.TEMPLATE_NAME}'...")
        
        if not PYVMOMI_AVAILABLE:
            logger.info("[MOCK] VM Deployed successfully.")
            return "192.168.1.105"

        template = self.get_obj([vim.VirtualMachine], Config.TEMPLATE_NAME)
        if not template:
            logger.error("Template not found.")
            raise Exception("Template not found")

        reloc_spec = vim.vm.RelocateSpec(
            datastore=self.get_obj([vim.Datastore], Config.DATASTORE),
            pool=self.get_obj([vim.ResourcePool], "Resources")
        )
        clone_spec = vim.vm.CloneSpec(location=reloc_spec, powerOn=True)

        task = template.Clone(folder=template.parent, name=Config.TARGET_VM_NAME, spec=clone_spec)
        
        while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
            time.sleep(2)
        
        if task.info.state == 'error':
            raise Exception(task.info.error)

        vm = task.info.result
        return self._get_vm_ip_vsphere(vm)

    def _get_vm_ip_vsphere(self, vm):
        """Waits for VMware Tools to report an IP"""
        logger.info("Waiting for IP address...")
        for _ in range(60):
            if vm.guest.net:
                for nic in vm.guest.net:
                    if nic.ipAddress:
                        for ip in nic.ipAddress:
                            if '.' in ip: # IPv4
                                logger.info(f"VM IP Found: {ip}")
                                return ip
            time.sleep(5)
        raise Exception("Timeout waiting for IP")

    def get_obj(self, vimtype, name):
        """Helper to find a vSphere object by name"""
        if not self.si: return None
        content = self.si.RetrieveContent()
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for obj in container.view:
            if obj.name == name: return obj
        return None
