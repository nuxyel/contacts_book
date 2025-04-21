import re

CONTACTS = {}

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_valid_phone(phone):
    phone_regex = r'^\+?(\d[\d\-\(\)\s]{4,})$'
    return re.match(phone_regex, phone) is not None

def show_contacts():
    if CONTACTS:
        for name in CONTACTS:
            search_contact(name)
        print(f"[INFO] Total contacts: {len(CONTACTS)}")
    else:
        print("[INFO] Contact list is empty.")

def search_contact(name):
    try:
        print("Name:     ", name)
        print("Phone:    ", CONTACTS[name]['phone'])
        print("Email:    ", CONTACTS[name]['email'])
        print("Address:  ", CONTACTS[name]['address'])
        print("----------------------------------------")
    except KeyError:
        print("[ERROR] Contact not found!")
    except Exception as error:
        print("[ERROR] Unexpected error occurred.")
        print(error)

def read_contact_details():
    phone = input("Enter contact phone: ")
    while not is_valid_phone(phone):
        print("[ERROR] Invalid phone number format. Please enter again.")
        phone = input("Enter contact phone: ")

    email = input("Enter contact email: ")
    while not is_valid_email(email):
        print("[ERROR] Invalid email format. Please enter again.")
        email = input("Enter contact email: ")

    address = input("Enter contact address: ")
    return phone, email, address

def add_contact(contact, phone, email, address):
    CONTACTS[contact] = {
        'phone': phone,
        'email': email,
        'address': address,
    }
    save()
    print(f"[INFO] Contact {contact} added/updated successfully!\n")

def edit_contact(contact):
    try:
        current = CONTACTS[contact]
        print(f"[INFO] Editing contact: {contact}")

        phone = input(f"Phone [{current['phone']}]: ") or current['phone']
        while not is_valid_phone(phone):
            print("[ERROR] Invalid phone number format. Please enter again.")
            phone = input(f"Phone [{current['phone']}]: ") or current['phone']

        email = input(f"Email [{current['email']}]: ") or current['email']
        while not is_valid_email(email):
            print("[ERROR] Invalid email format. Please enter again.")
            email = input(f"Email [{current['email']}]: ") or current['email']

        address = input(f"Address [{current['address']}]: ") or current['address']

        add_contact(contact, phone, email, address)
    except KeyError:
        print("[ERROR] Contact does not exist!")

def search_contacts_by_filter(filter_type, value):
    for name, details in CONTACTS.items():
        if filter_type == 'phone' and value in details['phone']:
            search_contact(name)
        elif filter_type == 'email' and value in details['email']:
            search_contact(name)
        elif filter_type == 'address' and value in details['address']:
            search_contact(name)

def delete_contact(name):
    try:
        CONTACTS.pop(name)
        save()
        print(f"\n[INFO] Contact '{name}' deleted successfully!\n")
    except KeyError:
        print("[ERROR] Contact not found!")
    except Exception as error:
        print("[ERROR] Unexpected error occurred.")
        print(error)

def export_contacts(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write('name;phone;email;address\n')
            for name in CONTACTS:
                phone = CONTACTS[name]['phone']
                email = CONTACTS[name]['email']
                address = CONTACTS[name]['address']
                file.write(f"{name};{phone};{email};{address}\n")
        print("[INFO] Contacts exported successfully!")
    except Exception as error:
        print("[ERROR] Unexpected error occurred.")
        print(error)

def import_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:
                details = line.strip().split(';')
                name, phone, email, address = details
                add_contact(name, phone, email, address)
    except FileNotFoundError:
        print("[ERROR] File not found.")
    except Exception as error:
        print("[ERROR] Unexpected error occurred.")
        print(error)

def save():
    export_contacts('database.csv')

def load():
    try:
        with open('database.csv', 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:
                name, phone, email, address = line.strip().split(';')
                CONTACTS[name] = {
                    'phone': phone,
                    'email': email,
                    'address': address,
                }
        print("[INFO] Database loaded successfully!")
        print(f"[INFO] {len(CONTACTS)} contact(s) loaded.")
    except FileNotFoundError:
        print("[ERROR] File not found.")
    except Exception as error:
        print("[ERROR] Unexpected error occurred.")
        print(error)

def print_menu():
    print("----------------------------------------")
    print("1 - Show all contacts")
    print("2 - Search contact")
    print("3 - Add new contact")
    print("4 - Edit contact")
    print("5 - Delete contact")
    print("6 - Export contacts to CSV")
    print("7 - Import contacts from CSV")
    print("8 - Search contacts by phone/email/address")
    print("0 - Exit")
    print("----------------------------------------")

load()
print(">>>>>> Contact Book by r3n4n <<<<<<")

while True:
    print_menu()

    option = input("Choose an option: ")
    if option == '1':
        show_contacts()
    elif option == '2':
        name = input("Enter contact name: ")
        search_contact(name)
    elif option == '3':
        name = input("Enter contact name: ")
        if name in CONTACTS:
            print("[ERROR] Contact already exists!")
        else:
            phone, email, address = read_contact_details()
            add_contact(name, phone, email, address)
    elif option == '4':
        contact = input("Enter the contact name: ")
        edit_contact(contact)
    elif option == '5':
        name = input("Enter contact name: ")
        delete_contact(name)
    elif option == '6':
        file_name = input("Enter file name: ")
        export_contacts(file_name)
    elif option == '7':
        file_name = input("Enter file name: ")
        import_contacts(file_name)
    elif option == '8':
        filter_type = input("Search by (phone/email/address): ").lower()
        value = input(f"Enter {filter_type} to search for: ")
        search_contacts_by_filter(filter_type, value)
    elif option == '0':
        print("[INFO] Exiting contact book.")
        break
    else:
        print("[ERROR] Invalid option.")
