import math
# class Person:
#     def __init__(self):
#         print("Person __init__")
#
#     def greeting(self):
#         print('hello')
#
#
# class University:
#     def manage_credit(self):
#         print('학점관리')
#
#
# class Student(Person, University):
#     def study(self):
#         print('study')
#
# class PersonList:
#     def __init__(self):
#         self.person_list = []
#
#     def appendPerson(self, person):
#         self.person_list.append(person)
# st = Student()
# st.greeting()
# st.study()
# st.manage_credit()
# # print(issubclass(Student, Person))
# plist = PersonList()
# person1 = Person()
# person2 = Person()
# plist.appendPerson(person1)
# plist.appendPerson(person2)
# print(plist.person_list)
from numbers import Real


class AdvancedList(list):
    def replace(self, origin, target):
        self[:] = [target if i == origin else i for i in self]


x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)
a = p2.x - p1.x
b = p2.y - p1.y
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(c)


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_width(self):
        return abs(self.x2-self.x1)

    def get_height(self):
        return abs(self.y2-self.y1)

    def get_area(self):
        return abs(self.x2-self.x1) * abs(self.y2-self.y1)


rect1 = Rectangle(x1=20, y1=20, x2=40, y2=30)
rect2 = Rectangle(x1=40, y1=30, x2=20, y2=20)
area = rect1.get_area()
print(rect1.get_area(), rect2.get_area())