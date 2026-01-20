"""
Reconnaissance Module
---------------------
Performs network scanning and service enumeration.
"""

import sys
import logging
import json

# Handle python-nmap dependency
try:
    import nmap
    NMAP_AVAILABLE = True
except ImportError:
    NMAP_AVAILABLE = False

logger = logging.getLogger("AtlasTech.Recon")

class ReconScanner:
    def __init__(self, target_range):
        self.target_range = target_range
        self.nm = nmap.PortScanner() if NMAP_AVAILABLE else None

    def scan_network(self):
        """Performs a ping scan to find live hosts"""
        logger.info(f"Scanning network: {self.target_range}")
        
        if not NMAP_AVAILABLE:
            logger.warning("python-nmap not installed. Returning MOCK data.")
            return self._get_mock_scan()

        try:
            # -sn: Ping Scan - disable port scan
            self.nm.scan(hosts=self.target_range, arguments='-sn')
            hosts = []
            for host in self.nm.all_hosts():
                if self.nm[host].state() == 'up':
                    hosts.append({
                        'ip': host,
                        'mac': self.nm[host]['addresses'].get('mac', 'Unknown'),
                        'vendor': self.nm[host]['vendor'].get(self.nm[host]['addresses'].get('mac', ''), '')
                    })
            return hosts
        except Exception as e:
            logger.error(f"Scan failed: {e}")
            return []

    def scan_host(self, ip):
        """Detailed port scan of a single host"""
        logger.info(f"Deep scanning {ip}...")
        
        if not NMAP_AVAILABLE:
            return self._get_mock_host_scan(ip)

        try:
            self.nm.scan(ip, arguments='-sV -sC -p 22,80,443,3306')
            if ip not in self.nm.all_hosts():
                return {}
            
            return self.nm[ip]
        except Exception as e:
            logger.error(f"Host scan failed: {e}")
            return {}

    def _get_mock_scan(self):
        return [
            {'ip': '192.168.1.1', 'mac': 'AA:BB:CC:DD:EE:01', 'vendor': 'Cisco'},
            {'ip': '192.168.1.100', 'mac': 'AA:BB:CC:DD:EE:02', 'vendor': 'VMware'},
            {'ip': '192.168.1.105', 'mac': 'AA:BB:CC:DD:EE:03', 'vendor': 'VMware (Target)'},
        ]

    def _get_mock_host_scan(self, ip):
        return {
            'tcp': {
                22: {'state': 'open', 'name': 'ssh', 'product': 'OpenSSH', 'version': '7.2p2'},
                80: {'state': 'open', 'name': 'http', 'product': 'Apache', 'version': '2.4.18'},
                3306: {'state': 'open', 'name': 'mysql', 'product': 'MariaDB', 'version': '10.0.38'}
            }
        }
