name = "Garbs Studio"

print(name.upper())
#use upper method to convert varibale string to upper case

print(name.lower())
#use lower method to convert varibale string to lower case

print(name.title())
#use title method to convert first letter of the string to upper case. In here every first letter in sentence is capital.

print(name.capitalize())
#use capitalize method to convert first letter of the string to upper case. In here only first letter in sentence is capital.

## ----------------------------------------------------- ##

print(name.find('Studio'))
#index values regards to specific String we can use find and index methods.

print(name.find('z'))
#if we provide a string that does not include in the variable, it will return -1 as the output.

print(name.find('s' , 5 , 11))
#find value from index 5 to 11.

print(name.rfind('u'))
#in rfind method program check from right side. reverse order.

# --> print(name.index('z'))
#only different in index and find is if we provide a value not in the variable find method return -1 value and index return an error.

## ------------------------------------------------------- ##

print(name.center(20))
#center the variable in 20 length space.

print(name.ljust(20))
#justify to left side in 20 lenght space.

print(name.rjust(20))
#justify to right side in 20 lenght space.

print(name.center(20, "-"))
#fill the spaces with some characters

print(name.ljust(20, "-"))

## ----------------------------------------------------------- ##

name_1 = "         Hasantha           "

print(name_1)
print(name_1.strip())
#remove spaces

print(name_1.lstrip())
#remove left side spaces

print(name_1.rstrip())
#remove right side spaces

name_2 = "-------------------Hasantha----------------------"
print(name_2)
print(name_2.strip('-'))
#remove spaces

print(name_2.lstrip('-'))
#remove left side spaces

print(name_2.rstrip('-'))


