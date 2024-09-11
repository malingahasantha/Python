# Filter Function

#let's filter even numbers from this list using filter function
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def even_number(x):
    return x % 2 == 0

y = list(filter(even_number,number)) #filter even numbers from numbers list and add them to a list and assigne that to y

print(y)

#we can do this easily with lambda function.
z = list(filter(lambda x: x%2==0,number)) 

print(z)

#-----------------------------------------------------------------------------------
print("\n")
# Map Function
#in map function we provide equation to the function and we get output of the provided list with that equation

y = list(map(lambda x : x*2, number))
print(y)

#-----------------------------------------------------------------------------------
print("\n")
# Reduce Function
#we can use reduce function to get multiplication or any other equation of our whole list in one number.

#reduce function in python is in module called functools, so we should import it before use this.

from functools import reduce

number = [1,2,3,4,5,6,7,8,9]

sum = reduce(lambda x,y : x+y , number)
print(sum)

mul = reduce(lambda x,y : x*y , number)
print(mul)

div = reduce(lambda x,y : x/y , number)
print(div)

