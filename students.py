# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:39:06 2026

@author: lenovo
"""

from database import cursor, conn



def add_student():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        major_id = int(input("Enter major id: "))

        cursor.execute("""
        INSERT INTO students (name, age, major_id)
        VALUES (?, ?, ?)
        """, (name, age, major_id))

        conn.commit()
        print("✅ Student added!")
    except ValueError:
        print("خطأ: يجب إدخال رقم صحيح العمر ورقم التخصص.")

    except Exception as e:
        conn.rollback()
        print("حدث خطأ:", e)
        
    
    

def show_students():
    cursor.execute("""
    SELECT s.name, s.age, m.major_name
    FROM students s
    JOIN majors m ON s.major_id = m.id
    """)

    rows = cursor.fetchall()
    
    if not rows:
        print("No Enrollments  found.")
    else:
        print("\n--- Students List ---")
        for row in rows:
            print(f"Name: {row[0]}, Age: {row[1]}, Major: {row[2]}")

    

def search_student():
    try:
        student_name = input("Enter student name: ")

        cursor.execute("""
        SELECT s.name, s.age, m.major_name
        FROM students s
        JOIN majors m
        ON s.major_id = m.id
        WHERE s.name LIKE ?
        """, (f"%{student_name}%",))

        rows = cursor.fetchall()

        if not rows:
            print("Student not found.")
        else:
            print("\n--- Students List ---")
            for row in rows:
                print(f"Name: {row[0]}, Age: {row[1]}, Major: {row[2]}")

    except Exception as e:
        print("حدث خطأ:", e)

def update_student():
    try:
        student_id =int( input("Enter student id: "))
        age =int(input("Enter age: "))
        major_id = int(input("Enter major id: "))

        cursor.execute("""
UPDATE students
SET age = ?, major_id = ?
WHERE id = ?
""", (age, major_id, student_id))

        if cursor.rowcount == 0:
            print("❌ Student not found.")
        else:
            conn.commit()
            print("✅ Student updated successfully.")

    except ValueError:
        print("خطأ: يجب إدخال أرقام صحيحة رقم الطالب أو العمر أو رقم التخصص.")

    except Exception as e:
         conn.rollback()
         print("حدث خطأ:", e)
        

    
def delete_student():
    try:
        student_id = int(input("Enter student id: "))

        cursor.execute("""
        DELETE FROM students
        WHERE id = ?
        """, (student_id,))

        if cursor.rowcount == 0:
            print("❌ Student not found.")
        else:
            conn.commit()
            print("✅ Student deleted successfully.")

    except ValueError:
        print("خطأ: يجب إدخال رقم صحيح للطالب.")

    except Exception as e:
        print("حدث خطأ:", e)
        
        
def students_menu():
    while True:
        print("\n===== Students Management =====")
        print("1- Add Students")
        print("2- Show Students")
        print("3- Search Students")
        print("4- Update Students")
        print("5- Delete Students")
        print("6- back")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()
            
        elif choice == "3":
            search_student()
            
        elif choice == "4":
            update_student()
        
        elif choice == "5":
            delete_student()

        elif choice == "6":
            break

        else:
            print("Invalid choice")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    