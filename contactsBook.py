# This is a contact Book program

contacts = {}

def addContact():
    name = input("Enter Name: ").strip()
    if name in contacts:
        print("Contact Already Exits")
    else:
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()
        contacts[name] = {'phone': phone, 'email': email}
        print("contact added Successfully")

def viewContact():
    if contacts:
        print("----- Contacts List ------")
        for name, info in contacts.items():
            print(f' Name: {name}\n Phone: {info["phone"]}\n Email: {info["email"]}')
            print("--------------------")
    else:
        print("No Contacts Found")

def updateContact():
    name = input("Enter the Name to update: ").strip()
    if name in contacts:
        print('Leave blank to keep old value')
        phone = input(f'New Phone Number ({contacts[name]["phone"]}): ').strip()
        email = input(f'New Email Id ({contacts[name]["email"]}): ').strip()

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email 
        print("Contact updated successfully")
    else:
        print("No Contacts Found")

def deleteContact():
    name = input("Enter the Name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("No Contacts Found")

def searchContact():
    name = input("Enter the Name to search: ").strip()
    if name in contacts:
        print(f'Name: {contacts[name]},\n Phone: {contacts[name]["phone"]},\n Email: {contacts[name]["email"]}')
        print("--------------------")
    else:
        print("No Contacts Found")

def countContact():
    print(f'Total Contacts Count: {len(contacts)}')

def menu():
    while True:
        print("\n***** Contacts Book Menu *****")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Count Contacts")
        print("7. Exit")

        choice = input("Enter your choice (1 - 7): ").strip()

        if choice == "1":
            addContact()
        elif choice == "2":
            viewContact()
        elif choice == "3":
            updateContact()
        elif choice == "4":
            deleteContact()
        elif choice == "5":
            searchContact()
        elif choice == "6":
            countContact()
        elif choice == "7":
            print("Exiting Contacts Book, Good Bye")
            break 
        else:
            print("invalid Choice")
        
menu()
