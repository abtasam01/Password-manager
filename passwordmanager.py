import json
from credential import Credential


class PasswordManager:
    def load_data(self):

        try:

            with open("passwords.json", "r") as f:
                return json.load(f)

        except:
            return {}

    def save_data(self, existing_data):

        with open("passwords.json", "w") as f:
            json.dump(existing_data, f, indent=4)

    def search_user(self, name) -> bool:

        existing_data = self.load_data()

        if name in existing_data:
            return True
        else:
            return False

    def search_website(self, name, website) -> bool:

        existing_data = self.load_data()

        if name in existing_data:

            if website in existing_data[name]:
                return True

        return False

    def show_user_data(self, name):
        existing_data = self.load_data()
        if name in existing_data:

            print(f"\nSaved Data For {name}:\n")

            for website, password in existing_data[name].items():

                print(f"Website/App: {website}")
                print(f"Password: {password}\n")

            else:

                print("User Does Not Exist!")

    def new_website(self, name):
        web = input("Enter Name Of The Website Or App You Want To Add: ").lower()

        if self.search_website(name, web):
            print(f'This "{web}" Website/App Already Exists')
        else:
            while True:
                pw = input("Please Enter The Password: ")

                confirm_pw = input("Please Re-enter The Password To Confirm: ")

                if pw == confirm_pw:

                    existing_data = self.load_data()

                    existing_data[name][web] = pw

                    self.save_data(existing_data)

                    print(f"{web} Added Successfully")

                    break

                else:
                    print("Passwords Do Not Match: ")

    def delete_existing_website(self, name):

        web = input("Enter The Website/App You Want To Delete: ").lower()

        existing_data = self.load_data()

        if web in existing_data[name]:

            del existing_data[name][web]

            self.save_data(existing_data)

            print(f"{web} Deleted Successfully! ")

        else:

            print("This Website/App Does Not exist! ")

            print(f"{web} Do Not Exist")

    def show_password(self, name):

        web = input("Enter The Website/App You Want To See: ")

        existing_data = self.load_data()

        if web in existing_data[name]:

            print(f'The Password Of Your {web} is "{existing_data[name][web]}"')

        else:

            print(f"{web} Do Not Exist")

    def update_password(self, name):

        web = input("Enter The Website/App You Want To Update: ")

        existing_data = self.load_data()

        if web in existing_data[name]:

            while True:
                new_pw = input("Please Enter The New Password: ")

                confirm_new_pw = input("Please Re-enter The New Password To Confirm: ")

                if new_pw == confirm_new_pw:

                    existing_data[name][web] = new_pw

                    self.save_data(existing_data)

                    print(f"{web} Password Updated successfully: ")

                    break
                else:
                    print("Passwords Do Not Match: ")


        else:

            print(f"{web} Do Not Exist")
