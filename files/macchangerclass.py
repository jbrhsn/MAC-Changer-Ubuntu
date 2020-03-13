import subprocess
import re


class MacChanger:
    def __init__(self, interface):
        self.interface = interface
        self.currentmac = self.getCurrMac()
        self.newmac = self.askNewMac()

    def getCurrMac(self):
        res = subprocess.check_output(['ifconfig', self.interface]).decode()
        res = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', res)[0]
        print('[+] Current MAC of Device ' + self.interface + ' is : ' + res)
        return res

    def askNewMac(self):
        nm = input('[+] Enter New MAC Address to Spoof : ')
        t = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', nm)
        if t:
            return nm
        else:
            print('[-] The Entered MAC is invalid eg: aa:aa:aa:aa:aa:aa')
            self.askNewMac()

    def changeMac(self):
        pass


n = MacChanger('enp2s0')
