
class Example: #class
    def say(self): #method
        print("Hello")

example1 = Example() #create object: To access a method inside a class we should create a object. example1 is a object we create to access method.
example1.say() #access the method.

print("\n --------------------------------------------------------------------------")

class Example:
    def say(self, name):
        print("Hello "+ name)

example1 = Example() 
example1.say("Python")

example2 = Example() 
example2.say("Shell")


print("\n --------------------------------------------------------------------------")

#try call a variable created in the method inside a class using a object
class Example:
    def say(self, name):
        self.x = name #to access this variable we need to coloborate it with self argument.
        print("Hello "+ name)

example3 = Example()
example3.say("Java")
print(example3.x)
example3.x = "Perl"
print(example3.x)