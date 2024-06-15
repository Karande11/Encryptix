#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email: ")
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the contact book.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"Contact {i}:")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print()

    def search_contact(self):
        name = input("Enter the contact's name to search: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact found:")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the contact's name to delete: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.delete_contact()
        elif choice == '5':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




