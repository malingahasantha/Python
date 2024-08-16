"""
Q17. input : 12345
The output should be: 1+2+3+4+5 = 15

Use:
1. List Comprehension
3. f.string

Additional Task
1. Take input from user
"""


#number = 12345
#str_number = str(number)
user_input = input('Please enter a number: ')
str_number = str(user_input)

addition = sum(int(digit) for digit in str_number)


print(f'Sum of the number is: ', addition)