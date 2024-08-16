"""
Q18. Take user input of the year : Example 2024
Print : 2024 is a / is not a leap year

Criteria:
1. Should be divisible by 4, and not by 100
2. Or, should be divisible by 400

Use:
1. Functions
2. User Input
3. f.string

Additional Task
1. Take input from user
"""




def check_leap_year(user_input):
    if (user_input % 4 == 0 and user_input % 100 != 0) or (user_input % 400 == 0):
        return True
    else:
        return False

user_input = input('Enter year here: ')
if check_leap_year(int(user_input)) is True:
    print(f'{user_input} is a leap year')
else:
    print(f'{user_input} is not a leap year')