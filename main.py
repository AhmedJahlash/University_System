# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:29:48 2026

@author: lenovo
"""


from students import students_menu
from majors import majors_menu
from courses import courses_menu
from enrollments import enrollments_menu
from reports import reports_menu
from database import create_tables, close_connection

create_tables()



while True:
     print("\n===== UNIVERSITY SYSTEM =====")
     print("1- Students Management")
     print("2- Majors Management")
     print("3- Courses Management")
     print("4- Enrollments Management")
     print("5- Reports")
     print("6- Exit")

     choice = input("Choose option: ")

     if choice == "1":
         students_menu()

     elif choice == "2":
         majors_menu()
         
     elif choice == "3":
         courses_menu()
         
     elif choice == "4":
         enrollments_menu()
         
     elif choice == "5":
         reports_menu()

     elif choice == "6":
         print("Goodbye 👋")
         close_connection()
         break

     else:
         print("Invalid choice")   
    



    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    