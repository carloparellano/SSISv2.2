import course
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="ssisv2"
)

def check_studentID(studentID):
    cursor = db.cursor()

    # Execute the query to check if studentID exists in the database
    query = "SELECT studentID FROM student WHERE studentID = %s"
    cursor.execute(query, (studentID,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False

def check_ccode(coursecode):
    cursor = db.cursor()

    query = "SELECT course FROM student WHERE LOWER(course) = LOWER(%s)"
    cursor.execute(query, (coursecode,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False


def add_student():
    cursor = db.cursor()

    studentID = input("Enter Student ID number: ")
    if check_studentID(studentID) is True:
        print("Student", studentID, "already exists.\n")
    else:
        fullname = input("Enter Student Full Name: ")
        gender = input("Enter Student's Gender: ")
        yearlevel = input("Enter Student Year Level: ")
        coursecode = input("Enter Course Code: ")
        if not course.check_course(coursecode):
            print("Add Course First.\n")
        else:
            query = "INSERT INTO student_info (studentID, fullname, gender, yearlevel, course) VALUES (%s, %s, %s, %s, %s)"
            values = (studentID, fullname, gender, yearlevel, coursecode)
            cursor.execute(query, values)
            db.commit()

            print("Student added successfully!\n")


def view_students():
    cursor = db.cursor()

    # Execute the query to fetch student data from the database
    query = "SELECT * FROM student"
    cursor.execute(query)
    data = cursor.fetchall()

    # Print the student data
    print("Course Code, Year Level, ID Number, Name, Gender")
    for row in data:
        print(row[4], row[3], row[0], "-", row[1], ",", row[2])
    print()


def delete_student():
    cursor = db.cursor()
    delstudentID = input("Enter Student ID number to be deleted: ")

    query = "DELETE FROM student WHERE studentID = %s"
    cursor.execute(query, (delstudentID,))
    db.commit()

    # Check if any rows were affected by the deletion
    if cursor.rowcount > 0:
        print("Student", delstudentID, "deleted successfully!\n")
    else:
        print("Student", delstudentID, "not found!\n")


def deleteByCourse(coursecode):
    cursor = db.cursor()
    query = "DELETE FROM student_info WHERE student_course = %s"
    cursor.execute(query, (coursecode,))
    db.commit()


def edit_student():
    cursor = db.cursor()

    # Execute the query to fetch student data from the database
    query = "SELECT * FROM student"
    cursor.execute(query)
    data = cursor.fetchall()

    studentID = input("Enter Student ID to edit: ")
    found = False
    for row in data:
        if row[0] == studentID:
            found = True
            print("Enter new student information:")
            new_name = input("Name: ") or row[1]
            new_gender = input("Gender: ") or row[2]
            new_yearlevel = input("Year Level: ") or row[3]
            new_coursecode = input("Course code: ") or row[4]
            if not course.check_course(new_coursecode):
                print("Student Information cannot be edited.\n")
            else:
                query = "UPDATE student SET fullname = %s, gender = %s, yearlevel = %s, coursecode = %s WHERE studentID = %s"
                values = (new_name, new_gender, new_yearlevel, new_coursecode, studentID)
                cursor.execute(query, values)
                db.commit()
                print("Student Information edited successfully.\n")
            break
    if not found:
        print("Student", studentID, "not found!\n")


def search_student():
    cursor = db.cursor()
    search_key = input("Enter Search Key: ")
    print()

    # Execute the query to search for students matching the search key
    query = "SELECT * FROM student WHERE studentID LIKE %s OR fullname LIKE %s OR gender LIKE %s OR yearlevel LIKE %s OR course LIKE %s"
    values = (f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%")
    cursor.execute(query, values)
    results = cursor.fetchall()

    if results:
        found = True
        for row in results:
            print("ID Number: ", row[0])
            print("Student Name: ", row[1])
            print("Gender: ", row[2])
            print("Year Level: ", row[3])
            print("Course Code: ", row[4], "\n")
    else:
        found = False
        print("Student not found.\n")