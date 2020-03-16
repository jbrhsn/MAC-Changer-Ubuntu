#!/usr/bin/env python3

import os
import subprocess
import re
from files import macchangerclass


def resetMac(obj):
    obj.resetMAC()


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
          '\nCommand line Mode : \t sudo python3 macchanger.py [interface name] [New MAC Address to Spoof] \n')


def showInterfaces():
    res = subprocess.check_output(["ifconfig"])
    res = res.decode()
    res = re.findall(r"(\w*)(?:: flags=)", res)
    res.remove('lo')
    print('[+] Available Intefaces in Your System')
    for i in range(len(res)):
        print("+++[" + str(i + 1) + "] " + res[i])
    return res


def selectInterface(interfaces, x=None):
    if x is None:
        x = input('\n[+] Enter the name of inteface : ')
    if x in interfaces:
        return x
    else:
        print('[-] Invalid Interface Name')
        return False


def askNewMac(nm=None):
    f = 0
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'e', 'd', 'f', ':']
    if nm is None:
        nm = input('[+] Enter New MAC Address to Spoof : ')
    nm = nm.lower()
    for x in nm:
        if x not in lst:
            f = 1
    t = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', nm)
    if len(t) == 1 and f == 0:
        return nm
    else:
        print('[-] The Entered MAC is invalid eg: aa:aa:aa:aa:aa:aa')
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
        print('++++ Pip3 is installed\n')
    else:
        print('---- Pip3 is not installed\n')
        flag = 1

    if flag == 1:
        print('\n[-] Requirements Not Met. Install the requirements using - sudo apt install packagename\n')
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


def commandLineArgs(args, ifcs):
    print('[+] Command Mode Triggered')
    if len(args) == 2:
        args.append(None)
    if args[1] in ifcs:
        args[1] = selectInterface(ifcs, args[1])
    mac = askNewMac(args[2])
    while not mac:
        mac = askNewMac()
    obj = execute(args[1], mac)
    return obj


def execute(ifc, mac):
    obj = macchangerclass.MacChanger(ifc, mac)
    obj.changeMac()
    return obj


def managePrompt(ifcs):
    print('[+] Prompt Mode Triggered')
    ifc = selectInterface(ifcs)
    while not ifc:
        ifc = selectInterface(ifcs)
    mac = askNewMac()
    while not mac:
        mac = askNewMac()
    obj = execute(ifc, mac)
    return obj


def start(a, args=None):
    try:
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
        obj = ''
        if a == 'prompt':
            obj = managePrompt(ifcs)
        else:
            obj = commandLineArgs(args, ifcs)
        print('[+] Press ctrl+c to reset MAC Address and Exit from Program')
        while True:
            pass
    except  Exception as e:
        try:
            resetMac(obj)
        except AttributeError as d:
            pass
        print('\n' + str(e) + '\n[-] Some Error Occured. Exiting...')
        return
    except KeyboardInterrupt as e:
        try:
            resetMac(obj)
        except AttributeError as d:
            pass
        print('[+] Exiting from Program..')
