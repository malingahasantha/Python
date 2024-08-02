#lambda is not a function it is a keyword.

#let's calculate area of a square.

def area(x):
    return x*x

print(area(5))

#this was we can calculate are a of square.
#we can use lambda function to calculate this kind of simple quations. we cannot use lambda function to do high level quations.

#------------------------------------------------------------------------------------
print("\n")

area = lambda x : x*x

print(area(5))

#------------------------------------------------------------------------------------
print("\n")

#area of a rectangle

area = lambda x,y : x*y

print(area(5,7))

#-------------------------------------------------------------------------------------
print("\n")

#use lambda function inside a function

def apple(unit_price):
    return (lambda number_of_apple : number_of_apple*unit_price)

x = apple(40) #pass unitprice variable
print(x(10)) #pass number of apple variable

