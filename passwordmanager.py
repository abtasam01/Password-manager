import json
from credential import Credential

class PasswordManager:
    def load_data(self):

        try:

            with open("passwords.json", "r") as f:
                return json.load(f)

        except:
            return {}


    def save_data(self,existing_data):

        with open("passwords.json", "w") as f:
            json.dump(existing_data, f, indent=4)


    def search_user(self,name) -> bool:

        existing_data = self.load_data()

        if name in existing_data:
            return True
        else:
            return False


    def search_website(self,name, website) -> bool:

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


    