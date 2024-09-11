
class Phone1:
    def feature1(self):
        print('camera')

class Phone3:
    def feature3(seld):
        print('blutooth')

class Phone2(Phone1, Phone3): #<-- inherit Phone1 to Phone2
    def feature2(self):
        print('internet')

myObj = Phone2()
myObj.feature2()
myObj.feature1()
myObj.feature3()

# we can access methods in Phone1 class via object created for Phone2 class. To do that we should inherit the resources in Phone1 class to Phone2 class.

# Three types of inheritance
# Single level inheritance
# Multiple inheritance
# Multi level inheritance