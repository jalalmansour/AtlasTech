"""
Reconnaissance Module
---------------------
Professional network scanning and service enumeration module.
Requires Nmap binary to be installed and available in PATH.
"""

import sys
import logging
import shutil
import nmap

logger = logging.getLogger("AtlasTech.Recon")

class ReconScanner:
    def __init__(self, target_range):
        self.target_range = target_range
        
        # Verify Nmap Installation
        if not shutil.which("nmap"):
            logger.critical("Nmap binary not found in system PATH.")
            raise EnvironmentError("Nmap is required but not installed.")
            
        try:
            self.nm = nmap.PortScanner()
        except nmap.PortScannerError as e:
            logger.critical(f"Nmap PortScanner instantiation failed: {e}")
            raise

    def scan_network(self):
        """
        Performs a host discovery scan (Ping Scan).
        Returns a list of dictionaries with IP, MAC, and Vendor.
        """
        logger.info(f"Initiating Host Discovery on {self.target_range}...")
        
        try:
            # -sn: Ping Scan - disable port scan
            # -PE: ICMP Echo
            self.nm.scan(hosts=self.target_range, arguments='-sn -PE')
            hosts = []
            
            for host in self.nm.all_hosts():
                if self.nm[host].state() == 'up':
                    mac = self.nm[host]['addresses'].get('mac', 'N/A')
                    vendor = self.nm[host]['vendor'].get(mac, 'Unknown Vendor')
                    
                    host_info = {
                        'ip': host,
                        'mac': mac,
                        'vendor': vendor
                    }
                    hosts.append(host_info)
                    logger.debug(f"Host found: {host} ({vendor})")
                    
            logger.info(f"Scan complete. Found {len(hosts)} live hosts.")
            return hosts
            
        except Exception as e:
            logger.error(f"Network scan failed: {e}")
            return []

    def scan_host(self, ip):
        """
        Detailed service version and OS detection scan on a single host.
        """
        logger.info(f"Starting Deep Scan on {ip}...")
        
        try:
            # -sV: Version detection
            # -O: OS detection
            # -T4: Aggressive timing
            self.nm.scan(ip, arguments='-sV -O -T4')
            
            if ip not in self.nm.all_hosts():
                logger.warning(f"Deep scan returned no data for {ip}.")
                return {}
            
            logger.info(f"Deep Scan finished for {ip}.")
            return self.nm[ip]
            
        except Exception as e:
            logger.error(f"Host scan failed: {e}")
            return {}
