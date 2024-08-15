"""
Q12. Check if a string is a palindrome.

A string is a palindrome if the reverse of the string is same as the original string.
Example: racecar == racecar (reverse)

Prime number is only divisible by 1 and itself.
1 is not a prime number.

Use:
1. User Input
2. Function
3. f.string

"""

def is_palindrome(a_string):
    a_string = a_string.lower()
    r_string = a_string[::-1]
    if a_string == r_string:
        return True
    else:
        return False


user_input = input('Enter a String: ')
if is_palindrome(user_input):
    print(f'{user_input} is a Palindrome')
else:
    print(f'{user_input} is not a Palindrome')