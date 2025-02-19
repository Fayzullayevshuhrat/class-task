import json

from abc import ABC, abstractmethod

from example import student1


class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod
    def get_info(self):
        pass



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

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
        return f"Course: {self.name}, Teacher: {self.teacher.get_info()}, Students: {len(self.students)}"

    def add_student(self, student):
        self.students.append(student)
        if student not in self.students:
            print("Student not added")
        else:
            print("Student added")




class School(Course):
    def __init__(self, name, teacher):
        super().__init__(name, teacher)
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []
    def get_info(self):

        return f"School: {self.name}, Students: {len(self.students)}"
    def add_student(self, student):
        self.students.append(student,)
        if student not in self.students:
            print("Student qo'shilmadi")
        else:
            print("Student qo'shildi")


# p= Student("Shuhrat",23,"999" )
# print(p.get_info())
# t = Teacher("Mr.Azamjon", 24, "IT")
# print(t.get_info())
# s = School("PDP school", t)
# print(s.get_info())
# s.add_student(p)
# s.add_student("Bobur")
#
# print(s.get_info())
#









