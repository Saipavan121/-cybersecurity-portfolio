# 🛡️ Cybersecurity Tools – Scripts Collection

A collection of beginner-friendly cybersecurity tools created using Python. Each tool is practical and perfect for learners or job seekers building a portfolio.

---

## 🔍 Project 1: Simple Port Scanner

**📁 File:** `simple-port-scanner.py`  
**🔧 Description:**  
Scans a given IP address to find open ports between 1 and 1024 using Python’s socket module.

**💡 Skills Covered:**
- Networking basics
- TCP port scanning
- Python socket programming

**🚀 How to Run:**
```bash
python simple-port-scanner.py

## 🔐 Project 2: Password Strength Checker

**📁 File:** `password-strength-checker.py`  
**📜 Description:**  
This Python script evaluates the strength of a user-entered password based on key criteria such as:
- Length
- Use of uppercase and lowercase letters
- Inclusion of numbers
- Special characters
- Avoiding common weak passwords (like `password`, `123456`, etc.)

The tool gives feedback and a score (out of 5) to help users create stronger passwords.

**💡 Key Skills:**
- Python input
Enter a password to check: mypass123
Password Strength Score: 2 / 5
⚠️ Suggestions to improve your password:
- Make it at least 12 characters long.
- Use both uppercase and lowercase letters.
- Add special characters (!@#$ etc).


Use Case:
This tool can be used by:

Beginners learning about password security

Developers building login systems

Security awareness workshops

yaml
Copy
Edit


---

## ✅ 📄 Project 3: Log File Analyzer

```markdown
## 📄 Project 3: Log File Analyzer

**📁 File:** `log-analyzer.py`  
**📜 Description:**  
This script analyzes server or system log files (like Linux's `/var/log/auth.log`) to:
- Detect failed SSH login attempts
- Extract and count suspicious IP addresses
- Flag IPs with multiple (e.g. 5+) failed attempts

It helps identify brute-force attempts or unauthorized access patterns.

**💡 Key Skills:**
- File handling in Python
- Regular expressions (regex) to extract IPs
- Dictionary-based counters
- Security event analysis

**🛠️ Features:**
- Works with any `.log` file (custom or real)
- Prints a report of suspicious IPs with failed login attempts
- Easy to modify for other log types

**🚀 How to Run:**
```bash
python log-analyzer.py
When prompted, enter the full path to the log file
(e.g., /var/log/auth.log or a test .log file)
Enter path to log file: sample-log.log

📊 Log Analysis Report
------------------------------
Total IPs with failed logins: 8
IPs with 5+ failed attempts (suspicious):
⚠️  103.82.44.12 (7 attempts)
⚠️  156.11.22.30 (9 attempts)
..
⚠️ Note:

On Windows: create a test .log file with failed login lines

On Linux: use real logs (you may need root permission)

📂 Use Case:
Useful for:

Security monitoring tools

Red team/blue team exercises

Real-time alert systems (if extended)
---

## 🧠 Author

**Name:** Saipavan R  
**GitHub:** [https://github.com/Saipavan-R](https://github.com/Saipavan-R)

---

## ✅ License

This project is licensed under the **MIT License**  
🆓 Free to use, modify, and share for any purpose.
