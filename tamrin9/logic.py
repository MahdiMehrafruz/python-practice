import csv 

class Contact :
    def __init__(self,name,phone_number):
        if not phone_number.isdigit():
            raise ValueError ("only number pls!")
        self.name = name
        self.phone_number = phone_number


class PhoneBook :
    def __init__(self):
        self.contacts = []

    def add_contact (self,name,phone):
        new = Contact (name,phone)
        self.contacts.append(new)

    def save_to_csv(self, filename = "contacts.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
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