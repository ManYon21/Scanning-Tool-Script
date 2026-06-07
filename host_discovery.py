import socket
import subprocess
import re

def get_gateway():
    try:
        output = subprocess.check_output("ip route", shell=True).decode()
        gateway = re.search(r"default via (\S+)", output)

        if gateway:
            return gateway.group(1)

    except:
        return "Not Found"

def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def ip_class(ip):
    first_octet = int(ip.split(".")[0])

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D"
    elif 240 <= first_octet <= 255:
        return "Class E"
    else:
        return "Unknown"

gateway_ip = get_gateway()
local_ip = get_local_ip()

print("\nHost Discovery Tool")
print("-" * 30)
print(f"Local IP Address : {local_ip}")
print(f"Gateway IP       : {gateway_ip}")
print(f"IP Class         : {ip_class(local_ip)}")
