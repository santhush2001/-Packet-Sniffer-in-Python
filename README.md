
# Python Packet Sniffer

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A cross-platform packet sniffer built with Scapy that works on Windows, Linux, and macOS.

## Features

- 🖥️ **Cross-platform** support (Windows, Linux, macOS)
- 🔍 **Multiple protocol** analysis (IP, TCP, UDP, ICMP)
- 🎚️ **BPF filtering** support (like Wireshark filters)
- 📊 **Real-time** packet inspection
- 🛠️ **Easy-to-use** command line interface

## Installation

1. **Install prerequisites**:

   ```bash
   # On Windows (install Npcap)
   https://npcap.com/#download

   # On Linux/macOS
   sudo apt-get install tcpdump  # Debian/Ubuntu
   brew install libpcap          # macOS
