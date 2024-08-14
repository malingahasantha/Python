"""
Q9. Take user input and convert Celceus to Faranhight?
"""

user_input = input("Enter Celsius Degrees: ")
number = int(user_input)

def convert_celsius(number):
    fahrenheit = (number * 9/5) + 32
    return fahrenheit

celsius_to_fahrenheit = convert_celsius(number)
print(celsius_to_fahrenheit)