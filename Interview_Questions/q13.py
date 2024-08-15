"""
Q13. Calculate the factorial of a given number.

Example: 4 factorial = 4*3*2*1. Factorial of 1 and 0 = 1.
7! = 7*6*5*4*3*2*1

Use:
1. User Input
2. Function
3. f.string

"""

def calculate_factorial(number):
    factorial = 1
    for item in range(1,number+1):
        factorial = factorial*item
    return factorial

user_input = input('Please enter a number: ')
number = int(user_input)


print(f'Factorial value of {number} is {calculate_factorial(number)}')
