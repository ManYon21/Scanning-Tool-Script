import socket
from datetime import datetime

target = input("Enter Target IP: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print(f"\nScanning {target}")
print(f"Started at: {datetime.now()}\n")

open_ports = []

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)

    result = s.connect_ex((target, port))

    if result == 0:
        open_ports.append(port)

    s.close()

if open_ports:
    print("PORT\tSTATE")
    for port in open_ports:
        print(f"{port}/tcp\topen")
else:
    print("No open ports found")

print(f"\nScan completed at: {datetime.now()}")

