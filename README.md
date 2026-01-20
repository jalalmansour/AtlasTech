<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=AtlasTech%20Security%20Framework&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Advanced%20Penetration%20Testing%20%26%20Infrastructure%20Control%20Platform&descSize=18&descAlignY=52"/>

<!-- Badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/VMware-Workstation-607078?style=for-the-badge&logo=vmware&logoColor=white"/>
  <img src="https://img.shields.io/badge/Windows_Server-2025-0078D6?style=for-the-badge&logo=windows&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
</p>

<p>
  <img src="https://img.shields.io/github/stars/jalalmansour/AtlasTech?style=social"/>
  <img src="https://img.shields.io/github/forks/jalalmansour/AtlasTech?style=social"/>
  <img src="https://img.shields.io/github/watchers/jalalmansour/AtlasTech?style=social"/>
</p>

<p>
  <a href="#-quick-start"><img src="https://img.shields.io/badge/🚀_Quick_Start-00C853?style=for-the-badge"/></a>
  <a href="#-features"><img src="https://img.shields.io/badge/✨_Features-6366F1?style=for-the-badge"/></a>
  <a href="#-documentation"><img src="https://img.shields.io/badge/📚_Documentation-FF6B6B?style=for-the-badge"/></a>
</p>

---

### 🎯 Automated Security Assessment Lab for Windows Server 2025

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

</div>

## 👨‍💻 Created By

<div align="center">
<table>
<tr>
<td align="center">
<a href="https://github.com/jalalmansour">
<img src="https://github.com/jalalmansour.png" width="120px;" alt="Jalal Mansour" style="border-radius:50%"/>
<br />
<sub><b>Jalal Mansour</b></sub>
</a>
<br />
<a href="https://github.com/jalalmansour" title="GitHub">🔗 GitHub</a>
</td>
</tr>
</table>

**🇲🇦 Moroccan Cybersecurity Professional | Full-Stack Developer | Blue Hat Security Researcher**

</div>

---

## 🌟 Overview

**AtlasTech Security Framework** is a comprehensive, fully automated penetration testing and infrastructure control platform designed for authorized security assessments. It provides complete control over VMware environments, deploys intentionally vulnerable applications for testing, and features a premium dark-themed command center dashboard.

<div align="center">

```
┌─────────────────────────────────────────────────────────────────┐
│                    🛡️ ATLASTECH FRAMEWORK                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│   │   VMware    │───▶│  Vulnerable │───▶│   Attack    │        │
│   │   Control   │    │     App     │    │   Suite     │        │
│   └─────────────┘    └─────────────┘    └─────────────┘        │
│          │                  │                  │                │
│          └──────────────────┴──────────────────┘                │
│                             │                                   │
│                    ┌────────▼────────┐                          │
│                    │    Dashboard    │                          │
│                    │  Command Center │                          │
│                    └─────────────────┘                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

</div>

---

## ✨ Features

<div align="center">

| 🖥️ VM Control | 🌐 Vulnerable App | ⚔️ Attack Suite | 📊 Dashboard |
|:-------------:|:-----------------:|:---------------:|:------------:|
| Start/Stop VMs | SQL Injection | SSH Brute Force | Dark Theme |
| Snapshot Mgmt | IDOR Flaws | Password Spray | VM Control |
| IP Detection | XSS Vectors | Network Scan | Reports |
| Script Exec | CSRF Missing | Data Exfil | Real-time |

</div>

### 🎛️ Core Capabilities

<details>
<summary><b>🖥️ VMware Workstation Control</b></summary>

- ✅ Start/Stop VMs via `vmrun.exe`
- ✅ Automatic IP address detection
- ✅ Snapshot creation & management
- ✅ PowerShell script execution in guest
- ✅ File transfer Host ↔ Guest

</details>

<details>
<summary><b>🌐 Vulnerable HR Application</b></summary>

- 💉 **SQL Injection** in login, add, edit, delete
- 🔓 **IDOR** (Insecure Direct Object Reference)
- 🍪 **Missing CSRF Protection**
- 🔑 **Plaintext Password Storage**
- 📂 **Sensitive Data Exposure** (SSN, Banking)
- 🎨 **Modern Glassmorphism UI**

</details>

<details>
<summary><b>⚔️ Attack Suite</b></summary>

- 🔍 Network reconnaissance with Nmap
- 🔐 SSH brute force attacks
- 💉 Automated SQL injection testing
- 🌊 Password spray attacks
- 📡 ARP spoofing capabilities
- 📸 Automatic screenshot capture

</details>

<details>
<summary><b>📊 Premium Dashboard</b></summary>

- 🌙 Dark theme with gradients
- 📈 Real-time metrics & status
- 🎮 VM control panel
- 🔍 Reconnaissance interface
- 📄 Report generation

</details>

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.10+
# VMware Workstation (with vmrun.exe)
# Windows Server 2025 VM
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/jalalmansour/AtlasTech.git
cd AtlasTech

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure your environment
# Edit config.py with your VMX path and credentials
```

### Usage

<div align="center">

| Command | Description |
|---------|-------------|
| `python automate.py --full` | 🎯 Complete automation workflow |
| `python automate.py --vm-start` | ▶️ Start the target VM |
| `python automate.py --vm-stop` | ⏹️ Stop the target VM |
| `python automate.py --deploy` | 📂 Deploy vulnerable app |
| `python automate.py --dashboard` | 🖥️ Launch command center |
| `python automate.py --git` | 📤 Sync to GitHub |
| `python automate.py --screenshot` | 📸 Capture screenshot |

</div>

---

## 📁 Project Structure

```
AtlasTech/
├── 🎯 automate.py              # Master automation controller
├── ⚙️ config.py                # Configuration settings
├── 📋 requirements.txt         # Python dependencies
│
├── 📂 infrastructure/
│   ├── 🖥️ vm_manager.py       # VMware control via vmrun
│   ├── 🔧 provisioner.py      # Windows deployment
│   └── 📸 screenshot.py       # Auto-capture utility
│
├── 📂 dashboard/
│   └── 🎨 app.py              # Streamlit command center
│
├── 📂 webapp/rh_crud/          # Vulnerable HR Application
│   ├── 🔐 login.php           # Auth bypass (SQLi)
│   ├── ➕ add.php             # Insert injection
│   ├── ✏️ edit.php            # IDOR + SQLi
│   ├── 🗑️ delete.php          # Delete injection
│   ├── 📄 index.php           # Employee listing
│   ├── 🎨 style.css           # Glassmorphism design
│   ├── ⚙️ config.php          # DB credentials
│   └── 🗄️ setup.sql           # Database schema
│
└── 📂 attack_suite/
    ├── 🔍 recon.py            # Network scanning
    ├── ⚔️ exploits.py         # Attack modules
    └── 🌐 network_control.py  # ARP spoofing
```

---

## 🎨 Screenshots

<div align="center">

### 🖥️ Command Center Dashboard

<img src="https://via.placeholder.com/800x450/1a1a3e/ffffff?text=AtlasTech+Command+Center" alt="Dashboard" width="80%"/>

### 🌐 Vulnerable HR Application

<img src="https://via.placeholder.com/800x450/667eea/ffffff?text=HR+Portal+with+Glassmorphism+UI" alt="HR App" width="80%"/>

</div>

---

## ⚠️ Legal Disclaimer

<div align="center">

> **🔒 AUTHORIZED USE ONLY**
>
> This framework is designed for **authorized penetration testing** and **security research** only.
> 
> ✅ Use in controlled lab environments<br>
> ✅ Get written authorization before testing<br>
> ✅ Follow Moroccan Law 07-03 guidelines<br>
> ❌ Never use against systems without permission

</div>

---

## 🛠️ Technologies

<div align="center">

<img src="https://skillicons.dev/icons?i=python,php,mysql,html,css,git,github,windows,linux" />

</div>

<div align="center">

| Category | Technologies |
|:--------:|:------------|
| **Backend** | Python 3.10+, PHP 8.x |
| **Frontend** | Streamlit, HTML5, CSS3 |
| **Database** | MySQL / MariaDB |
| **Virtualization** | VMware Workstation |
| **Target OS** | Windows Server 2025 |
| **Tools** | Nmap, Scapy, Paramiko |

</div>

---

## 📜 License

<div align="center">

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

<img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge"/>

</div>

---

## 🤝 Contributing

<div align="center">

Contributions are welcome! Please feel free to submit a Pull Request.

<a href="https://github.com/jalalmansour/AtlasTech/issues">
  <img src="https://img.shields.io/badge/Report_Bug-FF0000?style=for-the-badge&logo=github"/>
</a>
<a href="https://github.com/jalalmansour/AtlasTech/issues">
  <img src="https://img.shields.io/badge/Request_Feature-00C853?style=for-the-badge&logo=github"/>
</a>

</div>

---

## 📞 Contact

<div align="center">

<a href="https://github.com/jalalmansour">
  <img src="https://img.shields.io/badge/GitHub-jalalmansour-181717?style=for-the-badge&logo=github"/>
</a>

</div>

---

<div align="center">

<!-- Animated Footer -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer"/>

<p>
  <b>⭐ Star this repo if you find it useful!</b>
</p>

<p>
  Made with ❤️ by <a href="https://github.com/jalalmansour"><b>Jalal Mansour</b></a> 🇲🇦
</p>

</div>
