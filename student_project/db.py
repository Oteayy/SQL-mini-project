import sqlite3
from models import Student

sql_create_table = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    birth_year INTEGER
)
'''
def create_table():
    conn = sqlite3.connect('students.sqlite3')
    cursor = conn.cursor()
    cursor.execute(sql_create_table)
    conn.commit()
    conn.close()
    
insert_sql = "INSERT INTO students (name, surname, birth_year) VALUES (?, ?, ?)"

def insert_student(student: Student):
    conn = sqlite3.connect("students.sqlite")
    cursor = conn.cursor()
    cursor.execute(insert_sql, (student.name, student.surname, student.birth_year))
    conn.commit()
    conn.close()

get_sql = "SELECT * FROM students"

def get_students():
    conn = sqlite3.connect("students.sqlite")
    cursor = conn.cursor()
    cursor.execute(get_sql)
    rows = cursor.fetchall()
    conn.close()
    
    return [Student(row[1], row[2], row[3]) for row in rows]


get_sql_by_id = "SELECT * FROM students WHERE id = ?"

def get_student_by_id(id):
    conn = sqlite3.connect("students.sqlite")
    cursor = conn.cursor()
    cursor.execute(get_sql_by_id, (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Student(row[1], row[2], row[3])
    return None