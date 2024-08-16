"""
Q19. Armstrong number: 153
How?? Lenght of 153: 3
1^3 + 5^3 + 3^3 = 153

1634 = 1^4 + 6^4 + 3^4 + 4^4

Criteria:
1. Should be divisible by 4, and not by 100
2. Or, should be divisible by 400

Use:
1. Functions
2. User Input
3. f.string
"""

def is_armstrong(str_num):
    len_num = len(str_num)
    armstrong_num = sum(int(digit)**len_num for digit in str_num)
    return armstrong_num

user_input = input('Enter the number here: ')
str_num = str(user_input)

check_armstrong = is_armstrong(str_num)

if user_input == check_armstrong:
    print('This is an Armstrong Number')
else:
    print('This is not an Armstrong Number')


