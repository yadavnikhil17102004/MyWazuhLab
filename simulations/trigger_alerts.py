import subprocess
import os

def run_simulation(name, command):
    print(f"[!] Running Simulation: {name}")
    try:
        # We use shell=True for convenience in simulating command-line behavior
        # In a real environment, you'd use absolute paths and proper argument lists
        subprocess.run(command, shell=True, capture_output=True, text=True)
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    print("=== MyWazuhLab: Attack Simulation Suite ===")
    
    # Discovery Simulation
    run_simulation("Discovery - whoami", "whoami")
    run_simulation("Discovery - net user", "net user")
    
    # Persistence Simulation (Simulated via reg add, if on Windows)
    # Note: This is safe in a lab VM, but use caution
    if os.name == 'nt':
        run_simulation("Persistence - Registry Run Key", 'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v LabPersistence /t REG_SZ /d "C:\\Windows\\System32\\calc.exe" /f')
    else:
        print("[*] Skipping Windows-specific persistence simulations.")
        
    print("\n[+] Simulation run complete. Check the Wazuh Dashboard for alerts.")
