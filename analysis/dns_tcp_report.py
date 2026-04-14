from scapy.all import rdpcap, DNSQR, TCP, IP
from collections import defaultdict

PCAP_FILE = "../capture/traffic.pcap"

def generate_report():
    packets = rdpcap(PCAP_FILE)

    dns_count = defaultdict(int)
    tcp_ports = defaultdict(int)

    for pkt in packets:

        if pkt.haslayer(DNSQR):
            domain = pkt[DNSQR].qname.decode(errors="ignore")
            dns_count[domain] += 1

        if IP in pkt and TCP in pkt:
            tcp_ports[pkt[TCP].dport] += 1

    print("\n===== DNS ACTIVITY =====")
    for k, v in sorted(dns_count.items(), key=lambda x: x[1], reverse=True):
        print(k, v)

    print("\n===== TCP PORT USAGE =====")
    for k, v in sorted(tcp_ports.items(), key=lambda x: x[1], reverse=True):
        print(f"Port {k}: {v} packets")


if __name__ == "__main__":
    generate_report()