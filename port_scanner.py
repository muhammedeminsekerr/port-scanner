import socket
import threading
from datetime import datetime

# yaygin portlar ve uzerinde calisan servisler
COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
}

def scan_port(target, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        service = COMMON_PORTS.get(port, "Bilinmiyor")
        open_ports.append((port, service))
    sock.close()

def scan(target, ports):
    open_ports = []
    threads = []

    print(f"[*] {target} taraniyor...")
    start = datetime.now()

    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = (datetime.now() - start).total_seconds()
    print(f"[*] Tarama {elapsed:.2f} saniyede bitti\n")

    for port, service in sorted(open_ports):
        print(f"[+] Port {port} ACIK - {service}")

    return open_ports

if __name__ == "__main__":
    target = "scanme.nmap.org"  # Nmap'in test için acik biraktigi sunucu
    scan(target, list(COMMON_PORTS.keys()))