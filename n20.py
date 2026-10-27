import os
import time
members = []
found = False

#

def search(members):
    clear()
    print("Search By")
    print("\n1. Membersship ID")
    print("2. First Name")
    print("3. Membership Status")
    choose_number_serach = input("Choose number: ")
    clear()
    if choose_number_serach == "1":
        search_id = input("Enter the ID: ")
        for member in members:
            if member.id == search_id:
                member.show_members()
                found = True
            if not found:
                print("Member not found.")
    elif choose_number_serach == "2":
        search_name = input("Enter first name: ").lower()
        for member in members:
            if member.f_name == search_name:
                member.show_members()
                found = True
            if not found:
                print("Member not found")
    elif choose_number_serach == "3":
        search_status = input("Enter the status member: ").lower()
        for member in members:
            if member.status == search_status:
                member.show_members()
                found = True
            if not found:
                print("Member not found.")
    else:
        print("Filld, pleas try agine.")

#    
def clear():
    os.system("cls" if os.name  == "nt" else "clear")

class Menbers_op:
    def __init__(self, first_name, last_name, id, status="inactive"):
        self.f_name = first_name
        self.l_name = last_name
        self.id = id
        self.status = status

    def show_members(self):
        print(f"\nFirst Name: {self.f_name}\nLast Name: {self.l_name}\nMembership ID: {self.id}\nMembership Status: {self.status}\n_______________________")


def start():
    print("Welcome to Gym Membership Management!")

    print("\nChoose an Action\n1. Add new nember\n2. display all members\n3. Search for a member\n4. Exit")
while True:
    start()
    choose_number_user = input("\nEnter your choise: ")
    clear()
    if choose_number_user == "1":
        while True:
            f_name = input("Enter first name: ")
            if f_name:
                break
            else: 
                print("Filld, pleas try agine.")
        while True:
            l_name = input("Enter last name: ")
            if l_name :
                break
            else:
                print("Filld, pleas try agine.")    
        while True:
            Id = input("Enter the ID: ")
            if Id.isdigit():
                break
            else:
                print("Filled try agine.")
        while True:
            status = input("Enter membership status, Or click 'Enter': ")
            if status == "active":
                break
            elif status:
                print("sorry write 'active' or click 'Enter', try agine.")
            else:
                status = "inactive"
                break
        new_members = Menbers_op(f_name,l_name,Id,status)
        members.append(new_members)
        print("Member added successfully!!!")
        time.sleep(2)
        clear()
    elif choose_number_user == "2":
        if members:
            print("Displaying all members ....")
            for member in members:
                member.show_members()
            print("------------\nPleas wite '5' sic to back home list.")
            time.sleep(5)
            clear()
        else:
            print("Members is empty.")
            time.sleep(2)
            clear()
    elif choose_number_user == "3":
        if members:
            search(members)
            time.sleep(5)
        else:
            print("No members to search!")
    elif choose_number_user == "4":
        print("Ok, have see you next time.")
        exit()
    else:
        print("Invalid choise! Pleas try agine.")
        time.sleep(2) 

