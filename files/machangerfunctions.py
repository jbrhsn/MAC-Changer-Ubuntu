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
    res = str(subprocess.check_output(['ifconfig']))
    res = re.findall(r"(\w)(?::)", res)
    print(res)


showInterfaces()
