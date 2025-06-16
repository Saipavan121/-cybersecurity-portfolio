import re

def analyze_log(file_path):
    failed_logins = {}
    suspicious_ips = set()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Detect failed login attempts
                if "Failed password" in line:
                    ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                    if ip_match:
                        ip = ip_match.group(1)
                        failed_logins[ip] = failed_logins.get(ip, 0) + 1
                        if failed_logins[ip] >= 5:
                            suspicious_ips.add(ip)

        # Print report
        print("\n📊 Log Analysis Report\n" + "-"*30)
        print("Total IPs with failed logins:", len(failed_logins))
        print("IPs with 5+ failed attempts (suspicious):")
        for ip in suspicious_ips:
            print(f"⚠️  {ip} ({failed_logins[ip]} attempts)")

    except FileNotFoundError:
        print("❌ Log file not found. Check the file path.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    path = input("Enter path to log file (e.g. /var/log/auth.log): ")
    analyze_log(path)
