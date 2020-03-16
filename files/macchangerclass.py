#!/usr/bin/env python3

import subprocess
import re


class MacChanger:
    def __init__(self, interface, newmac):
        self.interface = interface
        self.currentmac = self.getCurrMac()
        self.newmac = newmac

    def getCurrMac(self):
        res = subprocess.check_output(['ifconfig', self.interface], stderr=subprocess.PIPE).decode()
        res = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', res)[0]
        print('[+] Current MAC of Device ' + self.interface + ' is : ' + res)
        return res

    def changeMac(self):
        subprocess.call(['ifconfig', self.interface, 'down'])
        subprocess.call(['ifconfig', self.interface, 'hw', 'ether', self.newmac])
        subprocess.call(['ifconfig', self.interface, 'up'])
        res = subprocess.check_output(['ifconfig', self.interface]).decode()
        mac = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', res)[0]
        if self.newmac == mac:
            print('\n[+] MAC Address change successfull')
            a = self.getCurrMac()
        else:
            print('\n[-] MAC Spoofing failed. Try Again')

    def resetMAC(self):
        subprocess.call(['ifconfig', self.interface, 'down'])
        subprocess.call(['ifconfig', self.interface, 'hw', 'ether', self.currentmac])
        subprocess.call(['ifconfig', self.interface, 'up'])
        res = subprocess.check_output(['ifconfig', self.interface]).decode()
        mac = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', res)[0]
        if self.currentmac == mac:
            print('\n[+] MAC Address reset successfull')
        else:
            print('\n[-] MAC Reset failed. Try Again')
