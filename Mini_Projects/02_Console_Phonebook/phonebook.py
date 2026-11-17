
# Console Phonebook
# Python Data Structures Mini Project

# Dictionary for storing contacts
# Key: Contact name
# Value: Phone number
contacts = {}

# Main menu
MENU = """
--- PHONEBOOK MENU ---
1. Add Contact
2. Search Contact
3. List All Contacts
4. Delete Contact
5. Exit
"""

# Keep the program running
while True:
    print(MENU)

    # Get the user's choice
    choice = input("Choose an option (1-5): ").strip()

    # Option 1: Add a contact
    if choice == "1":
        name = input("Name: ").strip().title()

        if not name:
            print("Name cannot be empty.")
        else:
            phone = input("Phone number: ").strip()

            contacts[name] = phone

            print(f"{name} was added successfully.")

    # Option 2: Search for a contact
    elif choice == "2":
        name = input("Search name: ").strip().title()

        phone = contacts.get(name)

        if phone is not None:
            print(f"Found -> {name}: {phone}")
        else:
            print("Contact not found.")

    # Option 3: List all contacts
    elif choice == "3":

        if not contacts:
            print("The phonebook is empty.")
        else:
            print("\n--- ALL CONTACTS ---")

            for number, (name, phone) in enumerate(
                sorted(contacts.items()), start=1
            ):
                print(f"{number}. {name:<15} -> {phone}")

    # Option 4: Delete a contact
    elif choice == "4":
        name = input("Name to delete: ").strip().title()

        if name in contacts:
            del contacts[name]

            print(f"{name} was deleted.")
        else:
            print("Contact not found.")

    # Option 5: Exit
    elif choice == "5":
        print("Goodbye!")
        break

    # Invalid menu selection
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
