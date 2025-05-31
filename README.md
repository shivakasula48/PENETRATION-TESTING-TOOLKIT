# Penetration Testing Toolkit

*COMPANY*: CODTECH IT SOLUTIONS

*NAME* : KASULA SHIVA

*INTERN ID* : CT08DM748

*DOMAIN* : Cyber Security & Ethical Hacking

*DURATION* : 8WEEKS

*MENTOR* : NEELA SANTOSH




A Python-based command-line toolkit for performing basic penetration testing tasks, including:

* Port Scanning

* FTP Brute-Force Attacks

* Subdomain Enumeration

This tool is designed for ethical hacking exercises, cybersecurity training, and learning how various attacks work at a low level using Python.


  
---

## 🧭 Overview

This project provides a beginner-friendly but effective way to understand the fundamental stages of penetration testing: reconnaissance, scanning, and brute-force access attempts. Built entirely in Python, it is intended for use in controlled environments like CTFs, local VMs (e.g., Metasploitable), and educational labs (e.g., DVWA, OWASP Juice Shop).




## Features

1. **Port Scanner**
   - Scans a range of ports on a target IP or domain to identify open ports.
   - Multithreaded for faster results.

2. **Brute-Force Attack**
   - Performs a brute-force attack on FTP servers.
   - Uses a custom password list to test login credentials.

3. **Subdomain Finder**
   - Discovers subdomains for a given domain.
   - Utilizes a predefined list of common subdomains.
  
4. **Menu-Driven Interface**
   - Simple and interactive menu lets users easily select tools and input targets.
  
5. **Extensible Design**
   - Modular code structure allows for easy addition of future penetration testing components.

---

## How It Works

Each module is self-contained and follows a logical sequence:

1. **Port Scanner**
    * Uses the `socket` module to attempt TCP connections to ports.

    * Employs `ThreadPoolExecutor` for multi-threaded scanning.

    * Displays open ports only.

2. FTP Brute-Forcer
    * Uses the `ftplib` library to attempt login using credentials from a password file.

    * Stops immediately once valid credentials are found.

    * Handles connection failures and invalid inputs gracefully.

3. Subdomain Finder
    * Uses `dnspython` to resolve subdomains.

    * Attempts to resolve common subdomain prefixes (e.g., `www`, `mail`, `admin`).

    * Displays all successfully resolved domains.

---

## Requirements

Make sure you have Python 3.6 or later installed.

Install dependencies using pip:
```bash
pip install dnspython
```

No additional libraries are required.

---

## Usage

1 Clone this repository:

```bash

git clone https://github.com/your-username/penetration_testing_toolkit.git
cd penetration_testing_toolkit
```
2 Run the toolkit:
```bash
python3 toolkit.py
```
3 Choose one of the options from the menu:
```markdown
Penetration Testing Toolkit
1. Port Scanner
2. Brute-Force Attack
3. Subdomain Finder
4. Exit
```

## Sample Output

### 🔍 Port Scanner

```sql
Enter target IP or domain: 192.168.1.1
Enter start port: 20
Enter end port: 100

Scanning 192.168.1.1 for open ports...

Port 21 is OPEN
Port 22 is OPEN

Open Ports Summary:
- Port 21
- Port 22
```

![Image](https://github.com/user-attachments/assets/a9edb5e4-5e95-4b87-b0c3-6c7205bac7b9)

### 🔐 FTP Brute-Force

```yaml
Enter target IP: 192.168.1.1
Enter username: admin
Enter path to password file: passwords.txt

Trying admin...
Trying root...
Trying password123...
Success! Password found: password123
```

![Image](https://github.com/user-attachments/assets/27f183b6-229c-4a14-a407-83755b0f0bb8)

### 🌐 Subdomain Finder
```yaml
Enter domain: example.com

Finding subdomains for example.com...

Found subdomain: www.example.com
Found subdomain: mail.example.com
Found subdomain: admin.example.com

Found Subdomains Summary:
- www.example.com
- mail.example.com
- admin.example.com
```

![Image](https://github.com/user-attachments/assets/18bb2771-b9b6-4106-8457-89bd3de0afb3)



##  Use Cases

  * Educational Labs: Practice attacks on DVWA, Metasploitable, OWASP Juice Shop, or custom vulnerable apps.

  * Security Training: Understand real-world enumeration and brute-force attack scenarios.

  * CTFs & Practice: Rapid testing of open ports and login attempts during Capture The Flag events.

  * Custom Expansion: Serve as a base framework to integrate more advanced tools (e.g., HTTP fuzzing, service detection, etc.).

⚠️ Important: Use this toolkit only on systems and networks you have explicit permission to test. Unauthorized usage may violate laws and ethical standards.




# License

This project is open-source and free to use by anyone for personal or educational purposes.  
Feel free to modify, distribute, and use the code as long as proper credit is given to the original author, **Kasula Shiva**.



