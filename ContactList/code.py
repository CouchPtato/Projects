import json

FILENAME = 'ContactList\contacts.json'

def is_valid_number(phone):
    return phone.isdigit() and len(phone) == 10

def load_contacts():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts):
    name = input("\nEnter name: ")

    while True:
        phone = input("Enter phone number: ")
        if is_valid_number(phone):
            break
        else:
            print("Number not valid")

    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print("Contact added!")

def delete_contact(contacts):
    name = input("\nEnter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted!")
            return
    print("Contact not found!")

def update_contact(contacts):
    name = input("\nEnter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            contact['name'] = new_name
            contact['phone'] = new_phone
            save_contacts(contacts)
            print("Contact updated!")
            return
    print("Contact not found!")

def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for contact in contacts:
            print(f"\nName: {contact['name']} \nPhone: {contact['phone']}")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


main()
