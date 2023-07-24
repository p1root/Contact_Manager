import modules.DbContext as db
from modules.model import Contact
db = db.Database()
def showAllContact():
    data = db.loadAll()
    printContact(data)
def createContact():
    name = input("\n         [1] Enter Name : ")
    phone = input("\n         [2] Enter phone Number: ")
    while not IsValidNumber(phone):
        print("\n         [Error] Phone Number Is Not Valid !!!")
        phone = input("\n         [2] Enter phone Number: ")

    
    email = input("\n         [3] Enter email : ")
    try:
        c= Contact(None , name , phone , email)
        db.addContact(c)
        return True
    except Exception as e:
        print(e)
        return False

def editContact():
    data = db.loadAll()
    printContact(data)
    while True:
        num = input("\n         [+] Enter Number Of Contact :")
        try:
            num = int(num)
            if len(data) < num:
                print("\n         [Error] Number Out Of Range List !!!")
                
            else:
                name = input("\n         [1] Enter New Name : ")
                phone = input("\n         [2] Enter New Phone Number : ")
                while not IsValidNumber(phone):
                    print("\n         [Error] Phone Number Is Not Valid !!!")
                    phone = input("\n         [2] Enter Phone Number: ")

                email = input("\n         [3] Enter New email : ")
                id = data[num-1].id
                try:
                    c= Contact(id , name , phone , email)
                    db.updateContact(c)
                    return True
                except Exception as e:
                    print(e)
                    return False
        except Exception as e:
            print("\n         [Erorr] Character Is Not Valid !!!")
            pass

def deleteContact():
    data = db.loadAll()
    printContact(data)
    while True:
        num = input("\n         [+] Enter Number Of Contact :")
        try:
            num = int(num)
            if len(data) < num:
                print("\n         [Error] Number Out Of Range List !!!")

            else:
                contact = data[num-1]
                db.remove(contact.id)
                return True
            
        except Exception as e:
            print("\n         [Erorr] Character Is Not Valid !!!")
            pass

def showWithName(name):
    data = db.loadWithName(name) 
    printContact(data)

def printContact(data):
    if len(data) == 0:
        print("\n         [-] No Contact To Show")
        return
    
    print("\n"+" "*11+"NAME"+" "*17+"PHONE NUMBER"+" "*8+"EMAIL")
    for index in range(len(data)):
        name = data[index].name
        if len(data[index].name) > 20:
            name = data[index].name[:17] + "..."
        print(" "*(9-len(str(index+1)))+ f"{index+1}. "+f"{name}" + " "*(20-len(name)) +f" {data[index].phone}" + " "*(20-len(data[index].phone)) + f"{data[index].email} ")
    
def IsValidNumber(num):
    if len(num) >=8 and len(num)<=11:
        for n in num:
            if   n >= "0" and n <= "9":
                pass
            else:
                return False
        return True
    else:
        return False

