"""
Q7. Write a program for given requirement?
input: x3y2z1

output : xxxyyz
"""

input_value = 'x3y2z1'
prev = ''
output_value = ''

for i in input_value:
    if i.isalpha():
        output_value += i
        prev = i
    else:
        if i.isdigit():
            output_value += prev*(int(i)-1)
            # output_value = output_value + prev*(3-1) --> x + x*2 this is for first round
            # output_value = output_value + prev*(2-1) --> y + y*1

print(output_value)
