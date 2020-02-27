import macchangerclass
import macchangerfunction

# Title And Intro
print("\n MAC-CHANGER / MAC-SPOOFER \n  You can change the MAC Address of your network "
      "\ninterface card temporarily.\n")
# Show Choices To User and Getting Choice Number
print(
    "[+] 1. Show All Interfaces \n[+] 2. Show Current MAC Address \n"
    "[+] 3. Change MAC Address \n[+] 4. Check For Dependencies \n")
ch = input("\nEnter Your Choice : ")
ch = int(ch)

dumy = macchangerclass.macChanger()

if ch == 1:
    print("\nThe Available Interfaces Are :")
    macchangerclass.macChanger.showInterfaces()
if ch == 2:
    pass
