import nmap
from datetime import datetime

target = input("Enter Target IP: ")
start_port = input("Start Port: ")
end_port = input("End Port: ")

port_range = f"{start_port}-{end_port}"

scanner = nmap.PortScanner()

print(f"\nScanning {target}")
print(f"Started at: {datetime.now()}\n")

scanner.scan(target, port_range)

open_ports = []

for host in scanner.all_hosts():
    for protocol in scanner[host].all_protocols():
        ports = scanner[host][protocol].keys()

        for port in ports:
            state = scanner[host][protocol][port]["state"]

            if state == "open":
                open_ports.append(port)

if open_ports:
    print("PORT\tSTATE")
    for port in sorted(open_ports):
        print(f"{port}/tcp\topen")
else:
    print("No open ports found")

print(f"\nScan completed at: {datetime.now()}")

