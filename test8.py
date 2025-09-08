<<<<<<< HEAD

=======
contacts = {}

def is_valid(name, phone):
    return name.strip() and phone.strip().replace('+', '').replace('-', '').isdigit()

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    if is_valid(name, phone):
        contacts[name] = phone
        print("Contact added.")
    else:
        print("Invalid name or phone.")

def search_contact():
    name = input("Name to search: ").strip()
    print(contacts.get(name, "Contact not found"))

def delete_contact():
    name = input("Name to delete: ").strip()
    print(contacts.pop(name, "Contact not found"))

def list_contacts():
    if not contacts:
        print("No contacts.")
    else:
        for name in sorted(contacts):
            print(f"{name}: {contacts[name]}")

def menu():
    while True:
        print("\n1 - Add, 2 - Search, 3 - Delete, 4 - List, 0 - Exit")
        choice = input("Choose: ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            list_contacts()
        elif choice == '0':
            break
        else:
            print("Wrong choice.")

menu()
>>>>>>> 460ef79 (conflict in test7.py)
