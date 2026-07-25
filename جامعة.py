# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:58:01 2026

@author: lenovo
"""

import sqlite3

# إنشاء اتصال بقاعدة البيانات (إذا ما كانت موجودة سيتم إنشاؤها)
conn = sqlite3.connect("university.db")

# إنشاء cursor للتعامل مع SQL
cursor = conn.cursor()




conn.commit()

cursor.execute("""
SELECT s.name, m.major_name
FROM students s
JOIN majors m
ON s.major_id = m.id
""")

rows = cursor.fetchall()
for row in rows:
    print(row)
    
cursor.execute("""
SELECT s.name, s.age, m.major_name
FROM students s
JOIN majors m
ON s.major_id = m.id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)



cursor.execute("""
SELECT s.name, s.age, m.major_name
FROM students s
JOIN majors m ON s.major_id = m.id
""")

rows = cursor.fetchall()

print("\n--- Students List ---")
for row in rows:
    print(f"Name: {row[0]}, Age: {row[1]}, Major: {row[2]}")
 
 
import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

while True:
    print("\n===== STUDENT SYSTEM =====")
    print("1- Add Student")
    print("2- Show Students")
    print("3- Exit")

    choice = input("Choose option: ")

    # ➜ إضافة طالب
    if choice == "1":
        
    # ➜ عرض الطلاب
    elif choice == "2":
        

    # ➜ خروج
    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("❌ Invalid choice")
        
''''''''''''''


    


while True:
    print("\n===== STUDENT SYSTEM =====")
    print("1- Add Student")
    print("2- Show Students")
    print("3- Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")
        





def add_course():
    try:
        course_code = input("Enter course code: ")
        course_name = input("Enter course name: ")
        credit_hours = int(input("Enter credit hours: "))
        major_id = int(input("Enter major id: "))

        cursor.execute("""
            INSERT INTO courses (course_code, course_name, credit_hours, major_id)
            VALUES (?, ?, ?, ?)
        """, (course_code, course_name, credit_hours, major_id))

        conn.commit()
        print("تمت إضافة المادة بنجاح.")

    except ValueError:
        print("خطأ: يجب إدخال أرقام صحيحة للساعات أو رقم التخصص.")

    except Exception as e:
        print("حدث خطأ:", e)

 
      

    
def show_courses():
    cursor.execute("""
        SELECT c.course_code,
               c.course_name,
               c.credit_hours,
               m.major_name
        FROM courses c
        LEFT JOIN majors m
        ON c.major_id = m.id
    """)

    rows = cursor.fetchall()

    print("\n--- Courses List ---")
    for row in rows:
        print(
            f"Code: {row[0]}, "
            f"Course: {row[1]}, "
            f"Credit Hours: {row[2]}, "
            f"Major: {row[3]}"
        )   




طلب:
student_id
course_id
grade
إضافة سجل إلى جدول enrollments.
حفظ التغييرات بـ conn.commit().
               
def enroll_student():
    try:
        student_id = int(input("Enter student id: "))
        course_id = int(input("Enter course id: "))
        grade = float(input("Enter grade: "))
        
        cursor.execute("""
            INSERT INTO enrollments (student_id, course_id, grade)
            VALUES (?, ?, ?)
        """, (student_id, course_id, grade))

        conn.commit()
        print("تم التسجيل بنجاح.")

    except ValueError:
        print("خطأ: يجب إدخال أرقام صحيحة رقم الطالب أو رقم المادة.")

    except Exception as e:
        print("حدث خطأ:", e)

تقوم بـ:

طلب student_id.
طلب العمر الجديد.
طلب major_id الجديد.
تحديث بيانات الطالب.
حفظ التغييرات.
طباعة رسالة نجاح.



لمطلوب:

طلب student_id.
حذف الطالب.
حفظ التغييرات.
معالجة الأخطاء بـ try/except.
    


    


cursor.execute("""
SELECT major_name ,count(s.id)
FROM majors m
LEFT JOIN students s
on m.id = s.major_id
GROUP BY m.name
""")

cursor.execute("""
SELECT s.name ,avg(e.grade)
FROM students s
LEFT JOIN enrollments e
on s.id = e.student_id
GROUP BY s.name
""")



