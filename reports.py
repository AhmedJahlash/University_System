# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:51:20 2026

@author: lenovo
"""

from database import cursor, conn


def students_per_major():
    cursor.execute("""
    SELECT m.major_name, COUNT(s.id)
    FROM majors m
    LEFT JOIN students s
    ON m.id = s.major_id
    GROUP BY m.id, m.major_name
    """)

    rows = cursor.fetchall()

    if not rows:
        print("No data found.")
    else:
        print("\n----- Students Per Major -----")
        for row in rows:
            print(f"Major: {row[0]}, Students: {row[1]}")
            
def students_per_course():
    cursor.execute("""
    SELECT c.course_name, COUNT(e.student_id)
    FROM courses c
    LEFT JOIN enrollments e
    ON c.id = e.course_id
    GROUP BY c.id, c.course_name
    """)

    rows = cursor.fetchall()

    if not rows:
        print("No data found.")
    else:
        print("\n----- Students Per Course  -----")
        for row in rows:
            print(f"Course: {row[0]}, Students: {row[1]}")
            
def student_average():
    cursor.execute("""
    SELECT s.name ,avg(e.grade)
    FROM students s
    LEFT JOIN enrollments e
    on s.id = e.student_id
    GROUP BY s.id, s.name
    """)
    
    rows = cursor.fetchall()

    if not rows:
        print("No data found.")
    else:
        print("\n----- Student Averages -----")
        for row in rows:
             average = row[1]
             if average is None:
                 average = "No grades"
             else:
                 average = f"{average:.2f}"

             print(f"Student: {row[0]}, Average: {average}")

def highest_average_student():
    cursor.execute("""
    SELECT s.name, AVG(e.grade)
    FROM students s
    JOIN enrollments e
    ON s.id = e.student_id
    GROUP BY s.id, s.name
    ORDER BY AVG(e.grade) DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    if row:
        print("\n----- Highest Average Student -----")
        print(f"Student: {row[0]}, Average: {row[1]:.2f}")
    else:
        print("No data found.")
        
def courses_by_enrollment():
    cursor.execute("""
    SELECT c.course_name, COUNT(e.student_id)
    FROM courses c
    LEFT JOIN enrollments e
    ON c.id = e.course_id
    GROUP BY c.id, c.course_name
    ORDER BY COUNT(e.student_id) DESC
    """)

    rows = cursor.fetchall()

    if not rows:
        print("No data found.")
    else:
        print("\n----- Courses Ordered By Enrollment -----")
        for row in rows:
            print(f"Course: {row[0]}, Students: {row[1]}")
            
def reports_menu():
    while True:
        print("\n===== Reports =====")
        print("1- Students Per Major")
        print("2- Students Per Course")
        print("3- Student Averages")
        print("4- Highest Average Student")
        print("5- Courses By Enrollment")
        print("6- Back")

        choice = input("Choose option: ")

        if choice == "1":
            students_per_major()

        elif choice == "2":
            students_per_course()

        elif choice == "3":
            student_average()

        elif choice == "4":
            highest_average_student()

        elif choice == "5":
            courses_by_enrollment()

        elif choice == "6":
            break

        else:
            print("Invalid choice")
    
    
            
    