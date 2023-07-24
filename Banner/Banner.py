import time
import os
def banner():
    os.system("cls")
    text = """       
        CCCCCCCCCCCCC        MMMMMMMM               MMMMMMMM
     CCC::::::::::::C        M:::::::M             M:::::::M
   CC:::::::::::::::C        M::::::::M           M::::::::M
  C:::::CCCCCCCC::::C        M:::::::::M         M:::::::::M
 C:::::C       CCCCCC        M::::::::::M       M::::::::::M
C:::::C                      M:::::::::::M     M:::::::::::M
C:::::C                      M:::::::M::::M   M::::M:::::::M
C:::::C                      M::::::M M::::M M::::M M::::::M
C:::::C                      M::::::M  M::::M::::M  M::::::M
C:::::C                      M::::::M   M:::::::M   M::::::M
C:::::C                      M::::::M    M:::::M    M::::::M
 C:::::C       CCCCCC        M::::::M     MMMMM     M::::::M
  C:::::CCCCCCCC::::C        M::::::M               M::::::M
   CC:::::::::::::::C ...... M::::::M               M::::::M
     CCC::::::::::::C .::::. M::::::M               M::::::M
        CCCCCCCCCCCCC ...... MMMMMMMM               MMMMMMMM
                                                                
         [1] Show All Cantacts                                                       
                                                                
         [2] Create Contact                                                       

         [3] Edit Contact

         [4] Delete Contact

         [5] Search Contact With Name
         
         [6] Clear Screen

         [7] EXIT 
                                                                """
    temp = 0
    for i in text:
        temp +=1
        print(i ,end="")
        if temp%8 == 0:
            time.sleep(.0000001)
    time.sleep(.2)

if __name__ == "__main__":
    banner()