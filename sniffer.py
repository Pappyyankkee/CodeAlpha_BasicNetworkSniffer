from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    if IP not in packet:
        return

    ip = packet[IP]
    protocol = "Other IP"

    if TCP in packet:
        protocol = "TCP"
    elif UDP in packet:
        protocol = "UDP"
    elif ICMP in packet:
        protocol = "ICMP"

    print("-" * 45)
    print(f"Source IP      : {ip.src}")
    print(f"Destination IP : {ip.dst}")
    print(f"Protocol       : {protocol}")
    print(f"Packet Length  : {len(packet)} bytes")

    if TCP in packet:
        print(f"Source Port    : {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")
    elif UDP in packet:
        print(f"Source Port    : {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")

print("CodeAlpha Basic Network Sniffer")
print("Listening on eth0. Press Ctrl+C to stop.")
sniff(iface="eth0", prn=analyze_packet, store=False)
