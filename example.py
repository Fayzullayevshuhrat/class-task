import json
from uuid import uuid4
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod
    def get_info(self):
        pass


class Student(Person):
    def __init__(self, name, age, student_id=None):
        super().__init__(name, age)
        self.student_id = student_id if student_id else str(uuid4())

    def get_info(self):
        return f"Student: {self._name}, Age: {self._age}, ID: {self.student_id}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_info(self):
        return f"Teacher: {self._name}, Age: {self._age}, Subject: {self.subject}"


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def get_info(self):
        return f"Course: {self.name}, Teacher: {self.teacher.get_info()}, Students: {len(self.students)}"

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(" Student qo‘shildi!")
        else:
            print("️ Student allaqachon ro‘yxatda.")


class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.courses = []
        self.students = []

    def get_info(self):
        return f"School: {self.name}, Teachers: {len(self.teachers)}, Courses: {len(self.courses)}, Students: {len(self.students)}"

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print("Student qo‘shildi!")
        else:
            print("Student allaqachon ro‘yxatda.")

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
            print("Teacher qo‘shildi!")
        else:
            print("Teacher allaqachon ro‘yxatda.")

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(" Kurs qo‘shildi!")
        else:
            print(" Kurs allaqachon mavjud.")



class Save:
    @staticmethod
    def save_to_file(filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f" {filename} saqlandi!")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Fayl topilmadi!")
            return None



class Manage:
    def __init__(self, school):
        self.school = school

    def show_info(self):
        print(self.school.get_info())



    def save_data(self, filename):
        data = self.school.get_info()
        Save.save_to_file(filename, data)

    def load_data(self, filename):
        data = Save.load_from_file(filename)
        if data:
            print("Ma'lumotlar yuklandi:", data)

school = School("PDP Academy")
manager = Manage(school)
while True:
    print("\n--- Maktab boshqaruv tizimi ---")
    print("1. Talaba qo'shish")
    print("2. O'qituvchi qo'shish")
    print("4. Maktab ma'lumotlarini ko'rish")
    print("5. Ma'lumotlarni saqlash")
    print("6. Ma'lumotlarni yuklash")
    print("7. Chiqish")

    choice = input("Tanlang (1-7): ")

    if choice == "1":
        name = input("Talabaning ismi: ")
        age = int(input("Yoshi: "))
        student = Student(name, age)
        school.add_student(student)

    elif choice == "2":
        name = input("O'qituvchining ismi: ")
        age = int(input("Yoshi: "))
        subject = input("Fan: ")
        teacher = Teacher(name, age, subject)
        school.add_teacher(teacher)


    elif choice == "4":
        manager.show_info()

    elif choice == "5":
        filename = input("Fayl nomini kiriting: ")
        manager.save_data(filename)

    elif choice == "6":
        filename = input("Fayl nomini kiriting: ")
        manager.load_data(filename)

    elif choice == "7":
        print("Dastur yakunlandi!")
        break

    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring!")



