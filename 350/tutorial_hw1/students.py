import sqlite3

db = sqlite3.connect("school.db")
db.execute("PRAGMA foreign_keys=on") 
cursor = db.cursor()

cursor.execute('''CREATE TABLE student (
    studentID int PRIMARY KEY, 
    stdname text, 
    stdage int)''')

cursor.execute('''CREATE TABLE registered_courses (
    studentID int, 
    courseID text,
    FOREIGN KEY(studentID) REFERENCES student(studentID))''')

cursor.execute('''CREATE TABLE grades (
    studentID int, 
    courseID text, 
    grade real,
    FOREIGN KEY(studentID) REFERENCES student(studentID))''')

db.commit()
cursor.execute('''SELECT studentID, courseID, MAX(grade) 
                  FROM grades 
                  GROUP BY studentID''')
max_grades = cursor.fetchall() 
cursor.execute('''SELECT studentID, AVG(grade) 
                  FROM grades 
                  GROUP BY studentID''')
avg_grades = cursor.fetchall()

db.close()