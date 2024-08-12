"""
Q5. Write a program to given requirement?
separate alphabetical and integers
Input: Alex12345Leesa789 Output:AlexLeesa12345789
"""

input_str = 'Alex12345Leesa789'
digits = ''
str = ''

for i in input_str:
    if i.isalpha():
        str += i
    elif i.isdigit():
        digits += i

output_str = str + digits
print(output_str)

