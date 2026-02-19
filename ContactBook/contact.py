import json
import os

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = input("Enter Name: ").strip()
        if name in self.contacts:
            print("Contact already exists!")
            return
        
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        print(f"Contact {name} added successfully.")

    def search_contact(self):
        query = input("Enter name to search: ").strip()
        contact = self.contacts.get(query)
        if contact:
            print(f"\nName: {query}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("Contact not found.")

    def display_all(self):
        if not self.contacts:
            print("Contact book is empty.")
            return
        print("\n--- Contact List ---")
        for name, info in self.contacts.items():
            print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")

def main():
    book = ContactBook()
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Quit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            book.add_contact()
        elif choice == '2':
            book.search_contact()
        elif choice == '3':
            book.display_all()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()