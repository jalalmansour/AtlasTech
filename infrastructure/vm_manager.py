"""
VMware Manager
--------------
Handles interaction with vSphere/ESXi to deploy the target infrastructure.
"""

import ssl
import time
import logging
import atexit
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

    def connect(self):
        """Connects to vCenter/ESXi"""
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

    def get_obj(self, vimtype, name):
        """Helper to find a vSphere object by name"""
        if not self.si: return None
        content = self.si.RetrieveContent()
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for obj in container.view:
            if obj.name == name: return obj
        return None

    def deploy_vm(self):
        """Clones the template to a new VM"""
        logger.info(f"Deploying VM '{Config.TARGET_VM_NAME}' from '{Config.TEMPLATE_NAME}'...")
        
        if not PYVMOMI_AVAILABLE:
            logger.info("[MOCK] VM Deployed successfully.")
            logger.info("[MOCK] Waiting for IP...")
            time.sleep(2)
            mock_ip = "192.168.1.105"
            logger.info(f"[MOCK] IP Assigned: {mock_ip}")
            return mock_ip

        template = self.get_obj([vim.VirtualMachine], Config.TEMPLATE_NAME)
        if not template:
            logger.error("Template not found.")
            raise Exception("Template not found")

        # Basic clone spec (simplistic for demo)
        reloc_spec = vim.vm.RelocateSpec(
            datastore=self.get_obj([vim.Datastore], Config.DATASTORE),
            pool=self.get_obj([vim.ResourcePool], "Resources")
        )
        clone_spec = vim.vm.CloneSpec(location=reloc_spec, powerOn=True)

        task = template.Clone(folder=template.parent, name=Config.TARGET_VM_NAME, spec=clone_spec)
        
        # Wait for completion
        while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
            time.sleep(2)
        
        if task.info.state == 'error':
            raise Exception(task.info.error)

        vm = task.info.result
        return self._get_vm_ip(vm)

    def _get_vm_ip(self, vm):
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
