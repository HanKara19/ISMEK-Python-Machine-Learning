
# Console Phonebook

## Project Description

Console Phonebook is a simple Python application that allows users to manage contacts through a terminal menu.

The application uses a dictionary to store names and phone numbers.

## Features

- Add new contacts
- Search for contacts by name
- List all contacts alphabetically
- Delete existing contacts
- Exit the application

## Python Concepts Used

- Dictionaries
- While loops
- If, elif, and else statements
- User input
- String methods
- Dictionary methods
- Sorting
- The break statement

## How It Works

The program displays a menu with five options.

### 1. Add Contact

The user enters a name and phone number.

The program stores this information in a dictionary.

### 2. Search Contact

The user enters a contact name.

The program searches the dictionary and displays the phone number if the contact exists.

### 3. List All Contacts

The program displays all saved contacts in alphabetical order.

### 4. Delete Contact

The user enters a contact name.

The program removes the contact if it exists.

### 5. Exit

The program stops running.

## Example

```text
--- PHONEBOOK MENU ---
1. Add Contact
2. Search Contact
3. List All Contacts
4. Delete Contact
5. Exit

Choose an option (1-5): 1
Name: Ahmet
Phone number: 05551112233
Ahmet was added successfully.
```

## How to Run

Open a terminal in this project folder and run:

```bash
python phonebook.py
```

## Limitations

- Contacts are stored in memory.
- All contacts are lost when the program closes.
- Adding an existing name updates its phone number.
- Phone numbers are not validated.
- An empty phone number is allowed.

## What I Learned

This project helped me understand how to combine dictionaries, loops, conditions, and string methods to create an interactive Python application.
