import matplotlib.pyplot as plt
from collections import Counter
from scapy.all import rdpcap, IP

PCAP_FILE = "../capture/traffic.pcap"

def plot_top_talkers():
    packets = rdpcap(PCAP_FILE)

    ips = []

    for pkt in packets:
        if IP in pkt:
            ips.append(pkt[IP].dst)

    top = Counter(ips).most_common(10)

    labels = [x[0] for x in top]
    values = [x[1] for x in top]

    plt.figure(figsize=(10,5))
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.title("Top Destination IPs (Traffic Distribution)")
    plt.show()


if __name__ == "__main__":
    plot_top_talkers()