# Wazuh-SOC-Lab
Welcome to my Wazuh SOC Lab repository! 
This project documents my journey of deploying, configuring, and implementing different security tools.

# 📌Overview
This project demonstrates the end-to-end deployment and configuration of different security tools using the open-source Wazuh SIEM/XDR platform, Suricata IDS and Pfsense firewall.

# 🏗️Lab Architecture

The lab is built using VMware VMs and includes the following components:

- **Wazuh Server**: Runs the central Wazuh Manager, Indexer, and Dashboard.
              Collects and correlates logs from agents, Suricata, and pfSense.
- **Windows Endpoint (Windows 11 Pro)**:Runs the Wazuh Agent for system monitoring and log forwarding.
- **Attacker Machine (Kali Linux)**:instance used to simulate threats.
- **pfSense Firewall**:Provides firewall logs.
                 Integrated into Wazuh for anomaly detection.
- **Suricata IDS/IPS**: Monitors network traffic, Sends IDS alerts to Wazuh.

# 🛠️ Wazuh Setup:

[Step 1. Wazuh Server & Agent setup📄 PDF Guide](docs/Wazuh_configuration.pdf)

**Summary:**
- Deploy Wazuh in a virtualized environment using the official OVA package.
- Configure and troubleshoot Wazuh services, then access the Dashboard for monitoring.
- Install and register endpoint agents to collect logs and centralize security visibility.

# 🔌 Implementaion & Configuration:

[Suricata Integration 📄 PDF Guide](docs/Suricata_integration.pdf)

**Summary:**
- Use IDS for passive detection and IPS for active blocking of threats.
- Install and configure Suricata on Windows with Npcap and detection rules.
- Integrate Suricata logs with Wazuh to centralize monitoring and alerts.

[pfSense Integration 📄 PDF Guide](docs/Pfsense_integration.pdf)

**Summary:**
- Deploy pfSense as a virtual firewall in VMware to control and monitor network traffic.
- Configure remote logging and forward pfSense events into Wazuh for analysis.
- Create custom decoders and rules in Wazuh to detect allowed, blocked, and authentication events.

[VirusTotal Integration 📄 PDF Guide](docs/VirusTotal_integration.pdf)

**Summary:**
- Obtain a VirusTotal API key and configure it in the Wazuh Manager for integration.
- Set up Wazuh agents to monitor directories in real time and trigger VirusTotal lookups.
- Enrich alerts with VirusTotal reputation data to speed up triage and threat analysis.

[File integrity monitoring 📄 PDF Guide](docs/File_integrity_monitoring.pdf)

**Summary:**
- Configure Wazuh File Integrity Monitoring (FIM) on Windows by defining directories in the agent’s ossec.conf.
- Enable real-time monitoring with recursion and change reporting for files and subdirectories.
- Validate by creating, modifying, and deleting files to confirm Wazuh generates alerts for each action.

[Logs & Sysmon ingestion 📄 PDF Guide](docs/Logs&Sysmon_ingestion.pdf)

**Summary:**
- Understand Windows Event Logs, key categories, and critical Event IDs for visibility into system and security activities.
- Deploy Sysmon to capture detailed system events and enhance detection of suspicious or attacker behavior.
- Ingest Sysmon logs into Wazuh for centralized monitoring, correlation, and custom rule-based threat detection.

# 🔐 Brute Force Attack: Simulation, Detection & Defense:

[Brute Force Attack Simulation & Wazuh Investigation 📄 PDF Guide](docs/SSH_Brute_Force.pdf)

**Summary:**
- Simulate an SSH brute force attack in a controlled lab using Hydra to generate repeated failed login attempts.
- Detect malicious activity in Wazuh through alerts, Windows Event Logs (e.g., Event ID 4625), and correlation rules highlighting authentication failures.
- Apply defensive measures such as strong passwords, MFA, account lockouts, and Wazuh active responses to prevent and mitigate brute force threats.

**Important:** perform these activities only in your isolated lab environment (the VMs described above) or on systems you own/are authorized to test. Never run brute-force activity against third-party or production systems.

# Conclusion
his SOC home lab project successfully demonstrated how open-source tools can be combined to build a functional security monitoring and detection environment. By integrating Wazuh as the central **SIEM**, **pfSense** as the firewall, **Suricata** as the IDS/IPS, and **Sysmon** for endpoint visibility, the lab replicated key components of a modern SOC. The addition of **VirusTotal** enrichment and **File Integrity Monitoring** further enhanced detection capabilities and contextual analysis.
  
**Note:** This is for educational purposes only. Do not use these techniques for unauthorized activities.


