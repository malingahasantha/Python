# Method Overriding
# Method Overloading
# Operator Overloading

# ----------------- Method Overriding ------------------ #

class Parent:
    x =  40

class Child(Parent):
    pass

myObj = Child()
print(myObj.x)

# This way we can access variable of Parent class via object created for Child class. We have inherited the Parent class to child class.

print("\n")

# Let's create variable call x in Child class and then assign a value to it and run again. You will see the variable was overrided.

class Parent:
    x =  40

class Child(Parent):
    x = 50

myObj = Child()
print(myObj.x)

print("\n")

# Now Let's override a function.

class Parent:
    def func(self):
        print("Hello")

class Child(Parent):
    def func(self):
        print("World")

myObj = Child()
print(myObj.func())

# If we use same name in the child function then the parent function will overrided.