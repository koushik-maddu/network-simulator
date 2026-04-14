from scapy.all import rdpcap, IP, TCP, UDP, DNS, DNSQR
from collections import defaultdict

PCAP_FILE = "../capture/traffic.pcap"

flows = defaultdict(int)
dns_queries = []

def analyze():
    packets = rdpcap(PCAP_FILE)

    for pkt in packets:

        # TCP flows
        if IP in pkt and TCP in pkt:
            key = (pkt[IP].src, pkt[IP].dst, pkt[TCP].dport)
            flows[key] += 1

        # DNS queries
        if pkt.haslayer(DNSQR):
            qname = pkt[DNSQR].qname.decode(errors="ignore")
            dns_queries.append(qname)

    print("\n===== TCP FLOWS =====")
    for k, v in list(flows.items())[:10]:
        print(f"{k} -> {v} packets")

    print("\n===== DNS QUERIES =====")
    for d in set(dns_queries):
        print(d)


if __name__ == "__main__":
    analyze()