import socket

def scan_ports(target_ip, start=1, end=1024):
    print(f"[+] Scanning {target_ip} from port {start} to {end}...\n")

    open_ports = []
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"[+] Port {port} is OPEN")

        s.close()

    if not open_ports:
        print("[-] No open ports found.")
    else:
        print(f"\n[✔] Open ports: {open_ports}")

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    scan_ports(target)
