from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course
import random

# Підключення до БД
engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Створення курсів (якщо ще не створені)
course_names = ['Math', 'Physics', 'History', 'Biology', 'Programming']
if not session.query(Course).first():
    for name in course_names:
        session.add(Course(name=name))
    session.commit()

# Створення студентів та рандомна реєстрація на курси
course_list = session.query(Course).all()
if not session.query(Student).first():
    for i in range(1, 21):
        student = Student(name=f'Student {i}')
        student.courses = random.sample(course_list, k=random.randint(1, 3))
        session.add(student)
    session.commit()

# Додавання нового студента та запис на курс
def add_student_to_course(student_name, course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    if not course:
        print(f"Курс {course_name} не знайдено.")
        return
    student = Student(name=student_name)
    student.courses.append(course)
    session.add(student)
    session.commit()
    print(f"{student_name} додано до курсу {course_name}.")

add_student_to_course("Volodymyr Pol", "Math")

# Показати студентів певного курсу
def students_in_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    if course:
        print(f"Студенти на курсі {course_name}:")
        for student in course.students:
            print(f"- {student.name}")
    else:
        print("Курс не знайдено.")

students_in_course("Programming")

# Показати курси певного студента
def courses_of_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f"Курси для студента {student_name}:")
        for course in student.courses:
            print(f"- {course.name}")
    else:
        print("Студента не знайдено.")

courses_of_student("Student 3")

# Оновлення імені студента
def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()
        print(f"Ім'я оновлено: {old_name} -> {new_name}")
    else:
        print("Студента не знайдено.")

update_student_name("Volodymyr Pol", "Volodymyr Polishchuk")

# Видалення студента
def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Студент {name} видалений.")
    else:
        print("Студента не знайдено.")

delete_student("Student 20")

session.close()
