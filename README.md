# CodeAlpha Basic Network Sniffer

## Project Overview
This project is a basic network sniffer developed in Python
using the Scapy library. It captures network packets and
displays useful information to help understand how data
travels across a network.

## Features
- Captures network packets using Scapy.
- Displays source IP addresses.
- Displays destination IP addresses.
- Identifies IP protocols such as TCP, UDP, and ICMP.
- Displays packet length in bytes.
- Displays source and destination ports for TCP and UDP.
- Allows the user to stop packet capture with Ctrl+C.

## Technologies Used
- Python 3
- Scapy
- Kali Linux

## Requirements
- Python 3
- Scapy
- Kali Linux or a compatible Linux environment

## Installation
Install Scapy on Kali Linux:

```bash
sudo apt install python3-scapy -y
```

## How to Run
1. Open a terminal.
2. Navigate to the project directory.
3. Run the following command:

```bash
sudo python3 sniffer.py
```

The program listens on the eth0 network interface.
Press Ctrl+C to stop capturing packets.

## Project Structure
CodeAlpha_BasicNetworkSniffer/
├── sniffer.py
└── README.md

## Learning Outcomes
- Understanding network packets.
- Learning about IP addresses and protocols.
- Understanding TCP and UDP port numbers.
- Practising Python programming with Scapy.
- Learning basic network traffic analysis.

## Ethical Use
Use this tool only on your own devices and networks
or in environments where you have explicit permission
to capture network traffic.

## Author
Abraham Agboola

## Internship
CodeAlpha Cyber Security Internship
