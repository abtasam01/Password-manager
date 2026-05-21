# main.py

import json
from credential import Credential
from passwordmanager import PasswordManager

pm = PasswordManager()


def main_menu():

    print("Please Enter Your Choice: \n")
    main_menu_choice = input("1. New User\n2. Existing User\n3. EXIT ")
    if not main_menu_choice.isdigit():
        print("Invalid Choice! ")
    else:
        main_menu_choice = int(main_menu_choice)
        if main_menu_choice >= 3 or main_menu_choice <= 1 and main_menu_choice != int():
            print("Invalid Choice! ")

    match main_menu_choice:

        case 1:
            new_user()
            print("Thank You For Registration! ")
        case 2:
            existing_user()
            pass
        case 3:
            print("Thankyou! ")


def new_user(name=None):
    if name is None:
        print("Enter Username: ")

        while True:

            name = input().lower()

            if pm.search_user(name):

                print("Username Already Exists! ")
                print("Please Enter A New Username: ")

            else:
                break

    web = input("Enter Website or App: ").lower()

    pw = input("Enter Password: ")

    c1 = Credential(web, name, pw)

    existing_data = pm.load_data()

    if c1.name not in existing_data:

        existing_data[c1.name] = {}

    existing_data[c1.name] = {c1.web: c1.pw}

    pm.save_data(existing_data)

    print("User Added Successfully! ")


def existing_user():

    while True:

        name = input("Enter Username: ").lower()

        if pm.search_user(name):
            print(name)
            print("Please Enter Your Choice: \n")
            existing_user_choice = input(
                "1. Show All Data: \n"
                "2. Add A New Website Or App: \n"
                "3. Delete An Existing Website Or App: \n"
                "4. Show Password: \n"
                "5. Update Password: \n"
                "6. EXIT: \n"
            )

            if not existing_user_choice.isdigit():
                print("Invalid Choice! ")
            else:
                existing_user_choice = int(existing_user_choice)
                if (
                    existing_user_choice > 6
                    or existing_user_choice < 1
                    and existing_user_choice != int()
                ):
                    print("Invalid Choice! ")

            match existing_user_choice:
                case 1:
                    pm.show_user_data(name)
                case 2:
                    pm.new_website(name)

        else:
            print("Username Doesn't Exist! \n" "Do You Want To Register?\n")

            register = input("Press y Or n: ").lower()

            if register == "y":
                new_user(name)
                print("User Added Successfully! ")
            elif register == "n":
                print("Thankyou! ")
                main_menu()
            else:
                print("Invalid Choice! ")


main_menu()
