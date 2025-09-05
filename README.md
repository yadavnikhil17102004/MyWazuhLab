# Wazuh-SOC-Lab
Welcome to my Wazuh SOC Lab repository!
This project documents my journey of deploying, configuring, and mastering a Security Operations Center (SOC) using the open-source Wazuh SIEM/XDR platform.

# 📌Overview
This project demonstrates the end-to-end deployment and configuration of a comprehensive Security Operations Center (SOC) using the open-source Wazuh SIEM/XDR platform.
The objective is to build a multi-machine virtual lab that simulates and defends against real-world security threats. 

# 🏗️Lab Architecture

The lab is built using VMware VMs and includes the following components:

- **Wazuh Server**: Runs the central Wazuh Manager, Indexer, and Dashboard.
              Collects and correlates logs from agents, Suricata, and pfSense.
- **Windows Endpoint (Windows 11 Pro)**:Runs the Wazuh Agent for system monitoring and log forwarding.
- **Attacker Machine (Kali Linux)**:instance used to simulate threats.
- **pfSense Firewall**:Provides firewall logs.
                 Integrated into Wazuh for anomaly detection.
- **Suricata IDS/IPS**: Monitors network traffic, Sends IDS alerts to Wazuh.

# 🛠️ Wazuh Setup

[Step 1. Wazuh Server & Agent setup📄 PDF Guide](docs/Wazuh Setup & Configuration.pdf)

**Summary:**
- Deploy Wazuh in a virtualized environment using the official OVA package.
- Configure and troubleshoot Wazuh services, then access the Dashboard for monitoring.
- Install and register endpoint agents to collect logs and centralize security visibility.
