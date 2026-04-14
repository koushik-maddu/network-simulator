#!/bin/bash

INTERFACE="any"
OUTPUT="../capture/traffic.pcap"

echo "Starting packet capture..."

sudo tcpdump -i $INTERFACE -w $OUTPUT \
"tcp or udp port 53 or port 80 or port 443"