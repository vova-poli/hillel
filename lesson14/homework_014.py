class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def display_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Прізвище: {self.surname}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.average_grade}")


student1 = Student("Олена", "Ковальчук", 20, 89.5)

print("Початкова інформація про студента:")
student1.display_info()

student1.update_average_grade(93.2)

print("\nОновлена інформація про студента:")
student1.display_info()
