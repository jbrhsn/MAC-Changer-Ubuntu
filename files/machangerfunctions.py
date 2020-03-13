#!/usr/bin/env python3

import os
import subprocess
import re
import macchangerclass


def dispTitle():
    print('''\n MAC - CHANGER\n----------------''')


def dispInfo():
    print(
        'This is a simple tool for spoofing your device MAC address temporarily for privacy protection.'
        '\nThis tool is intended to use in ethical manner for your own protection from malicious hackers.'
        '\n**USE AT YOUR OWN RISK - IF YOU DO HARM TO ANYONE, WE ARE NOT RESPONSIBLE.\n')


def dispUsage():
    print(' USAGE\n-------'
          '\nPrompt Mode :\tJust answer the questions asked. It is simple.'
          '\nCommand line Mode : \t To be Updated.\n')


def showInterfaces():
    res = subprocess.check_output(["ifconfig"])
    res = res.decode()
    res = re.findall(r"(\w*)(?:: flags=)", res)
    res.remove('lo')
    print('[+] Available Intefaces in Your System\n')
    for i in range(len(res)):
        print("[" + str(i + 1) + "] " + res[i])
    return res


def selectInterface(interfaces):
    x = input('\n[+] Enter the name of inteface : ')
    if x in interfaces:
        return x
    else:
        print('[-] Invalid Interface Name')
        return False


def requirementCheck():
    res = subprocess.check_output(['apt', 'list', '--installed'], stderr=subprocess.PIPE).decode()
    print('\n[+] Requirements Checking In Progress ... \n')
    flag = 0

    if 'net-tools' in res:
        print('++++ Net-Tools is installed')
    else:
        print('---- Net-Tools is not installed')
        flag = 1

    if 'python3' in res:
        print('++++ Python3 is installed')
    else:
        print('---- Python3 is not installed')
        flag = 1

    if 'python3-pip' in res:
        print('++++ Pip3 is installed')
    else:
        print('---- Pip3 is not installed')
        flag = 1

    if flag == 1:
        print('\n[-] Requirements Not Met. Install the requirements using - sudo apt install packagename')
        return False
    else:
        return True


def rootCheck():
    if os.geteuid() == 0:
        print('\n[+] You have root permission. Go on')
        return True
    else:
        print('\n[-] Root permission not found. Please Run macchanger as root (sudo)')
        return False


def commandLineArgs():
    pass


def manage():
    dispTitle()
    dispInfo()
    dispUsage()
    if not rootCheck():
        print('[-] Exiting Program ..')
        return
    if not requirementCheck():
        print('[-] Exiting Program ..')
        return
    ifcs = showInterfaces()
    ifc = selectInterface(ifcs)
    while not ifc:
        ifc = selectInterface(ifcs)
    obj = macchangerclass.MacChanger(ifc)
    obj.getCurrMac()
    obj.changeMac()
    obj.resetMAC()
