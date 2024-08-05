import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_Contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_Contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_Contact(contacts):
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.")

# Search for a contact by name
def search_Contact(contacts):
    search_Name = input("Enter contact name to search: ").strip().lower()
    found_Contacts = {name: details for name, details in contacts.items() if search_Name in name.lower()}
    
    if found_Contacts:
        for name, details in found_Contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}\n")
    else:
        print("No contacts found.")

# Update an existing contact
def update_Contact(contacts):
    name = input("Enter contact name to update: ").strip()
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()

        if not phone or not email:
            print("Phone number and email cannot be empty.")
            return
        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")
        
# Delete a contact
def delete_Contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

# View all contacts
def view_Contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}\n")

# Main menu
def main():
    contacts = load_Contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_Contact(contacts)
        elif choice == '2':
            search_Contact(contacts)
        elif choice == '3':
            update_Contact(contacts)
        elif choice == '4':
            delete_Contact(contacts)
        elif choice == '5':
            view_Contacts(contacts)
        elif choice == '6':
            save_Contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
