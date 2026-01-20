<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=AtlasTech%20Security%20Framework&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Enterprise%20Penetration%20Testing%20%26%20Infrastructure%20Control&descSize=18&descAlignY=52"/>

<!-- Badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/VMware-Workstation-607078?style=for-the-badge&logo=vmware&logoColor=white"/>
  <img src="https://img.shields.io/badge/Windows_Server-2025-0078D6?style=for-the-badge&logo=windows&logoColor=white"/>
  <img src="https://img.shields.io/badge/CLI-Professional-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white"/>
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

**AtlasTech Security Framework** is an enterprise-grade, CLI-driven penetration testing and infrastructure control platform. Designed for professional security assessments, it provides robust automation for VMware environments, deploys intentionally vulnerable applications, and executes precise attack vectors through a unified terminal interface.

### 🖼️ Architecture & Design

<div align="center">
  <img src="docs/assets/atlastech_architecture_diagram.png" alt="Architecture Diagram" width="800px"/>
  <br>
  <em>Secure Network Segmentation: DMZ vs Legacy Isolation</em>
  <br><br>
  <img src="docs/assets/atlastech_landing_page_mockup.png" alt="Landing Page Mockup" width="800px"/>
  <br>
  <em>Modern Digital Front-End (Next.js)</em>
</div>

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
│                    │   CLI Console   │                          │
│                    │  (root@atlas)   │                          │
│                    └─────────────────┘                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

</div>

---

## ✨ Features

<div align="center">

| 🖥️ VM Control | 🌐 Vulnerable App | ⚔️ Attack Suite | 💻 CLI Console |
|:-------------:|:-----------------:|:---------------:|:------------:|
| Start/Stop VMs | SQL Injection | SSH Brute Force | Logging & Audits |
| Snapshot Mgmt | IDOR Flaws | Password Spray | Robust Error Handling |
| IP Detection | XSS Vectors | Network Scan | Git Sync Integration |
| Script Exec | CSRF Missing | Data Exfil | Automation Ready |

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

- 🔍 Professional Reconnaissance with Nmap Integration
- 🔐 SSH Brute Force (Multi-threaded)
- 💉 Automated SQL Injection Detection
- ⚙️ Automated Logging and Reporting

</details>

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.10+
# VMware Workstation (with vmrun.exe)
# Windows Server 2025 VM
# Nmap (Added to System PATH)
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

**Launch the Interactive Console:**
```bash
python main.py
```

**Automated Deployment:**
```bash
python main.py --deploy
```

<div align="center">
<img src="https://via.placeholder.com/800x450/1a1a3e/00ff00?text=AtlasTech+CLI+Console" alt="CLI Console" width="80%"/>
</div>

---

## 📁 Project Structure

```
AtlasTech/
├── 🎯 main.py                  # CLI Entry Point & Controller
├── ⚙️ config.py                # Configuration settings
├── 📋 requirements.txt         # Python dependencies
│
├── 📂 infrastructure/
│   ├── 🖥️ vm_manager.py       # VMware control via vmrun
│   └── 🔧 provisioner.py      # Windows deployment
│
├── 📂 webapp/rh_crud/          # Vulnerable HR Application
│   ├── 🔐 login.php           # Auth bypass (SQLi)
│   ├── 📄 index.php           # Employee listing
│   └── 🗄️ setup.sql           # Database schema
│
└── 📂 attack_suite/
    ├── 🔍 recon.py            # Reconnaissance Scanner (Nmap)
    └── ⚔️ exploits.py         # Exploitation Modules
```

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

## 📜 License

<div align="center">

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

<img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge"/>

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

</div>
