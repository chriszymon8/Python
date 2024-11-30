# dictionary to store grades
grades = {} 

while True:
    print("\n1. View All Student Grades")
    print("2. Add or Update Student Grade")
    print("3. View Specific Student's Grades")
    print("4. Delete Student Grade")
    print("5. Exit")
    # get user choice
    choice = input("Enter an option (1-5): ") # get user's choice

    if choice == "1": # view all student grades
        if grades: # if grades dictionary is not empty
            print("\nAll Student Grades:")
            for student, subjects in grades.items():
                print(f"Student: {student}")
                # print each subject and grade
                for subject, grade in subjects.items():
                    print(f"  {subject}: {grade}")
                # print a newline for better readability
        else:
            print("No student grades available.")

    elif choice == "2":
        name = input("Enter the student's name: ").strip() # get student's name
        subject = input("Enter the subject: ").strip() # get subject
        grade_value = input("Enter the grade for this subject: ").strip() # get grade value
        if name not in grades: # if student is not in grades dictionary
            grades[name] = {} # add student to dictionary with empty dictionary as value
        grades[name][subject] = grade_value # add subject and grade to student's dictionary
        print(f"Grade for {name} in {subject} updated to {grade_value}.") # print confirmation
    
    elif choice == "3":
        name = input("Enter the student's name to view grades: ").strip() # get student's name
        if name in grades:
            print(f"\nGrades for {name}:") 
            for subject, grade in grades[name].items(): # print each subject and grade
                print(f"  {subject}: {grade}") # print subject and grade
        else:
            print(f"No grades found for {name}.")

    elif choice == "4":
        name = input("Enter the student's name to delete grades: ").strip()
        # check if student exists in grades dictionary
        if name in grades:
            removed_grades = grades.pop(name, None) 
            print(f"Grades for {name} deleted: {removed_grades}")
        else:
            print(f"No grades found for {name}.")

    # exit the program
    elif choice == "5":
        print("Exiting the program. Goodbye!") # 
        break

    else:
        print("Invalid choice. Please choose a valid option.") 
