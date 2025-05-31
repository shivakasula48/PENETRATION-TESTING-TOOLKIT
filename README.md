# Penetration Testing Toolkit

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
```
bash
python3 toolkit.py
```
3 Choose one of the options from the menu:
```
markdown
Penetration Testing Toolkit
1. Port Scanner
2. Brute-Force Attack
3. Subdomain Finder
4. Exit
```

