# Initialize an empty list to store tasks
to_do_list = [] 

# Start an infinite loop to display the menu and process user input
while True:
    # Display the menu options to the user
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")
    
    # Ask the user for their choice
    choice = input("Choose an option (1-4): ")

    # If the user chooses to view the to-do list
    if choice == "1":
        # Check if there are any tasks in the list
        if to_do_list:
            print("\n--- Your To-Do List ---")
            # Loop through the list and display each task with its number
            for to_do in range(len(to_do_list)):
                to_do_l = to_do_list[to_do]
                print(f"{to_do + 1}. {to_do_l}")
        # If the list is empty, notify the user
        else:
            print("Your to-do list is empty.")

    # If the user chooses to add a new task
    elif choice == "2":
        # Prompt the user to enter the new task
        task = input("Enter a new task: ")
        # Add the new task to the list
        to_do_list.append(task)
        # Confirm the task has been added
        print(f"Task '{task}' added.")

    # If the user chooses to mark a task as completed
    elif choice == "3":
        # Check if there are any tasks in the list
        if to_do_list:
            print("--- Your To-Do List ---")
            # Loop through the list and display each task with its number
            for to_do in range(len(to_do_list)):
                to_do_l = to_do_list[to_do]
                print(f"{to_do + 1}. {to_do_l}")
            # Ask the user to specify the number of the task they completed
            num = int(input("Enter the number of the task you completed: "))
            # Validate the user's input (it must correspond to a task in the list)
            if 1 <= num <= len(to_do_list):
                # Remove the completed task from the list and store it in a variable
                completed_task = to_do_list.pop(num - 1)
                # Confirm the task has been marked as completed
                print(f"Task '{completed_task}' marked as completed.")
            else:
                # Notify the user if they entered an invalid task number
                print("Invalid task number.")
        # If the list is empty, notify the user
        else:
            print("Your to-do list is empty.")

    # If the user chooses to exit the program
    elif choice == "4":
        # Display an exit message and break out of the loop
        print("Exiting the program. Goodbye!")
        break

    # If the user enters an invalid choice
    else:
        # Notify the user and prompt them to choose a valid option
        print("Invalid choice. Please choose a valid option.")



