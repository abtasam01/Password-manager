# main.py

import json
from credential import Credential


def main_menu():

    print("Please Enter Your Choice\n")
    choice = input("1. New User\n2. Existing User\n3. EXIT ")
    if not choice.isdigit():
        print("Invalid Choice")
    else:
        choice = int(choice)
        if choice >= 3 or choice <= 1 and choice != int():
            print("Invalid Choice")

    match choice:

        case 1:
            new_user()
            print("Thank You For Registration")
        case 2:
            existing_user()
            pass


def new_user(name=None):
    if name is None:
        print("Enter Username: ")

        while True:

            name = input().lower()

            if search_user(name):

                print("Username Already Exists!")
                print("Please Enter A New Username: ")

            else:
                break

    web = input("Enter Website or App: ").lower()

    pw = input("Enter Password: ")

    c1 = Credential(web, name, pw)

    existing_data = load_data()

    existing_data[c1.name] = {c1.web: c1.pw}

    save_data(existing_data)

    print("User Added Successfully")


def existing_user():

    while True:

        name = input("Enter Username: ").lower()

        if search_user(name):
            pass

        else:
            print("Username Doesn't Exist! \n" "Do you want to Register?\n")

            register = input("Press y or n").lower()

            if register == "y":
                new_user(name)
                print("User Added Successfully")
            elif register == "n":
                print("Thankyou!")
                main_menu()
            else:
                print("Invalid choice! ")


def load_data():

    try:

        with open("passwords.json", "r") as f:
            return json.load(f)

    except:
        return {}


def save_data(existing_data):

    with open("passwords.json", "w") as f:
        json.dump(existing_data, f, indent=4)


def search_user(data) -> bool:
    with open("passwords.json", "r") as f:
        existing_data = load_data()

    if data in existing_data:
        return True
    else:
        return False


main_menu()
