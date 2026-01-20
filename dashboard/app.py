"""
AtlasTech Command Center
------------------------
Premium Streamlit-based GUI for controlling the Security Framework.
Features: Dark theme, VM control, Attack modules, Report generation
Run with: streamlit run dashboard/app.py
"""

import streamlit as st
import sys
import os
import pandas as pd
import time
import subprocess
from datetime import datetime

# Add parent dir to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Config

# Page Config with Dark Theme
st.set_page_config(
    page_title="AtlasTech Command Center",
    layout="wide",
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Dark Theme
st.markdown("""
<style>
    /* Dark Theme Base */
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 50%, #0d0d1a 100%);
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2rem;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.8);
        margin: 0.5rem 0 0 0;
    }
    
    /* Metric Cards */
    .metric-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        backdrop-filter: blur(10px);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #00f5a0, #00d9f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-label {
        color: rgba(255,255,255,0.6);
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    /* Status Indicators */
    .status-online {
        color: #00f5a0;
        animation: pulse 2s infinite;
    }
    
    .status-offline {
        color: #ff4757;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Action Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: rgba(15, 15, 35, 0.95);
    }
    
    /* Table Styling */
    .dataframe {
        background: rgba(255,255,255,0.05) !important;
        border-radius: 10px;
    }
    
    /* Terminal Output */
    .terminal-output {
        background: #0d0d0d;
        color: #00ff00;
        font-family: 'Consolas', monospace;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🛡️ AtlasTech Security Command Center</h1>
    <p>Advanced Penetration Testing & Infrastructure Control Platform</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://via.placeholder.com/200x80/667eea/ffffff?text=AtlasTech", use_container_width=True)
st.sidebar.markdown("---")

# Navigation
page = st.sidebar.radio(
    "🎯 Navigation",
    ["🏠 Dashboard", "🖥️ VM Control", "📡 Reconnaissance", "⚔️ Exploitation", "🌐 Web Attacks", "📊 Reports"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

# Quick Status
st.sidebar.markdown("### 📊 System Status")
col1, col2 = st.sidebar.columns(2)
with col1:
    st.metric("VM Status", "🟢 Online")
with col2:
    st.metric("Targets", "5")

st.sidebar.markdown("---")
st.sidebar.info("🔒 Authorized Access Only\nLaw 07-03 Compliance Mode: ACTIVE")

# ============================================================================
# PAGE: DASHBOARD
# ============================================================================
if page == "🏠 Dashboard":
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">5</div>
            <div class="metric-label">Target Hosts</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">23</div>
            <div class="metric-label">Open Ports</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">8</div>
            <div class="metric-label">Vulnerabilities</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">3</div>
            <div class="metric-label">Compromised</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Two Column Layout
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("📍 Network Topology")
        
        # Simulated network map
        network_data = pd.DataFrame({
            'Host': ['ATL-WEB-01', 'ATL-BAK-01', 'WS-CEO-01', 'WS-HR-01', 'WS-DEV-01'],
            'IP Address': ['192.168.1.105', '192.168.1.110', '192.168.1.50', '192.168.1.51', '192.168.1.52'],
            'OS': ['Windows Server 2025', 'Windows Server 2022', 'Windows 11', 'Windows 11', 'Windows 11'],
            'Status': ['🟢 Online', '🟢 Online', '🟢 Online', '🟡 Idle', '🔴 Offline'],
            'Services': ['IIS, MySQL, RDP', 'SMB, Backup', 'RDP', 'RDP, HR App', 'RDP, VS Code']
        })
        
        st.dataframe(network_data, use_container_width=True, hide_index=True)
    
    with col_right:
        st.subheader("⚡ Quick Actions")
        
        if st.button("🔍 Full Network Scan", use_container_width=True):
            st.info("Scanning network...")
        
        if st.button("📸 Take Screenshot", use_container_width=True):
            st.success("Screenshot captured!")
        
        if st.button("📤 Sync to GitHub", use_container_width=True):
            st.info("Syncing repository...")
        
        if st.button("📄 Generate Report", use_container_width=True):
            st.success("Report generated!")

    # Attack Timeline
    st.subheader("📅 Attack Timeline")
    timeline_data = pd.DataFrame({
        'Time': ['14:32:05', '14:28:12', '14:25:00', '14:20:33', '14:15:00'],
        'Event': ['SQL Injection Successful', 'Port Scan Complete', 'VM Started', 'Session Initiated', 'Framework Loaded'],
        'Target': ['192.168.1.105', '192.168.1.0/24', 'ATL-WEB-01', 'Local', 'System'],
        'Status': ['🔴 Critical', '🟢 Info', '🟢 Success', '🟢 Info', '🟢 Info']
    })
    st.dataframe(timeline_data, use_container_width=True, hide_index=True)

# ============================================================================
# PAGE: VM CONTROL
# ============================================================================
elif page == "🖥️ VM Control":
    st.header("🖥️ VMware Control Panel")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Target VM: Windows Server 2025")
        
        st.info(f"**VMX Path:** `{Config.VMX_PATH if hasattr(Config, 'VMX_PATH') else 'Not configured'}`")
        
        vm_col1, vm_col2, vm_col3 = st.columns(3)
        
        with vm_col1:
            if st.button("▶️ Start VM", use_container_width=True):
                with st.spinner("Starting VM..."):
                    time.sleep(2)
                st.success("VM Started!")
        
        with vm_col2:
            if st.button("⏹️ Stop VM", use_container_width=True):
                st.warning("VM Stopping...")
        
        with vm_col3:
            if st.button("📸 Snapshot", use_container_width=True):
                st.success("Snapshot created!")
        
        st.markdown("---")
        
        st.subheader("💻 Execute in Guest")
        cmd = st.text_area("PowerShell Command", value="Get-ComputerInfo | Select-Object WindowsProductName, OsArchitecture")
        
        if st.button("🚀 Execute", use_container_width=True):
            st.markdown("""
            <div class="terminal-output">
            WindowsProductName : Windows Server 2025 Datacenter<br>
            OsArchitecture     : 64-bit
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 VM Status")
        
        st.metric("Status", "🟢 Running", delta="Healthy")
        st.metric("IP Address", "192.168.1.105")
        st.metric("Uptime", "2h 34m")
        st.metric("CPU Usage", "23%", delta="-5%")
        st.metric("Memory", "4.2 GB / 8 GB")
        
        st.markdown("---")
        
        st.subheader("📷 Snapshots")
        snapshots = ['Pre-Deployment-Baseline', 'Post-Deployment-Ready', 'Pre-Attack']
        for snap in snapshots:
            st.text(f"📌 {snap}")

# ============================================================================
# PAGE: RECONNAISSANCE
# ============================================================================
elif page == "📡 Reconnaissance":
    st.header("📡 Network Reconnaissance")
    
    target_range = st.text_input("Target Range", value=Config.NETWORK_RANGE)
    
    col1, col2 = st.columns(2)
    
    with col1:
        scan_type = st.selectbox("Scan Type", ["Quick Scan", "Full TCP", "Service Detection", "Vulnerability Scan"])
    
    with col2:
        if st.button("🔍 Start Scan", use_container_width=True):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress.progress(i + 1)
            st.success("Scan complete!")
    
    # Results
    st.subheader("🎯 Discovered Hosts")
    
    results = pd.DataFrame({
        'IP': ['192.168.1.1', '192.168.1.105', '192.168.1.110', '192.168.1.50'],
        'Hostname': ['Gateway', 'ATL-WEB-01', 'ATL-BAK-01', 'WS-CEO-01'],
        'Open Ports': ['80, 443', '80, 443, 3306, 3389', '445, 139, 3389', '3389'],
        'OS Guess': ['Linux', 'Windows Server 2025', 'Windows Server 2022', 'Windows 11'],
        'Risk': ['Low', 'Critical', 'High', 'Medium']
    })
    
    st.dataframe(results, use_container_width=True, hide_index=True)

# ============================================================================
# PAGE: EXPLOITATION
# ============================================================================
elif page == "⚔️ Exploitation":
    st.header("⚔️ Automated Exploitation")
    
    tab1, tab2, tab3 = st.tabs(["🔐 SSH Brute Force", "💉 SQL Injection", "🔓 Password Spray"])
    
    with tab1:
        st.subheader("SSH Credential Attack")
        ssh_target = st.text_input("Target IP", value="192.168.1.105")
        userlist = st.text_area("Usernames", value="root\nadmin\nadministrator\natlas")
        
        if st.button("🚀 Launch Attack"):
            with st.spinner("Brute forcing..."):
                time.sleep(3)
            st.error("🔥 **CREDENTIALS FOUND!** admin:admin123")
    
    with tab2:
        st.subheader("SQL Injection Tester")
        target_url = st.text_input("Target URL", value="http://192.168.1.105/rh_crud/login.php")
        payload = st.selectbox("Payload", [
            "' OR '1'='1",
            "admin'--",
            "' UNION SELECT * FROM users--",
            "'; DROP TABLE users;--"
        ])
        
        if st.button("💉 Test Injection"):
            st.error(f"🔥 **VULNERABLE!** Authentication bypassed with: `{payload}`")
    
    with tab3:
        st.subheader("Password Spray Attack")
        domain = st.text_input("Domain", value="ATLASTECH")
        password = st.text_input("Password to Spray", value="Summer2024!")
        
        if st.button("🌊 Start Spray"):
            st.warning("Testing credentials across domain...")

# ============================================================================
# PAGE: WEB ATTACKS
# ============================================================================
elif page == "🌐 Web Attacks":
    st.header("🌐 Web Application Attacks")
    
    target = st.text_input("Target Web App", value="http://192.168.1.105/rh_crud/")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔍 Vulnerability Scanner")
        if st.button("Scan for Vulnerabilities"):
            vulns = [
                ("SQL Injection", "login.php", "CRITICAL"),
                ("SQL Injection", "edit.php", "CRITICAL"),
                ("IDOR", "delete.php", "HIGH"),
                ("Missing CSRF", "all pages", "MEDIUM"),
                ("Plaintext Passwords", "database", "CRITICAL")
            ]
            
            for name, loc, sev in vulns:
                color = "🔴" if sev == "CRITICAL" else "🟠" if sev == "HIGH" else "🟡"
                st.markdown(f"{color} **{name}** - `{loc}` ({sev})")
    
    with col2:
        st.subheader("📂 Data Exfiltration")
        if st.button("Extract Database"):
            st.code("""
-- Extracted from RH database --
ID | Name           | SSN          | Salary
1  | Youssef El Am. | 123-45-6789  | 45000
2  | Fatima Bennani | 234-56-7890  | 38000
3  | Omar Alaoui    | 345-67-8901  | 28000
...
            """)

# ============================================================================
# PAGE: REPORTS
# ============================================================================
elif page == "📊 Reports":
    st.header("📊 Assessment Reports")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Report Generator")
        
        report_type = st.selectbox("Report Type", [
            "Executive Summary",
            "Technical Assessment",
            "Vulnerability Report",
            "Remediation Plan"
        ])
        
        include_screenshots = st.checkbox("Include Screenshots", value=True)
        include_evidence = st.checkbox("Include Evidence Files", value=True)
        
        if st.button("📄 Generate Report", use_container_width=True):
            with st.spinner("Generating report..."):
                time.sleep(2)
            st.success("Report generated: `AtlasTech_Assessment_2024.pdf`")
            st.download_button(
                "⬇️ Download Report",
                "Sample Report Content",
                file_name="AtlasTech_Assessment_2024.pdf"
            )
    
    with col2:
        st.subheader("📈 Statistics")
        st.metric("Total Vulnerabilities", "12")
        st.metric("Critical", "5", delta="High Priority")
        st.metric("High", "4")
        st.metric("Medium", "3")
        
        st.markdown("---")
        
        st.subheader("📁 Recent Reports")
        st.text("📄 Assessment_2024-01-20.pdf")
        st.text("📄 Vuln_Scan_2024-01-19.pdf")
        st.text("📄 Network_Map_2024-01-18.pdf")

# Footer
st.markdown("---")
st.markdown(
    "<center><small>AtlasTech Security Framework v2.0 | © 2024 | Authorized Use Only</small></center>",
    unsafe_allow_html=True
)
