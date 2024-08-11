"""
Q4. Write a program to remove the duplicates in string?
Input: Canada Output:cand
"""

input_str = str(input("Enter Your Input String: "))

output_str = ''

for i in input_str:
    if i not in output_str:
        output_str += i

print(output_str)