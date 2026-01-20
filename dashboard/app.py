import streamlit as st
import pandas as pd
import time
import os
import sys
from datetime import datetime

# Set page config for a premium look
st.set_page_config(
    page_title="AtlasTech | Security Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Glassmorphism and Premium Dark Theme
st.markdown("""
<style>
    .reportview-container {
        background: #0e1117;
    }
    .main {
        background: linear-gradient(135deg, #0e1117 0%, #1a1a2e 100%);
        color: #ffffff;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    .stSidebar {
        background: rgba(10, 10, 20, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    h1, h2, h3 {
        color: #00d4ff;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00d4ff 0%, #0072ff 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 212, 255, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/200x100/1a1a3e/00d4ff?text=ATLASTECH", use_container_width=True)
    st.title("🛡️ Ops Center")
    st.markdown("---")
    menu = st.radio("Navigation", ["Dashboard", "Network Recon", "Exploitation", "VM Control", "Logs"])
    st.markdown("---")
    st.status("System Status: Operational", state="running")
    st.info("Authorized Personnel Only")

# Header
st.title("AtlasTech Security Framework")
st.markdown("#### Enterprise-Grade Security Assessment & Orchestration")

if menu == "Dashboard":
    # Top Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Hosts", "25", "2 New")
    with col2:
        st.metric("Vulnerabilities", "14", "3 Critical")
    with col3:
        st.metric("Active Sessions", "3", "0")
    with col4:
        st.metric("Network Traffic", "1.2 GB/s", "↑ 15%")

    st.markdown("---")

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("🛰️ Real-Time Network Activity")
        # Dummy data for chart
        chart_data = pd.DataFrame({
            'time': pd.date_range(start='2026-01-20', periods=20, freq='S'),
            'packets': [100, 120, 150, 140, 180, 210, 200, 250, 300, 280, 260, 240, 290, 350, 400, 380, 360, 410, 450, 430]
        })
        st.line_chart(chart_data.set_index('time'))

        st.subheader("🎯 Active Targets")
        targets_df = pd.DataFrame([
            {"IP": "192.168.1.10", "Hostname": "ATL-WEB-01", "Status": "Compromised", "Vulnerability": "SQL Injection"},
            {"IP": "192.168.1.15", "Hostname": "ATL-BAK-01", "Status": "Scanning", "Vulnerability": "N/A"},
            {"IP": "192.168.1.5", "Hostname": "Router", "Status": "Protected", "Vulnerability": "Weak Auth"},
        ])
        st.table(targets_df)

    with col_right:
        st.subheader("⚡ Quick Actions")
        if st.button("🚀 Start Full Network Scan"):
            with st.spinner("Scanning..."):
                time.sleep(2)
                st.success("Scan Complete!")
        
        if st.button("⚔️ Deploy SQLi Payload"):
            st.warning("Payload deployed to ATL-WEB-01")

        st.markdown("---")
        st.subheader("🛡️ CVE Mappings")
        st.code("""
CVE-2021-21703: PHP RCE
CVE-2024-XXXXX: SQLi Bypass
CVE-2023-45678: Weak SSH
        """, language="text")

elif menu == "VM Control":
    st.subheader("🖥️ VMware Infrastructure Control")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Target VM:** Windows Server 2025")
        st.write("**Status:** Powered On")
    with col2:
        if st.button("🔴 Power Off"): st.error("Action denied: Demo mode")
        if st.button("🔄 Reboot"): st.info("Rebooting VM...")

elif menu == "Logs":
    st.subheader("📜 System Logs")
    log_file = "logs/atlastech_20260120.log"
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            st.text_area("Live Feed", f.read(), height=400)
    else:
        st.warning("Log file not found.")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>AtlasTech Security Solutions © 2026 | Authorized Use Only</div>", unsafe_allow_html=True)
