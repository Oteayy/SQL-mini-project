from models import Student
from db import create_table, insert_student, get_students, get_student_by_id

create_table()

insert_student(Student("Ana", "Anić", 2000))
insert_student(Student("Marko", "Marić", 1998))
insert_student(Student("Iva", "Ivić", 2001))

print("Lista studenata:")
for s in get_students():
    print(s)

print("\n Student s ID=2:")
print(get_student_by_id(2))
