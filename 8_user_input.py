# Use input() function to get input values from user
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")

print(f"Name is {name}")
print(type(name))
#Python, take inputs as string values and stote them as string values. So output values is also a string values. 
#So we have to convert the input values to it's data type.

name = input("Enter Your Name:")
age = int(input("Enter Your Age: "))
score = float(input("Enter your Score:"))

print(f"Your Name is {name}. Your age is {age}, and your score is {score}.")
print(type(name))
print(type(age))
print(type(score))