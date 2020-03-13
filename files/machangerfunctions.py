import subprocess
import re


def dispTitle():
    print('''\n    MAC - CHANGER\n----------------------\n''')


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
    selectInterface(res)


def selectInterface(interfaces):
    x = input('\n[+] Enter the name of inteface : ')
    if x in interfaces:
        return x
    else:
        print('[-] Invalid Interface Name')
        selectInterface(interfaces)


def requirementCheck():
    pass


def commandLineArgs():
    pass


showInterfaces()
