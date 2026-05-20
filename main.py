# main.py

import json
from credential import Credential


def main_menu():

    print("Please Enter Your Choice\n")
    choice = int(input("1. New User\n2. Existing User\n3. EXIT "))

    if choice > 3 or choice < 1:
        print("Invalid Choice")

    match choice:

        case 1:
            match choice:
                case 1:
                    pass
            new_user()
            print("Thank You For Registration")


def new_user():

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
