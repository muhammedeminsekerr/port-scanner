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
    # TODO: tek bir portu tara, aciksa listeye ekle
    pass

def scan(target, ports):
    # TODO: her port icin bir thread baslat, hepsini bekle
    pass

if __name__ == "__main__":
    # TODO: ornek tarama
    pass
