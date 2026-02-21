# 🌌 MyWazuhLab: Enterprise SOC Intelligence Lab

> **State-of-the-Art Detection Engineering & Automated Threat Hunting**

---

## 🏛️ System Architecture

```mermaid
graph TD
    subgraph "Perimeter Control"
        pfSense["pfSense Firewall"] --> |"Inbound/Outbound Traffic"| WAN["Public Internet"]
    end

    subgraph "Internal Intelligence"
        Suricata["Suricata IDS"] --> |"EVE JSON Logs"| WazuhMgr["Wazuh Manager (SIEM)"]
        WazuhMgr --> |"Analysis & Alerting"| Indexer["Wazuh Indexer / Dashboard"]
    end

    subgraph "Endpoints & Telemetry"
        WinAgent["Windows Endpoint"] --> |"Sysmon + Wazuh Agent"| WazuhMgr
        VT["VirusTotal API"] <--> |"Threat Enrichment"| WazuhMgr
    end

    pfSense -.-> |"Syslog"| WazuhMgr
```

---

## 🧬 Tactical Workflow: Detection-as-Code

This lab follows a continuous improvement cycle for security operations.

```mermaid
sequenceDiagram
    participant AD as Attack Simulation (Python)
    participant EP as Windows Endpoint (Sysmon)
    participant WZ as Wazuh SIEM
    participant Git as GitHub (Ruleset)

    AD->>EP: Trigger Offensive TTP (e.g. Discovery)
    EP->>WZ: Ship High-Fidelity Logs
    Git->>WZ: Deploy Custom Rules
    WZ->>WZ: Pattern Match & Alert
    Note right of WZ: SOC Alert Triggered!
```

---

## ⚡ What is this?

A fully weaponized, virtualized Security Operations Center (SOC) environment built to simulate, detect, and neutralize advanced persistent threats. This lab integrates an open-source XDR (Wazuh) with network-level deep packet inspection (Suricata) and firewalling (pfSense) to create a comprehensive perimeter of absolute visibility.

**Why?** Because reading about security isn't enough. You have to build the panopticon to understand how to break it (or defend it).

## 🏗 Architecture Blueprint

The environment operates entirely within isolated VMware infrastructure to emulate an enterprise corporate network under active simulation.

1. **Wazuh Central Hub:** The brain. Manages the Indexer, Server, and Dashboard. Ingests and correlates all endpoint and network telemetry.
2. **Windows 11 Client:** The sacrificial endpoint. Instrumented with Wazuh Agent and Sysmon for ring-0 telemetry.
3. **Kali Linux:** The aggressor. Dedicated attack infrastructure used to fire exploits and brute-force campaigns into the perimeter.
4. **pfSense Edge Firewall:** The gatekeeper. Controls ingress/egress and forwards structural traffic anomalies directly into Wazuh.
5. **Suricata IDS/IPS:** The wire-tap. Passively monitors deep packet traffic and fires high-fidelity signatures to the centralized SIEM.

## 📡 Operational Capabilities

This SOC implementation isn't just a logging sink; it actively leverages multiple threat intelligence streams to formulate a layered defense.

### 1. File Integrity & Reputation (VirusTotal)

- Integrates the VirusTotal API directly into the Wazuh Manager to automatically scan suspected binaries dropped on the Windows endpoint.
- FIM (File Integrity Monitoring) watches critical OS directories and triggers alerts the exact millisecond a file is mutated.

### 2. Deep Windows Telemetry (Sysmon)

- Basic Windows Event Logs aren't enough. Sysmon is deployed to track exact process creation trees, network connections spawned by executables, and file creation hashes.
- Sysmon logs are pipelined directly into Wazuh for centralized behavioral analysis.

### 3. Attack Simulation: SSH Brute Force Campaign

- Simulated sustained Hydra-based brute-force attacks from the Kali aggressor node against the internal infrastructure.
- Validated real-time alert generation via `Event ID 4625` (Failed Logon) and Wazuh native correlation engines.
- Actively defended using Active Response automation to outright ban the attacking IPs from the network layer.

## 📖 Deep-Dive Documentation

Every single phase of this infrastructure has been meticulously documented. If you want to replicate this setup, the operational manuals are included here:

- [Wazuh Core Configuration](docs/Wazuh_configuration.md)
- [Suricata IDS Integration](docs/Suricata_integration.md)
- [pfSense Edge Configuration](docs/Pfsense_integration.md)
- [VirusTotal API Enrichment](docs/VirusTotal_integration.md)
- [FIM (File Integrity Monitoring)](docs/File_integrity_monitoring.md)
- [Sysmon & Telemetry Pipeline](docs/Logs_Sysmon_ingestion.md)
- [Active Threat: Brute Force Simulation](docs/SSH_Brute_Force.md)

---

## 🚀 Phase 2: Automation & Detection Engineering

The lab has been evolved into an automated "Detection Engineering" platform.

### 1. Infrastructure-as-Code (Ansible)

- **Automatic Deployment:** Use the `ansible/` playbooks to deploy Wazuh agents and Sysmon configurations across new endpoints with a single command.
- **Config-as-Code:** Telemetry settings are versioned in [ansible/playbook.yml](ansible/playbook.yml).

### 2. Detection-as-Code (Wazuh Rules)

- **Custom Ruleset:** Custom high-fidelity detections are stored in [rules/wazuh/](rules/wazuh/).
- **Version Control:** Manage and audit your detections via Git, following industry best practices.

### 3. Automated Attack Simulation

- **Trigger Alerts:** Use the Python suite in [simulations/](simulations/) to programmatically trigger the custom detection rules and validate your SIEM pipeline.

```bash
# Example: Triggering a detection baseline
python3 simulations/trigger_alerts.py
```

## ⚠️ Engagement Rules

This environment is a controlled detonation chamber. Ensure all attack simulations map explicitly to authorized infrastructure.

---

_Built to detect. Engineered to secure._
