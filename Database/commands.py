def getStudentSQL(database):
    sql = ("SELECT * FROM students WHERE status ='1'")
    database.cursor.execute(sql)
    result = database.cursor.fetchall()
    return result


def addStudentSQL(student, database):
    sql = ("INSERT INTO students(name, class, math, english, bangla, marks, mathDays, englishDays, banglaDays, earnings, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    database.cursor.execute(sql, (student['name'], student['class'], student['math'], student['english'], student['bangla'], student['marks'], student['mathDays'], student['englishDays'], student['banglaDays'], student['earnings'], student['status']))
    database.db.commit()


def deleteStudentSQL(student, database):
    sql = ("UPDATE students SET status = %s WHERE name = %s AND class = %s")
    database.cursor.execute(sql, (0, student['name'], student['class'],))
    database.db.commit()


def updateStudentSQL(student, database):
    sql = ("UPDATE students SET math = %s, english = %s, bangla = %s, mathDays = %s, englishDays = %s, banglaDays = %s, marks = %s, earnings = %s WHERE name = %s")
    database.cursor.execute(sql, (student['math'], student['english'], student['bangla'], student['mathDays'], student['englishDays'],  student['banglaDays'], student['marks'], student['earnings'], student['name'],))
    database.db.commit()

