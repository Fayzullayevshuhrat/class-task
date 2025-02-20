from example import *
import json

t = Teacher("Azamjon", 24, "IT")
print(t.get_info())

s = Student("Shuhrat", 17, 999)
s1 = Student("Shaxzod", 18)
print(s.get_info())

sch = School("PDP")
print(sch.get_info())

c = Course("Python", t)
sch.add_course(c)

c.add_student(s)
c.add_student(s1)
print(c.get_info())

manage = Manage(sch)
manage.show_info()
manage.save_data("school_data.json")
manage.load_data("school_data.json")
