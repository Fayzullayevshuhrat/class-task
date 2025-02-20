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
        self.student_id = student_id if student_id else str(uuid4())  # UUID ni stringga o'zgartirdik

    def get_info(self):
        return f"Student: {self._name}, Age: {self._age}, ID: {self.student_id}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_info(self):
        return f"Teacher: {self._name}, Age: {self._age}, Subject: {self.subject}"


class Course(ABC):
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    @abstractmethod
    def get_info(self):
        pass

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print("Student Qo'shildi")
        else:
            print("Student Qo'shilmadi")


class School(Course):
    def __init__(self, name):
        super().__init__(name,Teacher("Mr Azamjon", 24, "IT"))
        self.teachers = []
        self.courses = []

    def get_info(self):
        return f"School: {self.name}, Teacher: {self.teacher.get_info()}, Students: {len(self.students)}"

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print("Student qo'shildi")
        else:
            print("Student allaqachon ro'yxatda")


# s = Student("Shuhrat", 17)
# print(s.get_info())
#
# t = Teacher("Mr Azamjon", 24, "IT")
# print(t.get_info())
#
#
# teacher = Teacher("Alibek", 26, "Math")
# sch = School("PDP",)
# print(sch.get_info())
