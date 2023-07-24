from Banner.Banner import banner
import sys
from modules.Controller import createContact, deleteContact, editContact, showAllContact , showWithName
import time

def main():
    banner()
    while True:

        num = input("\n         [+] Choose an Option : ")
        if num == "1":
            showAllContact()

        elif num == "2":
            if createContact():
                print("\n         [+] Contact Adedd :)")
                time.sleep(1)
            else:
                print("\n         [-] Contact Not Adedd :(")
                time.sleep(1)
            
        elif num == "3":
            if editContact():
                print("\n         [+] Contact Edited :)")
                time.sleep(1)
            else:
                print("\n         [-] Contact Not Edited :(")
                time.sleep(1)
            

        elif num == "4":
            if deleteContact():
                print("\n         [+] Contact Deleted :)")
                time.sleep(1)
            else:
                print("\n         [-] Contact Not Deleted :(")
                time.sleep(1)
            
        elif num == "5":
            name = input("\n         [+] Enter Name :")
            showWithName(name)
        
        elif num == "6":
           banner()

        elif num == "7":
            print("\n         [+] See You Next Time")
            sys.exit()

        else:
            pass


if __name__ == "__main__":
    main()
