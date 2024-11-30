# empty list to store contacts
contacts = [] 

while True:
    print("\n--- Contact LIst Menu ---")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Exit")
    # Displays the available menu options to the user.
    choice = input("Choose an option (1-4): ") 
    # Prompts the user to input a choice and assigns it to the variable choice

    # To view the contacts that add
    if choice == "1":
        if contacts:
            print("\nYour Contacts:")
            for conta in range(len(contacts)):
                contact = contacts[conta]
                print(f"{conta + 1}. Name: {contact['name']}- Number: {contact['number']}")
        # If there are contacts, it will display them with their index number
        else:
            print("Your contacts list is empty")
        # If there are no contacts, it will display a message saying that the contacts list is empty

    # To add a contact
    elif choice == "2":
        name= input("Enter contact name: ")
        num = input("Enter contact number: ")
        contacts.append({"name": name, "number": num}) 
        print(f"Contact '{name} - {num}' added.")
        # Adds a new contact to the list with the name and number provided by the user
    
    # To delete a contact
    elif choice == "3":
        print("\nYour Contacts:")
        if contacts:
            for conta in range(len(contacts)):
                contact = contacts[conta]
                print(f"{conta + 1}. Name: {contact['name']}- Number: {contact['number']}")
        name = int(input("Enter the number of the contact to delete: ")) # get the index of the contact to delete
        if 1 <= name <= len(contacts):
            deleted_contact = contacts.pop(name - 1)
            print(f"Deleted contact: {deleted_contact['name']} - {deleted_contact['number']}")
            # Deletes the contact at the index provided by the user
        else:
            print("Invalid contact number.")
        # If the user enters an invalid contact number, it will display a message saying that the contact number is invalid


    elif choice == "4":
        print("Exiting the program. Goodbye!") # Exits the program and displays a goodbye message
        break # Exits the loop and ends the program
    else:
        print("Invalid choice. Please choose a valid option.") # If the user enters an invalid choice, it will display a message saying that the choice is invalid
