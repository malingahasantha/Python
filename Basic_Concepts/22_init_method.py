
class Student:
    name = "Kamal"
    age = 20

student1 = Student()
print(student1.name)

student2 = Student()
print(student2.name)

print("\n")

class Students:
    def __init__(self):
        print("Hello")

students1 = Students()
Students2 = Students()
#in here everytime we create an object this init method is run without calling it.
#speciality of the ini method is everytime we create an object this method runs automatically.

print("\n")

#we can create general structure to access via objects.
class Std:
    def __init__(self,name,age):
        self.x = name
        self.y = age

std1 = Std('kamal', 23)
std2 = Std('nmimal',34)

print(std1.x)
print(std1.y)
print(std2.x)
print(std2.y)
