import student
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="ssisv2"
)

def check_course(coursecode):
    cursor = db.cursor()

    # Execute the query to check if course_code exists in the database
    query = "SELECT coursecode FROM course WHERE LOWER(coursecode) = LOWER(%s)"
    cursor.execute(query, (coursecode,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        # Prompt user to add the course if it doesn't exist in the database
        while True:
            print("Course not found in the database. Do you want to add it?\n[1] Yes\n[2] No")
            option = input("Enter your choice (1 or 2): ")
            if option == '1':
                add_course2(coursecode)  # Replace with your function to add the course to the database
                return True
            elif option == '2':
                break

    return False

def add_course():
    cursor = db.cursor()

    course_already_added = False
    coursecode = input("Enter Course Code: ")

    # Execute the query to check if course_code exists in the database
    query = "SELECT coursecode FROM course WHERE LOWER(coursecode) = LOWER(%s)"
    cursor.execute(query, (coursecode,))
    result = cursor.fetchone()

    if result:
        print("Course", coursecode.upper(), "already added!\n")
        course_already_added = True
    else:
        add_course2(coursecode)  # Call the function to add the course to the database

    if not course_already_added:
        print("Course added successfully!\n")


def add_course2(coursecode):
    cursor = db.cursor()

    coursename = input("Enter Course Title: ")

    # Execute the query to insert the course into the database
    query = "INSERT INTO course (course_code, coursename) VALUES (%s, %s)"
    values = (coursecode.upper(), coursename)
    cursor.execute(query, values)
    db.commit()


def view_course():
    cursor = db.cursor()

    query = "SELECT * FROM course"
    cursor.execute(query)
    data = cursor.fetchall()

    # Print the student data
    print("Course Code, Course Name")
    for row in data:
        print(row[0], "-", row[1])
    print()

def edit_course():
    cursor = db.cursor()

    # Execute the query to fetch course data from the database
    query = "SELECT * FROM course"
    cursor.execute(query)
    data = cursor.fetchall()

    ccode = input("Enter Course Code to be edited: ")
    found = False
    for row in data:
        if row[0].upper() == ccode.upper():
            found = True
            new_coursename = input("Enter new Course Title (ex: BS Computer Science for BSCS): ") or row[1]
            query = "UPDATE course SET course_title = %s WHERE course_code = %s"
            values = (new_coursename, ccode.upper())
            cursor.execute(query, values)
            db.commit()
            print("Course", ccode.upper(), "edited successfully.\n")
            break
    if not found:
        print("Course", ccode.upper(), "not found!\n")


def delete_course():
    cursor = db.cursor()

    delCourseCode = input("Enter Course Code to be deleted: ")

    query = "SELECT coursecode FROM course WHERE LOWER(coursecode) = LOWER(%s)"
    cursor.execute(query, (delCourseCode,))
    result = cursor.fetchone()

    if result:
        while True:
            print("Are you sure to delete this course? Students under this course will also be deleted.\n[1] Yes\n[2] No")
            option = input("Enter your choice (1-2): ")
            if option == '1':
                if student.check_ccode(delCourseCode) is True:
                    student.deleteByCourse(delCourseCode)
                delete_query = "DELETE FROM course WHERE LOWER(coursecode) = LOWER(%s)"
                cursor.execute(delete_query, (delCourseCode,))
                db.commit()
                print("Course", delCourseCode.upper(), "deleted successfully.\n")
                break
            elif option == '2':
                print("Course", delCourseCode.upper(), "not deleted.\n")
                break
            else:
                print("Invalid choice.\n")
    else:
        print("Course", delCourseCode.upper(), "not found!\n")


def search_course():
    cursor = db.cursor()
    search_key = input("Enter Search Key: ")
    print()

    # Execute the query to search for students matching the search key
    query = "SELECT * FROM course WHERE coursecode LIKE %s OR coursename LIKE %s"
    values = (f"%{search_key}%", f"%{search_key}%")
    cursor.execute(query, values)
    results = cursor.fetchall()

    if results:
        found = True
        for row in results:
            print("Course Code: ", row[0])
            print("Course Title: ", row[1], "\n")
    else:
        found = False
        print("Course not found.\n")