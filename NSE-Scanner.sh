#!/bin/bash

echo "Nmap NSE Scanner"

read -p "Enter Target IP: " ip
read -p "Enter NSE Script Name: " script

script_path="/usr/share/nmap/scripts/$script.nse"

if [ -f "$script_path" ]; then
    echo ""
    echo "Script Found: $script_path"
    echo "Running Scan..."
    echo ""

    nmap --script="$script_path" "$ip"

    echo ""
    echo "Scan Completed"
else
    echo ""
    echo "NSE script not found!"
fi
