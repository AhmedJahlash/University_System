# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 09:57:54 2026

@author: lenovo
"""

from database import cursor, conn


def add_major():
    try:
        major_name = input("Enter major name: ")
      
        cursor.execute("""
            INSERT INTO majors (major_name)
            VALUES (?)
        """, (major_name,))

        conn.commit()
        print("تمت إضافة التخصص بنجاح.")

    except Exception as e:
        print("❌ Major already exists.", e)
        
def show_majors():
    cursor.execute("""
    SELECT *
    FROM majors
    order by id asc
    """)

    rows = cursor.fetchall()
    
    if not rows:
        print("majors not found.")
    else:
        print("\n--- majors List ---")
        for row in rows:
            print(f"id: {row[0]}, major_name: {row[1]}")
            
def update_major():
    try:
        major_id =int(input("Enter major id: "))
        major_name =input("Enter major name: ")

        cursor.execute("""
UPDATE majors
SET  major_name = ?
WHERE id = ?
""", (major_name, major_id))

        if cursor.rowcount == 0:
            print("❌ major not found.")
        else:
            conn.commit()
            print("✅ major updated successfully.")

    except ValueError:
        print("خطأ: يجب إدخال أرقام صحيحة رقم التخصص ")

    except Exception as e:
         conn.rollback()
         print("حدث خطأ:", e)
         
         
def delete_major():
    try:
        major_id = int(input("Enter major id: "))

        cursor.execute("""
        SELECT COUNT(*)
        FROM students
        WHERE major_id = ?
        """, (major_id,))

        student_count = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*)
        FROM courses
        WHERE major_id = ?
        """, (major_id,))

        course_count = cursor.fetchone()[0]

        if student_count == 0 and course_count == 0:

            cursor.execute("""
            DELETE FROM majors
            WHERE id = ?
            """, (major_id,))

            if cursor.rowcount == 0:
                print("❌ Major not found.")
            else:
                conn.commit()
                print("✅ Major deleted successfully.")

        else:
            print("❌ Cannot delete major. It has students or courses.")

    except ValueError:
        print("خطأ: يجب إدخال رقم صحيح للتخصص.")

    except Exception as e:
        conn.rollback()
        print("حدث خطأ:", e)
        
def majors_menu():
    while True:
        print("\n===== Majors Management =====")
        print("1- Add Major")
        print("2- Show Majors")
        print("3- Update Major")
        print("4- Delete Major")
        print("5- Back")

        choice = input("Choose option: ")

        if choice == "1":
            add_major()

        elif choice == "2":
            show_majors()

        elif choice == "3":
            update_major()

        elif choice == "4":
            delete_major()

        elif choice == "5":
            break

        else:
            print("Invalid choice")