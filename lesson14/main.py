from student import Student

student1 = Student("Олена", "Ковальчук", 20, 89.5)

print("Початкова інформація про студента:")
student1.display_info()

student1.update_average_grade(93.2)

print("\nОновлена інформація про студента:")
student1.display_info()
