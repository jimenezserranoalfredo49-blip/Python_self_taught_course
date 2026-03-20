# Class variables = variables shared among all instances of a class

# Defined outside the constructor
# You can share data among all objects created from a class

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 25)

print(student1.name)
print(student1.age)
print(Student.class_year)
print(Student.num_students)

