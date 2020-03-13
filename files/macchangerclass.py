#!/usr/bin/env python3

import subprocess
import re


class MacChanger:
    def __init__(self, interface, mac=None):
        self.interface = interface
        self.currentmac = self.getCurrMac()
        self.newmac = self.askNewMac(mac)

    def getCurrMac(self):
        res = subprocess.check_output(['ifconfig', self.interface], stderr=subprocess.PIPE).decode()
        res = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', res)[0]
        print('[+] Current MAC of Device ' + self.interface + ' is : ' + res)
        return res

    def askNewMac(self, nm=None):
        f = 0
        lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'e', 'd', 'f', ':']
        if nm is None:
            nm = input('[+] Enter New MAC Address to Spoof : ')
        nm = nm.lower()
        for x in nm:
            if x not in lst:
                f = 1
        t = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', nm)
        if t and f == 0:
            return nm
        else:
            print('[-] The Entered MAC is invalid eg: aa:aa:aa:aa:aa:aa')
            self.newmac = self.askNewMac()

    def changeMac(self):
        subprocess.call(['ifconfig', self.interface, 'down'])
        subprocess.call(['ifconfig', self.interface, 'hw', 'ether', self.newmac])
        subprocess.call(['ifconfig', self.interface, 'up'])
        res = subprocess.check_output(['ifconfig', self.interface]).decode()
        mac = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', res)[0]
        if self.newmac == mac:
            print('\n[+] MAC Address change successfull')
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
