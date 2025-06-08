# 3) What is the __init__() function in Python?

# __init__() is a special method in Python known as a constructor. It is automatically called when an object of a class is created.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student('Vipin', 212)
print(s1.name)
print(s1.age)
