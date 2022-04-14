#!/usr/bin/env python3
import re
import nmap
import ipaddress

#To be able to use this program you need to have instaled python-nmap
#First install pip, which is a The standard package manager for Python
#In Linux:  sudo apt install python3-pip
#And then pip install python-namp
#If it doesn't work try to uninstall python-nmap 8in case you already have it) pip uninstall python-nmap
#and then install it back, pip install python-nmap

print("""  _______  _            _____  _              _        
 |__   __|| |          |  __ \(_)            | |       
    | |   | |__    ___ | |__) |_   ___  ___  | |  ___  
    | |   | '_ \  / _ \|  ___/| | / __|/ _ \ | | / _ \ 
    | |   | | | ||  __/| |    | || (__| (_) || || (_) |
    |_|   |_| |_| \___||_|    |_| \___|\___/ |_| \___/\[T]/ """)
print("\n************************************************************")
print("Welcome to a REALLY simple port scanning program")

#ip_address = re.compile("^(?:[0-9]{1-3}\.){3}[0-9]{1-3}$") Check Ip format with re.compile

port_pattern = re.compile("([0-9]+)-([0-9]+)") #Pattern for port range
port_min = 0
port_max = 65535

#Check if the IP format from the input is correct using ipaddress
while True:
    ip_address_recive = input("Enter an IP to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_address_recive)
        print("The ip entered is correct")
        break
    except:
        print("You entered an invalid ip address")

#Check if the Port range given is correct
while True:
    print("Entre the range of the port to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port rang: ")
    port_range_valid = port_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

#main thing
nm = nmap.PortScanner()
for port in range(port_min, port_max +1):
    try:
        result = nm.scan(ip_address_recive, str(port))
        #print(nm.command_line())
        #print(ip_address_recive,"is ", nm[ip_address_recive].state())
        port_status = (result['scan'][ip_address_recive]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        print(f"Cannot scan port {port}{ip_address_recive}")