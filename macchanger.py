import sys
from files import macchangerfunctions


def getCommandLineInputs():
    if len(sys.argv) > 1:
        macchangerfunctions.start('command', sys.argv)
    else:
        macchangerfunctions.start('prompt')


getCommandLineInputs()
