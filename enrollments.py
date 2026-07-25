# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:15:31 2026

@author: lenovo
"""

from database import cursor, conn
from students import show_students
from courses import show_courses



def enroll_student():
    show_students()
    show_courses()

    try:
        student_id = int(input("Enter Student ID: "))
        course_id = int(input("Enter Course ID: "))
        grade = float(input("Enter Grade: "))

        cursor.execute("""
        INSERT INTO enrollments (student_id, course_id, grade)
        VALUES (?, ?, ?)
        """, (student_id, course_id, grade))

        conn.commit()
        print("✅ Enrollment added successfully.")

    except ValueError:
        print("خطأ: يجب إدخال أرقام صحيحة.")

    except Exception as e:
        conn.rollback()
        print("حدث خطأ:", e)
    

def show_enrollments():
    cursor.execute("""
    SELECT s.name, c.course_code, c.course_name, e.grade
    FROM students s
    left JOIN enrollments e ON s.id = e.student_id
    left JOIN courses c ON e.course_id = c.id
    """)

    rows = cursor.fetchall()
    
    if not rows:
        print("No Enrollments  found.")
    else:
        print("\n--- Enrollments  List ---")
        for row in rows:
            print(f"Name: {row[0]}, Course_Code: {row[1]}, Course_Name: {row[2]},Grade: {row[3]} ")

    
def update_grade():
    try:
        show_enrollments()
        print()

        student_id =int( input("Enter student id:"))
        course_id =int( input("Enter course id:"))
        grade = float(input("Enter New Grade: "))
        
        
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return

        cursor.execute("""
UPDATE enrollments
SET grade = ?
WHERE student_id = ? and course_id = ?
""", (grade, student_id, course_id))

        if cursor.rowcount == 0:
            print("❌ Enrollment not found.")
        else:
            conn.commit()
            print("✅ Enrollment updated successfully.")

    except ValueError:
        print("خطأ: يجب إدخال أرقام صحيحة")

    except Exception as e:
         conn.rollback()
         print("حدث خطأ:", e)
         
         
def delete_enrollment():
    try:
        show_enrollments()

        student_id = int(input("Enter student id: "))
        course_id = int(input("Enter course id: "))

        cursor.execute("""
        DELETE FROM enrollments
        WHERE student_id = ? AND course_id = ?
        """, (student_id, course_id))

        if cursor.rowcount == 0:
            print("❌ Enrollment not found.")
        else:
            conn.commit()
            print("✅ Enrollment deleted successfully.")

    except ValueError:
        print("خطأ: يجب إدخال رقم صحيح للطالب ورقم المادة.")

    except Exception as e:
        conn.rollback()
        print("حدث خطأ:", e)
        
def enrollments_menu():
    while True:
        print("\n===== Enrollments Management =====")
        print("1- Enroll Student")
        print("2- Show Enrollments")
        print("3- Update Grade")
        print("4- Delete Enrollment")
        print("5- Back")

        choice = input("Choose option: ")

        if choice == "1":
            enroll_student()

        elif choice == "2":
            show_enrollments()

        elif choice == "3":
            update_grade()

        elif choice == "4":
            delete_enrollment()

        elif choice == "5":
            break

        else:
            print("Invalid choice")