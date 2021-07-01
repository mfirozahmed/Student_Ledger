from Database.commands import *

STUDENT_NOT_FOUND = 0

class Student:

    def __init__(self, database):
        self.students = []

        allStudents = getStudentSQL(database)
        for eachStudent in allStudents:
            if eachStudent[11] == 1:
                student = {
                    'name': eachStudent[1],
                    'class': eachStudent[2],
                    'math': eachStudent[3],
                    'english': eachStudent[4],
                    'bangla': eachStudent[5],
                    'marks': eachStudent[6],
                    'mathDays': eachStudent[7],
                    'englishDays': eachStudent[8],
                    'banglaDays': eachStudent[9],
                    'earnings': eachStudent[10],
                    'status': eachStudent[11]
                }
                self.students.append(student)

    def getStudent(self, name, classNo):
        for eachStudent in self.students:
            if eachStudent['name'] == name and eachStudent['class'] == classNo:
                return eachStudent
        return STUDENT_NOT_FOUND

    def getAllStudent(self, classNo):
        students = []
        for eachStudent in self.students:
            if eachStudent['class'] == classNo:
                students.append(eachStudent)
        if len(students) < 1:
            return STUDENT_NOT_FOUND
        return students

    def addStudent(self, database):
        classNo = input("Select class (8/9/10): ")
        name = input("Name: ")

        student = self.getStudent(name, classNo)
        if student != STUDENT_NOT_FOUND:
            print("Student Already Added.....")
            return

        math = input("Teach math (Yes/No): ")
        math = 1 if math == "Yes" else 0
        english = input("Teach english (Yes/No): ")
        english = 1 if english == "Yes" else 0
        bangla = input("Teach bangla (Yes/No): ")
        bangla = 1 if bangla == "Yes" else 0
        marks = 0
        mathDays = 0
        englishDays = 0
        banglaDays = 0
        earnings = 0
        status = 1

        student = {
            'name': name,
            'class': classNo,
            'math': math,
            'english': english,
            'bangla': bangla,
            'marks': marks,
            'mathDays': mathDays,
            'englishDays': englishDays,
            'banglaDays': banglaDays,
            'earnings': earnings,
            'status': status
        }

        addStudentSQL(student, database)
        self.students.append(student)
        print("\nStudent Added")
    
    def deleteStudent(self, database):
        classNo = input("Select class (8/9/10): ")
        name = input("Name: ")

        student = self.getStudent(name, classNo)
        print(student)
        if student == STUDENT_NOT_FOUND:
            print("Student Not Found.....")
            return

        deleteStudentSQL(student, database)
        newStudentList = []
        for eachStudent in self.students:
            print(eachStudent['name'])
            if eachStudent['name'] != name:
                newStudentList.append(eachStudent)
            else:
                if eachStudent['class'] != classNo:
                    newStudentList.append(eachStudent)
        self.students = newStudentList
        
        print("\nStudent Deleted")

    def editStudent(self, database):
        classNo = input("Select class (8/9/10): ")
        name = input("Name: ")

        student = self.getStudent(name, classNo)
        if student == STUDENT_NOT_FOUND:
            print("Student Not Found.....")
            return

        choose = int(input("Want to add days or marks? Choose 1 for days and 2 for marks: "))
        if choose == 1:
            subject = input("Subject (Math/English/Bangla): ")
            days = int(input("Days: "))
            if subject == 'Math':
                student['math'] = 1
                student['mathDays'] += days
            elif subject == 'English':
                student['english'] = 1
                student['englishDays'] += days
            else:
                student['bangla'] = 1
                student['banglaDays'] += days
        else:
            marks = int(input("Marks: "))
            student['marks'] = marks

        student['earnings'] = student['mathDays'] + student['englishDays'] + student['banglaDays']
        
        updateStudentSQL(student, database)
        
        print("\nStudent Updated")

    def showStudents(self, classNo):
        students = self.getAllStudent(classNo)
        if students == 0:
            print("No Student!!!")
            return
        print("Name               Earnings               Marks")
        for eachStudent in students:
            print(eachStudent['name'], end="")
            nameLength = len(eachStudent['name'])
            for i in range(22 - nameLength):
                print(" ", end="")
            print(eachStudent['earnings'], end="")
            earningsLength = len(str(eachStudent['earnings']))
            for i in range(22 - earningsLength):
                print(" ", end="")

            print(eachStudent['marks'])
        print()

    def showStudent(self, classNo, name):
        student = self.getStudent(name, classNo)
        if student == 0:
            print("No Student Found!!!")
            return

        print("Name   Class    Math    English   Bangla   Days   Earnings   Marks")
        print(student['name'], end="")
        nameLength = len(student['name'])
        value = 9
        for i in range(value - nameLength):
            print(" ", end="")

        print(student['class'], end="")
        classLength = len(student['class'])
        for i in range(value - classLength):
            print(" ", end="")

        print(student['math'], end="")
        mathLength = len(str(student['math']))
        for i in range(value - mathLength):
            print(" ", end="")

        print(student['english'], end="")
        englishLength = len(str(student['english']))
        for i in range(value - englishLength):
            print(" ", end="")
            
        print(student['bangla'], end="")
        banglaLength = len(str(student['bangla']))
        for i in range(value - banglaLength):
            print(" ", end="")


        days = student['mathDays'] + student['englishDays'] + student['banglaDays'] 
        print(days, end="")
        daysLength = len(str(days))
        for i in range(value - daysLength):
            print(" ", end="")

        print(student['earnings'], end="")
        earningsLength = len(str(student['earnings']))
        for i in range(value - earningsLength):
            print(" ", end="")

        print(student['marks'])
        print()

    def getTotalDaysAllClasses(self):
        count = 0
        for eachStudent in self.students:
            count += int(eachStudent['mathDays'])
            count += int(eachStudent['englishDays'])
            count += int(eachStudent['banglaDays'])
        return count

    def getTotalDaysSingleClass(self):
        class8, class9, class10 = 0, 0, 0
        for eachStudent in self.students:
            if eachStudent['class'] == '8':
                class8 += (int(eachStudent['mathDays']) + int(eachStudent['englishDays']) + int(eachStudent['banglaDays']))
            elif eachStudent['class'] == '9':
                class9 += (int(eachStudent['mathDays']) + int(eachStudent['englishDays']) + int(eachStudent['banglaDays']))
            else:
                class10 += (int(eachStudent['mathDays']) + int(eachStudent['englishDays']) + int(eachStudent['banglaDays']))

        data = {
            "Class 8": class8,
            "Class 9": class9,
            "Class 10": class10
        }
        return data

    def getTotalEarn(self):
        count = 0
        for eachStudent in self.students:
            count += int(eachStudent['earnings'])
        return count

    def getTotalClassEarn(self):
        class8, class9, class10 = 0, 0, 0
        for eachStudent in self.students:
            if eachStudent['class'] == '8':
                class8 += (int(eachStudent['mathDays']) + int(eachStudent['englishDays']) + int(eachStudent['banglaDays']))
            elif eachStudent['class'] == '9':
                class9 += (int(eachStudent['mathDays']) + int(eachStudent['englishDays']) + int(eachStudent['banglaDays']))
            else:
                class10 += (int(eachStudent['mathDays']) + int(eachStudent['englishDays']) + int(eachStudent['banglaDays']))

        value_for_each_class = 1
        data = {
            "Class 8": class8*value_for_each_class,
            "Class 9": class9*value_for_each_class,
            "Class 10": class10*value_for_each_class
        }
        return data
    
    def getTotalSubjectEarn(self):
        math, english, bangla = 0, 0, 0
        for eachStudent in self.students:
            math += int(eachStudent['mathDays'])
            english += int(eachStudent['englishDays']) 
            bangla += int(eachStudent['banglaDays'])

        value_for_each_class = 1
        data = {
            "Math": math*value_for_each_class,
            "English": english*value_for_each_class,
            "Bangla": bangla*value_for_each_class
        }

        return data

    def getAverageMark(self):
        count = 0
        for eachStudent in self.students:
            if eachStudent['status'] == 1:
                count += int(eachStudent['marks'])
        return count/len(self.students)
