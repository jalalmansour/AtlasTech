# SECURITY AUDIT: AtlasTech Solutions

## 1. Executive Summary
This document details the security transformation of AtlasTech Solutions' infrastructure. We have moved from a flat, insecure network architecture hosting a vulnerable legacy PHP application to a segmented, containerized environment hosting a secure Next.js application with strict RBAC.

## 2. Infrastructure Architecture

### 2.1 Current State (Legacy/Vulnerable)
*   **Architecture:** Flat Network.
*   **Risks:** Lateral movement is trivial. If the Web App is compromised, the DB and all other internal assets are accessible.
*   **Components:** Legacy PHP App + MySQL (same host/network).

```mermaid
graph TD
    User[Attacker/User] -->|HTTP| Switch
    Switch -->|All Traffic| PHP_App[Legacy PHP App (Vulnerable)]
    PHP_App -->|Direct Access| MySQL[Legacy DB]
    PHP_App -.->|Lateral Movement| Admin_PC[Internal Admin PC]
    style PHP_App fill:#ff9999,stroke:#333,stroke-width:2px
```

### 2.2 Target State (Secure/Segmented)
*   **Architecture:** Docker-based Network Segmentation (DMZ pattern).
*   **Improvements:**
    *   **Frontend Network (DMZ):** Public facing.
    *   **Backend Network:** Isolated application logic.
    *   **DB Network:** Strictly isolated database, only accessible by App container.

```mermaid
graph TD
    User[User] -->|HTTPS/443| NextApp[Next.js App (Secure)]
    
    subgraph "DMZ / Frontend Net"
        NextApp
    end

    subgraph "Backend Net (Internal)"
        NextApp -->|Prisma/TCP| Postgres[PostgreSQL DB]
    end

    subgraph "Legacy Net (Isolated)"
        LegacyApp[Legacy PHP App] --> LegacyDB[Legacy MySQL]
    end

    User -.->|HTTP/8080| LegacyApp
    
    %% Firewall Rules Simulation
    NextApp --x|Blocked| LegacyApp
    Postgres --x|Blocked| User
```

## 3. Vulnerability Analysis & Mitigation

| Vulnerability Category | Legacy State (PHP App) | Secure State (Next.js App) | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **SQL Injection** | High risk. Raw SQL queries used. | **Eliminated.** | Used **Prisma ORM** which parameterizes all queries by default. |
| **Broken Access Control** | None. Horizontal privilege escalation possible. | **Strict RBAC.** | Implemented **NextAuth.js** with Middleware. `/dashboard/hr` is strictly restricted to `HR` and `CEO` roles. |
| **XSS (Cross-Site Scripting)** | High risk. Unsanitized inputs. | **Mitigated.** | **React** automatically escapes content by default. Used strict typing. |
| **Network Security** | Flat network. | **Segmented.** | Docker Networks isolate the Database. Even if the App container is compromised, the attacker cannot easily scan the host network. |
| **Data Exposure** | Plaintext handling possible. | **Encrypted.** | Passwords hashed using `bcrypt` (simulated logic implemented in Auth). |

## 4. DevOps Strategy
A CI/CD pipeline is recommended to ensure continued security.

### .github/workflows/ci.yml
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Use Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20.x'
    - run: npm ci
    - run: npm run lint
    - run: npm run build
```
