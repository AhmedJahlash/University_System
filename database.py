# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:29:44 2026

@author: lenovo
"""

import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS majors (
        id INTEGER PRIMARY KEY,
        major_name TEXT NOT NULL UNIQUE
    )
    """)

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        major_id INTEGER,
        foreign key (major_id) references majors (id)
    )
    """)

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        course_code TEXT NOT NULL UNIQUE,
        course_name TEXT NOT NULL,
        credit_hours INTEGER
    )
    """)

    
    cursor.execute("""
                   create table if not exists enrollments(
                       id integer primary key ,
                       student_id integer NOT NULL,
                       course_id integer NOT NULL,
                       grade real ,
                       foreign key (student_id) references students (id),
                       foreign key (course_id) references courses (id),
                       UNIQUE(student_id, course_id)
                       )
                   """)
                   
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS course_majors (
    id INTEGER PRIMARY KEY,
    major_id INTEGER not null,
    course_id INTEGER not null,
    FOREIGN KEY (major_id) REFERENCES majors(id),
    FOREIGN KEY (course_id) REFERENCES courses(id),
    UNIQUE(major_id, course_id)
)
    """)
    
    conn.commit()
    
    

def close_connection():
    conn.close()
