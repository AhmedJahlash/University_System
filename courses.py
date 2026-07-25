# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 10:57:52 2026

@author: lenovo
"""




from database import cursor, conn
from majors import show_majors


def add_course():
    try:
        course_code = input("Enter Course Code: ")
        course_name = input("Enter Course Name: ")
        credit_hours = int(input("Enter Credit Hours: "))

        cursor.execute("""
        INSERT INTO courses (course_code, course_name, credit_hours)
        VALUES (?, ?, ?)
        """, (course_code, course_name, credit_hours))

        conn.commit()
        print("✅ Course added successfully.")

    except ValueError:
        print("خطأ: يجب إدخال رقم صحيح لعدد الساعات.")

    except Exception as e:
        conn.rollback()
        print("حدث خطأ:", e)
    
def assign_course_to_major():
    show_majors()
    show_courses()
    try:
        major_id =int(input("Enter Major ID:"))
        course_id= int(input("Enter Course ID:"))

        cursor.execute("""
        INSERT INTO course_majors (major_id,course_id)
        VALUES (?, ?)
        """, (major_id,course_id))

        conn.commit()
        print("✅ course majors added!")
    except ValueError:
        print("خطأ: يجب إدخال رقم لرقم التخصص و رقم المادة.")

    except Exception as e:
        conn.rollback()
        print("حدث خطأ:", e)
        
def show_courses():
    cursor.execute("""
    SELECT c.course_code, c.course_name, c.credit_hours, m.major_name
    FROM courses c
    LEFT JOIN course_majors cm
    ON c.id = cm.course_id
    LEFT JOIN majors m
    ON cm.major_id = m.id
    """)

    rows = cursor.fetchall()

    if not rows:
        print("No courses found.")
    else:
        print("\n--- Courses List ---")
        for row in rows:
            print(
                f"Course Code: {row[0]}, "
                f"Course Name: {row[1]}, "
                f"Credit Hours: {row[2]}, "
                f"Major: {row[3]}"
            )
            



            
def update_course():
    try:
        course_id =int( input("Enter course id:"))
        course_code =input("Enter new course code:")
        course_name =input("Enter new course name:")
        credit_hours=int( input("Enter credit hours:"))

        cursor.execute("""
UPDATE courses
SET course_code = ?, course_name = ? , credit_hours = ?
WHERE id = ?
""", (course_code, course_name, credit_hours,course_id ))

        if cursor.rowcount == 0:
            print("❌ course not found.")
        else:
            conn.commit()
            print("✅ course updated successfully.")

    except ValueError:
        print("خطأ: يجب إدخال أرقام صحيحة رقم المادة و عدد الساعات.")

    except Exception as e:
         conn.rollback()
         print("حدث خطأ:", e)
         
def delete_course():
    try:
        course_id = int(input("Enter course id: "))

        cursor.execute("""
        SELECT COUNT(*)
        FROM course_majors
        WHERE course_id = ?
        """, (course_id,))

        course_major_count = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*)
        FROM enrollments
        WHERE course_id = ?
        """, (course_id,))

        enrollment_count = cursor.fetchone()[0]

        if course_major_count == 0 and enrollment_count == 0:

            cursor.execute("""
            DELETE FROM courses
            WHERE id = ?
            """, (course_id,))

            if cursor.rowcount == 0:
                print("❌ course not found.")
            else:
                conn.commit()
                print("✅ course deleted successfully.")

        else:
            print("❌ Cannot delete course. It has  course_majors or enrollments.")

    except ValueError:
        print("خطأ: يجب إدخال رقم صحيح لمادة.")

    except Exception as e:
        conn.rollback()
        print("حدث خطأ:", e)

def courses_menu():
    while True:
        print("\n===== Courses Management =====")
        print("1- Add Course")
        print("2- Show Courses")
        print("3- Assign Course To Major")
        print("4- Update Course")
        print("5- Delete Course")
        print("6- Back")

        choice = input("Choose option: ")

        if choice == "1":
            add_course()

        elif choice == "2":
            show_courses()

        elif choice == "3":
            assign_course_to_major()

        elif choice == "4":
            update_course()

        elif choice == "5":
            delete_course()

        elif choice == "6":
            break

        else:
            print("Invalid choice")
   
