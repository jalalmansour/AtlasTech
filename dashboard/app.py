"""
AtlasTech Command Center
------------------------
Streamlit-based GUI for controlling the Security Framework.
Run with: streamlit run dashboard/app.py
"""

import streamlit as st
import sys
import os
import pandas as pd
import time

# Add parent dir to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Config
from attack_suite.recon import ReconScanner
from attack_suite.network_control import ArpSpoofer
from attack_suite.exploits import SSHBruteForcer, SQLInjector

st.set_page_config(page_title="AtlasTech Security Framework", layout="wide", page_icon="🔐")

st.title("🛡️ AtlasTech Security Assessment Framework")
st.markdown(f"**Target Environment**: `{Config.NETWORK_RANGE}` | **Gateway**: `{Config.GATEWAY_IP}`")

# Sidebar - Controls
st.sidebar.header("Mission Control")
action = st.sidebar.radio("Select Operation", ["Reconnaissance", "Network Control", "Exploitation", "Report Generation"])

if action == "Reconnaissance":
    st.header("📡 Network Reconnaissance")
    if st.button("Start Network Scan"):
        st.info("Scanning network... Please wait.")
        scanner = ReconScanner(Config.NETWORK_RANGE)
        hosts = scanner.scan_network()
        
        if hosts:
            st.success(f"Found {len(hosts)} live hosts.")
            df = pd.DataFrame(hosts)
            st.dataframe(df, use_container_width=True)
            
            # Host Details
            target = st.selectbox("Select Target for Deep Scan", [h['ip'] for h in hosts])
            if st.button(f"Scan {target}"):
                details = scanner.scan_host(target)
                st.json(details)
        else:
            st.warning("No hosts found (or Nmap unavailable).")

elif action == "Network Control":
    st.header("🕸️ Network Traffic Control")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("ARP Spoofing (MITM)")
        target_ip = st.text_input("Target IP", value="192.168.1.105")
        if st.button("Start Spoofing"):
            st.warning(f"⚠️ Spoofing started against {target_ip}. Traffic is being intercepted.")
            # In a real app, this would run in a background thread and update status
            # For this MVP, we simulate or just trigger the class
            spoofer = ArpSpoofer(target_ip, Config.GATEWAY_IP)
            spoofer.start()
            st.success("Spoofer running...")
    
    with col2:
        st.subheader("Traffic Monitor")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Wireshark_Icon.png/64px-Wireshark_Icon.png")
        st.metric(label="Packets Captured", value="1,240", delta="120/s")

elif action == "Exploitation":
    st.header("⚔️ Automated Exploitation")
    
    tab1, tab2 = st.tabs(["SSH Brute Force", "Web SQL Injection"])
    
    with tab1:
        target_ssh = st.text_input("SSH Target", value="192.168.1.105")
        user_list = st.text_area("Users (comma sep)", value="root,admin,atlas,user").split(',')
        if st.button("Launch Brute Force"):
            bf = SSHBruteForcer(target_ssh, [u.strip() for u in user_list], Config.WORDLIST_PATH)
            with st.spinner("Cracking..."):
                creds = bf.run()
            if creds:
                st.error(f"🔥 COMPROMISED! Credentials: {creds}")
            else:
                st.info("No credentials found.")

    with tab2:
        target_url = st.text_input("Target URL", value=f"http://{Config.VM_HOST}/hr/login.php")
        if st.button("Test SQL Injection"):
            injector = SQLInjector(target_url)
            vuln, payload = injector.test_bypass()
            if vuln:
                st.error(f"🔥 VULNERABLE! Bypass Payload: `{payload}`")
            else:
                st.success("Target appears secure (or WAF blocking).")

elif action == "Report Generation":
    st.header("📄 Engagement Report")
    st.write("Generating PDF report based on findings...")
    st.progress(100)
    st.success("Report generated: `AtlasTech_Assessment_Report_2024.pdf`")
    st.download_button("Download Report", "Mock Report Data", file_name="report.txt")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Authorized for AtlasTech Solutions Lab Only.\nLaw 07-03 Compliance Mode: ACTIVE")
