# Buy fruits from a shop and calculate total cost for the fruits we bought.

class Fruits:
    number_of_items = None
    unit_price = None

    def set_values(self,x,y):
        self.number_of_items = x
        self.unit_price = y

class Apple(Fruits):
    def price(self):
        print('For Apple: ', self.number_of_items*self.unit_price)

class Orange(Fruits):
    def price(self):
        print('For Orange ', self.number_of_items*self.unit_price)

class Grapes(Fruits):
    def price(self):
        print('For Grapes ', self.number_of_items*self.unit_price)

myObj1 = Apple()
myObj2 = Orange()
myObj3 = Grapes()

myObj1.set_values(12,40)
myObj2.set_values(8,30)
myObj3.set_values(40,3)

myObj1.price()
myObj2.price()
myObj3.price()