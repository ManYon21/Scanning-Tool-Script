# Cybersecurity Tools

A collection of beginner cybersecurity/networking tools built using Python and Bash for learning purposes.

## Tools

* **port_scanner_socket.py** → TCP port scanner using Python `socket`
* **port_scanner_nmap.py** → Port scanner using `python-nmap`
* **host_discovery.py** → Detects local IP, gateway IP, and IP class
* **nse_scanner.sh** → Runs Nmap NSE scripts using Bash

## Requirements

* Python 3
* Nmap
* `python-nmap` module

Install dependency:

```bash
pip install python-nmap --break-system-packages
```

## Run

Python tools:

```bash
python filename.py
```

Bash tool:

```bash
chmod +x nse_scanner.sh
./nse_scanner.sh
