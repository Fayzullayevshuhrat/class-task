import json
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self._name = name  # Encapsulation
        self._age = age

    @abstractmethod
    def get_info(self):
        return f"{self._name}, {self._age}"


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


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_info(self):
        return f"Course: {self.name}, Teacher: {self.teacher.get_info()}, Students: {len(self.students)}"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def get_data(self):
        return f"School: {self.name}, Students: {len(self.students)}, Teachers: {len(self.teachers)}, Courses: {len(self.courses)}"



class DataManager:
    @staticmethod
    def save_to_file(filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return None


# Example Usage
school = School("Elite High School")

student1 = Student("Alice", 15, "S001")
student2 = Student("Bob", 16, "S002")
teacher1 = Teacher("Mr. Smith", 40, "Mathematics")

course1 = Course("Algebra", teacher1)
course1.add_student(student1)
course1.add_student(student2)

school.add_student(student1)
school.add_student(student2)
school.add_teacher(teacher1)
school.add_course(course1)

# Save data to JSON
DataManager.save_to_file("school_data.json", school.get_data())
