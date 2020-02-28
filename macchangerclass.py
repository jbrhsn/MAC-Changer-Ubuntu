#! /env/python3

import subprocess
import re


class macChanger:
    def __init__(self, interface, new_mac):
        self.interface = interface # Interface Name
        self.current_mac = self.showCurrentMac(self.interface) # Gets Current MAC Address
	self.new_mac = new_mac # New MAC Address

    def showInterfaces():
        # Fetching all interfaces
        out = subprocess.check_output(["ifconfig"], shell=True)
        interfaces = re.findall(r"(\w+)(?:: flags)", str(out))
        # Display all the interfaces
        i = 1
        for interface in interfaces:
            print("[+] " + str(i) + " : " + interface)
            i = i + 1
        # Returns the list of interfaces
        return interfaces

    def askMac(self):
        #   Get Mac Address From User
        mac = input("\n[+] Enter New Mac Address : ")
        new_mac = re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", mac)
        # Checks if it is entered in correct form
        if new_mac[0] == mac:
            return new_mac
        else:
            print("\n[-] Not a Valid MAC Address. Eg: a1:b2:c3:4a:66:bs ")
            self.askMac()

    def showCurrentMac(self, interface):
        # Fetching MAC Address
        out = subprocess.check_output(["ifconfig", interface], shell=True)
        current_mac = re.findall(r"(\w\w:\w\w:\w\w:\w\w:\w\w)", str(out))
        # Display Current MAC Address
        print("\n[+] Current MAC Address : " + current_mac[0])
        # Returns Current MAC Address
        return current_mac

    def dependancyCheck():
	# checks net-tools installation
	out = subprocess.check_output(["ifconfig"])
	ls = re.findall(r"flag",str(out))
	''' It is Not Completed '''
	
