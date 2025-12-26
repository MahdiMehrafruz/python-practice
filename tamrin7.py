import csv 

class Contact :
    def __init__(self,name,phone_number):
        if not phone_number.isdigit():
            raise ValueError("only numbers pls!")
        self.name = name
        self.phone_number = phone_number
        
        
class PhoneBook :
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        self.contacts.append(new_contact)

    def save_to_csv(self, filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for c in self.contacts:
                writer.writerow([c.name, c.phone_number])

    def load_from_csv(self, filename):
        self.contacts = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        name, phone = row
                        new_contact = Contact(name, phone)
                        self.contacts.append(new_contact)
                    except ValueError:
                        continue
        except FileNotFoundError:
            print("PhoneBook not found!")


phonebook = PhoneBook()
filename = "contacts.csv"
phonebook.load_from_csv(filename)

while True:
        print("\n--- PhoneBook ---")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Save N Exit\n")

        try:
            x = int(input("Enter ur choice : "))
        except ValueError:
            print("pls enter a number!")
            continue

        if x == 1:
            name = input("Enter Name : ")
            phone = input("Enter Phone number : ")

            try:
                phonebook.add_contact(name, phone)
                print("done!")
            except ValueError:
                print("wrong number! try again")

        elif x == 2:
            if not phonebook.contacts:
                print ("No contacts to show!")
            else:
                for c in phonebook.contacts:
                    print(c.name, "-", c.phone_number)

        elif x == 3:
            phonebook.save_to_csv(filename)
            print("done! exiting...")
            break

        else:
            print("pls pick a number between (1 or 2 or 3)")
