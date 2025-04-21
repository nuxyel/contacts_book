# Contact Book

This is a simple **contact book** application developed as part of the **Introduction to Python and Algorithms** module of **Solyd Offensive Security**.

The main goal of this project is to store, edit, search, delete, and export contacts, all within a Python script running in the terminal.

## Features

- **Add New Contact**: Adds a new contact with phone, email, and address.
- **Edit Contact**: Allows editing an existing contact's details.
- **Delete Contact**: Deletes a contact from the list.
- **Search Contact**: Searches for a contact by name, phone, email, or address.
- **Export Contacts**: Exports the contact list to a CSV file.
- **Import Contacts**: Imports contacts from a CSV file.
- **Show All Contacts**: Displays all saved contacts.

## How to Use

### Step 1: Clone the Repository
Clone this repository to your computer using the following command:

```bash
git clone https://github.com/nuxyel/contacts_book.git
```

### Step 2: Run the Script
Open the terminal, navigate to the folder where the repository was cloned, and run the script:

```bash
python3 contact_book.py
```

### Step 3: Interaction
The program will show a menu in the terminal with the following options:

1. Show all contacts
2. Search a contact
3. Add a new contact
4. Edit a contact
5. Delete a contact
6. Export contacts to CSV
7. Import contacts from CSV
0. Exit

Type the corresponding number to choose an option.

## How It Works

1. **Local Storage**: Contacts are stored in a Python dictionary. Changes are saved in a CSV file (`database.csv`).
2. **Import and Export**: You can import or export the contact list in CSV format.
3. **Validation**: Some functions, like adding or editing contacts, include data validation (e.g., email format, phone number).

## Possible Future Improvements

- Implement **security and encryption** to protect sensitive data.
- Create a **graphical user interface (GUI)** for better usability.
- Add **user authentication** to limit access to data.

**_by r3n4n_**
