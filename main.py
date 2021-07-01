from student import *
from Database.database import *

database = Database()
student = Student(database)


while True:
    print("\n")
    print("* To add a student --> Enter 1")
    print("* To delete a student --> Enter 2")
    print("* To edit a student --> Enter 3")
    print("* To see all the students --> Enter 4")
    print("* Other infos --> Enter 5")
    print("* To exit --> Enter 0")
    print("\n")
    value = input("What you want to do? ")
    print("\n")

    
    if value == '0':
        break
    elif value == '1':
        student.addStudent(database)
    elif value == '2':
        student.deleteStudent(database)
    elif value == '3':
        student.editStudent(database)
    elif value == '4':
        classNo = input("Which class you wanna see? (8/9/10): ")
        student.showStudents(classNo)

        more = input("Wanna see anyone's details? (Y/N): ")
        if more == 'Y':
            name = input("Student's name: ")
            student.showStudent(classNo, name)
    elif value == '5':
        total_days_all_class = student.getTotalDaysAllClasses()
        total_days_specific_class = student.getTotalDaysSingleClass()
        total_earnings = student.getTotalEarn()
        total_earnings_subject = student.getTotalSubjectEarn()
        total_earnings_class = student.getTotalClassEarn()
        average_marks = student.getAverageMark()

        print("Total days taught across all classes: ", total_days_all_class)
        print("Total days taught across individual classes: ", total_days_specific_class)
        print("Total earnings: ", total_earnings)
        print("Total earnings of individual classes: ", total_earnings_class)
        print("Total earnings of individual subjects: ", total_earnings_subject)
        print("Average marks: ", average_marks)
                                          
    else:
        print("Invalid choice, please choose carefully.....")

    print("\n")
    print("==================================================")
    
