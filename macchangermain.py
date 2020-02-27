import macchangerclass
import macchangerfunction

# Title And Intro
print("\n MAC-CHANGER / MAC-SPOOFER \n  You can change the MAC Address of your network \ninterface card temporarily.\n")
# Show Choices To User and Getting Choice Number
print("[+] 1. Show All Interfaces \n[+] 2. Show Current MAC Address \n[+] 3. Change MAC Address \n[+] 4. Check For Dependencies \n")
ch = input("\n Enter Your Choice : ")

dumy = macchangerclass.macChanger()

if ch == 1:
    dumy.showInterfaces()
if ch == 2:
    pass
    