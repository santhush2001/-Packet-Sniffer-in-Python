from scapy.all import sniff, conf, get_windows_if_list
from scapy.layers.inet import IP, TCP, UDP, ICMP
import argparse
import platform
import datetime

def setup_windows():
    """Configure Scapy for Windows"""
    conf.use_pcap = True
    conf.use_winpcapy = False
    conf.use_dnet = False

def packet_callback(packet):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        print(f"\n[{timestamp}] Packet: {ip_src} -> {ip_dst}")
        print(f"Protocol: {'TCP' if TCP in packet else 'UDP' if UDP in packet else 'ICMP' if ICMP in packet else 'Other'}")
        
        if TCP in packet:
            print(f"TCP: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f"UDP: {packet[UDP].sport} -> {packet[UDP].dport}")
        
        print("-" * 50)

def main():
    if platform.system() == "Windows":
        setup_windows()
        print("Available interfaces:")
        for iface in get_windows_if_list():
            print(f"{iface['name']} - {iface['description']}")

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="Network interface", default=None)
    parser.add_argument("-f", "--filter", help="BPF filter", default="ip")
    args = parser.parse_args()

    print(f"\nStarting sniffer on {args.interface or 'default interface'}...")
    sniff(iface=args.interface, prn=packet_callback, filter=args.filter, store=0)

if __name__ == "__main__":
    main()
