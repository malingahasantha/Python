
# Private variables and methods

class myClass:
    x = 10   #public variable
    __y = 20 #private variable
    def disp(self):
        return self.__y

myObj = myClass()
print(myObj.x)

#we can't access to our private variable from the outside of the class. If we want to access it we can do it via a method.
myObj1 = myClass()
print(myObj1.disp())

print("\n")

#private methods

class myClass1:
    def meth1(self):
        print("Hello")
        self.__meth2()

    def __meth2(self):
        print("World")

myObject = myClass1()
myObject.meth1()

#but we can access our private methods through another private method. So when we access out public method, private method will also access via it.
