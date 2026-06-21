# Student Management System
# File: student_management.py
print("Made BY Vedant")       
All_students = {}   # Dictionary to store records

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"         #a+ grade if percentage greater or equals to 90
    elif percentage >= 80:
        return "A"          #a grade if percentage greater or equals to 80
    elif percentage >= 70:
        return "B+"         #b+ grade if percentage greater or equals to 70
    elif percentage >= 60:
        return "B"          #a+ grade if percentage greater or equals to 60
    elif percentage >= 50:
        return "C"          #a+ grade if percentage greater or equals to 50
    else:
        return "Fail"       #Fail if percentage is lower than 50 

def add_student():
    try:
        stu_name = input("Enter student name: ")              #input name & roll no
        stu_rno = int(input("Enter roll number: "))

        if stu_rno in All_students:                            #check if studets roll number is in the record
            print("Roll number already exists!")
            return

        stu_marks = list(map(float, input("Enter 5 subject marks(in one line ): ").split()))               #taking students marks of 5 subjects 
        if len(stu_marks) != 5:
            print("Enter exactly 5 marks.")                              #check if subject marks give are less than 5 
            return

        percentage = sum(stu_marks) / 5              #count percentage and assignes grade 
        stu_grades = calculate_grade(percentage)

        All_students[stu_rno] = {               #dictionary created to store data
            "Name": stu_name,
            "Marks": stu_marks,
            "Percentage": percentage,
            "Grade": stu_grades
        }
        print("Record added successfully!")              #checks if record added if not prints error 
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def view_all():                         #function executes and views all students stored
    if not All_students:                #if the data is empty this gets executed
        print("No records found.")
        return
    for rno, info in All_students.items():          #prints all items in the dictionary
        print(f"Roll: {rno} | Name: {info['Name']} | %: {info['Percentage']:.2f} | Grade: {info['Grade']}")

def search_student():      #this block to check and searh the student fromthe dictionary
    try:
        stu_rno = int(input("Enter roll number to search: "))
        if stu_rno in All_students:             #if student is in the dictionary then it will get executed
            info = All_students[stu_rno]
            print(f"Name: {info['Name']} | Roll: {stu_rno} | %: {info['Percentage']:.2f} | Grade: {info['Grade']}")
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input! Roll number must be a number.")    # or will print this error if inut is not as expected 

def update_student():            #this block will be executed when user whats to update the data from the dictionary 
    try: 
        stu_rno = int(input("Enter roll number to update: "))     #to update roll number
        if stu_rno in All_students:
            new_name = input("Enter new name (leave blank to keep same): ")     #to update name
            if new_name:
                All_students[stu_rno]["Name"] = new_name
            new_marks = input("Enter new 5 subject marks (leave blank to keep same): ")    #to update 5 subject marks
            if new_marks:
                marks = list(map(float, new_marks.split()))
                if len(marks) == 5:
                    All_students[stu_rno]["Marks"] = marks
                    All_students[stu_rno]["Percentage"] = sum(marks) / 5
                    All_students[stu_rno]["Grade"] = calculate_grade(All_students[stu_rno]["Percentage"])
            print("Record updated successfully!")
        else:
            print("Student not found.")
    except ValueError:          #prints error if input is wrong
        print("Invalid input! Roll number must be a number.")


def delete_student():      #this block will be executed when user whats to delete the data from the dictionary 
    try:
        stu_rno = int(input("Enter roll number to delete: "))  #to delete students through roll number
        if stu_rno in All_students:
            del All_students[stu_rno]
            print("Record deleted successfully!")       #prints when option was performed sucessfully 
        else:
            print("Student not found.")         #error
    except ValueError:
        print("Invalid input! Roll number must be a number.")


def save_final_output():                                 #saves the final output using file. function into an .txt file
    with open("final_output_for_vedants_student_project.txt", "w") as file:           #or creates a file named final_output_for_vedants_student_project.txt in write mode
        file.write("Final Student Records\n")
        file.write("=====================\n")
        if All_students:
            for rno, info in All_students.items():
                file.write(f"Roll: {rno} | Name: {info['Name']} | %: {info['Percentage']:.2f} | Grade: {info['Grade']}\n")
        else:
            file.write("No student records found.\n")
    print("Final output saved to final_output_for_vedants_student_project.txt")


while True:                                                 #options list 
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("\n| 1. Add | 2. View | 3. Search |  4. Update | 5. Delete |  6. Exit |")
    try:
        choice = int(input("\nEnter choice: "))
        if choice == 1:
            add_student()           #add
        elif choice == 2:
            view_all()              #view data
        elif choice == 3:
            search_student()        #search data
        elif choice == 4:
            update_student()        #update data
        elif choice == 5:
            delete_student()        #delete data 
        elif choice == 6:
            print("Exiting...")     #exits the program
            save_final_output()
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input! Please enter a number between 1–6.") #error 
