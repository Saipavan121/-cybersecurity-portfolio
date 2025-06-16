import subprocess

def run_nmap_scan(target_ip):
    print(f"[+] Scanning target: {target_ip}")
    command = ["nmap", "-sV", "-T4", target_ip]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("[+] Scan complete. Output:\n")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("[-] Error running Nmap:")
        print(e.stderr)

if __name__ == "__main__":
    target = input("Enter the target IP address or domain: ")
    run_nmap_scan(target)
